
"""Code-owned, isolated, local-only NON_PRODUCTION adapter execution."""

from __future__ import annotations

import os
import subprocess
import sys
from copy import deepcopy
from pathlib import Path
from typing import Any, Mapping

from .canonical import contains_secret_text, sha256_bytes
from .errors import AdapterFailure
from .receipt import ReceiptBuilder, ReceiptStore
from .spec import STAGES, spec_sha256, validate_spec


BUILTIN_ADAPTER_ID = "builtin.non_production"
BUILTIN_ADAPTER_RELATIVE_PATH = "adapters/adapter_stub.py"
_BUILTIN_TEMPLATE_PATH = Path(__file__).resolve().parent.parent / "templates" / "adapter_stub.py.tmpl"
BUILTIN_ADAPTER_STUB = _BUILTIN_TEMPLATE_PATH.read_bytes()
BUILTIN_ADAPTER_STUB_SHA256 = sha256_bytes(BUILTIN_ADAPTER_STUB)
_RUN_STAGES = ("install", "build", "test", "health")
_TIMEOUT_SECONDS = 30
_SAFE_ENV_KEYS = (
    "COMSPEC",
    "LANG",
    "LC_ALL",
    "PATHEXT",
    "SYSTEMROOT",
    "TEMP",
    "TMP",
    "TMPDIR",
    "WINDIR",
)


def _sanitized_environment() -> dict[str, str]:
    environment = {key: os.environ[key] for key in _SAFE_ENV_KEYS if key in os.environ}
    environment.update(
        {
            "HFO_DLC_FACTORY_ADAPTER": BUILTIN_ADAPTER_ID,
            "HFO_DLC_FACTORY_CLASSIFICATION": "NON_PRODUCTION",
            "PYTHONDONTWRITEBYTECODE": "1",
            "PYTHONHASHSEED": "0",
            "PYTHONNOUSERSITE": "1",
            "TZ": "UTC",
        }
    )
    return environment


class LocalAdapterExecutor:
    """Execute only the byte-pinned built-in adapter with isolated Python."""

    def __init__(self, unit_dir: str | Path, spec: Mapping[str, Any]) -> None:
        self.unit_dir = Path(unit_dir).resolve()
        self.spec = validate_spec(dict(spec))
        if self.spec["classification"] != "NON_PRODUCTION":
            raise AdapterFailure("local built-in adapter is restricted to NON_PRODUCTION specs")
        if self.spec["target"]["binding_state"] != "UNADMITTED":
            raise AdapterFailure("local built-in adapter requires an UNADMITTED target")
        if self.spec["adapters"]["provider"] != BUILTIN_ADAPTER_ID:
            raise AdapterFailure("only the code-owned built-in adapter is permitted")
        self._stub_path = self.unit_dir / Path(BUILTIN_ADAPTER_RELATIVE_PATH)

    def _resolved_stub(self) -> Path:
        if self._stub_path.is_symlink() or self._stub_path.parent.is_symlink():
            raise AdapterFailure("built-in adapter path cannot contain a symlink")
        try:
            resolved = self._stub_path.resolve(strict=True)
            resolved.relative_to(self.unit_dir)
        except (OSError, ValueError) as error:
            raise AdapterFailure("built-in adapter is missing or escapes the unit directory") from error
        if not resolved.is_file() or resolved.read_bytes() != BUILTIN_ADAPTER_STUB:
            raise AdapterFailure("materialized adapter bytes do not match code authority")
        return resolved

    def _approved_argv(self, stage: str, stub_path: Path) -> list[str]:
        if stage not in STAGES:
            raise AdapterFailure(f"unsupported adapter stage: {stage}")
        # -I ignores environment/user paths and implies safe-path behavior; -S
        # disables site initialization. A sibling json.py/argparse.py therefore
        # cannot shadow the standard library imported by the pinned stub.
        # Execute from the unit root so the recorded adapter path is stable and
        # does not disclose a checkout-specific absolute directory. The Python
        # executable remains exact execution provenance and may legitimately
        # make receipts differ across runtimes.
        argv = [sys.executable, "-I", "-S", BUILTIN_ADAPTER_RELATIVE_PATH, stage]
        options = self.spec["adapters"]["options"]
        if stage == "health" and options["force_health_failure"]:
            argv.append("--force-failure")
        if stage == "rollback" and options["force_rollback_failure"]:
            argv.append("--force-failure")
        return argv

    def run_stage(self, stage: str) -> dict[str, Any]:
        argv = self._approved_argv(stage, self._resolved_stub())
        timed_out = False
        executor_error: str | None = None
        exit_code: int | None
        stdout = b""
        stderr = b""
        try:
            completed = subprocess.run(
                argv,
                cwd=self.unit_dir,
                env=_sanitized_environment(),
                shell=False,
                stdin=subprocess.DEVNULL,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                timeout=_TIMEOUT_SECONDS,
                check=False,
            )
            exit_code = completed.returncode
            stdout = completed.stdout
            stderr = completed.stderr
        except subprocess.TimeoutExpired as error:
            timed_out = True
            exit_code = None
            stdout = error.stdout or b""
            stderr = error.stderr or b""
        except OSError as error:
            exit_code = None
            executor_error = type(error).__name__
        stdout_text = stdout.decode("utf-8", errors="replace")
        stderr_text = stderr.decode("utf-8", errors="replace")
        output_redacted = contains_secret_text(stdout_text) or contains_secret_text(stderr_text)
        if output_redacted:
            stdout_text = "[REDACTED_SENSITIVE_OUTPUT]\n" if stdout else ""
            stderr_text = "[REDACTED_SENSITIVE_OUTPUT]\n" if stderr else ""
        ok = exit_code == 0 and not timed_out and executor_error is None and not output_redacted
        return {
            "adapter_id": BUILTIN_ADAPTER_ID,
            "adapter_stub_sha256": BUILTIN_ADAPTER_STUB_SHA256,
            "stage": stage,
            "argv": argv,
            "cwd": ".",
            "timeout_seconds": _TIMEOUT_SECONDS,
            "exit_code": exit_code,
            "timed_out": timed_out,
            "executor_error": executor_error,
            "output_redacted": output_redacted,
            "ok": ok,
            "stdout": stdout_text,
            "stdout_sha256": sha256_bytes(stdout),
            "stderr": stderr_text,
            "stderr_sha256": sha256_bytes(stderr),
        }


