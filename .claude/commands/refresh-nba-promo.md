---
description: Refresh the NBA free throw promo data, upcoming-game predictions and dashboard with the newest games
argument-hint: "[--force]"
---

# Refresh "Miss Two, Win Chicken"

Rebuild the promo tables and the upcoming-game predictions from the newest public play-by-play. Then update the dashboard and commit the refreshed CSVs.

- Project folder: `nba-ft-promo/` in this repository (scripts in `nba-ft-promo/scripts`, data in `nba-ft-promo/data`)
- Dashboard: https://claude.ai/artifact/8FiLdsghUNoCZ3ETSg2EyQ (a Claude Dashboard artifact)
- Promo rule: in the 4th quarter, one visiting player misses two free throws in a row on the same trip to the line
- The ESPN archive usually posts the previous night's games by about 8:30 AM Eastern

Work through these steps in order. Stop at the first failure and report it.

## 1. Get the latest checkout

Run `git status`. If there are uncommitted changes under `nba-ft-promo/`, stop and ask what to do with them. Otherwise pull the current branch with `git pull --ff-only`.

## 2. Rebuild

Run from the repository root (it takes one to three minutes):

```bash
bash nba-ft-promo/scripts/refresh.sh $ARGUMENTS "${TMPDIR:-/tmp}/nba-ft-promo-work"
```

- If the output ends with `NO_NEW_GAMES`, report that one line and stop. There is nothing to upload or commit.
- If a download fails, name the host and the file that failed and stop. A 403 from a proxy means that host is blocked on this network, so do not retry it.
- Otherwise it ends with `REFRESH_OK` and a summary.

## 3. Check before publishing

Compare against the last committed state (`git show HEAD:nba-ft-promo/data/refresh_state.json`):

- `data_through` must be the same or later, and `games_so_far` must not go down.
- The average upcoming chance should sit between 5% and 40%.
- If no upcoming games remain, the regular season is over: say so and suggest turning off the daily schedule.

If any of these fails, stop before touching the dashboard and report what looked wrong.

## 4. Update the dashboard

Read `${TMPDIR:-/tmp}/nba-ft-promo-work/dashboard_json/changed.json`. It lists each dataset whose file changed: `id`, `file`, and `old_blob` (the file the dashboard uses now). If it is empty, skip to step 5.

1. **Upload.** Upload each changed `file` to the dashboard's asset store with the Artifact tool: `url` set to the dashboard link, `asset: true`, and `file_path` set to the file. Note each new blob id (the part after `/_blob/`).
2. **Repoint.** Read the dashboard's `datasets` collection with the ArtifactData tool to get each document's `version`. Then make one ArtifactData `batch` with an `update` for each changed dataset on `datasets/<id>`, pinned with `if_version`:
   ```json
   {"source": {"kind": "file", "url": "/_blob/<new blob id>", "name": "<id>.json", "format": "json"},
    "updated": {"at": "<now, UTC ISO>", "by": "Claude"},
    "edit": {"via": "claude", "at": "<now, UTC ISO>"}}
   ```
   If a pinned write is refused because the document changed, read it again and redo that write. Do not overwrite someone else's change blindly.
3. **Clean up.** Once the batch has committed, delete each `old_blob` with the Artifact tool (`action: "delete"`, the dashboard `url`, `path` set to the old blob id). Never delete a blob that a dataset document still points at.
4. **Record.** Record the new blob ids:
   ```bash
   python3 -I nba-ft-promo/scripts/manifest.py record "${TMPDIR:-/tmp}/nba-ft-promo-work/dashboard_json" nba-ft-promo/data/dashboard_manifest.json <id>=<new blob id> ...
   ```
5. **Read the check.** With ArtifactData, read the document `check` in collection `data/users/me` once. If it reports `failed`, include what it says in the report. It only exists while someone has the dashboard open.

Do not change the dashboard page itself (`files/index.html`) or any dataset's title or description during a refresh.

If the Artifact or ArtifactData tools are not available in this session, skip this step and say the dashboard was not updated. The CSVs still refresh.

## 5. Commit and push

```bash
git add nba-ft-promo/data
```

```bash
git commit -m "Refresh NBA promo data through <data_through>"
```

```bash
git push
```

Push to the current branch only, and never force-push. If the push fails on a network error, retry up to four times, waiting 2, 4, 8 and 16 seconds.

## 6. Report

In five lines or fewer:
- data through which date, and how many games this season
- the three most likely promo nights in the next seven days, with their chances and likely missers
- which dashboard datasets were updated
- anything that failed or was skipped

## When a new season starts

In `nba-ft-promo/scripts/refresh.sh`:
- Move `PRIOR` and `CURRENT` up one year (for 2027-28: `PRIOR=2027`, `CURRENT=2028`).
- Add the just-finished season to `NBA_SEASONS` once shufinskiy/nba_data publishes it (2026 for 2026-27), or keep using ESPN for it.

Then run with `--force`.
