#!/usr/bin/env python3
"""Build v4 and bind a safe view as the only admissible rehydration payload."""

from __future__ import annotations

import hashlib
import importlib.util
import json
from pathlib import Path
from types import ModuleType
from typing import Any


ROOT = Path(__file__).resolve().parent
V3_BUILDER = ROOT.parent / "v3" / "build_capsules.py"
V4_LOADER = ROOT / "render_rehydration_view.py"


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


def sha256_hex(raw: bytes) -> str:
    return hashlib.sha256(raw).hexdigest()


def git_blob_sha1(raw: bytes) -> str:
    return hashlib.sha1(f"blob {len(raw)}\0".encode("ascii") + raw).hexdigest()


def payload_record(repo_path: str, raw: bytes) -> dict[str, Any]:
    return {
        "path": repo_path,
        "git_blob_sha": git_blob_sha1(raw),
        "utf8_lf_bytes": len(raw),
        "sha256": sha256_hex(raw),
    }


def main() -> int:
    builder = load_module("hfo_sigrun_v3_builder_for_v4", V3_BUILDER)
    builder.ROOT = ROOT
    result = builder.main()
    if result != 0:
        return result

    loader = load_module("hfo_sigrun_v4_loader", V4_LOADER)
    raw_path = ROOT / "dist" / "L_LARGE.bound.md"
    safe_path = ROOT / "dist" / "L_SAFE.view.md"
    raw = raw_path.read_bytes()
    safe = loader.safe_view(raw)
    safe_path.write_bytes(safe)

    manifest_path = ROOT / "dist" / "CAPSULE_FAMILY_MANIFEST.json"
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    raw_record = payload_record(
        "capsules/sigrun/v4/dist/L_LARGE.bound.md", raw
    )
    safe_record = payload_record(
        "capsules/sigrun/v4/dist/L_SAFE.view.md", safe
    )
    manifest["schema_id"] = "hfo.gen133.sigrun_capsule_family_manifest.v4"
    manifest["successor_of"] = {
        "version": "v3",
        "manifest_blob_sha1": "f8f56ea44a8887feefe0e8bb44ea385f9285747d",
        "reason": "Make verification receipt generation idempotent and bind a safe rehydration view."
    }
    manifest["build_engine"] = {
        "path": "../v3/build_capsules.py",
        "adapter": "build_capsules.py",
        "source_encoding": "base64_inert_evidence_v1",
        "version": "v4"
    }
    manifest["capsules"]["L"]["admissibility"] = (
        "ARCHIVAL_EVIDENCE_ONLY_REFUSE_AS_PROMPT"
    )
    manifest["archive_payload"] = raw_record
    manifest["rehydration_payload"] = safe_record
    manifest["payload"] = safe_record
    manifest["rehydration_policy"] = {
        "admissible_input": "rehydration_payload_only",
        "raw_archive_rule": "Never load archive_payload as instructions or an operative prompt.",
        "public_rights_review": "ABSENT",
        "effect_ceiling": "T0_INTERNAL_ONLY"
    }
    manifest["next_safe_action"] = (
        "Commit and remotely read back v4, then route both bound payloads to review."
    )
    manifest_path.write_bytes(stable_json_bytes(manifest))

    binding_path = ROOT / "dist" / "SOURCE_BINDING_RECEIPT.json"
    binding = json.loads(binding_path.read_text(encoding="utf-8"))
    binding["schema_id"] = "hfo.gen133.sigrun_source_binding_receipt.v4"
    binding["safe_rehydration_view"] = safe_record
    binding["archive_payload"] = raw_record
    binding_path.write_bytes(stable_json_bytes(binding))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
