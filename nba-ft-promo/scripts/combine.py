"""Combine NBA-feed seasons with the current ESPN season into one set of tables.

ESPN and the NBA feed number players differently. Both feeds cover 2025-26, so each
ESPN player id is matched to an NBA person id through that season's lines: same team,
same free throw totals and same last name (falling back to team and short name).
ESPN players with no match (mostly rookies) get id 10,000,000 + ESPN id so the two
numbering systems cannot collide.

Usage: python combine.py <out_dir> <nba_build_dir> <espn_overlap_build_dir> <espn_current_build_dir>
"""
import sys
import unicodedata
from pathlib import Path

import pandas as pd

ESPN_OFFSET = 10_000_000
TABLES = ["games", "team_games", "q4_free_throws", "player_seasons", "player_games"]


def norm(s: str) -> str:
    s = unicodedata.normalize("NFKD", str(s)).encode("ascii", "ignore").decode().lower()
    for suffix in (" jr.", " sr.", " iii", " ii", " iv"):
        s = s.replace(suffix, "")
    return s.replace(".", "").replace("'", "").replace("-", " ").strip()


def last_name(short: str) -> str:
    n = norm(short).split()
    return n[-1] if n else ""


def crosswalk(nba_ps: pd.DataFrame, espn_ps: pd.DataFrame) -> pd.DataFrame:
    n = nba_ps.assign(last=nba_ps.player_short.map(last_name), key=nba_ps.player_short.map(norm))
    e = espn_ps.assign(last=espn_ps.player_short.map(last_name), key=espn_ps.player_short.map(norm))
    m1 = e.merge(n, on=["team", "fta", "ftm", "last"], suffixes=("_e", "_n"))
    m1 = m1.groupby("personId_e").filter(lambda g: g.personId_n.nunique() == 1)
    pairs = m1[["personId_e", "personId_n"]].drop_duplicates()
    rest_e = e[~e.personId.isin(pairs.personId_e)]
    m2 = rest_e.merge(n[~n.personId.isin(pairs.personId_n)], on=["team", "key"], suffixes=("_e", "_n"))
    m2 = m2.groupby("personId_e").filter(lambda g: g.personId_n.nunique() == 1)
    pairs = pd.concat([pairs, m2[["personId_e", "personId_n"]].drop_duplicates()])
    # One ESPN id per NBA id.
    pairs = pairs.groupby("personId_e").personId_n.first().reset_index()
    pairs = pairs[~pairs.personId_n.duplicated(keep=False)]
    return pairs.rename(columns={"personId_e": "espn_id", "personId_n": "nba_id"})


def main():
    out, nba_dir, overlap_dir, cur_dir = (Path(p) for p in sys.argv[1:5])
    out.mkdir(parents=True, exist_ok=True)
    nba_ps = pd.read_csv(nba_dir / "player_seasons.csv")
    ov_ps = pd.read_csv(overlap_dir / "player_seasons.csv")
    cw = crosswalk(nba_ps[nba_ps.season == ov_ps.season.iloc[0]], ov_ps)
    ov_players = ov_ps.personId.nunique()
    print(f"crosswalk: {len(cw)} of {ov_players} ESPN {ov_ps.season.iloc[0]} players matched to NBA ids")
    cw.to_csv(out / "player_id_crosswalk.csv", index=False)
    to_nba = dict(zip(cw.espn_id, cw.nba_id))
    cur_ps = pd.read_csv(cur_dir / "player_seasons.csv")
    cur_ids = cur_ps.personId.unique()
    print(f"current season: {sum(i in to_nba for i in cur_ids)} of {len(cur_ids)} players carry an NBA id")
    for t in TABLES:
        a = pd.read_csv(nba_dir / f"{t}.csv", dtype={"game_id": str}, low_memory=False)
        b = pd.read_csv(cur_dir / f"{t}.csv", dtype={"game_id": str}, low_memory=False)
        if "personId" in b.columns:
            b["personId"] = b.personId.map(lambda i: to_nba.get(i, ESPN_OFFSET + i))
        c = pd.concat([a, b], ignore_index=True)
        c.to_csv(out / f"{t}.csv", index=False)
        print(f"{t:15s} {len(a):7d} + {len(b):6d} rows")


if __name__ == "__main__":
    main()
