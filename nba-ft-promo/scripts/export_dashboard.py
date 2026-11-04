"""Aggregate the game-level data into the small tables the dashboard reads
(JSON) and the same tables as CSV for Tableau.

Usage: python export_dashboard.py <data_dir> <json_out_dir> <csv_out_dir>
  <data_dir> holds team_games.csv, player_seasons.csv, analysis_summary.json
"""
import json
import sys
from pathlib import Path

import numpy as np
import pandas as pd

HOME_GAMES_PER_SEASON = 41
ALL = "All"
ALL_LABEL = "2023-24 to 2025-26"

data_dir, json_dir, csv_dir = (Path(p) for p in sys.argv[1:4])
json_dir.mkdir(parents=True, exist_ok=True)
csv_dir.mkdir(parents=True, exist_ok=True)

tg = pd.read_csv(data_dir / "team_games.csv", dtype={"game_id": str})
tg = tg[~tg.neutral_site].copy()
summary = json.loads((data_dir / "analysis_summary.json").read_text())
seasons = sorted(tg.season.unique())
names = tg.drop_duplicates("team").set_index("team").team_name.to_dict()
arena_by_season = tg[tg.role == "Home"].drop_duplicates(["season", "team"]).set_index(["season", "team"]).arena.to_dict()


def scoped(df: pd.DataFrame):
    """Yield (scope, rows) for each season and for all seasons pooled."""
    for s in seasons:
        yield s, df[df.season == s]
    yield ALL, df


def r4(x):
    return None if x is None or (isinstance(x, float) and np.isnan(x)) else round(float(x), 4)


def clock(minutes: float) -> str:
    """4.4 minutes -> '4:24' (game-clock style)."""
    sec = int(round(minutes * 60))
    return f"{sec // 60}:{sec % 60:02d}"


def ft_block(x: pd.DataFrame) -> dict:
    fta, ftm, xftm = int(x.q4_fta.sum()), int(x.q4_ftm.sum()), float(x.q4_xftm.sum())
    return {
        "games": int(len(x)), "q4_fta": fta, "q4_ftm": ftm, "q4_line": f"{ftm}/{fta}",
        "q4_ft_pct": r4(ftm / fta) if fta else None,
        "q4_xft_pct": r4(xftm / fta) if fta else None,
        "ftoe_pts": round(100 * (ftm - xftm) / fta, 2) if fta else None,
        "promos_any": int(x.promo_any.sum()), "rate_any": r4(x.promo_any.mean()),
        "promos_trip": int(x.promo_same_trip.sum()), "rate_trip": r4(x.promo_same_trip.mean()),
        "xpromos_any": round(float(x.promo_xprob.sum()), 1),
        "xpromos_trip": round(float(x.promo_same_trip_xprob.sum()), 1),
    }


away = tg[tg.role == "Away"]
home = tg[tg.role == "Home"]
out = {}

# ---- kpis: one row per season scope
rows = []
for scope, a in scoped(away):
    h = home[home.game_id.isin(a.game_id)]
    b = ft_block(a)
    hb = ft_block(h)
    rows.append({
        "season": scope, "season_label": ALL_LABEL if scope == ALL else scope,
        "seasons_count": len(seasons) if scope == ALL else 1,
        **{k: b[k] for k in ["games", "q4_fta", "q4_ftm", "q4_ft_pct", "promos_any", "rate_any", "promos_trip",
                             "rate_trip", "xpromos_any", "xpromos_trip"]},
        "home_q4_ft_pct": hb["q4_ft_pct"], "home_rate_any": hb["rate_any"], "home_rate_trip": hb["rate_trip"],
        "lift_any": r4(b["promos_any"] / b["xpromos_any"] - 1),
        "lift_trip": r4(b["promos_trip"] / b["xpromos_trip"] - 1),
        "home_games_per_season": HOME_GAMES_PER_SEASON,
        "nights_any": round(b["rate_any"] * HOME_GAMES_PER_SEASON, 1),
        "nights_trip": round(b["rate_trip"] * HOME_GAMES_PER_SEASON, 1),
        "median_min_left_any": r4(a.loc[a.promo_any, "promo_min_left"].median()),
        "median_min_left_trip": r4(a.loc[a.promo_same_trip, "promo_trip_min_left"].median()),
        "median_clock_any": clock(a.loc[a.promo_any, "promo_min_left"].median()),
        "median_clock_trip": clock(a.loc[a.promo_same_trip, "promo_trip_min_left"].median()),
    })
out["kpis"] = rows

# ---- visitors: one row per scope x visiting team
rows = []
for scope, a in scoped(away):
    h = home[home.season.isin(a.season.unique())]
    for team, x in a.groupby("team"):
        hb = ft_block(h[h.team == team])
        rows.append({"key": f"{scope}|{team}", "season": scope, "team": team, "team_name": names[team],
                     **ft_block(x), "home_q4_ft_pct": hb["q4_ft_pct"],
                     "home_rate_any": hb["rate_any"], "home_rate_trip": hb["rate_trip"]})
