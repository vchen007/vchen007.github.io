"""Build game, team-game, attempt and player tables for the visiting-team
free throw promo from NBA play-by-play.

Promo rule: in the 4th quarter, one visiting player misses two free throws in a
row on the same trip to the line (both shots of a two-shot trip, or two straight
on a three-shot trip). Overtime does not count. A broader "any two straight team
misses" flag is kept for reference.

Two sources, one output shape:
  --nba   cdnnba_<startyear>.csv   NBA live-data feed, as archived by github.com/shufinskiy/nba_data
  --espn  play_by_play_<endyear>.parquet,nba_schedule_<endyear>.parquet
          ESPN feed, as archived by github.com/sportsdataverse (hoopR-nba-raw / sportsdataverse-data)

Usage: python build_dataset.py <out_dir> [--nba FILE ...] [--espn PBP,SCHEDULE ...]
Writes games.csv, team_games.csv, q4_free_throws.csv, player_seasons.csv, player_games.csv.
"""
import argparse
from pathlib import Path

import numpy as np
import pandas as pd

# --------------------------------------------------------------------------
# Reference data
# --------------------------------------------------------------------------
TEAMS = {
    # tricode: (team name, home arena 2025-26 name)
    "ATL": ("Atlanta Hawks", "State Farm Arena"),
    "BOS": ("Boston Celtics", "TD Garden"),
    "BKN": ("Brooklyn Nets", "Barclays Center"),
    "CHA": ("Charlotte Hornets", "Spectrum Center"),
    "CHI": ("Chicago Bulls", "United Center"),
    "CLE": ("Cleveland Cavaliers", "Rocket Arena"),
    "DAL": ("Dallas Mavericks", "American Airlines Center"),
    "DEN": ("Denver Nuggets", "Ball Arena"),
    "DET": ("Detroit Pistons", "Little Caesars Arena"),
    "GSW": ("Golden State Warriors", "Chase Center"),
    "HOU": ("Houston Rockets", "Toyota Center"),
    "IND": ("Indiana Pacers", "Gainbridge Fieldhouse"),
    "LAC": ("LA Clippers", "Intuit Dome"),
    "LAL": ("Los Angeles Lakers", "Crypto.com Arena"),
    "MEM": ("Memphis Grizzlies", "FedExForum"),
    "MIA": ("Miami Heat", "Kaseya Center"),
    "MIL": ("Milwaukee Bucks", "Fiserv Forum"),
    "MIN": ("Minnesota Timberwolves", "Target Center"),
    "NOP": ("New Orleans Pelicans", "Smoothie King Center"),
    "NYK": ("New York Knicks", "Madison Square Garden"),
    "OKC": ("Oklahoma City Thunder", "Paycom Center"),
    "ORL": ("Orlando Magic", "Kia Center"),
    "PHI": ("Philadelphia 76ers", "Xfinity Mobile Arena"),
    "PHX": ("Phoenix Suns", "Mortgage Matchup Center"),
    "POR": ("Portland Trail Blazers", "Moda Center"),
    "SAC": ("Sacramento Kings", "Golden 1 Center"),
    "SAS": ("San Antonio Spurs", "Frost Bank Center"),
    "TOR": ("Toronto Raptors", "Scotiabank Arena"),
    "UTA": ("Utah Jazz", "Delta Center"),
    "WAS": ("Washington Wizards", "Capital One Arena"),
}
ESPN_TO_NBA = {"GS": "GSW", "NO": "NOP", "NY": "NYK", "SA": "SAS", "UTAH": "UTA", "WSH": "WAS"}

# NBA feed only (the ESPN schedule carries its own venue and neutral-site flag).
ARENA_BY_SEASON_OVERRIDE = {("LAC", "2023-24"): "Crypto.com Arena"}
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

NBA_COLS = ["gameId", "actionNumber", "orderNumber", "clock", "timeActual", "period",
            "periodType", "actionType", "subType", "teamTricode", "personId",
            "playerName", "playerNameI", "shotResult", "scoreHome", "scoreAway"]
