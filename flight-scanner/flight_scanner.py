#!/usr/bin/env python3
"""Flight scanner: find the cheapest SNA -> TPE fares inside a travel window.

By default it prices a one-way ticket for every departure day in the window.
With --round-trip it prices every departure/return combination instead. It
keeps the cheapest itinerary for each date (or date pair) and prints a ranked
list, a price grid (round trips) and a Google Flights link for each. Results
can be saved to CSV/JSON or written as an email report, and a price history
file shows how fares move between runs.

Price sources:
  serpapi    Google Flights through SerpApi (needs SERPAPI_KEY; most reliable)
  google     Google Flights scraped directly with the `fast-flights` package
             (no key needed, but Google can rate-limit or change its page)
  firecrawl  Results saved from the Firecrawl connector's Google Flights
             capability (flights-google-com / flights/search_flights), passed
             with --firecrawl-json. For Claude sessions that can't reach
             Google directly.
  links      No prices, just a search link for every date

Default trip: one way, departing any day Nov 25 - Dec 2, 2026, 1 adult,
economy, USD. Departure dates before today are skipped. Because of the date
line, SNA -> TPE flights land the next day (morning departures) or two days
later (late-night departures).

Examples:
  python flight_scanner.py                       # one way, each day in window
  python flight_scanner.py --max-stops 1 --max-price 600
  python flight_scanner.py --round-trip --min-nights 5
  python flight_scanner.py --source links        # links only, no lookups
  python flight_scanner.py --source firecrawl --firecrawl-json fares.json \\
      --email-dir email --previous last_email.txt
"""

from __future__ import annotations

import argparse
import csv
import html
import json
import os
import re
import sys
import time
from dataclasses import asdict, dataclass, field
from datetime import date, datetime, timedelta, timezone
from pathlib import Path
from typing import Callable, Iterable
from urllib.parse import urlencode

DEFAULT_ORIGIN = "SNA"
DEFAULT_DESTINATION = "TPE"
DEFAULT_START = "2026-11-25"
DEFAULT_END = "2026-12-02"
DEFAULT_TZ = "America/Los_Angeles"
NOTABLE_CHANGE = 25  # price moves at least this big get called out in emails

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


def parse_firecrawl(data) -> dict:
    """Read results saved from Firecrawl's Google Flights capability.

    `data` is what firecrawl_scrape returns for
    {"provider": "flights-google-com", "capability": "flights/search_flights"}:
    the whole tool result, its data.alexandria list, or one capability result.
    Returns {DatePair.key: {"itineraries": [...], "url": ..., "observed_at_ms": ...}}
    plus "_errors", a list of calls that failed.
    """
    if isinstance(data, dict) and isinstance(data.get("data"), dict) and "alexandria" in data["data"]:
        entries = data["data"]["alexandria"]
    elif isinstance(data, list):
        entries = data
    else:
        entries = [data]
    out: dict = {"_errors": []}
    for e in entries:
        r = e.get("data") if isinstance(e, dict) else None
        q = r.get("query") if isinstance(r, dict) else None
        if not isinstance(q, dict) or not q.get("departure_date"):
            err = e.get("error") if isinstance(e, dict) else None
            out["_errors"].append(json.dumps(err or e)[:200])
            continue
        key = q["departure_date"] + (f"_{q['return_date']}" if q.get("return_date") else "")
        its = []
        for f in r.get("flights") or []:
            segs = f.get("segments") or []
            price = (f.get("price") or {}).get("amount")
            if price is None or not segs:
                continue
            airlines: list[str] = []
            for g in segs:
                name = g.get("airline_name") or g.get("airline")
                if name and name not in airlines:
                    airlines.append(name)
            notes = []
            if f.get("cabin_matches_request") is False:
                notes.append("different cabin")
            if f.get("airport_change"):
                notes.append("airport change")
            its.append(
                Itinerary(
                    price=float(price),
                    airlines=airlines,
                    stops=int(f.get("stops", len(segs) - 1)),
                    duration_min=f.get("duration_minutes"),
                    depart_time=_fmt_local(segs[0].get("departure_local")),
                    arrive_time=_fmt_local(segs[-1].get("arrival_local")),
                    route="-".join([segs[0].get("origin", "?")] + [g.get("destination", "?") for g in segs]),
                    note=", ".join(notes),
                )
            )
        out[key] = {"itineraries": its, "url": r.get("search_url", ""), "observed_at_ms": r.get("observed_at_ms")}
    return out


