"""Build game-level and attempt-level datasets for the "visiting team misses two
free throws in a row in the 4th quarter" chicken-sandwich promotion.

Input : NBA live-data (cdn.nba.com) play-by-play CSVs, one per season, as
        packaged by github.com/shufinskiy/nba_data (cdnnba_<startyear>.csv).
Output: CSVs in <out_dir>, shaped for Tableau.

Usage : python build_dataset.py <out_dir> <cdnnba_2023.csv> [<cdnnba_2024.csv> ...]
"""
import sys
from pathlib import Path

import numpy as np
import pandas as pd

# --------------------------------------------------------------------------
# Reference data
# --------------------------------------------------------------------------
TEAMS = {
    # tricode: (team name, home arena 2025-26 name, city)
    "ATL": ("Atlanta Hawks", "State Farm Arena", "Atlanta"),
    "BOS": ("Boston Celtics", "TD Garden", "Boston"),
    "BKN": ("Brooklyn Nets", "Barclays Center", "Brooklyn"),
    "CHA": ("Charlotte Hornets", "Spectrum Center", "Charlotte"),
    "CHI": ("Chicago Bulls", "United Center", "Chicago"),
    "CLE": ("Cleveland Cavaliers", "Rocket Arena", "Cleveland"),
    "DAL": ("Dallas Mavericks", "American Airlines Center", "Dallas"),
    "DEN": ("Denver Nuggets", "Ball Arena", "Denver"),
    "DET": ("Detroit Pistons", "Little Caesars Arena", "Detroit"),
    "GSW": ("Golden State Warriors", "Chase Center", "San Francisco"),
    "HOU": ("Houston Rockets", "Toyota Center", "Houston"),
    "IND": ("Indiana Pacers", "Gainbridge Fieldhouse", "Indianapolis"),
    "LAC": ("LA Clippers", "Intuit Dome", "Inglewood"),
    "LAL": ("Los Angeles Lakers", "Crypto.com Arena", "Los Angeles"),
    "MEM": ("Memphis Grizzlies", "FedExForum", "Memphis"),
    "MIA": ("Miami Heat", "Kaseya Center", "Miami"),
    "MIL": ("Milwaukee Bucks", "Fiserv Forum", "Milwaukee"),
    "MIN": ("Minnesota Timberwolves", "Target Center", "Minneapolis"),
    "NOP": ("New Orleans Pelicans", "Smoothie King Center", "New Orleans"),
    "NYK": ("New York Knicks", "Madison Square Garden", "New York"),
    "OKC": ("Oklahoma City Thunder", "Paycom Center", "Oklahoma City"),
    "ORL": ("Orlando Magic", "Kia Center", "Orlando"),
    "PHI": ("Philadelphia 76ers", "Xfinity Mobile Arena", "Philadelphia"),
    "PHX": ("Phoenix Suns", "Mortgage Matchup Center", "Phoenix"),
    "POR": ("Portland Trail Blazers", "Moda Center", "Portland"),
    "SAC": ("Sacramento Kings", "Golden 1 Center", "Sacramento"),
    "SAS": ("San Antonio Spurs", "Frost Bank Center", "San Antonio"),
    "TOR": ("Toronto Raptors", "Scotiabank Arena", "Toronto"),
    "UTA": ("Utah Jazz", "Delta Center", "Salt Lake City"),
    "WAS": ("Washington Wizards", "Capital One Arena", "Washington"),
}

# The Clippers played at Crypto.com Arena until Intuit Dome opened in 2024-25.
ARENA_BY_SEASON_OVERRIDE = {("LAC", "2023-24"): "Crypto.com Arena"}