ESPN_COLS = ["game_id", "season", "season_type", "sequence_number", "type_text", "text", "period_number",
             "clock_display_value", "team_id", "athlete_id_1", "athlete_id_2", "athlete_name_1",
             "scoring_play", "home_team_id", "away_team_id", "home_score", "away_score"]
PRIOR_ATTEMPTS = 20  # beta-prior strength used to shrink low-volume shooters toward league FT%


def season_label(start_year: int) -> str:
    return f"{start_year}-{str(start_year + 1)[-2:]}"


def short_name(full: str) -> str:
    """'Giannis Antetokounmpo' -> 'G. Antetokounmpo' (the NBA feed's style)."""
    if not isinstance(full, str) or not full.strip():
        return ""
    parts = full.split()
    return parts[0] if len(parts) == 1 else f"{parts[0][0]}. {' '.join(parts[1:])}"


def nba_clock_seconds(clock: pd.Series) -> pd.Series:
    """'PT04M31.00S' -> 271.0 seconds remaining in the period."""
    parts = clock.str.extract(r"PT(\d+)M([\d.]+)S")
    return parts[0].astype(float) * 60 + parts[1].astype(float)


def espn_clock_seconds(clock: pd.Series) -> pd.Series:
    """'4:31' -> 271.0 and '24.5' -> 24.5 seconds remaining in the period."""
    c = clock.astype(str)
    mm = c.str.extract(r"^(\d+):([\d.]+)$")
    secs = mm[0].astype(float) * 60 + mm[1].astype(float)
    return secs.fillna(pd.to_numeric(c, errors="coerce"))


# --------------------------------------------------------------------------
# Loaders: each returns (meta, ft, apps)
#   meta: gameId, season, game_date, home, away, home_pts_q3, away_pts_q3,
#         home_pts_final, away_pts_final, overtime, arena, neutral_site
#   ft:   gameId, order, period, sec_left, team, personId, player, player_short,
#         trip_pos, trip_len, made          (every free throw attempt)
#   apps: gameId, team, personId            (players who appeared)
# --------------------------------------------------------------------------
def infer_home_away(df: pd.DataFrame) -> pd.DataFrame:
    """NBA feed: home team = the team whose scoring plays move the scoreHome column."""
    d = df.sort_values(["gameId", "orderNumber"]).copy()
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
        if not (g.home_vote.iloc[0] > 0 > g.home_vote.iloc[1]):
            raise ValueError(f"game {gid}: ambiguous home/away votes {g.to_dict('records')}")
        games.append((gid, g.teamTricode.iloc[0], g.teamTricode.iloc[1]))
    return pd.DataFrame(games, columns=["gameId", "home", "away"])


