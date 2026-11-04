#!/usr/bin/env python3
"""Flight scanner: find the cheapest SNA -> TPE fares inside a travel window.

It scans every departure/return date combination in the window, keeps the
cheapest itinerary for each pair, and prints a ranked list, a price grid and
a Google Flights link for each pair. Results can be saved to CSV/JSON, and a
price history file shows how fares move between runs.

Price sources:
  serpapi  Google Flights through SerpApi (needs SERPAPI_KEY; most reliable)
  google   Google Flights scraped directly with the `fast-flights` package
           (no key needed, but Google can rate-limit or change its page)
  links    No prices, just a search link for every date pair

Default trip: Nov 25 - Dec 2, 2026, round trip, 1 adult, economy, USD.
All dates are the dates you DEPART (SNA -> TPE flights usually land in Taipei
two calendar days later because of the date line).

Examples:
  python flight_scanner.py                       # round trip, every date pair
  python flight_scanner.py --min-nights 5        # stays of 5+ nights only
  python flight_scanner.py --one-way             # one-way, each day in window
  python flight_scanner.py --max-stops 1 --max-price 900
  python flight_scanner.py --source links        # links only, no lookups
"""

from __future__ import annotations

import argparse
import csv
import json
import os
import sys
import time
from dataclasses import asdict, dataclass, field
from datetime import date, datetime, timedelta
from pathlib import Path
from typing import Callable, Iterable
from urllib.parse import urlencode

DEFAULT_ORIGIN = "SNA"
DEFAULT_DESTINATION = "TPE"
DEFAULT_START = "2026-11-25"
DEFAULT_END = "2026-12-02"

CABINS = ("economy", "premium-economy", "business", "first")
SERPAPI_CABIN = {"economy": 1, "premium-economy": 2, "business": 3, "first": 4}
HERE = Path(__file__).resolve().parent


# --------------------------------------------------------------------------
# Data model
# --------------------------------------------------------------------------


@dataclass(frozen=True)
class DatePair:
    depart: date
    ret: date | None  # None for one-way

    @property
    def nights(self) -> int | None:
        return (self.ret - self.depart).days if self.ret else None

    @property
    def key(self) -> str:
        return f"{self.depart}" + (f"_{self.ret}" if self.ret else "")


@dataclass
class Itinerary:
    price: float
    airlines: list[str]
    stops: int
    duration_min: int | None = None
    depart_time: str = ""
    arrive_time: str = ""
    route: str = ""  # e.g. SNA-SFO-TPE
    note: str = ""


@dataclass
class ScanResult:
    pair: DatePair
    link: str
    best: Itinerary | None = None
    options: int = 0
    error: str = ""
    extra: dict = field(default_factory=dict)


@dataclass
class Settings:
    origin: str
    destination: str
    adults: int
    cabin: str
    currency: str
    max_stops: int | None


# --------------------------------------------------------------------------
# Date combinations
# --------------------------------------------------------------------------


def daterange(start: date, end: date) -> Iterable[date]:
    d = start
    while d <= end:
        yield d
        d += timedelta(days=1)


def build_pairs(
    start: date,
    end: date,
    one_way: bool = False,
    min_nights: int = 1,
    max_nights: int | None = None,
) -> list[DatePair]:
    """Every (depart, return) inside [start, end] that fits the stay length."""
    if end < start:
        raise ValueError("end date is before start date")
    if one_way:
        return [DatePair(d, None) for d in daterange(start, end)]
    pairs = []
    for dep in daterange(start, end):
        for ret in daterange(dep + timedelta(days=max(min_nights, 0)), end):
            n = (ret - dep).days
            if max_nights is not None and n > max_nights:
                break
            pairs.append(DatePair(dep, ret))
    return pairs


# --------------------------------------------------------------------------
# Links
# --------------------------------------------------------------------------


def google_flights_link(pair: DatePair, s: Settings) -> str:
    """Exact Google Flights search URL (uses fast-flights' encoder if present)."""
    try:
        q = _fast_flights_query(pair, s)
        return q.url()
    except Exception:
        text = f"Flights from {s.origin} to {s.destination} on {pair.depart}"
        if pair.ret:
            text += f" returning {pair.ret}"
        else:
            text += " one way"
        if s.cabin != "economy":
            text += f" {s.cabin.replace('-', ' ')}"
        return "https://www.google.com/travel/flights?" + urlencode(
            {"q": text, "hl": "en", "curr": s.currency}
        )


