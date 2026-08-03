"""Walk `areas/phylactery/`, hash every file, build both manifests.

Two artifacts produced (in-memory dicts; caller decides where to write):

1. Arweave path manifest — native `arweave/paths` v0.1.0 schema. Root tx.
2. HFO semantic manifest — enriched with sha256 + signatures per file.
   Written to `arweave/manifest.json` inside the tree so it uploads as a data
   item and is reachable at `<manifest_tx>/arweave/manifest.json`.

Signature material and tx_ids come from callers — this module is pure walk +
hash. That keeps it dry-runnable with no keys, no network, no Node.

stdlib only.
"""

from __future__ import annotations

import fnmatch
import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path

# Extensions we upload. Others are skipped (chain-row `skipped:extension`).
UPLOAD_EXTS = {
    ".md", ".yaml", ".yml", ".json", ".txt", ".py", ".mjs", ".js",
    ".ps1", ".jsonl", ".toml", ".rst", ".sig", ".pub",
}

# Directories to skip entirely (never uploaded, never walked into for body).
SKIP_DIRS = {
    ".git", "__pycache__", "node_modules", ".venv", "venv",
    ".pytest_cache", ".mypy_cache", ".ruff_cache", "dist", ".next",
}

# Never-upload path patterns (belt for secret_scan's suspenders).
NEVER_UPLOAD_PATTERNS = [
    "arweave/keys/*", "arweave/keys/**/*",
    "arweave/AUTHORIZED_TO_UPLOAD.md",   # self-referential; do not include
    "**/.env", "**/.env.*",
    "**/*.key", "**/*.pem", "**/*.jwk",
    "**/arweave-keyfile*.json",
    "**/*_secret*",
]


