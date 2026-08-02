"""Wrap tools/olrun/approvals_parser.py — do not fork it.

Loops use this to check whether the operator has pre-authorized a class of
sends (LOOP-C directory submissions, LOOP-E partner pitches). Instance
lines still work; class lines are the fast path.

Public API
----------
gate_active(class_name)         -> (bool, remaining_quota_or_None)
resolve_class(class_name, rows) -> list of index rows the loop may act on
                                   (filtered by seq_range + quota + expiry)

Both call into approvals_parser.resolve() so behavior stays 1:1 with the
publish-batch parser Codex D1 uses.
"""

from __future__ import annotations

import datetime as dt
import sys
from pathlib import Path
from typing import Iterable

_TOOLS = Path(__file__).resolve().parents[3] / "tools"
sys.path.insert(0, str(_TOOLS))
from olrun import approvals_parser as ap  # type: ignore  # noqa: E402


FORGE_ROOT = Path(__file__).resolve().parents[3]
DEFAULT_GATE = FORGE_ROOT / "state" / "experiments" / "approvals" / "latest.txt"


def _now_utc() -> dt.datetime:
    return dt.datetime.now(tz=dt.timezone.utc)


def read_gate_lines(gate_path: Path | None = None) -> list[ap.GateLine]:
    path = gate_path or DEFAULT_GATE
    if not path.exists():
        return []
    return ap.parse_gate_file(path)


def gate_active(
    class_name: str,
    gate_path: Path | None = None,
    now: dt.datetime | None = None,
) -> tuple[bool, int | None]:
    """Is there a live class line for `class_name`? Returns (active, quota)."""
    lines = read_gate_lines(gate_path)
    now = now or _now_utc()
    for g in lines:
        if g.kind != "class":
            continue
        if g.class_name != class_name:
            continue
        if not g.expires_utc:
            continue
        exp = dt.datetime.fromisoformat(g.expires_utc.replace("Z", "+00:00"))
        if exp <= now:
            continue
        return True, g.quota
    return False, None


def resolve_class(
    class_name: str,
    index_rows: list[dict],
    gate_path: Path | None = None,
    now: dt.datetime | None = None,
) -> list[dict]:
    """Return the index rows the loop is allowed to act on for `class_name`.

    Delegates to approvals_parser.resolve() which enforces seq_range, quota,
    expiry, and reject lines. We simply filter down to the class_name the
    caller asked about, so mixed-class gate files don't cross-pollinate.
    """
    lines = read_gate_lines(gate_path)
    now = now or _now_utc()
    resolved = ap.resolve(lines, index_rows, now)
    return [r for r in resolved if r.get("class_name") == class_name]


def register_class_shape(class_name: str, market: str) -> None:
    """Extend the CLASS_TO_MARKET map at runtime for a new loop.

    Loops call this at import time so their class labels resolve without
    editing approvals_parser.py directly.
    """
    ap.CLASS_TO_MARKET[class_name] = market


# Register the loop-specific class families this file introduces.
# Extend as new loops ship. Keep in one place so audit is a single grep.
register_class_shape("directory_submissions", "directory_submission")
register_class_shape("partner_pitch", "partner_pitch")


if __name__ == "__main__":  # pragma: no cover
    import argparse
    import json

    p = argparse.ArgumentParser()
    p.add_argument("--class-name", required=True)
    p.add_argument("--gate", type=Path, default=None)
    a = p.parse_args()
    active, quota = gate_active(a.class_name, a.gate)
    print(json.dumps({"class_name": a.class_name, "active": active, "quota": quota}))
