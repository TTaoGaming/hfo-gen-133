---
schema_id: hfo.gen133.x13.cots_connector_event.v1
experiment_id: X13_GMAIL_SEARCH_EMAIL_IDS_READONLY_001
event_type: PHASE1_OFFICIAL_CONTRACT_AND_DIRECT_CAPABILITY_BASELINE
phase: 1_of_4
phase_status: PHASE1_ACCEPTED_WITH_GATES
candidate: Gmail_search_email_ids_readonly_surface
carrier_task_id: 6a55c1733708819185088bf334e33ea5
carrier_task_id_match: true
wip: 1
repository: TTaoGaming/hfo-gen-133
branch: agent/gen133-bootstrap-20260730
expected_current_version: 92
candidate_calls_this_wake: 1
mutation_count: 0
retry_count: 0
fallback_count: 0
query_boundary: NEWER_THAN_30_DAYS_EXCLUDE_SPAM_AND_TRASH_MAX_RESULTS_1
message_ids_returned_count: 1
continuation_token_returned: true
message_content_returned: false
headers_returned: false
thread_id_returned_by_connector: false
result_size_estimate_returned_by_connector: false
connector_error: NONE
connector_external_call_time_ms: 342
raw_identifier_persisted: false
raw_page_token_persisted: false
operator_minutes_removed_measured: 0
custom_code_avoided_estimate: 15_to_45_LOC_UNVALIDATED
paid_cost_usd_observed: 0_NO_CHARGE_SURFACED
actual_quota_consumed: UNKNOWN
official_method_candidate: GMAIL_USERS_MESSAGES_LIST
official_quota_contract: MESSAGES_LIST_5_UNITS_PER_REQUEST_AS_OF_2026_08_04
credentials: CONNECTOR_MANAGED_EFFECTIVE_IDENTITY_AND_SCOPE_UNKNOWN
durability: IMMUTABLE_GIT_EVENT_PENDING_READBACK
observability: PARTIAL_LATENCY_AND_NORMALIZED_ERROR_FIELDS_NO_HTTP_HEADERS_REQUEST_ID_QUOTA_OR_UPSTREAM_ATTEMPT_COUNT
portability: MEDIUM_GMAIL_QUERY_SYNTAX_AND_PAGE_TOKEN_ARE_PROVIDER_SPECIFIC
failure_behavior: NOT_PROBED_IN_PHASE1
consumer: NONE_NAMED
consumer_ack: NOT_OBSERVED
adoption_credit: 0
fitness_credit: 0
strongest_falsifier: SAME_PRINCIPAL_RAW_USERS_MESSAGES_LIST_RETURNS_DIFFERENT_RESULT_OR_PAGINATION_FOR_IDENTICAL_BOUNDARY
verifier: NOT_ASSIGNED
independent_verification_closed: false
honest_flaw: ONE_POSITIVE_QUERY_ONLY_IDENTITY_SCOPE_QUERY_TRANSLATION_ORDERING_COMPLETENESS_REAL_PAGINATION_FAILURES_RATE_LIMITS_HIDDEN_CALLS_AND_CONSUMER_VALUE_UNVERIFIED
valid_time_utc: 2026-08-04T17:47:32Z
recorded_time_utc: 2026-08-04T17:47:32Z
---

# X13 Gmail `search_email_ids` phase 1 baseline

## Official contract baseline

Google documents `users.messages.list` as a read-only mailbox listing method. A successful raw response can contain message resources limited to `id` and `threadId`, plus optional `nextPageToken` and `resultSizeEstimate`. `maxResults` supports 1 through 500. The `q` parameter uses Gmail search syntax, but Google states that `q` cannot be used when the API is accessed with only the `gmail.metadata` OAuth scope.

Primary sources:

- https://developers.google.com/workspace/gmail/api/reference/rest/v1/users.messages/list
- https://developers.google.com/workspace/gmail/api/reference/quota

As of 2026-08-04, Google documents `messages.list` at 5 quota units per request. Google also documents per-minute and daily-threshold controls, but this connector exposed no quota receipt or billing evidence. The upstream method and call count therefore remain unbound.

## Direct connector observation

One bounded `Gmail.search_email_ids` call used a 30-day window, excluded Spam and Trash, and capped output at one result. The connector returned exactly one message identifier and a continuation token. It returned no subject, sender, recipients, timestamps, body, snippet, attachment metadata, or headers. It also omitted the raw API's `threadId` and `resultSizeEstimate` fields.

The connector reported 342 ms external-call time and no normalized error. It exposed no HTTP status, response headers, provider request ID, quota counter, authenticated principal, OAuth scope, upstream method, or hidden-attempt count. The exact message identifier and continuation token were intentionally not persisted.

## Measured variance and gates

1. The connector output is narrower than the documented raw `users.messages.list` response because it omits `threadId` and `resultSizeEstimate`.
2. A successful query-bearing call proves only that the connector accepted and executed a Gmail-style query. It does not prove a specific OAuth scope. Because Google forbids `q` with metadata-only scope, do not label this connector least-privilege `gmail.metadata` without direct scope evidence.
3. A returned continuation token proves only that another connector page may exist; it does not prove ordering, completeness, or raw-provider token parity.
4. Message IDs and page tokens are sensitive mailbox metadata. Do not persist them without a named consumer and retention need.
5. No operational or fitness credit is allowed until identity and scope, raw-provider parity, pagination behavior, quota evidence, a named consumer, acknowledgment, and measured operator value are established.

## Decision for this wake

`PHASE1_ACCEPTED_WITH_GATES`

Admitted claim only:

`CONNECTOR_RETURNED_ONE_MESSAGE_IDENTIFIER_AND_ONE_CONTINUATION_TOKEN_WITHOUT_MESSAGE_CONTENT_FOR_ONE_BOUNDED_READ_ONLY_SEARCH`

No send, draft, label change, archive, delete, account action, paid call, retry, fallback, or production deployment occurred.

## Next phase

Phase 2 should perform one bounded synthetic unlikely-token search with `max_results=1`, retain no identifiers or query text, perform no pagination, and treat an empty result as nonauthoritative absence.