def _fmt_local(value: str | None) -> str:
    """'2026-11-25T07:00:00' -> '2026-11-25 07:00'."""
    return (value or "").replace("T", " ")[:16]


def firecrawl_fetcher(parsed: dict) -> Callable[[DatePair, Settings], list[Itinerary]]:
    """A fetch function that answers from parse_firecrawl() output."""

    def fetch(pair: DatePair, s: Settings) -> list[Itinerary]:
        entry = parsed.get(pair.key)
        if entry is None:
            raise LookupError("no Firecrawl result for this date")
        its = entry["itineraries"]
        if s.max_stops is not None:
            its = [i for i in its if i.stops <= s.max_stops]
        return its

    return fetch


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
    return f"{m // 60}h {m % 60:02d}m"


def render_table(results: list[ScanResult], s: Settings, top: int | None = None) -> str:
    priced = sorted([r for r in results if r.best], key=lambda r: (r.best.price, r.pair.key))
    if top:
        priced = priced[:top]
    if not priced:
        return "No priced results."
    one_way = all(r.pair.ret is None for r in priced)
    head = ["#", "Depart"] + ([] if one_way else ["Return", "Nights"])
    rows = [tuple(head + ["Price", "Stops", "Duration", "Airlines", "Route"])]
    for i, r in enumerate(priced, 1):
        b = r.best
        row = [str(i), r.pair.depart.strftime("%a %b %d")]
        if not one_way:
            row += [
                r.pair.ret.strftime("%a %b %d") if r.pair.ret else "one way",
                str(r.pair.nights) if r.pair.nights is not None else "-",
            ]
        row += [
            money(b.price, s.currency),
            "nonstop" if b.stops == 0 else str(b.stops),
            fmt_duration(b.duration_min),
            ", ".join(b.airlines)[:32],
            b.route,
        ]
        rows.append(tuple(row))
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
# Email report
# --------------------------------------------------------------------------

FARES_HEADER = "FARES BY DATE"
_FARE_LINE = re.compile(
    r"^\s*(\d{4}-\d{2}-\d{2})(?:\s*->\s*(\d{4}-\d{2}-\d{2}))?:\s*(?:[^\d\s]*?([\d,]+(?:\.\d+)?)|no price)"
)


def day_label(d: date) -> str:
    return f"{d:%a %b} {d.day}"


def pair_label(pair: DatePair) -> str:
    return day_label(pair.depart) + (f" → {day_label(pair.ret)}" if pair.ret else "")


def clock(stamp: str, ref: date | None = None) -> str:
    """'2026-11-26 20:30' -> '8:30 PM' when on `ref`, else 'Thu Nov 26 8:30 PM'."""
    try:
        dt = datetime.strptime(stamp[:16], "%Y-%m-%d %H:%M")
    except ValueError:
        return stamp
    t = f"{dt.hour % 12 or 12}:{dt.minute:02d} {'AM' if dt.hour < 12 else 'PM'}"
    return t if ref and dt.date() == ref else f"{day_label(dt.date())} {t}"


def stops_text(it: Itinerary, via: bool = True) -> str:
    text = "nonstop" if it.stops == 0 else f"{it.stops} stop" + ("s" if it.stops > 1 else "")
    airports = it.route.split("-")[1:-1] if it.route else []
    return text + (f" ({', '.join(airports)})" if via and airports else "")


def flight_summary(it: Itinerary) -> str:
    parts = [", ".join(it.airlines) or "?", stops_text(it), fmt_duration(it.duration_min)]
    if it.note:
        parts.append(it.note)
    return " · ".join(parts)


def fares_block(results: list[ScanResult], s: Settings) -> str:
    """Plain price list that the next report reads back to show changes."""
    lines = [FARES_HEADER]
    for r in sorted(results, key=lambda r: r.pair.key):
        label = str(r.pair.depart) + (f" -> {r.pair.ret}" if r.pair.ret else "")
        if r.best:
            b = r.best
            lines.append(f"{label}: {money(b.price, s.currency)} ({', '.join(b.airlines)}, {stops_text(b, via=False)})")
        else:
            lines.append(f"{label}: no price")
    return "\n".join(lines)


def parse_fares_block(text: str) -> dict[str, float | None] | None:
    """Prices from a previous report's FARES BY DATE block, or None if it has none."""
    if FARES_HEADER not in text:
        return None
    out: dict[str, float | None] = {}
    for line in text.split(FARES_HEADER, 1)[1].splitlines():
        m = _FARE_LINE.match(line)
        if m:
            key = m.group(1) + (f"_{m.group(2)}" if m.group(2) else "")
            out[key] = float(m.group(3).replace(",", "")) if m.group(3) else None
    return out


