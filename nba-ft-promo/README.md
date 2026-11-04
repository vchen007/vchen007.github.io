# Miss Two, Win Chicken: NBA visiting-team free throw project

Goal: predict whether the **visiting team will miss two free throws in a row in the 4th quarter**, the trigger for a free chicken sandwich for everyone in the arena. This folder holds the data pipeline, a first analysis, and Tableau-ready tables for the dashboard.

## The promo, as measured here

- **Any two in a row (default).** Two consecutive visitor free throw attempts in the 4th quarter are both missed. The streak can span trips to the line, e.g. a miss on the second shot of one trip followed by a miss on the first shot of the next.
- **Same trip only (stricter).** Both misses come on one trip to the line (0-for-2, or two straight misses on a three-shot trip).
- Both misses must happen in the 4th quarter. Overtime is excluded. Technical free throws count.

## Data

- Play-by-play from the NBA live data feed (cdn.nba.com), as archived by the open [shufinskiy/nba_data](https://github.com/shufinskiy/nba_data) project: files `cdnnba_2023`, `cdnnba_2024` and `cdnnba_2025`, which cover the 2023-24, 2024-25 and 2025-26 regular seasons. The 2026-27 season is not in the archive yet.
- 3,690 games in total. 14 neutral-site games are removed because no home crowd is running a promo: the Mexico City, Paris, Berlin and London games, and the Las Vegas NBA Cup semifinals. That leaves 3,676.
- The home team is inferred from which team's baskets move the home score column.
- Spot checks: opening-night scores for all three seasons match the published results, and Giannis Antetokounmpo's 2023-24 line comes out 514/784 against the published 514/783.
- Arena names are the 2025-26 names (Rocket Arena, Xfinity Mobile Arena, Mortgage Matchup Center). The Clippers played 2023-24 at Crypto.com Arena and moved to Intuit Dome in 2024-25.

## What the first pass found (2023-24 through 2025-26)

**How often it happens.** Visitors set off the promo in **22.5%** of road games (826 of 3,676), about **9.2 free-sandwich nights per 41-game home season**. Under the same-trip rule it's 15.4% (6.3 nights). 2025-26 was the highest of the three seasons at 24.6%.

**Road teams do shoot a little worse.** Visitors made 77.1% of 4th-quarter free throws, home teams 78.1%. The baseline is each shooter's own season FT%. Against that, visitors set off **12.8% more promos than expected** (826 actual vs. 732 expected); home teams set off 4% more (751 vs. 720). For the same team, road minus home is −0.77 points of FT% vs. expected (paired test, p = 0.049).

**Worst visiting teams, by promo rate on the road**

| Scope | 1 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|---|
| All three seasons | DAL 30.1% | IND 29.8% | MEM 29.5% | POR 29.3% | NOP 28.5% |
| 2025-26 | IND 43.9% | DET 41.5% | DAL 40.0% | LAC 34.2% | LAL 31.7% |
| 2024-25 | POR 41.5% | NOP 36.6% | MEM 34.2% | GSW 34.2% | CLE 26.8% |
| 2023-24 | HOU 36.6% | CHI 36.6% | DAL 31.7% | SAC 31.7% | CHA 31.7% |

Worst road 4th-quarter FT% in 2025-26: Dallas 67.8% (181/267), Indiana 69.6% (167/240), Detroit 72.2% (223/309).

**Arenas where visitors set it off most (three seasons):** Toyota Center, HOU 29.3%; Delta Center, UTA 27.6%; United Center, CHI 26.8%. Least: Golden 1 Center, SAC 14.6%; Crypto.com Arena, LAL 15.4%; State Farm Arena, ATL 16.4%.

These arena gaps are mostly noise. A permutation test that shuffles arena labels across games produces spreads this wide 43% of the time, and an arena's rate one season does not predict the next (r = 0.18, then −0.10). Houston is the one arena worth watching: visitors shot below their usual FT% there in all three seasons (−7.9, −2.2 and −4.5 points).

**Visitor at a given arena.** A pair has a median of 3 games over three seasons, so pair-level "worst" lists are anecdotes. The most promo nights by one visitor at one arena is 4, which happened seven times. Two examples: Dallas at Target Center (4 of 5 games, 22/38 in the 4th) and Dallas at Chase Center (4 of 6, 28/47). The worst visitor at every arena is in `data/summary_matchups.csv` and on the dashboard's "By arena" tab.

**Who misses them (visitors, three seasons):** Giannis Antetokounmpo 18 promo nights, Pascal Siakam 13, Zion Williamson 13, Domantas Sabonis 11, Paolo Banchero 11, Rudy Gobert 10.

**Game context.** When the visitor trails by 15+ entering the 4th, the rate is 25.6%: bench players go to the line. When the visitor leads by 15+, it's 19.4%. The median trigger comes with 4:24 left in the 4th.

## What this means for the prediction model

- Team-level history barely carries over. A visitor's road promo rate correlates 0.03 and 0.01 with its rate the next season. Team FT% carries over better (0.26 and 0.29).
- A season-holdout test (train 2023-24 and 2024-25, test on 2025-26) gives pre-game team features an AUC of at most 0.543, barely above a coin flip. Knowing which players actually shot in the 4th reaches 0.734.
- So build the model from **players, not teams or arenas**: the visitors' expected free throw shooters and their FT%, plus a **live** update as the 4th quarter unfolds (who is at the line, attempts so far, score margin).

## Files

| File | What it is |
|---|---|
| `data/team_games.csv` | One row per team per game (Home and Away). Main Tableau source. |
| `data/games.csv` | One row per game, home and visitor columns side by side. |
| `data/q4_free_throws.csv` | Every 4th-quarter free throw attempt: shooter, trip position, make, expected make chance, whether it was part of the triggering pair. |
| `data/player_seasons.csv` | Player season FT lines with road and home 4th-quarter splits. |
| `data/summary_*.csv` | The exact tables behind each dashboard chart, by season and for all three seasons (`season = All`). |
| `data/analysis_summary.json`, `data/analysis_output.txt` | Significance tests, stability checks and model results. |
| `scripts/build_dataset.py` | Play-by-play to game, team-game, attempt and player tables. |
| `scripts/analyze.py` | Rankings, permutation test, stability, model test. |
| `scripts/export_dashboard.py` | Aggregates the dashboard tables (JSON) and the `summary_*.csv` files. |

Key columns in `team_games.csv`: `role` (Home/Away), `arena_home_team` (whose building), `neutral_site`, `q4_fta`, `q4_ftm`, `q4_xftm` (expected makes), `promo_any`, `promo_same_trip`, `promo_xprob` (chance of the promo given who shot), `promo_min_left`, `promo_shooters`, `margin_after_q3`.

## Rebuild

```bash
pip install -r requirements.txt
```

```bash
mkdir -p raw && for y in 2023 2024 2025; do curl -sSL -o raw/cdnnba_$y.tar.xz https://raw.githubusercontent.com/shufinskiy/nba_data/main/datasets/cdnnba_$y.tar.xz && tar -xJf raw/cdnnba_$y.tar.xz -C raw; done
```

```bash
python scripts/build_dataset.py data raw/cdnnba_2023.csv raw/cdnnba_2024.csv raw/cdnnba_2025.csv
```

```bash
python scripts/analyze.py data > data/analysis_output.txt
```

```bash
python scripts/export_dashboard.py data dashboard_json data
```

## Tableau notes

- Promo rate: filter `role = "Away"` and `neutral_site = FALSE`, then `SUM(INT([promo_any])) / COUNTD([game_id])`.
- Arena × visitor heatmap: `arena_home_team` on columns, `team` on rows, promo rate as color, and `COUNTD([game_id])` in the tooltip so small samples stay visible.
- Road vs. home: the same calculation with `role` on color, per `team`.
- Expected vs. actual: `SUM([promo_xprob])` against `SUM(INT([promo_any]))` shows whether a team or arena misses more than its shooters' usual FT% predicts.
