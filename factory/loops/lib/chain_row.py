"""AIH2O chain-row append helper for factory-loop receipts.

Wraps tools/olrun/_chain.py where possible (schema id, valid claim_status,
utc_now_iso). Adds a per-loop path convention:

    state/loop_receipts/<loop>_<UTCDATE>.jsonl

Every row carries:
    row_id, ts_utc, clock_source=host_read, loop, action, verifier_result,
    claim_status, remaining_risk[], next_safe_action, honest_flaw
plus arbitrary extra keys the loop wants to persist (kept flat).

Writes are ATOMIC per row: tmp file + os.replace. Callers that need to
append many rows in a tight batch should call append_rows(rows) which
takes a single lock and a single fsync.

stdlib only.
"""

from __future__ import annotations

import json
import os
import sys
import tempfile
from datetime import datetime, timezone
from pathlib import Path
from typing import Iterable

# Reuse forge conventions where the older tool already ships them.
_TOOLS = Path(__file__).resolve().parents[3] / "tools" / "olrun"
sys.path.insert(0, str(_TOOLS.parent))
try:  # pragma: no cover - depends on repo layout
    from olrun._chain import (  # type: ignore
        VALID_CLAIM_STATUS,
        utc_now_iso,
        forge_root,
    )
except Exception:  # noqa: BLE001 - fall back to inline defs if import path shifts
    VALID_CLAIM_STATUS = ("wired_with_receipts", "proposed", "partial", "failed")

    def utc_now_iso() -> str:  # type: ignore[no-redef]
        return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

    def forge_root() -> str:  # type: ignore[no-redef]
        return str(Path(__file__).resolve().parents[3])


CHAIN_SCHEMA_ID = "hfo.gen133.factory_loops.receipt.v0_1"


def utc_today() -> str:
    return datetime.now(timezone.utc).strftime("%Y%m%d")


def loop_receipt_path(loop: str, day: str | None = None) -> Path:
    day = day or utc_today()
    root = Path(forge_root()) / "state" / "loop_receipts"
    root.mkdir(parents=True, exist_ok=True)
    return root / f"{loop}_{day}.jsonl"


def _next_row_id(path: Path) -> int:
    if not path.exists():
        return 1
    max_id = 0
    count = 0
    with path.open("r", encoding="utf-8") as fh:
        for line in fh:
            line = line.strip()
            if not line:
                continue
            count += 1
            try:
                rid = json.loads(line).get("row_id")
                if isinstance(rid, int) and rid > max_id:
                    max_id = rid
            except (ValueError, AttributeError):
                pass
    return max(count, max_id) + 1


def _atomic_append(path: Path, line: str) -> None:
    """Append `line` (with trailing \\n) atomically.

    Strategy: fsync after write so a crash mid-write cannot leave a torn
    row. We do NOT do read-modify-write; append mode is safe for concurrent
    writers on POSIX and single-writer on Windows (which is our target).
    """
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8", newline="\n") as fh:
        fh.write(line if line.endswith("\n") else line + "\n")
        fh.flush()
        try:
            os.fsync(fh.fileno())
        except (AttributeError, OSError):
            pass  # windows / non-file streams


def append_row(
    loop: str,
    action: str,
    verifier_result: str,
    claim_status: str,
    remaining_risk: Iterable[str] | str | None = None,
    next_safe_action: str = "",
    honest_flaw: str = "",
    extra: dict | None = None,
    receipt_path: Path | None = None,
    actor: str = "factory_loop",
) -> dict:
    """Append one receipt row and return the exact row written."""
    if claim_status not in VALID_CLAIM_STATUS:
        raise ValueError(
            f"claim_status must be one of {list(VALID_CLAIM_STATUS)}, got {claim_status!r}"
        )
    if isinstance(remaining_risk, str):
        remaining_risk = [remaining_risk]
    path = receipt_path or loop_receipt_path(loop)
    row = {
        "row_id": _next_row_id(path),
        "ts_utc": utc_now_iso(),
        "clock_source": "host_read",
        "schema_id": CHAIN_SCHEMA_ID,
        "actor": actor,
        "loop": loop,
        "action": action,
        "verifier_result": verifier_result,
        "claim_status": claim_status,
        "remaining_risk": list(remaining_risk or []),
        "next_safe_action": next_safe_action,
        "honest_flaw": honest_flaw,
    }
    if extra:
        for k, v in extra.items():
            if k not in row:
                row[k] = v
    _atomic_append(path, json.dumps(row, ensure_ascii=False, sort_keys=True))
    return row


def append_rows(loop: str, rows: list[dict], receipt_path: Path | None = None) -> list[dict]:
    """Append many rows. Convenience wrapper — still one row per line."""
    return [append_row(loop=loop, receipt_path=receipt_path, **r) for r in rows]


def read_rows(loop: str, day: str | None = None, receipt_path: Path | None = None) -> list[dict]:
    path = receipt_path or loop_receipt_path(loop, day)
    if not path.exists():
        return []
    out: list[dict] = []
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if line:
            out.append(json.loads(line))
    return out


# ---------------------------------------------------------------------------
# tiny self-test — invoke with `python chain_row.py --selftest`
# ---------------------------------------------------------------------------
if __name__ == "__main__":  # pragma: no cover
    import argparse

    ap = argparse.ArgumentParser()
    ap.add_argument("--selftest", action="store_true")
    args = ap.parse_args()
    if not args.selftest:
        raise SystemExit("Nothing to do. Try --selftest.")

    tmp = Path(tempfile.mkdtemp()) / "test.jsonl"
    r1 = append_row(
        loop="_selftest",
        action="probe",
        verifier_result="local: atomic append succeeded",
        claim_status="wired_with_receipts",
        remaining_risk=[],
        next_safe_action="none",
        honest_flaw="none",
        extra={"payload": {"k": "v"}},
        receipt_path=tmp,
    )
    r2 = append_row(
        loop="_selftest",
        action="probe2",
        verifier_result="second row",
        claim_status="proposed",
        receipt_path=tmp,
    )
    assert r1["row_id"] == 1
    assert r2["row_id"] == 2
    rows = read_rows("_selftest", receipt_path=tmp)
    assert len(rows) == 2 and rows[1]["row_id"] == 2
    print(f"OK — wrote 2 rows to {tmp}")