def load_nba(path: Path):
    season = season_label(int(path.stem.split("_")[-1]))
    df = pd.read_csv(path, usecols=NBA_COLS, low_memory=False).drop_duplicates(["gameId", "actionNumber"])
    df["scoreHome"] = pd.to_numeric(df["scoreHome"], errors="coerce")
    df["scoreAway"] = pd.to_numeric(df["scoreAway"], errors="coerce")
    first_ts = pd.to_datetime(df.groupby("gameId")["timeActual"].min(), utc=True, format="ISO8601")
    game_date = (first_ts - pd.Timedelta(hours=8)).dt.strftime("%Y-%m-%d").rename("game_date")
    meta = infer_home_away(df).merge(game_date, left_on="gameId", right_index=True)
    meta["season"] = season
    q3 = df[df.period <= 3].groupby("gameId")[["scoreHome", "scoreAway"]].max()
    fin = df.groupby("gameId")[["scoreHome", "scoreAway"]].max()
    meta = meta.merge(q3.rename(columns={"scoreHome": "home_pts_q3", "scoreAway": "away_pts_q3"}), left_on="gameId", right_index=True)
    meta = meta.merge(fin.rename(columns={"scoreHome": "home_pts_final", "scoreAway": "away_pts_final"}), left_on="gameId", right_index=True)
    meta["overtime"] = meta.gameId.isin(df[df.periodType == "OVERTIME"].gameId.unique())

    def venue(r):
        key = (r.game_date, frozenset({r.home, r.away}))
        if key in NEUTRAL_SITES:
            return NEUTRAL_SITES[key], True
        return ARENA_BY_SEASON_OVERRIDE.get((r.home, r.season), TEAMS[r.home][1]), False
    v = meta.apply(venue, axis=1, result_type="expand")
    meta["arena"], meta["neutral_site"] = v[0], v[1]
    found = {(r.game_date, frozenset({r.home, r.away})) for r in meta[meta.neutral_site].itertuples()}
    y0 = int(season[:4])
    expected = {k for k in NEUTRAL_SITES if f"{y0}-08-01" <= k[0] <= f"{y0 + 1}-07-31"}
    if expected - found:
        raise SystemExit(f"{path}: neutral-site games not found in data: {expected - found}")

    f = df[df.actionType == "freethrow"]
    trip = f.subType.str.extract(r"(\d) of (\d)").astype(float)
    ft = pd.DataFrame({
        "gameId": f.gameId, "order": f.orderNumber, "period": f.period, "sec_left": nba_clock_seconds(f.clock),
        "team": f.teamTricode, "personId": f.personId.astype("int64"), "player": f.playerNameI,
        "player_short": f.playerNameI, "trip_pos": trip[0].fillna(1), "trip_len": trip[1].fillna(1),
        "made": (f.shotResult == "Made").astype(int)})
    a = df[(df.personId > 0) & df.teamTricode.notna()]
    apps = a[["gameId", "teamTricode", "personId"]].drop_duplicates().rename(columns={"teamTricode": "team"})
    apps["personId"] = apps.personId.astype("int64")
    for t in (meta, ft, apps):
        t["gameId"] = t.gameId.astype(int).astype(str).str.zfill(10)
    return meta, ft, apps


def load_espn(pbp_path: Path, sched_path: Path):
    sch = pd.read_parquet(sched_path)
    sch = sch[sch.season_type == 2].copy()
    p = pd.read_parquet(pbp_path, columns=ESPN_COLS)
    p = p[p.season_type == 2].copy()
    season = season_label(int(p.season.iloc[0]) - 1)
    p["gameId"] = p.game_id.astype(str)
    sch["gameId"] = sch.game_id.astype(str)
    abbr = lambda s: s.map(lambda x: ESPN_TO_NBA.get(x, x))
    # Regular season as the NBA counts it: the 30 teams only (no All-Star games), no NBA Cup final.
    sch = sch[abbr(sch.home_abbreviation).isin(TEAMS) & abbr(sch.away_abbreviation).isin(TEAMS)
              & ~sch.notes_headline.fillna("").str.contains("Cup Championship")]
    sch = sch[sch.gameId.isin(p.gameId.unique())]
    p = p[p.gameId.isin(sch.gameId)]
    utc = pd.to_datetime(sch.date, utc=True)
    meta = pd.DataFrame({
        "gameId": sch.gameId, "season": season,
        "game_date": (utc - pd.Timedelta(hours=8)).dt.strftime("%Y-%m-%d"),
        "home": abbr(sch.home_abbreviation), "away": abbr(sch.away_abbreviation),
        "home_espn_id": sch.home_id.astype(int), "arena": sch.venue_full_name,
        "neutral_site": sch.neutral_site.astype(bool)})
    q3 = p[p.period_number <= 3].groupby("gameId")[["home_score", "away_score"]].max()
    fin = p.groupby("gameId")[["home_score", "away_score"]].max()
    meta = meta.merge(q3.rename(columns={"home_score": "home_pts_q3", "away_score": "away_pts_q3"}), left_on="gameId", right_index=True)
    meta = meta.merge(fin.rename(columns={"home_score": "home_pts_final", "away_score": "away_pts_final"}), left_on="gameId", right_index=True)
    meta["overtime"] = meta.gameId.isin(p[p.period_number >= 5].gameId.unique())

    p = p.merge(meta[["gameId", "home", "away", "home_espn_id"]], on="gameId")
    p["team"] = np.where(p.team_id == p.home_espn_id, p.home, p.away)
    f = p[p.type_text.str.startswith("Free Throw", na=False)]
    trip = f.type_text.str.extract(r"(\d) of (\d)").astype(float)
    made = np.where(f.text.str.contains(" makes ", na=False), 1,
                    np.where(f.text.str.contains(" misses ", na=False), 0, f.scoring_play.astype(int)))
    ft = pd.DataFrame({
        "gameId": f.gameId, "order": f.sequence_number, "period": f.period_number,
        "sec_left": espn_clock_seconds(f.clock_display_value), "team": f.team,
        "personId": f.athlete_id_1.astype("int64"), "player": f.athlete_name_1,
        "player_short": f.athlete_name_1.map(short_name), "trip_pos": trip[0].fillna(1),
        "trip_len": trip[1].fillna(1), "made": made.astype(int)})
    a1 = p[p.athlete_id_1.notna() & p.team_id.notna()][["gameId", "team", "athlete_id_1"]].rename(columns={"athlete_id_1": "personId"})
    sub = p[(p.type_text == "Substitution") & p.athlete_id_2.notna()][["gameId", "team", "athlete_id_2"]].rename(columns={"athlete_id_2": "personId"})
    apps = pd.concat([a1, sub]).drop_duplicates()
    apps["personId"] = apps.personId.astype("int64")
    return meta.drop(columns="home_espn_id"), ft, apps


