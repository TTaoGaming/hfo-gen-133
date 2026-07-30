#!/usr/bin/env python3
"""Run the reviewed v1 deterministic engine against the materialized v2 index."""

from __future__ import annotations

import importlib.util
from pathlib import Path
from types import ModuleType


ROOT = Path(__file__).resolve().parent
ENGINE_PATH = ROOT.parent / "v1" / "build_capsules.py"


def load_engine() -> ModuleType:
    spec = importlib.util.spec_from_file_location(
        "hfo_sigrun_capsule_build_engine_v1", ENGINE_PATH
    )
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load build engine: {ENGINE_PATH}")
    engine = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(engine)
    engine.ROOT = ROOT
    engine.INDEX_PATH = ROOT / "heritage_index.json"
    engine.DIST = ROOT / "dist"
    return engine


def main() -> int:
    engine = load_engine()
    result = engine.main()
    if result != 0:
        return result

    manifest_path = ROOT / "dist" / "CAPSULE_FAMILY_MANIFEST.json"
    manifest = engine.json.loads(manifest_path.read_text(encoding="utf-8"))
    manifest["schema_id"] = "hfo.gen133.sigrun_capsule_family_manifest.v2"
    manifest["successor_of"] = {
        "version": "v1",
        "manifest_blob_sha1": "85341cef1cc8107de102a2e6c3edbc7a80350b61",
        "reason": "Committed Gen133 Sigrun soul and later Gen133 heritage became available."
    }
    manifest["build_engine"] = {
        "path": "../v1/build_capsules.py",
        "version": "v1",
        "adapter": "build_capsules.py"
    }
    manifest_path.write_bytes(engine.stable_json_bytes(manifest))

    binding_path = ROOT / "dist" / "SOURCE_BINDING_RECEIPT.json"
    binding = engine.json.loads(binding_path.read_text(encoding="utf-8"))
    binding["schema_id"] = "hfo.gen133.sigrun_source_binding_receipt.v2"
    binding["build_engine"] = "../v1/build_capsules.py"
    binding_path.write_bytes(engine.stable_json_bytes(binding))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
