---
schema_id: hfo.gen133.x13.cots_connector_event.v1
experiment_id: X13_GMAIL_ID_ONLY_SEARCH_READONLY_017
expected_prior_current_version: 164
candidate: Gmail_search_email_ids_bounded_query
campaign_wake: 1_of_4
phase: 1
phase_status: PHASE1_ACCEPTED_WITH_GATES
wip: 1
supersedes_receipt_path: state/coordination/experiments/cots_connector_x13/20260807T174847Z_GMAIL_ID_ONLY_SEARCH_PHASE1_BASELINE.md
supersession_reason: PRIOR_RECEIPT_FRONTMATTER_HAS_ONE_ACCIDENTAL_LEADING_SPACE_BEFORE_DURABILITY_KEY;PRIOR_FILE_REMAINS_IMMUTABLE
candidate_calls_this_wake: 1
campaign_calls_total: 1
successful_nonempty_calls: 1
successful_empty_calls: 0
connector_errors_observed: 0
retries_total: 0
fallbacks_total: 0
candidate_mutations_total: 0
max_results: 3
returned_message_ids_count: 3
next_page_token_present: true
message_body_hydration_observed: false
message_header_hydration_observed: false
thread_id_hydration_observed: false
raw_message_ids_persisted_in_receipt: false
raw_next_page_token_persisted_in_receipt: false
request_digest_sha256: 91fa1bb6bba78deada9b4d1097a9082a56d4a76ff2b6e5d0b04b63580c1263bd
phase1_ordered_message_id_digest_sha256: 6ccac4a570c0d9375ed10f43b45eb71e139b8db12684857dd4dfa2acf44cd26d
connector_call_time_ms: 1151
operator_minutes_removed_measured: 0
custom_code_avoided_estimate: 40_to_120_LOC_UNVALIDATED
paid_cost_usd_observed: 0_NO_PAID_COST_SURFACED
direct_cost_or_quota_evidence: NONE_FROM_CONNECTOR
provider_contract_quota_regime: GMAIL_MESSAGES_LIST_5_QUOTA_UNITS;POST_MAY1_2026_LIMITS_1200000_UNITS_PER_MIN_PROJECT_6000_UNITS_PER_MIN_USER_PROJECT_80000000_UNITS_PER_DAY_PROJECT_BILLING_THRESHOLD;ACTUAL_CONNECTOR_PROJECT_MAY_RETAIN_PRIOR_SETTINGS_IF_USED_NOV2025_TO_APR2026
credentials: CONNECTOR_MANAGED_EFFECTIVE_PRINCIPAL_AND_SCOPES_UNKNOWN;LEAST_DATA_OUTPUT_DOES_NOT_PROVE_LEAST_PRIVILEGE_SCOPE
durability: GIT_RECEIPT_DURABLE;GMAIL_SEARCH_VIEW_MUTABLE
observability: RETURN_COUNT_NEXT_PAGE_TOKEN_PRESENCE_ID_ONLY_RESULT_ERROR_SHAPE_AND_EXTERNAL_CALL_TIME_VISIBLE;PROVIDER_REQUEST_ID_RATE_HEADERS_EFFECTIVE_SCOPE_ACTUAL_QUOTA_DEBIT_NOT_SURFACED
portability: MEDIUM_LIST_AND_PAGINATION_CONCEPTS_PORTABLE;GMAIL_QUERY_SYNTAX_MESSAGE_IDS_AND_SCOPE_MODEL_GOOGLE_SPECIFIC
failure_behavior: ONE_NONEMPTY_SUCCESS_WITH_NEXT_PAGE_TOKEN;NO_PERMISSION_DENIAL_EMPTY_SUCCESS_PAGINATION_REPLAY_RATE_LIMIT_TRANSIENT_FAILURE_OR_NATIVE_PARITY_TESTED
verifier: DIRECT_GMAIL_CONNECTOR_RECEIPT_PLUS_OFFICIAL_GOOGLE_GMAIL_API_CONTRACT_PLUS_GITHUB_IMMUTABLE_EVENT_READBACK
consumer: GMAIL_DISCOVERY_CANDIDATE_NO_OPERATIONAL_CONSUMER_ACK
adoption_credit: 0
fitness_credit: 0
mandatory_gate: READONLY_SEARCH_EMAIL_IDS_ONLY;SMALL_MAX_RESULTS;DO_NOT_PERSIST_RAW_MESSAGE_IDS_OR_PAGE_TOKENS;NEXT_PAGE_TOKEN_MEANS_FIRST_PAGE_IS_NOT_COMPLETE;DO_NOT_INFER_MAILBOX_WIDE_ABSENCE_OR_COMPLETENESS;DO_NOT_FETCH_MESSAGE_CONTENT_UNLESS_SEPARATELY_JUSTIFIED;EFFECTIVE_OAUTH_SCOPE_MUST_BE_TREATED_UNKNOWN;NO_UNBOUNDED_RETRY;PROVIDER_ERRORS_FAIL_CLOSED_NOT_AS_ABSENCE
strongest_falsifier: MATCHED_NATIVE_GMAIL_V1_USERS_MESSAGES_LIST_UNDER_SAME_EFFECTIVE_PRINCIPAL_AND_SAME_QUERY_RETURNS_MATERIALLY_DIFFERENT_ID_SET_PAGINATION_OR_AUTHORIZATION_ERROR_OUTCOME_WITHOUT_INTERVENING_MAILBOX_MUTATION_OR_INDEXING_CHANGE
honest_flaw: ONE_HAPPY_PATH_ONLY;NEXT_PAGE_TOKEN_SHOWS_BOUNDED_RESULT_IS_INCOMPLETE_BY_DESIGN;PERMISSION_DENIAL_EMPTY_SUCCESS_PAGINATION_REPLAY_ORDER_STABILITY_RATE_LIMIT_TRANSIENT_FAILURE_INDEX_LAG_NATIVE_PARITY_EFFECTIVE_SCOPE_PROVIDER_REQUEST_ID_ACTUAL_QUOTA_DEBIT_OPERATOR_SAVINGS_AND_OPERATIONAL_CONSUMER_VALUE_UNTESTED;OFFICIAL_GMAIL_CONTRACT_SAYS_Q_CANNOT_BE_USED_WITH_GMAIL_METADATA_SCOPE_SO_SUCCESSFUL_QUERY_SEARCH_DOES_NOT_ESTABLISH_LEAST_PRIVILEGE_AUTHORIZATION
next_phase: PHASE2_IDENTICAL_BOUNDED_ID_ONLY_REPLAY_AND_ORDERED_DIGEST_COMPARE
valid_time_utc: 2026-08-07T17:48:47Z
recorded_time_utc: 2026-08-07T17:48:47Z
---

