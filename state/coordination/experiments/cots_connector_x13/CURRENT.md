---
schema_id: hfo.gen133.x13.cots_connector_current.v1
experiment_id: X13_DBOS_PYTHON_DURABLE_KERNEL_001
version: 4
prior_version: 3
candidate: DBOS_Python
candidate_pin: 2.22.0
campaign_wake: 4_of_4
phase_1_completed: true
phase_2_completed: false
phase_3_completed_scope: CARRIER_CONNECTOR_VARIANCE_ONLY
phase_4_decision: DEFER
phase_status: CAMPAIGN_CLOSED_DEFER_DISTINCT_HOST_RUNTIME
last_event_commit: a22f14f872645913a25582ece70f146de5b77c3e
last_event_path: state/coordination/experiments/cots_connector_x13/20260801T005134Z_DBOS_PYTHON_PHASE3_CONNECTOR_VARIANCE_PHASE4_DEFER.md
adoption_credit: 0
reopen_condition: distinct authorized host completes pinned SQLite interruption/restart specimen with artifact hash, commands, exit codes, first-step execution count one, workflow and step history, cleanup, cost, credentials, and honest flaw
carrier_task_id: 6a55c1733708819185088bf334e33ea5
carrier_task_id_verified_from_native_inventory: true
official_artifact_existence_verified: true
official_wheel_sha256_published: 09edc621ec2857dae73cc1b01bc7379999fe9ee4ef8c6ff4ac69dd1a5263001f
official_sdist_sha256_published: 5d43a9d0388d851df0f7bbd4ed752bc8b67be3d6fbe358c8be4d22f6c4887db6
artifact_bytes_locally_recomputed: false
latest_measured_error_class: ARTIFACT_INGRESS_POLICY_REJECTED_BINARY_AND_ARCHIVE_MIME_PLUS_SHELL_DNS_UNAVAILABLE
operator_relay_minutes: 0
operator_minutes_removed_estimate: 3_to_5
paid_cost_usd: 0
verifier: S04_STRUCTURAL_PREFLIGHT_THEN_OLRUN_DISTINCT_HOST_RUNTIME
consumer: Ratatoskr_and_Olrun
next_campaign_experiment_id: X13_GITHUB_CONTENTS_API_001
next_campaign_candidate: GitHub_Contents_API
next_campaign_phase: OFFICIAL_CONTRACT_AND_DIRECT_CAPABILITY_BASELINE
valid_time_utc: 2026-08-01T00:51:34Z
transaction_time_utc: SEE_GIT_COMMIT_METADATA
sealed: false
---

# X13 current campaign

The DBOS Python `2.22.0` four-wake campaign is closed as **`DEFER`**, not `REJECT`.

Phase 1 established documentary fit. Phase 2 never completed because no DBOS package bytes entered this carrier. The final connector-variance probe established a stronger carrier fact: the controlled download broker reached both official artifacts with HTTP `200` and exposed exact content lengths, but rejected the wheel and source archive before filesystem persistence because their MIME classes were not allowed; the shell independently could not resolve the public package host. No SQLite database, workflow, interruption, recovery, nonduplication, or workflow-history evidence exists, so adoption credit remains zero.

Do not repeat the install on this unchanged carrier surface. Reopen DBOS only when a distinct authorized host returns the exact pinned SQLite interruption/restart receipt named above. The next campaign candidate is the native GitHub Contents API, which is directly exposed and can be tested without new infrastructure.

The immutable event and this pointer are separate Git commits. GitHub Contents API writes do not provide cross-file database atomicity, linearizable compare-and-swap, or exactly-once guarantees.
