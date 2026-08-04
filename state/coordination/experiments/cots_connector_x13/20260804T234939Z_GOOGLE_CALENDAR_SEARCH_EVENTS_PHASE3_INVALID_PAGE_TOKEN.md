---
schema_id: hfo.gen133.x13.cots_connector_event.v1
experiment_id: X13_GOOGLE_CALENDAR_SEARCH_EVENTS_READONLY_001
event_type: PHASE3_FAILURE_PERMISSION_PORTABILITY_CONNECTOR_VARIANCE
phase: 3_of_4
status: PHASE3_ACCEPTED_WITH_GATES
expected_current_version: 98
carrier_task_id: 6a55c1733708819185088bf334e33ea5
carrier_task_id_match: true
candidate: Google_Calendar_search_events_readonly_surface
wip: 1
probe: ONE_BOUNDED_SYNTHETIC_INVALID_PAGE_TOKEN
calendar_id: primary_alias
window_utc: 2026-07-05T00:00:00Z/2026-09-05T00:00:00Z
max_results: 1
query_class: SYNTHETIC_UNLIKELY_NONSECRET
query_retained_in_git: false
page_token_class: SYNTHETIC_INVALID_NONSECRET
page_token_retained_in_git: false
connector_result: TOOL_ERROR_INVALID_ARGUMENT
provider_method_inferred: calendar.events.list
http_status_observed: 400
provider_error_domain_observed: global
provider_error_reason_observed: invalid
provider_error_message_observed: Invalid_page_token_value
results_returned: 0
content_returned: 0
retries: 0
fallbacks: 0
pagination_followups: 0
hydration_calls: 0
mutations: 0
operator_minutes_removed_measured: 0
custom_code_avoided_estimate: 20_to_60_LOC_UNVALIDATED
credentials: CONNECTOR_MANAGED_IDENTITY_AND_EFFECTIVE_SCOPE_UNKNOWN
durability: PROVIDER_EXPECTED_CONNECTOR_UNVERIFIED
observability: PARTIAL_HTTP_STATUS_AND_PROVIDER_JSON_EXPOSED_NO_HEADERS_REQUEST_ID_SCOPE_QUOTA_LATENCY_OR_HIDDEN_ATTEMPTS
portability: MEDIUM_PROVIDER_PAGE_TOKEN_SEMANTICS_WITH_CONNECTOR_SPECIFIC_ERROR_WRAPPING
failure_behavior: FAIL_CLOSED_TYPED_INVALID_ARGUMENT_WITH_PROVIDER_HTTP_400_AND_RAW_JSON_DETAILS
paid_cost_usd_observed: 0_NO_CHARGE_SURFACED
actual_quota_consumed: UNKNOWN
consumer: NOT_ASSIGNED
consumer_ack: NOT_OBSERVED
verifier: NOT_ASSIGNED
independent_verification_closed: false
adoption_credit: 0
fitness_credit: 0
strongest_falsifier: SAME_PRINCIPAL_RAW_EVENTS_LIST_ACCEPTS_IDENTICAL_INVALID_TOKEN_OR_CONNECTOR_RETRIES_OR_MUTATES_BEHIND_THE_SURFACE
honest_flaw: ONE_SYNTHETIC_INVALID_TOKEN_DOES_NOT_TEST_EXPIRED_QUERY_MISMATCHED_OR_VALID_TOKENS_PERMISSION_DENIAL_RATE_LIMITS_TRANSIENT_FAILURES_HIDDEN_RETRIES_OR_RAW_PROVIDER_PARITY
valid_time_utc: 2026-08-04T23:49:39Z
recorded_time_utc: 2026-08-04T23:49:39Z
---

# X13 Google Calendar search — phase 3 invalid-page-token probe

## Measured fact

One bounded, read-only `Google_Calendar.search_events` call used the primary calendar alias, explicit RFC3339 bounds, `max_results=1`, a synthetic nonsecret unlikely query, and a synthetic invalid continuation token.

The connector failed closed with `INVALID_ARGUMENT`. The surfaced provider response was HTTP 400 with domain `global`, reason `invalid`, and message `Invalid page token value.` No events or event content were returned. No retry, fallback, follow-up pagination, hydration, or mutation occurred.

Unlike the prior Gmail failure probe, this Calendar surface exposed the provider HTTP status and raw JSON error details. It still omitted response headers, provider request ID, effective identity and OAuth scope, connector latency, quota debit, and hidden-attempt count.

## Official contract baseline

Google Calendar `events.list` defines `pageToken` as the token specifying which result page to return and returns `nextPageToken` only when another page exists. Google's Calendar error guidance classifies HTTP 400 as a permanent bad-request error caused by a missing, invalid, or incompatible parameter and says not to retry unchanged; the request must be corrected.

Google's currently published standard limits are 10,000 requests per minute per project, 600 requests per minute per user per project, and a 1,000,000-request daily project threshold before planned later-2026 billing. This connector returned no direct quota or billing receipt, so actual debit remains unknown.

## Gates added

1. Use only a continuation token returned by the immediately preceding compatible request.
2. Never retry a rejected token unchanged.
3. Fail closed on any connector error; zero events accompanying an error are not absence evidence.
4. Treat provider error bodies as potentially echoing query, token, calendar, or request details.
5. Do not drive unattended operational logic solely from connector error text until identity, scope, raw-provider parity, and hidden retry behavior are verified.
6. Keep adoption and fitness credit at zero until a named consumer acknowledges measured value.

## Measurements

- Custom code avoided: `20–60 LOC`, unvalidated estimate.
- Operator minutes removed: `0` measured.
- Credentials: connector-managed; identity and effective OAuth scope unknown.
- Durability: provider expected; connector durability unverified.
- Observability: partial; HTTP 400 and provider JSON exposed, but no headers, request ID, scope, quota, latency, or hidden-attempt count.
- Portability: medium; provider page-token semantics are common, connector error wrapping is not portable.
- Failure behavior: fail-closed permanent client error; no automatic retry observed.
- Direct cost: `$0` surfaced; actual quota debit unknown.
- Verifier: unassigned.
- Consumer: unassigned.

## Strongest falsifier

A same-principal raw Calendar `events.list` request accepts the identical invalid token, or evidence shows the connector retried, widened, changed, or mutated the request behind the exposed surface.

## Honest flaw

This one synthetic invalid-token probe does not test expired tokens, tokens bound to another query or window, valid pagination, permission denial, authentication expiry, rate limiting, transient backend errors, private-event redaction, hidden retries, or exact raw-provider parity.

## Phase-4 input

Provisional disposition remains `ADOPT_WITH_GATES` for bounded, read-only, human-reviewed event discovery only. Phase 4 must make no additional Calendar candidate call.