out["visitors"] = rows

# ---- arenas: one row per scope x home building
rows = []
for scope, a in scoped(away):
    for team, x in a.groupby("arena_home_team"):
        if scope == ALL:
            arenas = list(dict.fromkeys(arena_by_season[(s, team)] for s in reversed(seasons)))
            arena = arenas[0]
            note = "; ".join(f"{a} in {', '.join(s for s in seasons if arena_by_season[(s, team)] == a)}" for a in arenas[1:])
        else:
            arena, note = arena_by_season[(scope, team)], ""
        b = ft_block(x)
        rows.append({"key": f"{scope}|{team}", "season": scope, "home": team, "home_name": names[team],
                     "arena": arena, "arena_note": note, **b,
                     "xrate_any": r4(b["xpromos_any"] / b["games"]),
                     "xrate_trip": r4(b["xpromos_trip"] / b["games"]),
                     "nights_any": round(b["rate_any"] * HOME_GAMES_PER_SEASON, 1),
                     "nights_trip": round(b["rate_trip"] * HOME_GAMES_PER_SEASON, 1)})
out["arenas"] = rows

# ---- matchups: one row per scope x arena x visitor
rows = []
for scope, a in scoped(away):
    for (h_team, v_team), x in a.groupby(["arena_home_team", "team"]):
        b = ft_block(x)
        rows.append({"key": f"{scope}|{h_team}|{v_team}", "season": scope, "home": h_team, "team": v_team,
                     "team_name": names[v_team],
                     **{k: b[k] for k in ["games", "q4_fta", "q4_ftm", "q4_line", "q4_ft_pct",
                                          "promos_any", "rate_any", "promos_trip", "rate_trip"]}})
out["matchups"] = rows

# ---- games: visitor's 4th quarter, one row per game (for the matchup game log)
g = away.sort_values(["game_date", "game_id"])
out["games"] = [{
    "game_id": r.game_id, "season": r.season, "date": r.game_date, "home": r.arena_home_team, "team": r.team,
    "q4_line": f"{r.q4_ftm}/{r.q4_fta}", "q4_fta": int(r.q4_fta), "q4_ftm": int(r.q4_ftm),
    "promo_any": "Yes" if r.promo_any else "No", "promo_trip": "Yes" if r.promo_same_trip else "No",
    "min_left_any": r4(r.promo_min_left), "min_left_trip": r4(r.promo_trip_min_left),
    "shooters_any": r.promo_shooters if isinstance(r.promo_shooters, str) else "",
    "shooters_trip": r.promo_trip_shooters if isinstance(r.promo_trip_shooters, str) else "",
    "clock_any": clock(r.promo_min_left) if r.promo_any else "",
    "clock_trip": clock(r.promo_trip_min_left) if r.promo_same_trip else "",
    "margin_q3": int(r.margin_after_q3), "margin_final": int(r.margin_final),
} for r in g.itertuples()]

# ---- players: road 4th-quarter free throws by shooter
ps = pd.read_csv(data_dir / "player_seasons.csv")
rows = []
for scope in seasons + [ALL]:
    p = ps if scope == ALL else ps[ps.season == scope]
    p = p.sort_values("season")
    grp = p.groupby("personId")
    agg = grp.agg(player=("player_short", "last"), fta=("fta", "sum"), ftm=("ftm", "sum"),
                  road_q4_fta=("road_q4_fta", "sum"), road_q4_ftm=("road_q4_ftm", "sum"),
                  road_q4_xftm=("road_q4_xftm", "sum"),
                  promo_games_any=("road_promo_games", "sum"), promo_games_trip=("road_promo_games_trip", "sum"))
    agg["teams"] = grp.team.agg(lambda t: "/".join(dict.fromkeys(t)))
    agg = agg[agg.promo_games_any > 0]
    for pid, r in agg.iterrows():
        rows.append({"key": f"{scope}|{int(pid)}", "season": scope, "player": r.player, "teams": r.teams,
                     "road_q4_fta": int(r.road_q4_fta), "road_q4_ftm": int(r.road_q4_ftm),
                     "road_q4_line": f"{int(r.road_q4_ftm)}/{int(r.road_q4_fta)}",
                     "road_q4_ft_pct": r4(r.road_q4_ftm / r.road_q4_fta),
                     "season_ft_pct": r4(r.ftm / r.fta) if r.fta else None, "fta": int(r.fta),
                     "promo_games_any": int(r.promo_games_any), "promo_games_trip": int(r.promo_games_trip)})
out["players"] = rows

# ---- margin entering the 4th quarter
buckets = [(-100, -15, "Trailing by 15+"), (-15, -6, "Trailing by 6-14"), (-6, 5, "Within 5"),
           (5, 14, "Leading by 6-14"), (14, 100, "Leading by 15+")]