# Regular-season games played at neutral sites (no real home crowd).
# Keyed by (local game date, frozenset of the two teams).
NEUTRAL_SITES = {
    ("2023-11-09", frozenset({"ATL", "ORL"})): "Arena CDMX, Mexico City",
    ("2023-12-07", frozenset({"IND", "MIL"})): "T-Mobile Arena, Las Vegas (In-Season Tournament semifinal)",
    ("2023-12-07", frozenset({"LAL", "NOP"})): "T-Mobile Arena, Las Vegas (In-Season Tournament semifinal)",
    ("2024-01-11", frozenset({"BKN", "CLE"})): "Accor Arena, Paris",
    ("2024-11-02", frozenset({"MIA", "WAS"})): "Arena CDMX, Mexico City",
    ("2024-12-14", frozenset({"MIL", "ATL"})): "T-Mobile Arena, Las Vegas (NBA Cup semifinal)",
    ("2024-12-14", frozenset({"OKC", "HOU"})): "T-Mobile Arena, Las Vegas (NBA Cup semifinal)",
    ("2025-01-23", frozenset({"SAS", "IND"})): "Accor Arena, Paris",
    ("2025-01-25", frozenset({"SAS", "IND"})): "Accor Arena, Paris",
    ("2025-11-01", frozenset({"DET", "DAL"})): "Arena CDMX, Mexico City",
    ("2025-12-13", frozenset({"NYK", "ORL"})): "T-Mobile Arena, Las Vegas (NBA Cup semifinal)",
    ("2025-12-13", frozenset({"SAS", "OKC"})): "T-Mobile Arena, Las Vegas (NBA Cup semifinal)",
    ("2026-01-15", frozenset({"ORL", "MEM"})): "Uber Arena, Berlin",
    ("2026-01-18", frozenset({"ORL", "MEM"})): "The O2, London",
}

COLS = ["gameId", "actionNumber", "orderNumber", "clock", "timeActual", "period",
        "periodType", "actionType", "subType", "teamTricode", "personId",
        "playerName", "playerNameI", "shotResult", "scoreHome", "scoreAway",
        "description"]


def clock_to_seconds(clock: pd.Series) -> pd.Series:
    """'PT04M31.00S' -> 271.0 seconds remaining in the period."""
    parts = clock.str.extract(r"PT(\d+)M([\d.]+)S")
    return parts[0].astype(float) * 60 + parts[1].astype(float)


def season_label(start_year: int) -> str:
    return f"{start_year}-{str(start_year + 1)[-2:]}"


def infer_home_away(df: pd.DataFrame) -> pd.DataFrame:
    """Home team = the team whose scoring plays move the scoreHome column."""
    d = df.sort_values(["gameId", "orderNumber"]).copy()
    d["scoreHome"] = pd.to_numeric(d["scoreHome"], errors="coerce")
    d["scoreAway"] = pd.to_numeric(d["scoreAway"], errors="coerce")
    d[["scoreHome", "scoreAway"]] = d.groupby("gameId")[["scoreHome", "scoreAway"]].ffill().fillna(0)
    d["dh"] = d.groupby("gameId")["scoreHome"].diff().fillna(d["scoreHome"])
    d["da"] = d.groupby("gameId")["scoreAway"].diff().fillna(d["scoreAway"])
    made = d[(d["shotResult"] == "Made") & d["teamTricode"].notna()]
    votes = (made.assign(home_vote=(made["dh"] > 0).astype(int) - (made["da"] > 0).astype(int))
                 .groupby(["gameId", "teamTricode"])["home_vote"].sum().reset_index())
    games = []
    for gid, g in votes.groupby("gameId"):
        if len(g) != 2:
            raise ValueError(f"game {gid}: expected 2 teams, got {g.teamTricode.tolist()}")
        g = g.sort_values("home_vote", ascending=False)
        home, away = g.teamTricode.iloc[0], g.teamTricode.iloc[1]
        if not (g.home_vote.iloc[0] > 0 > g.home_vote.iloc[1]):
            raise ValueError(f"game {gid}: ambiguous home/away votes {g.to_dict('records')}")
        games.append((gid, home, away))
    return pd.DataFrame(games, columns=["gameId", "home", "away"])


PRIOR_ATTEMPTS = 20  # beta-prior strength used to shrink low-volume shooters toward league FT%


