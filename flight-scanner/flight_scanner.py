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
    itineraries: list[Itinerary] = field(default_factory=list)  # every option found


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


def parse_google_html(html: str) -> list:
    """Parse every flight on a Google Flights results page.

    Google puts results in two blocks of the page's data: "Top flights"
    (payload[2]) and "Other flights" (payload[3]). fast-flights 3.1.0 only
    reads payload[3], which drops the Top flights block, and that block
    usually holds the cheapest fares. So run fast-flights' parser once per
    block and merge the results, dropping repeats.
    """
    from fast_flights import FlightsNotFound
    from fast_flights.parser import parse_js
    from selectolax.lexbor import LexborHTMLParser

    script = LexborHTMLParser(html).css_first(r"script.ds\:1")
    if script is None:
        raise FlightsNotFound("no flight data on the Google Flights page")
    js = script.text()
    data = js.split("data:", 1)[1].rsplit(",", 1)[0]
    if data.endswith("errorHasStatus: true"):
        raise FlightsNotFound("no flights found; received error")
    payload = json.loads(data)

    flights, seen = [], set()
    for block in (2, 3):
        if len(payload) <= block or not payload[block] or not payload[block][0]:
            continue
        # parse_js reads flights from payload[3], so point it at this block.
        view = list(payload)
        view[3] = payload[block]
        for f in parse_js("data:" + json.dumps(view) + ",0"):
            key = (
                f.price,
                tuple(
                    (g.from_airport.code, g.to_airport.code, g.departure.date, g.departure.time)
                    for g in f.flights
                ),
            )
            if key not in seen:
                seen.add(key)
                flights.append(f)
    return flights


def fetch_google(pair: DatePair, s: Settings) -> list[Itinerary]:
    """Scrape Google Flights via fast-flights (no API key)."""
    try:
        from fast_flights import FlightsNotFound
        from fast_flights.fetcher import fetch_flights_html
    except ImportError as e:  # pragma: no cover - depends on environment
        raise RuntimeError(
            "the 'google' source needs fast-flights: pip install -r requirements.txt"
        ) from e

    try:
        results = parse_google_html(fetch_flights_html(_fast_flights_query(pair, s)))
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
            its.append(
                Itinerary(
                    price=float(price),
                    airlines=airlines,
                    stops=int(f.get("stops", len(segs) - 1)),
                    duration_min=f.get("duration_minutes"),
                    depart_time=_fmt_local(segs[0].get("departure_local")),
                    arrive_time=_fmt_local(segs[-1].get("arrival_local")),
                    route="-".join([segs[0].get("origin", "?")] + [g.get("destination", "?") for g in segs]),
                    note=_firecrawl_note(f.get("cabin_matches_request"), f.get("airport_change")),
                )
            )
        out[key] = {"itineraries": its, "url": r.get("search_url", ""), "observed_at_ms": r.get("observed_at_ms")}
    return out


def parse_firecrawl_listing(text: str) -> dict:
    """Read the compact one-way listing made from a Firecrawl search_flights result.

    Firecrawl keeps large results on its own side; running the jq projection in
    SKILL.md in that workspace turns one into a line per date and per flight:
      D|date|observed_at_ms|search_url
      F|date|price|stops|minutes|cabin_matches_request|airport_change|airline,...|SNA-SEA-TPE|departure_local|arrival_local
      E|error            (a date whose lookup failed)
    The F line names one airline per leg. Returns the same shape as parse_firecrawl().
    """
    out: dict = {"_errors": []}

    def entry(day: str) -> dict:
        return out.setdefault(day, {"itineraries": [], "url": "", "observed_at_ms": None})

    for line in text.splitlines():
        kind, _, rest = line.strip().partition("|")
        if kind == "D":
            day, ms, url = (rest.split("|", 2) + ["", ""])[:3]
            e = entry(day)
            e["url"], e["observed_at_ms"] = url, int(ms) if ms.isdigit() else None
        elif kind == "F":
            p = rest.split("|")
            if len(p) != 10:
                raise ValueError(f"listing line has {len(p) + 1} fields, expected 11: {line[:120]}")
            day, price, stops, minutes, cabin, change, names, route, dep, arr = p
            if price in ("", "null"):
                continue
            entry(day)["itineraries"].append(
                Itinerary(
                    price=float(price),
                    airlines=list(dict.fromkeys(n for n in names.split(",") if n not in ("", "null"))),
                    stops=int(stops) if stops.isdigit() else max(route.count("-") - 1, 0),
                    duration_min=int(minutes) if minutes.isdigit() else None,
                    depart_time=_fmt_local(None if dep == "null" else dep),
                    arrive_time=_fmt_local(None if arr == "null" else arr),
                    route=route,
                    note=_firecrawl_note({"true": True, "false": False}.get(cabin), change == "true"),
                )
            )
        elif kind == "E":
            out["_errors"].append(rest[:200])
    return out


