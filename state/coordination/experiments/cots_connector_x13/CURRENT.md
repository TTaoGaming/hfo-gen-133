---
schema_id: hfo.gen133.x13.cots_connector_current.v1
experiment_id: X13_GITHUB_CONTENTS_API_001
version: 6
prior_version: 5
candidate: GitHub_REST_Contents_API
candidate_contract_reference: official_REST_versions_2026-03-10_and_2022-11-28_connector_header_not_exposed
campaign_wake: 2_of_4
phase_1_completed: true
phase_2_completed: true
phase_3_completed: false
phase_4_decision: PENDING
phase_status: PHASE2_REVERSIBLE_MICRO_USE_COMPLETE_PHASE3_STALE_SHA_PROBE_NEXT
last_event_commit: 104defe984d51c1efdc66b0ba7f47b2a59afbb72
last_event_path: state/coordination/experiments/cots_connector_x13/20260801T024811Z_GITHUB_CONTENTS_API_PHASE2_REVERSIBLE_MICRO_USE.md
adoption_credit: 1
adoption_credit_basis: DIRECT_EXACT_BYTE_CREATE_UPDATE_FORWARD_ROLLBACK_ONLY
carrier_task_id: 6a55c1733708819185088bf334e33ea5
carrier_task_id_verified_from_native_inventory: true
specimen_path: state/coordination/experiments/cots_connector_x13/specimens/20260801T024651Z_GITHUB_CONTENTS_PHASE2_REVERSIBLE.txt
specimen_baseline_utf8_bytes: 195
specimen_baseline_sha256: 1c0cb81dff110dbc55b55bd4bddc8fecb761c3860f7851d64f981362488b15a3
specimen_baseline_blob_sha: a9826e11db433c9ae3180b8590b7720a2d4388f7
specimen_updated_utf8_bytes: 204
specimen_updated_sha256: 983982b4311670005ff68bd7d6b6120c3d9b85417b9880fd772f9700fbb25def
specimen_updated_blob_sha: a9ba2dad14ed9bc72179ee709e7712dd9ff50449
specimen_create_commit: 69bb7578d17559a409b2a60975912181fffd685c
specimen_update_commit: 611ebcc8af302719a7e8d56910f231f7104ec724
specimen_rollback_commit: aeaffd84eaa0af957c319e3c99c3d720c109923c
specimen_final_state: BASELINE_EXACT_BYTES_RESTORED
specimen_final_blob_sha: a9826e11db433c9ae3180b8590b7720a2d4388f7
create_latency_ms_exposed: 812
update_latency_ms_exposed: 702
rollback_latency_ms_exposed: 891
exact_readback: true
operator_relay_minutes: 0
operator_minutes_removed_estimate: 5_to_10
paid_cost_usd: 0
live_authentication_class: UNKNOWN
live_rate_limit_headers: NOT_EXPOSED
effective_api_version_from_direct_receipt: UNKNOWN
verifier: S04_STRUCTURAL_PREFLIGHT_THEN_DISTINCT_NONPRODUCER
consumer: Ratatoskr_and_Olrun
next_phase: QUARANTINED_STALE_SHA_REJECTION_AND_CONNECTOR_VARIANCE_PROBE
expiry_utc: 2026-08-08T02:48:11Z
valid_time_utc: 2026-08-01T02:48:11Z
transaction_time_utc: SEE_GIT_COMMIT_METADATA
sealed: false
---

# X13 current campaign

The GitHub REST Contents API campaign has completed phase 2 of 4.

A harmless UTF-8 specimen was created in the X13 experiment directory, read back exactly, replaced using the fetched current blob SHA, read back exactly, and restored to its baseline bytes with a second SHA-bound forward commit. The final readback recomputed to the original 195-byte SHA-256 and Git blob SHA.

This supports serial, reversible, single-path repository-content mutation through the connector. It does not support multi-file atomicity, exactly-once execution, stale-writer safety, least privilege, durable workflow semantics, independent verification, or ConsumerAck.

Phase 3 must use a new quarantined specimen to test whether a stale blob SHA is rejected without changing the newer bytes, then restore the baseline with a valid forward update. The wrapper still hides authentication identity and scope, effective API version, HTTP status and headers, rate-limit state, request ID, ETag, retry behavior, and audit attribution.
