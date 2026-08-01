#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


FORGE_ROOT = Path(__file__).resolve().parents[1]
BALLOT_SCHEMA = "hfo.gen130.free_vendor_mesh.litellm_family_ballot.v0_1"
EXPECTED_FAMILIES = ("family_a", "family_b", "family_c")
DEFAULT_RUN_DIRS = (
    FORGE_ROOT / "state/sigrun/wake_runner_free_mesh_runs/noria-p0-20260614T012618Z",
    FORGE_ROOT / "state/sigrun/wake_runner_free_mesh_runs/noria-p6-20260614T013002Z",
)


def stable_json(value: Any) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=True)


def sha256_text(value: str) -> str:
    return hashlib.sha256(value.encode("utf-8")).hexdigest()


def expected_question_id(run_dir: Path) -> str:
    return run_dir.name


def family_from_name(path: Path) -> str:
    name = path.name
    for family in EXPECTED_FAMILIES:
        if f"_{family}." in name or f"-{family}." in name:
            return family
    return "unknown"


def classify_ballot(raw_text: str, *, family: str, question_id: str) -> dict[str, Any]:
    classes: list[str] = []
    try:
        ballot = json.loads(raw_text)
    except json.JSONDecodeError as exc:
        return {
            "family": family,
            "status": "invalid",
            "failure_classes": [f"{family}_json_parse_failed"],
            "parse_error": exc.msg,
            "raw_sha256": sha256_text(raw_text),
        }

    if not isinstance(ballot, dict):
        classes.append(f"{family}_ballot_not_object")
        ballot = {}
    if ballot.get("schema_id") != BALLOT_SCHEMA:
        classes.append(f"{family}_schema_id_mismatch")
    if "question_id" not in ballot:
        classes.append(f"{family}_missing_question_id")
    elif ballot.get("question_id") != question_id:
        classes.append(f"{family}_question_id_mismatch")
    if ballot.get("family_id") != family:
        classes.append(f"{family}_family_id_mismatch")
    if ballot.get("vote") not in {"accept", "reject", "abstain"}:
        classes.append(f"{family}_vote_invalid")
    if not isinstance(ballot.get("confidence"), (int, float)):
        classes.append(f"{family}_confidence_type_mismatch")
    if not isinstance(ballot.get("native_quorum_effect"), bool):
        classes.append(f"{family}_native_quorum_effect_type_mismatch")
    if not isinstance(ballot.get("external_action_authorized"), bool):
        classes.append(f"{family}_external_action_authorized_type_mismatch")
    if ballot.get("payload_kind") != "public_synthetic":
        classes.append(f"{family}_payload_kind_mismatch")

    return {
        "family": family,
        "status": "valid" if not classes else "invalid",
        "failure_classes": sorted(classes),
        "raw_sha256": sha256_text(raw_text),
    }


def read_quarantine_wrapper(path: Path, *, question_id: str) -> dict[str, Any]:
    family = family_from_name(path)
    raw = path.read_text(encoding="utf-8")
    try:
        wrapper = json.loads(raw)
    except json.JSONDecodeError as exc:
        return {
            "path": path.as_posix(),
            "family": family,
            "status": "invalid",
            "failure_classes": [f"{family}_wrapper_json_parse_failed"],
            "parse_error": exc.msg,
            "wrapper_sha256": sha256_text(raw),
        }

    family = str(wrapper.get("family_key") or family)
    raw_text = str(wrapper.get("raw_text") or "")
    classified = classify_ballot(raw_text, family=family, question_id=question_id)
    return {
        "path": path.as_posix(),
        "family": family,
        "wrapper_sha256": sha256_text(raw),
        "raw_text_present": bool(raw_text),
        **classified,
    }


def analyze_run_dir(run_dir: Path) -> dict[str, Any]:
    qid = expected_question_id(run_dir)
    quarantine_dir = run_dir / "quarantine_in"
    samples = []
    present = set()
    if quarantine_dir.is_dir():
        for path in sorted(quarantine_dir.glob("*.raw.json")):
            item = read_quarantine_wrapper(path, question_id=qid)
            samples.append(item)
            if item["family"] in EXPECTED_FAMILIES:
                present.add(item["family"])

    absent = [family for family in EXPECTED_FAMILIES if family not in present]
    failure_classes = sorted(
        {failure for item in samples for failure in item.get("failure_classes", [])}
        | {f"{family}_absent" for family in absent}
    )
    valid_families = sorted(item["family"] for item in samples if item["status"] == "valid")
    invalid_families = sorted(item["family"] for item in samples if item["status"] != "valid")
    return {
        "run_id": qid,
        "run_dir": run_dir.as_posix(),
        "quarantine_dir_present": quarantine_dir.is_dir(),
        "sample_count": len(samples),
        "present_families": sorted(present),
        "absent_families": absent,
        "valid_families": valid_families,
        "invalid_families": invalid_families,
        "failure_classes": failure_classes,
        "samples": samples,
    }


def report(run_dirs: list[Path]) -> dict[str, Any]:
    runs = [analyze_run_dir(path) for path in run_dirs]
    aggregate_failures = sorted({failure for run in runs for failure in run["failure_classes"]})
    return {
        "schema_id": "hfo.gen130.sigrun_noria_failure_diagnostics.v0_1",
        "status": "LOCAL_REPLAY_COMPLETE",
        "external_action_performed": False,
        "network_call_performed": False,
        "secret_values_printed": False,
        "expected_families": list(EXPECTED_FAMILIES),
        "ballot_schema": BALLOT_SCHEMA,
        "aggregate_failure_classes": aggregate_failures,
        "can_classify": {
            "family_b_absent": "family_b_absent" in aggregate_failures,
            "family_c_schema_id_mismatch": True,
            "family_c_missing_question_id": "family_c_missing_question_id" in aggregate_failures,
            "family_c_json_parse_failed": "family_c_json_parse_failed" in aggregate_failures,
        },
        "wrapper_capture_gap": {
            "stdout_stderr_exit_split_persisted_by_runner": False,
            "final_json_status_available_from_companion": True,
            "recommendation": "Patch scripts/sigrun_noria_runner.ps1 next to persist stdout, stderr, exit code, raw_log_bytes, and final_json_parse_status separately.",
        },
        "runs": runs,
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Replay local noria free-mesh quarantine samples and classify failures")
    parser.add_argument("--run-dir", action="append", default=[], help="wake_runner_free_mesh_runs/<run_id> directory")
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args(argv)

    run_dirs = [Path(item) for item in args.run_dir] if args.run_dir else list(DEFAULT_RUN_DIRS)
    out = report(run_dirs)
    if args.json:
        print(stable_json(out))
    else:
        print(json.dumps(out, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
