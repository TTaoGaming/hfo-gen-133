---
schema_id: hfo.gen133.x13.cots_connector_event.v1
experiment_id: X13_GOOGLE_CALENDAR_READONLY_CONNECTOR_001
candidate: Calendar_read_only_event_search_and_free_busy_connector
phase: 1
phase_name: OFFICIAL_CONTRACT_AND_DIRECT_CAPABILITY_BASELINE
result: PHASE1_BASELINE_ACCEPTED
expected_prior_version: 16
next_version: 17
prior_current_blob_sha: b4b79c6401c42ef78240392e3c57ab4fdd88989d
carrier_task_id: 6a55c1733708819185088bf334e33ea5
carrier_task_id_match: true
carrier_task_id_observation_source: AUTOMATION_RUNTIME_PROMPT
wip: 1
effect_ceiling: READ_ONLY_CALENDAR_SEARCH_AND_FREEBUSY_BASELINE_NO_EVENT_BODY_PERSISTENCE_NO_WRITE
valid_time_utc: 2026-08-01T13:47:33Z
transaction_time_utc: SEE_GIT_COMMIT_METADATA
expiry_utc: 2026-08-08T13:47:33Z
verifier: S04_STRUCTURAL_PREFLIGHT_THEN_DISTINCT_NONPRODUCER_FOR_SCOPE_PRIVACY_QUOTA_OR_INTERNAL_CALL_SEQUENCE_CLAIMS
consumer: S05_OPERATOR_RELIEF_CELL_AND_X11_CARRIER_SURFACE_LAB
same_provider_binding_weight: 0
fitness_credit: 0_UNTIL_CONSUMED_BY_WORKITEM
---

# X13 Google Calendar read-only connector — phase 1 baseline

## Official contract baseline

Primary sources retrieved on 2026-08-01:

- Events list: https://developers.google.com/workspace/calendar/api/v3/reference/events/list
  - `GET /calendar/v3/calendars/{calendarId}/events` returns event resources and supports bounded time/query parameters.
  - Event resources can contain summaries, descriptions, locations, creator/organizer identities, attendees, and other private fields. Event search is therefore a higher-privacy surface than free/busy.
- Freebusy query: https://developers.google.com/workspace/calendar/api/v3/reference/freebusy/query
  - `POST /calendar/v3/freeBusy` returns calendar busy intervals and per-calendar/group errors, not event titles or descriptions.
  - Official maximum expansion values are 50 calendars and 100 group members per request.
- Calendar scopes: https://developers.google.com/workspace/calendar/api/auth
  - Narrow free/busy scopes exist (`calendar.freebusy` and `calendar.events.freebusy`).
  - Event reads can use read-only event/calendar scopes. The live connector scope is not exposed and is not claimed to be least privilege.
- Usage limits and pricing: https://developers.google.com/workspace/calendar/api/guides/quota
  - Google documents 10,000 requests per minute per project, 600 requests per minute per user per project, and a 1,000,000-request daily billing threshold for projects subject to the May 1, 2026 quota model.
  - Standard use below the threshold has no additional cost; charges above limits are planned later in 2026 with at least 90 days' notice.
  - The connector's project creation date, actual quota class, raw request count, and billing account state are hidden.

## Direct connector baseline

Two harmless read-only calls were executed against `primary` in the same bounded 30-minute interval.
No event body, title, attendee, description, location, exact busy interval, or calendar identity was persisted.

### Probe A — event search surface

- Connector/action: `Google Calendar / search_events`
- Connector ID: `connector_947e0d954944416db111db556030eea6`
- Query: `X13_NONEXISTENT_SENTINEL_20260801`
- Bounds: explicit RFC3339 interval; `max_results=5`; timezone `America/Denver`
- Result: success; `events=[]`; `next_page_token=null`
- Exposed latency: 191 ms
- Error class: none exposed
- Interpretation gate: this proves the wrapper can execute one authenticated bounded search. An empty synthetic result does not prove global absence, permission scope, raw Google behavior, or one upstream request.

