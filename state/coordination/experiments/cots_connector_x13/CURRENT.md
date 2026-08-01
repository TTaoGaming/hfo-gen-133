---
schema_id: hfo.gen133.x13.cots_connector_current.v1
experiment_id: X13_GITHUB_CONTENTS_API_001
version: 8
prior_version: 7
candidate: GitHub_REST_Contents_API
candidate_contract_reference: official_REST_versions_2026-03-10_and_2022-11-28_connector_header_not_exposed
campaign_wake: 4_of_4
phase_1_completed: true
phase_2_completed: true
phase_3_completed: true
phase_4_decision: ADOPT_WITH_GATES
phase_status: CAMPAIGN_COMPLETE_NARROW_INTERNAL_ADOPTION_WITH_GATES
binding_architecture_decision: false
last_event_commit: 9cb0a9368a7ccf3b6e4f1a5ae62cfada2e134db8
last_event_path: state/coordination/experiments/cots_connector_x13/20260801T044846Z_GITHUB_CONTENTS_API_PHASE4_ADOPT_WITH_GATES.md
last_event_utf8_bytes: 8424
last_event_sha256: 20d1efa2971969dd5a614e1451503f41bc14a8b33c8be7ff02f498d2cb990fc7
adoption_credit: 2
adoption_credit_basis: DIRECT_EXACT_BYTE_REVERSIBLE_MICRO_USE_PLUS_SINGLE_PATH_STALE_SHA_REJECTION
fitness_credit: 0_UNTIL_CONSUMED_BY_WORKITEM
carrier_task_id: 6a55c1733708819185088bf334e33ea5
carrier_task_id_verified: true
decision_scope: APPROVED_NON_SENSITIVE_SERIAL_SINGLE_FILE_UTF8_CONTENTS_OPERATIONS_ONLY
required_gates:
  - exact_repository_branch_path_binding
  - one_writer_per_path_and_serial_operations
  - fetch_current_blob_sha_before_update
  - conflict_or_ambiguity_fail_closed_then_exact_readback
  - exact_utf8_commit_blob_branch_path_readback
  - forward_commit_rollback_only
  - no_cross_file_atomicity_or_exactly_once_claim
  - hidden_auth_version_quota_retry_audit_fields_marked_unknown
  - distinct_nonproducer_before_higher_effect_use
  - estimates_zero_fitness_until_consumed
operator_relay_minutes: 0
operator_minutes_removed_estimate: 5_to_15_per_bounded_sequence_UNVALIDATED
custom_code_avoided_estimate: 40_to_120_LOC_UNVALIDATED
paid_cost_usd_observed: 0
live_authentication_class: UNKNOWN
live_authentication_scope: NOT_EXPOSED
live_rate_limit_headers: NOT_EXPOSED
effective_api_version_from_direct_receipt: UNKNOWN
observed_failure_behavior: ONE_SERIAL_STALE_SHA_UPDATE_REJECTED_WITH_409_NEWER_BYTES_PRESERVED
portability: MEDIUM_HIGH_CONTRACT_MEDIUM_LOW_CONNECTOR_OTHER_FORGES_UNPROVEN
verifier: S04_STRUCTURAL_PREFLIGHT_THEN_DISTINCT_NONPRODUCER_BEFORE_HIGHER_EFFECT_USE
consumer: Ratatoskr_and_Olrun
consumer_ack: NOT_OBSERVED
same_provider_binding_weight: 0
strongest_falsifier: STALE_BYTES_LAND_WRONG_TARGET_INCONSISTENT_READBACK_HIDDEN_RETRY_UNINTENDED_COMMIT_OR_SCOPE_CANNOT_BE_REDUCED
review_expiry_utc: 2026-09-01T04:48:46Z
next_candidate: Slack_public_channel_connector
next_candidate_phase: PHASE1_OFFICIAL_CONTRACT_AND_DIRECT_BASELINE
valid_time_utc: 2026-08-01T04:48:46Z
transaction_time_utc: SEE_GIT_COMMIT_METADATA
sealed: false
---

# X13 current campaign

The four-wake GitHub REST Contents API campaign is complete with
`ADOPT_WITH_GATES` at a narrow internal effect ceiling.

Admitted use is limited to serialized single-file UTF-8 create, fetch, current-SHA-bound
replacement, exact readback, and forward rollback on explicitly approved non-sensitive
paths. Any conflict or ambiguous connector result fails closed and requires exact
readback before reconciliation.

The result does not establish database transactions, cross-file atomicity, exactly-once
execution, linearizability, workflow durability, least privilege, independent
verification, or ConsumerAck. Authentication identity/scope, effective API version,
rate-limit state, ETag, request IDs, retries, and audit attribution remain hidden.

Same-provider evidence has binding weight zero. A distinct nonproducer must reproduce or
consume the exact packet before higher-effect dependency. Estimated operator minutes and
custom code avoided remain unvalidated and earn zero fitness credit until tied to a
consumed WorkItem.

The next queued candidate is the Slack public-channel connector. No phase-1 Slack
experiment was started in this wake.