def sha256_hex(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def utc_now_iso() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def is_never_upload(relpath: str) -> bool:
    rp = relpath.replace("\\", "/")
    for pat in NEVER_UPLOAD_PATTERNS:
        if fnmatch.fnmatch(rp, pat):
            return True
    return False


def _in_skip_dir(path: Path, root: Path) -> bool:
    rel = path.relative_to(root)
    for part in rel.parts:
        if part in SKIP_DIRS:
            return True
    return False


def walk(root: Path) -> list[dict]:
    """Walk `root` and return per-file dicts:

    [{ 'path': absolute Path str,
       'relpath': 'apex/sigrun/soul.md',
       'size': int,
       'sha256': hex,
       'ext': '.md',
       'skipped': None | 'extension' | 'never_upload' | 'skip_dir',
       'mtime_utc': ISO }]

    Callers pass this straight into build_path_manifest / build_semantic_manifest.
    """
    out: list[dict] = []
    for p in root.rglob("*"):
        if not p.is_file():
            continue
        if _in_skip_dir(p, root):
            continue  # skip_dir files are not even reported
        rel = p.relative_to(root).as_posix()
        ext = p.suffix.lower()

        skipped: str | None = None
        if is_never_upload(rel):
            skipped = "never_upload"
        elif ext not in UPLOAD_EXTS:
            skipped = "extension"

        try:
            st = p.stat()
            size = st.st_size
            mtime_utc = datetime.fromtimestamp(st.st_mtime, tz=timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
        except OSError as e:
            out.append({"path": str(p), "relpath": rel, "ext": ext, "skipped": f"stat_error:{e}"})
            continue

        row = {
            "path": str(p),
            "relpath": rel,
            "ext": ext,
            "size": size,
            "mtime_utc": mtime_utc,
            "skipped": skipped,
        }
        if not skipped:
            try:
                row["sha256"] = sha256_hex(p.read_bytes())
            except OSError as e:
                row["skipped"] = f"read_error:{e}"
        out.append(row)
    return out


def signer_for(relpath: str) -> str:
    """Return the signer key_id for the given relative path.

    Rules (mirror runner_map.md):
      apex/<name>/**       → apex/<name>
      valkyries/<name>/**  → valkyries/<name>
      else                 → master
    """
    rp = relpath.replace("\\", "/")
    parts = rp.split("/")
    if len(parts) >= 3 and parts[0] == "apex":
        return f"apex/{parts[1]}"
    if len(parts) >= 3 and parts[0] == "valkyries":
        return f"valkyries/{parts[1]}"
    return "master"


def build_path_manifest(walk_rows: list[dict], tx_id_by_relpath: dict[str, str], index_relpath: str = "README.md") -> dict:
    """Build the native Arweave path manifest (v0.1.0)."""
    paths: dict[str, dict] = {}
    for row in walk_rows:
        if row.get("skipped"):
            continue
        rel = row["relpath"]
        tx = tx_id_by_relpath.get(rel)
        if not tx:
            # dry-run: leave a placeholder
            tx = f"DRYRUN_{row.get('sha256', 'nosize')[:12]}"
        paths[rel] = {"id": tx}
    return {
        "manifest": "arweave/paths",
        "version": "0.1.0",
        "index": {"path": index_relpath},
        "paths": paths,
    }


def build_semantic_manifest(
    walk_rows: list[dict],
    tx_id_by_relpath: dict[str, str],
    sig_by_relpath: dict[str, str | None],
    signer_by_relpath: dict[str, str] | None = None,
    signer_pubkey_b64: str | None = None,
    generation: int = 133,
    valid_time_utc: str | None = None,
    manifest_tx_id: str | None = None,
) -> dict:
    """Build the HFO extension manifest (STANDARDS.md §7 + hashes/sigs)."""
    now = utc_now_iso()
    vt = valid_time_utc or now
    signer_by = signer_by_relpath or {}

    # Semantic slots
    root: dict = {"world_state": None, "apex": {}, "valkyries": {}, "skills": None, "tools": None, "memory_capsule": None}
    full_tree: list[dict] = []

    def _entry(rel: str, tx: str | None, sha: str | None, sig: str | None, signer: str) -> dict:
        return {"path": rel, "tx_id": tx or "DRYRUN", "sha256": sha, "sig": sig, "signer": signer}

    for row in walk_rows:
        if row.get("skipped"):
            continue
        rel = row["relpath"]
        tx = tx_id_by_relpath.get(rel)
        sig = sig_by_relpath.get(rel)
        signer = signer_by.get(rel) or signer_for(rel)
        entry = _entry(rel, tx, row.get("sha256"), sig, signer)
        full_tree.append(entry)

        rp = rel
        if rp.startswith("apex/") and rp.endswith("/soul.md"):
            name = rp.split("/")[1]
            root["apex"][name] = entry
        elif rp.startswith("valkyries/") and rp.endswith("/soul.md"):
            name = rp.split("/")[1]
            root["valkyries"][name] = entry
        elif rp.startswith("world_state/") and rp.endswith(".md"):
            # keep latest by lex sort — YYYYMMDD.md
            cur = root.get("world_state")
            if cur is None or rp > cur["path"]:
                root["world_state"] = entry
        elif rp == "skills/README.md":
            root["skills"] = entry
        elif rp == "tools/README.md":
            root["tools"] = entry
        elif rp.startswith("memory_capsules/") and (rp.endswith("/README.md") or rp.count("/") == 1):
            cur = root.get("memory_capsule")
            if cur is None or rp > cur["path"]:
                root["memory_capsule"] = entry

    return {
        "manifest_version": "0.1",
        "generation": generation,
        "generated_utc": now,
        "valid_time_utc": vt,
        "transaction_time_utc": now,
        "signer_pubkey": signer_pubkey_b64,
        "signature": None,  # filled by signer.py after body canonicalized
        "arweave_root_tx": manifest_tx_id,
        "root": root,
        "full_tree": full_tree,
    }


def summarize(walk_rows: list[dict]) -> dict:
    n = len(walk_rows)
    skipped = sum(1 for r in walk_rows if r.get("skipped"))
    total_size = sum(r.get("size", 0) for r in walk_rows if not r.get("skipped"))
    per_class = {"apex": 0, "valkyries": 0, "world_state": 0, "memory_capsules": 0, "tools": 0, "skills": 0, "arweave": 0, "other": 0}
    for r in walk_rows:
        if r.get("skipped"):
            continue
        rel = r["relpath"]
        head = rel.split("/", 1)[0]
        per_class[head] = per_class.get(head, 0) + 1
    return {"files_total": n, "files_skipped": skipped, "files_uploaded": n - skipped, "size_bytes_uploaded": total_size, "per_class": per_class}


if __name__ == "__main__":  # pragma: no cover
    import argparse
    import sys

    ap = argparse.ArgumentParser()
    ap.add_argument("--root", default="areas/phylactery")
    ap.add_argument("--json", action="store_true", help="print full walk as JSON")
    args = ap.parse_args()

    root = Path(args.root).resolve()
    if not root.exists():
        print(f"root not found: {root}", file=sys.stderr)
        raise SystemExit(2)
    rows = walk(root)
    summary = summarize(rows)
    if args.json:
        print(json.dumps({"summary": summary, "rows": rows}, indent=2))
    else:
        print(json.dumps({"summary": summary, "first_10": rows[:10]}, indent=2))
    raise SystemExit(0)
