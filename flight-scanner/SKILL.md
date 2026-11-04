---
name: flight-scanner
description: Scan flight prices from SNA (Orange County) to TPE (Taipei) for every departure/return date combination between Nov 25 and Dec 2, 2026, and report the cheapest options, a price grid, booking links and price changes since the last scan. Use when the user asks to check, scan, compare, track or watch flight prices or fares for their SNA to TPE / Taiwan trip, or asks what the cheapest dates to fly are. Also works for other routes and dates through flags.
---

# Flight scanner: SNA → TPE, Nov 25 – Dec 2, 2026

This skill runs `flight_scanner.py` (in the same folder as this file) to price
every date combination in the travel window and summarize the best options.

## Trip defaults

| Setting | Default |
|---|---|
| Route | SNA (John Wayne, Orange County) → TPE (Taoyuan, Taipei) |
| Window | Depart on or after **2026-11-25**, fly home on or before **2026-12-02** |
| Trip | Round trip, every depart/return pair in the window (28 pairs) |
| Travelers | 1 adult, economy, USD |

All dates are departure dates. Flights from SNA usually land in Taipei two
calendar days later (date line), so a Nov 25 departure arrives about Nov 27.

## Setup (first run only)

```bash
cd ~/.claude/skills/flight-scanner
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt
```

If `requirements.txt` or `flight_scanner.py` is missing, the user saved only
this file. Tell them to copy the whole `flight-scanner` folder from their
`vchen007.github.io` repo into `~/.claude/skills/`.

Optional, more reliable prices: if the user has a SerpApi key
(https://serpapi.com, free tier 250 searches/month), set `SERPAPI_KEY` in the
environment. A full round-trip scan uses 28 searches.

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
| "at least N nights" / "at most N nights" | `--min-nights N` / `--max-nights N` |
| "nonstop" / "max 1 stop" | `--max-stops 0` / `--max-stops 1` |
| "one way" | `--one-way` |
| "under $900" / "alert me below X" | `--max-price 900` |
| "business class" / "premium economy" | `--cabin business` / `--cabin premium-economy` |
| "2 people" | `--adults 2` |
| "in TWD" | `--currency TWD` |
| "save a spreadsheet" | `--csv sna_tpe.csv` |
| "just give me links" or lookups keep failing | `--source links` |
| different route/dates | `--origin LAX --destination TPE --start 2026-11-24 --end 2026-12-03` |

Without `SERPAPI_KEY` the scanner uses `--source google`, which reads Google
Flights directly. A full scan takes about a minute because of the 2-second
delay between lookups. If several lookups fail with errors, Google is
probably rate-limiting: rerun with `--delay 5`, suggest a SerpApi key, or
fall back to `--source links`.

## How to report results

1. Lead with the single best option: dates (with weekdays), price, airlines,
   stops, and its Google Flights link.
2. Show the top 5 from the "Cheapest options" table.
3. Point out patterns in the price grid, for example "returning Dec 1
   instead of Dec 2 saves about $120", or "Thanksgiving (Nov 26) departures
   cost more".
4. If the output has a "Changes since last run" section, summarize the
   biggest drops and rises.
5. If `--max-price` was given, list the fares under the threshold, or say
   none were found.
6. Say that prices come from Google Flights at scan time, can change, and
   should be confirmed on the booking link before buying. Never claim a fare
   is booked or guaranteed.

## Recurring checks

To watch prices over time, run the scan on a schedule (for example with
`/loop 6h` or a scheduled task). Price history is saved to
`price_history.json` next to the script, so each run reports what changed.
Use `--no-history` for a one-off scan that should not affect the history.
