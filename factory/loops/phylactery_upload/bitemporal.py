"""Bitemporal front-matter enforcement.

Rule: `apex/**/soul.md`, `valkyries/**/soul.md`, `world_state/*.md`, and
`memory_capsules/**/*.md` MUST carry `valid_time_utc` and `transaction_time_utc`
in their YAML front-matter. Other files are exempt.

Missing timestamps → chain-row `claim_status: partial` on the row. Not a HALT.
Rationale: gen-133 open holes list acknowledges the tree is incrementally
populated; failing loud here would block progress on ready files.

stdlib only.
"""

from __future__ import annotations

import fnmatch
import re
from datetime import datetime, timezone
from pathlib import Path

# Directories that MUST have bitemporal front-matter
ENFORCED_PATTERNS = [
    "apex/*/soul.md",
    "apex/*/soul.md.sig",  # signatures inherit
    "valkyries/*/soul.md",
    "valkyries/*/soul.md.sig",
    "world_state/*.md",
    "memory_capsules/*/*.md",
    "memory_capsules/*/*/*.md",
]

FRONTMATTER_RE = re.compile(r"^---\s*\n(.*?)\n---\s*\n", re.DOTALL)


def is_enforced(relpath: str) -> bool:
    """Return True if `relpath` (relative to phylactery root, forward slashes)
    is in the bitemporal-enforced set."""
    rp = relpath.replace("\\", "/")
    for pat in ENFORCED_PATTERNS:
        if fnmatch.fnmatch(rp, pat):
            return True
    return False


def parse_frontmatter(text: str) -> dict:
    """Naive YAML front-matter parser — top-level `key: value` only.

    We intentionally avoid a YAML dependency. If a file uses nested YAML for
    the bitemporal keys, the operator can flatten them or write a `_flat`
    duplicate.
    """
    m = FRONTMATTER_RE.match(text)
    if not m:
        return {}
    body = m.group(1)
    out: dict = {}
    for raw in body.splitlines():
        line = raw.rstrip()
        if not line or line.startswith("#"):
            continue
        # skip nested keys (start with whitespace)
        if line != line.lstrip():
            continue
        if ":" not in line:
            continue
        k, v = line.split(":", 1)
        out[k.strip()] = v.strip().strip("'\"")
    return out


ISO_RE = re.compile(r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}(\.\d+)?Z$")


def _parse_iso(s: str) -> datetime | None:
    if not s or not ISO_RE.match(s):
        return None
    try:
        return datetime.fromisoformat(s.replace("Z", "+00:00"))
    except ValueError:
        return None


def check_file(path: Path, relpath: str) -> dict:
    """Return {'ok': bool, 'reason': str, 'valid_time': str|None, 'transaction_time': str|None}."""
    if not is_enforced(relpath):
        return {"ok": True, "reason": "not_enforced", "valid_time": None, "transaction_time": None}
    try:
        text = path.read_text(encoding="utf-8", errors="replace")
    except OSError as e:
        return {"ok": False, "reason": f"read_error:{e}", "valid_time": None, "transaction_time": None}
    fm = parse_frontmatter(text)
    vt = fm.get("valid_time_utc") or fm.get("valid_time")
    tt = fm.get("transaction_time_utc") or fm.get("transaction_time")
    if not vt:
        return {"ok": False, "reason": "missing:valid_time_utc", "valid_time": None, "transaction_time": tt}
    if not tt:
        return {"ok": False, "reason": "missing:transaction_time_utc", "valid_time": vt, "transaction_time": None}
    if not _parse_iso(vt):
        return {"ok": False, "reason": f"bad_iso:valid_time_utc={vt}", "valid_time": vt, "transaction_time": tt}
    if not _parse_iso(tt):
        return {"ok": False, "reason": f"bad_iso:transaction_time_utc={tt}", "valid_time": vt, "transaction_time": tt}
    return {"ok": True, "reason": "ok", "valid_time": vt, "transaction_time": tt}


def check_tree(root: Path) -> list[dict]:
    """Walk the tree; return the list of {'path', 'relpath', 'ok', 'reason', ...}
    for enforced files only."""
    out: list[dict] = []
    for p in root.rglob("*"):
        if not p.is_file():
            continue
        rel = p.relative_to(root).as_posix()
        if not is_enforced(rel):
            continue
        res = check_file(p, rel)
        res["path"] = str(p)
        res["relpath"] = rel
        out.append(res)
    return out


def utc_now_iso() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


if __name__ == "__main__":  # pragma: no cover
    import argparse
    import json
    import sys

    ap = argparse.ArgumentParser()
    ap.add_argument("--root", default="areas/phylactery")
    args = ap.parse_args()

    root = Path(args.root).resolve()
    if not root.exists():
        print(f"root not found: {root}", file=sys.stderr)
        raise SystemExit(1)
    rows = check_tree(root)
    n_ok = sum(1 for r in rows if r["ok"])
    n_partial = len(rows) - n_ok
    print(json.dumps({"checked": len(rows), "ok": n_ok, "partial": n_partial, "rows": rows}, indent=2))
    # never nonzero — bitemporal misses are partial not halt
    raise SystemExit(0)