def kayak_link(pair: DatePair, s: Settings) -> str:
    path = f"{s.origin}-{s.destination}/{pair.depart}"
    if pair.ret:
        path += f"/{pair.ret}"
    cabin = {"economy": "", "premium-economy": "/premium", "business": "/business", "first": "/first"}[s.cabin]
    return f"https://www.kayak.com/flights/{path}{cabin}/{s.adults}adults?sort=price_a"


# --------------------------------------------------------------------------
# Price sources
# --------------------------------------------------------------------------


def _fast_flights_query(pair: DatePair, s: Settings):
    from fast_flights import FlightQuery, Passengers, create_query

    legs = [FlightQuery(date=str(pair.depart), from_airport=s.origin, to_airport=s.destination)]
    if pair.ret:
        legs.append(FlightQuery(date=str(pair.ret), from_airport=s.destination, to_airport=s.origin))
    return create_query(
        flights=legs,
        trip="round-trip" if pair.ret else "one-way",
        seat=s.cabin,
        passengers=Passengers(adults=s.adults),
        language="en",
        currency=s.currency,
        max_stops=s.max_stops,
    )


def fetch_google(pair: DatePair, s: Settings) -> list[Itinerary]:
    """Scrape Google Flights via fast-flights (no API key)."""
    try:
        from fast_flights import FlightsNotFound, get_flights
    except ImportError as e:  # pragma: no cover - depends on environment
        raise RuntimeError(
            "the 'google' source needs fast-flights: pip install -r requirements.txt"
        ) from e

    try:
        results = get_flights(_fast_flights_query(pair, s))
    except FlightsNotFound:
        return []
    out = []
    for f in results:
        segs = list(getattr(f, "flights", []) or [])
        price = getattr(f, "price", None)
        if not price:
            continue
        stops = max(len(segs) - 1, 0)
        if s.max_stops is not None and stops > s.max_stops:
            continue
        route = "-".join([segs[0].from_airport.code] + [g.to_airport.code for g in segs]) if segs else ""
        out.append(
            Itinerary(
                price=float(price),
                airlines=list(getattr(f, "airlines", []) or []),
                stops=stops,
                # fast-flights gives per-segment times only, so this is air
                # time without layovers.
                duration_min=sum(g.duration for g in segs) if segs else None,
                depart_time=_fmt_simple_dt(segs[0].departure) if segs else "",
                arrive_time=_fmt_simple_dt(segs[-1].arrival) if segs else "",
                route=route,
                note="air time only",
            )
        )
    return out


def _fmt_simple_dt(sdt) -> str:
    try:
        y, m, d = sdt.date
        hh, mm = sdt.time
        return f"{y:04d}-{m:02d}-{d:02d} {hh:02d}:{mm:02d}"
    except Exception:
        return ""


def fetch_serpapi(pair: DatePair, s: Settings, api_key: str | None = None) -> list[Itinerary]:
    """Google Flights results from SerpApi (https://serpapi.com/google-flights-api)."""
    import requests

    key = api_key or os.environ.get("SERPAPI_KEY")
    if not key:
        raise RuntimeError("SERPAPI_KEY is not set")
    params = {
        "engine": "google_flights",
        "departure_id": s.origin,
        "arrival_id": s.destination,
        "outbound_date": str(pair.depart),
        "type": 1 if pair.ret else 2,
        "currency": s.currency,
        "hl": "en",
        "gl": "us",
        "adults": s.adults,
        "travel_class": SERPAPI_CABIN[s.cabin],
        "api_key": key,
    }
    if pair.ret:
        params["return_date"] = str(pair.ret)
    if s.max_stops is not None:
        # SerpApi: 1 = nonstop, 2 = 1 stop or fewer, 3 = 2 stops or fewer
        params["stops"] = min(s.max_stops + 1, 3)
    r = requests.get("https://serpapi.com/search.json", params=params, timeout=60)
    data = r.json()
    if "error" in data:
        if "returned any results" in data["error"]:
            return []
        raise RuntimeError(data["error"])
    return parse_serpapi(data)


