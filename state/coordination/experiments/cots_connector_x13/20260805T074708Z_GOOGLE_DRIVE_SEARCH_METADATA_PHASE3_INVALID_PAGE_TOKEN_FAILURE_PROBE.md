---
schema_id: hfo.gen133.x13.cots_connector_event.v1
event_id: X13_GOOGLE_DRIVE_SEARCH_METADATA_PHASE3_INVALID_PAGE_TOKEN_FAILURE_PROBE_20260805T074708Z
experiment_id: X13_GOOGLE_DRIVE_SEARCH_READONLY_002
candidate: Google_Drive_search_metadata_only_document_surface
phase: 3
phase_name: FAILURE_PERMISSION_PORTABILITY_AND_CONNECTOR_VARIANCE_PROBE
phase_status: PHASE3_ACCEPTED_WITH_GATES
current_version_expected: 106
current_version_next: 107
carrier_task_id: 6a55c1733708819185088bf334e33ea5
carrier_task_id_match: true
wip: 1
call_count_this_event: 1
call_mode: READONLY_METADATA_ONLY
query_class: SHORT_NONSECRET_PROJECT_ACRONYM
query: HFO
item_type: document
topn: 1
best_effort_fetch: false
require_viewed_by_user: false
page_token_class: SYNTHETIC_INVALID_NONSECRET
exact_page_token_persisted: false
connector_result: ERROR
connector_error_class: INVALID_ARGUMENT
provider_http_status: 400
provider_error_domain: global
provider_error_reason: invalid
provider_error_location: pageToken
provider_error_location_type: parameter
provider_error_message: Invalid_Value
results_returned: 0
content_hydrated: false
caller_retries: 0
caller_fallbacks: 0
secondary_reads: 0
mutations: 0
connector_latency_ms: NOT_EXPOSED
hidden_attempt_count: UNKNOWN
raw_error_body_surfaced: true
request_url_surfaced: true
request_url_echoed_query: true
request_url_echoed_page_token: true
http_headers_surfaced: false
request_id_surfaced: false
identity_surfaced: false
effective_scope_surfaced: false
quota_debit_surfaced: false
paid_cost_usd_observed: 0_NO_CHARGE_SURFACED
actual_quota_consumed: UNKNOWN_FILES_LIST_IS_DOCUMENTED_AS_100_QUOTA_UNITS_BUT_CONNECTOR_FANOUT_HIDDEN_CALLS_AND_PROJECT_QUOTA_CLASS_ARE_UNEXPOSED
measured_fact: SYNTHETIC_INVALID_PAGE_TOKEN_FAILED_CLOSED_AS_HTTP_400_INVALID_ARGUMENT_AND_THE_CONNECTOR_ERROR_SURFACE_ECHOED_THE_QUERY_AND_PAGE_TOKEN_IN_A_PROVIDER_REQUEST_URL
admitted_claim: ONE_BOUNDED_METADATA_SEARCH_WITH_A_SYNTHETIC_INVALID_PAGE_TOKEN_FAILED_CLOSED_WITH_PROVIDER_400_INVALID_AND_RETURNED_NO_RESULTS
custom_code_avoided_estimate: 40_to_120_LOC_UNVALIDATED
operator_minutes_removed_measured: 0
operator_minutes_removed_estimate: NOT_CLAIMED
credentials: CONNECTOR_MANAGED_AUTHENTICATION_OBSERVED_LIVE_IDENTITY_SCOPE_TOKEN_TYPE_AND_CREDENTIAL_CUSTODY_UNKNOWN
durability: PROVIDER_STORED_METADATA_AND_STABLE_ITEM_ID_ONLY_NO_WORKFLOW_REPLAY_RESUME_TRANSACTION_OR_EXACTLY_ONCE_SEMANTICS
observability: PROVIDER_HTTP_STATUS_JSON_ERROR_DOMAIN_REASON_LOCATION_MESSAGE_AND_FULL_REQUEST_URL_SURFACED_BUT_NO_HEADERS_REQUEST_ID_IDENTITY_SCOPE_QUOTA_DEBIT_LATENCY_OR_HIDDEN_ATTEMPT_GRAPH
portability: MEDIUM_HTTP_400_AND_INVALID_PAGE_TOKEN_ARE_COMMON_BUT_ERROR_SCHEMA_REQUEST_URL_ECHO_QUERY_TRANSLATION_MIME_FILTERS_CORPUS_AND_TOKEN_FORMAT_ARE_PROVIDER_AND_CONNECTOR_SPECIFIC
failure_behavior: FAIL_CLOSED_ON_INVALID_TOKEN_NO_RESULTS_RETURNED_NO_CALLER_RETRY_OR_FALLBACK_OBSERVED_ERROR_MUST_NOT_BE_INTERPRETED_AS_ABSENCE
connector_variance: WRAPPER_EXPOSED_A_TRANSFORMED_INVALID_ARGUMENT_ERROR_WITH_PROVIDER_HTTP_STATUS_RAW_JSON_AND_FULL_REQUEST_URL_INCLUDING_QUERY_AND_PAGE_TOKEN_WHILE_OMITTING_HEADERS_REQUEST_ID_PRINCIPAL_SCOPE_QUOTA_AND_LATENCY
official_contract: FILES_LIST_REQUIRES_PAGE_TOKEN_TO_BE_THE_NEXT_PAGE_TOKEN_FROM_THE_PREVIOUS_RESPONSE_AND_DOCUMENTS_THAT_REJECTED_TOKENS_SHOULD_BE_DISCARDED_AND_PAGINATION_RESTARTED_FROM_THE_FIRST_PAGE
official_contract_url: https://developers.google.com/workspace/drive/api/reference/rest/v3/files/list
official_error_contract: HTTP_400_MEANS_CLIENT_REQUEST_ERROR_AND_INVALID_PARAMETER_VALUES_MUST_BE_CORRECTED_RATHER_THAN_RETRIED_UNCHANGED
official_error_url: https://developers.google.com/workspace/drive/api/guides/handle-errors
official_quota_contract: POST_2026_05_01_MODEL_1000000_UNITS_PER_MINUTE_PER_PROJECT_325000_PER_MINUTE_PER_USER_PER_PROJECT_400000000_DAILY_BILLING_THRESHOLD_FILES_LIST_100_UNITS_WITH_GRANDFATHERING_POSSIBLE
official_quota_url: https://developers.google.com/workspace/drive/api/guides/limits
consumer: HFO_COTS_CAPABILITY_INVENTORY_CATALOG_ONLY
operational_consumer: NOT_ASSIGNED
consumer_ack: NOT_OBSERVED
verifier: DISTINCT_AUTHORIZED_SAME_PRINCIPAL_RAW_DRIVE_FILES_LIST_WITNESS_REQUIRED_NOT_ASSIGNED
verifier_result: NOT_RUN
independent_verification_closed: false
adoption_credit: 0
fitness_credit: 0
allowed_use: BOUNDED_READONLY_HUMAN_REVIEWED_METADATA_DISCOVERY_WITH_ERRORS_FAILING_CLOSED
mandatory_gate: USE_ONLY_NEXT_PAGE_TOKEN_FROM_IMMEDIATELY_PRECEDING_COMPATIBLE_REQUEST_NEVER_RETRY_A_REJECTED_TOKEN_UNCHANGED_FAIL_CLOSED_ON_ERROR_NEVER_TREAT_ZERO_RESULTS_DURING_ERROR_AS_ABSENCE_SANITIZE_QUERY_AND_PAGE_TOKEN_FROM_LOGS_NO_UNATTENDED_USE_WITHOUT_IDENTITY_SCOPE_RAW_PARITY_VALID_PAGINATION_QUOTA_CONSUMER_AND_VALUE_EVIDENCE
strongest_falsifier: SAME_PRINCIPAL_RAW_FILES_LIST_ACCEPTS_THE_IDENTICAL_INVALID_TOKEN_OR_CONNECTOR_SILENTLY_RESTARTS_PAGINATION_RETURNS_RESULTS_OR_HIDES_MULTIPLE_RETRIES_FOR_THE_SAME_INPUT
honest_flaw: ONE_SYNTHETIC_INVALID_TOKEN_ONLY_TESTED_A_PERMANENT_CLIENT_ERROR_IT_DID_NOT_TEST_A_VALID_EXPIRED_OR_QUERY_MISMATCHED_TOKEN_PERMISSION_DENIAL_AUTHENTICATION_RATE_LIMIT_TRANSIENT_FAILURE_HIDDEN_RETRY_RAW_PARITY_ACTUAL_QUOTA_OPERATOR_TIME_SAVED_OR_CONSUMER_VALUE_AND_CONNECTOR_LATENCY_WAS_NOT_EXPOSED
next_phase: PHASE4_DECISION_ONLY_NO_ADDITIONAL_DRIVE_CALL
provisional_decision: ADOPT_WITH_GATES
review_expiry_utc: 2026-08-12T07:47:08Z
valid_time_utc: 2026-08-05T07:47:08Z
recorded_time_utc: 2026-08-05T07:47:08Z
---

