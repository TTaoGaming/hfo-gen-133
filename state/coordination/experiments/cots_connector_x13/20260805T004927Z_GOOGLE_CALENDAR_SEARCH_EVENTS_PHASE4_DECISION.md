---
schema_id: hfo.gen133.x13.cots_connector_event.v1
experiment_id: X13_GOOGLE_CALENDAR_SEARCH_EVENTS_READONLY_001
event_type: PHASE4_ADOPTION_DECISION
phase: 4_of_4
status: ADOPT_WITH_GATES
candidate: Google_Calendar_search_events_readonly_surface
carrier_task_id: 6a55c1733708819185088bf334e33ea5
carrier_task_id_match: true
wip: 1
repository: TTaoGaming/hfo-gen-133
branch: agent/gen133-bootstrap-20260730
prior_current_version: 99
expected_current_version: 100
phase4_candidate_calls: 0
campaign_calls: 3
campaign_successes: 2
campaign_failures: 1
campaign_positive_results: 1
campaign_empty_results: 1
campaign_invalid_argument_results: 1
retries: 0
fallbacks: 0
pagination_followups: 0
hydration_calls: 0
mutations: 0
content_bearing_surface: true
phase1_events_returned: 1
phase1_continuation_token_returned: true
phase2_events_returned: 0
phase2_continuation_token_returned: false
phase3_events_returned: 0
phase3_provider_http_status: 400
phase3_connector_error: INVALID_ARGUMENT
adoption_decision: ADOPT_WITH_GATES
adoption_mode: MANUAL_BOUNDED_EVENT_DISCOVERY_ONLY_NONOPERATIONAL
allowed_use: HUMAN_REVIEWED_READONLY_PRIMARY_OR_EXPLICIT_CALENDAR_EVENT_DISCOVERY_WITH_EXPLICIT_RFC3339_BOUNDS_MINIMAL_RESULT_CAP_AND_EPHEMERAL_CONTENT_HANDLING
prohibited_use: UNATTENDED_CONTROL_AUTHORITATIVE_ABSENCE_COMPLETENESS_OR_ORDERING_CLAIMS_PRIVATE_CONTENT_PERSISTENCE_UNBOUNDED_SEARCH_OR_TOKEN_REUSE_OUTSIDE_THE_IMMEDIATELY_PRECEDING_COMPATIBLE_REQUEST
custom_code_avoided_estimate: 20_to_60_LOC_UNVALIDATED
operator_minutes_removed_measured: 0
credentials: CONNECTOR_MANAGED_IDENTITY_AND_EFFECTIVE_SCOPE_UNKNOWN
durability: PROVIDER_DURABILITY_EXPECTED_CONNECTOR_DURABILITY_UNVERIFIED_IMMUTABLE_GIT_DECISION_PERSISTED
observability: PARTIAL_RESULT_SHAPE_LATENCY_HTTP_STATUS_AND_PROVIDER_JSON_EXPOSED_NO_HEADERS_REQUEST_ID_PRINCIPAL_SCOPE_QUOTA_OR_HIDDEN_ATTEMPT_COUNT
portability: MEDIUM_PROVIDER_SPECIFIC_EVENT_QUERY_WINDOW_AND_PAGE_TOKEN_SEMANTICS_WITH_PORTABLE_BOUNDED_FAIL_CLOSED_GATES
failure_behavior: SYNTHETIC_INVALID_PAGE_TOKEN_FAILED_CLOSED_WITH_HTTP_400_INVALID_ARGUMENT_AND_NO_EVENT_CONTENT
paid_cost_usd_observed: 0_NO_CHARGE_SURFACED
actual_quota_consumed: UNKNOWN
official_quota_contract: 10000_REQUESTS_PER_MINUTE_PER_PROJECT_600_PER_MINUTE_PER_USER_PER_PROJECT_1000000_PER_DAY_PROJECT_BILLING_THRESHOLD_AS_OF_2026_08_05
mandatory_gates: CONTENT_BEARING_RESULTS_EXPLICIT_RFC3339_BOUNDS_MINIMAL_RESULT_CAP_HUMAN_REVIEW_EMPTY_RESULTS_NONAUTHORITATIVE_ZERO_EVENTS_DURING_ERROR_NONAUTHORITATIVE_USE_ONLY_IMMEDIATELY_PRECEDING_COMPATIBLE_RETURNED_TOKEN_NO_UNCHANGED_RETRY_NO_EVENT_VALUE_QUERY_URL_OR_TOKEN_RETENTION_WITHOUT_NAMED_NEED_RAW_SCOPE_VALID_PAGINATION_QUOTA_CONSUMER_AND_FAILURE_WITNESS_REQUIRED_BEFORE_UNATTENDED_USE
strongest_falsifier: SAME_PRINCIPAL_RAW_EVENTS_LIST_MATERIALLY_DISAGREES_WITH_CONNECTOR_RESULT_OR_ACCEPTS_THE_IDENTICAL_INVALID_TOKEN_OR_CONNECTOR_REJECTS_AN_IMMEDIATELY_PRECEDING_VALID_RETURNED_TOKEN_UNDER_IDENTICAL_BOUNDS_QUERY_CALENDAR_AND_PAGE_SIZE
verifier: S03_REDUCER_AND_S04_STRUCTURAL_PREFLIGHT
verifier_result: REVISE_NONBINDING_WEIGHT_ZERO
verifier_receipt_s03: state/coordination/receipts/chatgpt_runtime/seat-03/20260805T000801Z_X13_GOOGLE_CALENDAR_SEARCH_EVENTS_PHASE3_RETURN_BINDINGS_REVISE.yaml
verifier_receipt_s04: state/coordination/receipts/chatgpt_runtime/seat-04/20260805T001454Z_X13_GOOGLE_CALENDAR_SEARCH_PHASE3_STRUCTURAL_REVISE.yaml
independent_verification_closed: false
consumer: NOT_ASSIGNED
consumer_ack: NOT_OBSERVED
adoption_credit: 0
fitness_credit: 0
honest_flaw: ONE_POSITIVE_ONE_SYNTHETIC_EMPTY_AND_ONE_SYNTHETIC_INVALID_TOKEN_CALL_DO_NOT_VERIFY_IDENTITY_SCOPE_QUERY_TRANSLATION_ORDERING_COMPLETENESS_VALID_PAGINATION_RECURRING_EVENT_EXPANSION_PRIVATE_EVENT_REDACTION_SECONDARY_CALENDAR_COVERAGE_AUTH_PERMISSION_RATE_LIMIT_TRANSIENT_FAILURE_HIDDEN_CALLS_RAW_PROVIDER_PARITY_ACTUAL_QUOTA_CONSUMPTION_OPERATOR_TIME_SAVED_OR_CONSUMER_VALUE
next_campaign_candidate: Google_Calendar_get_availability_readonly_surface
next_campaign_phase: PHASE1_OFFICIAL_CONTRACT_AND_DIRECT_CAPABILITY_BASELINE
valid_time_utc: 2026-08-05T00:49:27Z
recorded_time_utc: 2026-08-05T00:49:27Z
---

