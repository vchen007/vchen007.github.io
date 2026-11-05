"""Aggregate the combined tables into what the dashboard reads (JSON) and the same
tables as CSV for Tableau.

Usage: python export_dashboard.py <data_dir> <model_dir> <json_out_dir> <csv_out_dir>
  <data_dir>  team_games.csv, player_seasons.csv, analysis_summary.json (combine.py + analyze.py)
  <model_dir> upcoming_raw.json, model_meta.json (predict.py)
"""
import json
import re
import sys
from pathlib import Path

import numpy as np
import pandas as pd

HOME_GAMES_PER_SEASON = 41
ALL = "All"

data_dir, model_dir, json_dir, csv_dir = (Path(p) for p in sys.argv[1:5])
json_dir.mkdir(parents=True, exist_ok=True)
csv_dir.mkdir(parents=True, exist_ok=True)

tg = pd.read_csv(data_dir / "team_games.csv", dtype={"game_id": str})
tg = tg[~tg.neutral_site].copy()
summary = json.loads((data_dir / "analysis_summary.json").read_text())
meta = json.loads((model_dir / "model_meta.json").read_text())
seasons = sorted(tg.season.unique())
current = seasons[-1]
through = meta["data_through"]
names = tg.drop_duplicates("team").set_index("team").team_name.to_dict()
# ESPN writes some venues differently ("Toyota Center (Houston)", "crypto.com Arena"): use the NBA-feed spelling.
known = {a.lower(): a for a in tg.loc[tg.source == "nba_cdn", "arena"].unique()}
def clean_arena(v: str) -> str:
    v = re.sub(r"\s*\([^)]*\)$", "", str(v))
    return known.get(v.lower(), v)
tg["arena"] = tg.arena.map(clean_arena)


def season_text(s: str) -> str:
    if s == ALL:
        return f"{seasons[0]} to {current} so far"
    return f"{s} so far" if s == current else s


def scoped(df: pd.DataFrame):
    for s in seasons:
        yield s, df[df.season == s]
    yield ALL, df


def r4(x):
    return None if x is None or (isinstance(x, float) and np.isnan(x)) else round(float(x), 4)


def clock(minutes: float) -> str:
    sec = int(round(minutes * 60))
    return f"{sec // 60}:{sec % 60:02d}"


def ft_block(x: pd.DataFrame) -> dict:
    fta, ftm, xftm = int(x.q4_fta.sum()), int(x.q4_ftm.sum()), float(x.q4_xftm.sum())
    return {"games": int(len(x)), "q4_fta": fta, "q4_ftm": ftm, "q4_line": f"{ftm}/{fta}",
            "q4_ft_pct": r4(ftm / fta) if fta else None, "q4_xft_pct": r4(xftm / fta) if fta else None,
            "ftoe_pts": round(100 * (ftm - xftm) / fta, 2) if fta else None,
            "promos": int(x.promo.sum()), "rate": r4(x.promo.mean()) if len(x) else None,
            "xpromos": round(float(x.promo_xprob.sum()), 1)}


# Arena label per home team and scope: the building most of its home games were in.
home_rows = tg[tg.role == "Home"]
venue = home_rows.groupby(["season", "team"]).arena.agg(lambda a: a.value_counts().index[0]).to_dict()

away, home = tg[tg.role == "Away"], tg[tg.role == "Home"]
out = {}

rows = []
for scope, a in scoped(away):
    h = home[home.game_id.isin(a.game_id)]
    b, hb = ft_block(a), ft_block(h)
    rows.append({"season": scope, "season_label": season_text(scope), "data_through": through,
                 **{k: b[k] for k in ["games", "q4_fta", "q4_ftm", "q4_ft_pct", "promos", "rate", "xpromos"]},
                 "home_q4_ft_pct": hb["q4_ft_pct"], "home_rate": hb["rate"],
                 "lift": r4(b["promos"] / b["xpromos"] - 1), "home_games_per_season": HOME_GAMES_PER_SEASON,
                 "nights": round(b["rate"] * HOME_GAMES_PER_SEASON, 1),
                 "median_clock": clock(a.loc[a.promo, "promo_min_left"].median())})
out["kpis"] = rows

rows = []
for scope, a in scoped(away):
    h = home[home.season.isin(a.season.unique())]
    for team, x in a.groupby("team"):
        hb = ft_block(h[h.team == team])
        rows.append({"key": f"{scope}|{team}", "season": scope, "team": team, "team_name": names[team],
                     **ft_block(x), "home_q4_ft_pct": hb["q4_ft_pct"], "home_rate": hb["rate"]})
