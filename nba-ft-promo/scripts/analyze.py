"""Summaries, significance checks and a first predictive test for the
Q4 free throw promo. Reads the CSVs written by build_dataset.py.

Usage: python analyze.py <data_dir>
"""
import json
import sys
from pathlib import Path

import numpy as np
import pandas as pd
from scipy import stats
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import brier_score_loss, log_loss, roc_auc_score

pd.set_option("display.width", 200)
pd.set_option("display.max_columns", 30)

d = Path(sys.argv[1])
tg = pd.read_csv(d / "team_games.csv", dtype={"game_id": str})
tg = tg[~tg.neutral_site].copy()
away = tg[tg.role == "Away"].copy()
home = tg[tg.role == "Home"].copy()
summary = {}


def agg(x: pd.DataFrame) -> pd.Series:
    fta, ftm, xftm = x.q4_fta.sum(), x.q4_ftm.sum(), x.q4_xftm.sum()
    var = (x.promo_xprob * (1 - x.promo_xprob)).sum()
    return pd.Series({
        "games": len(x), "q4_fta": fta, "q4_ftm": ftm,
        "q4_ft_pct": ftm / fta if fta else np.nan,
        "q4_xft_pct": xftm / fta if fta else np.nan,
        "ftoe_pts": 100 * (ftm - xftm) / fta if fta else np.nan,
        "ftoe_z": (ftm - xftm) / np.sqrt(max(fta * 0.78 * 0.22, 1e-9)),
        "promos": int(x.promo_any.sum()), "promo_rate": x.promo_any.mean(),
        "promo_same_trip_rate": x.promo_same_trip.mean(),
        "xpromos": x.promo_xprob.sum(), "promo_z": (x.promo_any.sum() - x.promo_xprob.sum()) / np.sqrt(max(var, 1e-9)),
    })


# ---------------------------------------------------------------- 1. home vs road
print("=" * 90, "\n1. HOME vs ROAD, Q4 (neutral sites excluded)")
hr = tg.groupby(["season", "role"]).apply(agg, include_groups=False)
print(hr[["games", "q4_fta", "q4_ft_pct", "q4_xft_pct", "ftoe_pts", "promos", "promo_rate", "xpromos", "promo_z"]].round(3))
hr_all = tg.groupby("role").apply(agg, include_groups=False)
print(hr_all[["games", "q4_fta", "q4_ft_pct", "q4_xft_pct", "ftoe_pts", "promos", "promo_rate", "xpromos", "promo_z"]].round(3))
summary["home_road"] = hr_all.round(4).to_dict(orient="index")

# Paired test: same team, road vs home Q4 FT over expected, per team-season.
ts = tg.groupby(["season", "team", "role"]).apply(agg, include_groups=False)["ftoe_pts"].unstack("role")
t = stats.ttest_rel(ts["Away"], ts["Home"])
print(f"Paired team-season FTOE road-home: mean diff {(ts.Away - ts.Home).mean():.2f} pts, t={t.statistic:.2f}, p={t.pvalue:.4f}, n={len(ts)}")
summary["road_minus_home_ftoe_pts"] = round(float((ts.Away - ts.Home).mean()), 2)
summary["road_minus_home_p"] = float(t.pvalue)

# ---------------------------------------------------------------- 2. worst visitors
print("=" * 90, "\n2. VISITING TEAMS, Q4 on the road")
vis_all = away.groupby("team").apply(agg, include_groups=False)
home_ft = home.groupby("team").apply(agg, include_groups=False)
vis_all["home_q4_ft_pct"] = home_ft.q4_ft_pct
vis_all["home_promo_rate"] = home_ft.promo_rate
print("Pooled 2023-24 to 2025-26, worst promo rate first:")
print(vis_all.sort_values("promo_rate", ascending=False)[["games", "q4_fta", "q4_ft_pct", "home_q4_ft_pct", "ftoe_pts", "promos", "promo_rate", "home_promo_rate", "xpromos"]].round(3).head(12))
vis_season = away.groupby(["season", "team"]).apply(agg, include_groups=False)
for s, x in vis_season.groupby(level=0):
    w = x.droplevel(0).sort_values("promo_rate", ascending=False)
    print(f"\n{s} worst 5 by promo rate:")
    print(w[["games", "q4_fta", "q4_ft_pct", "promos", "promo_rate"]].round(3).head(5))

