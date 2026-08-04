---
schema_id: hfo.gen133.x13.cots_connector_event.v1
experiment_id: X13_GOOGLE_CALENDAR_SEARCH_EVENTS_READONLY_001
event_type: PHASE1_DIRECT_CAPABILITY_BASELINE
phase: 1_of_4
phase_status: PHASE1_ACCEPTED_WITH_GATES
candidate: Google_Calendar_search_events_readonly_surface
carrier_task_id: 6a55c1733708819185088bf334e33ea5
carrier_task_id_match: true
wip: 1
repository: TTaoGaming/hfo-gen-133
branch: agent/gen133-bootstrap-20260730
call_count_this_event: 1
mutation_count: 0
retry_count: 0
fallback_count: 0
pagination_followup_count: 0
hydration_count: 0
calendar_id_class: PRIMARY_ALIAS
query: OMITTED
window_time_min_utc: 2026-07-05T00:00:00Z
window_time_max_utc: 2026-09-05T00:00:00Z
response_timezone_requested: America/Denver
max_results: 1
events_returned: 1
next_page_token_returned: true
connector_external_call_time_ms: 909
private_event_values_persisted: false
paid_cost_usd_observed: 0_NO_CHARGE_SURFACED
actual_quota_consumed: UNKNOWN
operator_minutes_removed_measured: 0
custom_code_avoided_estimate: 20_to_60_LOC_UNVALIDATED
credentials: CONNECTOR_MANAGED_IDENTITY_AND_EFFECTIVE_SCOPE_UNKNOWN
durability: PROVIDER_DURABILITY_EXPECTED_CONNECTOR_DURABILITY_UNVERIFIED
observability: PARTIAL_RESULT_SHAPE_AND_LATENCY_NO_TRANSPORT_SCOPE_OR_QUOTA_RECEIPT
portability: MEDIUM
failure_behavior: NOT_PROBED_IN_PHASE1
consumer: NOT_ASSIGNED
consumer_ack: NOT_OBSERVED
verifier: NOT_ASSIGNED
independent_verification_closed: false
adoption_credit: 0
fitness_credit: 0
strongest_falsifier: SAME_PRINCIPAL_RAW_EVENTS_LIST_DISAGREES_OR_CONNECTOR_REJECTS_ITS_IMMEDIATELY_RETURNED_TOKEN_UNDER_IDENTICAL_BOUNDS
honest_flaw: ONE_POSITIVE_PRIMARY_CALENDAR_CALL_WITH_NO_QUERY_OR_PAGINATION_DOES_NOT_VERIFY_IDENTITY_SCOPE_ORDERING_COMPLETENESS_RECURRING_EVENTS_PRIVATE_REDACTION_PERMISSIONS_RATE_LIMITS_RAW_PARITY_QUOTA_OR_VALUE
valid_time_utc: 2026-08-04T21:47:04Z
recorded_time_utc: 2026-08-04T21:47:04Z
---

# Google Calendar search events — phase 1

## Official baseline

Google Calendar `events.list` accepts a calendar identifier, RFC3339 time bounds, a page size, free-text query, and page token. The raw response can expose event items, a continuation token, a sync token, and calendar-level metadata. Google documents read-only event scopes. Current published limits are 10,000 requests per minute per project and 600 per minute per user per project. Standard use has no additional cost below a daily project threshold; the connector exposed no quota receipt.

Official references checked 2026-08-04:
- https://developers.google.com/workspace/calendar/api/v3/reference/events/list
- https://developers.google.com/workspace/calendar/api/auth
- https://developers.google.com/workspace/calendar/api/guides/quota

## Direct result

One read-only call searched the primary calendar alias inside explicit bounds with `max_results=1`. It returned one event result and a continuation token in 909 ms. No page follow-up, event hydration, retry, fallback, or mutation occurred.

The connector result included event identifier, summary, start/end, URL, description, transparency, and recurrence-related fields. It did not expose raw collection metadata, transport status, request ID, effective scope, or quota evidence. Event-specific identifiers, text, URLs, and token were not copied here.

Measured variance: this search surface is content-bearing, not metadata-only, because summary and description can be emitted without a separate read call.

## Decision

`PHASE1_ACCEPTED_WITH_GATES`

Admitted claim: one bounded primary-calendar search returned one event object and a continuation token without a separate hydration call.

Gates:
1. Treat results as content-bearing.
2. Retain no event values or tokens without a named need.
3. Always use explicit bounds and a minimal result cap.
4. Do not infer completeness, identity, scope, access role, ordering, or raw parity.
5. Require raw same-principal verification, quota evidence, consumer acknowledgment, and measured value before unattended use.
6. Keep adoption and fitness credit at zero.

Next: one synthetic unlikely-token, bounded, read-only phase-2 search with no pagination, hydration, retry, fallback, retention, or mutation.