# --------------------------------------------------------------------------
# Promo logic
# --------------------------------------------------------------------------
def assign_trips(tp: np.ndarray, tl: np.ndarray, pid: np.ndarray) -> np.ndarray:
    """Trip id for each multi-shot attempt (-1 for one-shot trips such as and-ones and
    technicals). Shot 1 opens a trip for its shooter; the next number of the same trip by
    the same shooter joins it, even if a teammate's technical shot falls in between."""
    ids = np.full(len(tp), -1)
    open_trip, nxt = {}, 0
    for i in range(len(tp)):
        if tl[i] < 2:
            continue
        cur = open_trip.get(pid[i])
        if cur is not None and tp[i] >= 2 and cur[1] == tp[i] - 1 and cur[2] == tl[i]:
            ids[i] = cur[0]
        else:
            ids[i] = nxt
            nxt += 1
        open_trip[pid[i]] = (ids[i], tp[i], tl[i])
    return ids


def run_probability(miss_p: np.ndarray) -> float:
    """P(at least two straight misses) for independent shots with these miss chances."""
    p_make, p_miss = 1.0, 0.0  # probability mass with no pair yet, by last shot
    for m in miss_p:
        alive = p_make + p_miss
        p_make, p_miss = alive * (1 - m), p_make * m
    return 1.0 - (p_make + p_miss)


def team_q4_summary(g: pd.DataFrame) -> tuple[dict, list, list]:
    """One team's 4th-quarter attempts in order -> summary, promo-pair rows, any-pair rows."""
    made = g.made.to_numpy()
    tp, tl, pid = g.trip_pos.to_numpy(), g.trip_len.to_numpy(), g.personId.to_numpy()
    miss_p = 1 - g.exp_make.to_numpy()
    trips = assign_trips(tp, tl, pid)

    # Official rule: two straight misses inside one player's trip.
    first, xprob_keep = None, 1.0
    for t in np.unique(trips[trips >= 0]):
        ix = np.flatnonzero(trips == t)
        xprob_keep *= 1 - run_probability(miss_p[ix])
        for a, b in zip(ix[:-1], ix[1:]):
            if made[a] == 0 and made[b] == 0 and (first is None or b < first[1]):
                first = (a, b)
                break
    # Reference: any two straight team misses.
    run = best = 0
    first_any = None
    for i in range(len(made)):
        run = 0 if made[i] else run + 1
        best = max(best, run)
        if run >= 2 and first_any is None:
            first_any = (i - 1, i)
    s = {
        "q4_fta": len(made), "q4_ftm": int(made.sum()), "q4_xftm": round(float(g.exp_make.sum()), 3),
        "q4_trips": int(((tp == 1) & (tl >= 2)).sum()), "q4_max_miss_streak": best,
        "promo": first is not None, "promo_xprob": round(1 - xprob_keep, 4),
        "promo_sec_left": g.sec_left.iloc[first[1]] if first else np.nan,
        "promo_shooter": g.player_short.iloc[first[1]] if first else "",
        "any_two": first_any is not None, "any_two_xprob": round(run_probability(miss_p), 4),
    }
    idx = g.index.to_numpy()
    return s, list(idx[list(first)]) if first else [], list(idx[list(first_any)]) if first_any else []


