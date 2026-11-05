"""Pre-game chance that the visiting team sets off the promo (one player misses two
free throws in a row on the same 4th-quarter trip), backtested and applied to the
upcoming schedule.

Model, per visiting player j who has been playing:
    trips_j  expected 4th-quarter multi-shot trips per game (this season, blended with last)
    miss_j   1 - FT% (this season plus last, pulled toward league average)
    avail_j  share of the team's last three games he played in
Expected two-miss trips  L = opp_H * sum_j avail_j * trips_j * h(miss_j),  h(q) = q^2 (two-shot trip)
or 2q^2 - q^3 (three-shot), where opp_H is how often the home team sends visitors to the line
in the 4th, relative to the league. The raw chance 1 - exp(-L) is then calibrated with a
logistic fit on log(L) from backtest seasons.

Usage:
  python predict.py <out_dir> --history NBA_BUILD_DIR --prior ESPN_PREV_DIR --current ESPN_CUR_DIR
                    --schedule nba_schedule_<year>.parquet [--after 2026-11-05T00:00Z]
Scores scheduled games that start after --after (default: now).
"""
import argparse
import json
from pathlib import Path
from zoneinfo import ZoneInfo

import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import brier_score_loss, log_loss, roc_auc_score

K_FT = 20       # attempts of league-average shooting added to each player's free throw line
M_TRIPS = 10    # games of last season's trip rate blended into this season's
N_OPP = 15      # games of league-average fouling blended into each opponent's
LAST_N = 3      # recent team games used to judge who is available
ROOKIE_TRIP_SHARE = 0.7  # players without a prior season start at this share of the league trip rate
ESPN_TO_NBA = {"GS": "GSW", "NO": "NOP", "NY": "NYK", "SA": "SAS", "UTAH": "UTA", "WSH": "WAS"}


def h(q: np.ndarray, w3: float) -> np.ndarray:
    """Chance that one trip has two straight misses, for miss chance q."""
    return (1 - w3) * q ** 2 + w3 * (2 * q ** 2 - q ** 3)


def prior_table(pg: pd.DataFrame) -> pd.DataFrame:
    """Last season's line per player: free throws, 4th-quarter trips and games played."""
    return pg.groupby("personId").agg(p_fta=("fta", "sum"), p_ftm=("ftm", "sum"), p_trips=("q4_trips", "sum"),
                                      p_games=("game_id", "nunique"))


def constants(pg: pd.DataFrame, tg: pd.DataFrame) -> dict:
    return {"lg_ft": pg.ftm.sum() / pg.fta.sum(),
            "lg_trip_app": pg.q4_trips.sum() / len(pg),
            "lg_trips_team": tg.q4_trips.mean(),
            "w3": pg.q4_trips3.sum() / max(1, pg.q4_trips.sum())}