def _firecrawl_note(cabin_matches_request, airport_change) -> str:
    notes = []
    if cabin_matches_request is False:
        notes.append("different cabin")
    if airport_change:
        notes.append("airport change")
    return ", ".join(notes)


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
                    res.itineraries = list(options)
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
    return _text_table(rows)


def _text_table(rows: list[tuple[str, ...]]) -> str:
    """Left-aligned columns with a dashed line under the header row."""
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


def _day_offset(it: Itinerary) -> int:
    """Calendar days between departure and arrival, in local dates."""
    try:
        return (date.fromisoformat(it.arrive_time[:10]) - date.fromisoformat(it.depart_time[:10])).days
    except ValueError:
        return 0


def shortest_flights(results: list[ScanResult], n: int = 6) -> list[dict]:
    """The n fastest distinct flights across all dates, with each date's price.

    The same airlines, route and departure/arrival times on several dates count
    as one flight, so the list shows n different flights instead of one fast
    flight repeated for every day. Each entry is {"itinerary", "offset",
    "prices"}, where prices is [(ScanResult, price), ...], cheapest first.
    """
    groups: dict[tuple, dict] = {}
    for r in results:
        for it in r.itineraries:
            if not it.duration_min:
                continue
            offset = _day_offset(it)
            key = (tuple(it.airlines), it.route, it.depart_time[11:16], it.arrive_time[11:16],
                   offset, it.duration_min, it.note)
            g = groups.setdefault(key, {"itinerary": it, "offset": offset, "prices": {}})
            prev = g["prices"].get(r.pair.key)
            if prev is None or it.price < prev[1]:  # Google can list a flight twice
                g["prices"][r.pair.key] = (r, it.price)
    flights = []
    for g in groups.values():
        prices = sorted(g["prices"].values(), key=lambda x: (x[1], x[0].pair.key))
        flights.append({"itinerary": g["itinerary"], "offset": g["offset"], "prices": prices})
    flights.sort(key=lambda g: (g["itinerary"].duration_min, g["prices"][0][1]))
    return flights[:n] if n > 0 else []


def render_shortest(results: list[ScanResult], s: Settings, n: int = 6) -> str:
    flights = shortest_flights(results, n)
    if not flights:
        return ""
    rows = [("Duration", "Flight", "Departs -> Arrives", "Prices by date (cheapest first)")]
    for g in flights:
        it = g["itinerary"]
        rows.append((
            fmt_duration(it.duration_min),
            flight_summary(it, duration=False),
            flight_times(it, g["offset"], "->"),
            ", ".join(f"{pair_label(r.pair)} {money(p, s.currency)}" for r, p in g["prices"]),
        ))
    return _text_table(rows)


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


def hour_min(stamp: str) -> str:
    """'2026-11-27 19:56' -> '7:56 PM'."""
    try:
        dt = datetime.strptime(stamp[:16], "%Y-%m-%d %H:%M")
    except ValueError:
        return stamp
    return f"{dt.hour % 12 or 12}:{dt.minute:02d} {'AM' if dt.hour < 12 else 'PM'}"


def clock(stamp: str, ref: date | None = None) -> str:
    """'2026-11-26 20:30' -> '8:30 PM' when on `ref`, else 'Thu Nov 26 8:30 PM'."""
    try:
        day = date.fromisoformat(stamp[:10])
    except ValueError:
        return stamp
    t = hour_min(stamp)
    return t if ref and day == ref else f"{day_label(day)} {t}"


