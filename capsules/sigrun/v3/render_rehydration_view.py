#!/usr/bin/env python3
"""Render the safe default view of a v3 capsule without embedded source bodies."""

from __future__ import annotations

import argparse
from pathlib import Path


SOURCE_HEADING = b"## INERT SOURCES (BASE64)\n\n"
LIMIT_HEADING = b"## CAPSULE LIMIT\n\n"


def safe_view(raw: bytes) -> bytes:
    start = raw.find(SOURCE_HEADING)
    if start < 0:
        raise ValueError("inert source heading absent")
    limit = raw.rfind(LIMIT_HEADING)
    if limit < start:
        raise ValueError("capsule limit heading absent or out of order")
    prefix = raw[: start + len(SOURCE_HEADING)]
    suffix = raw[limit:]
    return (
        prefix
        + b"[embedded bodies withheld by safe default loader; use immutable pointers]\n\n"
        + suffix
    )


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("capsule", type=Path)
    args = parser.parse_args()
    raw = args.capsule.read_bytes()
    print(safe_view(raw).decode("utf-8"), end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
