---
schema_id: hfo.gen133.x13.cots_connector_event.v1
experiment_id: X13_GMAIL_ID_ONLY_SEARCH_READONLY_017
expected_prior_current_version: 167
candidate: Gmail_search_email_ids_bounded_query
campaign_wake: 4_of_4
phase: 4
phase_status: PHASE4_DECIDED_ADOPT_WITH_GATES
phase_4_decision: ADOPT_WITH_GATES
operational_decision: ADOPT_WITH_GATES_ID_ONLY_DISCOVERY_ONLY
campaign_status: CLOSED
wip: 1
candidate_calls_this_wake: 0
campaign_calls_total: 2
successful_nonempty_calls: 1
successful_empty_calls: 1
connector_errors_observed: 0
retries_total: 0
fallbacks_total: 0
candidate_mutations_total: 0
phase1_max_results: 3
phase1_returned_message_ids_count: 3
phase1_next_page_token_present: true
phase1_message_content_hydration_observed: false
phase2_identical_replay_provable: false
phase2_result_repeatability: UNKNOWN
phase2_blocker_class: X13_EVIDENCE_DESIGN_DEFECT_NOT_GMAIL_CONNECTOR_FAILURE
phase3_max_results: 3
phase3_returned_message_ids_count: 0
phase3_next_page_token_present: false
phase3_message_content_hydration_observed: false
phase3_exact_privacy_safe_request_descriptor_persisted: true
phase3_request_descriptor_sha256: 240d38eec986c449846e7040866864e2f1c671c14d75ccef6622242d2a68b317
raw_message_ids_persisted_in_receipts: false
raw_next_page_tokens_persisted_in_receipts: false
operator_minutes_removed_measured: 0
custom_code_avoided_estimate: 40_to_120_LOC_UNVALIDATED
paid_cost_usd_observed: 0_NO_PAID_COST_SURFACED
direct_cost_or_quota_evidence: NONE_FROM_CONNECTOR
provider_contract_quota_regime: OFFICIAL_GMAIL_MESSAGES_LIST_5_QUOTA_UNITS_IF_WRAPPER_MAPS_TO_NATIVE_MESSAGES_LIST;POST_MAY1_2026_LIMITS_1200000_UNITS_PER_MIN_PROJECT_6000_UNITS_PER_MIN_USER_PROJECT_80000000_UNITS_PER_DAY_PROJECT_BILLING_THRESHOLD;ACTUAL_CONNECTOR_MAPPING_PROJECT_REGIME_AND_DEBIT_UNKNOWN
credentials: CONNECTOR_MANAGED_EFFECTIVE_PRINCIPAL_AND_SCOPES_UNKNOWN;Q_QUERY_IS_INCOMPATIBLE_WITH_GMAIL_METADATA_SCOPE_PER_OFFICIAL_NATIVE_CONTRACT;LEAST_DATA_OUTPUT_DOES_NOT_PROVE_LEAST_PRIVILEGE_AUTHORIZATION
durability: GIT_OBSERVATION_RECEIPTS_DURABLE;PHASE1_REQUEST_PREIMAGE_NOT_DURABLE;PHASE3_SYNTHETIC_REQUEST_PREIMAGE_AND_CANONICALIZATION_DURABLE;GMAIL_SEARCH_VIEW_MUTABLE
observability: RETURN_COUNT_NEXT_PAGE_TOKEN_PRESENCE_ID_ONLY_RESULT_ERROR_SHAPE_AND_EXTERNAL_CALL_TIME_VISIBLE;PROVIDER_REQUEST_ID_RATE_HEADERS_EFFECTIVE_SCOPE_NATIVE_MAPPING_ACTUAL_QUOTA_DEBIT_NOT_SURFACED
portability: MEDIUM_LIST_AND_PAGINATION_CONCEPTS_PORTABLE;GMAIL_QUERY_SYNTAX_MESSAGE_IDS_SCOPE_MODEL_ALIAS_EXPANSION_AND_THREAD_SEARCH_BEHAVIOR_GOOGLE_SPECIFIC
failure_behavior: ONE_BOUNDED_NONEMPTY_SUCCESS_WITH_CONTINUATION_PLUS_ONE_BOUNDED_SYNTHETIC_EMPTY_SUCCESS_DISTINCT_FROM_ERROR;PHASE2_REPEATABILITY_UNKNOWN_DUE_X13_RECEIPT_DEFECT;NO_PERMISSION_DENIAL_PAGINATION_REPLAY_RATE_LIMIT_TRANSIENT_FAILURE_OR_NATIVE_PARITY_TESTED
verifier: DIRECT_GMAIL_CONNECTOR_RECEIPTS_PLUS_OFFICIAL_GOOGLE_USERS_MESSAGES_LIST_FILTERING_AND_QUOTA_CONTRACTS_PLUS_GITHUB_IMMUTABLE_EVENT_AND_CURRENT_READBACK
consumer: GMAIL_DISCOVERY_CANDIDATE_NO_OPERATIONAL_CONSUMER_ACK
adoption_credit: 1_ID_ONLY_DISCOVERY_ONLY
fitness_credit: 0
decision_confidence: LOW_TO_MEDIUM
mandatory_gate: READONLY_SEARCH_EMAIL_IDS_ONLY;SMALL_MAX_RESULTS;DURABLY_PERSIST_EXACT_PRIVACY_SAFE_REQUEST_DESCRIPTOR_AND_CANONICALIZATION_BEFORE_ANY_REPEATABILITY_CLAIM;DO_NOT_PERSIST_RAW_MESSAGE_IDS_OR_PAGE_TOKENS_IN_X13_RECEIPTS;NEXT_PAGE_TOKEN_MEANS_FIRST_PAGE_IS_NOT_COMPLETE;EMPTY_SUCCESS_IS_NOT_MAILBOX_WIDE_ABSENCE;DO_NOT_FETCH_MESSAGE_CONTENT_UNLESS_SEPARATELY_JUSTIFIED;EFFECTIVE_OAUTH_SCOPE_AND_NATIVE_MAPPING_MUST_BE_TREATED_UNKNOWN;LEAST_DATA_OUTPUT_IS_NOT_EVIDENCE_OF_LEAST_PRIVILEGE_AUTHORIZATION;DO_NOT_ASSUME_GMAIL_UI_SEARCH_PARITY_BECAUSE_API_LACKS_UI_ALIAS_EXPANSION_AND_THREAD_WIDE_SEARCH;USE_EPOCH_SECONDS_FOR_TIMEZONE_PRECISE_DATE_FILTERS;NO_UNBOUNDED_RETRY;PROVIDER_ERRORS_FAIL_CLOSED_NOT_AS_ABSENCE;NO_CONSEQUENTIAL_ACTION_OR_COMPLETENESS_CLAIM_FROM_ID_ONLY_DISCOVERY_WITHOUT_STRONGER_DIRECT_OR_MATCHED_NATIVE_EVIDENCE
strongest_falsifier: A_MATCHED_NATIVE_GMAIL_USERS_MESSAGES_LIST_UNDER_THE_SAME_EFFECTIVE_PRINCIPAL_AND_EXACT_DURABLE_PHASE3_SYNTHETIC_REQUEST_RETURNS_A_NONEMPTY_RESULT_OR_AUTHORIZATION_ERROR_WITHOUT_INTERVENING_MAILBOX_OR_INDEX_CHANGE_OR_THE_WRAPPER_HYDRATES_CONTENT_BEYOND_IDS_IN_A_BOUNDED_SEARCH
honest_flaw: ONLY_TWO_GMAIL_PROVIDER_CALLS_EXIST;PHASE2_REPEATABILITY_REMAINS_UNKNOWN_BECAUSE_PHASE1_REQUEST_PREIMAGE_WAS_NOT_DURABLE;PERMISSION_DENIAL_PAGINATION_REPLAY_ORDER_STABILITY_RATE_LIMIT_TRANSIENT_FAILURE_INDEX_LAG_NATIVE_PARITY_EFFECTIVE_SCOPE_NATIVE_MAPPING_PROVIDER_REQUEST_ID_ACTUAL_QUOTA_DEBIT_OPERATOR_SAVINGS_AND_OPERATIONAL_CONSUMER_VALUE_REMAIN_UNTESTED
next_phase: NEW_CANDIDATE_PHASE1_WIP1
valid_time_utc: 2026-08-07T20:49:18Z
recorded_time_utc: 2026-08-07T20:49:18Z
---

