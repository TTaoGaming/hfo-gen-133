#!/usr/bin/env python3
"""Append one hash-linked row to chains/SIGRUN_P4.jsonl using the chain's own
declared hash_rule (ported from verify_chain.py's canonical_bytes/sha256_hex)."""
import hashlib
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent
CHAIN = ROOT / "chains" / "SIGRUN_P4.jsonl"


def canonical_bytes(obj: dict) -> bytes:
    return json.dumps(obj, sort_keys=True, separators=(",", ":"), ensure_ascii=True).encode("utf-8")


def sha256_hex(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def last_row_sha(path: Path) -> str | None:
    last = None
    with path.open("r", encoding="utf-8-sig") as fh:
        for line in fh:
            line = line.strip()
            if not line:
                continue
            row = json.loads(line)
            if isinstance(row.get("row_sha256"), str) and len(row["row_sha256"]) == 64:
                last = row["row_sha256"]
    return last


def main() -> int:
    row = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
    row["prev_sha256"] = last_row_sha(CHAIN)
    row["row_sha256"] = sha256_hex(canonical_bytes(row))
    with CHAIN.open("a", encoding="utf-8") as fh:
        fh.write(json.dumps(row, sort_keys=True, separators=(",", ":"), ensure_ascii=True) + "\n")
    print(f"APPENDED row_sha256={row['row_sha256']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