# ---------------------------------------------------------------- 3. arenas
print("=" * 90, "\n3. ARENAS: how visitors shoot in Q4 at each home building")
ar = away.groupby("arena_home_team").apply(agg, include_groups=False)
print(ar.sort_values("promo_rate", ascending=False)[["games", "q4_fta", "q4_ft_pct", "q4_xft_pct", "ftoe_pts", "ftoe_z", "promos", "promo_rate", "xpromos", "promo_z"]].round(3))
chi_ftoe = float((ar.ftoe_z ** 2).sum())
chi_promo = float((ar.promo_z ** 2).sum())
p_ftoe = float(stats.chi2.sf(chi_ftoe, df=len(ar)))
p_promo = float(stats.chi2.sf(chi_promo, df=len(ar)))
print(f"Dispersion test across 30 arenas (is any arena different from expectation?)\n"
      f"  FT% over expected: chi2={chi_ftoe:.1f} on 30 df, p={p_ftoe:.3f}\n"
      f"  promos over expected: chi2={chi_promo:.1f} on 30 df, p={p_promo:.3f}")
ar_season = away.groupby(["season", "arena_home_team"]).apply(agg, include_groups=False)
piv = ar_season["ftoe_pts"].unstack("season")
piv_p = ar_season["promo_rate"].unstack("season")
seasons = list(piv.columns)
yoy = []
for a, b in zip(seasons, seasons[1:]):
    r1 = stats.pearsonr(piv[a], piv[b])
    r2 = stats.pearsonr(piv_p[a], piv_p[b])
    yoy.append({"from": a, "to": b, "arena_ftoe_r": round(r1.statistic, 3), "arena_ftoe_p": round(r1.pvalue, 3),
                "arena_promo_rate_r": round(r2.statistic, 3), "arena_promo_rate_p": round(r2.pvalue, 3)})
print("Year-over-year correlation of arena effects:", yoy)


# Permutation test: shuffle arena labels across visitor games (within season), which keeps
# within-game correlation intact. Statistic = spread of arena-level values around the mean.
def arena_spread(df: pd.DataFrame, labels: np.ndarray) -> tuple[float, float]:
    g = pd.DataFrame({"a": labels, "ftm": df.q4_ftm.to_numpy(), "xftm": df.q4_xftm.to_numpy(),
                      "fta": df.q4_fta.to_numpy(), "p": df.promo_any.to_numpy(dtype=float)}).groupby("a").sum()
    ftoe = (g.ftm - g.xftm) / g.fta
    w = g.fta / g.fta.sum()
    return float((w * (ftoe - (w * ftoe).sum()) ** 2).sum()), float(g.p.var())


rng = np.random.default_rng(7)
obs_ftoe, obs_promo = arena_spread(away, away.arena_home_team.to_numpy())
perm = []
labels = away.arena_home_team.to_numpy().copy()
season_idx = [np.flatnonzero(away.season.to_numpy() == s) for s in seasons]
for _ in range(2000):
    lab = labels.copy()
    for ix in season_idx:
        lab[ix] = rng.permutation(lab[ix])
    perm.append(arena_spread(away, lab))
perm = np.array(perm)
p_perm_ftoe = float((perm[:, 0] >= obs_ftoe).mean())
p_perm_promo = float((perm[:, 1] >= obs_promo).mean())
print(f"Permutation test (2,000 shuffles of arena labels across games):\n"
      f"  arena FT%-over-expected spread p={p_perm_ftoe:.3f}; arena promo-rate spread p={p_perm_promo:.3f}")