# X13 Gmail ID-only search — Phase 1 baseline (immutable correction receipt)

This receipt immutably supersedes the immediately prior Phase-1 file because that file's YAML frontmatter contains one accidental leading space before the `durability` key. The prior file is intentionally not edited.

## Direct measured capability

One bounded `Gmail.search_email_ids` call used a generic recent-mail query with `max_results=3`. It returned exactly 3 message IDs and a next-page token, with no connector error, retry, fallback, or Gmail mutation. Connector-reported external call time was 1151 ms.

The wrapper returned IDs only: no subject, sender, snippet, headers, body, attachment metadata, or thread IDs were hydrated into the model-visible result. Raw Gmail message IDs and the raw pagination token are intentionally omitted from this Git receipt; only counts, presence flags, and SHA-256 digests are retained.

## Official contract baseline

Google's native `users.messages.list` contract lists messages in the authenticated user's mailbox, supports `maxResults`, `pageToken`, `q`, and label filtering, and returns message resources containing only `id` and `threadId` until a separate `messages.get` is used for details. A populated `nextPageToken` is the provider's explicit signal that another result page can be retrieved.

Official contract: https://developers.google.com/workspace/gmail/api/reference/rest/v1/users.messages/list

Google documents `messages.list` at 5 quota units/request. Under the post-May-1-2026 model, documented limits are 1,200,000 quota units/minute/project, 6,000 quota units/minute/user/project, and an 80,000,000-unit/day/project threshold before future billing; projects that used the API from November 2025 through April 2026 can retain prior quota settings. The connector does not expose which regime applies or the actual debit for this call.

Official quota contract: https://developers.google.com/workspace/gmail/api/reference/quota

## Permission / least-data gate

Google states that the `q` parameter cannot be used when accessing `messages.list` with the `gmail.metadata` OAuth scope. The connector successfully executed a query while returning only IDs, but its effective OAuth scope is not exposed. Therefore **least-data output must not be confused with least-privilege authorization**.

Official filtering guide: https://developers.google.com/workspace/gmail/api/guides/filtering

## Phase-1 disposition

**PHASE1_ACCEPTED_WITH_GATES.** This is a promising COTS least-data discovery surface because it can enumerate bounded candidate message IDs without hydrating message content. It is not yet adopted: one happy-path call proves neither pagination behavior, empty-success semantics, permission failure behavior, ordering stability, native parity, effective scope, quota debit, operator savings, nor consumer value.

Next wake: one identical bounded ID-only replay and ordered-result digest comparison. No message-content fetch and no raw Gmail identifiers persisted.
