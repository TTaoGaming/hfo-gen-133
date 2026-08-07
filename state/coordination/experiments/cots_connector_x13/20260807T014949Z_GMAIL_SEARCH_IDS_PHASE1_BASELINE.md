---
schema_id: hfo.gen133.x13.cots_connector_event.v1
experiment_id: X13_GMAIL_SEARCH_IDS_READONLY_013
phase: 1_of_4
phase_status: PHASE1_ACCEPTED_WITH_GATES
candidate: Gmail_search_email_ids_readonly_surface
carrier_task_id: 6a55c1733708819185088bf334e33ea5
carrier_task_id_match: true
wip: 1
prior_current_version: 148
expected_current_version_after_event: 149
valid_time_utc: 2026-08-07T01:49:49Z
recorded_time_utc: 2026-08-07T01:49:49Z
candidate_calls_this_wake: 1
candidate_mutations_this_wake: 0
retries: 0
fallbacks: 0
query: "after:2026/07/30 before:2026/08/08 -in:spam -in:trash"
max_results: 3
returned_message_ids_count: 3
next_page_token_present: true
message_content_hydrated: false
raw_message_ids_persisted: false
raw_next_page_token_persisted: false
connector_error: none
external_call_time_ms: 405
request_sha256: deea67e1897a313be60455d1004de694b170ac9aea4900b30956f2955c5de828
normalized_result_sha256: 4fa78819291c56fc127d851403f232b29124caf38d99565ac35c9567e0c3932d
normalization_contract: ORDERED_MESSAGE_IDS_PLUS_BOOLEAN_NEXT_PAGE_TOKEN_PRESENCE; RAW_IDS_AND_PAGE_TOKEN_NOT_PERSISTED
measured_fact: BOUNDED_GMAIL_SEARCH_EMAIL_IDS_RETURNED_THREE_IDS_WITH_NEXT_PAGE_TOKEN_AND_NO_MESSAGE_BODY_HYDRATION_OR_CONNECTOR_ERROR
provisional_decision: ADOPT_WITH_GATES_CATALOG_ONLY
custom_code_avoided_estimate: 40_to_120_LOC_UNVALIDATED
operator_minutes_removed_measured: 0
credentials: CONNECTOR_MANAGED_EFFECTIVE_IDENTITY_AND_OAUTH_SCOPES_UNKNOWN
durability: GIT_EVENT_DURABLE_GMAIL_MAILBOX_AND_SEARCH_VIEW_MUTABLE_NO_PROVIDER_SNAPSHOT_RECEIPT
observability: MESSAGE_ID_COUNT_PAGE_TOKEN_PRESENCE_ERROR_AND_EXTERNAL_CALL_TIME_EXPOSED; RESULT_SIZE_ESTIMATE_PROVIDER_REQUEST_ID_EFFECTIVE_SCOPE_AND_ACTUAL_QUOTA_DEBIT_NOT_EXPOSED
portability: LOW_TO_MEDIUM_GMAIL_QUERY_SYNTAX_AND_WRAPPER_SPECIFIC
failure_behavior: SUCCESS_WITH_PAGINATION_OBSERVED; EMPTY_PERMISSION_DENIAL_RATE_LIMIT_TRANSIENT_AND_PAGINATION_REPLAY_UNTESTED
paid_cost_usd_observed: 0_NO_CHARGE_SURFACED
direct_cost_or_quota_evidence: NONE_FROM_CONNECTOR
nominal_provider_quota_contract: GMAIL_API_MESSAGES_LIST_COSTS_5_QUOTA_UNITS; 1200000_UNITS_PER_MINUTE_PROJECT; 6000_UNITS_PER_MINUTE_USER_PROJECT; 80000000_UNITS_PER_DAY_PROJECT_BILLING_THRESHOLD; CONNECTOR_MAPPING_AND_DEBIT_UNVERIFIED
catalog_consumer: HFO_COTS_CAPABILITY_INVENTORY
operational_consumer: NOT_ASSIGNED
consumer_ack: NOT_OBSERVED
verifier: DIRECT_CONNECTOR_RECEIPT_PLUS_GIT_EVENT_AND_CURRENT_READBACK; MATCHED_RAW_PROVIDER_CALL_NOT_RUN
strongest_falsifier: MATCHED_RAW_GMAIL_V1_USERS_MESSAGES_LIST_CALL_UNDER_SAME_EFFECTIVE_PRINCIPAL_RETURNS_MATERIALLY_DIFFERENT_ORDER_PAGINATION_QUERY_SCOPE_OR_AUTHORIZATION_SEMANTICS
mandatory_gate: BOUNDED_QUERY; SMALL_MAX_RESULTS; DO_NOT_PERSIST_RAW_MESSAGE_IDS_OR_PAGE_TOKEN; MAX_RESULTS_IS_A_CAP_NOT_COMPLETENESS; NEXT_PAGE_TOKEN_MEANS_MORE_PAGES_MAY_EXIST; DO_NOT_INFER_EFFECTIVE_SCOPE_FROM_WRAPPER_SUCCESS; NO_UNBOUNDED_RETRY; CONSEQUENTIAL_MAILBOX_CLAIMS_REQUIRE_MESSAGE_READ_OR_MATCHED_PROVIDER_WITNESS
honest_flaw: ONE_BOUNDED_RECENT_MAILBOX_SEARCH_TESTS_ONLY_SUCCESS_AND_PAGINATION_SHAPE_NOT_EMPTY_RESULTS_PERMISSION_DENIAL_SPAM_TRASH_SCOPE_VARIANCE_PAGINATION_REPLAY_RATE_LIMIT_TRANSIENT_FAILURE_RAW_PROVIDER_PARITY_OPERATOR_SAVINGS_OR_CONSUMER_VALUE
next_phase: PHASE2_IDENTICAL_BOUNDED_REPLAY_AND_ORDERED_DIGEST_COMPARISON
official_contract_source_1: https://developers.google.com/workspace/gmail/api/reference/rest/v1/users.messages/list
official_contract_source_2: https://developers.google.com/workspace/gmail/api/guides/list-messages
official_quota_source: https://developers.google.com/workspace/gmail/api/reference/quota
---

# X13 Gmail search IDs phase 1 baseline

A single bounded `search_email_ids` call was executed with a seven-day Gmail query and `max_results=3`. The connector returned three message IDs, exposed a next-page token, returned no connector error, and did not hydrate message bodies, subjects, senders, recipients, snippets, or attachments into the tool response.

The raw message IDs and page token are intentionally omitted from this immutable receipt. Only count, token-presence, timing, request digest, and normalized-result digest are retained.

Google's native `users.messages.list` contract returns only message `id` and `threadId` in each listed message, supports `q`, `maxResults`, and `pageToken`, and requires a separate `messages.get` call for full message details. The native method's `maxResults` is a cap, not a completeness claim; pagination is represented by `nextPageToken`.

This establishes only a direct capability baseline for bounded ID-only discovery. Effective OAuth identity/scopes, raw-provider parity, quota debit, permission failures, empty-success behavior, and consumer/operator value remain unknown. No adoption or fitness credit is earned.