rows = []
for scope, a in scoped(away):
    for i, (lo, hi, label) in enumerate(buckets):
        x = a[(a.margin_after_q3 > lo) & (a.margin_after_q3 <= hi)]
        b = ft_block(x)
        rows.append({"key": f"{scope}|{i}", "season": scope, "order": i, "bucket": label, "games": b["games"],
                     "promos_any": b["promos_any"], "rate_any": b["rate_any"],
                     "promos_trip": b["promos_trip"], "rate_trip": b["rate_trip"],
                     "q4_fta_per_game": round(b["q4_fta"] / b["games"], 2), "q4_ft_pct": b["q4_ft_pct"]})
out["margin"] = rows

# ---- when the second miss happens (minutes left in the 4th)
rows = []
for scope, a in scoped(away):
    for m in range(12):
        n_any = int(((a.promo_min_left >= m) & (a.promo_min_left < m + 1) & a.promo_any).sum())
        n_trip = int(((a.promo_trip_min_left >= m) & (a.promo_trip_min_left < m + 1) & a.promo_same_trip).sum())
        if m == 11:  # include the 12:00 mark itself
            n_any += int(((a.promo_min_left == 12) & a.promo_any).sum())
            n_trip += int(((a.promo_trip_min_left == 12) & a.promo_same_trip).sum())
        rows.append({"key": f"{scope}|{m}", "season": scope, "min_left": m, "label": f"{m + 1}:00-{m}:00",
                     "promos_any": n_any, "promos_trip": n_trip})
out["timing"] = rows

# ---- predictability checks
rows = []
for i, y in enumerate(summary["team_yoy"], 1):
    tag = f"{y['from']} to {y['to']}"
    rows.append({"key": f"team_promo_{i}", "group": "Visiting team", "label": f"Road promo rate, {tag}",
                 "kind": "correlation", "value": y["road_promo_rate_r"]})
    rows.append({"key": f"team_ft_{i}", "group": "Visiting team", "label": f"Road free throw %, {tag}",
                 "kind": "correlation", "value": y["road_full_game_ft_pct_r"]})
for i, y in enumerate(summary["arena_dispersion"]["yoy"], 1):
    tag = f"{y['from']} to {y['to']}"
    rows.append({"key": f"arena_promo_{i}", "group": "Arena", "label": f"Visitor promo rate at arena, {tag}",
                 "kind": "correlation", "value": y["arena_promo_rate_r"]})
rows.append({"key": "arena_perm_promo", "group": "Arena", "label": "Arena promo rates vs. random shuffle",
             "kind": "p-value", "value": summary["arena_dispersion"]["perm_p_promo"]})
rows.append({"key": "arena_perm_ftoe", "group": "Arena", "label": "Arena FT% vs. expected, vs. random shuffle",
             "kind": "p-value", "value": summary["arena_dispersion"]["perm_p_ftoe"]})
rows.append({"key": "road_minus_home", "group": "Road effect", "label": "Same team, road minus home Q4 FT% vs. expected (pts)",
             "kind": "points", "value": summary["road_minus_home_ftoe_pts"]})
rows.append({"key": "road_minus_home_p", "group": "Road effect", "label": "Road vs. home difference, paired test",
             "kind": "p-value", "value": round(summary["road_minus_home_p"], 3)})
out["checks"] = rows

pred = summary["prediction"]
MODEL_KEYS = ["league", "ft", "ft_volume", "ft_volume_team", "ft_volume_team_arena", "live_margin"]
MODEL_LABELS = ["League average only", "Visitor FT%, last 40 games", "+ visitor 4th-quarter FT volume",
                "+ visitor road promo rate", "+ arena promo rate", "Live: + score after three quarters"]
rows = [{"key": k, "model": lbl, "auc": r["auc"], "brier_skill_pct": r["brier_skill_pct"],
         "kind": "live" if r["model"].startswith("live") else "pre-game",
         "n_train": pred["n_train"], "n_test": pred["n_test"]} for k, lbl, r in zip(MODEL_KEYS, MODEL_LABELS, pred["results"])]
rows.append({"key": "hindsight", "model": "who actually shot (hindsight)",
             "auc": pred["auc_shooter_sequence"], "brier_skill_pct": None, "kind": "reference",
             "n_train": pred["n_train"], "n_test": pred["n_test"]})
out["models"] = rows

JSON_DROP = {"games": {"min_left_any", "min_left_trip", "margin_final"}}
for name, rows in out.items():
    slim = [{k: v for k, v in r.items() if k not in JSON_DROP.get(name, set())} for r in rows]
    (json_dir / f"{name}.json").write_text(json.dumps(slim, separators=(",", ":"), allow_nan=False))
    pd.DataFrame(rows).to_csv(csv_dir / f"summary_{name}.csv", index=False)
    print(f"{name:10s} {len(rows):5d} rows  {(json_dir / f'{name}.json').stat().st_size / 1024:7.1f} KB")
