"""Track which dashboard datasets differ from what is live on the dashboard.

  python manifest.py changed <json_dir> <manifest.json>
      Print a JSON list of datasets whose file differs from the live copy:
      [{"id", "file", "sha256", "bytes", "old_blob"}]. New datasets have old_blob null.
  python manifest.py record <json_dir> <manifest.json> <id>=<blob_id> [<id>=<blob_id> ...]
      After uploading, record each dataset's new blob id and file hash.

The manifest maps dataset id -> {"file", "sha256", "bytes", "blob"}; "blob" is the asset id
the dashboard's datasets/<id> document points at (its source url is /_blob/<blob>).
"""
import hashlib
import json
import sys
from pathlib import Path


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load(manifest: Path) -> dict:
    return json.loads(manifest.read_text()) if manifest.exists() else {"datasets": {}}


def changed(json_dir: Path, manifest: Path) -> list:
    live = load(manifest)["datasets"]
    out = []
    for f in sorted(json_dir.glob("*.json")):
        if f.name in ("changed.json",):
            continue
        ds = f.stem
        h = sha(f)
        if live.get(ds, {}).get("sha256") != h:
            out.append({"id": ds, "file": str(f), "sha256": h, "bytes": f.stat().st_size,
                        "old_blob": live.get(ds, {}).get("blob")})
    return out


def record(json_dir: Path, manifest: Path, pairs: list) -> None:
    m = load(manifest)
    for p in pairs:
        ds, blob = p.split("=", 1)
        f = json_dir / f"{ds}.json"
        m["datasets"][ds] = {"file": f.name, "sha256": sha(f), "bytes": f.stat().st_size, "blob": blob}
    manifest.write_text(json.dumps(m, indent=1, sort_keys=True) + "\n")
    print(f"recorded {len(pairs)} datasets in {manifest}")


if __name__ == "__main__":
    cmd, json_dir, manifest = sys.argv[1], Path(sys.argv[2]), Path(sys.argv[3])
    if cmd == "changed":
        print(json.dumps(changed(json_dir, manifest), indent=1))
    elif cmd == "record":
        record(json_dir, manifest, sys.argv[4:])
    else:
        raise SystemExit(__doc__)