def promo_probability(miss_p: np.ndarray, same_trip_next: np.ndarray | None = None) -> float:
    """P(at least one pair of back-to-back misses) for a fixed sequence of attempts,
    assuming each attempt is independent with the given miss probability.
    If same_trip_next is given, a pair only counts when attempt i continues the
    same trip as attempt i-1 (the "same trip" promo definition)."""
    p_last_make, p_last_miss = 1.0, 0.0  # probability mass with no trigger yet
    for i, m in enumerate(miss_p):
        chained = True if same_trip_next is None else bool(same_trip_next[i])
        alive = p_last_make + p_last_miss
        new_miss = (p_last_make if chained else alive) * m
        p_last_make, p_last_miss = alive * (1 - m), new_miss
    return 1.0 - (p_last_make + p_last_miss)


def streak_flags(made: np.ndarray, trip_pos: np.ndarray, trip_len: np.ndarray):
    """Return (max consecutive misses, index of 2nd miss of first any-pair,
    index of 2nd miss of first same-trip pair) for one team's Q4 FT sequence."""
    run = best = 0
    first_any = first_trip = None
    for i in range(len(made)):
        if made[i]:
            run = 0
            continue
        run += 1
        best = max(best, run)
        if run >= 2 and first_any is None:
            first_any = i
        # Same trip: previous attempt was the prior shot of this same trip.
        if (first_trip is None and i > 0 and not made[i - 1]
                and trip_pos[i] >= 2 and trip_pos[i - 1] == trip_pos[i] - 1
                and trip_len[i - 1] == trip_len[i]):
            first_trip = i
    return best, first_any, first_trip