out["visitors"] = rows

rows = []
for scope, a in scoped(away):
    for team, x in a.groupby("arena_home_team"):
        if scope == ALL:
            labels = list(dict.fromkeys(venue[(s, team)] for s in reversed(seasons) if (s, team) in venue))
            arena, note = labels[0], "; ".join(f"{v} in {', '.join(s for s in seasons if venue.get((s, team)) == v)}" for v in labels[1:])
        else:
            arena, note = venue[(scope, team)], ""
        b = ft_block(x)
        rows.append({"key": f"{scope}|{team}", "season": scope, "home": team, "home_name": names[team], "arena": arena,
                     "arena_note": note, **b, "xrate": r4(b["xpromos"] / b["games"]),
                     "nights": round(b["rate"] * HOME_GAMES_PER_SEASON, 1)})
out["arenas"] = rows

rows = []
for scope, a in scoped(away):
    for (h_team, v_team), x in a.groupby(["arena_home_team", "team"]):
        b = ft_block(x)
        rows.append({"key": f"{scope}|{h_team}|{v_team}", "season": scope, "home": h_team, "team": v_team,
                     "team_name": names[v_team], **{k: b[k] for k in ["games", "q4_fta", "q4_ftm", "q4_line", "q4_ft_pct", "promos", "rate"]}})
out["matchups"] = rows

g = away.sort_values(["game_date", "game_id"])
out["games"] = [{"game_id": r.game_id, "season": r.season, "date": r.game_date, "home": r.arena_home_team, "team": r.team,
                 "q4_line": f"{r.q4_ftm}/{r.q4_fta}", "q4_fta": int(r.q4_fta), "q4_ftm": int(r.q4_ftm),
                 "promo": "Yes" if r.promo else "No", "clock": clock(r.promo_min_left) if r.promo else "",
                 "shooter": r.promo_shooter if isinstance(r.promo_shooter, str) else "", "margin_q3": int(r.margin_after_q3)}
                for r in g.itertuples()]

ps = pd.read_csv(data_dir / "player_seasons.csv")
rows = []
for scope in seasons + [ALL]:
    p = (ps if scope == ALL else ps[ps.season == scope]).sort_values("season")
    grp = p.groupby("personId")
    agg = grp.agg(player=("player_short", "last"), fta=("fta", "sum"), ftm=("ftm", "sum"),
                  road_q4_fta=("road_q4_fta", "sum"), road_q4_ftm=("road_q4_ftm", "sum"),
                  road_q4_trips=("road_q4_trips", "sum"), promo_games=("road_promo_games", "sum"))
    agg["teams"] = grp.team.agg(lambda t: "/".join(dict.fromkeys(t)))
    for pid, r in agg[agg.promo_games > 0].iterrows():
        rows.append({"key": f"{scope}|{int(pid)}", "season": scope, "player": r.player, "teams": r.teams,
                     "promo_games": int(r.promo_games), "road_q4_trips": int(r.road_q4_trips),
                     "road_q4_line": f"{int(r.road_q4_ftm)}/{int(r.road_q4_fta)}",
                     "road_q4_ft_pct": r4(r.road_q4_ftm / r.road_q4_fta) if r.road_q4_fta else None,
                     "season_ft_pct": r4(r.ftm / r.fta) if r.fta else None})
out["players"] = rows

buckets = [(-100, -15, "Trailing by 15+"), (-15, -6, "Trailing by 6-14"), (-6, 5, "Within 5"),
           (5, 14, "Leading by 6-14"), (14, 100, "Leading by 15+")]
rows = []
for scope, a in scoped(away):
    for i, (lo, hi, label) in enumerate(buckets):
        x = a[(a.margin_after_q3 > lo) & (a.margin_after_q3 <= hi)]
        b = ft_block(x)
        rows.append({"key": f"{scope}|{i}", "season": scope, "order": i, "bucket": label, "games": b["games"],
                     "promos": b["promos"], "rate": b["rate"], "q4_fta_per_game": round(b["q4_fta"] / max(1, b["games"]), 2),
                     "q4_ft_pct": b["q4_ft_pct"]})
out["margin"] = rows

