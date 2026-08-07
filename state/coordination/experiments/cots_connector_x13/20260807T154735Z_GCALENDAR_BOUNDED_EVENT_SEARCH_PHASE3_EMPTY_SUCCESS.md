---
schema_id: hfo.gen133.x13.cots_connector_event.v1
experiment_id: X13_GCALENDAR_BOUNDED_EVENT_SEARCH_READONLY_016
candidate: Google_Calendar_bounded_keyword_event_search
phase: 3
phase_status: PHASE3_ACCEPTED_WITH_GATES
campaign_wake: 3_of_4
prior_current_version: 162
expected_current_version: 163
wip: 1
valid_time_utc: 2026-08-07T15:47:35Z
recorded_time_utc: 2026-08-07T15:47:35Z
---

# X13 Google Calendar bounded event search — Phase 3 empty-success probe

## Direct connector receipt

Issued exactly one bounded read-only Google Calendar search against `primary` in the same explicit RFC3339 window used by Phases 1–2: `2026-08-01T00:00:00Z` through `2026-09-01T00:00:00Z`, `max_results=3`, using a synthetic free-text token designed not to match. The raw synthetic token is intentionally not persisted in this receipt.

Measured wrapper result:

- returned_events: 0
- next_page_token_present: false
- connector_error_present: false
- retries: 0
- fallbacks: 0
- candidate_mutations: 0
- external_call_time_ms: 212
- event_content_hydration_observed: false_on_empty_result
- raw_event_ids_summaries_descriptions_links_attendees_tokens_or_synthetic_query_persisted_here: false

Measured fact: the Calendar connector can represent an empty bounded search as a successful result distinct from a connector error. This is only empty-success semantics for one deliberately nonmatching query. It is not evidence that no relevant event exists elsewhere in the calendar, outside the bounded window, under different indexed text, on another calendar, or behind visibility/permission boundaries.

## Measures

- campaign_calls_total: `3_BOUNDED_READONLY_GCALENDAR_SEARCHES`
- successful_nonempty_calls: `2`
- successful_empty_calls: `1`
- connector_errors_observed: `0`
- retries_total: `0`
- fallbacks_total: `0`
- candidate_mutations_total: `0`
- custom_code_avoided_estimate: `60_to_180_LOC_UNVALIDATED`
- operator_minutes_removed_measured: `0`
- credentials: `CONNECTOR_MANAGED_EFFECTIVE_PRINCIPAL_AND_SCOPES_UNKNOWN`
- durability: `GIT_RECEIPT_DURABLE;CALENDAR_SEARCH_VIEW_MUTABLE`
- observability: `RETURN_COUNT_NEXT_PAGE_TOKEN_PRESENCE_ERROR_SHAPE_AND_EXTERNAL_CALL_TIME_VISIBLE;PROVIDER_REQUEST_ID_RATE_HEADERS_ACCESS_ROLE_EFFECTIVE_SCOPE_ACTUAL_QUOTA_DEBIT_NOT_SURFACED`
- portability: `MEDIUM_QUERY_TIME_WINDOW_AND_EVENT_RESOURCE_SEMANTICS_GOOGLE_SPECIFIC`
- failure_behavior: `TWO_NONEMPTY_SUCCESSES_PLUS_ONE_EMPTY_SUCCESS;EMPTY_RESULT_DISTINGUISHABLE_FROM_CONNECTOR_ERROR;NO_PERMISSION_DENIAL_PRIVATE_VISIBILITY_SECONDARY_SHARED_CALENDAR_VARIANCE_RATE_LIMIT_TRANSIENT_FAILURE_OR_PAGINATION_REPLAY_TESTED`
- paid_cost_usd_observed: `0_NO_PAID_COST_SURFACED`
- direct_cost_or_quota_evidence: `NONE_FROM_CONNECTOR`
- verifier: `DIRECT_GOOGLE_CALENDAR_CONNECTOR_PHASE3_RECEIPT_PLUS_PHASE1_PHASE2_GIT_RECEIPTS_PLUS_GITHUB_READBACK`
- consumer: `CALENDAR_DISCOVERY_ELIGIBLE_BUT_NO_OPERATIONAL_CONSUMER_ACK`
- adoption_credit: `0`
- fitness_credit: `0`

## Gates

Keep prior gates unchanged: explicit bounded RFC3339 window, small result cap, read-only search, Google overlap semantics for `timeMin`/`timeMax`, no raw Calendar-content persistence in X13 receipts, and no completeness or absence claim from an empty result. Consequential claims require direct event retrieval or a matched native-provider witness with explicit pagination/visibility evidence. No unbounded retry.

## Strongest falsifier

A matched native Google Calendar v3 `events.list` call under the same effective principal and same bounded query returns a materially different empty/nonempty shape, visibility set, pagination state, or error/authorization outcome without an intervening calendar mutation or indexing change.

## Honest flaw

The synthetic token was intentionally designed to miss. Phase 3 therefore tested only empty-success semantics, not real permission denial or provider failure. Private-event visibility, secondary/shared-calendar variance, recurrence expansion, pagination replay, rate limiting, transient failure, index lag, native parity, effective OAuth scope, actual quota debit, measured operator savings, and operational-consumer value remain untested or unexposed.

## Next

Phase 4: decide `ADOPT | ADOPT_WITH_GATES | DEFER | REJECT | UNKNOWN` from the frozen three-call evidence set only; issue no additional Calendar candidate call.