# X13 Google Calendar search-events phase 4 decision

## Decision

`ADOPT_WITH_GATES`

Adopt the Google Calendar `search_events` connector only as a bounded, read-only, human-reviewed event-discovery surface. This is a catalog/manual-use decision, not operational approval. No additional Calendar candidate call was made in phase 4.

## Evidence considered

Across three bounded calls, the connector produced one content-bearing event result with a continuation token, one normal empty event array with no continuation token, and one fail-closed `INVALID_ARGUMENT` response for a synthetic invalid page token. The failure exposed provider HTTP 400 JSON detail. No retry, fallback, pagination follow-up, hydration, or mutation occurred.

The campaign establishes that the connector can perform a narrow Calendar search inside explicit RFC3339 bounds, return event content without a separate hydration call, normalize an easy empty-result path, and fail closed on one invalid-token probe. It does not establish authoritative absence, complete calendar coverage, exact query translation, stable ordering, recurring-event semantics, private-event redaction, effective identity or OAuth scope, valid pagination, raw-provider parity, hidden-call behavior, actual quota use, or consumer value.

## Official contract checked

Google's `events.list` contract supports calendar IDs, `timeMin`, `timeMax`, free-text `q`, `maxResults`, and `pageToken`. Google states that `maxResults` does not guarantee a full page and that a non-empty `nextPageToken` requires the exact same request plus that returned token. Read-only scopes include `calendar.events.readonly` and `calendar.readonly`.

