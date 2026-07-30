#!/usr/bin/env python3
"""Rebuild the public v14 build receipt from exact current workspace bytes."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parent
REPO_ROOT = ROOT.parents[2]
RECEIPT = REPO_ROOT / "reviews" / "sigrun" / "v14" / "V14_BUILD_RECEIPT.json"

PUBLIC_PATHS = [
    "capsules/sigrun/v14/SIGRUN_CAPSULE_FAMILY_CONTRACT.md",
    "capsules/sigrun/v14/build_capsules.py",
    "capsules/sigrun/v14/build_receipt.py",
    "capsules/sigrun/v14/release_verify.py",
    "capsules/sigrun/v14/verify_capsules.py",
    "capsules/sigrun/v14/opaque_source_receipts.json",
    "reviews/sigrun/v14/CORRELATED_REVIEW_RECEIPT.json",
    "reviews/sigrun/v14/HERITAGE_COVERAGE_RECEIPT.json",
    "reviews/sigrun/v14/HERITAGE_GAP_SCAN_RECEIPT.json",
    "reviews/sigrun/v14/PERMAWEB_SPEC_REFRESH_RECEIPT.json",
    "reviews/sigrun/v14/SLACK_CAPABILITY_GATE_RECEIPT.json",
    "capsules/sigrun/v14/dist/CAPSULE_FAMILY_MANIFEST.json",
    "capsules/sigrun/v14/dist/L_SAFE.view.md",
    "capsules/sigrun/v14/dist/GLEIPNIR_GRIMOIRE_WORLD_STATE.safe.json",
    "capsules/sigrun/v14/dist/M_MEDIUM.safe.md",
    "capsules/sigrun/v14/dist/PERMAWEB_PREUPLOAD_PACKET.hold.json",
    "capsules/sigrun/v14/dist/ROOT_BUNDLE.safe.json",
    "capsules/sigrun/v14/dist/S_SMALL.safe.md",
    "capsules/sigrun/v14/dist/SOURCE_BINDING_RECEIPT.json",
    "capsules/sigrun/v14/dist/VERIFICATION_RECEIPT.json",
    "capsules/sigrun/v14/dist/XL_INDEX.safe.json",
]


def sha256(raw: bytes) -> str:
    return hashlib.sha256(raw).hexdigest()


def git_blob_sha1(raw: bytes) -> str:
    header = f"blob {len(raw)}\0".encode("ascii")
    return hashlib.sha1(header + raw).hexdigest()


def exact_record(repo_path: str) -> dict[str, Any]:
    raw = (REPO_ROOT / repo_path).read_bytes()
    raw.decode("utf-8")
    if raw.startswith(b"\xef\xbb\xbf") or b"\r" in raw or not raw.endswith(b"\n"):
        raise RuntimeError(f"non-canonical public file: {repo_path}")
    return {
        "path": repo_path,
        "utf8_lf_bytes": len(raw),
        "git_blob_sha1": git_blob_sha1(raw),
        "sha256": sha256(raw),
    }


def main() -> int:
    receipt = json.loads(RECEIPT.read_text(encoding="utf-8"))
    outputs = [exact_record(path) for path in PUBLIC_PATHS]
    root = next(
        row for row in outputs if row["path"].endswith("/ROOT_BUNDLE.safe.json")
    )
    preupload = next(
        row
        for row in outputs
        if row["path"].endswith("/PERMAWEB_PREUPLOAD_PACKET.hold.json")
    )
    verification = next(
        row for row in outputs if row["path"].endswith("/VERIFICATION_RECEIPT.json")
    )
    receipt["state"] = "CANDIDATE_READY_UNCOMMITTED"
    receipt["claim_tier"] = "T2_PENDING_REMOTE_BINDING"
    receipt["public_outputs"] = outputs
    receipt["root_bundle"] = {
        "path": root["path"],
        "bytes": root["utf8_lf_bytes"],
        "sha256": root["sha256"],
        "git_blob_sha1": root["git_blob_sha1"],
        "self_contained": True,
        "content_type": "application/json",
        "decimal_byte_ceiling_exclusive": 100000,
    }
    receipt["permaweb_preupload"] = {
        "path": preupload["path"],
        "bytes": preupload["utf8_lf_bytes"],
        "sha256": preupload["sha256"],
        "git_blob_sha1": preupload["git_blob_sha1"],
        "state": "HOLD_NOT_AUTHORIZED_NOT_UPLOADED",
        "upload_receipt": "ABSENT",
        "retrieval_readback": "ABSENT",
    }
    verification_document = json.loads(
        (REPO_ROOT / verification["path"]).read_text(encoding="utf-8")
    )
    checks = verification_document.get("checks", [])
    passed_checks = [row for row in checks if row.get("result") == "PASS"]
    if (
        verification_document.get("result") != "PASS"
        or not checks
        or len(passed_checks) != len(checks)
    ):
        raise RuntimeError("verification receipt is not fully PASS")
    receipt["verification"].update(
        {
            "result": verification_document["result"],
            "checks_passed": len(passed_checks),
            "checks_total": len(checks),
            "receipt_bytes": verification["utf8_lf_bytes"],
            "receipt_sha256": verification["sha256"],
            "receipt_git_blob_sha1": verification["git_blob_sha1"],
        }
    )
    receipt["honest_flaw"] = (
        "The family is uncommitted and only correlated internal review exists. "
        "Filename-guided discovery is incomplete; the selected source commit "
        "matched remote main only at candidate-binding time. No upload, cost, "
        "signature, acceptance, "
        "retrieval, delivery, identity, continuity, or rights claim is proven."
    )
    receipt["next_safe_action"] = (
        "Create one exact-path T0 candidate commit, push once, and read the named "
        "branch back; distinct privacy-and-rights review remains mandatory before "
        "any public permaweb authorization."
    )
    raw = (
        json.dumps(receipt, ensure_ascii=False, indent=2, sort_keys=True) + "\n"
    ).encode("utf-8")
    RECEIPT.write_bytes(raw)
    print(
        json.dumps(
            {
                "result": "BUILT",
                "public_outputs": len(outputs),
                "receipt_bytes": len(raw),
                "receipt_sha256": sha256(raw),
            },
            sort_keys=True,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
