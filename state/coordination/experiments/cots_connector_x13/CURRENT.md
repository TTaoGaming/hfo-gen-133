---
schema_id: hfo.gen133.x13.cots_connector_current.v1
experiment_id: X13_GITHUB_CONTENTS_API_001
version: 5
prior_version: 4
candidate: GitHub_REST_Contents_API
candidate_contract_reference: official_REST_versions_2026-03-10_and_2022-11-28_connector_header_not_exposed
campaign_wake: 1_of_4
phase_1_completed: true
phase_2_completed: false
phase_3_completed: false
phase_4_decision: PENDING
phase_status: PHASE1_BASELINE_COMPLETE_PHASE2_REVERSIBLE_SPECIMEN_NEXT
last_event_commit: 9999d02d2b3f91d62e667cfd921aac9c333ccb3f
last_event_path: state/coordination/experiments/cots_connector_x13/20260801T014949Z_GITHUB_CONTENTS_API_PHASE1_BASELINE.md
adoption_credit: 0
carrier_task_id: 6a55c1733708819185088bf334e33ea5
carrier_task_id_verified_from_native_inventory: true
direct_read_path: state/coordination/experiments/cots_connector_x13/CURRENT.md
direct_read_prior_blob_sha: a8d22776fac07de20bfe7db7e97325d6d76c11e3
direct_read_prior_utf8_bytes: 3049
direct_read_prior_sha256: 137bd6dbc9443bf335515b7ef6bf09b3780a823fbd7b6e34c524241e81865de7
event_create_commit_latency_ms_exposed: 784
effective_api_version_from_direct_receipt: UNKNOWN
live_authentication_class: UNKNOWN
live_rate_limit_headers: NOT_EXPOSED
operator_relay_minutes: 0
operator_minutes_removed_estimate: 3_to_6
paid_cost_usd: 0
verifier: S04_STRUCTURAL_PREFLIGHT_THEN_DISTINCT_NONPRODUCER
consumer: Ratatoskr_and_Olrun
next_phase: HARMLESS_DETERMINISTIC_REVERSIBLE_UTF8_SPECIMEN
expiry_utc: 2026-08-08T01:49:49Z
valid_time_utc: 2026-08-01T01:49:49Z
transaction_time_utc: SEE_GIT_COMMIT_METADATA
sealed: false
---

# X13 current campaign

The GitHub REST Contents API campaign has completed phase 1 of 4.

Official contract review established the required update SHA, documented create/update status classes, content-write permission requirements, serial mutation warning, API-version support window, and general authenticated rate-limit baselines. Direct carrier readback succeeded on the canonical branch and returned the prior `CURRENT.md` content plus blob SHA without operator relay.

The connector has now also created this immutable phase-1 event. That required bookkeeping is useful write evidence but does not count as the dedicated phase-2 micro-use. Adoption credit remains zero until a harmless deterministic specimen is created, read back byte-for-byte, reversibly replaced with the fetched blob SHA, and read back again.

The wrapper does not expose token identity, exact permission scope, effective API-version header, HTTP status/headers, rate-limit budget, ETag, request ID, audit event, or retry behavior. The event and this pointer are separate commits and are not cross-file atomic, exactly-once, or transactionally coupled.
