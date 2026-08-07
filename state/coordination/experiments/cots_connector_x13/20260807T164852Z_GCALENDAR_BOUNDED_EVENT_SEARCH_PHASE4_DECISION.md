---
schema_id: hfo.gen133.x13.cots_connector_event.v1
experiment_id: X13_GCALENDAR_BOUNDED_EVENT_SEARCH_READONLY_016
candidate: Google_Calendar_bounded_keyword_event_search
phase: 4
phase_status: PHASE4_DECIDED
phase_4_decision: ADOPT_WITH_GATES
campaign_wake: 4_of_4
prior_current_version: 163
expected_current_version: 164
wip: 1
valid_time_utc: 2026-08-07T16:48:52Z
recorded_time_utc: 2026-08-07T16:48:52Z
---

# X13 Google Calendar bounded event search — Phase 4 decision

## Decision

**ADOPT_WITH_GATES** for bounded read-only Calendar discovery/catalog use only.

Phase 4 issued no additional Calendar candidate call. This decision uses the frozen three-call evidence set from Phases 1–3.

## Frozen evidence

- campaign_calls_total: `3_BOUNDED_READONLY_GCALENDAR_SEARCHES`
- successful_nonempty_calls: `2`
- successful_empty_calls: `1`
- phase1_phase2_request_digest_match: `true`
- phase1_phase2_ordered_result_digest_match: `true`
- connector_errors_observed: `0`
- retries_total: `0`
- fallbacks_total: `0`
- candidate_mutations_total: `0`
- event_content_hydration_observed: `TRUE_ON_NONEMPTY_FALSE_ON_EMPTY`
- phase1_connector_call_time_ms: `334`
- phase2_connector_call_time_ms: `437`
- phase3_connector_call_time_ms: `212`
- measured_overlap_boundary_behavior: `TRUE_ONE_RETURNED_EVENT_STARTED_BEFORE_TIMEMIN_AND_ENDED_AFTER_TIMEMIN`

The identical Phase-1/Phase-2 bounded query produced the same ordered result digest over the short replay interval. Phase 3 showed that an intentionally nonmatching bounded search can return an empty success distinctly from a connector error. Neither fact establishes immutable ordering, snapshot semantics, permission completeness, or Calendar-wide absence.

## Measures

- custom_code_avoided_estimate: `60_to_180_LOC_UNVALIDATED`
- operator_minutes_removed_measured: `0`
- credentials: `CONNECTOR_MANAGED_EFFECTIVE_PRINCIPAL_AND_SCOPES_UNKNOWN`
- durability: `GIT_RECEIPT_DURABLE;CALENDAR_SEARCH_VIEW_MUTABLE`
- observability: `RETURN_COUNT_NEXT_PAGE_TOKEN_PRESENCE_CONTENT_FIELDS_ERROR_SHAPE_AND_EXTERNAL_CALL_TIME_VISIBLE;PROVIDER_REQUEST_ID_RATE_HEADERS_ACCESS_ROLE_EFFECTIVE_SCOPE_ACTUAL_QUOTA_DEBIT_NOT_SURFACED`
- portability: `MEDIUM_QUERY_TIME_WINDOW_AND_EVENT_RESOURCE_SEMANTICS_GOOGLE_SPECIFIC`
- failure_behavior: `TWO_NONEMPTY_SUCCESSES_PLUS_ONE_EMPTY_SUCCESS;EMPTY_RESULT_DISTINGUISHABLE_FROM_CONNECTOR_ERROR;NO_PERMISSION_DENIAL_PRIVATE_VISIBILITY_SECONDARY_SHARED_CALENDAR_VARIANCE_RATE_LIMIT_TRANSIENT_FAILURE_OR_PAGINATION_REPLAY_TESTED`
- paid_cost_usd_observed: `0_NO_PAID_COST_SURFACED`
- direct_cost_or_quota_evidence: `NONE_FROM_CONNECTOR`
- verifier: `PHASE1_PHASE2_PHASE3_DIRECT_CONNECTOR_RECEIPTS_PLUS_GITHUB_IMMUTABLE_EVENT_AND_CURRENT_READBACK`
- consumer: `CALENDAR_DISCOVERY_ELIGIBLE_BUT_NO_OPERATIONAL_CONSUMER_ACK`
- adoption_credit: `1_CATALOG_ONLY`
- fitness_credit: `0`

## Mandatory gates

1. Use an explicit bounded RFC3339 window and a small result cap.
2. Keep the candidate read-only; no Calendar mutation follows from discovery without a separate operator-approved action.
3. Interpret Google Calendar time-window semantics correctly: `timeMin` bounds event end and `timeMax` bounds event start; overlap is not equivalent to event-start-inside-window.
4. Do not persist raw event IDs, titles, descriptions, attendee identities, links, page tokens, or synthetic search text into X13 receipts; persist only derived counts/digests and bounded measurements.
5. Treat search output as mutable discovery, not snapshot-stable evidence.
6. An empty success is not a Calendar-wide absence claim. Other calendars, visibility restrictions, indexing, recurrence handling, and pagination can omit relevant events.
7. A missing next-page token is evidence only for the wrapper response seen, not proof of global completeness under unknown visibility/effective scopes.
8. Consequential or completeness claims require direct event retrieval or a matched native Google Calendar witness under the same effective principal with explicit pagination/visibility evidence.
9. No unbounded retry. Connector/provider errors fail closed rather than being converted into absence.

## Strongest falsifier

A matched native Google Calendar v3 `events.list` call under the same effective principal and same bounded query returns a materially different result set, empty/nonempty shape, visibility set, pagination state, or authorization/error outcome without an intervening Calendar mutation or indexing change.

## Honest flaw

This campaign never exercised permission denial, private-event visibility, secondary/shared-calendar variance, recurrence expansion, pagination replay, rate limiting, transient provider failure, index lag, native-provider parity, effective OAuth scope, provider request identity, or actual quota debit. The connector hydrates event content on nonempty searches, so it is not a least-data ID-only discovery surface. Measured operator-minute savings and operational-consumer value remain zero, so fitness credit remains zero despite narrow adoption credit.

## Closure

Campaign closed at wake 4 of 4 with `ADOPT_WITH_GATES`. Next wake may start one new candidate at Phase 1 with WIP=1.