def build_season(path: Path):
    start_year = int(path.stem.split("_")[-1])
    season = season_label(start_year)
    df = pd.read_csv(path, usecols=COLS, low_memory=False)
    df = df.drop_duplicates(["gameId", "actionNumber"])

    # Local calendar date: shift UTC back 8h so late West Coast tips stay on the right day.
    first_ts = pd.to_datetime(df.groupby("gameId")["timeActual"].min(), utc=True, format="ISO8601")
    game_date = (first_ts - pd.Timedelta(hours=8)).dt.strftime("%Y-%m-%d").rename("game_date")

    ha = infer_home_away(df).merge(game_date, left_on="gameId", right_index=True)
    ha["season"] = season

    # Score at end of regulation periods (for game-context features).
    d = df.copy()
    d["scoreHome"] = pd.to_numeric(d["scoreHome"], errors="coerce")
    d["scoreAway"] = pd.to_numeric(d["scoreAway"], errors="coerce")
    d = d.sort_values(["gameId", "orderNumber"])
    end_q3 = d[d.period <= 3].groupby("gameId")[["scoreHome", "scoreAway"]].max()
    final = d.groupby("gameId")[["scoreHome", "scoreAway"]].max()
    ha = ha.merge(end_q3.rename(columns={"scoreHome": "home_pts_q3", "scoreAway": "away_pts_q3"}),
                  left_on="gameId", right_index=True)
    ha = ha.merge(final.rename(columns={"scoreHome": "home_pts_final", "scoreAway": "away_pts_final"}),
                  left_on="gameId", right_index=True)
    ha["overtime"] = ha.gameId.isin(d[d.periodType == "OVERTIME"].gameId.unique())

    # Free throw attempts.
    ft = df[df.actionType == "freethrow"].copy()
    trip = ft.subType.str.extract(r"(\d) of (\d)").astype(float)
    ft["trip_pos"], ft["trip_len"] = trip[0], trip[1]
    ft["made"] = (ft.shotResult == "Made").astype(int)
    ft["sec_left"] = clock_to_seconds(ft.clock)
    ft = ft.merge(ha[["gameId", "home", "away"]], on="gameId")
    ft["role"] = np.where(ft.teamTricode == ft.home, "Home", "Away")
    ft["opponent"] = np.where(ft.role == "Home", ft.away, ft.home)
    ft = ft.sort_values(["gameId", "orderNumber"])

    full_game = (ft.groupby(["gameId", "role"])["made"].agg(fta="count", ftm="sum")
                   .unstack("role").fillna(0).astype(int))
    full_game.columns = [f"{r.lower()}_{s}_game" for s, r in full_game.columns]

    # Shooter skill: season FT% (all quarters, leave-one-out, shrunk toward league).
    league_pct = ft.made.mean()
    ps = ft.groupby("personId")["made"].agg(["sum", "count"])

    q4 = ft[(ft.period == 4)].copy()
    ps_ftm = q4.personId.map(ps["sum"]).fillna(0)
    ps_fta = q4.personId.map(ps["count"]).fillna(0)
    q4["exp_make"] = ((ps_ftm - q4.made + PRIOR_ATTEMPTS * league_pct)
                      / (ps_fta - 1 + PRIOR_ATTEMPTS)).clip(0, 1)
    q4["promo_pair_any"] = False
    q4["promo_pair_same_trip"] = False
    rows = []
    for (gid, role), g in q4.groupby(["gameId", "role"], sort=False):
        made = g.made.to_numpy()
        tp, tl = g.trip_pos.fillna(1).to_numpy(), g.trip_len.fillna(1).to_numpy()
        best, i_any, i_trip = streak_flags(made, tp, tl)
        miss_p = 1 - g.exp_make.to_numpy()
        chained = np.r_[False, (tp[1:] >= 2) & (tp[:-1] == tp[1:] - 1) & (tl[:-1] == tl[1:])]
        idx = g.index.to_numpy()
        if i_any is not None:
            q4.loc[idx[[i_any - 1, i_any]], "promo_pair_any"] = True
        if i_trip is not None:
            q4.loc[idx[[i_trip - 1, i_trip]], "promo_pair_same_trip"] = True
        rows.append({
            "gameId": gid, "role": role,
            "q4_fta": len(made), "q4_ftm": int(made.sum()),
            "q4_xftm": round(float(g.exp_make.sum()), 3),
            "promo_xprob": round(promo_probability(miss_p), 4),
            "promo_same_trip_xprob": round(promo_probability(miss_p, chained), 4),
            "q4_max_miss_streak": best,
            "promo_any": i_any is not None,
            "promo_same_trip": i_trip is not None,
            "promo_sec_left": g.sec_left.iloc[i_any] if i_any is not None else np.nan,
            "promo_trip_sec_left": g.sec_left.iloc[i_trip] if i_trip is not None else np.nan,
            "promo_shooters": " / ".join(dict.fromkeys(g.playerNameI.iloc[[i_any - 1, i_any]])) if i_any is not None else "",
            "promo_trip_shooters": " / ".join(dict.fromkeys(g.playerNameI.iloc[[i_trip - 1, i_trip]])) if i_trip is not None else "",
        })
    q4_team = pd.DataFrame(rows)

    games = ha.merge(full_game, left_on="gameId", right_index=True, how="left")
    for role in ["Away", "Home"]:
        part = q4_team[q4_team.role == role].drop(columns="role").set_index("gameId")
        part.columns = [f"{role.lower()}_{c}" for c in part.columns]
        games = games.merge(part, left_on="gameId", right_index=True, how="left")
    for role in ["away", "home"]:
        for c in ["q4_fta", "q4_ftm", "q4_max_miss_streak"]:
            games[f"{role}_{c}"] = games[f"{role}_{c}"].fillna(0).astype(int)
        for c in ["q4_xftm", "promo_xprob", "promo_same_trip_xprob"]:
            games[f"{role}_{c}"] = games[f"{role}_{c}"].fillna(0.0)
        for c in ["promo_any", "promo_same_trip"]:
            games[f"{role}_{c}"] = games[f"{role}_{c}"].fillna(False).astype(bool)
        games[f"{role}_promo_shooters"] = games[f"{role}_promo_shooters"].fillna("")
        games[f"{role}_promo_trip_shooters"] = games[f"{role}_promo_trip_shooters"].fillna("")
        for s in ["fta", "ftm"]:
            games[f"{role}_{s}_game"] = games[f"{role}_{s}_game"].fillna(0).astype(int)

    # Venue.
    def venue(r):
        key = (r.game_date, frozenset({r.home, r.away}))
        if key in NEUTRAL_SITES:
            return NEUTRAL_SITES[key], True
        return ARENA_BY_SEASON_OVERRIDE.get((r.home, r.season), TEAMS[r.home][1]), False
    v = games.apply(venue, axis=1, result_type="expand")
    games["arena"], games["neutral_site"] = v[0], v[1]

    # Player-season free throw lines (team = team he shot for; traded players get one row per team).
    neutral_gids = set(games.loc[games.neutral_site, "gameId"])
    q4v = q4[~q4.gameId.isin(neutral_gids)]
    road_q4 = q4v[q4v.role == "Away"]
    players = (ft.groupby(["personId", "teamTricode"])
                 .agg(player=("playerName", "last"), player_short=("playerNameI", "last"),
                      fta=("made", "count"), ftm=("made", "sum")))
    players = players.join(road_q4.groupby(["personId", "teamTricode"])
                           .agg(road_q4_fta=("made", "count"), road_q4_ftm=("made", "sum"),
                                road_q4_xftm=("exp_make", "sum")), how="left")
    trig = road_q4[road_q4.promo_pair_any & (road_q4.made == 0)]
    players = players.join(trig.groupby(["personId", "teamTricode"])
                           .agg(road_promo_games=("gameId", "nunique"),
                                road_promo_misses=("made", "count")), how="left")
    trig_trip = road_q4[road_q4.promo_pair_same_trip & (road_q4.made == 0)]
    players = players.join(trig_trip.groupby(["personId", "teamTricode"])
                           .agg(road_promo_games_trip=("gameId", "nunique")), how="left")
    players = players.join(q4v[q4v.role == "Home"].groupby(["personId", "teamTricode"])
                           .agg(home_q4_fta=("made", "count"), home_q4_ftm=("made", "sum")), how="left")
    players = players.fillna(0).reset_index().rename(columns={"teamTricode": "team"})
    for c in ["road_q4_fta", "road_q4_ftm", "road_promo_games", "road_promo_misses", "road_promo_games_trip",
              "home_q4_fta", "home_q4_ftm"]:
        players[c] = players[c].astype(int)
    players["road_q4_xftm"] = players["road_q4_xftm"].round(2)
    players.insert(0, "season", season)
    players = players[players.personId > 0]

    q4 = q4.merge(ha[["gameId", "game_date", "season"]], on="gameId")
    return games, q4, players


