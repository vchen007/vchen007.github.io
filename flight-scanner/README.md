# Flight scanner: SNA → TPE

Finds the cheapest flights from Orange County (SNA) to Taipei (TPE) for every
date combination between **Nov 25 and Dec 2, 2026**. For each
departure/return pair it keeps the cheapest itinerary, then prints:

- a ranked table of the cheapest date pairs (price, stops, duration, airlines, route)
- a departure × return price grid
- the best option with a Google Flights link to book or verify
- fares under your target price (`--max-price`)
- price changes since the last run (saved in `price_history.json`)

## Quick start

```bash
cd flight-scanner
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt
.venv/bin/python flight_scanner.py
```

Example output layout:

```
SNA -> TPE  round trip  Nov 25 - Dec 02, 2026  1 adult(s), economy, USD
Source: google   Date combinations: 28

Cheapest options
#  Depart      Return      Nights  Price  Stops  Duration  Airlines  Route
...
Price grid
Depart \ Return   Nov 26   Nov 27 ...   Dec 02
Wed Nov 25          ...
```

## Price sources

| Source | Needs | Notes |
|---|---|---|
| `google` (default without a key) | nothing | Reads Google Flights with [`fast-flights`](https://github.com/AWeirdDev/fast-flights). Free, but Google can rate-limit or change its page. Duration is air time without layovers. |
| `serpapi` (default when `SERPAPI_KEY` is set) | [SerpApi key](https://serpapi.com) | Google Flights results as JSON. More reliable; free tier is 250 searches/month and a full scan uses 28. |
| `links` | nothing | No prices; prints a Google Flights and Kayak link for every date pair. |

```bash
export SERPAPI_KEY=your_key_here
.venv/bin/python flight_scanner.py
```

## Options

```bash
.venv/bin/python flight_scanner.py --min-nights 5          # stays of 5+ nights
.venv/bin/python flight_scanner.py --max-stops 1           # 1 stop or fewer (SNA has no nonstop to TPE)
.venv/bin/python flight_scanner.py --max-price 900         # flag fares at or under $900
.venv/bin/python flight_scanner.py --one-way               # one-way fares, each day in the window
.venv/bin/python flight_scanner.py --cabin business --adults 2
.venv/bin/python flight_scanner.py --csv sna_tpe.csv --json sna_tpe.json
.venv/bin/python flight_scanner.py --source links          # links only
.venv/bin/python flight_scanner.py --origin LAX            # compare a nearby airport
```

Run `python flight_scanner.py --help` for all flags. All dates are departure
dates. Because of the date line, SNA → TPE flights land the next day (morning
departures) or two days later (late-night departures).

## Use it from Claude Code

`SKILL.md` makes this folder a Claude Code skill. Copy the whole folder into
your skills directory:

```bash
mkdir -p ~/.claude/skills
cp -r flight-scanner ~/.claude/skills/flight-scanner
```

Then ask Claude things like "scan my Taipei flights", "cheapest SNA to TPE
with at least 5 nights", or "any fares under $850?".

## Tests

```bash
.venv/bin/pip install pytest
.venv/bin/python -m pytest -q
```

The tests run offline with fake price data.
