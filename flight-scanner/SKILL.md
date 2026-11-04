---
name: flight-scanner
description: Scan one-way flight prices from SNA (Orange County) to TPE (Taipei) for each departure day between Nov 25 and Dec 2, 2026, and report the cheapest fares, booking links and price changes since the last scan. Use when the user asks to check, scan, compare, track or watch flight prices or fares for their SNA to TPE / Taiwan trip, or asks which day is cheapest to fly. Also handles round trips, other routes and other dates through flags.
---

# Flight scanner: SNA → TPE, Nov 25 – Dec 2, 2026

This skill runs `flight_scanner.py` (in the same folder as this file) to price
each departure day in the travel window and summarize the best options.

## Trip defaults

| Setting | Default |
|---|---|
| Route | SNA (John Wayne, Orange County) → TPE (Taoyuan, Taipei) |
| Trip | **One way**, departing any day from **2026-11-25** to **2026-12-02** (8 days) |
| Travelers | 1 adult, economy, USD |

Departure dates before today are skipped. Because of the date line, flights
from SNA land in Taipei the next day (morning departures) or two days later
(late-night departures), so a Nov 25 departure arrives Nov 26 or Nov 27.

## Setup (first run only)

```bash
cd ~/.claude/skills/flight-scanner
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt
```

If `flight_scanner.py` is missing, only this file was saved. Get the folder
from GitHub (or tell the user to copy the whole `flight-scanner` folder into
`~/.claude/skills/`):

```bash
git clone --depth 1 https://github.com/vchen007/vchen007.github.io /tmp/vchen-site
cd /tmp/vchen-site/flight-scanner
```

Optional, more reliable prices: if the user has a SerpApi key
(https://serpapi.com, free tier 250 searches/month), set `SERPAPI_KEY` in the
environment. A one-way scan uses 8 searches.

## How to run

Use the venv's Python if it exists, otherwise `python3`:

```bash
cd ~/.claude/skills/flight-scanner
.venv/bin/python flight_scanner.py
```

Map the user's request to flags:

| User says | Flags |
|---|---|
| "check prices" / "scan flights" | (none) |
| "round trip" / "coming back on ..." | `--round-trip`, plus `--min-nights N` / `--max-nights N` for stay length |
| "nonstop" / "max 1 stop" | `--max-stops 0` / `--max-stops 1` (SNA has no nonstop to TPE) |
| "under $600" / "alert me below X" | `--max-price 600` |
| "fastest flights" / "shortest flight time" | `--fastest N` (default 6 shortest flights, each with its price per date) |
| "business class" / "premium economy" | `--cabin business` / `--cabin premium-economy` |
| "2 people" | `--adults 2` |
| "in TWD" | `--currency TWD` |
| "save a spreadsheet" | `--csv sna_tpe.csv` |
| "just give me links" | `--source links` |
| different route/dates | `--origin LAX --destination TPE --start 2026-11-24 --end 2026-12-03` |

Without `SERPAPI_KEY` the scanner uses `--source google`, which reads Google
Flights directly with a 2-second delay between lookups. If several lookups
fail, Google is probably rate-limiting: rerun with `--delay 5`, use the
Firecrawl route below, or fall back to `--source links`.

## When Google can't be reached (cloud sessions)

Cloud sessions often block Google Flights, so `--source google` fails with
connection errors. If the Firecrawl connector is available, get prices through
it instead:

1. Call `firecrawl_scrape` with an `alexandria` array holding one entry per
   departure date (up to 10 per call; each entry costs 5 Firecrawl credits):
   `{"provider": "flights-google-com", "capability": "flights/search_flights", "options": {"origin": "SNA", "destination": "TPE", "departure_date": "YYYY-MM-DD", "adults": 1, "cabin_class": "economy", "currency": "USD", "limit": 50}}`
   Add `"return_date"` for round trips.
2. The result is large, so it is usually saved to a file. Pass that file to the
   scanner, which needs no installed packages for this:
   `python3 flight_scanner.py --source firecrawl --firecrawl-json <saved result file>`
3. For an email report add `--email-dir DIR` (writes `subject.txt`, `body.txt`,
   `body.html`), and `--previous FILE` with the last report's plain-text body to
   show price changes. The plain-text body ends with `FARES BY DATE` and
   `PRICE HISTORY` blocks that the next report reads back, so each report
   carries the whole price history and shows a Price trend section once
   there are two checks.

## How to report results

1. Lead with the single best option: departure date (with weekday), price,
   airlines, stops, and its Google Flights link. If several dates tie, say so.
2. Show the cheapest fare for each departure day from the "Cheapest options"
   table.
3. From the "Shortest flights" table, point out fast options that cost little
   more than the cheapest fare (e.g. "United via SFO is 4 hours shorter for
   $25 more").
4. Point out patterns across dates, for example "leaving Tue Dec 1 instead of
   Wed Nov 25 saves about $120", or "Thanksgiving week costs more".
5. If the output has a "Changes since last run" section, summarize the
   biggest drops and rises.
6. If `--max-price` was given, list the fares under the threshold, or say
   none were found.
7. Say that prices come from Google Flights at scan time, can change, and
   should be confirmed on the booking link before buying. Never claim a fare
   is booked or guaranteed.

## Recurring checks

To watch prices over time, run the scan on a schedule (for example with
`/loop 6h` or a scheduled task). Price history is saved to
`price_history.json` next to the script, so each run reports what changed.
Use `--no-history` for a one-off scan that should not affect the history.