print("Houston (the most extreme arena) by season:")
print(ar_season.xs("HOU", level="arena_home_team")[["games", "q4_fta", "q4_ft_pct", "q4_xft_pct", "ftoe_pts", "promo_rate"]].round(3))
summary["arena_dispersion"] = {"chi2_ftoe": round(chi_ftoe, 1), "p_ftoe": round(p_ftoe, 3),
                               "chi2_promo": round(chi_promo, 1), "p_promo": round(p_promo, 3),
                               "perm_p_ftoe": round(p_perm_ftoe, 3), "perm_p_promo": round(p_perm_promo, 3),
                               "yoy": yoy}

# ---------------------------------------------------------------- 4. team stability
print("=" * 90, "\n4. Do visiting-team tendencies persist season to season?")
vp = vis_season["promo_rate"].unstack("season")
vf = vis_season["q4_ft_pct"].unstack("season")
full = away.groupby(["season", "team"]).apply(lambda x: x.ftm_game.sum() / x.fta_game.sum(), include_groups=False).unstack("season")
team_yoy = []
for a, b in zip(seasons, seasons[1:]):
    team_yoy.append({"from": a, "to": b,
                     "road_promo_rate_r": round(stats.pearsonr(vp[a], vp[b]).statistic, 3),
                     "road_q4_ft_pct_r": round(stats.pearsonr(vf[a], vf[b]).statistic, 3),
                     "road_full_game_ft_pct_r": round(stats.pearsonr(full[a], full[b]).statistic, 3)})
print(team_yoy)
summary["team_yoy"] = team_yoy

# ---------------------------------------------------------------- 5. visitor x arena
print("=" * 90, "\n5. Worst visitor at each arena (pooled, >= 15 Q4 FTA)")
mx = away.groupby(["arena_home_team", "team"]).apply(agg, include_groups=False).reset_index()
mx15 = mx[mx.q4_fta >= 15]
worst = mx15.sort_values(["arena_home_team", "q4_ft_pct"]).groupby("arena_home_team").head(1)
print(worst[["arena_home_team", "team", "games", "q4_fta", "q4_ftm", "q4_ft_pct", "promos", "promo_rate"]].round(3).to_string(index=False))
print("\nMost promos by a single visitor at one arena (pooled):")
print(mx.sort_values(["promos", "promo_rate"], ascending=False)[["arena_home_team", "team", "games", "q4_fta", "q4_ft_pct", "promos", "promo_rate"]].head(12).round(3).to_string(index=False))
print(f"Pairs: {len(mx)}; median games per pair {mx.games.median():.0f}; median Q4 FTA per pair {mx.q4_fta.median():.0f}")

# ---------------------------------------------------------------- 6. game context
print("=" * 90, "\n6. Game context: visitor margin entering the 4th")
away["q3_bucket"] = pd.cut(away.margin_after_q3, [-100, -15, -6, 5, 14, 100],
                           labels=["Trailing 15+", "Trailing 6-14", "Within 5", "Leading 6-14", "Leading 15+"])
ctx = away.groupby("q3_bucket", observed=True).agg(games=("promo_any", "size"), promo_rate=("promo_any", "mean"),
                                                    q4_fta=("q4_fta", "mean"), ft_pct=("q4_ftm", "sum"))
ctx["ft_pct"] = ctx.ft_pct / away.groupby("q3_bucket", observed=True).q4_fta.sum()
print(ctx.round(3))
summary["context"] = ctx.round(4).reset_index().astype({"q3_bucket": str}).to_dict(orient="records")
timing = away.loc[away.promo_any, "promo_min_left"]
summary["timing_quartiles_min_left"] = timing.quantile([.25, .5, .75]).round(2).tolist()
print("Promo timing, minutes left in Q4 (25/50/75%):", summary["timing_quartiles_min_left"])

# ---------------------------------------------------------------- 7. predictive test
print("=" * 90, "\n7. Can we predict it? Pre-game features from each team's trailing games")
tg_sorted = tg.sort_values(["game_date", "game_id"]).copy()