def render_email(
    results: list[ScanResult],
    s: Settings,
    previous: dict[str, float | None] | None,
    checked_at: datetime,
    today: date,
    note: str | None = None,
    max_price: float | None = None,
) -> tuple[str, str, str]:
    """Subject, plain-text body and HTML body for a fare report email."""
    rows = sorted(results, key=lambda r: r.pair.key)
    priced = [r for r in rows if r.best]
    one_way = all(r.pair.ret is None for r in rows)
    title = f"{s.origin} to {s.destination} {'one-way' if one_way else 'round-trip'} fares"
    low = min((r.best.price for r in priced), default=None)
    best = next((r for r in priced if r.best.price == low), None)
    ties = [r for r in priced if r.best.price == low and r is not best]
    if best:
        subject = f"{title}, {day_label(today)}: from {money(low, s.currency)} on {pair_label(best.pair)}"
    else:
        subject = f"{title}, {day_label(today)}: no prices found"

    def change(r: ScanResult) -> float | None:
        if previous is None or not r.best or previous.get(r.pair.key) is None:
            return None
        return r.best.price - previous[r.pair.key]

    def change_text(r: ScanResult) -> str:
        d = change(r)
        if d is None:
            return "new" if r.best else ""
        if abs(d) < 1:
            return "no change"
        return f"{'▼' if d < 0 else '▲'} {money(abs(d), s.currency)}"

    if previous is None:
        changes = "" if note else "First report, nothing to compare yet."
    else:
        moves = [(r, change(r)) for r in priced]
        moves = sorted([(r, d) for r, d in moves if d is not None and abs(d) >= NOTABLE_CHANGE], key=lambda x: -abs(x[1]))
        if moves:
            changes = "Biggest moves since the last report: " + ", ".join(
                f"{pair_label(r.pair)} {'down' if d < 0 else 'up'} {money(abs(d), s.currency)}" for r, d in moves[:5]
            ) + "."
        else:
            changes = f"No fare moved by {money(NOTABLE_CHANGE, s.currency)} or more since the last report."
    extra = []
    if max_price is not None:
        n = sum(1 for r in priced if r.best.price <= max_price)
        extra.append(f"{n} {'departure date' if one_way else 'date pair'}{'' if n == 1 else 's'} "
                     f"at or below your {money(max_price, s.currency)} target.")
    hour = f"{checked_at.hour % 12 or 12}:{checked_at.minute:02d} {'AM' if checked_at.hour < 12 else 'PM'}"
    footer = (
        f"Google Flights prices checked {day_label(checked_at.date())} at {hour} {checked_at.tzname() or ''}".rstrip()
        + f" for {s.adults} adult{'s' if s.adults > 1 else ''} in {s.cabin.replace('-', ' ')}. Fares change often "
        "and may not include checked bags; confirm before booking. Flight times are local to each airport."
    )
    table_title = "Cheapest fare by " + ("departure date" if one_way else "date pair")

    # Plain text
    t = [f"{title}, {day_label(today)}", ""]
    if note:
        t += [note, ""]
    if best:
        b = best.best
        t += [
            f"Cheapest: {money(b.price, s.currency)} on {pair_label(best.pair)}",
            flight_summary(b),
            f"Departs {clock(b.depart_time)}, arrives {clock(b.arrive_time)}",
            f"Google Flights: {best.link}",
        ]
        if ties:
            t.append("Same price on: " + ", ".join(pair_label(r.pair) for r in ties))
    else:
        t.append("No prices found today.")
    t += ["", table_title]
    for r in rows:
        if r.best:
            ch = change_text(r) if previous is not None else ""
            t.append(
                f"{pair_label(r.pair)}: {money(r.best.price, s.currency)}" + (f" ({ch})" if ch else "")
                + f" - {flight_summary(r.best)}, {clock(r.best.depart_time, r.pair.depart)}"
                + f" -> {clock(r.best.arrive_time, r.pair.depart)}"
            )
            t.append(f"  {r.link}")
        else:
            t.append(f"{pair_label(r.pair)}: no price" + (f" ({r.error})" if r.error else ""))
    t.append("")
    for line in ([changes] if changes else []) + extra:
        t += [line, ""]
    t += [footer, "", fares_block(results, s), ""]
    text = "\n".join(t)

    # HTML
    e = html.escape
    muted = "color:#57606a;"
    cell = "padding:6px;border-bottom:1px solid #d8dee4;vertical-align:top;"
    link = "color:#0969da;"
    h = [
        '<div style="font-family:-apple-system,BlinkMacSystemFont,\'Segoe UI\',Roboto,Helvetica,Arial,sans-serif;'
        'color:#1f2328;max-width:680px;margin:0 auto;padding:4px;">',
        f'<p style="margin:0 0 8px;font-size:13px;{muted}">{e(title)} · {e(day_label(today))}</p>',
    ]
    if note:
        h.append(f'<p style="margin:0 0 12px;padding:8px 10px;background:#fff8c5;border-radius:6px;font-size:14px;">{e(note)}</p>')
    if best:
        b = best.best
        h += [
            '<div style="border:1px solid #d0d7de;border-radius:10px;padding:14px 16px;margin:0 0 18px;">',
            f'<div style="font-size:13px;{muted}">Cheapest fare</div>',
            f'<div style="font-size:28px;font-weight:700;margin:2px 0 4px;">{e(money(b.price, s.currency))} '
            f'<span style="font-size:17px;font-weight:600;">on {e(pair_label(best.pair))}</span></div>',
            f'<div style="font-size:14px;">{e(flight_summary(b))}</div>',
            f'<div style="font-size:14px;">Departs {e(clock(b.depart_time))}, arrives {e(clock(b.arrive_time))}</div>',
        ]
        if ties:
            h.append(f'<div style="font-size:13px;{muted}margin-top:4px;">Same price on '
                     f'{e(", ".join(pair_label(r.pair) for r in ties))}</div>')
        h += [
            f'<a href="{e(best.link)}" style="display:inline-block;margin-top:12px;padding:9px 14px;background:#0969da;'
            'color:#ffffff;border-radius:6px;text-decoration:none;font-weight:600;font-size:14px;">See it on Google Flights</a>',
            "</div>",
        ]
    else:
        h.append('<p style="font-size:15px;font-weight:600;">No prices found today.</p>')
    h.append(f'<h3 style="font-size:15px;margin:0 0 6px;">{e(table_title)}</h3>')
    h.append('<table style="border-collapse:collapse;width:100%;font-size:13px;line-height:1.35;">')
    heads = ["Date", "Price"] + (["Change"] if previous is not None else []) + ["Flight", "Departs → Arrives", ""]
    h.append("<tr>" + "".join(f'<th style="{cell}text-align:left;font-weight:600;{muted}">{e(x)}</th>' for x in heads) + "</tr>")
    for r in rows:
        if r.best:
            b = r.best
            tds = [e(pair_label(r.pair)), e(money(b.price, s.currency))]
            if previous is not None:
                d = change(r)
                color = "#1a7f37" if d is not None and d <= -1 else "#cf222e" if d is not None and d >= 1 else "#57606a"
                tds.append(f'<span style="color:{color};">{e(change_text(r) or "—")}</span>')
            tds += [
                e(flight_summary(b)),
                e(f"{clock(b.depart_time, r.pair.depart)} → {clock(b.arrive_time, r.pair.depart)}"),
                f'<a href="{e(r.link)}" style="{link}">View</a>',
            ]
        else:
            tds = [e(pair_label(r.pair)), "no price"] + (["—"] if previous is not None else [])
            tds += [e(r.error), "", f'<a href="{e(r.link)}" style="{link}">Search</a>']
        # Highlight the cheapest row(s), unless every date costs the same.
        highlight = r.best is not None and r.best.price == low and len(ties) + 1 < len(priced)
        style = "font-weight:700;background:#f6f8fa;" if highlight else ""
        h.append(f'<tr style="{style}">' + "".join(f'<td style="{cell}">{x}</td>' for x in tds) + "</tr>")
    h.append("</table>")
    for line in ([changes] if changes else []) + extra:
        h.append(f'<p style="font-size:14px;margin:14px 0 0;">{e(line)}</p>')
    h += [f'<p style="font-size:12px;{muted}margin:16px 0 0;">{e(footer)}</p>', "</div>"]
    return subject, text, "\n".join(h)


