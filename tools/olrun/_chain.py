"""Shared append-only chain writer for the Olrun facade tools.

Contract (gen-133):
  chains/OLRUN_FACADE.jsonl, one JSON object per line, APPEND ONLY.
  Existing rows are NEVER rewritten. row_id is monotonically increasing.
  ts_utc is read from the host clock at write time -- never a literal.

stdlib only.
"""

from __future__ import annotations

import json
import os
from datetime import datetime, timezone

CHAIN_SCHEMA_ID = "hfo.gen133.olrun_facade_chain.v0_1"
DEFAULT_ACTOR = "olrun_dispatcher"

VALID_CLAIM_STATUS = ("wired_with_receipts", "proposed", "partial", "failed")


def forge_root() -> str:
    """Repo root = parent of tools/olrun/."""
    return os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))


def default_chain_path() -> str:
    return os.path.join(forge_root(), "chains", "OLRUN_FACADE.jsonl")


def utc_now_iso() -> str:
    """Host clock read. clock_source='host_read' is only honest if this is used."""
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def utc_today() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%d")


def _next_row_id(path: str) -> int:
    """Monotonic from existing file length, and never below max existing row_id."""
    if not os.path.exists(path):
        return 1
    count = 0
    max_id = 0
    with open(path, "r", encoding="utf-8") as fh:
        for line in fh:
            if not line.strip():
                continue
            count += 1
            try:
                rid = json.loads(line).get("row_id")
                if isinstance(rid, int) and rid > max_id:
                    max_id = rid
            except (ValueError, AttributeError):
                pass
    return max(count, max_id) + 1


def append_row(
    action: str,
    verifier_result: str,
    claim_status: str,
    remaining_risk,
    next_safe_action: str,
    honest_flaw: str,
    skill=None,
    actor: str = DEFAULT_ACTOR,
    chain_path: str = None,
    extra: dict = None,
) -> dict:
    """Append one row. Returns the row as written (including row_id / ts_utc)."""
    if claim_status not in VALID_CLAIM_STATUS:
        raise ValueError(
            "claim_status must be one of %s, got %r" % (list(VALID_CLAIM_STATUS), claim_status)
        )
    if isinstance(remaining_risk, str):
        remaining_risk = [remaining_risk]

    path = chain_path or default_chain_path()
    os.makedirs(os.path.dirname(path), exist_ok=True)

    row = {
        "row_id": _next_row_id(path),
        "ts_utc": utc_now_iso(),
        "clock_source": "host_read",
        "actor": actor,
        "action": action,
        "skill": skill,
        "verifier_result": verifier_result,
        "claim_status": claim_status,
        "remaining_risk": list(remaining_risk or []),
        "next_safe_action": next_safe_action,
        "honest_flaw": honest_flaw,
    }
    if extra:
        for key, val in extra.items():
            if key not in row:
                row[key] = val

    # Append mode only. No read-modify-write of prior bytes.
    with open(path, "a", encoding="utf-8", newline="\n") as fh:
        fh.write(json.dumps(row, ensure_ascii=False) + "\n")
    return row


def read_rows(chain_path: str = None):
    path = chain_path or default_chain_path()
    if not os.path.exists(path):
        return []
    out = []
    with open(path, "r", encoding="utf-8") as fh:
        for line in fh:
            if line.strip():
                out.append(json.loads(line))
    return out
