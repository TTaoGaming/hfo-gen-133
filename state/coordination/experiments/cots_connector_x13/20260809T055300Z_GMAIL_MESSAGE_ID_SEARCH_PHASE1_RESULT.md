---
schema_id: hfo.gen133.x13.cots_connector_event.v1
experiment_id: X13_GMAIL_MESSAGE_ID_SEARCH_READONLY_026
event_type: PHASE1_RESULT
phase: 1
campaign_wake: 1_of_4
expected_current_version: 200
next_current_version: 201
candidate: Gmail_search_email_ids_readonly
phase_status: PHASE1_ACCEPTED_WITH_GATES
wip: 1
candidate_calls_this_wake: 1
candidate_invocations_total: 1
usable_candidate_results: 1
result_count: 5
max_results_requested: 5
next_page_token_present: true
ordered_message_id_sha256: 55886e1c075eb5b19ebbf4034601148f6b84c0826f4bb1385f0def01ce05257c
raw_message_ids_persisted: false
raw_page_token_persisted: false
content_hydrations_total: 0
connector_errors_total: 0
retries_total: 0
fallbacks_total: 0
candidate_mutations_total: 0
external_call_time_ms: 281
operator_minutes_removed_measured: 0
custom_code_avoided_estimate: 30_to_90_LOC_UNVALIDATED
custom_code_avoided_realized_by_this_candidate: 0
paid_cost_usd_observed: 0_NO_CHARGE_SURFACED_NOT_BILLING_PROOF
direct_cost_or_quota_evidence: CONNECTOR_EXPOSED_NO_QUOTA_DEBIT_RATE_HEADERS_OR_BILLING_METADATA;OFFICIAL_GMAIL_MESSAGES_LIST_COST_IS_5_QUOTA_UNITS;CURRENT_STANDARD_LIMITS_ARE_1200000_UNITS_PER_MINUTE_PER_PROJECT_AND_6000_PER_MINUTE_PER_USER_PER_PROJECT_WITH_80000000_UNITS_PER_DAY_PER_PROJECT_BEFORE_PLANNED_FUTURE_CHARGES_FOR_NEWER_PROJECT_QUOTAS
credentials: GMAIL_CONNECTOR_MANAGED_EFFECTIVE_SCOPE_PRINCIPAL_AND_CLOUD_PROJECT_UNKNOWN;SUCCESSFUL_QUERY_FILTERED_READ_PROVES_NONINTERACTIVE_ACCESS_FOR_THIS_CALL_ONLY;IF_CONNECTOR_MAPS_DIRECTLY_TO_NATIVE_USERS_MESSAGES_LIST_THEN_Q_SUCCESS_IS_INCONSISTENT_WITH_GMAIL_METADATA_ONLY_SCOPE_BUT_NATIVE_MAPPING_IS_NOT_PROVEN
durability: GIT_PHASE1_PREFLIGHT_AND_RESULT_EVENTS_ON_CANONICAL_BRANCH_WITH_PREFLIGHT_READBACK_VERIFIED
observability: RESULT_COUNT_NEXT_PAGE_TOKEN_PRESENCE_WRAPPER_TIMING_AND_ORDERED_ID_DIGEST_AVAILABLE;NO_PROVIDER_REQUEST_ID_RATE_HEADERS_NATIVE_METHOD_EFFECTIVE_SCOPE_OR_QUOTA_DEBIT_EXPOSED
portability: MEDIUM_QUERY_LABEL_MAX_RESULTS_AND_PAGE_TOKEN_CONCEPTS_ALIGN_WITH_NATIVE_USERS_MESSAGES_LIST_BUT_CONNECTOR_WRAPPER_MAPPING_AND_ORDERING_SEMANTICS_REMAIN_UNPROVEN
failure_behavior: NOT_PROBED_IN_PHASE1;SUCCESS_PATH_RETURNED_BOUNDED_IDS_AND_PAGE_TOKEN_WITHOUT_RETRY_FALLBACK_OR_MUTATION
verifier: GITHUB_PREFLIGHT_READBACK_PLUS_DIRECT_GMAIL_SEARCH_EMAIL_IDS_RECEIPT_PLUS_RESULT_EVENT_READBACK
consumer: HFO_BOUNDED_MAILBOX_DISCOVERY_AND_PREFLIGHT_FILTERING
adoption_credit: 0
fitness_credit: 0
mandatory_gate: READ_ONLY;ID_ONLY;BOUNDED_MAX_RESULTS;NO_CONTENT_HYDRATION;NO_RAW_MAILBOX_IDENTIFIERS_IN_X13_RECEIPTS;NO_COMPLETENESS_OR_STABLE_ORDER_INFERENCE_FROM_CAPPED_PAGE
strongest_falsifier: EXACT_REPLAY_ON_A_STABLE_WINDOW_FAILS_NONINTERACTIVELY_OR_VIOLATES_MAX_RESULTS_OR_LOSES_PAGE_TOKEN_CONTRACT_WITHOUT_EXPLANATION
honest_flaw: ONE_SUCCESSFUL_PAGE_ONLY;QUERY_WINDOW_IS_TIME_RELATIVE_AND_CAN_CHANGE_BETWEEN_WAKES;PAGINATION_PERMISSION_DENIAL_RATE_LIMITING_EFFECTIVE_SCOPE_NATIVE_MAPPING_AND_ACTUAL_QUOTA_DEBIT_UNVERIFIED
next_phase: PHASE2_EXACT_REQUEST_REPLAY_COMPARE_COUNT_TOKEN_PRESENCE_AND_ORDERED_ID_DIGEST_WITH_TIME_WINDOW_DRIFT_EXPLICITLY_ALLOWED
valid_time_utc: 2026-08-09T05:53:00Z
recorded_time_utc: 2026-08-09T05:53:00Z
---

# X13 Phase 1 Result — Gmail message-ID search

The preflighted read-only `search_email_ids` request completed non-interactively in 281 ms and returned exactly 5 message IDs, equal to the requested cap, plus a next-page token. No message bodies, subjects, senders, snippets, attachments, thread content, or Gmail mutations were requested. X13 persisted only the count, token presence, wrapper timing, and a privacy-safe ordered-ID digest.

Official Gmail API contract baseline: native `users.messages.list` is `GET /gmail/v1/users/{userId}/messages`; `maxResults` defaults to 100 and permits up to 500, `pageToken` selects a page, `q` uses Gmail search syntax, and `labelIds[]` filters labels. A successful native response contains message entries with only ID/thread ID until `messages.get` is called. Native `q` cannot be used with the `gmail.metadata` OAuth scope. The connector did not expose its native mapping or effective scope, so no direct-equivalence claim is made.

Current official quota context (updated June 3, 2026): `messages.list` costs 5 quota units; standard quotas are 1,200,000 units/minute/project and 6,000 units/minute/user/project; the daily billing threshold is 80,000,000 units/project, and standard use is currently available at no additional cost. This call exposed no actual quota debit, rate-limit headers, billing project, or charge evidence.

Phase 1 is accepted with gates. This establishes only one bounded ID-only success page. It does not establish completeness, stable ordering, valid pagination, permission-denial behavior, rate-limit handling, native method mapping, effective OAuth scope, or actual quota consumption.