#!/usr/bin/env python3
"""Run the reviewed v1 verifier against the isolated v2 capsule family."""

from __future__ import annotations

import importlib.util
from pathlib import Path
from types import ModuleType


ROOT = Path(__file__).resolve().parent
ENGINE_PATH = ROOT.parent / "v1" / "verify_capsules.py"


def load_engine() -> ModuleType:
    spec = importlib.util.spec_from_file_location(
        "hfo_sigrun_capsule_verify_engine_v1", ENGINE_PATH
    )
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load verify engine: {ENGINE_PATH}")
    engine = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(engine)
    engine.ROOT = ROOT
    engine.DIST = ROOT / "dist"
    engine.INDEX_PATH = ROOT / "heritage_index.json"
    engine.MANIFEST_PATH = engine.DIST / "CAPSULE_FAMILY_MANIFEST.json"
    engine.RECEIPT_PATH = engine.DIST / "VERIFICATION_RECEIPT.json"
    return engine


def main() -> int:
    engine = load_engine()
    result = engine.main()
    receipt_path = ROOT / "dist" / "VERIFICATION_RECEIPT.json"
    if receipt_path.is_file():
        receipt = engine.json.loads(receipt_path.read_text(encoding="utf-8"))
        receipt["schema_id"] = "hfo.gen133.sigrun_capsule_verification_receipt.v2"
        receipt["verification_engine"] = "../v1/verify_capsules.py"
        receipt_path.write_bytes(engine.stable_json_bytes(receipt))
    return result


if __name__ == "__main__":
    raise SystemExit(main())
