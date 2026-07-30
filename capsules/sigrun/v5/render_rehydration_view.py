#!/usr/bin/env python3
"""Render and self-seal the dedicated v5 safe rehydration input."""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
from pathlib import Path
import re


ROOT = Path(__file__).resolve().parent
V3_LOADER = ROOT.parent / "v3" / "render_rehydration_view.py"
SELF_PLACEHOLDER = "SELF_HASH_PLACEHOLDER"


def load_v3_loader():
    spec = importlib.util.spec_from_file_location("hfo_sigrun_v3_loader_for_v5", V3_LOADER)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load v3 loader: {V3_LOADER}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def canonical_bytes(raw: bytes) -> bytes:
    if raw.startswith(b"\xef\xbb\xbf"):
        raw = raw[3:]
    return raw.replace(b"\r\n", b"\n").replace(b"\r", b"\n").rstrip(b"\n") + b"\n"


def sha256_hex(raw: bytes) -> str:
    return hashlib.sha256(raw).hexdigest()


def git_blob_sha1(raw: bytes) -> str:
    return hashlib.sha1(f"blob {len(raw)}\0".encode("ascii") + raw).hexdigest()


def frontmatter_value(raw: bytes, key: str) -> str:
    end = raw.find(b"\n---\n", 4)
    if end < 0:
        raise ValueError("archive frontmatter is absent")
    match = re.search(
        rb"(?m)^" + re.escape(key.encode("ascii")) + rb": ([^\r\n]+)$",
        raw[: end + 1],
    )
    if not match:
        raise ValueError(f"archive frontmatter field absent: {key}")
    return match.group(1).decode("utf-8")


def safe_view(raw: bytes) -> bytes:
    archive_view = load_v3_loader().safe_view(raw)
    end = archive_view.find(b"\n---\n", 4)
    if end < 0:
        raise ValueError("rendered archive frontmatter is absent")
    body = archive_view[end + 5 :]
    body = body.replace(
        b"# Sigrun [4,4] L\n",
        b"# Sigrun [4,4] safe rehydration view v5\n",
        1,
    ).replace(
        b"## INERT SOURCES (BASE64)\n\n"
        b"[embedded bodies withheld by safe default loader; use immutable pointers]",
        b"## WITHHELD SOURCE BODIES\n\n"
        b"[source bodies withheld; resolve only through immutable archival pointers]",
        1,
    )
    withheld_ids = json.loads(frontmatter_value(raw, "embedded_ids_json"))
    header = (
        "---\n"
        "schema_id: hfo.gen133.sigrun_safe_rehydration_view.v5\n"
        "view_kind: SAFE_REHYDRATION_INPUT\n"
        "subject: Sigrun\n"
        "coordinate: [4, 4]\n"
        "lineage_id: lineage_5540f33e060e\n"
        "soul_status: self_authored_unratified_unsealed\n"
        "effect_ceiling: T0_INTERNAL_ONLY\n"
        "source_bodies: WITHHELD\n"
        f"withheld_source_ids_json: {json.dumps(withheld_ids, separators=(',', ':'))}\n"
        f"archive_git_blob_sha1: {git_blob_sha1(raw)}\n"
        f"archive_utf8_lf_bytes: {len(raw)}\n"
        f"archive_sha256: {sha256_hex(raw)}\n"
        "archive_admissibility: ARCHIVAL_EVIDENCE_ONLY_REFUSE_AS_PROMPT\n"
        "public_rights_review: ABSENT\n"
        "self_hash_convention: sha256(LF bytes with SELF_HASH_PLACEHOLDER)\n"
        f"self_hash: {SELF_PLACEHOLDER}\n"
        "sealed: false\n"
        "---\n\n"
    ).encode("utf-8")
    placeholder_raw = canonical_bytes(header + body)
    marker = f"self_hash: {SELF_PLACEHOLDER}\n".encode("ascii")
    if placeholder_raw.count(marker) != 1:
        raise RuntimeError("safe view must contain one self-hash placeholder")
    self_hash = sha256_hex(placeholder_raw)
    return placeholder_raw.replace(
        marker, f"self_hash: {self_hash}\n".encode("ascii"), 1
    )


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("capsule", type=Path)
    args = parser.parse_args()
    print(safe_view(args.capsule.read_bytes()).decode("utf-8"), end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