def snapshot(cur_pg: pd.DataFrame, cur_tg: pd.DataFrame, prior: pd.DataFrame, prior_pg: pd.DataFrame, c: dict):
    """Player skill, availability and opponent factors from games before the slate."""
    cur = cur_pg.groupby("personId").agg(c_fta=("fta", "sum"), c_ftm=("ftm", "sum"), c_trips=("q4_trips", "sum"),
                                         c_games=("game_id", "nunique"), name=("player_short", "last"))
    pl = cur.join(prior, how="outer").fillna({"c_fta": 0, "c_ftm": 0, "c_trips": 0, "c_games": 0,
                                              "p_fta": 0, "p_ftm": 0, "p_trips": 0, "p_games": 0})
    pl["ft"] = (pl.c_ftm + pl.p_ftm + K_FT * c["lg_ft"]) / (pl.c_fta + pl.p_fta + K_FT * 1.0)
    prior_rate = np.where(pl.p_games >= 5, pl.p_trips / pl.p_games.clip(lower=1), ROOKIE_TRIP_SHARE * c["lg_trip_app"])
    pl["trips"] = (pl.c_trips + M_TRIPS * prior_rate) / (pl.c_games + M_TRIPS)
    pl["h"] = h(1 - pl.ft.to_numpy(), c["w3"])

    # Availability: share of each team's last LAST_N games a player appeared in.
    avail = {}
    if len(cur_tg):
        last = (cur_tg.sort_values(["game_date", "game_id"]).groupby("team").tail(LAST_N)[["team", "game_id"]])
        n_last = last.groupby("team").size()
        seen = cur_pg.merge(last, on=["team", "game_id"])
        cnt = seen.groupby(["team", "personId"]).size()
        share = cnt / cnt.index.get_level_values("team").map(n_last).to_numpy()
        for (team, pid), a in share.items():
            avail.setdefault(team, {})[pid] = float(a)
    # Teams with no games yet: last season's regular rotation.
    pri_roster = prior_pg.groupby(["team", "personId"]).size()
    fallback = {}
    for (team, pid), n in pri_roster.items():
        if n >= 20:
            fallback.setdefault(team, {})[pid] = 1.0

    # Opponent factor: visitors' (and any opponent's) 4th-quarter trips against each team.
    allowed = cur_tg.groupby("opponent").agg(trips=("q4_trips", "sum"), games=("game_id", "nunique"))
    L = c["lg_trips_team"]
    opp = ((allowed.trips + N_OPP * L) / (allowed.games + N_OPP) / L).to_dict()
    names = pl.name.dropna().to_dict()
    return pl, avail, fallback, opp, names


def score(slate: pd.DataFrame, pl, avail, fallback, opp, names) -> pd.DataFrame:
    rows = []
    for g in slate.itertuples():
        roster = avail.get(g.away) or fallback.get(g.away, {})
        pids = [p for p in roster if p in pl.index]
        a = np.array([roster[p] for p in pids])
        sub = pl.loc[pids]
        contrib = a * sub.trips.to_numpy() * sub.h.to_numpy()
        o = opp.get(g.home, 1.0)
        lam_no_opp = float(contrib.sum())
        order = np.argsort(-contrib)[:3]
        top = [{"personId": int(pids[i]), "player": names.get(pids[i], ""), "ft": round(float(sub.ft.iloc[i]), 4),
                "trips": round(float(a[i] * sub.trips.iloc[i] * o), 3), "share": round(float(contrib[i] / max(lam_no_opp, 1e-9)), 3)}
               for i in order if contrib[i] > 0]
        rows.append({"game_id": g.game_id, "lam_no_opp": lam_no_opp, "lam": lam_no_opp * o, "opp": o,
                     "exp_trips": float((a * sub.trips.to_numpy()).sum() * o),
                     "team_miss": float(np.average(1 - sub.ft.to_numpy(), weights=np.maximum(a * sub.trips.to_numpy(), 1e-9))) if len(pids) else np.nan,
                     "top": top})
    return pd.DataFrame(rows)


def backtest(season: str, prev: str, pg: pd.DataFrame, tg: pd.DataFrame) -> pd.DataFrame:
    """Score every game of `season` using only games before its date (plus all of `prev`)."""
    prior_pg = pg[pg.season == prev]
    prior = prior_table(prior_pg)
    c = constants(prior_pg, tg[tg.season == prev])
    spg, stg = pg[pg.season == season], tg[tg.season == season]
    visitors = stg[(stg.role == "Away") & ~stg.neutral_site]
    out = []
    for d, slate in visitors.groupby("game_date"):
        snap = snapshot(spg[spg.game_date < d], stg[stg.game_date < d], prior, prior_pg, c)
        sc = score(slate.rename(columns={"team": "away", "opponent": "home"}), *snap)
        sc = sc.merge(slate[["game_id", "game_date", "team", "opponent", "promo"]], on="game_id")
        # Baseline: visitor's season-to-date road promo rate, shrunk to last season's league rate.
        past = stg[(stg.game_date < d) & (stg.role == "Away") & ~stg.neutral_site]
        base = tg[(tg.season == prev) & (tg.role == "Away") & ~tg.neutral_site].promo.mean()
        tr = past.groupby("team").promo.agg(["sum", "count"])
        sc["team_rate"] = sc.team.map(lambda t: (tr["sum"].get(t, 0) + 20 * base) / (tr["count"].get(t, 0) + 20))
        out.append(sc)
    res = pd.concat(out, ignore_index=True)
    res["season"] = season
    return res


