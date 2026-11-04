"""Offline tests: no network calls. Run with  python -m pytest -q  (or python test_flight_scanner.py)."""

import json
from datetime import date, datetime

import flight_scanner as fs

S = fs.Settings("SNA", "TPE", 1, "economy", "USD", None)


def test_round_trip_pairs_cover_window():
    pairs = fs.build_pairs(date(2026, 11, 25), date(2026, 12, 2))
    assert len(pairs) == 28  # 7+6+...+1
    assert pairs[0] == fs.DatePair(date(2026, 11, 25), date(2026, 11, 26))
    assert pairs[-1] == fs.DatePair(date(2026, 12, 1), date(2026, 12, 2))
    assert all(p.ret > p.depart for p in pairs)


def test_min_max_nights_and_one_way():
    pairs = fs.build_pairs(date(2026, 11, 25), date(2026, 12, 2), min_nights=5, max_nights=6)
    assert {p.nights for p in pairs} == {5, 6}
    assert len(pairs) == 5  # 3 five-night + 2 six-night
    ow = fs.build_pairs(date(2026, 11, 25), date(2026, 12, 2), one_way=True)
    assert len(ow) == 8 and all(p.ret is None for p in ow)


def test_scan_picks_cheapest_and_survives_errors():
    def fake(pair, s):
        if pair.depart == date(2026, 11, 27):
            raise RuntimeError("blocked")
        base = 1000 - pair.nights * 10 - pair.depart.day
        return [fs.Itinerary(base + 200, ["EVA Air"], 1), fs.Itinerary(base, ["China Airlines"], 0, 900)]

    pairs = fs.build_pairs(date(2026, 11, 25), date(2026, 12, 2))
    res = fs.scan(pairs, S, "fake", fetch=fake, delay=0, retries=0, log=lambda *a, **k: None)
    ok = [r for r in res if r.best]
    assert len(ok) == 28 - 5 and all(r.best.airlines == ["China Airlines"] for r in ok)
    assert sum(1 for r in res if r.error) == 5
    table = fs.render_table(res, S, top=3)
    assert "China Airlines" in table and "nonstop" in table
    grid = fs.render_grid(res, S)
    assert "err" in grid and "*" in grid


def test_parse_serpapi():
    data = {
        "best_flights": [{
            "price": 812, "total_duration": 1010,
            "flights": [
                {"airline": "Alaska", "departure_airport": {"id": "SNA", "time": "2026-11-25 07:00"},
                 "arrival_airport": {"id": "SFO", "time": "2026-11-25 08:30"}},
                {"airline": "EVA Air", "departure_airport": {"id": "SFO", "time": "2026-11-25 11:00"},
                 "arrival_airport": {"id": "TPE", "time": "2026-11-26 17:00"}},
            ],
        }],
        "other_flights": [{"price": 990, "flights": [
            {"airline": "Delta", "departure_airport": {"id": "SNA"}, "arrival_airport": {"id": "TPE"}}]}],
    }
    its = fs.parse_serpapi(data)
    assert [i.price for i in its] == [812, 990]
    assert its[0].route == "SNA-SFO-TPE" and its[0].stops == 1 and its[0].airlines == ["Alaska", "EVA Air"]


def test_links_and_history(tmp_path):
    p = fs.DatePair(date(2026, 11, 25), date(2026, 12, 2))
    assert fs.google_flights_link(p, S).startswith("https://www.google.com/travel/flights")
    assert fs.kayak_link(p, S) == "https://www.kayak.com/flights/SNA-TPE/2026-11-25/2026-12-02/1adults?sort=price_a"
    h = tmp_path / "h.json"
    r = fs.ScanResult(p, "x", fs.Itinerary(900, ["EVA Air"], 1))
    assert fs.update_history([r], h, S) == []
    r.best = fs.Itinerary(850, ["EVA Air"], 1)
    notes = fs.update_history([r], h, S)
    assert notes and "down $50" in notes[0]
    assert len(json.loads(h.read_text())["SNA-TPE-economy-1-USD"]["2026-11-25_2026-12-02"]) == 2


