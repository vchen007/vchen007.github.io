# Flight scanner: SNA → TPE

Finds the cheapest one-way flights from Orange County (SNA) to Taipei (TPE)
for each departure day between **Nov 25 and Dec 2, 2026**. For each day it
keeps the cheapest itinerary, then prints:

- a ranked table of the cheapest days (price, stops, duration, airlines, route)
- the best option with a Google Flights link to book or verify
- fares under your target price (`--max-price`)
- price changes since the last run (saved in `price_history.json`)
- the 6 shortest flights, each with its price on every departure date (`--fastest N`)
- optionally, an email report with day-over-day changes (`--email-dir`)

With `--round-trip` it prices every departure/return pair instead and adds a
departure × return price grid.

## Quick start

```bash
cd flight-scanner
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt
.venv/bin/python flight_scanner.py
```

Example output layout:

```
SNA -> TPE  one way  Nov 25 - Dec 02, 2026  1 adult(s), economy, USD
Source: google   Departure dates: 8

Cheapest options
#  Depart      Price  Stops  Duration  Airlines  Route
1  Wed Nov 25  $503   1      21h 30m   Delta     SNA-SEA-TPE
...
```

## Price sources

| Source | Needs | Notes |
|---|---|---|
| `google` (default without a key) | nothing | Reads Google Flights with [`fast-flights`](https://github.com/AWeirdDev/fast-flights). Free, but Google can rate-limit or change its page. Duration is air time without layovers. |
| `serpapi` (default when `SERPAPI_KEY` is set) | [SerpApi key](https://serpapi.com) | Google Flights results as JSON. More reliable; free tier is 250 searches/month and a one-way scan uses 8. |
| `firecrawl` | a saved Firecrawl result | For Claude sessions that can't reach Google: Claude calls the Firecrawl connector's Google Flights capability (`flights-google-com` / `flights/search_flights`, 5 credits per date) and passes the saved result with `--firecrawl-json`. Needs no installed packages. |
| `links` | nothing | No prices; prints a Google Flights and Kayak link for every date. |

```bash
export SERPAPI_KEY=your_key_here
.venv/bin/python flight_scanner.py
```

## Options

```bash
.venv/bin/python flight_scanner.py --max-stops 1           # 1 stop or fewer (SNA has no nonstop to TPE)
.venv/bin/python flight_scanner.py --max-price 600         # flag fares at or under $600
.venv/bin/python flight_scanner.py --fastest 10            # list the 10 shortest flights (0 hides them)
.venv/bin/python flight_scanner.py --round-trip --min-nights 5
.venv/bin/python flight_scanner.py --cabin business --adults 2
.venv/bin/python flight_scanner.py --csv sna_tpe.csv --json sna_tpe.json
.venv/bin/python flight_scanner.py --source links          # links only
.venv/bin/python flight_scanner.py --origin LAX            # compare a nearby airport
```

Run `python flight_scanner.py --help` for all flags. All dates are departure
dates, and dates before today are skipped. Because of the date line, SNA → TPE
flights land the next day (morning departures) or two days later (late-night
departures).

## Email report

```bash
python3 flight_scanner.py --source firecrawl --firecrawl-json fares.json \
    --email-dir email --previous last_email.txt
```

This writes `email/subject.txt`, `email/body.txt` and `email/body.html`: the
cheapest fare per day, then the shortest flights with their prices. The
plain-text body ends with a `FARES BY DATE` block; pass a previous report's
plain-text body as `--previous` and the new report shows each day's price
change and calls out moves of $25 or more.

## Use it from Claude Code

`SKILL.md` makes this folder a Claude Code skill. Copy the whole folder into
your skills directory:

```bash
mkdir -p ~/.claude/skills
cp -r flight-scanner ~/.claude/skills/flight-scanner
```

Then ask Claude things like "scan my Taipei flights", "which day is cheapest
to fly to Taipei?", or "any fares under $500?".

## Tests

```bash
.venv/bin/pip install pytest
.venv/bin/python -m pytest -q
```

The tests run offline with fake price data.
