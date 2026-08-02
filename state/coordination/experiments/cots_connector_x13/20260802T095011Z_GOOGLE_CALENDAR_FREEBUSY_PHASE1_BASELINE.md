---
schema_id: hfo.gen133.x13.cots_connector_event.v1
experiment_id: X13_GOOGLE_CALENDAR_FREEBUSY_READONLY_001
phase: 1_of_4
event_kind: OFFICIAL_CONTRACT_AND_DIRECT_CAPABILITY_BASELINE
prior_current_version: 36
expected_next_current_version: 37
carrier_task_id: 6a55c1733708819185088bf334e33ea5
carrier_task_id_match: true
candidate: Google_Calendar_freebusy_readonly_connector_surface
campaign_status: IN_PROGRESS
candidate_invocations_this_wake: 1
effect_ceiling: OFFICIAL_CONTRACT_BASELINE_AND_ONE_BOUNDED_READ_ONLY_PRIMARY_CALENDAR_FREEBUSY_QUERY_ONLY
valid_time_utc: 2026-08-02T09:50:11Z
transaction_time_utc: SEE_GIT_COMMIT_METADATA
sealed: true
---

# X13 phase-1 baseline — Google Calendar Freebusy read-only

## Direct capability baseline

One bounded read-only availability query was executed against the authenticated connector's `primary` calendar alias for `2026-08-02T10:00:00Z` through `2026-08-02T11:00:00Z`, with response timestamps requested in `America/Denver`.

Normalized connector result:

- calendar identifier returned: `primary`
- busy intervals returned: `0`
- per-calendar errors returned: `null`
- top-level connector error: `null`
- observed external-call time: `214 ms`
- event titles, descriptions, attendees, locations, conferencing data, and event identifiers returned: `none`
- write side effects: `none`

The result establishes only that this connector returned no busy interval for this one calendar alias and one bounded interval. It does not prove the calendar had no private, declined, transparent, hidden, all-day, out-of-office, focus-time, or otherwise omitted events, nor does it establish independent completeness.

## Official contract baseline checked 2026-08-02

- Google Calendar `freeBusy.query` is `POST https://www.googleapis.com/calendar/v3/freeBusy` and returns free/busy information for calendars or groups: https://developers.google.com/workspace/calendar/api/v3/reference/freebusy/query
- Required request fields are RFC3339 `timeMin`, RFC3339 `timeMax`, and one or more calendar/group IDs; response timezone is optional and defaults to UTC.
- The response contract includes inclusive busy starts, exclusive busy ends, and per-calendar or per-group errors. Calendar expansion is capped at 50 and group expansion at 100.
- The documented acceptable scopes include `calendar.readonly`, `calendar`, `calendar.events.freebusy`, and `calendar.freebusy`; the connector did not expose which scope or credential it used.
- As of the official quota page updated 2026-05-01, Calendar API limits are 10,000 requests per minute per project and 600 requests per minute per user per project, with a 1,000,000-request daily project threshold before planned charges later in 2026. Live project-specific quota and billing state were not exposed: https://developers.google.com/workspace/calendar/api/guides/quota
- Google documents `403` or `429` `rateLimitExceeded` responses and recommends truncated exponential backoff. That failure path was not exercised: https://developers.google.com/workspace/calendar/api/guides/errors

## Measurements

- Custom code avoided estimate: `40–120 LOC` for authenticated Freebusy request construction, RFC3339/timezone validation, response normalization, and basic per-calendar error handling; unvalidated.
- Operator relay minutes: `0`.
- Operator minutes removed measured: `0`.
- Estimated future relief: `1–5 minutes` per bounded availability check, unvalidated and not credited.
- Operator-supplied credentials this wake: `0`.
- Live identity, OAuth client/project, token type, scopes, calendar ownership, delegated authority, and credential custody: `UNKNOWN`.
- Durability: no persistent Freebusy resource; this is an ephemeral point-in-time query over mutable calendar state.
- Observability: medium for normalized calendar ID, busy intervals, per-calendar errors, and connector timing; low for raw HTTP status/body/headers, request ID, OAuth scope, quota project/user, retries, and upstream request count.
- Portability: medium. Busy intervals and RFC3339 are broadly portable, but calendar IDs, `primary`, OAuth scopes, group expansion, error reasons, and quota semantics are Google-specific.
- Failure behavior: not yet probed. The successful empty result did not test inaccessible calendars, invalid IDs, malformed windows, partial per-calendar errors, rate limits, or transient backend errors.
- Direct cost evidence: `$0` surfaced by the connector. Official standard use is currently no additional cost below applicable thresholds, but the live project quota class, daily count, billing account, and future charge exposure are unknown.
- Fitness credit: `0` pending a source-bound ConsumerAck and measured operator outcome.

## Gates established in phase 1

1. Use explicit RFC3339 start/end datetimes with offsets or `Z`; never pass naive time values.
2. Treat response timezone as formatting only; it does not redefine the queried interval.
3. Treat `primary` as an authenticated-context alias, not a durable portable calendar identifier.
4. Freebusy results are occupancy windows only, not authorization to inspect event details or schedule over a person.
5. Preserve per-calendar errors separately from successful busy intervals; a partial response is not global success.
6. An empty busy array proves only that this call returned no busy block for the specified interval and calendar alias.
7. Do not persist calendar IDs, email-like resource IDs, or busy patterns to Slack or Git without need and data classification.
8. Do not claim live scope, identity, quota class, cost, completeness, or independent verification when the connector does not expose them.
9. No event creation, invitation, response, edit, deletion, or broad calendar mining is admitted.

## Verifier, consumer, falsifier, flaw

- Verifier: raw Google Calendar Freebusy API or a distinct authorized Calendar client using the same explicit interval and a source-bound calendar ID, with raw response and scope evidence.
- Consumer: HFO scheduling and executive-assistant planning logic that needs occupancy windows without event content.
- Strongest falsifier: a distinct authorized client returns a busy interval or per-calendar error for the same source-bound calendar and exact UTC interval that this connector omitted.
- Honest flaw: this baseline used only the `primary` alias and an empty one-hour interval; it did not test a known-busy interval, secondary/shared calendar, inaccessible calendar, partial errors, DST boundary, all-day event, group expansion, quota response, retries, or independent readback.

## Next phase

Phase 2 should perform the smallest harmless micro-use: query one explicitly bounded near-term planning window on `primary`, then separately read event candidates only if needed to validate whether returned busy windows correspond structurally. Event details are not required for adoption credit; no event mutation is permitted.