# Trimmed from a real flights-google-com / flights/search_flights result.
FIRECRAWL = {"success": True, "data": {"alexandria": [
    {"provider": "flights-google-com", "capability": "flights/search_flights", "data": {
        "query": {"departure_date": "2026-11-25", "return_date": None, "currency": "USD"},
        "search_url": "https://www.google.com/travel/flights?tfs=A&curr=USD",
        "observed_at_ms": 1793826400000,
        "flights": [
            {"price": {"amount": 528, "currency": "USD"}, "stops": 1, "duration_minutes": 1090,
             "segments": [
                 {"airline_name": "United", "origin": "SNA", "destination": "SFO",
                  "departure_local": "2026-11-25T19:35:00", "arrival_local": "2026-11-25T21:10:00"},
                 {"airline_name": "United", "origin": "SFO", "destination": "TPE",
                  "departure_local": "2026-11-26T01:00:00", "arrival_local": "2026-11-27T05:45:00"}]},
            {"price": {"amount": 503, "currency": "USD"}, "stops": 1, "duration_minutes": 1290,
             "segments": [
                 {"airline_name": "Delta", "origin": "SNA", "destination": "SEA",
                  "departure_local": "2026-11-25T07:00:00", "arrival_local": "2026-11-25T10:05:00"},
                 {"airline_name": "Delta", "origin": "SEA", "destination": "TPE",
                  "departure_local": "2026-11-25T15:05:00", "arrival_local": "2026-11-26T20:30:00"}]},
        ]}},
    {"provider": "flights-google-com", "capability": "flights/search_flights",
     "error": {"code": "UPSTREAM_TIMEOUT", "message": "timed out"}},
]}}


def test_default_trip_is_one_way():
    assert fs.parse_args([]).round_trip is False
    assert fs.parse_args(["--round-trip"]).round_trip is True
    res = [fs.ScanResult(fs.DatePair(date(2026, 11, 25), None), "x", fs.Itinerary(503, ["Delta"], 1))]
    table = fs.render_table(res, S)
    assert "Return" not in table and "$503" in table


def test_firecrawl_source():
    parsed = fs.parse_firecrawl(FIRECRAWL)
    assert len(parsed["_errors"]) == 1 and "UPSTREAM_TIMEOUT" in parsed["_errors"][0]
    pairs = fs.build_pairs(date(2026, 11, 25), date(2026, 11, 26), one_way=True)
    res = fs.scan(pairs, S, "firecrawl", fetch=fs.firecrawl_fetcher(parsed), delay=0, retries=0,
                  log=lambda *a, **k: None)
    best = res[0].best
    assert best.price == 503 and best.airlines == ["Delta"] and best.route == "SNA-SEA-TPE"
    assert best.depart_time == "2026-11-25 07:00" and best.arrive_time == "2026-11-26 20:30"
    assert res[1].best is None and "no Firecrawl result" in res[1].error


def test_email_report_round_trips_prices():
    parsed = fs.parse_firecrawl(FIRECRAWL)
    pairs = fs.build_pairs(date(2026, 11, 25), date(2026, 11, 26), one_way=True)
    res = fs.scan(pairs, S, "firecrawl", fetch=fs.firecrawl_fetcher(parsed), delay=0, retries=0,
                  log=lambda *a, **k: None)
    prev = fs.parse_fares_block("Earlier report\nFARES BY DATE\n2026-11-25: $543 (Delta, 1 stop)\n2026-11-26: no price\n")
    assert prev == {"2026-11-25": 543.0, "2026-11-26": None}
    subject, text, html_body = fs.render_email(res, S, prev, datetime(2026, 11, 4, 13, 15), date(2026, 11, 4))
    assert subject == "SNA to TPE one-way fares, Wed Nov 4: from $503 on Wed Nov 25"
    assert "▼ $40" in html_body and "Delta · 1 stop (SEA) · 21h 30m" in html_body
    assert "Biggest moves since the last report: Wed Nov 25 down $40." in text
    assert "7:00 AM -> Thu Nov 26 8:30 PM" in text
    # the next day's run reads this report's prices back
    assert fs.parse_fares_block(text) == {"2026-11-25": 503.0, "2026-11-26": None}
    first = fs.render_email(res, S, None, datetime(2026, 11, 4, 13, 15), date(2026, 11, 4))[1]
    assert "First report, nothing to compare yet." in first


def _it(price, dep, arr, minutes, airlines=("STARLUX Airlines",), route="SNA-SFO-TPE"):
    return fs.Itinerary(price, list(airlines), len(route.split("-")) - 2, minutes, dep, arr, route)


def test_shortest_flights_groups_same_flight_across_dates():
    d1, d2 = date(2026, 11, 27), date(2026, 11, 28)
    r1 = fs.ScanResult(fs.DatePair(d1, None), "u1")
    r1.itineraries = [
        _it(1416, "2026-11-27 19:56", "2026-11-29 05:15", 1039),
        _it(503, "2026-11-27 07:00", "2026-11-28 20:30", 1290, ("Delta",), "SNA-SEA-TPE"),
    ]
    r2 = fs.ScanResult(fs.DatePair(d2, None), "u2")
    r2.itineraries = [
        _it(662, "2026-11-28 19:56", "2026-11-30 05:15", 1039),
        _it(700, "2026-11-28 19:56", "2026-11-30 05:15", 1039),  # same flight listed twice
        _it(503, "2026-11-28 07:00", "2026-11-29 20:30", 1290, ("Delta",), "SNA-SEA-TPE"),
    ]
    top = fs.shortest_flights([r1, r2], n=6)
    assert [g["itinerary"].airlines for g in top] == [["STARLUX Airlines"], ["Delta"]]
    fastest = top[0]
    assert fastest["offset"] == 2
    assert [(r.pair.depart, p) for r, p in fastest["prices"]] == [(d2, 662), (d1, 1416)]  # cheapest first
    assert len(fs.shortest_flights([r1, r2], n=1)) == 1 and fs.shortest_flights([r1, r2], n=0) == []
    table = fs.render_shortest([r1, r2], S)
    assert "17h 19m" in table and "7:56 PM -> 5:15 AM (+2 days)" in table
    assert "Sat Nov 28 $662, Fri Nov 27 $1,416" in table