def parse_serpapi(data: dict) -> list[Itinerary]:
    out = []
    for group in ("best_flights", "other_flights"):
        for opt in data.get(group, []) or []:
            if opt.get("price") is None:
                continue
            segs = opt.get("flights", []) or []
            airlines = []
            for g in segs:
                a = g.get("airline")
                if a and a not in airlines:
                    airlines.append(a)
            route = ""
            if segs:
                route = "-".join(
                    [segs[0]["departure_airport"]["id"]] + [g["arrival_airport"]["id"] for g in segs]
                )
            out.append(
                Itinerary(
                    price=float(opt["price"]),
                    airlines=airlines,
                    stops=max(len(segs) - 1, 0),
                    duration_min=opt.get("total_duration"),
                    depart_time=segs[0]["departure_airport"].get("time", "") if segs else "",
                    arrive_time=segs[-1]["arrival_airport"].get("time", "") if segs else "",
                    route=route,
                )
            )
    return out


SOURCES: dict[str, Callable[[DatePair, Settings], list[Itinerary]]] = {
    "serpapi": fetch_serpapi,
    "google": fetch_google,
}


# --------------------------------------------------------------------------
# Scan
# --------------------------------------------------------------------------


def scan(
    pairs: list[DatePair],
    s: Settings,
    source: str,
    fetch: Callable[[DatePair, Settings], list[Itinerary]] | None = None,
    delay: float = 2.0,
    retries: int = 2,
    log=print,
) -> list[ScanResult]:
    results = []
    fetch = fetch or SOURCES.get(source)
    for i, pair in enumerate(pairs, 1):
        res = ScanResult(pair=pair, link=google_flights_link(pair, s))
        if source != "links":
            label = f"{pair.depart}" + (f" -> {pair.ret}" if pair.ret else " (one way)")
            log(f"  [{i}/{len(pairs)}] {label} ...", end="", flush=True)
            for attempt in range(retries + 1):
                try:
                    options = fetch(pair, s)
                    res.options = len(options)
                    res.best = min(options, key=lambda it: it.price) if options else None
                    res.error = ""
                    break
                except Exception as e:  # keep scanning other dates
                    res.error = f"{type(e).__name__}: {e}"[:200]
                    if attempt < retries:
                        time.sleep(delay * (attempt + 2))
            if res.best:
                log(f" {money(res.best.price, s.currency)}")
            else:
                log(f" {'error: ' + res.error if res.error else 'no flights'}")
            if i < len(pairs) and delay:
                time.sleep(delay)
        results.append(res)
    return results


# --------------------------------------------------------------------------
# Output
# --------------------------------------------------------------------------


def money(v: float | None, cur: str = "USD") -> str:
    if v is None:
        return "-"
    sym = {"USD": "$", "TWD": "NT$", "EUR": "€", "GBP": "£", "JPY": "¥"}.get(cur, cur + " ")
    return f"{sym}{v:,.0f}"


def fmt_duration(m: int | None) -> str:
    if not m:
        return "-"
    return f"{m // 60}h{m % 60:02d}m"


def render_table(results: list[ScanResult], s: Settings, top: int | None = None) -> str:
    priced = sorted([r for r in results if r.best], key=lambda r: r.best.price)
    if top:
        priced = priced[:top]
    if not priced:
        return "No priced results."
    rows = [("#", "Depart", "Return", "Nights", "Price", "Stops", "Duration", "Airlines", "Route")]
    for i, r in enumerate(priced, 1):
        b = r.best
        rows.append(
            (
                str(i),
                r.pair.depart.strftime("%a %b %d"),
                r.pair.ret.strftime("%a %b %d") if r.pair.ret else "one way",
                str(r.pair.nights) if r.pair.nights is not None else "-",
                money(b.price, s.currency),
                "nonstop" if b.stops == 0 else str(b.stops),
                fmt_duration(b.duration_min),
                ", ".join(b.airlines)[:32],
                b.route,
            )
        )
    widths = [max(len(row[c]) for row in rows) for c in range(len(rows[0]))]
    lines = []
    for j, row in enumerate(rows):
        lines.append("  ".join(cell.ljust(widths[c]) for c, cell in enumerate(row)).rstrip())
        if j == 0:
            lines.append("  ".join("-" * w for w in widths))
    return "\n".join(lines)


