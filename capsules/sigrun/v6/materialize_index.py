#!/usr/bin/env python3
"""Materialize immutable v6 from v5 plus the reviewed pointer-only mining delta."""

from __future__ import annotations

import hashlib
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

    delta_path = ROOT / overlay["pointer_delta"]
    delta_raw = delta_path.read_bytes()
    delta = json.loads(delta_raw.decode("utf-8"))
    additions = delta["sources"]
    existing_ids = {
        source["id"]
        for source in index["embedded_sources"] + index["pointer_sources"]
    }
    addition_ids = [source["id"] for source in additions]
    if len(addition_ids) != len(set(addition_ids)):
        raise RuntimeError("v6 pointer delta contains duplicate source ids")
    collisions = sorted(existing_ids.intersection(addition_ids))
    if collisions:
        raise RuntimeError(f"v6 pointer delta collides with v5 ids: {collisions}")
    for source in additions:
        required = (
            "id",
            "repository",
            "commit",
            "path",
            "blob_sha1",
            "bytes",
            "sha256",
            "disposition",
            "privacy_class",
            "rights_status",
            "body_embedding",
        )
        missing = [key for key in required if key not in source]
        if missing:
            raise RuntimeError(f"{source.get('id', 'UNKNOWN')} missing {missing}")
        if source["body_embedding"] not in (
            "PROHIBITED",
            "POINTER_ONLY_BY_V6_POLICY",
        ):
            raise RuntimeError(f"{source['id']} is not pointer-only")
    index["pointer_sources"].extend(additions)

    tier_ids = delta["tier_pointer_ids"]
    for tier in ("M", "L"):
        requested = addition_ids if tier_ids[tier] == "ALL" else tier_ids[tier]
        unknown = sorted(set(requested).difference(addition_ids))
        if unknown:
            raise RuntimeError(f"{tier} pointer ids not in v6 delta: {unknown}")
        current = index["tier_policy"][tier]["pointer_source_ids"]
        for source_id in requested:
            if source_id not in current:
                current.append(source_id)

    index["source_mining_delta"] = {
        "schema_id": delta["schema_id"],
        "base_index": overlay["base_index"],
        "base_manifest_blob_sha1": overlay["base_manifest_blob_sha1"],
        "pointer_delta_path": overlay["pointer_delta"],
        "pointer_delta_bytes": len(delta_raw),
        "pointer_delta_sha256": hashlib.sha256(delta_raw).hexdigest(),
        "added_pointer_sources": len(additions),
        "body_embedding": "PROHIBITED_FOR_ALL_V6_ADDITIONS",
        "independent_review": "ABSENT",
        "correlated_privacy_review": "ABSTAIN_POINTER_METADATA_SAFE",
    }
    (ROOT / "heritage_index.json").write_bytes(stable_json_bytes(index))
    print(
        json.dumps(
            {
                "base_index": str(base_path),
                "embedded_sources": len(index["embedded_sources"]),
                "output": str(ROOT / "heritage_index.json"),
                "pointer_sources": len(index["pointer_sources"]),
                "schema_id": index["schema_id"],
                "v6_added_pointer_sources": len(additions),
            },
            sort_keys=True,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
