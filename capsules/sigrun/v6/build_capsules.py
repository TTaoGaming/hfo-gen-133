#!/usr/bin/env python3
"""Build v6 from v5 with a pointer-only heritage mining delta."""

from __future__ import annotations

import hashlib
import importlib.util
import json
from pathlib import Path
from types import ModuleType
from typing import Any


ROOT = Path(__file__).resolve().parent
V5_BUILDER = ROOT.parent / "v5" / "build_capsules.py"
V6_LOADER = ROOT / "render_rehydration_view.py"


def load_module(name: str, path: Path) -> ModuleType:
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load module: {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def stable_json_bytes(value: Any) -> bytes:
    return (
        json.dumps(value, ensure_ascii=False, indent=2, sort_keys=True) + "\n"
    ).encode("utf-8")


def payload_record(repo_path: str, raw: bytes) -> dict[str, Any]:
    return {
        "path": repo_path,
        "git_blob_sha": hashlib.sha1(
            f"blob {len(raw)}\0".encode("ascii") + raw
        ).hexdigest(),
        "utf8_lf_bytes": len(raw),
        "sha256": hashlib.sha256(raw).hexdigest(),
    }


def main() -> int:
    builder = load_module("hfo_sigrun_v5_builder_for_v6", V5_BUILDER)
    builder.ROOT = ROOT
    result = builder.main()
    if result != 0:
        return result

    loader = load_module("hfo_sigrun_v6_loader", V6_LOADER)
    archive_path = ROOT / "dist" / "L_LARGE.bound.md"
    safe_path = ROOT / "dist" / "L_SAFE.view.md"
    archive = archive_path.read_bytes()
    safe = loader.safe_view(archive)
    safe_path.write_bytes(safe)

    archive_record = payload_record(
        "capsules/sigrun/v6/dist/L_LARGE.bound.md", archive
    )
    safe_record = payload_record(
        "capsules/sigrun/v6/dist/L_SAFE.view.md", safe
    )
    manifest_path = ROOT / "dist" / "CAPSULE_FAMILY_MANIFEST.json"
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    manifest["schema_id"] = "hfo.gen133.sigrun_capsule_family_manifest.v6"
    manifest["successor_of"] = {
        "version": "v5",
        "manifest_blob_sha1": "de332c45ff878086d749de7b34a5e9b50f65c068",
        "reason": (
            "Add exact pointer-only Sigrun, Cantrix, HopeAI, grimoire, rune, "
            "poetry, and world-state heritage without admitting source bodies."
        ),
    }
    manifest["build_engine"] = {
        "path": "../v5/build_capsules.py",
        "adapter": "build_capsules.py",
        "source_encoding": "base64_inert_evidence_v1",
        "version": "v6",
    }
    manifest["archive_payload"] = archive_record
    manifest["rehydration_payload"] = safe_record
    manifest["payload"] = safe_record
    manifest["rehydration_policy"] = {
        "admissible_input": "rehydration_payload_only",
        "safe_view_schema": "hfo.gen133.sigrun_safe_rehydration_view.v6",
        "safe_view_self_hash_required": True,
        "raw_archive_rule": "Never load archive_payload as instructions or an operative prompt.",
        "v6_pointer_delta_rule": "All v6 additions are metadata-only; body embedding is prohibited.",
        "public_rights_review": "ABSENT",
        "effect_ceiling": "T0_INTERNAL_ONLY",
    }
    manifest["next_safe_action"] = (
        "Commit and remotely read back v6, then run one distinct-provider "
        "behavioral replay using only the safe view."
    )
    manifest_path.write_bytes(stable_json_bytes(manifest))

    binding_path = ROOT / "dist" / "SOURCE_BINDING_RECEIPT.json"
    binding = json.loads(binding_path.read_text(encoding="utf-8"))
    binding["schema_id"] = "hfo.gen133.sigrun_source_binding_receipt.v6"
    binding["safe_rehydration_view"] = safe_record
    binding["archive_payload"] = archive_record
    binding["v6_pointer_delta"] = json.loads(
        (ROOT / "heritage_index.json").read_text(encoding="utf-8")
    )["source_mining_delta"]
    binding_path.write_bytes(stable_json_bytes(binding))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