def _tz(name: str):
    try:
        from zoneinfo import ZoneInfo

        return ZoneInfo(name)
    except Exception:  # no time zone database available
        return timezone.utc


def _observed_at(parsed: dict | None, tz) -> datetime | None:
    if not parsed:
        return None
    stamps = [v.get("observed_at_ms") for k, v in parsed.items() if k != "_errors" and v.get("observed_at_ms")]
    return datetime.fromtimestamp(max(stamps) / 1000, tz) if stamps else None


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
    p.add_argument("--end", default=DEFAULT_END,
                   help="last day you can depart (one way) or fly home (round trip), YYYY-MM-DD")
    trip = p.add_mutually_exclusive_group()
    trip.add_argument("--one-way", dest="round_trip", action="store_false",
                      help="one-way fares for each departure day (the default)")
    trip.add_argument("--round-trip", dest="round_trip", action="store_true",
                      help="round trips: every departure/return pair in the window")
    p.set_defaults(round_trip=False)
    p.add_argument("--min-nights", type=int, default=1, help="round trip: shortest stay to consider")
    p.add_argument("--max-nights", type=int, default=None, help="round trip: longest stay to consider")
    p.add_argument("--adults", type=int, default=1)
    p.add_argument("--cabin", choices=CABINS, default="economy")
    p.add_argument("--currency", default="USD")
    p.add_argument("--max-stops", type=int, default=None, help="0 = nonstop only")
    p.add_argument("--max-price", type=float, default=None, help="flag fares at or below this")
    p.add_argument(
        "--source",
        choices=["auto", "serpapi", "google", "firecrawl", "links"],
        default="auto",
        help="auto = serpapi when SERPAPI_KEY is set, otherwise google; firecrawl reads --firecrawl-json",
    )
    p.add_argument("--firecrawl-json", type=Path, default=None,
                   help="saved result of Firecrawl's flights-google-com / flights/search_flights capability")
    p.add_argument("--email-dir", type=Path, default=None,
                   help="write an email report here: subject.txt, body.txt and body.html")
    p.add_argument("--previous", type=Path, default=None,
                   help="plain-text body of the previous email report, used to show price changes")
    p.add_argument("--note", default=None, help="extra line to show near the top of the email report")
    p.add_argument("--tz", default=DEFAULT_TZ, help="time zone for today's date and the checked-at time")
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
    tz = _tz(a.tz)
    today = datetime.now(tz).date()
    s = Settings(a.origin.upper(), a.destination.upper(), a.adults, a.cabin, a.currency.upper(), a.max_stops)
    source = a.source
    if source == "auto":
        source = "serpapi" if os.environ.get("SERPAPI_KEY") else "google"
    if source == "firecrawl" and not a.firecrawl_json:
        print("--source firecrawl needs --firecrawl-json FILE", file=sys.stderr)
        return 2
    one_way = not a.round_trip

    if start < today:
        print(f"Skipping departure dates before today ({today}).")
        start = today
    pairs = build_pairs(start, end, one_way, a.min_nights, a.max_nights) if start <= end else []
    if not pairs:
        print("No dates fit those settings (or the travel window has passed).", file=sys.stderr)
        return 2

    trip = "one way" if one_way else "round trip"
    print(f"{s.origin} -> {s.destination}  {trip}  {start:%b %d} - {end:%b %d, %Y}  "
          f"{s.adults} adult(s), {s.cabin}, {s.currency}"
          + (f", max {s.max_stops} stop(s)" if s.max_stops is not None else ""))
    print(f"Source: {source}   {'Departure dates' if one_way else 'Date combinations'}: {len(pairs)}\n")

    parsed = None
    fetch = None
    if source == "firecrawl":
        parsed = parse_firecrawl(json.loads(a.firecrawl_json.read_text()))
        fetch = firecrawl_fetcher(parsed)
    live = source not in ("links", "firecrawl")
    results = scan(pairs, s, source, fetch=fetch, delay=a.delay if live else 0, retries=2 if live else 0)
    if parsed:
        for r in results:
            url = (parsed.get(r.pair.key) or {}).get("url")
            if url:
                r.link = url
        for err in parsed["_errors"]:
            print(f"A Firecrawl call failed: {err}")

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

    if a.email_dir:
        previous = None
        note = a.note
        if a.previous:
            previous = parse_fares_block(a.previous.read_text())
            if previous is None and not note:
                note = "Couldn't find the price list in the previous report, so changes aren't shown."
        checked_at = _observed_at(parsed, tz) or datetime.now(tz)
        subject, text, html_body = render_email(results, s, previous, checked_at, today, note, a.max_price)
        a.email_dir.mkdir(parents=True, exist_ok=True)
        (a.email_dir / "subject.txt").write_text(subject + "\n")
        (a.email_dir / "body.txt").write_text(text)
        (a.email_dir / "body.html").write_text(html_body)
        print(f"\nEmail report written to {a.email_dir} (subject.txt, body.txt, body.html)")
        print(f"Subject: {subject}")

    return 0 if priced else 1


if __name__ == "__main__":
    sys.exit(main())
