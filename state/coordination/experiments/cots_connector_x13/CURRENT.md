---
schema_id: hfo.gen133.x13.cots_connector_current.v1
experiment_id: X13_GMAIL_SEARCH_EMAIL_IDS_READONLY_001
version: 93
prior_version: 92
candidate: Gmail_search_email_ids_readonly_surface
campaign_wake: 1_of_4
campaign_status: ACTIVE
phase_1_completed: true
phase_1_status: PHASE1_ACCEPTED_WITH_GATES
phase_2_completed: false
phase_2_status: PENDING
phase_3_completed: false
phase_3_status: PENDING
phase_4_completed: false
phase_4_decision: PENDING
adoption_mode: NONE_NONOPERATIONAL
carrier_task_id: 6a55c1733708819185088bf334e33ea5
carrier_task_id_match: true
wip: 1
last_event_commit: a5a31521657b340e8efb341f0773411da6b5697d
last_event_path: state/coordination/experiments/cots_connector_x13/20260804T174732Z_GMAIL_SEARCH_EMAIL_IDS_PHASE1_BASELINE.md
last_event_blob_sha: 67ef6c3f50e654601fa9cb7ff839a7a9d5048320
last_event_readback: true
prior_current_commit: c9da65bce3b99f61a9ecf4f80aa750022e61a8ce
prior_current_blob_sha: 76c8034a3751f0e9f7d5c0f733545243d319fcd7
adoption_credit: 0
fitness_credit: 0
consumer_ack: NOT_OBSERVED
operator_minutes_removed_measured: 0
custom_code_avoided_estimate: 15_to_45_LOC_UNVALIDATED
paid_cost_usd_observed: 0_NO_CHARGE_SURFACED
actual_quota_consumed: UNKNOWN
official_quota_contract: MESSAGES_LIST_5_UNITS_PER_REQUEST_AS_OF_2026_08_04
campaign_calls: 1_READONLY_1_SUCCESS_0_RETRY_0_FALLBACK_0_MUTATION
result_shape: ONE_MESSAGE_ID_AND_CONTINUATION_TOKEN_NO_CONTENT_HEADERS_THREAD_ID_OR_RESULT_SIZE_ESTIMATE
connector_variance: OUTPUT_NARROWER_THAN_RAW_USERS_MESSAGES_LIST_QUERY_SUCCESS_DOES_NOT_PROVE_METADATA_SCOPE
credentials: CONNECTOR_MANAGED_IDENTITY_AND_EFFECTIVE_SCOPE_UNKNOWN
durability: CANONICAL_GIT_EVENT_READ_BACK_AND_VERSIONED_CURRENT_PENDING_READBACK
observability: PARTIAL_342MS_AND_NORMALIZED_ERROR_FIELDS_NO_HTTP_HEADERS_REQUEST_ID_QUOTA_OR_HIDDEN_ATTEMPTS
portability: MEDIUM
failure_behavior: NOT_PROBED_IN_PHASE1
mandatory_gate: BOUNDED_READONLY_ID_ONLY_SEARCH_NO_IDENTIFIER_RETENTION_ZERO_RESULTS_NONAUTHORITATIVE_RAW_SCOPE_AND_PAGINATION_WITNESS_REQUIRED
strongest_falsifier: SAME_PRINCIPAL_RAW_USERS_MESSAGES_LIST_RETURNS_DIFFERENT_RESULT_OR_PAGINATION_FOR_IDENTICAL_BOUNDARY
verifier: NOT_ASSIGNED
independent_verification_closed: false
honest_flaw: ONE_POSITIVE_QUERY_ONLY_IDENTITY_SCOPE_QUERY_TRANSLATION_ORDERING_COMPLETENESS_REAL_PAGINATION_FAILURES_RATE_LIMITS_HIDDEN_CALLS_AND_CONSUMER_VALUE_UNVERIFIED
next_phase: PHASE2_SMALLEST_HARMLESS_READONLY_MICRO_USE
next_probe: ONE_SYNTHETIC_UNLIKELY_TOKEN_SEARCH_MAX_RESULTS_1_NO_PAGINATION_NO_IDENTIFIER_OR_QUERY_RETENTION
valid_time_utc: 2026-08-04T17:47:32Z
recorded_time_utc: 2026-08-04T17:47:32Z
---

# X13 CURRENT v93

The Gmail `search_email_ids` campaign is active at phase 1 of 4. One bounded read-only search over the last 30 days, excluding Spam and Trash and capped at one result, returned one message identifier and one continuation token without message content, headers, subject, sender, timestamps, thread ID, or result-size estimate. The exact identifier and token were not persisted.

Google's raw `users.messages.list` contract can return message `id` and `threadId`, optional `nextPageToken`, and `resultSizeEstimate`; Google documents `messages.list` at 5 quota units per request as of 2026-08-04. This connector's upstream method, call count, authenticated principal, effective OAuth scope, and actual quota debit remain unknown. Because Google forbids `q` under metadata-only scope, successful connector query execution must not be represented as proof of least-privilege `gmail.metadata` authorization.

Phase 1 is `PHASE1_ACCEPTED_WITH_GATES`. Adoption and fitness credit remain zero. Phase 2 is limited to one synthetic unlikely-token search with `max_results=1`, no pagination, no identifier or exact-query persistence, and no inference that an empty result proves absence.
