
"""Fixed-root orchestration for one checkout-local factory transition."""

from __future__ import annotations

from pathlib import Path
from typing import Any, Mapping

from .adapters import AdapterRunner, LocalAdapterExecutor
from .canonical import canonical_json_bytes, sha256_bytes
from .errors import MaterializationConflict
from .lease import WipLease, package_runs_root
from .materializer import Materializer
from .policy import authority_binding
from .receipt import ReceiptStore
from .spec import spec_sha256, validate_spec


MAKER_HOLDER = "codex-maker-019fc470-762c-7683-9573-e75d64c3435a"


class FactoryRuntime:
    """Materialize and exercise one spec beneath the checkout's fixed run root.

    Root injection is available only to direct Python tests. The public CLI does
    not expose it. Workspace names use the first 128 bits of the full intent
    digest to stay below legacy Windows path limits; an improbable prefix
    collision fails closed during exact-tree comparison.
    """

    def __init__(
        self,
        *,
        runs_root: Path | None = None,
        materializer: Materializer | None = None,
    ) -> None:
        self.runs_root = Path(runs_root) if runs_root is not None else package_runs_root()
        self.materializer = materializer or Materializer()

    def intent(self, spec: Mapping[str, Any]) -> dict[str, Any]:
        checked = validate_spec(dict(spec))
        _, expected_tree_sha256 = self.materializer._artifacts(
            self.materializer.render(checked)
        )
        payload = {
            "schema_id": "hfo.gen133.dlc_foss_factory.run_intent.v1",
            "authority": authority_binding(),
            "operation": "LOCAL_REGRESSION",
            "unit_id": checked["unit_id"],
            "unit_spec_sha256": spec_sha256(checked),
            "expected_artifact_tree_sha256": expected_tree_sha256,
        }
        return {**payload, "run_id": sha256_bytes(canonical_json_bytes(payload))}

    def _workspace(self, run_id: str) -> Path:
        return self.runs_root / "workspaces" / run_id[:32]

    def materialize(self, spec: Mapping[str, Any]) -> dict[str, Any]:
        checked = validate_spec(dict(spec))
        intent = self.intent(checked)
        with WipLease.acquire(MAKER_HOLDER, intent["run_id"], runs_root=self.runs_root):
            result = self.materializer.materialize(checked, self._workspace(intent["run_id"]))
            if result.tree_sha256 != intent["expected_artifact_tree_sha256"]:
                raise MaterializationConflict("materialized tree differs from the bound run intent")
        return {"intent": intent, "materialization": result.manifest()}

    def run(self, spec: Mapping[str, Any]) -> dict[str, Any]:
        checked = validate_spec(dict(spec))
        intent = self.intent(checked)
        with WipLease.acquire(MAKER_HOLDER, intent["run_id"], runs_root=self.runs_root):
            materialized = self.materializer.materialize(
                checked, self._workspace(intent["run_id"])
            )
            if materialized.tree_sha256 != intent["expected_artifact_tree_sha256"]:
                raise MaterializationConflict("materialized tree differs from the bound run intent")
            lifecycle = AdapterRunner(
                LocalAdapterExecutor(materialized.output_root, checked),
                ReceiptStore(self.runs_root),
                authority_binding(),
            ).run(checked, materialized.tree_sha256)
        return {
            "intent": intent,
            "materialization": materialized.manifest(),
            "lifecycle": lifecycle,
        }
