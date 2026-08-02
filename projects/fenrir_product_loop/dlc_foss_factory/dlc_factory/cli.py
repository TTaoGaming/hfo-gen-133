"""Dependency-light command-line interface for the factory scaffold."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any, Sequence

from .errors import (
    AdapterFailure,
    FactoryError,
    MaterializationConflict,
    PathTraversalError,
    ReceiptIntegrityError,
    SecretRejected,
    SpecValidationError,
    WipCollisionError,
)
from .lease import package_runs_root
from .provenance import preflight
from .receipt import ReceiptStore
from .runtime import FactoryRuntime
from .spec import load_spec, spec_sha256


def _emit(value: Any, *, stream: Any = sys.stdout) -> None:
    print(json.dumps(value, ensure_ascii=False, sort_keys=True, indent=2), file=stream)


def _parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="dlc-factory",
        description="Target-agnostic, NON_PRODUCTION DLC-style extension factory scaffold.",
    )
    commands = parser.add_subparsers(dest="command", required=True)
    validate = commands.add_parser("validate")
    validate.add_argument("--spec", type=Path, required=True)
    check = commands.add_parser("preflight")
    check.add_argument("--spec", type=Path, required=True)
    check.add_argument("--license-file", type=Path)
    for name in ("materialize", "run"):
        command = commands.add_parser(name)
        command.add_argument("--spec", type=Path, required=True)
    verify = commands.add_parser("verify-receipt")
    verify.add_argument("--sha256", required=True)
    return parser


def _summary(result: dict[str, Any]) -> dict[str, Any]:
    lifecycle = result["lifecycle"]
    return {
        "run_id": result["intent"]["run_id"],
        "unit_spec_sha256": result["intent"]["unit_spec_sha256"],
        "artifact_tree_sha256": result["materialization"]["tree_sha256"],
        "materialization_created": result["materialization"]["created"],
        "status": lifecycle["status"],
        "ok": lifecycle["ok"],
        "stage_exits": [
            {"stage": row["stage"], "exit_code": row["exit_code"], "ok": row["ok"]}
            for row in lifecycle["stage_results"]
        ],
        "rollback_exit": (
            None if lifecycle["rollback_result"] is None else lifecycle["rollback_result"]["exit_code"]
        ),
        "receipt": lifecycle["receipt_ref"],
        "claim_scope": "LOCAL_REGRESSION",
        "independent_verification": False,
        "target_admitted": False,
    }


def main(argv: Sequence[str] | None = None) -> int:
    args = _parser().parse_args(argv)
    try:
        if args.command == "validate":
            spec = load_spec(args.spec)
            _emit(
                {
                    "status": "VALID",
                    "classification": spec["classification"],
                    "unit_id": spec["unit_id"],
                    "unit_spec_sha256": spec_sha256(spec),
                }
            )
            return 0
        if args.command == "preflight":
            license_bytes = None if args.license_file is None else args.license_file.read_bytes()
            result = preflight(load_spec(args.spec), license_bytes)
            _emit(result)
            return 0 if result["review_ready"] else 5
        if args.command == "materialize":
            _emit(FactoryRuntime().materialize(load_spec(args.spec)))
            return 0
        if args.command == "run":
            summary = _summary(FactoryRuntime().run(load_spec(args.spec)))
            _emit(summary)
            if summary["ok"]:
                return 0
            return 7 if summary["status"].startswith("ROLLBACK_FAILED") else 6
        if args.command == "verify-receipt":
            receipt = ReceiptStore(package_runs_root()).verify(
                Path("sha256") / args.sha256 / "receipt.json"
            )
            _emit(
                {
                    "status": "VERIFIED",
                    "receipt_sha256": args.sha256,
                    "receipt_schema_id": receipt["schema_id"],
                    "claim": receipt["claim"],
                }
            )
            return 0
        raise AssertionError(f"unhandled command: {args.command}")
    except (SecretRejected, PathTraversalError, SpecValidationError) as error:
        _emit({"status": "REJECTED_INPUT", "error": str(error)}, stream=sys.stderr)
        return 3
    except WipCollisionError as error:
        _emit({"status": "WIP_COLLISION", "error": str(error)}, stream=sys.stderr)
        return 4
    except AdapterFailure as error:
        _emit({"status": "ADAPTER_FAILURE", "error": str(error)}, stream=sys.stderr)
        return 6
    except ReceiptIntegrityError as error:
        _emit({"status": "RECEIPT_INTEGRITY_FAILURE", "error": str(error)}, stream=sys.stderr)
        return 8
    except MaterializationConflict as error:
        _emit({"status": "MATERIALIZATION_CONFLICT", "error": str(error)}, stream=sys.stderr)
        return 9
    except OSError as error:
        _emit({"status": "LOCAL_IO_FAILURE", "error": type(error).__name__}, stream=sys.stderr)
        return 2
    except FactoryError as error:
        _emit({"status": "FACTORY_FAILURE", "error": str(error)}, stream=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