Current official Calendar API limits are 10,000 requests per minute per project and 600 per minute per user per project. Google publishes a 1,000,000-request daily project threshold before planned later-2026 billing and states that standard use currently has no additional cost. The connector exposed no direct quota or billing receipt.

Official references checked 2026-08-05:
- https://developers.google.com/workspace/calendar/api/v3/reference/events/list
- https://developers.google.com/workspace/calendar/api/guides/pagination
- https://developers.google.com/workspace/calendar/api/guides/quota
- https://developers.google.com/identity/protocols/oauth2/scopes

## Adopted boundary

Allowed:

1. Explicitly bounded, read-only searches using a named calendar or `primary`, full RFC3339 time bounds, and a minimal result cap.
2. Human review before downstream interpretation or follow-up.
3. Ephemeral handling of returned event values and continuation tokens unless a named retention need exists.
4. Treating every result as potentially sensitive calendar content.

Not allowed:

1. Unattended control-plane decisions or automatic downstream writes.
2. Treating empty results or zero events during errors as proof of absence.
3. Completeness, ordering, identity, permission, private-redaction, or quota claims without an independent same-principal witness.
4. Retaining event text, identifiers, URLs, queries, or tokens without a named consumer and retention requirement.
5. Retrying a rejected page token unchanged or reusing a token outside the immediately preceding compatible request.

## Measurements

- Custom code avoided: `20-60 LOC`, estimate only and unvalidated.
- Operator minutes removed: `0` measured.
- Credentials: connector-managed; effective principal and OAuth scope unknown.
- Durability: provider durability expected but connector durability unverified; immutable Git event and CURRENT pointer provide local audit durability.
- Observability: partial; result shape, success latency, HTTP status, and provider JSON error detail were observed, but headers, provider request ID, identity, scope, quota debit, and hidden attempts were not.
- Portability: medium; Calendar query, time-window, event, and pagination semantics are provider-specific, while bounded fail-closed gates are portable.
- Failure behavior: one synthetic invalid page token failed closed with HTTP 400 `INVALID_ARGUMENT` and no event content.
- Direct cost: no charge surfaced; actual quota debit unknown.
- Verifier: S03 reducer and S04 structural preflight both returned `REVISE`, same-provider and nonbinding with weight zero. Exact Git bytes were structurally bound, but the provider request, identity, scope, raw parity, and consumer value remain unverified.
- Consumer: not assigned; acknowledgment not observed.
- Adoption and fitness credit: zero.

## Strongest falsifier

A same-principal raw `events.list` witness materially disagrees with the connector result, accepts the identical invalid token, or the connector rejects an immediately preceding valid returned token under identical calendar, bounds, query, and page-size parameters.

## Honest flaw

The decision rests on only one easy positive call, one deliberately empty query, and one synthetic invalid-token failure. Identity, scope, query translation, ordering, completeness, valid pagination, recurring-event expansion, private-event redaction, secondary-calendar coverage, authentication and permission failures, rate limits, transient failures, hidden retries, raw-provider parity, actual quota consumption, operator time saved, and consumer value remain unverified.

## Next campaign

Queue phase 1 for the bounded, read-only Google Calendar `get_availability` surface. No availability call is made in this event.
