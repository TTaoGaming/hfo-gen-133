#!/usr/bin/env python3
"""Materialize the immutable Sigrun v2 index from the reviewed v1 base plus overlay."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parent
OVERLAY_PATH = ROOT / "heritage_overlay.json"
OUTPUT_PATH = ROOT / "heritage_index.json"


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def stable_json_bytes(value: Any) -> bytes:
    return (
        json.dumps(value, ensure_ascii=False, indent=2, sort_keys=True) + "\n"
    ).encode("utf-8")


def main() -> int:
    overlay = load_json(OVERLAY_PATH)
    base_path = (ROOT / overlay["base_index"]).resolve()
    index = load_json(base_path)

    for key, value in overlay["set"].items():
        index[key] = value

    removed = set(overlay["remove_pointer_source_ids"])
    index["pointer_sources"] = [
        item for item in index["pointer_sources"] if item["id"] not in removed
    ]
    index["embedded_sources"].extend(overlay["append_embedded_sources"])
    index["pointer_sources"].extend(overlay["append_pointer_sources"])
    index["tier_policy"] = overlay["tier_policy"]

    all_sources = index["embedded_sources"] + index["pointer_sources"]
    source_ids = [item["id"] for item in all_sources]
    if len(source_ids) != len(set(source_ids)):
        raise ValueError("duplicate source id in materialized heritage index")

    known = set(source_ids)
    for tier, policy in index["tier_policy"].items():
        for field in ("embedded_source_ids", "pointer_source_ids"):
            declared = policy.get(field, [])
            if declared == "ALL":
                continue
            unknown = sorted(set(declared) - known)
            if unknown:
                raise ValueError(f"{tier}.{field} references unknown ids: {unknown}")

    OUTPUT_PATH.write_bytes(stable_json_bytes(index))
    print(
        json.dumps(
            {
                "base_index": str(base_path),
                "embedded_sources": len(index["embedded_sources"]),
                "output": str(OUTPUT_PATH),
                "pointer_sources": len(index["pointer_sources"]),
                "schema_id": index["schema_id"],
            },
            sort_keys=True,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
