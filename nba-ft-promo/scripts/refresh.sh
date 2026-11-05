#!/usr/bin/env bash
# Daily refresh for the NBA free throw promo project.
# Downloads the public play-by-play archives, rebuilds every table, reruns the
# analysis and the upcoming-game model, and writes the dashboard datasets.
#
# Usage: bash nba-ft-promo/scripts/refresh.sh [--force] [WORK_DIR]
#   --force   rebuild even when the archive has no new games since the last refresh
#   WORK_DIR  downloads and intermediate builds (default: $TMPDIR/nba-ft-promo-work)
# Ends with NO_NEW_GAMES (nothing to do) or REFRESH_OK followed by a summary.
# The changed dashboard datasets are listed in WORK_DIR/dashboard_json/changed.json.
set -euo pipefail

FORCE=0
if [ "${1:-}" = "--force" ]; then FORCE=1; shift; fi
PROJECT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
WORK="${1:-${TMPDIR:-/tmp}/nba-ft-promo-work}"
RAW="$WORK/raw"; BUILD="$WORK/build"; OUT="$WORK/dashboard_json"
DATA="$PROJECT/data"; SCRIPTS="$PROJECT/scripts"
NBA_SEASONS="2023 2024 2025"   # NBA-feed seasons by start year: fixed history
PRIOR=2026                     # ESPN season (end year) used for player priors: 2025-26
CURRENT=2027                   # ESPN season (end year) being refreshed: 2026-27
ESPN_PBP="https://github.com/sportsdataverse/sportsdataverse-data/releases/download/espn_nba_pbp"
ESPN_SCHED="https://raw.githubusercontent.com/sportsdataverse/hoopR-nba-raw/main/nba/schedules/parquet"
NBA_FEED="https://raw.githubusercontent.com/shufinskiy/nba_data/main/datasets"
PY="python3 -I"
mkdir -p "$RAW" "$BUILD"

fetch() { curl -sSfL --retry 4 --retry-delay 3 --max-time 900 -o "$2.part" "$1" && mv "$2.part" "$2"; }
stale() { [ ! -s "$1" ] || [ "$SCRIPTS/build_dataset.py" -nt "$1" ]; }

echo "== Python packages"
python3 -m pip install --quiet --disable-pip-version-check --only-binary=:all: -r "$PROJECT/requirements.txt"

echo "== Current season"
fetch "$ESPN_PBP/play_by_play_$CURRENT.parquet" "$RAW/play_by_play_$CURRENT.parquet"
fetch "$ESPN_SCHED/nba_schedule_$CURRENT.parquet" "$RAW/nba_schedule_$CURRENT.parquet"
PBP_SHA=$($PY -c 'import hashlib, sys; print(hashlib.sha256(open(sys.argv[1], "rb").read()).hexdigest())' "$RAW/play_by_play_$CURRENT.parquet")
LAST_SHA=$($PY -c 'import json, sys; print(json.load(open(sys.argv[1])).get("pbp_sha256", ""))' "$DATA/refresh_state.json" 2>/dev/null || true)
if [ "$FORCE" = 0 ] && [ "$PBP_SHA" = "$LAST_SHA" ]; then
  $PY -c 'import json, sys; s = json.load(open(sys.argv[1])); print("NO_NEW_GAMES: the archive still ends", s["data_through"])' "$DATA/refresh_state.json"
  exit 0
fi

echo "== History and last season"
for y in $NBA_SEASONS; do
  if [ ! -s "$RAW/cdnnba_$y.csv" ]; then
    fetch "$NBA_FEED/cdnnba_$y.tar.xz" "$RAW/cdnnba_$y.tar.xz"
    tar -xJf "$RAW/cdnnba_$y.tar.xz" -C "$RAW"
  fi
