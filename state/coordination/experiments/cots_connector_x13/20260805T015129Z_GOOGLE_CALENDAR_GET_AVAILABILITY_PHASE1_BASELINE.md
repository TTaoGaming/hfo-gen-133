---
schema_id: hfo.gen133.x13.cots_connector_event.v1
experiment_id: X13_GOOGLE_CALENDAR_GET_AVAILABILITY_READONLY_001
candidate: Google_Calendar_get_availability_readonly_surface
phase: 1
phase_name: OFFICIAL_CONTRACT_AND_DIRECT_CAPABILITY_BASELINE
phase_status: PHASE1_ACCEPTED_WITH_GATES
carrier_task_id: 6a55c1733708819185088bf334e33ea5
carrier_task_id_match: true
wip: 1
prior_current_version: 100
expected_current_version: 101
branch: agent/gen133-bootstrap-20260730
operation: ONE_BOUNDED_PRIMARY_CALENDAR_FREEBUSY_QUERY
mutation: false
calendar_count_requested: 1
calendar_identifier_class: PRIMARY_ALIAS
query_window_minutes: 120
response_timezone: America/Denver
calendar_results_returned: 1
busy_blocks_returned: 1
aggregate_busy_minutes_observed: 120
exact_busy_intervals_retained: false
event_titles_or_details_returned: false
per_calendar_errors: 0
connector_error: NONE
connector_latency_ms: 162
retry_count: 0
fallback_count: 0
hidden_attempt_count: UNKNOWN
operator_minutes_removed_measured: 0
custom_code_avoided_estimate: 30_to_80_LOC_UNVALIDATED
credentials: CONNECTOR_MANAGED_IDENTITY_AND_EFFECTIVE_SCOPE_UNKNOWN
durability: PROVIDER_QUERY_EPHEMERAL_IMMUTABLE_GIT_EVENT_AND_VERSIONED_CURRENT
observability: PARTIAL_BUSY_COUNT_AGGREGATE_DURATION_PER_CALENDAR_ERROR_FIELD_AND_CONNECTOR_LATENCY_EXPOSED_NO_HTTP_STATUS_HEADERS_REQUEST_ID_PRINCIPAL_SCOPE_QUOTA_OR_HIDDEN_ATTEMPT_COUNT
portability: MEDIUM_FREEBUSY_IS_COMMON_BUT_CALENDAR_IDS_RFC3339_AND_PROVIDER_ERROR_SHAPE_ARE_PROVIDER_SPECIFIC
failure_behavior: NOT_PROBED_PHASE1_SUCCESS_PATH_ONLY
paid_cost_usd_observed: 0_NO_CHARGE_SURFACED
actual_quota_consumed: UNKNOWN
official_contract: GOOGLE_CALENDAR_FREEBUSY_QUERY_RETURNS_BUSY_WINDOWS_ONLY_WITH_INCLUSIVE_START_EXCLUSIVE_END_AND_PER_CALENDAR_ERRORS_SUPPORTS_UP_TO_50_CALENDARS_AND_GROUP_EXPANSION_UP_TO_100
official_quota_contract: 10000_REQUESTS_PER_MINUTE_PER_PROJECT_600_PER_MINUTE_PER_USER_PER_PROJECT_1000000_PER_DAY_PROJECT_BILLING_THRESHOLD_AS_OF_2026_08_05
consumer: NOT_ASSIGNED
consumer_ack: NOT_OBSERVED
verifier: NOT_ASSIGNED
verifier_result: NOT_RUN
independent_verification_closed: false
adoption_credit: 0
fitness_credit: 0
strongest_falsifier: SAME_PRINCIPAL_RAW_FREEBUSY_QUERY_MATERIALLY_DISAGREES_ON_BUSY_WINDOWS_OR_CONNECTOR_RETURNS_EVENT_TITLES_DETAILS_OR_SILENTLY_OMITS_PER_CALENDAR_ERRORS
honest_flaw: ONE_PRIMARY_CALENDAR_WINDOW_THAT_WAS_FULLY_BUSY_DOES_NOT_VERIFY_FREE_WINDOWS_MULTIPLE_CALENDARS_INACCESSIBLE_CALENDAR_ERRORS_EFFECTIVE_IDENTITY_OR_SCOPE_RAW_PROVIDER_PARITY_TIMEZONE_OR_DST_EDGES_RATE_LIMITS_TRANSIENT_FAILURES_HIDDEN_RETRIES_ACTUAL_QUOTA_CONSUMPTION_OPERATOR_TIME_SAVED_OR_CONSUMER_VALUE
next_phase: PHASE2_SMALLEST_HARMLESS_READONLY_MICRO_USE
next_probe: ONE_BOUNDED_PRIMARY_CALENDAR_FREEBUSY_QUERY_OVER_A_DIFFERENT_SHORT_WINDOW_WITH_NO_EXACT_BUSY_INTERVAL_RETENTION_OR_MUTATION
valid_time_utc: 2026-08-05T01:51:29Z
recorded_time_utc: 2026-08-05T01:51:29Z
---

# X13 Google Calendar `get_availability` phase 1 baseline

## Direct measurement

One read-only connector call queried the `primary` calendar across an explicit 120-minute RFC3339 interval. The connector returned one calendar result, one busy block covering the full interval, no event titles or descriptions, no per-calendar error, and no connector-level error. Exact busy timestamps were not retained in this event; only the aggregate count and duration were recorded.

Connector latency was 162 ms. No retry, fallback, secondary read, write, send, spend, account action, or production deployment occurred.

## Official capability baseline

Google Calendar `freeBusy.query` accepts RFC3339 `timeMin` and `timeMax`, a response time zone, and calendar or group identifiers. A successful raw response contains per-calendar busy ranges and optional per-calendar errors rather than event titles or details. Busy starts are inclusive and busy ends are exclusive. The documented expansion limits are 50 calendars and 100 members for a group.

The connector surface is narrower than the raw contract: it accepts explicit calendar IDs and returns busy windows and per-calendar errors, but does not expose raw response kind, top-level bounds, group expansion controls, HTTP metadata, request IDs, authenticated principal, effective OAuth scope, quota debit, or hidden attempt count.

## Measurement ledger

| Measure | Result |
|---|---|
| Custom code avoided | 30-80 LOC estimated, unvalidated |
| Operator minutes removed | 0 measured |
| Credentials | Connector-managed; identity and effective scope unknown |
| Durability | Provider query ephemeral; Git event immutable |
| Observability | Busy count, aggregate duration, per-calendar error field, latency |
| Portability | Medium |
| Failure behavior | Not probed in phase 1 |
| Direct surfaced cost | $0 |
| Actual quota debit | Unknown |
| Verifier | Not assigned |
| Consumer | Not assigned |

## Gates

- Use explicit RFC3339 bounds and the smallest calendar set needed.
- Treat busy windows as sensitive schedule data even though titles and details are absent.
- Persist only aggregate measurements unless a named consumer requires exact windows.
- Do not infer identity, OAuth scope, access level, raw-provider parity, completeness, quota debit, or hidden retries from this success.
- Require same-principal raw verification, an inaccessible-calendar error witness, quota evidence, consumer acknowledgment, and measured value before unattended scheduling decisions.

## Honest flaw

This easiest positive path used only the primary calendar and happened to return a fully busy interval. It does not test a free interval, multiple calendars, inaccessible calendars, per-calendar errors, timezone or DST edges, permissions, rate limiting, transient failures, hidden retries, actual quota consumption, or downstream value.
