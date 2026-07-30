#!/usr/bin/env python3
"""Render the only admissible v4 rehydration view."""

from __future__ import annotations

import argparse
import importlib.util
from pathlib import Path


ROOT = Path(__file__).resolve().parent
V3_LOADER = ROOT.parent / "v3" / "render_rehydration_view.py"


def load_v3_loader():
    spec = importlib.util.spec_from_file_location("hfo_sigrun_v3_loader_for_v4", V3_LOADER)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load v3 loader: {V3_LOADER}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def safe_view(raw: bytes) -> bytes:
    return load_v3_loader().safe_view(raw)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("capsule", type=Path)
    args = parser.parse_args()
    print(safe_view(args.capsule.read_bytes()).decode("utf-8"), end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