def fit_calibration(df: pd.DataFrame, col: str = "lam"):
    m = LogisticRegression(C=1e6).fit(np.log(df[[col]].clip(lower=1e-6)), df.promo.astype(int))
    return m


def evaluate(train: pd.DataFrame, test: pd.DataFrame) -> tuple[list, list, LogisticRegression]:
    y = test.promo.astype(int).to_numpy()
    base = train.promo.mean()
    preds = {"League average": np.full(len(test), base)}
    m_team = LogisticRegression(C=1e6).fit(train[["team_rate"]], train.promo.astype(int))
    preds["Visitor's promo rate so far"] = m_team.predict_proba(test[["team_rate"]])[:, 1]
    m_noopp = fit_calibration(train, "lam_no_opp")
    preds["Players: trips x miss chance"] = m_noopp.predict_proba(np.log(test[["lam_no_opp"]].clip(lower=1e-6)))[:, 1]
    m_full = fit_calibration(train, "lam")
    preds["Players + home team's fouling"] = m_full.predict_proba(np.log(test[["lam"]].clip(lower=1e-6)))[:, 1]
    results = []
    b0 = brier_score_loss(y, preds["League average"])
    for k, p in preds.items():
        results.append({"model": k, "auc": round(roc_auc_score(y, p), 3) if k != "League average" else 0.5,
                        "brier_skill_pct": round(100 * (1 - brier_score_loss(y, p) / b0), 2),
                        "log_loss": round(log_loss(y, p), 4)})
    p = preds["Players + home team's fouling"]
    test = test.assign(p=p)
    test["bin"] = pd.qcut(test.p.rank(method="first"), 5, labels=False)
    bins = [{"bin": int(b), "label": lbl, "games": int(len(x)), "predicted": round(float(x.p.mean()), 4),
             "actual": round(float(x.promo.mean()), 4), "promos": int(x.promo.sum())}
            for (b, x), lbl in zip(test.groupby("bin"), ["Lowest fifth", "Second", "Middle", "Fourth", "Highest fifth"])]
    return results, bins, m_full


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("out")
    ap.add_argument("--history", required=True)
    ap.add_argument("--prior", required=True)
    ap.add_argument("--current", required=True)
    ap.add_argument("--schedule", required=True)
    ap.add_argument("--after", default=None, help="UTC time; only games starting later are scored (default now)")
    a = ap.parse_args()
    out = Path(a.out)
    out.mkdir(parents=True, exist_ok=True)

    # ---- backtest on the NBA-feed seasons
    hpg = pd.read_csv(Path(a.history) / "player_games.csv", dtype={"game_id": str})
    htg = pd.read_csv(Path(a.history) / "team_games.csv", dtype={"game_id": str})
    bt24 = backtest("2024-25", "2023-24", hpg, htg)
    bt25 = backtest("2025-26", "2024-25", hpg, htg)
    results, bins, _ = evaluate(bt24, bt25)
    print(pd.DataFrame(results).to_string(index=False))
    print(pd.DataFrame(bins).to_string(index=False))
    both = pd.concat([bt24, bt25])
    raw_p = 1 - np.exp(-both.lam)
    print(f"raw Poisson chance: mean {raw_p.mean():.4f} vs actual {both.promo.mean():.4f}")
    calib = fit_calibration(both, "lam")
    print("calibration on both seasons: intercept", calib.intercept_[0].round(3), "slope", calib.coef_[0][0].round(3))

    # ---- 2026-27: snapshot from games so far, applied to every remaining game
    ppg = pd.read_csv(Path(a.prior) / "player_games.csv", dtype={"game_id": str})
    ptg = pd.read_csv(Path(a.prior) / "team_games.csv", dtype={"game_id": str})
    cpg = pd.read_csv(Path(a.current) / "player_games.csv", dtype={"game_id": str})
    ctg = pd.read_csv(Path(a.current) / "team_games.csv", dtype={"game_id": str})
    c = constants(ppg, ptg)
    snap = snapshot(cpg, ctg, prior_table(ppg), ppg, c)
    sch = pd.read_parquet(a.schedule)
    sch = sch[(sch.season_type == 2) & (sch.status_type_name == "STATUS_SCHEDULED") & ~sch.neutral_site]
    sch["home"] = sch.home_abbreviation.map(lambda x: ESPN_TO_NBA.get(x, x))
    sch["away"] = sch.away_abbreviation.map(lambda x: ESPN_TO_NBA.get(x, x))
    sch = sch[(sch.home != "TBD") & (sch.away != "TBD")]
    after = pd.Timestamp(a.after, tz="UTC") if a.after else pd.Timestamp.now(tz="UTC")
    start = pd.to_datetime(sch.date, utc=True)
    et = start.dt.tz_convert(ZoneInfo("America/New_York"))
    sch["date_et"] = et.dt.strftime("%Y-%m-%d")
    sch["time_et"] = et.dt.strftime("%-I:%M %p")
    sch["start_utc"] = start.dt.strftime("%Y-%m-%dT%H:%MZ")
    sch = sch[start > after].copy()
    sch["game_id"] = sch.game_id.astype(str)
    sc = score(sch[["game_id", "home", "away"]], *snap)
    sc["prob"] = calib.predict_proba(np.log(sc[["lam"]].clip(lower=1e-6)))[:, 1]
    up = sch[["game_id", "start_utc", "date_et", "time_et", "home", "away", "venue_full_name", "notes_headline"]].merge(sc, on="game_id")
    up = up.sort_values(["start_utc", "game_id"])
    up.to_json(out / "upcoming_raw.json", orient="records")
    flat = up.drop(columns=["top"]).copy()
    for i in range(3):
        flat[f"shooter_{i + 1}"] = up.top.map(lambda t: t[i]["player"] if len(t) > i else "")
        flat[f"shooter_{i + 1}_ft_pct"] = up.top.map(lambda t: t[i]["ft"] if len(t) > i else None)
        flat[f"shooter_{i + 1}_risk_share"] = up.top.map(lambda t: t[i]["share"] if len(t) > i else None)
    flat.rename(columns={"venue_full_name": "arena", "prob": "promo_chance", "exp_trips": "expected_q4_trips",
                         "team_miss": "visitor_miss_rate", "opp": "home_fouling_factor"}).round(4).to_csv(out / "upcoming_predictions.csv", index=False)
    bt = pd.concat([bt24, bt25]).drop(columns=["top"])
    bt.to_csv(out / "backtest.csv", index=False)
    meta = {"results": results, "bins": bins, "calibration": {"intercept": float(calib.intercept_[0]), "slope": float(calib.coef_[0][0])},
            "constants_2026_27": {k: float(v) for k, v in c.items()},
            "data_through": str(ctg.game_date.max()), "games_so_far": int(ctg.game_id.nunique()),
            "scored_after_utc": after.strftime("%Y-%m-%dT%H:%MZ"),
            "train": "2024-25", "test": "2025-26", "n_test": int(len(bt25)), "n_train": int(len(bt24)),
            "test_rate": float(bt25.promo.mean())}
    (out / "model_meta.json").write_text(json.dumps(meta, indent=2))
    print(f"scored {len(up)} upcoming games from {up.date_et.min()} to {up.date_et.max()}; mean chance {up.prob.mean():.3f}")
    print(up.sort_values("prob", ascending=False).head(12)[["date_et", "away", "home", "prob", "exp_trips", "team_miss", "opp"]].round(3).to_string(index=False))


if __name__ == "__main__":
    main()
