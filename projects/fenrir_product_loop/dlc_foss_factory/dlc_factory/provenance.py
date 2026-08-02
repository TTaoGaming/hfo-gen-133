"""Target-independent provenance byte checks without a legal opinion."""

from __future__ import annotations

import hashlib
from typing import Any

from .canonical import sha256_bytes
from .spec import spec_sha256, validate_spec


def _git_blob_sha1(data: bytes) -> str:
    header = f"blob {len(data)}\0".encode("ascii")
    return hashlib.sha1(header + data, usedforsecurity=False).hexdigest()


def preflight(spec: dict[str, Any], license_bytes: bytes | None = None) -> dict[str, Any]:
    """Check immutable identifiers and supplied bytes; never infer compatibility."""

    checked = validate_spec(spec)
    binding_state = checked["target"]["binding_state"]
    base = {
        "schema_id": "hfo.gen133.dlc_foss_factory.preflight.v1",
        "unit_id": checked["unit_id"],
        "unit_spec_sha256": spec_sha256(checked),
        "target_binding_state": binding_state,
        "license_compatibility_opinion": "NONE",
        "target_admitted": False,
    }
    if binding_state == "UNADMITTED":
        return {
            **base,
            "status": "UNKNOWN_UNBOUND_TARGET",
            "review_ready": False,
            "observed_license_hashes": None,
            "reasons": [
                "No immutable upstream or license-byte identity is bound.",
                "The factory does not opine on an unbound target.",
            ],
        }
    if license_bytes is None:
        return {
            **base,
            "status": "HOLD_LICENSE_BYTES_NOT_SUPPLIED",
            "review_ready": False,
            "observed_license_hashes": None,
            "reasons": [
                "Declared hashes were not checked because no local license bytes were supplied.",
                "No compatibility opinion or target admission is made.",
            ],
        }
    observed = {
        "git_blob_sha1": _git_blob_sha1(license_bytes),
        "sha256": sha256_bytes(license_bytes),
    }
    declared = checked["provenance"]["license"]
    if (
        observed["git_blob_sha1"] != declared["git_blob_sha1"]
        or observed["sha256"] != declared["sha256"]
    ):
        return {
            **base,
            "status": "HOLD_PROVENANCE_HASH_MISMATCH",
            "review_ready": False,
            "observed_license_hashes": observed,
            "reasons": [
                "Supplied license bytes do not match the declared immutable hashes.",
                "No compatibility opinion or target admission is made.",
            ],
        }
    if declared["spdx_expression"] == "NOASSERTION":
        return {
            **base,
            "status": "HOLD_LICENSE_NOASSERTION",
            "review_ready": False,
            "observed_license_hashes": observed,
            "reasons": [
                "License bytes match their declarations but SPDX remains NOASSERTION.",
                "Distinct license review is required; no compatibility opinion is made.",
            ],
        }
    return {
        **base,
        "status": "BOUND_EVIDENCE_REQUIRES_DISTINCT_REVIEW",
        "review_ready": True,
        "observed_license_hashes": observed,
        "reasons": [
            "Supplied license bytes match the declared Git blob and SHA-256 identities.",
            "Byte identity is not license compatibility, target admission, or legal advice.",
        ],
    }