def trailing(df: pd.DataFrame, key: str, cols: list[str], n: int) -> pd.DataFrame:
    """Sum of cols over the previous n rows of the same key (no leakage)."""
    g = df.groupby(key)[cols]
    return g.transform(lambda s: s.shift(1).rolling(n, min_periods=10).sum())


# Visitor skill from its last 40 games anywhere (crosses season boundaries).
roll = trailing(tg_sorted, "team", ["fta_game", "ftm_game", "q4_fta", "q4_ftm"], 40)
tg_sorted[["t_fta", "t_ftm", "t_q4fta", "t_q4ftm"]] = roll.to_numpy()
tg_sorted["t_promo"] = tg_sorted.groupby(["team", "role"])["promo_any"].transform(
    lambda s: s.astype(float).shift(1).rolling(40, min_periods=10).mean())
# Arena: visitors' promo rate in the arena's previous 60 home games.
aw = tg_sorted[tg_sorted.role == "Away"].copy()
aw["arena_promo_prev"] = aw.groupby("arena_home_team")["promo_any"].transform(
    lambda s: s.astype(float).shift(1).rolling(60, min_periods=20).mean())
aw["ft_pct_trail"] = aw.t_ftm / aw.t_fta
aw["q4_fta_trail"] = aw.t_q4fta / 40
aw["abs_margin_q3"] = aw.margin_after_q3.abs()
aw["y"] = aw.promo_any.astype(int)
feat_sets = {
    "league average only": [],
    "visitor FT% (last 40 g)": ["ft_pct_trail"],
    "visitor FT% + Q4 FT volume": ["ft_pct_trail", "q4_fta_trail"],
    "+ visitor road promo rate": ["ft_pct_trail", "q4_fta_trail", "t_promo"],
    "+ arena promo rate": ["ft_pct_trail", "q4_fta_trail", "t_promo", "arena_promo_prev"],
    "live: + score margin after Q3": ["ft_pct_trail", "q4_fta_trail", "margin_after_q3", "abs_margin_q3"],
}
data = aw.dropna(subset=["ft_pct_trail", "q4_fta_trail", "t_promo", "arena_promo_prev"])
train = data[data.season != "2025-26"]
test = data[data.season == "2025-26"]
results = []
base_p = train.y.mean()
for name, cols in feat_sets.items():
    if cols:
        m = LogisticRegression(C=1.0).fit(train[cols], train.y)
        p = m.predict_proba(test[cols])[:, 1]
    else:
        p = np.full(len(test), base_p)
    res = {"model": name, "auc": round(roc_auc_score(test.y, p), 3) if cols else 0.5,
           "brier": round(brier_score_loss(test.y, p), 4), "log_loss": round(log_loss(test.y, p), 4)}
    results.append(res)
base_brier = results[0]["brier"]
for r in results:
    r["brier_skill_pct"] = round(100 * (1 - r["brier"] / base_brier), 2)
pred = pd.DataFrame(results)
print(f"train 2023-25 n={len(train)}, test 2025-26 n={len(test)}; test promo rate {test.y.mean():.3f}")
print(pred.to_string(index=False))
summary["prediction"] = {"train": "2023-24 + 2024-25", "test": "2025-26", "n_train": len(train), "n_test": len(test),
                         "test_rate": round(float(test.y.mean()), 4), "results": results}
# Shooter-sequence expectation is the ceiling for pre-game info about who shoots.
print("Reference (uses who actually shot in Q4, not pre-game): AUC of expected-prob model",
      round(roc_auc_score(test.y, test.promo_xprob), 3))
summary["prediction"]["auc_shooter_sequence"] = round(float(roc_auc_score(test.y, test.promo_xprob)), 3)

(d / "analysis_summary.json").write_text(json.dumps(summary, indent=2, default=float))
print("\nwrote", d / "analysis_summary.json")