def render_grid(results: list[ScanResult], s: Settings) -> str:
    """Departure (rows) x return (columns) price grid; cheapest cell starred."""
    rt = [r for r in results if r.pair.ret]
    if not rt:
        return ""
    deps = sorted({r.pair.depart for r in rt})
    rets = sorted({r.pair.ret for r in rt})
    cell = {(r.pair.depart, r.pair.ret): r for r in rt}
    prices = [r.best.price for r in rt if r.best]
    low = min(prices) if prices else None
    w = 9
    head = "Depart \\ Return".ljust(16) + "".join(d.strftime("%b %d").rjust(w) for d in rets)
    lines = [head]
    for d in deps:
        line = d.strftime("%a %b %d").ljust(16)
        for rd in rets:
            r = cell.get((d, rd))
            if r is None:
                txt = ""
            elif r.best:
                txt = money(r.best.price, s.currency) + ("*" if r.best.price == low else "")
            elif r.error:
                txt = "err"
            else:
                txt = "none"
            line += txt.rjust(w)
        lines.append(line)
    if low is not None:
        lines.append("* = cheapest")
    return "\n".join(lines)


def render_links(results: list[ScanResult], s: Settings) -> str:
    out = []
    for r in results:
        label = f"{r.pair.depart}" + (f" -> {r.pair.ret}" if r.pair.ret else " (one way)")
        price = f"  {money(r.best.price, s.currency)}" if r.best else ""
        out.append(f"{label}{price}\n    Google: {r.link}\n    Kayak:  {kayak_link(r.pair, s)}")
    return "\n".join(out)


def write_csv(results: list[ScanResult], path: Path, s: Settings) -> None:
    with path.open("w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["depart", "return", "nights", "price", "currency", "stops", "duration_min",
                    "airlines", "route", "depart_time", "arrive_time", "options", "error", "google_flights_url"])
        for r in sorted(results, key=lambda r: (r.best is None, r.best.price if r.best else 0)):
            b = r.best
            w.writerow([
                r.pair.depart, r.pair.ret or "", r.pair.nights if r.pair.nights is not None else "",
                b.price if b else "", s.currency, b.stops if b else "", b.duration_min if b else "",
                "; ".join(b.airlines) if b else "", b.route if b else "",
                b.depart_time if b else "", b.arrive_time if b else "", r.options, r.error, r.link,
            ])


def results_to_json(results: list[ScanResult], s: Settings, source: str) -> dict:
    return {
        "scanned_at": datetime.now().isoformat(timespec="seconds"),
        "source": source,
        "settings": asdict(s),
        "results": [
            {
                "depart": str(r.pair.depart),
                "return": str(r.pair.ret) if r.pair.ret else None,
                "nights": r.pair.nights,
                "best": asdict(r.best) if r.best else None,
                "options": r.options,
                "error": r.error,
                "google_flights_url": r.link,
            }
            for r in results
        ],
    }


# --------------------------------------------------------------------------
# Price history (compare with previous runs)
# --------------------------------------------------------------------------


def update_history(results: list[ScanResult], path: Path, s: Settings) -> list[str]:
    """Append this run's prices to a JSON history file; return change notes."""
    try:
        history = json.loads(path.read_text())
    except (FileNotFoundError, json.JSONDecodeError):
        history = {}
    route = f"{s.origin}-{s.destination}-{s.cabin}-{s.adults}-{s.currency}"
    book = history.setdefault(route, {})
    stamp = datetime.now().isoformat(timespec="minutes")
    notes = []
    for r in results:
        if not r.best:
            continue
        series = book.setdefault(r.pair.key, [])
        if series:
            prev = series[-1]["price"]
            diff = r.best.price - prev
            if abs(diff) >= 1:
                arrow = "down" if diff < 0 else "up"
                notes.append(
                    f"{r.pair.key.replace('_', ' -> ')}: {arrow} {money(abs(diff), s.currency)} "
                    f"({money(prev, s.currency)} -> {money(r.best.price, s.currency)})"
                )
        series.append({"at": stamp, "price": r.best.price})
    path.write_text(json.dumps(history, indent=2))
    return notes


