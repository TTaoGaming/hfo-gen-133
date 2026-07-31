---
schema_id: hfo.gen133.x13.cots_connector_current.v1
experiment_id: X13_DBOS_PYTHON_DURABLE_KERNEL_001
version: 2
prior_version: 1
candidate: DBOS_Python
candidate_pin: 2.22.0
phase_attempted: 2_of_4
phase_completed: 1_of_4
phase_status: HOLD_EXECUTION_SURFACE
last_event_commit: 209ef850d1eb756cf0cef3356a5b6dcb5b7d7bfe
last_event_path: state/coordination/experiments/cots_connector_x13/20260731T225132Z_DBOS_PYTHON_PHASE2_EXECUTION_SURFACE_HOLD.md
next_phase: RETRY_SMALLEST_HARMLESS_REVERSIBLE_MICRO_USE
next_acceptance: pinned SQLite workflow is interrupted after CLAIMED, restarted, advances once without duplicate transition, exposes workflow history, and cleans up
carrier_task_id: 6a55c1733708819185088bf334e33ea5
carrier_task_id_verified_from_native_inventory: true
prior_projection_defect: version_1_current_and_phase_1_prose_carried_incorrect_task_ids
last_error_class: PACKAGE_NOT_AVAILABLE_ON_CONFIGURED_INDEX_AND_PUBLIC_DNS_UNAVAILABLE
operator_relay_minutes: 0
paid_cost_usd: 0
verifier: S04_STRUCTURAL_PREFLIGHT_THEN_OLRUN_DISTINCT_HOST_RUNTIME
consumer: Ratatoskr_and_Olrun
valid_time_utc: 2026-07-31T22:51:32Z
transaction_time_utc: SEE_GIT_COMMIT_METADATA
sealed: false
---

# X13 current campaign

DBOS Python remains a **candidate**, not an adopted runtime. Phase 2 was attempted on a real ephemeral Python 3.13.5 execution surface, but the configured package mirror did not expose `dbos==2.22.0` and the container could not resolve public GitHub DNS. No DBOS package or workflow ran, so durability, restart, idempotency, observability, and custom-code reduction remain unproved.

The previous live pointer's task ID and the Phase 1 prose contained inconsistent X13 task bindings. Version 2 corrects the live pointer to the native task ID `6a55c1733708819185088bf334e33ea5`; immutable prior bytes remain unchanged and are explicitly contradicted by the Phase 2 event.

The next accepted wake must retry the same bounded SQLite specimen only on an already-authorized host with ordinary package resolution. It must not create an account, provision DBOS Cloud/Conductor, or broaden into architecture work. Until exact restart/recovery evidence exists, the campaign remains `HOLD_EXECUTION_SURFACE`.
