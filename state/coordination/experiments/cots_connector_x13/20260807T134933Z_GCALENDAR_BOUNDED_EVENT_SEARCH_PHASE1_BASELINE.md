---
schema_id: hfo.gen133.x13.cots_connector_event.v1
experiment_id: X13_GCALENDAR_BOUNDED_EVENT_SEARCH_READONLY_016
candidate: Google_Calendar_bounded_keyword_event_search
phase: 1
phase_status: PHASE1_ACCEPTED_WITH_GATES
campaign_wake: 1_of_4
prior_current_version: 160
expected_current_version: 161
wip: 1
valid_time_utc: 2026-08-07T13:49:33Z
recorded_time_utc: 2026-08-07T13:49:33Z
---

# X13 Google Calendar bounded event search — Phase 1 baseline

## Direct connector receipt

One bounded read-only Google Calendar search was issued against `primary` with free-text query `HFO`, `max_results=3`, and explicit RFC3339 bounds `2026-08-01T00:00:00Z` through `2026-09-01T00:00:00Z`.

Measured wrapper result:

- returned_events: 2
- next_page_token_present: false
- connector_error_present: false
- retries: 0
- fallbacks: 0
- candidate_mutations: 0
- external_call_time_ms: 334
- event_content_hydration_observed: true
- raw_event_ids_summaries_descriptions_links_attendees_or_tokens_persisted_here: false
- request_digest_sha256: `ddee55c7b58dab58713adc1946cf1e966f2336d639ed5afd0e8cc95fb7498d4c`
- ordered_result_digest_sha256: `0ab726a1b9f8b223ebd0eb9c6d074ac57f9f9de1550f10b02fd2608d44f9ff5c`
- normalized_wrapper_shape_digest_sha256: `c3674c1fc40004e945a0eafc1829f7c32e91c65f1c137b50e40a1066dc8376d4`

Measured Andon: this search surface hydrates event content/metadata, including summaries, descriptions, start/end timestamps and event links. It is not a least-data ID-only discovery surface.

Measured boundary behavior: one returned event began before `time_min` but ended after `time_min`. This is consistent with the native Calendar `events.list` contract: `timeMin` is an exclusive lower bound on an event's **end** time, while `timeMax` is an exclusive upper bound on an event's **start** time. A bounded query therefore selects overlapping events; it must not be interpreted as “event start lies inside the window.”

## Official contract baseline

Primary documentation:

- https://developers.google.com/workspace/calendar/api/v3/reference/events/list
- https://developers.google.com/workspace/calendar/api/guides/quota
- https://developers.google.com/workspace/calendar/api/guides/errors
- https://developers.google.com/workspace/tools-safety

Native `events.list` facts relevant to the wrapper:

- Endpoint: `GET /calendar/v3/calendars/{calendarId}/events`.
- `q` is free-text search over event summary, description, location, attendee/organizer names and emails, plus supported working-location fields.
- `maxResults` controls page size; a result page can contain fewer than the requested maximum or none even when more matches exist. A non-empty `nextPageToken` is the explicit pagination signal.
- `timeMin` is the exclusive lower bound for an event's end time; `timeMax` is the exclusive upper bound for an event's start time.
- Read-capable authorization scopes include `calendar.readonly` and `calendar.events.readonly`, among others. The connector's effective principal and granted scope are not exposed by this wrapper receipt.
- Native error classes include invalid credentials, rate-limit/quota errors, inaccessible-resource/not-found cases, and backend failures.

Current Google Calendar quota documentation, updated for the May 1 2026 model, is request-based rather than per-method quota-unit based: 10,000 requests/minute/project, 600 requests/minute/user/project, and a 1,000,000 requests/day/project threshold before planned later-2026 billing. Projects that used the API between November 2025 and April 2026 can retain their prior quota settings. This connector did not expose its backing project, actual quota regime, request debit, or billing state.

## Measures

- custom_code_avoided_estimate: `60_to_180_LOC_UNVALIDATED`
- operator_minutes_removed_measured: `0`
- credentials: `CONNECTOR_MANAGED_EFFECTIVE_PRINCIPAL_AND_SCOPES_UNKNOWN`
- durability: `GIT_RECEIPT_DURABLE;CALENDAR_SEARCH_VIEW_MUTABLE`
- observability: `RETURN_COUNT_NEXT_PAGE_TOKEN_PRESENCE_CONTENT_FIELDS_AND_EXTERNAL_CALL_TIME_VISIBLE;PROVIDER_REQUEST_ID_RATE_HEADERS_ACCESS_ROLE_EFFECTIVE_SCOPE_ACTUAL_QUOTA_DEBIT_NOT_SURFACED`
- portability: `MEDIUM_QUERY_TIME_WINDOW_AND_EVENT_RESOURCE_SEMANTICS_GOOGLE_SPECIFIC`
- failure_behavior: `ONE_NONEMPTY_HAPPY_PATH;NO_PERMISSION_DENIAL_RATE_LIMIT_TRANSIENT_FAILURE_OR_PAGINATION_REPLAY_TESTED`
- paid_cost_usd_observed: `0_NO_PAID_COST_SURFACED`
- direct_cost_or_quota_evidence: `NONE_FROM_CONNECTOR`
- verifier: `DIRECT_GOOGLE_CALENDAR_CONNECTOR_RECEIPT_PLUS_OFFICIAL_GOOGLE_CONTRACT_PLUS_GITHUB_READBACK`
- consumer: `CALENDAR_DISCOVERY_ELIGIBLE_BUT_NO_OPERATIONAL_CONSUMER_ACK`
- adoption_credit: `0`
- fitness_credit: `0`

## Gates

Use only explicit bounded RFC3339 windows and small result caps. Treat `timeMin`/`timeMax` with their native overlap semantics, not as start-time containment. Do not persist raw event IDs, titles, descriptions, attendee identities, links, or page tokens in X13 receipts. A missing `next_page_token` is only page-level evidence for this wrapper call; an empty result in a later probe must not be promoted to an authoritative calendar-wide absence claim. Consequential claims require `read_event` or a matched native-provider witness. No unbounded retries.

## Strongest falsifier

A matched native Google Calendar v3 `events.list` call under the same effective principal materially disagrees on query scope, overlap-window semantics, result visibility, ordering/pagination, or content hydration behavior.

## Honest flaw

This phase used one successful keyword query and observed two events. It did not test empty-success behavior, permission denial, private-event visibility, secondary/shared-calendar variance, recurrence expansion, pagination replay, rate limiting, transient failure, native parity, effective OAuth scope, actual quota debit, measured operator savings, or operational-consumer value.

## Next

Phase 2: replay the identical bounded read-only request once and compare request and ordered-result digests. Persist no raw Calendar content.
