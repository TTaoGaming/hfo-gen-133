---
schema_id: hfo.gen133.x13.cots_connector_event.v1
experiment_id: X13_GOOGLE_DRIVE_SEARCH_METADATA_READONLY_001
event_type: PHASE3_FAILURE_PERMISSION_PORTABILITY_VARIANCE_PROBE
phase: 3_of_4
phase_status: PHASE3_ACCEPTED_WITH_GATES
candidate: Google_Drive_search_metadata_only_surface
carrier_task_id: 6a55c1733708819185088bf334e33ea5
carrier_task_id_match: true
wip: 1
repository: TTaoGaming/hfo-gen-133
branch: agent/gen133-bootstrap-20260730
prior_current_version_expected: 90
probe_mutability: READ_ONLY
probe_scope: ONE_DOCUMENT_CATEGORY_SEARCH_TOPN_1_WITH_SYNTHETIC_INVALID_PAGE_TOKEN
query_retention: EXACT_QUERY_AND_TOKEN_NOT_RECORDED
provider_method_observed: GET_GOOGLE_DRIVE_V3_FILES_LIST
connector_result: INVALID_ARGUMENT
provider_http_status_observed: 400
provider_error_reason_observed: invalid
provider_error_location_observed: pageToken
provider_error_message_observed: Invalid_Value
results_returned: 0
file_content_returned: 0
connector_failed_closed: true
retry_attempted: false
fallback_attempted: false
mutation_attempted: false
paid_cost_usd_observed: 0_NO_CHARGE_SURFACED
actual_quota_consumed: UNKNOWN
official_method_quota_contract: FILES_LIST_100_QUOTA_UNITS_PER_REQUEST_AS_OF_2026_08_04
operator_minutes_removed_measured: 0
custom_code_avoided_estimate: 25_to_70_LOC_UNVALIDATED
credentials: CONNECTOR_MANAGED_IDENTITY_AND_EFFECTIVE_SCOPE_UNKNOWN
durability: IMMUTABLE_GIT_EVENT_PLUS_VERSIONED_CURRENT
observability: PARTIAL_PROVIDER_400_REASON_LOCATION_AND_REQUEST_URL_EXPOSED_NO_HEADERS_REQUEST_ID_OR_QUOTA_COUNTER
portability: LOW_TO_MEDIUM_DRIVE_V3_AND_CONNECTOR_ERROR_SHAPE_SPECIFIC
failure_behavior: FAIL_CLOSED_TYPED_INVALID_ARGUMENT_WITH_PROVIDER_400_DETAILS
strongest_falsifier: CONNECTOR_ACCEPTS_OR_SILENTLY_RESTARTS_FROM_A_SYNTHETIC_INVALID_TOKEN
verifier: SAME_PRINCIPAL_RAW_DRIVE_FILES_LIST_OR_FUTURE_PROVIDER_ISSUED_CURSOR_PROBE
consumer: NONE_NAMED
consumer_ack: NOT_OBSERVED
adoption_credit: 0
fitness_credit: 0
honest_flaw: ONE_SYNTHETIC_INVALID_TOKEN_DOES_NOT_TEST_EXPIRED_MISMATCHED_PERMISSION_RATE_LIMIT_OR_SHARED_DRIVE_FAILURES
next_phase: PHASE4_DECISION_WITH_NO_ADDITIONAL_CANDIDATE_CALL
valid_time_utc: 2026-08-04T15:49:07Z
recorded_time_utc: 2026-08-04T15:49:07Z
---

# X13 Google Drive metadata search — phase 3 invalid page-token probe

## Direct observation

A single bounded read-only `Google_Drive.search` call used `item_type=document`, `topn=1`, no content hydration, and a synthetic nonsecret invalid page token. The connector returned `INVALID_ARGUMENT` and exposed a Google Drive v3 `files.list` HTTP `400 Bad Request` payload with reason `invalid`, location `pageToken`, and message `Invalid Value`. It returned no results or file content. No retry, fallback, or mutation was attempted.

The connector failed closed and preserved useful provider diagnostics. It also exposed the full generated request URL in the tool error, including the exact query and page-token values. Therefore query strings, raw filters, and cursor values must be treated as potentially echoed telemetry and must not carry secrets or unnecessarily sensitive terms.

## Official contract baseline

Google documents `pageToken` as an opaque continuation value that must come from the prior response's `nextPageToken`. If a token is rejected, clients should discard it and restart pagination from the first page rather than repeatedly retrying the rejected token:

- https://developers.google.com/workspace/drive/api/reference/rest/v3/files/list

Google's current usage-limits documentation assigns 100 quota units to list operations such as `files.list`, while standard API use remains no-additional-cost below applicable limits. The connector exposed no quota debit, billing record, response headers, or request identifier, so actual consumption for this failed request is unknown:

- https://developers.google.com/workspace/drive/api/guides/limits

## Adopt-before-invent measurements

| Measure | Observation |
|---|---|
| Custom code avoided | 25–70 LOC estimated, unvalidated |
| Operator minutes removed | 0 measured |
| Credentials | Connector-managed; identity and effective scopes unknown |
| Durability | This immutable Git event plus versioned CURRENT |
| Observability | Provider method, HTTP 400, reason, location, message, and generated request URL exposed; no headers, request ID, quota counter, or hidden-attempt count |
| Portability | Low-to-medium; Drive v3 and connector error shape are provider-specific |
| Failure behavior | Fail closed with typed connector error and provider details |
| Direct cost/quota evidence | $0 charge surfaced; actual quota debit unknown; official `files.list` contract is 100 units/request |
| Strongest falsifier | The connector accepts a synthetic invalid token or silently restarts pagination while presenting results as continuation data |
| Verifier | Same-principal raw Drive API witness, or a later provider-issued cursor probe |
| Consumer | None named; no acknowledgment |
| Honest flaw | One synthetic invalid token does not test expired tokens, tokens from another query/corpus, permission denial, rate limiting, shared-drive variance, or transient failures |

## Gates added

1. Use only the opaque `next_page_token` returned by the immediately preceding compatible request.
2. On a rejected token, discard it and restart from the first page only when the consumer explicitly permits a fresh non-snapshot search; do not retry the same token unchanged.
3. Fail closed and never interpret zero returned files during an error as absence.
4. Assume errors may echo exact queries, filters, URLs, and tokens; never place secrets in these fields and minimize sensitive search terms.
5. Do not branch unattended operational logic solely on connector error strings until raw-provider parity and a typed stable schema are verified.
6. Keep operational and fitness credit at zero until a named consumer measures value.

## Phase status

`PHASE3_ACCEPTED_WITH_GATES`

Provisional phase-4 disposition: `ADOPT_WITH_GATES`, restricted to bounded, human-reviewed metadata discovery. No additional candidate call is required for phase 4.