# X13 Google Drive metadata search — Phase 3 invalid page-token probe

## Direct receipt

One bounded metadata-only `Google_Drive.search` call used `query=HFO`, `item_type=document`, `topn=1`, `best_effort_fetch=false`, and one synthetic invalid page token. The connector failed closed with `INVALID_ARGUMENT`, provider HTTP `400`, `domain=global`, `reason=invalid`, `location=pageToken`, and message `Invalid Value`. No result metadata or file content was returned. The caller performed no retry, fallback, secondary read, or mutation.

## Measured connector variance

The connector surfaced the provider status, structured JSON error, and the full provider request URL. That URL echoed both the search query and page token. This improves debugging but creates a logging and secret-handling hazard: real queries and opaque continuation tokens can leak into traces, Git events, Slack, or exception aggregators unless sanitized.

The connector did not expose response headers, request ID, authenticated identity, effective OAuth scope, latency, quota debit, or hidden-attempt count.

## Official contract baseline

Google documents `pageToken` as the `nextPageToken` returned by the previous compatible `files.list` response. If a token is rejected, it should be discarded and pagination restarted from the first page. Google classifies HTTP 400 as a client request error; invalid parameter values must be corrected rather than retried unchanged.

As of May 1, 2026, Google documents 1,000,000 quota units per minute per project, 325,000 per minute per user per project, and a 400,000,000-unit daily billing threshold for newly governed projects, with grandfathering possible. `files.list` is documented as 100 quota units. This connector call exposed no direct quota receipt.

## Gates added

1. Use only a `nextPageToken` from the immediately preceding compatible request.
2. Never retry a rejected page token unchanged.
3. Fail closed on connector errors; zero results accompanying an error are not absence.
4. Sanitize query strings and page tokens from logs and durable receipts.
5. Keep unattended use disabled until identity, effective scope, valid pagination, raw-provider parity, quota evidence, consumer acknowledgment, and measured value are verified.

## Honest flaw

This was one synthetic permanent client-error probe. It did not test valid, expired, or query-mismatched tokens; authentication or permission denial; rate limiting; transient failures; hidden retries; raw-provider parity; actual quota use; operator time saved; or consumer value. Connector latency was not exposed.

## Next

Phase 4 decision only. No additional Drive call is authorized for the next wake.
