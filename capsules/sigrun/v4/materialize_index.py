#!/usr/bin/env python3
"""Materialize v4 from immutable v3 and add fail-closed rights dispositions."""

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

    for source in index["embedded_sources"] + index["pointer_sources"]:
        if source.get("privacy_class") == "PUBLIC_ALREADY":
            source["rights_status"] = "PUBLICLY_AVAILABLE_LICENSE_UNVERIFIED"
        else:
            source["rights_status"] = "INTERNAL_REVIEW_RELEASE_NOT_AUTHORIZED"

    index["source_rights_policy"] = {
        "default": "INTERNAL_REVIEW_RELEASE_NOT_AUTHORIZED",
        "publication_rule": "No source may be publicly released or uploaded without explicit rights clearance.",
        "public_rights_review": "ABSENT"
    }
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