rows = []
for scope, a in scoped(away):
    for m in range(12):
        sel = (a.promo_min_left >= m) & ((a.promo_min_left < m + 1) | ((m == 11) & (a.promo_min_left <= 12))) & a.promo
        rows.append({"key": f"{scope}|{m}", "season": scope, "min_left": m, "label": f"{m + 1}:00-{m}:00", "promos": int(sel.sum())})
out["timing"] = rows

rows = []
for i, y in enumerate(summary["team_yoy"], 1):
    tag = f"{y['from']} to {y['to']}"
    rows.append({"key": f"team_promo_{i}", "group": "Visiting team", "label": f"Road promo rate, {tag}", "kind": "correlation", "value": y["road_promo_rate_r"]})
    rows.append({"key": f"team_ft_{i}", "group": "Visiting team", "label": f"Road free throw %, {tag}", "kind": "correlation", "value": y["road_full_game_ft_pct_r"]})
for i, y in enumerate(summary["arena_dispersion"]["yoy"], 1):
    tag = f"{y['from']} to {y['to']}"
    rows.append({"key": f"arena_promo_{i}", "group": "Arena", "label": f"Visitor promo rate at arena, {tag}", "kind": "correlation", "value": y["arena_promo_rate_r"]})
rows.append({"key": "arena_perm_promo", "group": "Arena", "label": "Arena promo rates vs. random shuffle", "kind": "p-value", "value": summary["arena_dispersion"]["perm_p_promo"]})
rows.append({"key": "road_minus_home", "group": "Road effect", "label": "Same team, road minus home Q4 FT% vs. expected (pts)", "kind": "points", "value": summary["road_minus_home_ftoe_pts"]})
rows.append({"key": "road_minus_home_p", "group": "Road effect", "label": "Road vs. home difference, paired test", "kind": "p-value", "value": round(summary["road_minus_home_p"], 3)})
out["checks"] = rows

keys = ["league", "team_rate", "players", "players_opp"]
out["models"] = [{"key": k, "model": r["model"], "auc": r["auc"], "brier_skill_pct": r["brier_skill_pct"],
                  "n_test": meta["n_test"], "test_season": meta["test"], "train_season": meta["train"]}
                 for k, r in zip(keys, meta["results"])]
out["model_bins"] = [{"key": str(b["bin"]), **b} for b in meta["bins"]]

up = pd.read_json(model_dir / "upcoming_raw.json", dtype={"game_id": str})
rows = []
for r in up.itertuples():
    top = list(r.top)
    row = {"game_id": r.game_id, "start_utc": r.start_utc, "date": r.date_et, "time_et": r.time_et,
           "home": r.home, "home_name": names[r.home], "away": r.away, "away_name": names[r.away],
           "arena": clean_arena(r.venue_full_name), "note": r.notes_headline or "", "prob": round(float(r.prob), 4),
           "exp_trips": round(float(r.exp_trips), 2), "visitor_ft": round(1 - float(r.team_miss), 4),
           "home_factor": round(float(r.opp), 3)}
    for i in range(2):
        t = top[i] if len(top) > i else None
        row[f"shooter{i + 1}"] = f"{t['player']} ({round(100 * t['ft'])}%)" if t else ""
        row[f"shooter{i + 1}_share"] = round(float(t["share"]), 3) if t else None
    rows.append(row)
up_rows = pd.DataFrame(rows)
up_rows["rank"] = up_rows.prob.rank(ascending=False, method="first").astype(int)
out["upcoming"] = up_rows.to_dict(orient="records")
b = {x["bin"]: x for x in meta["bins"]}
out["model_info"] = [{"key": "now", "data_through": through, "games_so_far": meta["games_so_far"],
                      "scored_after_utc": meta["scored_after_utc"], "upcoming_games": int(len(up_rows)),
                      "mean_prob": round(float(up_rows.prob.mean()), 4), "max_prob": round(float(up_rows.prob.max()), 4),
                      "min_prob": round(float(up_rows.prob.min()), 4),
                      "test_season": meta["test"], "n_test": meta["n_test"], "test_rate": round(meta["test_rate"], 4),
                      "top_fifth_rate": b[4]["actual"], "bottom_fifth_rate": b[0]["actual"]}]

for name, rows in out.items():
    (json_dir / f"{name}.json").write_text(json.dumps(rows, separators=(",", ":"), allow_nan=False, default=str))
    pd.DataFrame(rows).to_csv(csv_dir / f"summary_{name}.csv", index=False)
    print(f"{name:11s} {len(rows):5d} rows  {(json_dir / f'{name}.json').stat().st_size / 1024:7.1f} KB")
