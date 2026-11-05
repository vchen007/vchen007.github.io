"""Rankings, significance checks and season-to-season stability for the promo
(one visiting player misses two free throws in a row on the same 4th-quarter trip).
Reads team_games.csv written by build_dataset.py / combine.py. Tests use complete
seasons only; the prediction model lives in predict.py.

Usage: python analyze.py <data_dir>
"""
import json
import sys
from pathlib import Path

import numpy as np
import pandas as pd
from scipy import stats

pd.set_option("display.width", 200)
pd.set_option("display.max_columns", 30)
COMPLETE = ["2023-24", "2024-25", "2025-26"]

d = Path(sys.argv[1])
tg = pd.read_csv(d / "team_games.csv", dtype={"game_id": str})
tg = tg[~tg.neutral_site & tg.season.isin(COMPLETE)].copy()
away, home = tg[tg.role == "Away"].copy(), tg[tg.role == "Home"].copy()
summary = {"seasons": COMPLETE}


def agg(x: pd.DataFrame) -> pd.Series:
    fta, ftm, xftm = x.q4_fta.sum(), x.q4_ftm.sum(), x.q4_xftm.sum()
    var = (x.promo_xprob * (1 - x.promo_xprob)).sum()
    return pd.Series({
        "games": len(x), "q4_fta": fta, "q4_ft_pct": ftm / fta if fta else np.nan,
        "q4_xft_pct": xftm / fta if fta else np.nan, "ftoe_pts": 100 * (ftm - xftm) / fta if fta else np.nan,
        "promos": int(x.promo.sum()), "promo_rate": x.promo.mean(), "xpromos": x.promo_xprob.sum(),
        "promo_z": (x.promo.sum() - x.promo_xprob.sum()) / np.sqrt(max(var, 1e-9)),
    })


print("=" * 90, "\n1. HOME vs ROAD, 4th quarter")
hr_all = tg.groupby("role").apply(agg, include_groups=False)
print(tg.groupby(["season", "role"]).apply(agg, include_groups=False).round(3))
print(hr_all.round(3))
summary["home_road"] = hr_all.round(4).to_dict(orient="index")
ts = tg.groupby(["season", "team", "role"]).apply(agg, include_groups=False)["ftoe_pts"].unstack("role")
t = stats.ttest_rel(ts["Away"], ts["Home"])
print(f"Paired team-season FT% vs expected, road minus home: {(ts.Away - ts.Home).mean():.2f} pts, p={t.pvalue:.4f}")
summary["road_minus_home_ftoe_pts"] = round(float((ts.Away - ts.Home).mean()), 2)
summary["road_minus_home_p"] = float(t.pvalue)

print("=" * 90, "\n2. VISITING TEAMS on the road")
vis_all = away.groupby("team").apply(agg, include_groups=False)
print(vis_all.sort_values("promo_rate", ascending=False).head(10).round(3))
vis_season = away.groupby(["season", "team"]).apply(agg, include_groups=False)

print("=" * 90, "\n3. ARENAS")
ar = away.groupby("arena_home_team").apply(agg, include_groups=False)
print(ar.sort_values("promo_rate", ascending=False).round(3))
ar_season = away.groupby(["season", "arena_home_team"]).apply(agg, include_groups=False)
piv_f, piv_p = ar_season["ftoe_pts"].unstack("season"), ar_season["promo_rate"].unstack("season")
yoy = []
for a, b in zip(COMPLETE, COMPLETE[1:]):
    yoy.append({"from": a, "to": b, "arena_ftoe_r": round(float(stats.pearsonr(piv_f[a], piv_f[b]).statistic), 3),
                "arena_promo_rate_r": round(float(stats.pearsonr(piv_p[a], piv_p[b]).statistic), 3)})
print("Year-over-year correlation of arena effects:", yoy)


def arena_spread(df: pd.DataFrame, labels: np.ndarray) -> tuple[float, float]:
    g = pd.DataFrame({"a": labels, "ftm": df.q4_ftm.to_numpy(), "xftm": df.q4_xftm.to_numpy(),
                      "fta": df.q4_fta.to_numpy(), "p": df.promo.to_numpy(dtype=float)}).groupby("a").sum()
    ftoe = (g.ftm - g.xftm) / g.fta
    w = g.fta / g.fta.sum()
    return float((w * (ftoe - (w * ftoe).sum()) ** 2).sum()), float(g.p.var())


rng = np.random.default_rng(7)
obs = arena_spread(away, away.arena_home_team.to_numpy())
labels = away.arena_home_team.to_numpy().copy()
idx = [np.flatnonzero(away.season.to_numpy() == s) for s in COMPLETE]
perm = []
for _ in range(2000):
    lab = labels.copy()
    for ix in idx:
        lab[ix] = rng.permutation(lab[ix])
    perm.append(arena_spread(away, lab))
perm = np.array(perm)
p_ftoe, p_promo = float((perm[:, 0] >= obs[0]).mean()), float((perm[:, 1] >= obs[1]).mean())
print(f"Permutation test: arena FT%-vs-expected spread p={p_ftoe:.3f}; arena promo-rate spread p={p_promo:.3f}")
summary["arena_dispersion"] = {"perm_p_ftoe": round(p_ftoe, 3), "perm_p_promo": round(p_promo, 3), "yoy": yoy}

print("=" * 90, "\n4. Stability of visiting-team tendencies")
vp, vf = vis_season["promo_rate"].unstack("season"), vis_season["q4_ft_pct"].unstack("season")
full = away.groupby(["season", "team"]).apply(lambda x: x.ftm_game.sum() / x.fta_game.sum(), include_groups=False).unstack("season")
team_yoy = []
for a, b in zip(COMPLETE, COMPLETE[1:]):
    team_yoy.append({"from": a, "to": b, "road_promo_rate_r": round(float(stats.pearsonr(vp[a], vp[b]).statistic), 3),
                     "road_q4_ft_pct_r": round(float(stats.pearsonr(vf[a], vf[b]).statistic), 3),
                     "road_full_game_ft_pct_r": round(float(stats.pearsonr(full[a], full[b]).statistic), 3)})
print(team_yoy)
summary["team_yoy"] = team_yoy

print("=" * 90, "\n5. Visitor at each arena")
mx = away.groupby(["arena_home_team", "team"]).apply(agg, include_groups=False).reset_index()
print(mx.sort_values(["promos", "promo_rate"], ascending=False).head(10)[["arena_home_team", "team", "games", "promos", "promo_rate", "q4_ft_pct"]].round(3).to_string(index=False))
print(f"Pairs: {len(mx)}; median games per pair {mx.games.median():.0f}")

print("=" * 90, "\n6. Game context")
away["q3_bucket"] = pd.cut(away.margin_after_q3, [-100, -15, -6, 5, 14, 100],
                           labels=["Trailing 15+", "Trailing 6-14", "Within 5", "Leading 6-14", "Leading 15+"])
print(away.groupby("q3_bucket", observed=True).agg(games=("promo", "size"), promo_rate=("promo", "mean"), q4_fta=("q4_fta", "mean")).round(3))
summary["timing_quartiles_min_left"] = away.loc[away.promo, "promo_min_left"].quantile([.25, .5, .75]).round(2).tolist()
print("Promo timing, minutes left (25/50/75%):", summary["timing_quartiles_min_left"])

(d / "analysis_summary.json").write_text(json.dumps(summary, indent=2, default=float))
print("\nwrote", d / "analysis_summary.json")
