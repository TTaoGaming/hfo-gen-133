---
schema_id: hfo.gen133.x13.cots_connector_event.v1
experiment_id: X13_GMAIL_ID_ONLY_SEARCH_READONLY_017
phase: 3
phase_status: PHASE3_ACCEPTED_WITH_GATES_EMPTY_SUCCESS
candidate: Gmail_search_email_ids_bounded_query
wip: 1
expected_current_version: 166
candidate_calls_this_wake: 1
campaign_calls_after_wake: 2
successful_nonempty_calls_after_wake: 1
successful_empty_calls_after_wake: 1
connector_errors_observed_after_wake: 0
retries_this_wake: 0
fallbacks_this_wake: 0
candidate_mutations_this_wake: 0
max_results: 3
returned_message_ids_count: 0
next_page_token_present: false
message_body_hydration_observed: false
message_header_hydration_observed: false
thread_id_hydration_observed: false
raw_message_ids_persisted_in_receipt: false
raw_next_page_token_persisted_in_receipt: false
exact_privacy_safe_request_descriptor_persisted: true
request_descriptor_canonicalization: UTF8_JSON_SORTED_KEYS_COMPACT_SEPARATORS_NO_ASCII_ESCAPING
request_descriptor_sha256: 240d38eec986c449846e7040866864e2f1c671c14d75ccef6622242d2a68b317
connector_call_time_ms: 293
operator_minutes_removed_measured: 0
custom_code_avoided_estimate: 40_to_120_LOC_UNVALIDATED
paid_cost_usd_observed: 0_NO_PAID_COST_SURFACED
direct_cost_or_quota_evidence: NONE_FROM_CONNECTOR
provider_contract_quota_regime: GMAIL_MESSAGES_LIST_5_QUOTA_UNITS;POST_MAY1_2026_LIMITS_1200000_UNITS_PER_MIN_PROJECT_6000_UNITS_PER_MIN_USER_PROJECT_80000000_UNITS_PER_DAY_PROJECT_BILLING_THRESHOLD;ACTUAL_CONNECTOR_PROJECT_MAY_RETAIN_PRIOR_SETTINGS_IF_USED_NOV2025_TO_APR2026
credentials: CONNECTOR_MANAGED_EFFECTIVE_PRINCIPAL_AND_SCOPES_UNKNOWN;Q_QUERY_IS_INCOMPATIBLE_WITH_GMAIL_METADATA_SCOPE_PER_OFFICIAL_CONTRACT_SO_SUCCESSFUL_QUERY_IMPLIES_SOME_OTHER_ACCEPTED_SCOPE_BUT_EXACT_SCOPE_REMAINS_UNKNOWN
durability: THIS_PHASE3_SYNTHETIC_REQUEST_PREIMAGE_AND_CANONICALIZATION_ARE_DURABLE_IN_GIT;GMAIL_SEARCH_VIEW_REMAINS_MUTABLE
observability: EMPTY_RESULT_ERROR_NULL_NEXT_PAGE_ABSENT_AND_EXTERNAL_CALL_TIME_VISIBLE;PROVIDER_REQUEST_ID_RATE_HEADERS_EFFECTIVE_SCOPE_ACTUAL_QUOTA_DEBIT_NOT_SURFACED
portability: MEDIUM_LIST_AND_PAGINATION_CONCEPTS_PORTABLE;GMAIL_QUERY_SYNTAX_MESSAGE_IDS_AND_SCOPE_MODEL_GOOGLE_SPECIFIC
failure_behavior: ONE_SYNTHETIC_NONMATCHING_QUERY_RETURNED_EMPTY_SUCCESS_DISTINCT_FROM_ERROR;NO_RETRY;NO_MAILBOX_WIDE_ABSENCE_CLAIM
verifier: DIRECT_GMAIL_CONNECTOR_RECEIPT_PLUS_OFFICIAL_GOOGLE_USERS_MESSAGES_LIST_AND_GMAIL_QUOTA_CONTRACT_PLUS_GITHUB_IMMUTABLE_EVENT_AND_CURRENT_READBACK_PENDING
consumer: GMAIL_DISCOVERY_CANDIDATE_NO_OPERATIONAL_CONSUMER_ACK
adoption_credit: 0
fitness_credit: 0
mandatory_gate: READONLY_SEARCH_EMAIL_IDS_ONLY;SMALL_MAX_RESULTS;DO_NOT_PERSIST_RAW_MESSAGE_IDS_OR_PAGE_TOKENS;EMPTY_SUCCESS_IS_NOT_MAILBOX_WIDE_ABSENCE;NEXT_PAGE_TOKEN_MEANS_FIRST_PAGE_IS_NOT_COMPLETE;DO_NOT_FETCH_MESSAGE_CONTENT_UNLESS_SEPARATELY_JUSTIFIED;EFFECTIVE_OAUTH_SCOPE_MUST_BE_TREATED_UNKNOWN;LEAST_DATA_OUTPUT_IS_NOT_EVIDENCE_OF_LEAST_PRIVILEGE_AUTHORIZATION;NO_UNBOUNDED_RETRY;PROVIDER_ERRORS_FAIL_CLOSED_NOT_AS_ABSENCE
strongest_falsifier: A_MATCHED_NATIVE_GMAIL_USERS_MESSAGES_LIST_UNDER_THE_SAME_EFFECTIVE_PRINCIPAL_AND_EXACT_SYNTHETIC_REQUEST_RETURNS_A_NONEMPTY_RESULT_OR_AUTHORIZATION_ERROR_WITHOUT_INTERVENING_MAILBOX_OR_INDEX_CHANGE
honest_flaw: THE_SYNTHETIC_TOKEN_WAS_DESIGNED_TO_MISS_SO_THIS_PROBES_ONLY_EMPTY_SUCCESS_SEMANTICS;PERMISSION_DENIAL_PAGINATION_REPLAY_ORDER_STABILITY_RATE_LIMIT_TRANSIENT_FAILURE_INDEX_LAG_NATIVE_PARITY_EFFECTIVE_SCOPE_PROVIDER_REQUEST_ID_ACTUAL_QUOTA_DEBIT_OPERATOR_SAVINGS_AND_OPERATIONAL_CONSUMER_VALUE_REMAIN_UNTESTED
next_phase: PHASE4_DECISION_FROM_FROZEN_TWO_GMAIL_CALL_EVIDENCE_SET_PLUS_PHASE2_REPRODUCIBILITY_ANDON_NO_ADDITIONAL_GMAIL_CANDIDATE_CALL
valid_time_utc: 2026-08-07T19:50:00Z
recorded_time_utc: 2026-08-07T19:50:00Z
---

