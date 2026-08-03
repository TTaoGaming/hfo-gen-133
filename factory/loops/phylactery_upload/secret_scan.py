"""Secret-scan gate.

Two-tier check:

1. PATH_HALT_PATTERNS — file path matches → HALT (never uploads, no override)
2. BODY_HALT_REGEXES  — file body matches → HALT unless (path, pattern) is in
   SCAN_ALLOWLIST.md

Halt = the runner refuses to upload ANYTHING that day. Fail loud.

Rationale: Arweave storage is permanent. A false positive is fixable; a
permanent leak is not. Every match gets read by the operator, then either
rotated + purged from the tree OR allowlisted with a one-line justification.

stdlib only.
"""

from __future__ import annotations

import fnmatch
import re
from pathlib import Path

PATH_HALT_PATTERNS = [
    "**/.env",
    "**/.env.*",
    "**/*.key",
    "**/*.pem",
    "**/*_secret*",
    "**/secrets/*",
    "**/secrets/**/*",
    "**/*.jwk",
    "**/arweave-keyfile*.json",
    "arweave/keys/*",
    "arweave/keys/**/*",
]

BODY_HALT_PATTERNS: list[tuple[str, str]] = [
    ("private_key_pem",      r"BEGIN (RSA |EC |OPENSSH |PGP )?PRIVATE KEY"),
    ("aws_secret",           r"AWS_SECRET_ACCESS_KEY\s*=\s*[A-Za-z0-9/+=]{20,}"),
    ("slack_webhook",        r"SLACK_WEBHOOK_URL\s*=\s*https://hooks\.slack\.com/"),
    ("slack_bot_token",      r"xoxb-[A-Za-z0-9-]{20,}"),
    ("openai_key",           r"sk-[A-Za-z0-9]{20,}"),
    ("github_pat",           r"ghp_[A-Za-z0-9]{20,}"),
    ("anthropic_key",        r"sk-ant-[A-Za-z0-9\-_]{20,}"),
    ("google_api_key",       r"AIza[0-9A-Za-z\-_]{35}"),
    ("stripe_secret",        r"sk_live_[0-9a-zA-Z]{24,}"),
]

BODY_HALT_REGEXES = [(name, re.compile(pat)) for name, pat in BODY_HALT_PATTERNS]

# Only scan bodies of files with these extensions. Binary and big blobs skipped.
BODY_SCAN_EXTS = {
    ".md", ".yaml", ".yml", ".json", ".txt", ".py", ".mjs", ".js", ".ts",
    ".ps1", ".jsonl", ".toml", ".rst", ".env", ".sh", ".bat",
}
BODY_SCAN_MAX_BYTES = 2_000_000  # 2 MB cap on individual body scan


def match_path(relpath: str) -> str | None:
    """Return matching PATH_HALT_PATTERN or None."""
    rp = relpath.replace("\\", "/")
    for pat in PATH_HALT_PATTERNS:
        if fnmatch.fnmatch(rp, pat):
            return pat
    return None


def scan_body(path: Path) -> list[tuple[str, str, int]]:
    """Return [(pattern_name, matched_text, line_number), ...] for body hits."""
    if path.suffix.lower() not in BODY_SCAN_EXTS:
        return []
    try:
        size = path.stat().st_size
        if size > BODY_SCAN_MAX_BYTES:
            return []
        text = path.read_text(encoding="utf-8", errors="replace")
    except OSError:
        return []
    hits: list[tuple[str, str, int]] = []
    lines = text.splitlines()
    for name, rgx in BODY_HALT_REGEXES:
        for i, line in enumerate(lines, 1):
            m = rgx.search(line)
            if m:
                # redact the matched text down to first 8 chars + len
                sample = m.group(0)
                redacted = (sample[:8] + "…" + f"[+{len(sample) - 8} chars]") if len(sample) > 8 else sample
                hits.append((name, redacted, i))
    return hits


def load_allowlist(allowlist_path: Path) -> set[tuple[str, str]]:
    """Parse SCAN_ALLOWLIST.md — table rows | path | pattern | ... |."""
    out: set[tuple[str, str]] = set()
    if not allowlist_path.exists():
        return out
    try:
        text = allowlist_path.read_text(encoding="utf-8", errors="replace")
    except OSError:
        return out
    for line in text.splitlines():
        s = line.strip()
        if not s.startswith("|") or not s.endswith("|"):
            continue
        parts = [p.strip() for p in s.strip("|").split("|")]
        if len(parts) < 2:
            continue
        path, pattern = parts[0], parts[1]
        if path in ("path", "---") or not path or path.startswith("_"):
            continue
        out.add((path.replace("\\", "/"), pattern))
    return out


def scan_tree(root: Path, allowlist_path: Path | None = None) -> dict:
    """Returns {'halt': bool, 'path_hits': [...], 'body_hits': [...], 'files_scanned': int}."""
    allow = load_allowlist(allowlist_path) if allowlist_path else set()
    path_hits: list[dict] = []
    body_hits: list[dict] = []
    files_scanned = 0
    for p in root.rglob("*"):
        if not p.is_file():
            continue
        rel = p.relative_to(root).as_posix()
        files_scanned += 1
        # path check
        m = match_path(rel)
        if m:
            path_hits.append({"path": rel, "pattern": m, "kind": "path_halt"})
            continue  # never even scan body of a path-halted file
        # body check
        hits = scan_body(p)
        for name, sample, lineno in hits:
            allowed = (rel, name) in allow or (rel, f"body:{name}") in allow
            body_hits.append({
                "path": rel,
                "pattern": name,
                "sample_redacted": sample,
                "line": lineno,
                "kind": "body_halt",
                "allowlisted": allowed,
            })
    active_body_halts = [h for h in body_hits if not h["allowlisted"]]
    halt = bool(path_hits) or bool(active_body_halts)
    return {
        "halt": halt,
        "path_hits": path_hits,
        "body_hits": body_hits,
        "active_body_halts": active_body_halts,
        "files_scanned": files_scanned,
    }


if __name__ == "__main__":  # pragma: no cover
    import argparse
    import json
    import sys

    ap = argparse.ArgumentParser()
    ap.add_argument("--root", default="areas/phylactery")
    ap.add_argument("--allowlist", default="areas/phylactery/arweave/SCAN_ALLOWLIST.md")
    args = ap.parse_args()

    root = Path(args.root).resolve()
    allow = Path(args.allowlist).resolve() if args.allowlist else None
    if not root.exists():
        print(f"root not found: {root}", file=sys.stderr)
        raise SystemExit(2)
    result = scan_tree(root, allow)
    print(json.dumps(result, indent=2))
    raise SystemExit(1 if result["halt"] else 0)
