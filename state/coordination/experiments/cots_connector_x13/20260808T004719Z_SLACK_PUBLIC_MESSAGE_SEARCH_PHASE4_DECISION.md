---
schema_id: hfo.gen133.x13.cots_connector_event.v1
experiment_id: X13_SLACK_PUBLIC_MESSAGE_SEARCH_READONLY_018
event_type: PHASE4_DECISION
phase: 4_of_4
phase_status: PHASE4_ACCEPTED_WITH_GATES
decision: ADOPT_WITH_GATES
operational_decision: ADOPT_BOUNDED_PUBLIC_READONLY_DISCOVERY_ONLY
expected_current_version: 171
next_current_version: 172
wip: 1
candidate: Slack_slack_search_public_bounded_message_search
candidate_calls_this_wake: 0
campaign_calls_total: 3
successful_nonempty_calls: 2
successful_empty_calls: 1
connector_errors_observed: 0
retries_total: 0
fallbacks_total: 0
candidate_mutations_total: 0
phase1_returned_message_count: 3
phase2_returned_message_count: 3
phase3_returned_message_count: 0
phase1_next_cursor_present: true
phase2_next_cursor_present: true
phase3_next_cursor_present: false
phase1_message_text_hydration_observed: true
phase2_message_text_hydration_observed: true
phase3_message_text_hydration_observed: false
phase2_identical_request_replay_proven: true
phase2_live_top3_changed_after_intervening_matching_messages: true
phase3_empty_success_observed: true
raw_message_text_persisted_in_x13_receipts: false
raw_result_urls_persisted_in_x13_receipts: false
raw_pagination_cursor_persisted_in_x13_receipts: false
operator_minutes_removed_measured: 0
custom_code_avoided_estimate: 60_to_180_LOC_UNVALIDATED
paid_cost_usd_observed: 0_NO_CHARGE_SURFACED_NOT_BILLING_PROOF
direct_cost_or_quota_evidence: NONE_FROM_CONNECTOR
credentials: CONNECTOR_MANAGED_EFFECTIVE_PRINCIPAL_TOKEN_TYPE_AND_SCOPES_UNKNOWN;PUBLIC_ONLY_WRAPPER_OBSERVED;NATIVE_PROVIDER_METHOD_MAPPING_UNKNOWN
durability: GIT_DECISION_AND_OBSERVATION_RECEIPTS_DURABLE;SLACK_SEARCH_RESULTS_ARE_MUTABLE_QUERY_VIEWS_NOT_SNAPSHOTS
observability: REQUEST_DESCRIPTOR_RESULT_COUNT_CONTINUATION_OR_END_OF_RESULTS_CONTENT_HYDRATION_AND_DISPLAY_TIMES_OBSERVED;PROVIDER_REQUEST_ID_HTTP_STATUS_RATE_HEADERS_EFFECTIVE_SCOPE_TOKEN_TYPE_NATIVE_METHOD_AND_ACTUAL_QUOTA_DEBIT_NOT_SURFACED
portability: LOW_TO_MEDIUM_SEARCH_EMPTY_SUCCESS_CURSOR_PAGINATION_AND_TIME_SORT_ARE_GENERIC;SLACK_QUERY_MODIFIERS_CHANNEL_IDENTIFIERS_RESULT_MODEL_AND_AUTHORIZATION_ARE_SLACK_SPECIFIC
failure_behavior: THREE_BOUNDED_PUBLIC_READONLY_SEARCHES_COMPLETED_WITH_TWO_NONEMPTY_SUCCESS_ONE_EMPTY_SUCCESS_AND_ZERO_OBSERVED_CONNECTOR_ERRORS;PERMISSION_DENIAL_INVALID_CURSOR_RATE_LIMIT_TRANSIENT_FAILURE_AND_NATIVE_PARITY_UNTESTED
connector_variance_probe: NONEMPTY_SEARCH_RETURNS_MATCHING_MESSAGE_CONTENT_PLUS_CONTINUATION_WHILE_SYNTHETIC_NONMATCHING_SEARCH_RETURNS_ZERO_MATCHES_PLUS_EXPLICIT_END_OF_RESULTS;CONCISE_IS_NOT_LEAST_DATA
verifier: DIRECT_SLACK_CONNECTOR_RECEIPTS_PLUS_DURABLE_PRIVACY_SAFE_REQUEST_DESCRIPTORS_PLUS_OFFICIAL_SLACK_DEVELOPER_DOCUMENTATION_PLUS_GITHUB_IMMUTABLE_EVENT_AND_CURRENT_READBACK
consumer: HFO_COMMAND_AND_CONTROL_DISCOVERY_CANDIDATE_NO_DOWNSTREAM_CONSUMER_ACK
adoption_credit: 1_PUBLIC_READONLY_DISCOVERY_ONLY
fitness_credit: 0
mandatory_gate: READONLY_PUBLIC_SEARCH_ONLY;SMALL_EXPLICIT_RESULT_CAP;KEEP_CONTEXT_DISABLED_UNLESS_SEPARATELY_JUSTIFIED;TREAT_CONCISE_AS_CONTENT_BEARING_NOT_LEAST_DATA;DO_NOT_PERSIST_RAW_SLACK_MESSAGE_TEXT_RESULT_URLS_OR_PAGINATION_CURSORS_IN_X13_RECEIPTS;DURABLY_PERSIST_EXACT_PRIVACY_SAFE_REQUEST_DESCRIPTOR_AND_RESULT_DIGEST_CANONICALIZATION_BEFORE_REPEATABILITY_CLAIMS;CONTINUATION_MEANS_FIRST_PAGE_INCOMPLETE;EMPTY_SUCCESS_IS_NOT_WORKSPACE_WIDE_ABSENCE_OR_COMPLETENESS;REPEATED_SEARCH_IS_A_LIVE_MUTABLE_QUERY_NOT_A_SNAPSHOT;NATIVE_METHOD_EFFECTIVE_PRINCIPAL_TOKEN_TYPE_AND_SCOPES_REMAIN_UNKNOWN;DO_NOT_ASSUME_CONNECTOR_MAPS_TO_ASSISTANT_SEARCH_CONTEXT_OR_LEGACY_SEARCH_MESSAGES;NO_UNBOUNDED_RETRY;PROVIDER_ERRORS_FAIL_CLOSED;NO_CONSEQUENTIAL_AUTHORIZATION_COMPLETENESS_OR ABSENCE_CLAIMS_FROM_SEARCH_ONLY
strongest_falsifier: UNDER_A_QUIESCENT_MATCH_SET_A_MATCHED_PROVIDER_DIRECT_SLACK_SEARCH_UNDER_THE_SAME_EFFECTIVE_PRINCIPAL_AND_EXACT_DURABLE_REQUEST_MATERIALLY_DISAGREES_ON_PUBLIC_RESULT_SET_ORDER_OR_CONTINUATION_OR_THE_PUBLIC_ONLY_WRAPPER_RETURNS_CONTENT_FROM_A_NONPUBLIC_CONVERSATION
honest_flaw: THREE_CALL_CAMPAIGN_DID_NOT_TEST_PERMISSION_DENIAL_INVALID_CURSOR RATE_LIMIT TRANSIENT_FAILURE EFFECTIVE_PRINCIPAL TOKEN_TYPE SCOPES NATIVE_METHOD ACTUAL_COST_OR_QUOTA OPERATOR_SAVINGS OR_DOWNSTREAM_CONSUMER_VALUE;PHASE1_RESULT_DIGEST_SERIALIZATION_WAS_UNDERSPECIFIED;NONEMPTY_SEARCH_HYDRATES_MATCHING_MESSAGE_TEXT
provider_contract_summary: SLACK_OFFICIAL_DOCS_CURRENTLY_RECOMMEND_REAL_TIME_SEARCH_ASSISTANT_SEARCH_CONTEXT_OVER_LEGACY_SEARCH_MESSAGES;ASSISTANT_SEARCH_CONTEXT_SUPPORTS_GRANULAR_SEARCH_READ_PUBLIC_SCOPE_AND_CURSOR_PAGINATION_WITH_SPECIAL_RATE_LIMITS;SEARCH_MESSAGES_IS_EXPLICITLY_LEGACY;CONNECTOR_NATIVE_MAPPING_REMAINS_UNKNOWN
provider_docs:
  - https://docs.slack.dev/reference/methods/assistant.search.context/
  - https://docs.slack.dev/apis/web-api/real-time-search-api/
  - https://docs.slack.dev/reference/methods/search.messages/
