#!/usr/bin/env python3
"""Materialize immutable v5 from the reviewed v4 index."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parent


def stable_json_bytes(value: Any) -> bytes:
    return (
        json.dumps(value, ensure_ascii=False, indent=2, sort_keys=True) + "\n"
    ).encode("utf-8")


def main() -> int:
    overlay = json.loads((ROOT / "heritage_overlay.json").read_text(encoding="utf-8"))
    base_path = (ROOT / overlay["base_index"]).resolve()
    index = json.loads(base_path.read_text(encoding="utf-8"))
    for key, value in overlay["set"].items():
        index[key] = value
    (ROOT / "heritage_index.json").write_bytes(stable_json_bytes(index))
    print(
        json.dumps(
            {
                "base_index": str(base_path),
                "embedded_sources": len(index["embedded_sources"]),
                "output": str(ROOT / "heritage_index.json"),
                "pointer_sources": len(index["pointer_sources"]),
                "schema_id": index["schema_id"],
            },
            sort_keys=True,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