# X13 Gmail ID-only search — Phase 4 decision

## Decision

**ADOPT_WITH_GATES** for bounded, read-only Gmail ID-only discovery only.

No Gmail candidate call was issued in this decision wake. The decision uses the frozen evidence set: Phase 1 observed one bounded nonempty ID-only success with a continuation token; Phase 2 correctly refused to fabricate an identical replay because the Phase-1 request preimage was not durable; Phase 3 observed one bounded synthetic empty success distinct from error using a durable privacy-safe request descriptor.

The Phase-2 Andon is a lab evidence-design defect, not evidence of Gmail instability. It does reduce confidence because cross-wake repeatability remains unknown. For that reason this campaign does not justify stable-result, completeness, trigger, or consequential-action semantics.

## Why adopt instead of invent

The connector exposed a useful least-data search surface without hydrating subject, sender, headers, body, attachment metadata, or thread IDs in either observed provider call. That is enough to prefer the COTS connector over custom Gmail search plumbing for narrow candidate discovery, subject to the gates below. The estimated custom code avoided remains `40–120 LOC` and is explicitly unvalidated; measured operator minutes removed remain `0`, so no fitness credit is claimed.

## Required gates

- Read-only `search_email_ids` use only, with a small explicit result cap.
- Persist an exact privacy-safe request descriptor and canonicalization before making repeatability claims.
- Do not persist raw Gmail message IDs or page tokens in X13 experiment receipts.
- A populated continuation token means the first page is not complete; an empty success is not mailbox-wide absence.
- Do not fetch message content unless a separate capability and data-minimization justification requires it.
- Treat the effective OAuth principal, scope, native-provider mapping, provider request identity, and actual quota debit as unknown unless directly surfaced.
- Least-data output is not evidence of least-privilege authorization. Google's native `users.messages.list` contract says `q` cannot be used with the `gmail.metadata` scope.
- Do not assume Gmail UI/API search parity. Google's filtering guide documents that the API does not perform the UI's alias expansion and does not provide the UI's thread-wide search behavior. For timezone-precise date filters, use epoch seconds rather than relying on date-string midnight interpretation.
- Provider errors fail closed and must never be converted into absence; use bounded retry only if a future operational workflow explicitly justifies it.
- Do not use this ID-only surface as the sole basis for consequential actions or completeness claims without stronger direct-message or matched native-provider evidence.

