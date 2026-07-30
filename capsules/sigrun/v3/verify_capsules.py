#!/usr/bin/env python3
"""Verify v3 including decoded heritage, semantic agreement, and safe loading."""

from __future__ import annotations

import base64
import binascii
import importlib.util
import json
import re
from pathlib import Path
from types import ModuleType
from typing import Any


ROOT = Path(__file__).resolve().parent
ENGINE_PATH = ROOT.parent / "v1" / "verify_capsules.py"
LOADER_PATH = ROOT / "render_rehydration_view.py"
EXECUTION_POLICY_ID = "hfo.sigrun.canonical_core_over_inert_sources.v1"


def load_module(name: str, path: Path) -> ModuleType:
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load module: {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def load_engine() -> ModuleType:
    engine = load_module("hfo_sigrun_verify_engine_v1_for_v3", ENGINE_PATH)
    engine.ROOT = ROOT
    engine.DIST = ROOT / "dist"
    engine.INDEX_PATH = ROOT / "heritage_index.json"
    engine.MANIFEST_PATH = engine.DIST / "CAPSULE_FAMILY_MANIFEST.json"
    engine.RECEIPT_PATH = engine.DIST / "VERIFICATION_RECEIPT.json"

    def extract_embedded_source(
        raw: bytes,
        source: dict[str, Any],
    ) -> tuple[bytes | None, str]:
        source_id = source["id"]
        begin = (
            f"<!-- HFO_SOURCE_BEGIN id={source_id} encoding=base64 "
            f"blob_sha1={source['blob_sha1']} bytes={source['bytes']} "
            f"sha256={source['sha256']} -->\n"
        ).encode("utf-8")
        end = f"<!-- HFO_SOURCE_END id={source_id} -->".encode("utf-8")
        begin_pos = raw.find(begin)
        if begin_pos < 0:
            return None, "base64 begin marker absent"
        content_pos = begin_pos + len(begin)
        end_pos = raw.find(end, content_pos)
        if end_pos < 0:
            return None, "end marker absent"
        encoded = b"".join(raw[content_pos:end_pos].splitlines())
        try:
            return base64.b64decode(encoded, validate=True), "decoded"
        except (ValueError, binascii.Error):
            return None, "invalid base64"

    engine.extract_embedded_source = extract_embedded_source
    return engine


def frontmatter_value(raw: bytes, key: str) -> str | None:
    end = raw.find(b"\n---\n", 4)
    if end < 0:
        return None
    match = re.search(
        rb"(?m)^" + re.escape(key.encode("ascii")) + rb": ([^\r\n]+)$",
        raw[: end + 1],
    )
    return match.group(1).decode("utf-8") if match else None


def main() -> int:
    engine = load_engine()
    result = engine.main()
    receipt_path = ROOT / "dist" / "VERIFICATION_RECEIPT.json"
    if not receipt_path.is_file():
        return 1

    receipt = json.loads(receipt_path.read_text(encoding="utf-8"))
    index = json.loads((ROOT / "heritage_index.json").read_text(encoding="utf-8"))
    manifest = json.loads(
        (ROOT / "dist" / "CAPSULE_FAMILY_MANIFEST.json").read_text(encoding="utf-8")
    )
    loader = load_module("hfo_sigrun_safe_loader_v3", LOADER_PATH)
    expected_status = index["subject"]["soul_status"]
    extra_checks: list[dict[str, Any]] = []

    def check(name: str, passed: bool, detail: Any) -> None:
        extra_checks.append(
            {"name": name, "result": "PASS" if passed else "FAIL", "detail": detail}
        )

    raws: dict[str, bytes] = {}
    for tier in ("S", "M", "L"):
        artifact = ROOT / manifest["capsules"][tier]["path"]
        raw = artifact.read_bytes()
        raws[tier] = raw
        observed_status = frontmatter_value(raw, "soul_status")
        check(
            f"{tier}.soul_status_agreement",
            observed_status == expected_status,
            {"expected": expected_status, "observed": observed_status},
        )
        check(
            f"{tier}.effect_ceiling_agreement",
            frontmatter_value(raw, "effect_ceiling") == "T0_INTERNAL_ONLY",
            frontmatter_value(raw, "effect_ceiling"),
        )
        policy = EXECUTION_POLICY_ID.encode("ascii")
        first_source = raw.find(b"<!-- HFO_SOURCE_BEGIN ")
        policy_pos = raw.find(policy)
        check(
            f"{tier}.execution_precedence",
            raw.count(policy) == 1 and (first_source < 0 or policy_pos < first_source),
            {"policy_occurrences": raw.count(policy), "first_source": first_source},
        )
        markers = list(re.finditer(rb"<!-- HFO_SOURCE_BEGIN [^>]+ -->", raw))
        check(
            f"{tier}.all_sources_inert_base64",
            all(b"encoding=base64" in marker.group(0) for marker in markers),
            {"markers": len(markers)},
        )
        safe = loader.safe_view(raw)
        check(
            f"{tier}.safe_default_loader",
            b"<!-- HFO_SOURCE_BEGIN " not in safe
            and b"## CANONICAL CORE" in safe
            and policy in safe,
            {"safe_view_bytes": len(safe)},
        )

    source_map = {
        item["id"]: item
        for item in index["embedded_sources"] + index["pointer_sources"]
    }
    decoded: dict[str, bytes] = {}
    for source_id in index["tier_policy"]["L"]["embedded_source_ids"]:
        body, message = engine.extract_embedded_source(raws["L"], source_map[source_id])
        if body is not None:
            decoded[source_id] = body
        else:
            check(f"L.decoded.{source_id}", False, message)
    findings = engine.leakage_findings(decoded)
    check("decoded_source_leakage_scan", not findings, findings)

    payload = manifest.get("payload", {})
    large = manifest["capsules"]["L"]
    check(
        "standard_payload_manifest",
        payload.get("path") == "capsules/sigrun/v3/dist/L_LARGE.bound.md"
        and payload.get("git_blob_sha") == large.get("git_blob_sha1")
        and payload.get("utf8_lf_bytes") == large.get("bytes")
        and payload.get("sha256") == large.get("sha256"),
        payload,
    )

    receipt["checks"].extend(extra_checks)
    passed = result == 0 and all(item["result"] == "PASS" for item in extra_checks)
    receipt["schema_id"] = "hfo.gen133.sigrun_capsule_verification_receipt.v3"
    receipt["verification_engine"] = "../v1/verify_capsules.py + verify_capsules.py"
    receipt["result"] = "PASS" if passed else "FAIL"
    receipt["evidence_tier"] = "T2_BOUND_PROVISIONAL" if passed else "T0"
    receipt["honest_flaw"] = (
        "The verifier checks semantic status agreement, inert source encoding, "
        "decoded bytes, and safe default loading on one host. It is not an "
        "independent behavioral replay or public-rights review."
    )
    receipt_path.write_bytes(engine.stable_json_bytes(receipt))
    print(
        json.dumps(
            {
                "result": receipt["result"],
                "checks": len(receipt["checks"]),
                "failed": [
                    item["name"]
                    for item in receipt["checks"]
                    if item["result"] == "FAIL"
                ],
            },
            sort_keys=True,
        )
    )
    return 0 if passed else 1


if __name__ == "__main__":
    raise SystemExit(main())