def summarize(meta: pd.DataFrame, ft: pd.DataFrame, apps: pd.DataFrame, source: str):
    meta = meta.copy()
    meta["source"] = source
    ft = ft.merge(meta[["gameId", "home", "away"]], on="gameId")
    ft["role"] = np.where(ft.team == ft.home, "Home", "Away")
    ft["opponent"] = np.where(ft.role == "Home", ft.away, ft.home)
    ft = ft.sort_values(["gameId", "order"]).reset_index(drop=True)

    # Shooter skill: season FT% across all games, leaving out the shot itself, shrunk to league.
    league = ft.made.mean()
    ps = ft.groupby("personId")["made"].agg(["sum", "count"])
    ft["exp_make"] = ((ft.personId.map(ps["sum"]) - ft.made + PRIOR_ATTEMPTS * league)
                      / (ft.personId.map(ps["count"]) - 1 + PRIOR_ATTEMPTS)).clip(0, 1)

    full = ft.groupby(["gameId", "role"])["made"].agg(fta="count", ftm="sum").unstack("role").fillna(0).astype(int)
    full.columns = [f"{r.lower()}_{s}_game" for s, r in full.columns]
    q4 = ft[ft.period == 4].copy()
    q4["promo_pair"] = False
    q4["any_pair"] = False
    rows = []
    for (gid, role), g in q4.groupby(["gameId", "role"], sort=False):
        s, pair, any_pair = team_q4_summary(g)
        q4.loc[pair, "promo_pair"] = True
        q4.loc[any_pair, "any_pair"] = True
        rows.append({"gameId": gid, "role": role, **s})
    q4_team = pd.DataFrame(rows)

    games = meta.merge(full, left_on="gameId", right_index=True, how="left")
    defaults = {"q4_fta": 0, "q4_ftm": 0, "q4_xftm": 0.0, "q4_trips": 0, "q4_max_miss_streak": 0, "promo": False,
                "promo_xprob": 0.0, "promo_sec_left": np.nan, "promo_shooter": "", "any_two": False, "any_two_xprob": 0.0}
    for role in ["Away", "Home"]:
        part = q4_team[q4_team.role == role].drop(columns="role").set_index("gameId")
        games = games.merge(part.add_prefix(f"{role.lower()}_"), left_on="gameId", right_index=True, how="left")
        for c, dv in defaults.items():
            col = f"{role.lower()}_{c}"
            games[col] = games[col].fillna(dv) if not isinstance(dv, float) or not np.isnan(dv) else games[col]
            if isinstance(dv, bool):
                games[col] = games[col].astype(bool)
            elif isinstance(dv, int):
                games[col] = games[col].astype(int)
        for s in ["fta", "ftm"]:
            games[f"{role.lower()}_{s}_game"] = games[f"{role.lower()}_{s}_game"].fillna(0).astype(int)
    games["away_margin_after_q3"] = games.away_pts_q3 - games.home_pts_q3
    games["away_margin_final"] = games.away_pts_final - games.home_pts_final

    # Player-game table: every appearance, with free throw counts.
    pg = apps.merge(meta[["gameId", "season", "game_date", "home", "away", "neutral_site"]], on="gameId")
    pg["role"] = np.where(pg.team == pg.home, "Home", "Away")
    pg["opponent"] = np.where(pg.role == "Home", pg.away, pg.home)
    agg_all = ft.groupby(["gameId", "personId"]).made.agg(fta="count", ftm="sum")
    agg_q4 = q4.assign(trip=((q4.trip_pos == 1) & (q4.trip_len >= 2)).astype(int),
                       trip3=((q4.trip_pos == 1) & (q4.trip_len == 3)).astype(int),
                       pair=q4.promo_pair.astype(int))
    agg_q4 = agg_q4.groupby(["gameId", "personId"]).agg(q4_fta=("made", "count"), q4_ftm=("made", "sum"),
                                                        q4_trips=("trip", "sum"), q4_trips3=("trip3", "sum"),
                                                        promo=("pair", "max"))
    pg = pg.merge(agg_all, left_on=["gameId", "personId"], right_index=True, how="left")
    pg = pg.merge(agg_q4, left_on=["gameId", "personId"], right_index=True, how="left")
    for c in ["fta", "ftm", "q4_fta", "q4_ftm", "q4_trips", "q4_trips3", "promo"]:
        pg[c] = pg[c].fillna(0).astype(int)
    names = ft.groupby("personId").player_short.last()
    pg["player_short"] = pg.personId.map(names).fillna("")
    pg["source"] = source
    pg = pg.drop(columns=["home", "away"])

    # Player-season lines (team = the team he played for; traded players get a row per team).
    neutral = set(meta.loc[meta.neutral_site, "gameId"])
    q4v = q4[~q4.gameId.isin(neutral)]
    road = q4v[q4v.role == "Away"]
    players = ft.groupby(["personId", "team"]).agg(player=("player", "last"), player_short=("player_short", "last"),
                                                   fta=("made", "count"), ftm=("made", "sum"))
    players = players.join(road.assign(trip=((road.trip_pos == 1) & (road.trip_len >= 2)).astype(int))
                           .groupby(["personId", "team"]).agg(road_q4_fta=("made", "count"), road_q4_ftm=("made", "sum"),
                                                              road_q4_xftm=("exp_make", "sum"), road_q4_trips=("trip", "sum")), how="left")
    players = players.join(road[road.promo_pair].groupby(["personId", "team"]).agg(road_promo_games=("gameId", "nunique")), how="left")
    players = players.join(q4v[q4v.role == "Home"].groupby(["personId", "team"]).agg(home_q4_fta=("made", "count"), home_q4_ftm=("made", "sum")), how="left")
    players = players.fillna(0).reset_index()
    for c in ["road_q4_fta", "road_q4_ftm", "road_q4_trips", "road_promo_games", "home_q4_fta", "home_q4_ftm"]:
        players[c] = players[c].astype(int)
    players["road_q4_xftm"] = players.road_q4_xftm.round(2)
    players.insert(0, "season", meta.season.iloc[0])
    players["source"] = source
    players = players[players.personId > 0]

    q4 = q4.merge(meta[["gameId", "game_date", "season"]], on="gameId")
    q4["neutral_site"] = q4.gameId.isin(neutral)
    return games, q4, players, pg


