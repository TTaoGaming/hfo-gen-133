---
schema_id: hfo.gen133.x13.cots_connector_event.v1
experiment_id: X13_GCALENDAR_BOUNDED_EVENT_SEARCH_READONLY_016
candidate: Google_Calendar_bounded_keyword_event_search
phase: 2
phase_status: PHASE2_ACCEPTED_WITH_GATES
campaign_wake: 2_of_4
prior_current_version: 161
expected_current_version: 162
wip: 1
valid_time_utc: 2026-08-07T14:49:09Z
recorded_time_utc: 2026-08-07T14:49:09Z
---

# X13 Google Calendar bounded event search — Phase 2 replay

## Direct connector receipt

Replayed the identical bounded read-only Google Calendar search from Phase 1 against `primary` with free-text query `HFO`, `max_results=3`, and explicit RFC3339 bounds `2026-08-01T00:00:00Z` through `2026-09-01T00:00:00Z`.

Measured wrapper result:

- returned_events: 2
- next_page_token_present: false
- connector_error_present: false
- retries: 0
- fallbacks: 0
- candidate_mutations: 0
- external_call_time_ms: 437
- event_content_hydration_observed: true
- raw_event_ids_summaries_descriptions_links_attendees_or_tokens_persisted_here: false
- request_digest_sha256: `ddee55c7b58dab58713adc1946cf1e966f2336d639ed5afd0e8cc95fb7498d4c`
- phase1_request_digest_match: true
- ordered_result_digest_sha256: `0ab726a1b9f8b223ebd0eb9c6d074ac57f9f9de1550f10b02fd2608d44f9ff5c`
- phase1_ordered_result_digest_match: true

Ordered-result digest canonicalization is the ordered array of `{id, summary, start, end}` records serialized as UTF-8 JSON with sorted keys and compact separators, then SHA-256 hashed. The raw values used to compute the digest are intentionally not persisted in this receipt.

Measured fact: the identical bounded request reproduced the same ordered-result digest one wake later. This is narrow short-horizon repeatability evidence only. It does not prove snapshot semantics, immutable ordering, completeness, or stability under calendar mutation.

The Phase 1 overlap-boundary observation remains in force: this bounded search expresses event overlap using Google Calendar native `timeMin`/`timeMax` semantics, not start-time containment.

## Measures

- campaign_calls_total: `2_BOUNDED_READONLY_GCALENDAR_SEARCHES`
- successful_nonempty_calls: `2`
- successful_empty_calls: `0`
- connector_errors_observed: `0`
- retries_total: `0`
- fallbacks_total: `0`
- candidate_mutations_total: `0`
- custom_code_avoided_estimate: `60_to_180_LOC_UNVALIDATED`
- operator_minutes_removed_measured: `0`
- credentials: `CONNECTOR_MANAGED_EFFECTIVE_PRINCIPAL_AND_SCOPES_UNKNOWN`
- durability: `GIT_RECEIPT_DURABLE;CALENDAR_SEARCH_VIEW_MUTABLE`
- observability: `RETURN_COUNT_NEXT_PAGE_TOKEN_PRESENCE_CONTENT_FIELDS_AND_EXTERNAL_CALL_TIME_VISIBLE;PROVIDER_REQUEST_ID_RATE_HEADERS_ACCESS_ROLE_EFFECTIVE_SCOPE_ACTUAL_QUOTA_DEBIT_NOT_SURFACED`
- portability: `MEDIUM_QUERY_TIME_WINDOW_AND_EVENT_RESOURCE_SEMANTICS_GOOGLE_SPECIFIC`
- failure_behavior: `TWO_NONEMPTY_HAPPY_PATHS_WITH_MATCHED_ORDERED_DIGEST;NO_PERMISSION_DENIAL_RATE_LIMIT_TRANSIENT_FAILURE_OR_PAGINATION_REPLAY_TESTED`
- paid_cost_usd_observed: `0_NO_PAID_COST_SURFACED`
- direct_cost_or_quota_evidence: `NONE_FROM_CONNECTOR`
- verifier: `DIRECT_GOOGLE_CALENDAR_CONNECTOR_REPLAY_PLUS_PHASE1_GIT_RECEIPT_PLUS_GITHUB_READBACK`
- consumer: `CALENDAR_DISCOVERY_ELIGIBLE_BUT_NO_OPERATIONAL_CONSUMER_ACK`
- adoption_credit: `0`
- fitness_credit: `0`

## Gates

Keep the Phase 1 gates unchanged: explicit bounded RFC3339 window, small result cap, read-only search, native overlap semantics, no raw Calendar-content persistence in X13 receipts, no completeness or absence claim without pagination evidence, consequential claims require `read_event` or a matched native-provider witness, and no unbounded retry.

## Strongest falsifier

A later identical bounded search or matched native Google Calendar v3 `events.list` call under the same effective principal materially disagrees on query scope, overlap-window semantics, result visibility, ordering/pagination, or content-hydration behavior in a way not explained by an intervening calendar mutation.

## Honest flaw

The two-call digest match is only short-horizon repeatability on one keyword/window. Empty-success behavior, permission denial, private-event visibility, secondary/shared-calendar variance, recurrence expansion, pagination replay, rate limiting, transient failure, native parity, effective OAuth scope, actual quota debit, measured operator savings, and operational-consumer value remain untested.

## Next

Phase 3: issue one bounded synthetic nonmatching Calendar search in the same explicit window, with no retry and no authoritative calendar-wide absence claim.
