---
schema_id: hfo.gen133.x13.cots_connector_event.v1
experiment_id: X13_SLACK_PUBLIC_CHANNEL_CONNECTOR_001
seat: X13_COTS_CONNECTOR_PDCA
addressed_to: S04_STRUCTURAL_PREFLIGHT
carrier_task_id_expected: 6a55c1733708819185088bf334e33ea5
carrier_task_id_observed: 6a55c1733708819185088bf334e33ea5
carrier_task_id_match: true
campaign_wake: 3_of_4
phase_attempted: 3_of_4
phase_1_completed: true
phase_2_completed: true
phase_3_completed: true
phase_4_decision: PENDING
candidate: Slack_public_channel_connector
result: INVALID_CHANNEL_EXPLICIT_ERROR_AND_VALID_CHANNEL_RECOVERY_CONFIRMED
measured_fact_changed: true
prior_current_version: 10
next_current_version: 11
prior_current_blob_sha: a28e8d9992a06c2761c1e7c078194d30f4fc1a83
valid_time_utc: 2026-08-01T07:49:39Z
transaction_time_utc: SEE_GIT_COMMIT_METADATA
canonical_repository: TTaoGaming/hfo-gen-133
canonical_branch: agent/gen133-bootstrap-20260730
wip: 1
effect_ceiling: TWO_BOUNDED_READS_NO_WRITE
verifier: S04_STRUCTURAL_PREFLIGHT_THEN_DISTINCT_NONPRODUCER
consumer: Ratatoskr_and_Olrun
consumer_ack: NOT_OBSERVED
same_provider_evidence_binding_weight: 0
review_expiry_utc: 2026-08-08T07:49:39Z
invalid_probe_channel_id: C0X13INVALID0001
invalid_probe_result_class: execution_failed_channel_not_found
valid_recovery_channel_id: C0BGNGPJFHU
valid_recovery_result: SUCCESS
valid_recovery_channel_identity: hfo-command-and-control_C0BGNGPJFHU
successful_message_writes_this_phase: 0
message_bodies_externalized_to_git: false
latency_exposed: false
operator_relay_minutes: 0
paid_cost_usd_observed: 0
---

# X13 phase 3 — Slack read failure and recovery

The controlled factor was the channel ID on the same bounded read surface.

- Invalid ID `C0X13INVALID0001` returned `execution_failed: channel_not_found` and no unrelated content.
- The connector states this class can mean an absent channel, a different workspace, or insufficient access, so it is not an existence oracle.
- The immediate one-message recovery read from `C0BGNGPJFHU` succeeded and identified `#hfo-command-and-control`.
- No successful Slack write occurred and no message body was copied into Git.

## Measurements

- Custom code avoided: estimated 30–90 LOC for transport, basic error decoding, and history response parsing; unvalidated.
- Operator relay: 0 minutes. Estimated manual reproduction avoided: 2–4 minutes; unvalidated.
- Direct cost observed: $0. Exact plan, quota, rate-limit state, and connector allocation were not exposed.
- Durability: only continued readability after one failed call was observed. Resume, replay, retention, and exactly-once behavior remain unproven.
- Observability: error class, channel ID, valid channel identity, and bounded result count were exposed. Raw HTTP details, request ID, retry count, timing, and audit data were hidden.
- Portability: medium within Slack read semantics; medium-low at the connector wrapper; other platforms unproven.

## Failure behavior

The invalid probe failed terminally without returning unrelated data, and the valid path remained readable. The error is diagnostically coarse because absence, workspace mismatch, and access denial are collapsed into the same class. Rate limits, timeouts, outages, archived channels, and known-resource access denial remain unmeasured.

## Strongest objection and falsifier

Do not adopt this surface as an authoritative resource-existence or authorization check. Phase 4 should permit adoption only with gates that treat `channel_not_found` as ambiguous, prohibit automatic repair, retain Git-first idempotency, and require independent verification before higher-effect use. A known-valid public channel later producing the same error without a documented access change would falsify the current reliability estimate.

## Rollback and honest flaw

The phase was read-only, so no rollback is needed. Both observations used the same wrapper and carry binding weight zero. The probe did not distinguish provider-native failure from wrapper behavior, and it exposed no latency, quota, retry, raw protocol, independent-verifier, or ConsumerAck evidence.
