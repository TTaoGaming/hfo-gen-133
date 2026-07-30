#!/usr/bin/env python3
"""Independently verify the deterministic Sigrun capsule family.

This verifier does not import the builder. It reimplements the byte, hash,
budget, monotonicity, embedding, chunk-reconstruction, and leakage checks from
the published capsule contract using only the generated artifacts and the
committed heritage index.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import re
import sys
from typing import Any


ROOT = Path(__file__).resolve().parent
DIST = ROOT / "dist"
INDEX_PATH = ROOT / "heritage_index.json"
MANIFEST_PATH = DIST / "CAPSULE_FAMILY_MANIFEST.json"
RECEIPT_PATH = DIST / "VERIFICATION_RECEIPT.json"
SELF_PLACEHOLDER = "SELF_HASH_PLACEHOLDER"


def canonical_bytes(raw: bytes) -> bytes:
    if raw.startswith(b"\xef\xbb\xbf"):
        raw = raw[3:]
    raw = raw.replace(b"\r\n", b"\n").replace(b"\r", b"\n")
    return raw.rstrip(b"\n") + b"\n"


def sha256_hex(raw: bytes) -> str:
    return hashlib.sha256(raw).hexdigest()


def git_blob_sha1(raw: bytes) -> str:
    header = f"blob {len(raw)}\0".encode("ascii")
    return hashlib.sha1(header + raw).hexdigest()


def stable_json_bytes(value: Any) -> bytes:
    text = json.dumps(value, ensure_ascii=False, sort_keys=True, indent=2)
    return (text + "\n").encode("utf-8")


def load_json(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as handle:
        value = json.load(handle)
    if not isinstance(value, dict):
        raise ValueError(f"{path} must contain a JSON object")
    return value


class Verification:
    def __init__(self) -> None:
        self.checks: list[dict[str, Any]] = []

    def check(self, name: str, condition: bool, detail: Any) -> None:
        self.checks.append(
            {
                "name": name,
                "result": "PASS" if condition else "FAIL",
                "detail": detail,
            }
        )

    @property
    def passed(self) -> bool:
        return all(item["result"] == "PASS" for item in self.checks)


def resolve_record_path(record: dict[str, Any]) -> Path:
    relative = record["path"]
    if not isinstance(relative, str) or not relative.startswith("dist/"):
        raise ValueError(f"invalid artifact path {relative!r}")
    path = (ROOT / relative).resolve()
    if DIST.resolve() not in path.parents:
        raise ValueError(f"artifact escaped dist: {relative!r}")
    return path


def verify_record(
    verification: Verification,
    name: str,
    record: dict[str, Any],
) -> bytes:
    path = resolve_record_path(record)
    exists = path.is_file()
    verification.check(f"{name}.exists", exists, record["path"])
    if not exists:
        return b""
    raw = path.read_bytes()
    observed = {
        "bytes": len(raw),
        "sha256": sha256_hex(raw),
        "git_blob_sha1": git_blob_sha1(raw),
    }
    expected = {
        "bytes": record["bytes"],
        "sha256": record["sha256"],
        "git_blob_sha1": record["git_blob_sha1"],
    }
    verification.check(
        f"{name}.byte_hash_binding",
        observed == expected,
        {"expected": expected, "observed": observed},
    )
    return raw


def verify_markdown_self_hash(
    verification: Verification,
    tier: str,
    raw: bytes,
    declared: str,
) -> None:
    header_end = raw.find(b"\n---\n", 4)
    verification.check(
        f"{tier}.frontmatter_envelope",
        raw.startswith(b"---\n") and header_end > 4,
        {"closing_delimiter_offset": header_end},
    )
    if header_end < 0:
        return
    header = raw[: header_end + 5]
    matches = list(re.finditer(rb"(?m)^self_hash: ([0-9a-f]{64})$", header))
    field_value = (
        matches[0].group(1).decode("ascii") if len(matches) == 1 else None
    )
    verification.check(
        f"{tier}.self_hash_field",
        len(matches) == 1 and field_value == declared,
        {"matches": len(matches), "declared": declared, "field": field_value},
    )
    if len(matches) != 1:
        return
    placeholder = (
        raw[: matches[0].start(1)]
        + SELF_PLACEHOLDER.encode("ascii")
        + raw[matches[0].end(1) :]
    )
    observed = sha256_hex(canonical_bytes(placeholder))
    verification.check(
        f"{tier}.self_hash_recomputed",
        observed == declared,
        {"declared": declared, "observed": observed},
    )


def verify_xl_self_hash(
    verification: Verification,
    raw: bytes,
    declared: str,
) -> None:
    try:
        value = json.loads(raw.decode("utf-8"))
    except (UnicodeDecodeError, json.JSONDecodeError) as exc:
        verification.check("XL.valid_json", False, str(exc))
        return
    verification.check("XL.valid_json", isinstance(value, dict), "JSON object")
    if not isinstance(value, dict):
        return
    field_value = value.get("self_hash")
    verification.check(
        "XL.self_hash_field",
        field_value == declared,
        {"declared": declared, "field": field_value},
    )
    value["self_hash"] = SELF_PLACEHOLDER
    observed = sha256_hex(stable_json_bytes(value))
    verification.check(
        "XL.self_hash_recomputed",
        observed == declared,
        {"declared": declared, "observed": observed},
    )


def extract_embedded_source(
    raw: bytes,
    source: dict[str, Any],
) -> tuple[bytes | None, str]:
    source_id = source["id"]
    begin = (
        f"<!-- HFO_SOURCE_BEGIN id={source_id} "
        f"blob_sha1={source['blob_sha1']} bytes={source['bytes']} "
        f"sha256={source['sha256']} -->\n"
    ).encode("utf-8")
    end = f"\n<!-- HFO_SOURCE_END id={source_id} -->".encode("utf-8")
    begin_pos = raw.find(begin)
    if begin_pos < 0:
        return None, "begin marker absent"
    content_pos = begin_pos + len(begin)
    end_pos = raw.find(end, content_pos)
    if end_pos < 0:
        return None, "end marker absent"
    if raw.find(begin, content_pos) >= 0:
        return None, "duplicate begin marker"
    return raw[content_pos:end_pos], "found"


def verify_embedded_sources(
    verification: Verification,
    tier: str,
    raw: bytes,
    embedded_ids: list[str],
    sources: dict[str, dict[str, Any]],
) -> None:
    observed_markers = {
        match.group(1).decode("utf-8")
        for match in re.finditer(rb"<!-- HFO_SOURCE_BEGIN id=([^ ]+) ", raw)
    }
    verification.check(
        f"{tier}.embedded_marker_set",
        observed_markers == set(embedded_ids),
        {
            "expected": sorted(embedded_ids),
            "observed": sorted(observed_markers),
        },
    )
    for source_id in embedded_ids:
        source = sources[source_id]
        body, message = extract_embedded_source(raw, source)
        if body is None:
            verification.check(
                f"{tier}.embedded.{source_id}",
                False,
                message,
            )
            continue
        observed = {
            "bytes": len(body),
            "sha256": sha256_hex(body),
            "git_blob_sha1": git_blob_sha1(body),
        }
        expected = {
            "bytes": source["bytes"],
            "sha256": source["sha256"],
            "git_blob_sha1": source["blob_sha1"],
        }
        verification.check(
            f"{tier}.embedded.{source_id}",
            observed == expected,
            {"expected": expected, "observed": observed},
        )


def verify_large_chunks(
    verification: Verification,
    large_raw: bytes,
    large_record: dict[str, Any],
) -> list[bytes]:
    chunk_manifest_path = DIST / "L_LARGE.manifest.json"
    exists = chunk_manifest_path.is_file()
    verification.check(
        "L.chunk_manifest.exists",
        exists,
        "dist/L_LARGE.manifest.json",
    )
    if not exists:
        return []
    value = load_json(chunk_manifest_path)
    chunk_max = value.get("chunk_max_bytes")
    manifest_records = value.get("chunks", [])
    family_records = large_record.get("chunks", [])
    verification.check(
        "L.chunk_records_agree",
        manifest_records == family_records,
        {
            "chunk_manifest_count": len(manifest_records),
            "family_manifest_count": len(family_records),
        },
    )
    chunks: list[bytes] = []
    for position, record in enumerate(manifest_records):
        raw = verify_record(
            verification,
            f"L.chunk.{position:03d}",
            record,
        )
        verification.check(
            f"L.chunk.{position:03d}.order_and_budget",
            record.get("order") == position
            and isinstance(chunk_max, int)
            and len(raw) <= chunk_max,
            {
                "declared_order": record.get("order"),
                "expected_order": position,
                "bytes": len(raw),
                "chunk_max_bytes": chunk_max,
            },
        )
        chunks.append(raw)
    reconstructed = b"".join(chunks)
    verification.check(
        "L.chunk_reconstruction",
        reconstructed == large_raw,
        {
            "reconstructed_bytes": len(reconstructed),
            "bound_bytes": len(large_raw),
            "reconstructed_sha256": sha256_hex(reconstructed),
            "bound_sha256": sha256_hex(large_raw),
        },
    )
    merkle_input = b"".join(
        bytes.fromhex(record["sha256"]) for record in manifest_records
    )
    observed_merkle = sha256_hex(merkle_input)
    declared_merkle = value.get("merkle_root")
    verification.check(
        "L.chunk_merkle",
        observed_merkle == declared_merkle
        and declared_merkle == large_record.get("chunk_merkle_root"),
        {
            "observed": observed_merkle,
            "chunk_manifest": declared_merkle,
            "family_manifest": large_record.get("chunk_merkle_root"),
        },
    )
    return chunks


def leakage_findings(files: dict[str, bytes]) -> list[dict[str, str]]:
    patterns = {
        "pem_private_key": re.compile(rb"-----BEGIN [A-Z ]*PRIVATE KEY-----"),
        "aws_access_key": re.compile(rb"\bAKIA[0-9A-Z]{16}\b"),
        "github_token": re.compile(rb"\bgh[pousr]_[A-Za-z0-9]{30,}\b"),
        "openai_secret": re.compile(rb"\bsk-[A-Za-z0-9_-]{20,}\b"),
        "assigned_secret": re.compile(
            rb"(?i)\b(?:api[_-]?key|password|passwd|client[_-]?secret|"
            rb"private[_-]?key)\b\s*[:=]\s*['\"]?[A-Za-z0-9_./+=-]{16,}"
        ),
        "windows_user_home": re.compile(rb"(?i)\bC:\\Users\\[^\\\s]+"),
        "email_address": re.compile(
            rb"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b"
        ),
        "us_ssn": re.compile(rb"\b\d{3}-\d{2}-\d{4}\b"),
    }
    findings: list[dict[str, str]] = []
    for name, raw in files.items():
        for pattern_name, pattern in patterns.items():
            match = pattern.search(raw)
            if match:
                findings.append(
                    {
                        "artifact": name,
                        "pattern": pattern_name,
                        "sample_sha256": sha256_hex(match.group(0)),
                    }
                )
    return findings


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write-receipt", action="store_true")
    args = parser.parse_args()

    verification = Verification()
    index = load_json(INDEX_PATH)
    manifest = load_json(MANIFEST_PATH)
    capsules = manifest["capsules"]

    raw_by_tier: dict[str, bytes] = {}
    for tier in ("S", "M", "L", "XL"):
        raw_by_tier[tier] = verify_record(
            verification,
            f"{tier}.artifact",
            capsules[tier],
        )

    budgets = {"S": 4096, "M": 32768, "L": 262144}
    for tier, budget in budgets.items():
        record = capsules[tier]
        verification.check(
            f"{tier}.budget",
            record.get("max_bytes") == budget
            and len(raw_by_tier[tier]) <= budget,
            {
                "canonical_budget": budget,
                "declared_budget": record.get("max_bytes"),
                "observed_bytes": len(raw_by_tier[tier]),
            },
        )
        verify_markdown_self_hash(
            verification,
            tier,
            raw_by_tier[tier],
            record["self_hash"],
        )

    verify_xl_self_hash(
        verification,
        raw_by_tier["XL"],
        capsules["XL"]["self_hash"],
    )

    core_path = DIST / "CORE_PAYLOAD.json"
    core_raw = core_path.read_bytes() if core_path.is_file() else b""
    core_sha = sha256_hex(core_raw)
    verification.check(
        "core_payload.binding",
        bool(core_raw) and core_sha == manifest["core_payload_sha256"],
        {
            "declared": manifest["core_payload_sha256"],
            "observed": core_sha,
            "bytes": len(core_raw),
        },
    )
    for tier in ("S", "M", "L"):
        verification.check(
            f"{tier}.core_exact_inclusion",
            bool(core_raw) and raw_by_tier[tier].count(core_raw) == 1,
            {
                "occurrences": raw_by_tier[tier].count(core_raw),
                "core_sha256": core_sha,
            },
        )
        verification.check(
            f"{tier}.core_manifest_agreement",
            capsules[tier]["core_payload_sha256"] == core_sha,
            capsules[tier]["core_payload_sha256"],
        )
    verification.check(
        "XL.core_manifest_agreement",
        capsules["XL"]["core_payload_sha256"] == core_sha,
        capsules["XL"]["core_payload_sha256"],
    )

    pointer_sets = {
        tier: set(capsules[tier]["pointer_source_ids"])
        for tier in ("S", "M", "L", "XL")
    }
    embedded_sets = {
        tier: set(capsules[tier]["embedded_source_ids"])
        for tier in ("S", "M", "L")
    }
    verification.check(
        "tier.pointer_monotonicity",
        pointer_sets["S"]
        <= pointer_sets["M"]
        <= pointer_sets["L"]
        <= pointer_sets["XL"],
        {tier: sorted(values) for tier, values in pointer_sets.items()},
    )
    verification.check(
        "tier.embedded_monotonicity",
        embedded_sets["S"] <= embedded_sets["M"] <= embedded_sets["L"],
        {tier: sorted(values) for tier, values in embedded_sets.items()},
    )

    sources = {
        item["id"]: item
        for item in index["embedded_sources"] + index["pointer_sources"]
    }
    expected_all = set(sources)
    verification.check(
        "XL.pointer_coverage",
        pointer_sets["XL"] == expected_all,
        {
            "expected": sorted(expected_all),
            "observed": sorted(pointer_sets["XL"]),
        },
    )
    for tier in ("S", "M", "L"):
        expected_pointer = set(index["tier_policy"][tier]["pointer_source_ids"])
        expected_embedded = set(
            index["tier_policy"][tier]["embedded_source_ids"]
        )
        verification.check(
            f"{tier}.index_pointer_agreement",
            pointer_sets[tier] == expected_pointer,
            sorted(pointer_sets[tier]),
        )
        verification.check(
            f"{tier}.index_embedded_agreement",
            embedded_sets[tier] == expected_embedded,
            sorted(embedded_sets[tier]),
        )
        verify_embedded_sources(
            verification,
            tier,
            raw_by_tier[tier],
            capsules[tier]["embedded_source_ids"],
            sources,
        )

    chunks = verify_large_chunks(
        verification,
        raw_by_tier["L"],
        capsules["L"],
    )

    source_receipt_path = DIST / "SOURCE_BINDING_RECEIPT.json"
    source_receipt = (
        load_json(source_receipt_path) if source_receipt_path.is_file() else {}
    )
    bound_sources = source_receipt.get("sources", [])
    verification.check(
        "source_binding_receipt",
        source_receipt.get("result") == "PASS"
        and len(bound_sources) == len(index["embedded_sources"])
        and all(item.get("result") == "PASS" for item in bound_sources),
        {
            "result": source_receipt.get("result"),
            "source_count": len(bound_sources),
            "expected_source_count": len(index["embedded_sources"]),
        },
    )

    scan_files = {
        "S_SMALL.soul.md": raw_by_tier["S"],
        "M_MEDIUM.soul.md": raw_by_tier["M"],
        "L_LARGE.bound.md": raw_by_tier["L"],
        "XL_XLARGE.pointer.json": raw_by_tier["XL"],
        "CORE_PAYLOAD.json": core_raw,
        **{
            f"L_chunk_{position:03d}": raw
            for position, raw in enumerate(chunks)
        },
    }
    findings = leakage_findings(scan_files)
    verification.check(
        "bounded_secret_and_pii_scan",
        not findings,
        findings,
    )

    verification.check(
        "claim_ceiling",
        manifest.get("claim_status") == "partial"
        and manifest.get("publication_status") == "NOT_UPLOADED"
        and manifest.get("independent_review") == "ABSENT"
        and manifest.get("sealed") is False
        and all(
            capsules[tier].get("evidence_tier") == "T2_BOUND_PROVISIONAL"
            for tier in ("S", "M", "L")
        )
        and capsules["XL"].get("evidence_tier") == "T0_POINTER",
        {
            "claim_status": manifest.get("claim_status"),
            "publication_status": manifest.get("publication_status"),
            "independent_review": manifest.get("independent_review"),
            "sealed": manifest.get("sealed"),
        },
    )

    result = "PASS" if verification.passed else "FAIL"
    receipt = {
        "schema_id": "hfo.gen133.sigrun_capsule_verification_receipt.v1",
        "valid_time_utc": index["valid_time_utc"],
        "transaction_time_utc": index["built_time_utc"],
        "result": result,
        "checks": verification.checks,
        "capsule_sizes": {
            tier: len(raw_by_tier[tier]) for tier in ("S", "M", "L", "XL")
        },
        "claim_status": "partial",
        "evidence_tier": "T2_BOUND_PROVISIONAL" if result == "PASS" else "T0",
        "honest_flaw": (
            "This verifier is a separate process and implementation, but it ran "
            "on the same host and is not a non-author held-out re-instantiation."
        ),
        "falsifier": (
            "Any independent byte/hash disagreement, source leakage, behavioral "
            "re-instantiation failure, or public-rights rejection."
        ),
        "next_safe_action": (
            "Commit exact generated bytes and route their Git readback to a "
            "distinct held-out reviewer."
        ),
        "effect_ceiling": "T0_INTERNAL_ONLY",
        "sealed": False,
    }
    if args.write_receipt:
        RECEIPT_PATH.write_bytes(stable_json_bytes(receipt))
    print(
        json.dumps(
            {
                "result": result,
                "checks": len(verification.checks),
                "failed": [
                    item["name"]
                    for item in verification.checks
                    if item["result"] == "FAIL"
                ],
                "capsule_sizes": receipt["capsule_sizes"],
                "receipt": (
                    str(RECEIPT_PATH.relative_to(ROOT))
                    if args.write_receipt
                    else None
                ),
            },
            sort_keys=True,
        )
    )
    return 0 if verification.passed else 1


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as exc:
        print(f"VERIFY_FAIL: {exc}", file=sys.stderr)
        raise
