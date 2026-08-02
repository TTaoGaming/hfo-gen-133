


"""Canonical, content-addressed, maker-local lifecycle receipts."""

from __future__ import annotations

import json
import os
import re
import tempfile
from copy import deepcopy
from pathlib import Path
from typing import Any, Mapping, NoReturn, Sequence

from .canonical import assert_no_secrets, canonical_json_bytes, sha256_bytes
from .errors import DuplicateEventError, ReceiptIntegrityError
from .lease import is_link_or_reparse
from .policy import authority_binding


RECEIPT_SCHEMA_ID = "hfo.gen133.dlc_foss_factory.receipt.v1"
_HEX64 = re.compile(r"^[0-9a-f]{64}$")
_PYTHON_BASENAME = re.compile(r"^python(?:\d+(?:\.\d+)*)?(?:\.exe)?$", re.IGNORECASE)
_APPROVED_ADAPTER_PATH = "adapters/adapter_stub.py"
_APPROVED_ADAPTER_STUB_SHA256 = sha256_bytes(
    (Path(__file__).resolve().parent.parent / "templates" / "adapter_stub.py.tmpl").read_bytes()
)
_FAIL_STATUS = re.compile(
    r"^(ROLLED_BACK|ROLLBACK_FAILED)_AFTER_(INSTALL|BUILD|TEST|HEALTH)_FAILURE$"
)
_STAGE_KEYS = {
    "adapter_id",
    "adapter_stub_sha256",
    "stage",
    "argv",
    "cwd",
    "timeout_seconds",
    "exit_code",
    "timed_out",
    "executor_error",
    "output_redacted",
    "ok",
    "stdout",
    "stdout_sha256",
    "stderr",
    "stderr_sha256",
}


def _fail(message: str) -> NoReturn:
    raise ReceiptIntegrityError(message)


def _require_sha256(value: Any, field: str) -> str:
    if not isinstance(value, str) or not _HEX64.fullmatch(value):
        _fail(f"{field} must be a lowercase SHA-256 digest")
    return value


