---
schema_id: hfo.gen133.x13.cots_connector_event.v1
experiment_id: X13_GMAIL_SEARCH_EMAIL_IDS_READONLY_001
event_type: PHASE3_FAILURE_PERMISSION_PORTABILITY_CONNECTOR_VARIANCE_PROBE
phase: 3_of_4
status: PHASE3_ACCEPTED_WITH_GATES
candidate: Gmail_search_email_ids_readonly_surface
carrier_task_id: 6a55c1733708819185088bf334e33ea5
carrier_task_id_match: true
wip: 1
prior_current_version: 94
expected_current_version: 95
probe_boundary: ONE_READONLY_SEARCH_MAX_RESULTS_1_LAST_30_DAYS_SPAM_TRASH_EXCLUDED_WITH_SYNTHETIC_INVALID_PAGE_TOKEN
exact_query_retained: false
exact_page_token_retained: false
connector_calls: 1
connector_successes: 0
connector_failures: 1
retries: 0
fallbacks: 0
pagination_followups: 0
hydration_calls: 0
mutations: 0
messages_returned: 0
content_or_headers_returned: 0
connector_error_type: google_api_error
connector_error_code: invalidArgument
connector_error_status: INVALID_ARGUMENT
connector_error_reason: invalidArgument
connector_error_message: Failed_to_search_email_ids
http_status_exposed: false
http_headers_exposed: false
provider_request_id_exposed: false
raw_provider_error_body_exposed: false
query_or_token_echo_observed: false
latency_exposed: false
paid_cost_usd_observed: 0_NO_CHARGE_SURFACED
actual_quota_consumed: UNKNOWN
official_quota_contract: USERS_MESSAGES_LIST_5_UNITS_PER_REQUEST_AS_OF_2026_08_04
custom_code_avoided_estimate: 15_to_45_LOC_UNVALIDATED
operator_minutes_removed_measured: 0
credentials: CONNECTOR_MANAGED_IDENTITY_AND_EFFECTIVE_SCOPE_UNKNOWN
durability: IMMUTABLE_GIT_EVENT_AND_VERSIONED_CURRENT
observability: PARTIAL_TYPED_NORMALIZED_INVALID_ARGUMENT_WITHOUT_HTTP_STATUS_HEADERS_REQUEST_ID_RAW_BODY_LATENCY_QUOTA_OR_HIDDEN_ATTEMPTS
portability: MEDIUM
failure_behavior: FAILED_CLOSED_WITH_TYPED_NORMALIZED_CLIENT_ARGUMENT_ERROR_AND_NO_MESSAGE_IDS
strongest_falsifier: SAME_PRINCIPAL_RAW_USERS_MESSAGES_LIST_ACCEPTS_THE_IDENTICAL_INVALID_TOKEN_OR_CONNECTOR_REJECTS_AN_IMMEDIATELY_PRECEDING_VALID_RETURNED_TOKEN_UNDER_AN_IDENTICAL_QUERY_BOUNDARY
verifier: NOT_ASSIGNED
consumer: NOT_ASSIGNED
consumer_ack: NOT_OBSERVED
adoption_credit: 0
fitness_credit: 0
honest_flaw: ONE_SYNTHETIC_INVALID_TOKEN_DOES_NOT_TEST_EXPIRED_OR_QUERY_MISMATCHED_TOKENS_AUTHENTICATION_PERMISSION_RATE_LIMIT_TRANSIENT_SERVER_FAILURE_HIDDEN_RETRIES_RAW_PROVIDER_PARITY_OR_CONSUMER_VALUE
valid_time_utc: 2026-08-04T19:47:23Z
recorded_time_utc: 2026-08-04T19:47:23Z
---

# X13 Gmail search-email-IDs phase 3

## Direct probe

One bounded Gmail `search_email_ids` call used the same read-only last-30-days boundary as the prior wakes, excluded Spam and Trash, capped results at one, and supplied a synthetic invalid pagination token. The connector returned a failure object with:

- `type=google_api_error`
- `code=invalidArgument`
- `status=INVALID_ARGUMENT`
- `reason=invalidArgument`
- message `Failed to search email ids`

No message identifiers, content, headers, continuation token, retry, fallback, hydration, or mutation occurred. The exact query and synthetic token were not retained in this event.

## Official contract baseline

Google documents `pageToken` on `users.messages.list` as the token used to retrieve a specific result page. A successful raw response can include `messages[]`, `nextPageToken`, and `resultSizeEstimate`. Google documents HTTP 400 as a client-side bad request and says applications should inspect returned error details and adjust invalid parameters rather than treating the response as mailbox state. Google currently assigns five quota units to `messages.list` per request.

## Measured result

The connector failed closed and preserved a useful normalized client-argument classification. It did not expose the raw HTTP status, response headers, provider request ID, raw provider error body, latency, quota receipt, upstream call count, effective identity, or OAuth scope. Unlike the prior Drive failure probe, this response did not echo the query or page-token value.

The only admitted claim is:

`CONNECTOR_REJECTED_ONE_SYNTHETIC_INVALID_PAGE_TOKEN_WITH_A_TYPED_NORMALIZED_INVALID_ARGUMENT_ERROR_AND_RETURNED_NO_MESSAGE_IDS`

Zero message IDs during this error are not evidence of absence.

## Gates

1. Use only a continuation token returned by the immediately preceding compatible search.
2. Never retry a rejected token unchanged.
3. Fail closed on every connector error; do not interpret zero IDs accompanying an error as mailbox absence.
4. Do not branch unattended operational logic solely on the connector's normalized error string.
5. Retain no query, message ID, or page token without a named consumer and retention need.
6. Require same-principal raw-provider parity, verified identity and scope, quota evidence, consumer acknowledgment, and measured operator value before operational adoption.

## Measurements

- Custom code avoided: `15-45 LOC`, estimate only and unvalidated.
- Operator minutes removed: `0` measured.
- Credentials: connector-managed; effective principal and OAuth scope unknown.
- Durability: supplied by the immutable Git event and versioned CURRENT, not by the transient connector result.
- Observability: partial; typed normalized error present, transport/provider detail absent.
- Portability: medium; Gmail query and pagination semantics remain provider-specific, while fail-closed handling is portable.
- Direct cost: no charge surfaced; actual quota debit unknown.
- Official quota reference: five units per raw `messages.list` request as of 2026-08-04.
- Verifier: not assigned.
- Consumer: not assigned; acknowledgment not observed.
- Adoption and fitness credit: zero.

## Strongest falsifier

A same-principal raw `users.messages.list` call accepts the identical invalid token, or the connector rejects an immediately preceding valid returned token under an otherwise identical query boundary.

## Honest flaw

One synthetic invalid-token probe does not test expired tokens, tokens reused with changed query parameters, authentication or permission failures, rate limits, transient server failures, hidden retries, raw-provider parity, real quota consumption, or consumer value.

## Phase disposition

`PHASE3_ACCEPTED_WITH_GATES`

Phase 4 must be decision-only with no additional Gmail candidate call. Provisional disposition: `ADOPT_WITH_GATES` for bounded human-reviewed ID discovery only, nonoperational and zero credit.
