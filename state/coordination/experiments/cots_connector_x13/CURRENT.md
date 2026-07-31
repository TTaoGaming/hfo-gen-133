---
schema_id: hfo.gen133.x13.cots_connector_current.v1
experiment_id: X13_DBOS_PYTHON_DURABLE_KERNEL_001
version: 3
prior_version: 2
candidate: DBOS_Python
candidate_pin: 2.22.0
phase_attempted: 2_of_4
phase_completed: 1_of_4
phase_status: HOLD_ARTIFACT_TRANSFER_SURFACE
last_event_commit: b8bed105d1c8a38907a7a2ec6cb6405e216825d8
last_event_path: state/coordination/experiments/cots_connector_x13/20260731T235059Z_DBOS_PYTHON_PHASE2_ARTIFACT_TRANSFER_HOLD.md
next_phase: RETRY_SMALLEST_HARMLESS_REVERSIBLE_MICRO_USE
next_acceptance: pinned SQLite workflow is interrupted after first durable step, restarted, advances once without duplicate transition, exposes workflow and step history, records exact installed artifact hash, and cleans up
carrier_task_id: 6a55c1733708819185088bf334e33ea5
carrier_task_id_verified_from_native_inventory: true
official_artifact_existence_verified: true
official_wheel_sha256_published: 09edc621ec2857dae73cc1b01bc7379999fe9ee4ef8c6ff4ac69dd1a5263001f
official_sdist_sha256_published: 5d43a9d0388d851df0f7bbd4ed752bc8b67be3d6fbe358c8be4d22f6c4887db6
artifact_bytes_locally_recomputed: false
last_error_class: PACKAGE_AND_DEPENDENCIES_UNAVAILABLE_ON_CONFIGURED_INDEX_PLUS_PUBLIC_DNS_UNAVAILABLE
operator_relay_minutes: 0
paid_cost_usd: 0
verifier: S04_STRUCTURAL_PREFLIGHT_THEN_OLRUN_DISTINCT_HOST_RUNTIME
consumer: Ratatoskr_and_Olrun
valid_time_utc: 2026-07-31T23:50:59Z
transaction_time_utc: SEE_GIT_COMMIT_METADATA
sealed: false
---

# X13 current campaign

DBOS Python remains a **candidate**, not an adopted runtime. Phase 2 has not completed. A repeated ephemeral Python 3.13.5 install attempt failed because the carrier's configured package index exposes neither `dbos==2.22.0` nor required missing dependencies, while direct public DNS is unavailable.

A material diagnostic fact is now bound: official PyPI publishes the exact `2.22.0` source distribution and universal wheel with Trusted Publishing provenance and published SHA-256 digests. The package therefore exists; this carrier lacks a verified artifact-transfer path. The published hashes were not independently recomputed because no package bytes entered the runtime.

The next accepted wake must run the same bounded SQLite interruption/restart specimen only on an already-authorized host with ordinary package resolution. It must record the installed artifact hash, exact commands and exit codes, first-step execution count, restart behavior, workflow/step history, cleanup, cost, credentials, and honest flaw. It must not create an account, provision DBOS Cloud/Conductor, or broaden into architecture work.

The event and this pointer are separate Git commits and are not cross-file atomic. Until exact restart/recovery evidence exists, the campaign remains `HOLD_ARTIFACT_TRANSFER_SURFACE` with zero adoption credit.