def _strict_object(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in pairs:
        if key in result:
            _fail(f"duplicate JSON key rejected: {key}")
        result[key] = value
    return result


def _reject_constant(value: str) -> NoReturn:
    _fail(f"non-finite JSON value rejected: {value}")


def _event_core(event: Mapping[str, Any]) -> dict[str, Any]:
    return {
        "seq": event["seq"],
        "event_id": event["event_id"],
        "type": event["type"],
        "prev_event_sha256": event["prev_event_sha256"],
        "payload": event["payload"],
    }


def _validate_events(events: Any) -> None:
    if not isinstance(events, list):
        _fail("receipt.events must be an array")
    seen: set[str] = set()
    previous: str | None = None
    expected = {"seq", "event_id", "type", "prev_event_sha256", "payload", "event_sha256"}
    for sequence, event in enumerate(events, start=1):
        if not isinstance(event, dict) or set(event) != expected:
            _fail(f"event {sequence} has an invalid shape")
        event_id = event["event_id"]
        if not isinstance(event_id, str) or not event_id.strip():
            _fail(f"event {sequence} has an invalid event_id")
        if event_id in seen:
            raise DuplicateEventError(f"duplicate receipt event_id rejected: {event_id}")
        seen.add(event_id)
        if event["seq"] != sequence or event["prev_event_sha256"] != previous:
            _fail(f"event {event_id} has invalid sequence linkage")
        calculated = sha256_bytes(canonical_json_bytes(_event_core(event)))
        if event["event_sha256"] != calculated:
            _fail(f"event {event_id} hash mismatch")
        previous = calculated


def _validate_stage(result: Any, expected_stage: str | None = None) -> dict[str, Any]:
    if not isinstance(result, dict) or set(result) != _STAGE_KEYS:
        _fail("stage result has an invalid shape")
    if result["adapter_id"] != "builtin.non_production":
        _fail("stage result uses an unapproved adapter")
    _require_sha256(result["adapter_stub_sha256"], "adapter_stub_sha256")
    if result["adapter_stub_sha256"] != _APPROVED_ADAPTER_STUB_SHA256:
        _fail("stage result does not bind the code-owned adapter bytes")
    if result["stage"] not in ("install", "build", "test", "health", "rollback"):
        _fail("stage result has an unsupported stage")
    if expected_stage is not None and result["stage"] != expected_stage:
        _fail(f"expected {expected_stage} result, got {result['stage']}")
    argv = result["argv"]
    if not isinstance(argv, list) or not all(isinstance(item, str) for item in argv):
        _fail("stage argv must be an array of strings")
    if len(argv) not in (5, 6):
        _fail("stage argv differs from the fixed adapter command plan")
    executable_name = argv[0].replace("\\", "/").rsplit("/", 1)[-1]
    if not _PYTHON_BASENAME.fullmatch(executable_name):
        _fail("stage argv does not identify an approved Python executable")
    if argv[1:5] != ["-I", "-S", _APPROVED_ADAPTER_PATH, result["stage"]]:
        _fail("stage argv differs from the fixed adapter command plan")
    if len(argv) == 6 and (
        argv[5] != "--force-failure" or result["stage"] not in ("health", "rollback")
    ):
        _fail("stage argv has an unsupported failure-injection option")
    if result["cwd"] != "." or result["timeout_seconds"] != 30:
        _fail("stage cwd or timeout differs from the fixed local adapter contract")
    exit_code = result["exit_code"]
    if exit_code is not None and (not isinstance(exit_code, int) or isinstance(exit_code, bool)):
        _fail("stage exit_code must be an integer or null")
    for key in ("timed_out", "output_redacted", "ok"):
        if not isinstance(result[key], bool):
            _fail(f"stage {key} must be boolean")
    if result["executor_error"] is not None and not isinstance(result["executor_error"], str):
        _fail("stage executor_error must be string or null")
    for stream in ("stdout", "stderr"):
        if not isinstance(result[stream], str):
            _fail(f"stage {stream} must be a string")
        _require_sha256(result[f"{stream}_sha256"], f"{stream}_sha256")
        if not result["output_redacted"]:
            observed = sha256_bytes(result[stream].encode("utf-8"))
            if result[f"{stream}_sha256"] != observed:
                _fail(f"stage {stream} bytes do not match their digest")
    expected_ok = (
        exit_code == 0
        and not result["timed_out"]
        and result["executor_error"] is None
        and not result["output_redacted"]
    )
    if result["ok"] != expected_ok:
        _fail("stage ok flag conflicts with raw execution outcome")
    return result


def _validate_receipt(value: Any) -> dict[str, Any]:
    expected_top = {
        "schema_id",
        "authority",
        "unit",
        "status",
        "claim",
        "events",
        "stage_results",
        "rollback_result",
        "remaining_risk",
        "honest_flaw",
        "next_safe_action",
    }
    if not isinstance(value, dict) or set(value) != expected_top:
        _fail("receipt has an invalid top-level shape")
    if value["schema_id"] != RECEIPT_SCHEMA_ID:
        _fail(f"receipt.schema_id must equal {RECEIPT_SCHEMA_ID}")
    if value["authority"] != authority_binding():
        _fail("receipt authority does not match the frozen controller binding")
    unit = value["unit"]
    if not isinstance(unit, dict) or set(unit) != {"unit_id", "unit_spec_sha256", "artifact_manifest_sha256"}:
        _fail("receipt.unit has an invalid shape")
    if not isinstance(unit["unit_id"], str) or not unit["unit_id"].strip():
        _fail("receipt.unit.unit_id is required")
    _require_sha256(unit["unit_spec_sha256"], "unit_spec_sha256")
    _require_sha256(unit["artifact_manifest_sha256"], "artifact_manifest_sha256")
    claim = value["claim"]
    expected_claim_keys = {
        "verification_scope",
        "verifier_relationship",
        "independent_verification",
        "target_admitted",
        "pilot_ready",
        "production_ready",
        "result",
    }
    if not isinstance(claim, dict) or set(claim) != expected_claim_keys:
        _fail("receipt.claim has an invalid shape")
    expected_fixed_claim = {
        "verification_scope": "LOCAL_REGRESSION",
        "verifier_relationship": "MAKER_LOCAL_SAME_IMPLEMENTATION",
        "independent_verification": False,
        "target_admitted": False,
        "pilot_ready": False,
        "production_ready": False,
    }
    for key, expected in expected_fixed_claim.items():
        if claim[key] != expected:
            _fail(f"receipt claim {key} exceeds the maker evidence ceiling")
    results = value["stage_results"]
    if not isinstance(results, list) or not results:
        _fail("receipt.stage_results must be a non-empty array")
    run_order = ["install", "build", "test", "health"]
    for index, result in enumerate(results):
        if index >= len(run_order):
            _fail("receipt contains too many lifecycle stage results")
        _validate_stage(result, run_order[index])
    status = value["status"]
    rollback = value["rollback_result"]
    if status == "LOCAL_REGRESSION_PASS":
        if claim["result"] != "PASS" or len(results) != 4 or not all(item["ok"] for item in results):
            _fail("pass status conflicts with lifecycle results")
        if rollback is not None:
            _fail("successful lifecycle must not contain a rollback result")
    else:
        match = _FAIL_STATUS.fullmatch(str(status))
        if match is None or claim["result"] != "FAIL":
            _fail("failure status or claim result is invalid")
        failed_stage = match.group(2).lower()
        if results[-1]["stage"] != failed_stage or results[-1]["ok"]:
            _fail("failure status does not bind the actual failed stage")
        if any(not item["ok"] for item in results[:-1]):
            _fail("lifecycle continued after an earlier failed stage")
        _validate_stage(rollback, "rollback")
        rollback_should_pass = match.group(1) == "ROLLED_BACK"
        if rollback["ok"] != rollback_should_pass:
            _fail("rollback status conflicts with rollback execution")
    _validate_events(value["events"])
    expected_payloads = list(results) + ([] if rollback is None else [rollback])
    if len(value["events"]) != len(expected_payloads):
        _fail("event count does not bind every lifecycle result")
    for event, payload in zip(value["events"], expected_payloads, strict=True):
        if event["payload"] != payload:
            _fail("event payload differs from its lifecycle result")
    for field in ("remaining_risk", "honest_flaw", "next_safe_action"):
        if not isinstance(value[field], str) or not value[field].strip():
            _fail(f"receipt.{field} is required")
    assert_no_secrets(value)
    canonical_json_bytes(value)
    return value


class ReceiptBuilder:
    def __init__(
        self,
        authority: Mapping[str, Any],
        *,
        unit_id: str,
        unit_spec_sha256: str,
        artifact_manifest_sha256: str,
    ) -> None:
        if dict(authority) != authority_binding():
            _fail("builder authority does not match the frozen controller")
        self._authority = deepcopy(dict(authority))
        self._unit_id = unit_id
        self._unit_spec_sha256 = _require_sha256(unit_spec_sha256, "unit_spec_sha256")
        self._artifact_manifest_sha256 = _require_sha256(
            artifact_manifest_sha256, "artifact_manifest_sha256"
        )
        self._events: list[dict[str, Any]] = []
        self._event_ids: set[str] = set()

    def add_event(self, event_id: str, type: str, payload: Any) -> None:
        if not isinstance(event_id, str) or not event_id.strip() or event_id in self._event_ids:
            if event_id in self._event_ids:
                raise DuplicateEventError(f"duplicate receipt event_id rejected: {event_id}")
            _fail("event_id must be a unique non-empty string")
        if not isinstance(type, str) or not type.strip():
            _fail("event type must be a non-empty string")
        event_payload = deepcopy(payload)
        assert_no_secrets(event_payload)
        core = {
            "seq": len(self._events) + 1,
            "event_id": event_id,
            "type": type,
            "prev_event_sha256": self._events[-1]["event_sha256"] if self._events else None,
            "payload": event_payload,
        }
        event = {**core, "event_sha256": sha256_bytes(canonical_json_bytes(core))}
        self._events.append(event)
        self._event_ids.add(event_id)

    def build(
        self,
        stage_results: Sequence[Mapping[str, Any]],
        status: str,
        rollback_result: Mapping[str, Any] | None = None,
    ) -> dict[str, Any]:
        passed = status == "LOCAL_REGRESSION_PASS"
        receipt = {
            "schema_id": RECEIPT_SCHEMA_ID,
            "authority": deepcopy(self._authority),
            "unit": {
                "unit_id": self._unit_id,
                "unit_spec_sha256": self._unit_spec_sha256,
                "artifact_manifest_sha256": self._artifact_manifest_sha256,
            },
            "status": status,
            "claim": {
                "verification_scope": "LOCAL_REGRESSION",
                "verifier_relationship": "MAKER_LOCAL_SAME_IMPLEMENTATION",
                "independent_verification": False,
                "target_admitted": False,
                "pilot_ready": False,
                "production_ready": False,
                "result": "PASS" if passed else "FAIL",
            },
            "events": deepcopy(self._events),
            "stage_results": [deepcopy(dict(item)) for item in stage_results],
            "rollback_result": None if rollback_result is None else deepcopy(dict(rollback_result)),
            "remaining_risk": (
                "Target admission, license compatibility, real-user acceptance, deployment, "
                "and production behavior remain unverified."
            ),
            "honest_flaw": (
                "Maker-owned fixture and executor; no distinct held-out or independent "
                "verification was performed."
            ),
            "next_safe_action": (
                "Hand the exact receipt SHA-256 and candidate commit to the distinct held-out verifier."
            ),
        }
        return _validate_receipt(receipt)


class ReceiptStore:
    def __init__(self, root: str | Path) -> None:
        self.root = Path(root)

    def _path(self, digest: str) -> Path:
        _require_sha256(digest, "receipt sha256")
        return self.root / "sha256" / digest / "receipt.json"

    def put(self, receipt: Mapping[str, Any]) -> dict[str, Any]:
        checked = _validate_receipt(deepcopy(dict(receipt)))
        data = canonical_json_bytes(checked)
        digest = sha256_bytes(data)
        path = self._path(digest)
        # Reject an existing junction/symlink before mkdir can follow it and
        # create the digest directory outside the configured receipt root.
        # Repeat after creation to detect a concurrent path swap.
        for ancestor in (path.parent, *path.parent.parents):
            if ancestor.exists() and is_link_or_reparse(ancestor):
                _fail("receipt path crosses a symlink or reparse point")
        path.parent.mkdir(parents=True, exist_ok=True)
        for ancestor in (path.parent, *path.parent.parents):
            if ancestor.exists() and is_link_or_reparse(ancestor):
                _fail("receipt path crosses a symlink or reparse point")
        if path.exists():
            if is_link_or_reparse(path) or path.read_bytes() != data:
                _fail("existing receipt address contains different bytes")
            self.verify(path)
            return {"sha256": digest, "path": path.relative_to(self.root).as_posix(), "idempotent": True}
        temporary: str | None = None
        created = False
        try:
            with tempfile.NamedTemporaryFile(mode="wb", prefix=".receipt-", dir=path.parent, delete=False) as handle:
                temporary = handle.name
                handle.write(data)
                handle.flush()
                os.fsync(handle.fileno())
            try:
                os.link(temporary, path)
                created = True
            except OSError:
                try:
                    with path.open("xb") as handle:
                        handle.write(data)
                        handle.flush()
                        os.fsync(handle.fileno())
                    created = True
                except FileExistsError:
                    created = False
        finally:
            if temporary is not None:
                Path(temporary).unlink(missing_ok=True)
        if not created and (is_link_or_reparse(path) or path.read_bytes() != data):
            _fail("receipt address collision contains different bytes")
        self.verify(path)
        return {"sha256": digest, "path": path.relative_to(self.root).as_posix(), "idempotent": not created}

    def verify(self, path: str | Path) -> dict[str, Any]:
        candidate = Path(path)
        if ".." in candidate.parts:
            _fail("receipt path may not contain parent traversal")
        root_absolute = self.root.absolute()
        candidate_absolute = candidate.absolute() if candidate.is_absolute() else root_absolute / candidate
        try:
            relative = candidate_absolute.relative_to(root_absolute)
        except ValueError as error:
            raise ReceiptIntegrityError("receipt path escapes its root") from error
        if len(relative.parts) != 3 or relative.parts[0] != "sha256" or relative.parts[2] != "receipt.json":
            _fail("receipt path must be sha256/<digest>/receipt.json")
        digest = _require_sha256(relative.parts[1], "receipt path digest")
        current = root_absolute
        for part in relative.parts:
            current = current / part
            if is_link_or_reparse(current):
                _fail("symlinks and reparse points are forbidden in receipt paths")
        if not current.is_file():
            _fail("receipt address is not a regular file")
        data = current.read_bytes()
        if sha256_bytes(data) != digest:
            _fail("receipt bytes do not match their content address")
        try:
            parsed = json.loads(
                data.decode("utf-8"),
                object_pairs_hook=_strict_object,
                parse_constant=_reject_constant,
            )
        except ReceiptIntegrityError:
            raise
        except (UnicodeDecodeError, json.JSONDecodeError) as error:
            raise ReceiptIntegrityError(f"receipt is not strict UTF-8 JSON: {error}") from error
        if canonical_json_bytes(parsed) != data:
            _fail("receipt bytes are not canonical JSON")
        return _validate_receipt(parsed)