done
[ -s "$RAW/play_by_play_$PRIOR.parquet" ] || fetch "$ESPN_PBP/play_by_play_$PRIOR.parquet" "$RAW/play_by_play_$PRIOR.parquet"
[ -s "$RAW/nba_schedule_$PRIOR.parquet" ] || fetch "$ESPN_SCHED/nba_schedule_$PRIOR.parquet" "$RAW/nba_schedule_$PRIOR.parquet"

echo "== Build tables"
if stale "$BUILD/nba/team_games.csv"; then
  $PY "$SCRIPTS/build_dataset.py" "$BUILD/nba" --nba $(for y in $NBA_SEASONS; do printf '%s ' "$RAW/cdnnba_$y.csv"; done)
fi
if stale "$BUILD/espn$PRIOR/team_games.csv"; then
  $PY "$SCRIPTS/build_dataset.py" "$BUILD/espn$PRIOR" --espn "$RAW/play_by_play_$PRIOR.parquet,$RAW/nba_schedule_$PRIOR.parquet"
fi
$PY "$SCRIPTS/build_dataset.py" "$BUILD/espn$CURRENT" --espn "$RAW/play_by_play_$CURRENT.parquet,$RAW/nba_schedule_$CURRENT.parquet"
$PY "$SCRIPTS/combine.py" "$DATA" "$BUILD/nba" "$BUILD/espn$PRIOR" "$BUILD/espn$CURRENT"

echo "== Analysis and model"
$PY "$SCRIPTS/analyze.py" "$DATA" > "$DATA/analysis_output.txt"
$PY "$SCRIPTS/predict.py" "$BUILD/model" --history "$BUILD/nba" --prior "$BUILD/espn$PRIOR" \
  --current "$BUILD/espn$CURRENT" --schedule "$RAW/nba_schedule_$CURRENT.parquet" > "$BUILD/model_log.txt"
cp "$BUILD/model/upcoming_predictions.csv" "$BUILD/model/model_meta.json" "$DATA/"
cp "$BUILD/model/backtest.csv" "$DATA/model_backtest.csv"

echo "== Dashboard datasets"
rm -rf "$OUT"
$PY "$SCRIPTS/export_dashboard.py" "$DATA" "$BUILD/model" "$OUT" "$DATA" > "$BUILD/export_log.txt"
$PY "$SCRIPTS/manifest.py" changed "$OUT" "$DATA/dashboard_manifest.json" > "$WORK/changed.json"
mv "$WORK/changed.json" "$OUT/changed.json"

$PY - "$DATA" "$OUT" "$PBP_SHA" <<'EOF'
import datetime, json, sys
from pathlib import Path
import pandas as pd
data, out, pbp_sha = Path(sys.argv[1]), Path(sys.argv[2]), sys.argv[3]
meta = json.loads((data / "model_meta.json").read_text())
state = {"pbp_sha256": pbp_sha, "data_through": meta["data_through"], "games_so_far": meta["games_so_far"],
         "refreshed_at": datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%MZ")}
(data / "refresh_state.json").write_text(json.dumps(state, indent=1) + "\n")
up = pd.read_csv(data / "upcoming_predictions.csv")
now = pd.Timestamp.now(tz="UTC")
start = pd.to_datetime(up.start_utc, utc=True)
week = up[(start > now) & (start <= now + pd.Timedelta(days=7))].sort_values("promo_chance", ascending=False)
changed = json.loads((out / "changed.json").read_text())
print("REFRESH_OK")
print(f"data through {meta['data_through']}: {meta['games_so_far']} games of the current season; "
      f"{len(up)} upcoming games, average chance {up.promo_chance.mean():.1%}")
print("top games in the next 7 days:")
for r in week.head(5).itertuples():
    print(f"  {r.date_et} {r.time_et} {r.away} at {r.home}: {r.promo_chance:.1%} ({r.shooter_1}, {r.shooter_2})")
print("changed dashboard datasets:", ", ".join(c["id"] for c in changed) or "none")
EOF