provider_docs_checked_utc: 2026-08-08T00:47:19Z
next_phase: CLOSE_CAMPAIGN_AND_START_EXACTLY_ONE_NEW_CANDIDATE_PHASE1_ON_NEXT_WAKE
valid_time_utc: 2026-08-08T00:47:19Z
recorded_time_utc: 2026-08-08T00:47:19Z
---

# X13 Slack public message search — Phase 4 decision

Decision: **ADOPT_WITH_GATES** for bounded, read-only, public Slack discovery only.

No Slack candidate call was issued in Phase 4. The decision uses the frozen three-call campaign evidence: two bounded nonempty successes with continuation, one bounded synthetic empty success with explicit end-of-results, zero observed connector errors, zero retries, zero fallbacks, and zero Slack mutations.

The surface is useful enough to prefer over custom search plumbing for narrow discovery, but it is not a reliability, authorization, privacy-minimization, or completeness certification. Nonempty `concise` results hydrate matching message text; repeated identical searches are live mutable query views rather than snapshots; and the connector does not expose its effective Slack principal, token type, OAuth scopes, provider-native method, request ID, rate-limit headers, or actual quota debit.

## Official contract check

Slack's current developer documentation recommends the Real-time Search API (`assistant.search.context`) rather than legacy `search.messages`. `assistant.search.context` supports granular `search:read.public` authorization and cursor pagination and has special rate limits. `search.messages` is explicitly marked legacy. X13 cannot prove that the connector maps to either provider-native method, so native mapping and actual quota regime remain unknown.

