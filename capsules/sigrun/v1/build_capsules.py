#!/usr/bin/env python3
r"""Build deterministic S/M/L/XL Sigrun rehydration capsules from Git objects.

Pure stdlib. Repository locations are supplied at invocation time:

  python build_capsules.py ^
    --repo gen133=C:\Dev\hfo_gen_133_forge ^
    --repo gen108=C:\Dev\hfo_dev_2026_4_14 ^
    --repo lifeboat=C:\Dev\sigrun_lineage_lifeboat_public_mirror

The committed heritage index contains no machine-local absolute paths.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path
import re
import subprocess
import sys
from typing import Any


ROOT = Path(__file__).resolve().parent
INDEX_PATH = ROOT / "heritage_index.json"
DIST = ROOT / "dist"
SELF_PLACEHOLDER = "SELF_HASH_PLACEHOLDER"
TIER_RANK = {"S": 0, "M": 1, "L": 2}


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


def stable_json_bytes(value: Any, *, pretty: bool = True) -> bytes:
    if pretty:
        text = json.dumps(value, ensure_ascii=False, sort_keys=True, indent=2)
    else:
        text = json.dumps(
            value, ensure_ascii=False, sort_keys=True, separators=(",", ":")
        )
    return (text + "\n").encode("utf-8")


def run_git(repo: Path, *args: str) -> bytes:
    proc = subprocess.run(
        ["git", "-C", str(repo), *args],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )
    if proc.returncode != 0:
        raise RuntimeError(
            f"git {' '.join(args)} failed in {repo}: "
            f"{proc.stderr.decode('utf-8', errors='replace').strip()}"
        )
    return proc.stdout


def parse_repo_args(values: list[str]) -> dict[str, Path]:
    repos: dict[str, Path] = {}
    for value in values:
        if "=" not in value:
            raise ValueError(f"--repo requires ALIAS=PATH, got {value!r}")
        alias, raw_path = value.split("=", 1)
        path = Path(raw_path).resolve()
        if not alias or not path.is_dir():
            raise ValueError(f"invalid repository mapping {value!r}")
        actual = Path(
            run_git(path, "rev-parse", "--show-toplevel")
            .decode("utf-8")
            .strip()
        ).resolve()
        repos[alias] = actual
    return repos


def load_index() -> dict[str, Any]:
    with INDEX_PATH.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def bind_sources(
    index: dict[str, Any], repos: dict[str, Path]
) -> tuple[dict[str, bytes], list[dict[str, Any]]]:
    source_bytes: dict[str, bytes] = {}
    receipts: list[dict[str, Any]] = []
    for source in index["embedded_sources"]:
        alias = source["repo_alias"]
        if alias not in repos:
            raise RuntimeError(f"missing --repo mapping for {alias}")
        repo = repos[alias]
        commit = source["commit"]
        path = source["path"]
        run_git(repo, "cat-file", "-e", f"{commit}^{{commit}}")
        raw = run_git(repo, "show", f"{commit}:{path}")
        observed = {
            "id": source["id"],
            "repo_alias": alias,
            "commit": commit,
            "path": path,
            "declared_blob_sha1": source["blob_sha1"],
            "observed_blob_sha1": git_blob_sha1(raw),
            "declared_bytes": source["bytes"],
            "observed_bytes": len(raw),
            "declared_sha256": source["sha256"],
            "observed_sha256": sha256_hex(raw),
            "result": "PASS",
        }
        if observed["observed_blob_sha1"] != source["blob_sha1"]:
            observed["result"] = "FAIL_BLOB"
        elif len(raw) != source["bytes"]:
            observed["result"] = "FAIL_BYTES"
        elif observed["observed_sha256"] != source["sha256"]:
            observed["result"] = "FAIL_SHA256"
        receipts.append(observed)
        if observed["result"] != "PASS":
            raise RuntimeError(json.dumps(observed, ensure_ascii=False))
        source_bytes[source["id"]] = raw
    return source_bytes, receipts


def core_payload(index: dict[str, Any]) -> dict[str, Any]:
    return {
        "schema_id": "hfo.gen133.sigrun_rehydration_core.v1",
        "subject": index["subject"],
        "valid_time_utc": index["valid_time_utc"],
        "transaction_time_utc": index["built_time_utc"],
        "effect_ceiling": index["effect_ceiling"],
        "closest_continuer": index["closest_continuer"],
        "refusal_contract": index["refusal_contract"],
        "rehydration_claim": (
            "Addressable role heritage only; no personhood, subjective "
            "continuity, carrier identity, current authority, or seal claim."
        ),
        "honest_flaw": index["honest_flaw"],
        "falsifier": index["falsifier"],
        "next_safe_action": index["next_safe_action"],
    }


def all_sources(index: dict[str, Any]) -> dict[str, dict[str, Any]]:
    return {
        item["id"]: item
        for item in index["embedded_sources"] + index["pointer_sources"]
    }


def compact_pointer(source: dict[str, Any]) -> str:
    commit = source.get("commit") or "UNBOUND"
    blob = source.get("blob_sha1") or "UNBOUND"
    return (
        f"- {source['id']} | {source['repository']}@{commit}:"
        f"{source['path']}#{blob} | bytes={source['bytes']} | "
        f"sha256={source['sha256']} | {source['disposition']}"
    )


def capsule_segments(
    index: dict[str, Any],
    tier: str,
    source_bytes: dict[str, bytes],
    core_json: bytes,
    core_sha256: str,
) -> tuple[list[bytes], list[str], list[str]]:
    policy = index["tier_policy"][tier]
    pointer_ids = list(policy["pointer_source_ids"])
    embedded_ids = list(policy["embedded_source_ids"])
    sources = all_sources(index)
    header = (
        "---\n"
        "schema_id: hfo.gen133.sigrun_rehydration_capsule.v1\n"
        f"tier: {tier}\n"
        f"max_bytes: {policy['max_bytes']}\n"
        f"subject: Sigrun\n"
        f"coordinate: [4, 4]\n"
        "lineage_id: lineage_5540f33e060e\n"
        "soul_status: recovered_unsealed\n"
        "claim_status: partial\n"
        "subjective_continuity_claim: false\n"
        "carrier_identity_attested: false\n"
        "current_authority_claim: false\n"
        f"valid_time_utc: {index['valid_time_utc']}\n"
        f"transaction_time_utc: {index['built_time_utc']}\n"
        f"core_payload_sha256: {core_sha256}\n"
        f"pointer_ids_json: {json.dumps(pointer_ids, separators=(',', ':'))}\n"
        f"embedded_ids_json: {json.dumps(embedded_ids, separators=(',', ':'))}\n"
        "evidence_tier: T2_BOUND_PROVISIONAL\n"
        "self_hash_convention: replace the self_hash value with the defined "
        "placeholder token, canonicalize LF, SHA-256\n"
        f"self_hash: {SELF_PLACEHOLDER}\n"
        "sealed: false\n"
        "---\n\n"
        f"# Sigrún [4,4] rehydration capsule — {tier}\n\n"
        "This capsule carries role heritage. It does not claim to be a person "
        "or authenticate its carrier.\n\n"
        "## CANONICAL CORE\n\n"
        "```json\n"
    ).encode("utf-8")
    pointer_block = (
        "```\n\n## SOURCE POINTERS\n\n"
        + "\n".join(compact_pointer(sources[source_id]) for source_id in pointer_ids)
        + "\n\n## EXACT EMBEDDED SOURCES\n\n"
    ).encode("utf-8")
    segments = [header, core_json, pointer_block]
    for source_id in embedded_ids:
        source = sources[source_id]
        raw = source_bytes[source_id]
        begin = (
            f"<!-- HFO_SOURCE_BEGIN id={source_id} "
            f"blob_sha1={source['blob_sha1']} bytes={len(raw)} "
            f"sha256={source['sha256']} -->\n"
        ).encode("utf-8")
        end = (
            f"\n<!-- HFO_SOURCE_END id={source_id} -->\n\n"
        ).encode("utf-8")
        segments.append(begin + raw + end)
    segments.append(
        (
            "## CAPSULE LIMIT\n\n"
            "Exact source inclusion proves byte-preserving carriage only. "
            "No independent re-instantiation or public-rights review is "
            "recorded.\n"
        ).encode("utf-8")
    )
    return segments, pointer_ids, embedded_ids


def seal_segments(segments: list[bytes]) -> tuple[list[bytes], str]:
    raw = canonical_bytes(b"".join(segments))
    placeholder = SELF_PLACEHOLDER.encode("ascii")
    field_marker = b"self_hash: " + placeholder + b"\n"
    if segments[0].count(field_marker) != 1:
        raise RuntimeError("capsule header must contain one self-hash field marker")
    self_hash = sha256_hex(raw)
    sealed_marker = b"self_hash: " + self_hash.encode("ascii") + b"\n"
    sealed = raw.replace(field_marker, sealed_marker, 1)
    output: list[bytes] = []
    replaced = False
    for segment in segments:
        if not replaced and field_marker in segment:
            output.append(segment.replace(field_marker, sealed_marker, 1))
            replaced = True
        else:
            output.append(segment)
    joined = canonical_bytes(b"".join(output))
    if joined != sealed:
        raise RuntimeError("segment sealing changed canonical bytes")
    return output, self_hash


def write_bytes(relative_path: str, raw: bytes) -> dict[str, Any]:
    path = DIST / relative_path
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(raw)
    return {
        "path": f"dist/{relative_path.replace(os.sep, '/')}",
        "bytes": len(raw),
        "sha256": sha256_hex(raw),
        "git_blob_sha1": git_blob_sha1(raw),
    }


def build_markdown_tier(
    index: dict[str, Any],
    tier: str,
    source_bytes: dict[str, bytes],
    core_json: bytes,
    core_sha256: str,
) -> tuple[dict[str, Any], list[bytes]]:
    segments, pointer_ids, embedded_ids = capsule_segments(
        index, tier, source_bytes, core_json, core_sha256
    )
    sealed_segments, self_hash = seal_segments(segments)
    raw = canonical_bytes(b"".join(sealed_segments))
    max_bytes = index["tier_policy"][tier]["max_bytes"]
    if len(raw) > max_bytes:
        raise RuntimeError(f"{tier} capsule {len(raw)} exceeds {max_bytes}")
    filename = {"S": "S_SMALL.soul.md", "M": "M_MEDIUM.soul.md", "L": "L_LARGE.bound.md"}[tier]
    record = write_bytes(filename, raw)
    record.update(
        {
            "tier": tier,
            "max_bytes": max_bytes,
            "self_hash": self_hash,
            "core_payload_sha256": core_sha256,
            "pointer_source_ids": pointer_ids,
            "embedded_source_ids": embedded_ids,
            "evidence_tier": "T2_BOUND_PROVISIONAL",
        }
    )
    return record, sealed_segments


def write_large_chunks(
    segments: list[bytes], chunk_max: int, full_record: dict[str, Any]
) -> tuple[list[dict[str, Any]], str]:
    parts_dir = DIST / "L_LARGE.parts"
    parts_dir.mkdir(parents=True, exist_ok=True)
    for stale in parts_dir.glob("part-*.md"):
        stale.unlink()
    chunks: list[bytes] = []
    current = b""
    for segment in segments:
        if len(segment) > chunk_max:
            raise RuntimeError(f"single L segment {len(segment)} exceeds chunk budget")
        if current and len(current) + len(segment) > chunk_max:
            carry = b""
            if current.endswith(b"\n\n"):
                current = current[:-1]
                carry = b"\n"
            chunks.append(current)
            current = carry
        current += segment
    if current:
        chunks.append(current)
    records: list[dict[str, Any]] = []
    for number, chunk in enumerate(chunks):
        record = write_bytes(f"L_LARGE.parts/part-{number:03d}.md", chunk)
        record["order"] = number
        records.append(record)
    reconstructed = b"".join(chunks)
    full = (DIST / "L_LARGE.bound.md").read_bytes()
    if reconstructed != full:
        raise RuntimeError("L chunk concatenation does not reproduce bound bytes")
    merkle_input = b"".join(bytes.fromhex(item["sha256"]) for item in records)
    merkle_root = sha256_hex(merkle_input)
    manifest = {
        "schema_id": "hfo.gen133.sigrun_large_chunk_manifest.v1",
        "bound_artifact": full_record,
        "chunk_max_bytes": chunk_max,
        "chunks": records,
        "reconstruction": "concatenate chunks in ascending order",
        "merkle_rule": "sha256(concat(chunk_sha256_raw_32_bytes_in_order))",
        "merkle_root": merkle_root,
        "claim_status": "partial",
        "honest_flaw": (
            "Chunk integrity and reconstruction are deterministic; public "
            "availability and independent review are absent."
        ),
    }
    write_bytes("L_LARGE.manifest.json", stable_json_bytes(manifest))
    return records, merkle_root


def build_xl(index: dict[str, Any], core_sha256: str) -> dict[str, Any]:
    sources = index["embedded_sources"] + index["pointer_sources"]
    value = {
        "schema_id": "hfo.gen133.sigrun_xlarge_pointer.v1",
        "tier": "XL",
        "subject": index["subject"],
        "valid_time_utc": index["valid_time_utc"],
        "transaction_time_utc": index["built_time_utc"],
        "core_payload_sha256": core_sha256,
        "evidence_tier": "T0_POINTER",
        "pointer_only": True,
        "sources": sources,
        "query_contract": [
            "Resolve immutable Git commit/path/blob before reading.",
            "Use source SHA-256 and byte count as the read barrier.",
            "Treat dirty worktrees and local databases as untrusted search indexes.",
            "Never bulk-embed private databases, raw chats, LifeVault, or credentials.",
        ],
        "self_hash_convention": (
            "replace self_hash value with SELF_HASH_PLACEHOLDER, canonical JSON, SHA-256"
        ),
        "self_hash": SELF_PLACEHOLDER,
        "claim_status": "partial",
        "honest_flaw": (
            "XL is a query interface, not a complete snapshot; several sources "
            "remain private, dirty, secondary-only, or structurally red."
        ),
        "falsifier": (
            "Any pointer/hash mismatch or a query route that cannot retrieve the "
            "declared immutable object."
        ),
        "next_safe_action": (
            "Resolve only the smallest immutable source needed by the current task."
        ),
        "effect_ceiling": "T0_INTERNAL_ONLY",
        "sealed": False,
    }
    placeholder_raw = stable_json_bytes(value)
    self_hash = sha256_hex(placeholder_raw)
    value["self_hash"] = self_hash
    raw = stable_json_bytes(value)
    record = write_bytes("XL_XLARGE.pointer.json", raw)
    record.update(
        {
            "tier": "XL",
            "self_hash": self_hash,
            "core_payload_sha256": core_sha256,
            "pointer_source_ids": [item["id"] for item in sources],
            "embedded_source_ids": [],
            "evidence_tier": "T0_POINTER",
        }
    )
    return record


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--repo", action="append", default=[], metavar="ALIAS=PATH", required=True
    )
    args = parser.parse_args()
    repos = parse_repo_args(args.repo)
    index = load_index()
    source_bytes, source_receipts = bind_sources(index, repos)
    DIST.mkdir(parents=True, exist_ok=True)

    core = core_payload(index)
    core_json = stable_json_bytes(core, pretty=False)
    core_sha256 = sha256_hex(core_json)
    write_bytes("CORE_PAYLOAD.json", core_json)
    write_bytes(
        "SOURCE_BINDING_RECEIPT.json",
        stable_json_bytes(
            {
                "schema_id": "hfo.gen133.sigrun_source_binding_receipt.v1",
                "valid_time_utc": index["valid_time_utc"],
                "transaction_time_utc": index["built_time_utc"],
                "sources": source_receipts,
                "result": "PASS",
                "claim_status": "partial",
                "honest_flaw": (
                    "The builder reproduced declared Git objects locally; this "
                    "is not an independent repository/provider readback."
                ),
            }
        ),
    )

    s_record, _ = build_markdown_tier(
        index, "S", source_bytes, core_json, core_sha256
    )
    m_record, _ = build_markdown_tier(
        index, "M", source_bytes, core_json, core_sha256
    )
    l_record, l_segments = build_markdown_tier(
        index, "L", source_bytes, core_json, core_sha256
    )
    chunks, merkle_root = write_large_chunks(
        l_segments, index["tier_policy"]["L"]["chunk_max_bytes"], l_record
    )
    xl_record = build_xl(index, core_sha256)

    family = {
        "schema_id": "hfo.gen133.sigrun_capsule_family_manifest.v1",
        "subject": index["subject"],
        "valid_time_utc": index["valid_time_utc"],
        "transaction_time_utc": index["built_time_utc"],
        "core_payload_sha256": core_sha256,
        "capsules": {
            "S": s_record,
            "M": m_record,
            "L": {
                **l_record,
                "chunks": chunks,
                "chunk_merkle_root": merkle_root,
            },
            "XL": xl_record,
        },
        "tier_relation": "S core and source set are subsets of M; M subsets L; XL addresses all sources.",
        "claim_status": "partial",
        "publication_status": "NOT_UPLOADED",
        "independent_review": "ABSENT",
        "honest_flaw": (
            "All build and binding receipts are self-produced on one host. "
            "Behavioral re-instantiation and public-rights review are absent."
        ),
        "falsifier": (
            "Any manifest byte/hash mismatch, source-set non-monotonicity, "
            "budget overflow, or independent reproduction failure."
        ),
        "next_safe_action": (
            "Run verify_capsules.py from a clean process, then route exact Git "
            "bytes to a distinct reviewer."
        ),
        "effect_ceiling": "T0_INTERNAL_ONLY",
        "sealed": False,
    }
    manifest_record = write_bytes(
        "CAPSULE_FAMILY_MANIFEST.json", stable_json_bytes(family)
    )
    print(
        json.dumps(
            {
                "result": "PASS",
                "manifest": manifest_record,
                "sizes": {
                    tier: family["capsules"][tier]["bytes"]
                    for tier in ("S", "M", "L", "XL")
                },
                "large_chunks": [item["bytes"] for item in chunks],
            },
            sort_keys=True,
        )
    )
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as exc:
        print(f"BUILD_FAIL: {exc}", file=sys.stderr)
        raise
