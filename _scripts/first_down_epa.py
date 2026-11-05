"""Build the data behind /portfolio/first-down-epa/ from nflverse play-by-play.

Usage (from the repo root):
    pip install pandas pyarrow
    python3 _scripts/first_down_epa.py --seasons 2016-2026 --cache /tmp/nflverse

Downloads play_by_play_<season>.parquet from the nflverse-data GitHub release
into --cache (skipping files already there), keeps regular-season first-down
runs and passes, and writes:
    assets/data/first-down-epa.json      compact cells the page aggregates in the browser
    assets/data/first-down-epa-teams.csv one row per season and team (neutral situations)

Play selection follows common public EPA work (nflfastR conventions): plays
where pass == 1 or rush == 1 with a non-missing EPA, excluding QB kneels and
spikes. Sacks and scrambles count as passes. Plays wiped out by a penalty are
kept, so their EPA reflects the penalty.
"""
import argparse
import json
import os
import sys
import urllib.request
from datetime import date

import pandas as pd

URL = "https://github.com/nflverse/nflverse-data/releases/download/pbp/play_by_play_{season}.parquet"
COLUMNS = ["season", "season_type", "week", "posteam", "down", "pass", "rush", "epa",
           "success", "qb_kneel", "qb_spike", "wp", "qtr", "half_seconds_remaining", "yardline_100"]
# Use today's abbreviation for relocated teams so each franchise is one line.
RELOCATED = {"OAK": "LV", "SD": "LAC", "STL": "LA"}
SCRIPTS = ["neutral", "ahead", "behind", "late"]   # game situation buckets
ZONES = ["own", "opp", "red"]                      # own territory, opponent territory, red zone
TYPES = ["pass", "run"]


def parse_seasons(text):
    if "-" in text:
        a, b = text.split("-")
        return list(range(int(a), int(b) + 1))
    return [int(s) for s in text.split(",")]


def load(season, cache):
    path = os.path.join(cache, f"play_by_play_{season}.parquet")
    if not os.path.exists(path):
        print(f"downloading {season}...", file=sys.stderr)
        urllib.request.urlretrieve(URL.format(season=season), path)
    return pd.read_parquet(path, columns=COLUMNS)


def situation(df):
    late = (df["qtr"] >= 5) | (df["half_seconds_remaining"] <= 120)
    out = pd.Series("neutral", index=df.index)
    out[late] = "late"
    out[df["wp"] > 0.8] = "ahead"
    out[df["wp"] < 0.2] = "behind"
    return out


def zone(df):
    return pd.cut(df["yardline_100"], bins=[0, 20, 50, 100], labels=["red", "opp", "own"],
                  include_lowest=True).astype(str)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--seasons", default="2016-2026")
    ap.add_argument("--cache", default="/tmp/nflverse")
    ap.add_argument("--out", default="assets/data")
    args = ap.parse_args()
    os.makedirs(args.cache, exist_ok=True)
    seasons = parse_seasons(args.seasons)

    frames = []
    for season in seasons:
        df = load(season, args.cache)
        df = df[(df["season_type"] == "REG") & (df["down"] == 1) & df["epa"].notna()
                & ((df["pass"] == 1) | (df["rush"] == 1))
                & (df["qb_kneel"] != 1) & (df["qb_spike"] != 1) & df["posteam"].notna()
                & df["wp"].notna() & df["yardline_100"].notna()].copy()
        frames.append(df)
    df = pd.concat(frames, ignore_index=True)
    df["posteam"] = df["posteam"].replace(RELOCATED)
    df["type"] = df["pass"].eq(1).map({True: "pass", False: "run"})
    df["script"] = situation(df)
    df["zone"] = zone(df)

    teams = sorted(df["posteam"].unique())
    g = (df.groupby(["season", "posteam", "script", "zone", "type"], observed=True)
           .agg(n=("epa", "size"), epa=("epa", "sum"), succ=("success", "sum"))
           .reset_index())
    rows = [[seasons.index(int(r.season)), teams.index(r.posteam), SCRIPTS.index(r.script),
             ZONES.index(r.zone), TYPES.index(r.type), int(r.n), round(float(r.epa), 2), int(r.succ)]
            for r in g.itertuples()]

    last = max(seasons)
    last_week = int(df.loc[df["season"] == last, "week"].max())
    complete = last_week >= 18
    data = {
        "generated": date.today().isoformat(),
        "source": "nflverse play-by-play (github.com/nflverse/nflverse-data)",
        "seasons": seasons,
        "seasonNotes": {} if complete else {str(last): f"through Week {last_week}"},
        "teams": teams,
        "dims": {"script": SCRIPTS, "zone": ZONES, "type": TYPES},
        "columns": ["season", "team", "script", "zone", "type", "plays", "epaSum", "successes"],
        "rows": rows,
    }
    os.makedirs(args.out, exist_ok=True)
    with open(os.path.join(args.out, "first-down-epa.json"), "w") as f:
        json.dump(data, f, separators=(",", ":"))

    neutral = df[df["script"] == "neutral"]
    t = (neutral.groupby(["season", "posteam", "type"]).agg(plays=("epa", "size"), epa=("epa", "mean"),
                                                             success=("success", "mean"))
                .unstack("type"))
    t.columns = [f"{b}_{a}" for a, b in t.columns]
    t = t.reset_index().rename(columns={"posteam": "team"})
    t["pass_rate"] = t["pass_plays"] / (t["pass_plays"] + t["run_plays"])
    t = t[["season", "team", "pass_plays", "run_plays", "pass_rate", "pass_epa", "run_epa",
           "pass_success", "run_success"]].round(4)
    t.to_csv(os.path.join(args.out, "first-down-epa-teams.csv"), index=False)
    print(f"{len(df):,} first-down plays, {len(rows):,} cells, {len(teams)} teams; "
          f"{last} {'complete' if complete else f'through Week {last_week}'}", file=sys.stderr)


if __name__ == "__main__":
    main()