def write(out: Path, parts: list):
    games = pd.concat([p[0] for p in parts], ignore_index=True)
    q4 = pd.concat([p[1] for p in parts], ignore_index=True)
    players = pd.concat([p[2] for p in parts], ignore_index=True)
    pg = pd.concat([p[3] for p in parts], ignore_index=True)

    games = games.rename(columns={"gameId": "game_id"})
    games["home_team"] = games.home.map(lambda t: TEAMS[t][0])
    games["away_team"] = games.away.map(lambda t: TEAMS[t][0])
    games["promo_min_left"] = (games.away_promo_sec_left / 60).round(2)
    games["home_promo_min_left"] = (games.home_promo_sec_left / 60).round(2)
    cols = ["season", "source", "game_id", "game_date", "home", "home_team", "away", "away_team", "arena", "neutral_site",
            "overtime", "away_q4_fta", "away_q4_ftm", "away_q4_xftm", "away_q4_trips", "away_promo", "away_promo_xprob",
            "promo_min_left", "away_promo_shooter", "away_any_two", "away_any_two_xprob", "away_q4_max_miss_streak",
            "home_q4_fta", "home_q4_ftm", "home_q4_xftm", "home_q4_trips", "home_promo", "home_promo_xprob",
            "home_promo_min_left", "home_promo_shooter", "home_any_two", "away_fta_game", "away_ftm_game",
            "home_fta_game", "home_ftm_game", "away_margin_after_q3", "away_margin_final"]
    games = games.sort_values(["game_date", "game_id"])[cols]
    games.to_csv(out / "games.csv", index=False)

    long = []
    for role, opp in [("away", "home"), ("home", "away")]:
        long.append(pd.DataFrame({
            "season": games.season, "source": games.source, "game_id": games.game_id, "game_date": games.game_date,
            "team": games[role], "team_name": games[f"{role}_team"], "opponent": games[opp],
            "role": role.capitalize(), "arena": games.arena, "arena_home_team": games.home,
            "neutral_site": games.neutral_site, "q4_fta": games[f"{role}_q4_fta"], "q4_ftm": games[f"{role}_q4_ftm"],
            "q4_xftm": games[f"{role}_q4_xftm"].round(3), "q4_trips": games[f"{role}_q4_trips"],
            "promo": games[f"{role}_promo"], "promo_xprob": games[f"{role}_promo_xprob"],
            "promo_min_left": games["promo_min_left" if role == "away" else "home_promo_min_left"],
            "promo_shooter": games[f"{role}_promo_shooter"], "any_two": games[f"{role}_any_two"],
            "fta_game": games[f"{role}_fta_game"], "ftm_game": games[f"{role}_ftm_game"],
            "margin_after_q3": games.away_margin_after_q3 * (1 if role == "away" else -1),
            "margin_final": games.away_margin_final * (1 if role == "away" else -1)}))
    pd.concat(long).sort_values(["game_date", "game_id", "role"]).to_csv(out / "team_games.csv", index=False)

    q4 = q4.rename(columns={"gameId": "game_id"})
    q4["exp_make"] = q4.exp_make.round(4)
    q4[["season", "game_id", "game_date", "order", "team", "role", "opponent", "neutral_site", "personId", "player",
        "player_short", "trip_pos", "trip_len", "made", "exp_make", "sec_left", "promo_pair", "any_pair"]
       ].to_csv(out / "q4_free_throws.csv", index=False)
    players.sort_values(["season", "team", "player"]).to_csv(out / "player_seasons.csv", index=False)
    pg.rename(columns={"gameId": "game_id"}).sort_values(["game_date", "game_id", "team", "personId"]).to_csv(out / "player_games.csv", index=False)
    print(f"wrote {len(games)} games, {len(q4)} Q4 attempts, {len(pg)} player-games to {out}")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("out")
    ap.add_argument("--nba", nargs="*", default=[])
    ap.add_argument("--espn", nargs="*", default=[], help="PBP.parquet,SCHEDULE.parquet")
    a = ap.parse_args()
    out = Path(a.out)
    out.mkdir(parents=True, exist_ok=True)
    parts = []
    for f in a.nba:
        parts.append(summarize(*load_nba(Path(f)), source="nba_cdn"))
        g = parts[-1][0]
        print(f"{f}: {len(g)} games, {int(g.neutral_site.sum())} neutral-site")
    for pair in a.espn:
        pbp, sched = pair.split(",")
        parts.append(summarize(*load_espn(Path(pbp), Path(sched)), source="espn"))
        g = parts[-1][0]
        print(f"{pbp}: {len(g)} games, {int(g.neutral_site.sum())} neutral-site")
    write(out, parts)


if __name__ == "__main__":
    main()
