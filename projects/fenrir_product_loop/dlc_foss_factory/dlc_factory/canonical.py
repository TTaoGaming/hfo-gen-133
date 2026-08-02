"""Canonical encoding, hashing, and conservative secret rejection."""

from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path
from typing import Any

from .errors import SecretRejected


_SECRET_KEY = re.compile(
    r"(?:^|_)(?:api_?key|access_?token|refresh_?token|password|passwd|secret|"
    r"private_?key|credential|authorization)(?:$|_)",
    re.IGNORECASE,
)
_SECRET_VALUES = (
    re.compile(r"-----BEGIN [A-Z0-9 ]*PRIVATE KEY-----"),
    re.compile(r"\bgh[pousr]_[A-Za-z0-9]{20,}\b"),
    re.compile(r"\b(?:sk|rk)-[A-Za-z0-9_-]{16,}\b"),
    re.compile(r"\bAKIA[0-9A-Z]{16}\b"),
    re.compile(r"\bBearer\s+[A-Za-z0-9._~-]{16,}\b", re.IGNORECASE),
)


def canonical_json_bytes(value: Any) -> bytes:
    """Return deterministic UTF-8 JSON bytes with one trailing newline."""

    return (
        json.dumps(
            value,
            ensure_ascii=False,
            allow_nan=False,
            sort_keys=True,
            separators=(",", ":"),
        )
        + "\n"
    ).encode("utf-8")


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def assert_no_secrets(value: Any, path: str = "$") -> None:
    """Reject obvious credential keys and high-confidence credential values."""

    if isinstance(value, dict):
        for key, child in value.items():
            key_text = str(key)
            if _SECRET_KEY.search(key_text):
                raise SecretRejected(f"potential credential field rejected at {path}.{key_text}")
            assert_no_secrets(child, f"{path}.{key_text}")
        return
    if isinstance(value, list):
        for index, child in enumerate(value):
            assert_no_secrets(child, f"{path}[{index}]")
        return
    if isinstance(value, str):
        for pattern in _SECRET_VALUES:
            if pattern.search(value):
                raise SecretRejected(f"potential credential value rejected at {path}")


def contains_secret_text(value: str) -> bool:
    return any(pattern.search(value) for pattern in _SECRET_VALUES)