# X13 Gmail ID-only search — Phase 3

## Exact privacy-safe request descriptor

The synthetic query contains no mailbox-derived data and is durable by design.

```json
{"label_ids":null,"max_results":3,"next_page_token":"","query":"subject:__HFO_X13_SYNTHETIC_NONMATCH_017_PHASE3_9F4C2B__"}
```

Canonicalization: UTF-8 JSON, keys sorted lexicographically, compact separators `,` and `:`, `ensure_ascii=false`. SHA-256: `240d38eec986c449846e7040866864e2f1c671c14d75ccef6622242d2a68b317`.

## Direct micro-use result

Exactly one `search_email_ids` call was issued with the descriptor above. It returned zero message IDs, no next-page token, and null connector error fields in 293 ms. No retry, fallback, Gmail mutation, message-content fetch, or raw mailbox identifier persistence occurred.

This demonstrates only that the connector can represent an empty successful bounded ID-only search distinctly from an error for this synthetic query. It does **not** demonstrate mailbox-wide absence, completeness, stable ordering, permission coverage, or native-provider parity.

## Official contract baseline

Google Gmail API `users.messages.list`: https://developers.google.com/workspace/gmail/api/reference/rest/v1/users.messages/list

The official contract says `q` filters messages using Gmail search syntax; `maxResults` bounds a page; `pageToken` retrieves another page; a listed message contains only `id` and `threadId` until separately fetched; and `q` cannot be used with the `gmail.metadata` scope.

Google Gmail API usage limits: https://developers.google.com/workspace/gmail/api/reference/quota

As documented for the post-May-1-2026 quota model, `messages.list` costs 5 quota units; limits are 1,200,000 units/minute/project and 6,000 units/minute/user/project, with an 80,000,000-unit/day/project billing threshold. Projects active from November 2025 through April 2026 may retain prior quotas. The connector did not expose its actual quota debit or project regime.

## Decision posture

Phase 3 is accepted with gates. The strongest observed property is empty-success/error distinction with least-data output. The strongest remaining defect is evidence coverage: permission denial, pagination replay, transient/rate-limit behavior, effective OAuth scope, provider request identity, actual quota debit, and operational consumer value remain unknown.

Phase 4 must decide from the frozen evidence set only: Phase 1 one bounded nonempty ID-only success with continuation token; Phase 2 reproducibility Andon caused by missing durable request preimage; Phase 3 one bounded synthetic empty success with a durable exact request descriptor. No additional Gmail candidate call is authorized for the decision wake.
