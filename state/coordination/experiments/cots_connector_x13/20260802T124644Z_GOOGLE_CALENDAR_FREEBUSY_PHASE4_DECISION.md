---
schema_id: hfo.gen133.x13.cots_connector_event.v1
experiment_id: X13_GOOGLE_CALENDAR_FREEBUSY_READONLY_001
event_type: PHASE_4_ADOPTION_DECISION
phase: 4_of_4
prior_current_version: 39
next_current_version: 40
valid_time_utc: 2026-08-02T12:46:44Z
carrier_task_id: 6a55c1733708819185088bf334e33ea5
candidate_invocation_this_wake: false
write_side_effect_on_candidate: false
sealed: true
---

# Google Calendar Freebusy phase 4 decision

Decision: `ADOPT_WITH_GATES`.

Admitted use is narrow: bounded, read-only occupancy checks against explicitly selected calendars and RFC3339 intervals in the current authenticated connector context. The connector may normalize busy intervals and resource-scoped errors for scheduling assistance, but it is not an authority to inspect event details, create or change events, or decide that a person is available when any calendar result is missing or errored.

Evidence admitted:
- one bounded `primary` query returned an empty busy result without event content or write effects;
- one bounded `primary` query returned two ordered, non-overlapping busy intervals that passed local bounds and duration checks; only privacy-minimized aggregates were persisted;
- one synthetic invalid-calendar query returned a per-calendar `global/notFound` while the top-level request completed, proving callers must inspect each calendar result;
- Google documents explicit RFC3339 bounds, per-calendar busy/error fields, inclusive busy starts, exclusive busy ends, multiple authorization scopes, and no persistent Freebusy resource.

Mandatory gates:
1. Supply explicit RFC3339 start and end values with `Z` or an offset.
2. Treat `primary` as a context-dependent alias, not a durable identity.
3. Inspect every calendar's error field; any error means unknown availability, never free time.
4. Treat empty busy arrays only as the result of that query, not proof of calendar completeness or personal availability.
5. Preserve successful and failed calendar results separately.
6. Minimize or redact exact busy patterns and calendar identifiers before Git or Slack persistence.
7. Do not infer nonexistence versus permission denial from `notFound` alone.
8. Handle unknown future error reasons safely; use bounded exponential backoff only for documented transient or rate-limit classes.
9. Do not claim authenticated identity, OAuth scope, project, billing state, live quota, independent accuracy, or portability without separate evidence.
10. No event creation, invitations, responses, edits, deletion, broad event mining, or automatic booking authority.

Measurements:
- measured operator minutes removed: 0;
- estimated future relief: 1-5 minutes per bounded availability check, unvalidated;
- custom code avoided estimate: 40-120 LOC for authenticated request/normalization/error handling plus 20-60 LOC for interval validation, unvalidated and non-additive;
- surfaced paid cost: $0;
- credentials: connector authenticated, but identity, token type, scopes, project, authority, and custody remain unknown;
- durability: ephemeral point-in-time query over mutable calendar state;
- observability: normalized intervals and per-calendar errors visible; raw HTTP, request ID, retries, scopes, quota, and billing counters hidden;
- portability: medium for generic RFC3339 free/busy intervals, medium-low for Google aliases, IDs, OAuth scopes, errors, limits, and connector rendering;
- failure behavior: synthetic invalid resource failed closed at the resource level, but real access denial, mixed-calendar responses, 403/429/500, and DST boundaries remain untested;
- fitness credit: 0 pending source-bound ConsumerAck and measured operator outcome.

Official references checked on 2026-08-02:
- https://developers.google.com/workspace/calendar/api/v3/reference/freebusy/query
- https://developers.google.com/workspace/calendar/api/guides/errors
- https://developers.google.com/workspace/calendar/api/guides/quota

Verifier: raw Google Calendar Freebusy API or a distinct authorized calendar client using the same explicit interval and source-bound calendar ID, with raw response and scope evidence.

Consumer: HFO scheduling and executive-assistant planning logic.

Strongest falsifier: a distinct authorized client returns materially different busy or error results for the same source-bound calendar and interval, or the connector collapses mixed success/error results into misleading global availability.

Honest flaw: the campaign did not establish authenticated identity or scope, test a shared or secondary calendar, distinguish inaccessible from nonexistent resources, exercise mixed results, 403/429/500, DST boundaries, or obtain independent readback or ConsumerAck.

Result: `ADOPT_WITH_GATES` for bounded read-only occupancy assistance only.