## Adoption gates

Use only for small, bounded, read-only public discovery. Keep context disabled unless separately justified. Treat `concise` as content-bearing, not least-data. Do not persist raw Slack message text, result URLs, or pagination cursors in X13 receipts. A continuation cursor means the observed page is incomplete. Empty success does not establish workspace-wide absence or completeness. Repeated search does not establish snapshot stability. Do not infer provider-native method, effective principal, token type, or scopes from wrapper shape. Fail closed on provider errors, do not use unbounded retry, and do not make consequential, authorization, completeness, or absence claims from search alone.

## Measures

Measured operator minutes removed: `0`. Estimated custom code avoided: `60–180 LOC`, unvalidated. Direct paid cost observed: `$0` only in the narrow sense that no charge surfaced; this is not billing proof. Direct quota debit evidence: none from connector. Adoption credit: `1_PUBLIC_READONLY_DISCOVERY_ONLY`. Fitness credit: `0` pending an acknowledged downstream consumer and measured operator value.

## Strongest falsifier

Under a quiescent match set, a matched provider-direct Slack search under the same effective principal and exact durable request materially disagrees on public result set, ordering, or continuation; or the public-only wrapper returns content from a nonpublic conversation.

## Honest flaw

This three-call campaign did not test permission denial, invalid cursors, throttling, transient failure, native parity, effective authorization, actual cost/quota debit, measured operator savings, or downstream consumer value. Phase 1 also under-specified result-digest serialization. Most importantly for privacy, nonempty search hydrates matching message text.