def flight_times(it: Itinerary, offset: int, arrow: str = "→") -> str:
    """'7:56 PM → 5:15 AM (+2 days)'."""
    plus = f" (+{offset} day{'' if offset == 1 else 's'})" if offset else ""
    return f"{hour_min(it.depart_time)} {arrow} {hour_min(it.arrive_time)}{plus}"


def stops_text(it: Itinerary, via: bool = True) -> str:
    text = "nonstop" if it.stops == 0 else f"{it.stops} stop" + ("s" if it.stops > 1 else "")
    airports = it.route.split("-")[1:-1] if it.route else []
    return text + (f" ({', '.join(airports)})" if via and airports else "")


def flight_summary(it: Itinerary, duration: bool = True) -> str:
    parts = [", ".join(it.airlines) or "?", stops_text(it)]
    if duration:
        parts.append(fmt_duration(it.duration_min))
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
    for line in text.split(FARES_HEADER, 1)[1].splitlines()[1:]:  # [0] is the rest of the header line
        if not line.strip():
            break  # the block ends at the first blank line
        m = _FARE_LINE.match(line)
        if m:
            key = m.group(1) + (f"_{m.group(2)}" if m.group(2) else "")
            out[key] = float(m.group(3).replace(",", "")) if m.group(3) else None
    return out


_VERDICT_WORD = re.compile(r"\b(low|typical|high)\b", re.I)
VERDICT_ICON = {"high": ("▲", "#cf222e"), "low": ("▼", "#1a7f37"), "typical": ("●", "#57606a")}


def parse_verdicts(items: list[str]) -> dict[str, str]:
    """'2026-11-25=Prices are currently high' -> {'2026-11-25': 'high'}.

    The value is Google Flights' price insight for that departure date; any
    text holding low, typical or high works, so a quoted sentence can be passed.
    """
    out = {}
    for item in items or []:
        key, _, value = item.partition("=")
        m = _VERDICT_WORD.search(value)
        if key.strip() and m:
            out[key.strip()] = m.group(1).lower()
    return out


HISTORY_HEADER = "PRICE HISTORY"
_HISTORY_LINE = re.compile(r"^\s*checked (\d{4}-\d{2}-\d{2}):\s*(.*)$")
_HISTORY_ITEM = re.compile(r"(\d{4}-\d{2}-\d{2}(?:_\d{4}-\d{2}-\d{2})?)=(\d+(?:\.\d+)?|-)")
_CHECKED_AT = re.compile(r"prices checked \w{3} (\w{3}) (\d{1,2}) at")
SPARK = "▁▂▃▄▅▆▇█"
SPARK_MIN_SPAN = 40  # dollars: moves smaller than this stay low on the sparkline
SPARK_MAX_POINTS = 14  # the email shows the most recent checks only


def history_block(history: dict[str, dict[str, float | None]]) -> str:
    """Every check's cheapest fare per date, carried forward from report to report."""
    lines = [f"{HISTORY_HEADER} (cheapest fare per departure date at each check)"]
    for checked in sorted(history):
        items = " ".join(f"{k}={'-' if v is None else f'{v:.0f}'}" for k, v in sorted(history[checked].items()))
        lines.append(f"checked {checked}: {items}")
    return "\n".join(lines)


def parse_history(text: str, today: date) -> dict[str, dict[str, float | None]]:
    """Price history from a previous report.

    Reads its PRICE HISTORY block. A report sent before that block existed only
    has FARES BY DATE, which is used as one check on the date its footer gives.
    """
    history: dict[str, dict[str, float | None]] = {}
    if HISTORY_HEADER in text:
        for line in text.split(HISTORY_HEADER, 1)[1].splitlines():
            m = _HISTORY_LINE.match(line)
            if m:
                history[m.group(1)] = {k: None if v == "-" else float(v) for k, v in _HISTORY_ITEM.findall(m.group(2))}
    if history:
        return history
    fares = parse_fares_block(text)
    m = _CHECKED_AT.search(text)
    if fares and m:
        checked = date(today.year, datetime.strptime(m.group(1), "%b").month, int(m.group(2)))
        if checked > today:  # a December report read in January
            checked = checked.replace(year=today.year - 1)
        history[checked.isoformat()] = fares
    return history