### Probe B — free/busy surface

- Connector/action: `Google Calendar / get_availability`
- Connector ID: `connector_947e0d954944416db111db556030eea6`
- Calendar selector: `primary`
- Bounds: same explicit RFC3339 interval; response timezone `America/Denver`
- Result: success; calendar-level error field was null; busy interval values and count were observed but deliberately not persisted
- Exposed latency: 155 ms
- Error class: none exposed
- Interpretation gate: this proves one authenticated free/busy call and the wrapper's privacy-narrow output shape. It does not prove the live OAuth scope, access to secondary calendars, permission-denial semantics, or raw request count.

## Measurements

- custom_code_avoided_estimate:
  - bounded event search, pagination, and normalization: 40–120 LOC, unvalidated
  - free/busy request and response normalization: 30–80 LOC, unvalidated
  - authentication/token management avoided: material but unquantified because connector internals and scope are hidden
  - no additive total claimed because these functions overlap
- operator_minutes_this_wake: 0
- operator_minutes_removed_potential: 2–5 per consumed availability or obligation-reconciliation check, unvalidated
- credentials: connector authenticated; identity, token type, OAuth client, scopes, refresh policy, and credential custody are unknown
- durability: Google Calendar provider durability only; no workflow replay, resume, transaction, exactly-once, or cross-system atomicity claim
- observability: action name, connector ID, normalized result, exposed latency, and connector error envelope available; raw HTTP status, headers, quota counters, retries, internal call sequence, and audit identity hidden
- portability: medium at the Calendar/free-busy semantic level; low for wrapper-specific action schemas and normalized outputs; other providers untested
- direct_cost_or_quota_evidence: no paid charge surfaced; official standard use is currently no-additional-cost below the applicable threshold; actual connector request count and project quota class unknown
- failure_behavior: not probed in phase 1; empty success is not a permission or provider-failure receipt

## Supported claims

- The connected surface can run bounded read-only primary-calendar event search and free/busy calls.
- Free/busy is the lower-privacy default for availability questions because its contract returns intervals rather than event content.
- Direct calls completed without operator relay, event mutation, login, or account change.

## Excluded claims

- Least-privilege OAuth scope, exact connector request count, exact quota consumption, billing safety, secondary-calendar access, permission-denial semantics, raw Google error behavior, durable workflow execution, exactly-once behavior, independent verification, or consumer value.
- The empty sentinel search is not evidence that matching events never exist or that permissions are complete.

## Gates before adoption

1. Prefer free/busy for availability; use event search only when titles or known obligation pointers are required.
2. Bound every search by explicit time window and low result cap; page only inside the same bounded window.
3. Keep event bodies, attendee lists, descriptions, locations, exact private busy intervals, and calendar IDs in the source system unless an explicit WorkItem requires sanitized extraction.
4. Treat empty search results as `not found or unknown`, never as permission proof or global absence.
5. Do not describe the connector as least privilege while live scope and credential custody are hidden.
6. Use low-rate bounded calls while raw quota, retries, billing class, and internal call sequence are hidden.
7. Do not claim provider durability as workflow durability or exactly-once execution.

## Strongest falsifier

A distinct review or direct connector inspection shows that free/busy causes hidden event-body reads or excessive upstream calls; a known-existing bounded event cannot be found while the same calendar is otherwise accessible; or the live connector scope is materially broader than required and cannot be gated.

## Honest flaw

This baseline used only the primary calendar, one synthetic empty search, and one live free/busy interval. It did not test a known event, pagination, secondary calendars, inaccessible calendars, permission failure, quota failure, recurrence expansion, all-day events, timezone edge cases, connector retries, or portability. The connector receipts are same-provider telemetry with binding weight zero.

## Next phase

Phase 2: use the smallest harmless read-only micro-use against one already-externalized operator obligation, with an exact bounded search and no private event-body persistence. Candidate: reconcile the existing Reed HVAC verification event and measure operator minutes removed.