# --------------------------------------------------------------------------
# CLI
# --------------------------------------------------------------------------


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    p = argparse.ArgumentParser(
        description="Scan every date combination in a travel window for the cheapest fare.",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    p.add_argument("--origin", default=DEFAULT_ORIGIN, help="origin airport code")
    p.add_argument("--destination", default=DEFAULT_DESTINATION, help="destination airport code")
    p.add_argument("--start", default=DEFAULT_START, help="first day you can depart (YYYY-MM-DD)")
    p.add_argument("--end", default=DEFAULT_END, help="last day you can fly home (YYYY-MM-DD)")
    p.add_argument("--one-way", action="store_true", help="one-way fares for each day in the window")
    p.add_argument("--min-nights", type=int, default=1, help="shortest stay to consider")
    p.add_argument("--max-nights", type=int, default=None, help="longest stay to consider")
    p.add_argument("--adults", type=int, default=1)
    p.add_argument("--cabin", choices=CABINS, default="economy")
    p.add_argument("--currency", default="USD")
    p.add_argument("--max-stops", type=int, default=None, help="0 = nonstop only")
    p.add_argument("--max-price", type=float, default=None, help="flag fares at or below this")
    p.add_argument(
        "--source",
        choices=["auto", "serpapi", "google", "links"],
        default="auto",
        help="auto = serpapi when SERPAPI_KEY is set, otherwise google",
    )
    p.add_argument("--delay", type=float, default=2.0, help="seconds between lookups")
    p.add_argument("--top", type=int, default=15, help="rows to show in the ranked table")
    p.add_argument("--csv", type=Path, default=None, help="write all results to this CSV")
    p.add_argument("--json", type=Path, default=None, help="write all results to this JSON")
    p.add_argument("--history", type=Path, default=HERE / "price_history.json",
                   help="price history file used to report changes between runs")
    p.add_argument("--no-history", action="store_true", help="don't read or write price history")
    p.add_argument("--links", action="store_true", help="also print booking links for every pair")
    return p.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    a = parse_args(argv)
    start = date.fromisoformat(a.start)
    end = date.fromisoformat(a.end)
    s = Settings(a.origin.upper(), a.destination.upper(), a.adults, a.cabin, a.currency.upper(), a.max_stops)
    source = a.source
    if source == "auto":
        source = "serpapi" if os.environ.get("SERPAPI_KEY") else "google"

    pairs = build_pairs(start, end, a.one_way, a.min_nights, a.max_nights)
    if not pairs:
        print("No date combinations fit those settings.", file=sys.stderr)
        return 2

    trip = "one way" if a.one_way else "round trip"
    print(f"{s.origin} -> {s.destination}  {trip}  {start:%b %d} - {end:%b %d, %Y}  "
          f"{s.adults} adult(s), {s.cabin}, {s.currency}"
          + (f", max {s.max_stops} stop(s)" if s.max_stops is not None else ""))
    print(f"Source: {source}   Date combinations: {len(pairs)}\n")

    results = scan(pairs, s, source, delay=a.delay if source != "links" else 0)

    if source == "links":
        print(render_links(results, s))
        return 0

    print("\nCheapest options")
    print(render_table(results, s, a.top))
    grid = render_grid(results, s)
    if grid:
        print("\nPrice grid")
        print(grid)

    priced = sorted([r for r in results if r.best], key=lambda r: r.best.price)
    if priced:
        b = priced[0]
        print(f"\nBest: {b.pair.depart:%a %b %d}"
              + (f" -> {b.pair.ret:%a %b %d}" if b.pair.ret else "")
              + f" for {money(b.best.price, s.currency)} ({', '.join(b.best.airlines)})")
        print(f"Book/verify: {b.link}")

    if a.max_price is not None:
        deals = [r for r in priced if r.best.price <= a.max_price]
        print(f"\nFares at or below {money(a.max_price, s.currency)}: {len(deals)}")
        for r in deals:
            print(f"  DEAL  {r.pair.key.replace('_', ' -> ')}  {money(r.best.price, s.currency)}  {r.link}")

    errors = [r for r in results if r.error]
    if errors:
        print(f"\n{len(errors)} lookup(s) failed, e.g. {errors[0].error}")
        if source == "google":
            print("Tip: Google may be rate-limiting you. Try --delay 5, or set SERPAPI_KEY.")

    if not a.no_history and priced:
        notes = update_history(results, a.history, s)
        if notes:
            print("\nChanges since last run")
            for n in notes:
                print("  " + n)

    if a.csv:
        write_csv(results, a.csv, s)
        print(f"\nSaved CSV: {a.csv}")
    if a.json:
        a.json.write_text(json.dumps(results_to_json(results, s, source), indent=2))
        print(f"Saved JSON: {a.json}")
    if a.links:
        print("\nLinks")
        print(render_links(results, s))

    return 0 if priced else 1


if __name__ == "__main__":
    sys.exit(main())