def price_trend(results: list[ScanResult], history: dict | None) -> dict | None:
    """Each date's cheapest fare across checks; None until there are two checks."""
    if not history or len(history) < 2:
        return None
    checks = sorted(history)
    rows_in = sorted(results, key=lambda r: r.pair.key)
    keys = [r.pair.key for r in rows_in]
    values = [history[c][k] for c in checks for k in keys if history[c].get(k) is not None]
    if not values:
        return None
    lo = min(values)
    span = max(max(values) - lo, SPARK_MIN_SPAN)
    rows = []
    for r in rows_in:
        series = [history[c].get(r.pair.key) for c in checks]
        known = [v for v in series if v is not None]
        recent = series[-SPARK_MAX_POINTS:]
        spark = "".join("·" if v is None else SPARK[round((v - lo) / span * (len(SPARK) - 1))] for v in recent)
        rows.append({
            "result": r, "now": series[-1], "first": known[0] if known else None,
            "low": min(known) if known else None, "high": max(known) if known else None, "spark": spark,
        })
    overall = [min((history[c][k] for k in keys if history[c].get(k) is not None), default=None) for c in checks]
    return {"checks": checks, "rows": rows, "overall": overall, "truncated": len(checks) > SPARK_MAX_POINTS}


def render_email(
    results: list[ScanResult],
    s: Settings,
    previous: dict[str, float | None] | None,
    checked_at: datetime,
    today: date,
    note: str | None = None,
    max_price: float | None = None,
    fastest: int = 6,
    history: dict[str, dict[str, float | None]] | None = None,
    verdicts: dict[str, str] | None = None,
) -> tuple[str, str, str]:
    """Subject, plain-text body and HTML body for a fare report email."""
    fast = shortest_flights(results, fastest)
    # Google's price insight, for dates still being checked, in date order.
    judged = [(r, verdicts[r.pair.key]) for r in sorted(results, key=lambda r: r.pair.key)
              if verdicts and r.pair.key in verdicts]
    if judged:
        parts = [f"{word} for {pair_label(r.pair)}" for r, word in judged]
        joined = parts[0] if len(parts) == 1 else ", ".join(parts[:-1]) + " and " + parts[-1]
        verdict_line = f"Google says prices are currently {joined}, compared with usual prices for each date."
    trend = price_trend(results, history)
    if trend:
        since = day_label(date.fromisoformat(trend["checks"][0]))
        o_first = next((v for v in trend["overall"] if v is not None), None)
        o_now = trend["overall"][-1]
        if o_first is None or o_now is None:
            trend_summary = ""
        elif abs(o_now - o_first) < 1:
            trend_summary = f"The cheapest fare in your window has held at {money(o_now, s.currency)} since {since}."
        else:
            trend_summary = (
                f"The cheapest fare in your window is {'down' if o_now < o_first else 'up'} "
                f"{money(abs(o_now - o_first), s.currency)} since {since} "
                f"({money(o_first, s.currency)} → {money(o_now, s.currency)})."
            )
        n_checks = len(trend["checks"])
        trend_note = (f"Trend shows the last {SPARK_MAX_POINTS} of {n_checks} daily checks." if trend["truncated"]
                      else "Trend shows both daily checks." if n_checks == 2
                      else f"Trend shows all {n_checks} daily checks.")

    def price_range(row: dict, dash: str) -> str:
        if abs(row["high"] - row["low"]) < 1:
            return money(row["low"], s.currency)
        return f"{money(row['low'], s.currency)}{dash}{money(row['high'], s.currency)}"

    def since_text(row: dict) -> str:
        if row["now"] is None or row["first"] is None:
            return "—"
        d = row["now"] - row["first"]
        return "no change" if abs(d) < 1 else f"{'▼' if d < 0 else '▲'} {money(abs(d), s.currency)}"
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
    if judged:
        t += ["", verdict_line]
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
    if trend:
        t.append(f"Price trend since {since} (cheapest fare at each daily check)")
        if trend_summary:
            t.append(trend_summary)
        for row in trend["rows"]:
            r = row["result"]
            if row["now"] is None:
                t.append(f"{pair_label(r.pair)}: no price now  {row['spark']}")
                continue
            t.append(f"{pair_label(r.pair)}: {money(row['now'], s.currency)} now, {since_text(row)} since {since}, "
                     f"range {price_range(row, '-')}  {row['spark']}")
        t += [trend_note, ""]
    if fast:
        t.append(f"Shortest flights (the {len(fast)} fastest, with each departure date's price, cheapest first)")
        for g in fast:
            it = g["itinerary"]
            t.append(f"{fmt_duration(it.duration_min)} - {flight_summary(it, duration=False)}, "
                     f"{flight_times(it, g['offset'], '->')}")
            t.append("  " + ", ".join(f"{pair_label(r.pair)} {money(p, s.currency)}" for r, p in g["prices"]))
        t.append("")
    t += [footer, "", fares_block(results, s), ""]
    if history:
        t += [history_block(history), ""]
    text = "\n".join(t)

    # HTML
    e = html.escape
    muted = "color:#57606a;"
    cell = "border-bottom:1px solid #d8dee4;"  # padding and alignment come from the table/row attributes
    table = '<table cellpadding="6" style="border-collapse:collapse;width:100%;font-size:13px;line-height:1.35;">'
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
    if judged:
        badges = " · ".join(
            f'<span style="white-space:nowrap;">{e(pair_label(r.pair))}: '
            f'<span style="color:{VERDICT_ICON[word][1]};">{VERDICT_ICON[word][0]}</span> {e(word)}</span>'
            for r, word in judged
        )
        h.append(f'<p style="font-size:14px;margin:0 0 18px;"><strong>Google&#x27;s price check:</strong> {badges}'
                 f'<br><span style="font-size:12px;{muted}">Compared with usual prices for each date, '
                 "from Google Flights&#x27; price insights.</span></p>")
    h.append(f'<h3 style="font-size:15px;margin:0 0 6px;">{e(table_title)}</h3>')
    h.append(table)
    heads = ["Date", "Price"] + (["Change"] if previous is not None else []) + ["Flight", "Departs → Arrives", ""]
    h.append('<tr valign="bottom">' + "".join(f'<th style="{cell}text-align:left;font-weight:600;{muted}">{e(x)}</th>' for x in heads) + "</tr>")
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
        style = ' style="font-weight:700;background:#f6f8fa;"' if highlight else ""
        h.append(f'<tr valign="top"{style}>' + "".join(f'<td style="{cell}">{x}</td>' for x in tds) + "</tr>")
    h.append("</table>")
    for line in ([changes] if changes else []) + extra:
        h.append(f'<p style="font-size:14px;margin:14px 0 0;">{e(line)}</p>')
    if trend:
        h.append(f'<h3 style="font-size:15px;margin:24px 0 2px;">Price trend since {e(since)}</h3>')
        if trend_summary:
            h.append(f'<p style="font-size:14px;margin:0 0 6px;">{e(trend_summary)}</p>')
        h.append(table)
        h.append('<tr valign="bottom">' + "".join(
            f'<th style="{cell}text-align:left;font-weight:600;{muted}">{e(x)}</th>'
            for x in ["Date", "Now", f"Since {since}", "Low – high", "Trend"]) + "</tr>")
        for row in trend["rows"]:
            r = row["result"]
            d = None if row["now"] is None or row["first"] is None else row["now"] - row["first"]
            color = "#1a7f37" if d is not None and d <= -1 else "#cf222e" if d is not None and d >= 1 else "#57606a"
            tds = [
                e(pair_label(r.pair)),
                e(money(row["now"], s.currency)) if row["now"] is not None else "no price",
                f'<span style="color:{color};white-space:nowrap;">{e(since_text(row))}</span>',
                e(price_range(row, " – ")) if row["low"] is not None else "—",
                f'<span style="font-family:Menlo,Consolas,monospace;font-size:14px;color:#2a78d6;white-space:nowrap;">'
                f"{e(row['spark'])}</span>",
            ]
            h.append('<tr valign="top">' + "".join(f'<td style="{cell}">{x}</td>' for x in tds) + "</tr>")
        h.append("</table>")
        h.append(f'<p style="font-size:12px;{muted}margin:6px 0 0;">{e(trend_note)} Taller bars mean higher prices; '
                 "the bars share one scale across all dates.</p>")
    if fast:
        h += [
            '<h3 style="font-size:15px;margin:24px 0 2px;">Shortest flights</h3>',
            f'<p style="font-size:13px;{muted}margin:0 0 6px;">The {len(fast)} fastest flights, with their price on '
            "each departure date (cheapest first).</p>",
            table,
            '<tr valign="bottom">' + "".join(f'<th style="{cell}text-align:left;font-weight:600;{muted}">{e(x)}</th>'
                             for x in ["Duration", "Flight", "Departs → Arrives", "Price by departure date"]) + "</tr>",
        ]
        for g in fast:
            it = g["itinerary"]
            prices = " · ".join(
                f'<a href="{e(r.link)}" style="{link}white-space:nowrap;">'
                f"{e(pair_label(r.pair))} {e(money(p, s.currency))}</a>"
                for r, p in g["prices"]
            )
            tds = [
                f'<span style="white-space:nowrap;font-weight:600;">{e(fmt_duration(it.duration_min))}</span>',
                e(flight_summary(it, duration=False)),
                e(flight_times(it, g["offset"])),
                prices,
            ]
            h.append('<tr valign="top">' + "".join(f'<td style="{cell}">{x}</td>' for x in tds) + "</tr>")
        h.append("</table>")
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
        help="auto = serpapi when SERPAPI_KEY is set, otherwise google; "
             "firecrawl reads --firecrawl-json or --firecrawl-listing",
    )
    p.add_argument("--firecrawl-json", type=Path, default=None,
                   help="saved result of Firecrawl's flights-google-com / flights/search_flights capability")
    p.add_argument("--firecrawl-listing", type=Path, default=None,
                   help="one-way D|/F| listing made from that result with the jq projection in SKILL.md")
    p.add_argument("--email-dir", type=Path, default=None,
                   help="write an email report here: subject.txt, body.txt and body.html")
    p.add_argument("--previous", type=Path, default=None,
                   help="plain-text body of the previous email report, used to show price changes")
    p.add_argument("--note", default=None, help="extra line to show near the top of the email report")
    p.add_argument("--verdict", action="append", default=[], metavar="DATE=VERDICT",
                   help="Google Flights' price insight for a departure date, e.g. 2026-11-25=high "
                        "(repeatable); shown in the email report")
    p.add_argument("--tz", default=DEFAULT_TZ, help="time zone for today's date and the checked-at time")
    p.add_argument("--delay", type=float, default=2.0, help="seconds between lookups")
    p.add_argument("--top", type=int, default=15, help="rows to show in the ranked table")
    p.add_argument("--fastest", type=int, default=6,
                   help="list this many of the shortest flights with their prices (0 hides the list)")
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
    if source == "firecrawl" and not (a.firecrawl_json or a.firecrawl_listing):
        print("--source firecrawl needs --firecrawl-json FILE or --firecrawl-listing FILE", file=sys.stderr)
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
        parsed = (parse_firecrawl_listing(a.firecrawl_listing.read_text()) if a.firecrawl_listing
                  else parse_firecrawl(json.loads(a.firecrawl_json.read_text())))
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
    fast = render_shortest(results, s, a.fastest)
    if fast:
        print("\nShortest flights")
        print(fast)

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
        history: dict[str, dict[str, float | None]] = {}
        note = a.note
        if a.previous:
            prev_text = a.previous.read_text()
            previous = parse_fares_block(prev_text)
            history = parse_history(prev_text, today)
            if previous is None and not note:
                note = "Couldn't find the price list in the previous report, so changes aren't shown."
        history[today.isoformat()] = {r.pair.key: r.best.price if r.best else None for r in results}
        checked_at = _observed_at(parsed, tz) or datetime.now(tz)
        subject, text, html_body = render_email(results, s, previous, checked_at, today, note, a.max_price,
                                                a.fastest, history, parse_verdicts(a.verdict))
        a.email_dir.mkdir(parents=True, exist_ok=True)
        (a.email_dir / "subject.txt").write_text(subject + "\n")
        (a.email_dir / "body.txt").write_text(text)
        (a.email_dir / "body.html").write_text(html_body)
        print(f"\nEmail report written to {a.email_dir} (subject.txt, body.txt, body.html)")
        print(f"Subject: {subject}")

    return 0 if priced else 1


if __name__ == "__main__":
    sys.exit(main())