def main():
    out = Path(sys.argv[1])
    out.mkdir(parents=True, exist_ok=True)
    all_games, all_q4, all_players = [], [], []
    for p in sys.argv[2:]:
        g, q, pl = build_season(Path(p))
        print(f"{p}: {len(g)} games, {g.neutral_site.sum()} neutral-site")
        all_games.append(g)
        all_q4.append(q)
        all_players.append(pl)
    games = pd.concat(all_games, ignore_index=True)
    q4 = pd.concat(all_q4, ignore_index=True)
    players = pd.concat(all_players, ignore_index=True)
    players.sort_values(["season", "team", "player"]).to_csv(out / "player_seasons.csv", index=False)

    # Sanity: every neutral-site key we listed must match exactly one game.
    matched = {(r.game_date, frozenset({r.home, r.away})) for r in games[games.neutral_site].itertuples()}
    missing = set(NEUTRAL_SITES) - matched
    if missing:
        raise SystemExit(f"neutral-site games not found in data: {missing}")

    games["game_id"] = games.gameId.astype(str).str.zfill(10)
    games["home_team"] = games.home.map(lambda t: TEAMS[t][0])
    games["away_team"] = games.away.map(lambda t: TEAMS[t][0])
    games["home_arena_label"] = games.home.map(lambda t: TEAMS[t][1])
    games["away_margin_after_q3"] = games.away_pts_q3 - games.home_pts_q3
    games["away_margin_final"] = games.away_pts_final - games.home_pts_final
    games["promo_min_left"] = (games.away_promo_sec_left / 60).round(2)
    games["home_promo_min_left"] = (games.home_promo_sec_left / 60).round(2)
    games["promo_trip_min_left"] = (games.away_promo_trip_sec_left / 60).round(2)
    games["home_promo_trip_min_left"] = (games.home_promo_trip_sec_left / 60).round(2)

    # Long format: one row per team per game (the easiest shape for Tableau).
    long_rows = []
    for role, opp in [("away", "home"), ("home", "away")]:
        t = pd.DataFrame({
            "season": games.season, "game_id": games.game_id, "game_date": games.game_date,
            "team": games[role], "team_name": games[f"{role}_team"],
            "opponent": games[opp], "role": "Away" if role == "away" else "Home",
            "arena": games.arena, "arena_home_team": games.home, "neutral_site": games.neutral_site,
            "q4_fta": games[f"{role}_q4_fta"], "q4_ftm": games[f"{role}_q4_ftm"],
            "q4_xftm": games[f"{role}_q4_xftm"].round(3),
            "q4_max_miss_streak": games[f"{role}_q4_max_miss_streak"],
            "promo_any": games[f"{role}_promo_any"], "promo_same_trip": games[f"{role}_promo_same_trip"],
            "promo_xprob": games[f"{role}_promo_xprob"],
            "promo_min_left": games["promo_min_left" if role == "away" else "home_promo_min_left"],
            "promo_trip_min_left": games["promo_trip_min_left" if role == "away" else "home_promo_trip_min_left"],
            "promo_same_trip_xprob": games[f"{role}_promo_same_trip_xprob"],
            "promo_shooters": games[f"{role}_promo_shooters"],
            "promo_trip_shooters": games[f"{role}_promo_trip_shooters"],
            "fta_game": games[f"{role}_fta_game"], "ftm_game": games[f"{role}_ftm_game"],
            "margin_after_q3": games.away_margin_after_q3 * (1 if role == "away" else -1),
            "margin_final": games.away_margin_final * (1 if role == "away" else -1),
        })
        long_rows.append(t)
    pd.concat(long_rows).sort_values(["game_date", "game_id", "role"]).to_csv(out / "team_games.csv", index=False)

    game_cols = ["season", "game_id", "game_date", "home", "home_team", "away", "away_team",
                 "arena", "home_arena_label", "neutral_site", "overtime",
                 "away_q4_fta", "away_q4_ftm", "away_q4_xftm", "away_q4_max_miss_streak",
                 "away_promo_any", "away_promo_same_trip", "away_promo_xprob", "away_promo_same_trip_xprob",
                 "promo_min_left", "promo_trip_min_left", "away_promo_shooters", "away_promo_trip_shooters",
                 "home_q4_fta", "home_q4_ftm", "home_q4_xftm", "home_q4_max_miss_streak",
                 "home_promo_any", "home_promo_same_trip", "home_promo_xprob",
                 "away_fta_game", "away_ftm_game", "home_fta_game", "home_ftm_game",
                 "away_margin_after_q3", "away_margin_final"]
    games = games.sort_values(["game_date", "game_id"])[game_cols]
    games.to_csv(out / "games.csv", index=False)

    q4 = q4.rename(columns={"teamTricode": "team", "playerName": "player", "playerNameI": "player_short"})
    q4["game_id"] = q4.gameId.astype(str).str.zfill(10)
    q4["arena_home"] = q4.home
    attempt_cols = ["season", "game_id", "game_date", "orderNumber", "team", "role", "opponent", "arena_home",
                    "personId", "player", "player_short", "subType", "trip_pos", "trip_len", "made",
                    "exp_make", "sec_left", "promo_pair_any", "promo_pair_same_trip", "description"]
    q4["exp_make"] = q4.exp_make.round(4)
    neutral_ids = set(games.loc[games.neutral_site, "game_id"])
    q4["neutral_site"] = q4.game_id.isin(neutral_ids)
    q4[attempt_cols + ["neutral_site"]].to_csv(out / "q4_free_throws.csv", index=False)
    print(f"wrote {len(games)} games, {len(q4)} Q4 free throw attempts to {out}")


if __name__ == "__main__":
    main()
