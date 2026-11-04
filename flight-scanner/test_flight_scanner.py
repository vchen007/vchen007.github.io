"""Offline tests: no network calls. Run with  python -m pytest -q  (or python test_flight_scanner.py)."""

import json
from datetime import date

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
