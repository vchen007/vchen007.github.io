# Miss Two, Win Chicken: NBA visiting-team free throw project

Goal: predict which upcoming games give the crowd a free chicken sandwich. The trigger: **in the 4th quarter, one visiting player misses two free throws in a row on the same trip to the line**. This folder holds the data pipeline, the analysis, the upcoming-game model and Tableau-ready tables.

## The promo rule

- Both shots of a two-shot trip missed, or two straight misses on a three-shot trip, by the same visiting player.
- 4th quarter only; overtime does not count. Single free throws (and-ones, technicals) cannot trigger it.
- A teammate's technical shot in the middle of the trip does not break it.
- `any_two` in the tables is a broader reference flag: any two straight visitor misses in the 4th, across trips or players.

## Data

| Seasons | Source |
|---|---|
| 2023-24, 2024-25, 2025-26 | NBA live play-by-play feed, archived by [shufinskiy/nba_data](https://github.com/shufinskiy/nba_data) (`cdnnba_<start year>`) |
| 2026-27 so far, and the remaining schedule | ESPN play-by-play and schedule, archived daily by [sportsdataverse](https://github.com/sportsdataverse) (`play_by_play_2027.parquet`, `nba_schedule_2027.parquet`) |

- **The two feeds agree.** Both cover 2025-26. On all 1,229 shared games they match exactly on every visitor 4th-quarter free throw, trip and promo flag (217 promo nights in each).
- **Player IDs.** ESPN and the NBA feed number players differently. `player_id_crosswalk.csv` maps them through 2025-26 player lines (562 of 563 matched). ESPN players with no NBA match, mostly rookies, get `10,000,000 + ESPN id`.
- **Excluded games.** Neutral-site games (Mexico City, Paris, Berlin, London, Manchester and the NBA Cup semifinals) are excluded because no home crowd runs a promo. All-Star games and the NBA Cup final are not counted as regular season.
- **Freshness.** The current-season snapshot covers games through **Nov 2, 2026** (107 games). There were no games on Nov 3.

## Findings, three complete seasons (2023-24 to 2025-26)

**How often it happens.** Visitors set it off in **15.5%** of road games (569 of 3,676), about **6.3 nights per 41-game home season**. By season: 15.2%, 13.6%, then 17.7%. 2026-27 has started hot, at 25.2% (27 of 107), but that is a small sample.

**Road teams miss a bit more.** Visitors make 77.1% of 4th-quarter free throws to home teams' 78.1%. Visitors set off 15% more promos than their shooters' usual FT% predicts (569 vs. 495 expected). For the same team, road minus home is −0.77 points of FT% against expected (paired test, p = 0.049).

**Worst visiting teams (promo rate on the road)**

| Scope | 1 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|---|
| Three seasons | POR 22.8% | GSW 22.0% | DAL 21.1% | NOP 20.3% | IND 19.8% |
| 2025-26 | IND 34.2% | DAL 32.5% | DET 31.7% | NOP 26.8% | LAL 24.4% |
| 2024-25 | GSW 31.7% | POR 31.7% | NOP 22.0% | MEM 22.0% | MIL 20.0% |
| 2023-24 | CHA 26.8% | DAL 24.4% | SAC 24.4% | HOU 24.4% | MIN 22.0% |

**Arenas.** Visitors set it off most at Toyota Center, HOU (22.0%), Madison Square Garden (19.7%), Fiserv Forum (19.5%) and Delta Center (19.5%). They set it off least at State Farm Arena, ATL (9.8%), Golden 1 Center (10.6%) and Crypto.com Arena for Lakers games (10.6%). These gaps are consistent with chance: shuffling arena labels across games produces spreads this wide 46% of the time, and arena rates do not carry over from season to season (r = 0.06, then 0.11).

**Players.** The most promo nights as a visitor over three seasons:

| Player | Promo nights | Season FT% |
|---|---|---|
| Giannis Antetokounmpo | 14 | 64% |
| Rudy Gobert | 9 | 61% |
| Alperen Şengün | 7 | 69% |
| Pascal Siakam | 7 | 72% |
| Zion Williamson | 6 | 70% |
| Evan Mobley | 6 | 68% |

Luka Dončić and Jaylen Brown also had 6.

**Game context.**
- Visitors trailing by 15+ entering the 4th set it off 18.6% of the time, against 12.6% when leading by 15+. Bench players go to the line in blowouts.
- The median trigger comes with 4:38 left.

## The upcoming-game model (`scripts/predict.py`)

For each visiting player who has been playing (share of the team's last three games), the model estimates two things:

- **Late trips.** His 4th-quarter two- or three-shot trips per game: this season blended with last season, worth 10 games of weight.
- **Miss chance.** 1 − FT%, from this season and last, pulled toward the league average by 20 attempts.

Expected two-miss trips = Σ trips × miss² (adjusted for three-shot trips) × the home team's late-fouling factor. That factor is visitors' 4th-quarter trips against that team relative to the league, shrunk by 15 games. A logistic fit on past seasons turns the total into a probability. Uncalibrated, the chance runs low (14.2% on average vs. 15.6% actual in the backtest seasons), in line with the road effect above.

**Backtest.** Trained on 2024-25 and scored on every 2025-26 game, using only information available before each game:

| Model | AUC | Brier skill |
|---|---|---|
| League average | 0.500 | 0.0% |
| Visitor's promo rate so far | 0.538 | 0.5% |
| Players: trips × miss chance | 0.559 | 0.5% |
| Players + home team's fouling | **0.572** | **1.1%** |

The top-rated fifth of 2025-26 games hit 20.8% of the time; the lowest fifth hit 11.4%. Scored the same way, 2024-25 gives the same AUC (0.571). The promo is mostly luck. The model is a useful lean, not a lock.

**Upcoming games as of Nov 4, 2026** (1,088 remaining games; average chance 16.2%):

| Date | Game | Chance | Most likely to miss |
|---|---|---|---|
| Nov 4 | MIA at LAC | 28.2% | Giannis Antetokounmpo (65%), Donovan Mitchell (68%) |
| Nov 11 | LAL at MIL | 26.0% | Walker Kessler (66%), Luka Dončić (79%) |
| Nov 10 | MIA at UTA | 25.9% | Antetokounmpo, Mitchell |
| Nov 6 | MIN at NOP | 24.1% | Rudy Gobert (53%), Jonathan Kuminga (71%) |
| Nov 9 | LAL at ATL | 23.8% | Kessler, Dončić |

Visitors with the highest average chance on the road this season: Miami (24.7%), the Lakers (23.9%), Cleveland (22.2%) and Minnesota (22.0%). The lowest are Orlando (9.8%), Oklahoma City (10.4%) and New York (10.7%).

Limits: rosters and availability are a snapshot of each team's last three games through Nov 2. Injuries, trades and minutes changes since then are not reflected. Far-off games carry today's form.

## Files

| File | What it is |
|---|---|
| `data/upcoming_predictions.csv` | Every remaining 2026-27 game: `promo_chance`, the three visiting players carrying the most risk (FT% and share of risk), expected 4th-quarter trips, home fouling factor. |
| `data/team_games.csv` | One row per team per game since 2023-24 (Home and Away). Main Tableau source. Key columns: `promo`, `promo_xprob`, `promo_min_left`, `promo_shooter`, `q4_fta`, `q4_ftm`, `q4_trips`, `margin_after_q3`, `source`. |
| `data/games.csv` | One row per game, both teams side by side. |
| `data/q4_free_throws.csv` | Every 4th-quarter free throw attempt: shooter, trip position, make, expected make chance, `promo_pair`. |
| `data/player_games.csv` | Every player appearance with free throws and 4th-quarter trips (the model's input). |
| `data/player_seasons.csv` | Player season lines with road and home 4th-quarter splits and road promo nights. |
| `data/player_id_crosswalk.csv` | ESPN id to NBA id. |
| `data/model_backtest.csv`, `data/model_meta.json` | Game-by-game backtest scores and model results. |
| `data/summary_*.csv` | The exact tables behind each dashboard chart (`season = All` is every season combined). |
| `data/analysis_summary.json`, `data/analysis_output.txt` | Significance and stability tests. |

## Daily refresh

```bash
bash nba-ft-promo/scripts/refresh.sh
```

Run it from the repository root. It does everything below in one step: downloads the archives, rebuilds the tables, reruns the analysis and model, and writes the dashboard datasets. It prints `NO_NEW_GAMES` when the archive has nothing newer than the last refresh (`data/refresh_state.json`). `data/dashboard_manifest.json` records which dataset files are live on the dashboard, so a refresh uploads only what changed.

The Claude Code command `.claude/commands/refresh-nba-promo.md` (run `/refresh-nba-promo`) wraps the script with checks, the dashboard upload and the commit. A scheduled task runs the same steps every day at 12:39 PM Eastern.

## Rebuild step by step

```bash
pip install -r requirements.txt
```

```bash
mkdir -p raw && for y in 2023 2024 2025; do curl -sSL -o raw/cdnnba_$y.tar.xz https://raw.githubusercontent.com/shufinskiy/nba_data/main/datasets/cdnnba_$y.tar.xz && tar -xJf raw/cdnnba_$y.tar.xz -C raw; done
```

```bash
for y in 2026 2027; do curl -sSL -o raw/play_by_play_$y.parquet https://github.com/sportsdataverse/sportsdataverse-data/releases/download/espn_nba_pbp/play_by_play_$y.parquet && curl -sSL -o raw/nba_schedule_$y.parquet https://raw.githubusercontent.com/sportsdataverse/hoopR-nba-raw/main/nba/schedules/parquet/nba_schedule_$y.parquet; done
```

```bash
python scripts/build_dataset.py build/nba --nba raw/cdnnba_2023.csv raw/cdnnba_2024.csv raw/cdnnba_2025.csv
```

```bash
python scripts/build_dataset.py build/espn26 --espn raw/play_by_play_2026.parquet,raw/nba_schedule_2026.parquet
```

```bash
python scripts/build_dataset.py build/espn27 --espn raw/play_by_play_2027.parquet,raw/nba_schedule_2027.parquet
```

```bash
python scripts/combine.py data build/nba build/espn26 build/espn27
```

```bash
python scripts/analyze.py data > data/analysis_output.txt
```

```bash
python scripts/predict.py build/model --history build/nba --prior build/espn26 --current build/espn27 --schedule raw/nba_schedule_2027.parquet
```

```bash
cp build/model/upcoming_predictions.csv build/model/model_meta.json data/ && cp build/model/backtest.csv data/model_backtest.csv
```

```bash
python scripts/export_dashboard.py data build/model dashboard_json data
```

To refresh during the season, re-download the two 2027 files and rerun every command after the downloads.

## Tableau notes

- **Upcoming slate.** Use `upcoming_predictions.csv`: sort by `promo_chance`, filter `home` for one arena, and show `shooter_1` and `shooter_2` in the tooltip.
- **Promo rate.** Filter `role = "Away"` and `neutral_site = FALSE` in `team_games.csv`, then use `SUM(INT([promo])) / COUNTD([game_id])`.
- **Arena × visitor heatmap.** Put `arena_home_team` on columns and `team` on rows, color by promo rate, and keep `COUNTD([game_id])` in the tooltip so small samples stay visible.
- **Expected vs. actual.** Compare `SUM([promo_xprob])` with `SUM(INT([promo]))` to see who misses more than their usual FT% predicts.