class AdapterRunner:
    """Run install/build/test/health and one rollback after any failure."""

    def __init__(
        self,
        executor: LocalAdapterExecutor,
        receipt_store: ReceiptStore,
        authority: Mapping[str, Any],
    ) -> None:
        self.executor = executor
        self.receipt_store = receipt_store
        self.authority = deepcopy(dict(authority))

    def run(self, spec: Mapping[str, Any], artifact_manifest_sha256: str) -> dict[str, Any]:
        checked = validate_spec(dict(spec))
        if spec_sha256(checked) != spec_sha256(self.executor.spec):
            raise AdapterFailure("executor spec does not match lifecycle spec")
        builder = ReceiptBuilder(
            self.authority,
            unit_id=checked["unit_id"],
            unit_spec_sha256=spec_sha256(checked),
            artifact_manifest_sha256=artifact_manifest_sha256,
        )
        stage_results: list[dict[str, Any]] = []
        rollback_result: dict[str, Any] | None = None
        failed_stage: str | None = None
        for stage in _RUN_STAGES:
            result = self.executor.run_stage(stage)
            stage_results.append(result)
            builder.add_event(
                f"adapter-stage-{len(stage_results)}-{stage}",
                "adapter.stage.completed",
                result,
            )
            if not result["ok"]:
                failed_stage = stage
                break
        if failed_stage is None:
            status = "LOCAL_REGRESSION_PASS"
        else:
            rollback_result = self.executor.run_stage("rollback")
            builder.add_event("adapter-stage-rollback", "adapter.rollback.completed", rollback_result)
            label = failed_stage.upper()
            status = (
                f"ROLLED_BACK_AFTER_{label}_FAILURE"
                if rollback_result["ok"]
                else f"ROLLBACK_FAILED_AFTER_{label}_FAILURE"
            )
        receipt = builder.build(stage_results, status, rollback_result)
        receipt_ref = self.receipt_store.put(receipt)
        return {
            "ok": status == "LOCAL_REGRESSION_PASS",
            "status": status,
            "stage_results": stage_results,
            "rollback_result": rollback_result,
            "receipt": receipt,
            "receipt_ref": receipt_ref,
        }