def test_email_lists_shortest_flights():
    parsed = fs.parse_firecrawl(FIRECRAWL)
    pairs = fs.build_pairs(date(2026, 11, 25), date(2026, 11, 25), one_way=True)
    res = fs.scan(pairs, S, "firecrawl", fetch=fs.firecrawl_fetcher(parsed), delay=0, retries=0,
                  log=lambda *a, **k: None)
    _, text, html_body = fs.render_email(res, S, None, datetime(2026, 11, 4, 13, 15), date(2026, 11, 4))
    assert "Shortest flights (the 2 fastest" in text
    assert "18h 10m - United · 1 stop (SFO), 7:35 PM -> 5:45 AM (+2 days)\n  Wed Nov 25 $528" in text
    assert "Shortest flights</h3>" in html_body and "Wed Nov 25 $528</a>" in html_body
    assert fs.parse_fares_block(text) == {"2026-11-25": 503.0}  # still readable by the next run
    _, text, html_body = fs.render_email(res, S, None, datetime(2026, 11, 4, 13, 15), date(2026, 11, 4), fastest=0)
    assert "Shortest flights" not in text and "Shortest flights" not in html_body


OLD_REPORT = """SNA to TPE one-way fares, Wed Nov 4

Google Flights prices checked Wed Nov 4 at 1:07 PM PST for 1 adult in economy.

FARES BY DATE
2026-11-25: $503 (Delta, 1 stop)
2026-11-26: $503 (Delta, 1 stop)
"""


def test_price_history_carries_forward():
    today = date(2026, 11, 5)
    history = fs.parse_history(OLD_REPORT, today)  # older report: no PRICE HISTORY block yet
    assert history == {"2026-11-04": {"2026-11-25": 503.0, "2026-11-26": 503.0}}
    r1 = fs.ScanResult(fs.DatePair(date(2026, 11, 25), None), "u1", fs.Itinerary(510, ["Delta"], 1, 1290))
    r2 = fs.ScanResult(fs.DatePair(date(2026, 11, 26), None), "u2")  # no price today
    history["2026-11-05"] = {"2026-11-25": 510.0, "2026-11-26": None}
    _, text, html_body = fs.render_email([r1, r2], S, fs.parse_fares_block(OLD_REPORT), datetime(2026, 11, 5, 6, 40),
                                         today, history=history)
    assert "Price trend since Wed Nov 4" in text and "Price trend since Wed Nov 4</h3>" in html_body
    assert "The cheapest fare in your window is up $7 since Wed Nov 4 ($503 → $510)." in text
    assert "Wed Nov 25: $510 now, ▲ $7 since Wed Nov 4, range $503-$510  ▁▂" in text
    assert "Price trend since Wed Nov 4 (cheapest fare at each daily check)" in text
    assert "Thu Nov 26: no price now  ▁·" in text
    # the next run reads both checks back, and the history lines don't leak into the day-over-day prices
    assert fs.parse_history(text, date(2026, 11, 6)) == history
    assert fs.parse_fares_block(text) == {"2026-11-25": 510.0, "2026-11-26": None}


def test_no_trend_until_two_checks():
    r1 = fs.ScanResult(fs.DatePair(date(2026, 11, 25), None), "u1", fs.Itinerary(503, ["Delta"], 1, 1290))
    history = {"2026-11-04": {"2026-11-25": 503.0}}
    _, text, html_body = fs.render_email([r1], S, None, datetime(2026, 11, 4, 13, 7), date(2026, 11, 4), history=history)
    assert "Price trend" not in text and "Price trend" not in html_body
    assert "PRICE HISTORY" in text and "checked 2026-11-04: 2026-11-25=503" in text


if __name__ == "__main__":
    import pathlib, tempfile
    for name, fn in list(globals().items()):
        if name.startswith("test_"):
            if "tmp_path" in fn.__code__.co_varnames[: fn.__code__.co_argcount]:
                with tempfile.TemporaryDirectory() as d:
                    fn(pathlib.Path(d))
            else:
                fn()
            print("ok", name)