## Official primary contracts

- `users.messages.list`: https://developers.google.com/workspace/gmail/api/reference/rest/v1/users.messages/list
- Search/filter semantics and Gmail UI differences: https://developers.google.com/workspace/gmail/api/guides/filtering
- Gmail API usage limits: https://developers.google.com/workspace/gmail/api/reference/quota

Google's current native contract says a successful `messages.list` page contains message resources with only `id` and `threadId`, and additional message details require `messages.get`. The current filtering guide documents the UI/API alias-expansion and thread-search differences. The current quota page documents `messages.list` at 5 quota units under the native API, but X13 has no evidence that the connector wrapper maps one-for-one to that native method or which quota regime/debit applies to the connected account.

## Measures and evidence boundary

Campaign provider calls: `2`; nonempty successes: `1`; empty successes: `1`; observed connector errors/retries/fallbacks/mutations: `0/0/0/0`. Phase-2 identical replay repeatability is `UNKNOWN`, not failed. Operator minutes removed: `0` measured. Custom code avoided: `40–120 LOC`, unvalidated. Adoption credit: `1_ID_ONLY_DISCOVERY_ONLY`; fitness credit: `0`.

The strongest falsifier is a matched native `users.messages.list` call under the same effective principal and exact durable Phase-3 synthetic request that materially disagrees on result/error shape without an intervening mailbox/index change, or any bounded connector search that unexpectedly hydrates message content beyond the ID-only contract used here.

## Honest flaw

The campaign is thin: only two Gmail provider calls were made, one nonempty and one synthetic empty. Permission denial, continuation replay, ordering stability, throttling, transient failure, index lag, native parity, effective OAuth scope, wrapper-to-native mapping, provider request identity, actual quota debit, measured operator savings, and an acknowledged operational consumer remain untested. This decision is therefore a narrow COTS preference, not a reliability or completeness certification.
