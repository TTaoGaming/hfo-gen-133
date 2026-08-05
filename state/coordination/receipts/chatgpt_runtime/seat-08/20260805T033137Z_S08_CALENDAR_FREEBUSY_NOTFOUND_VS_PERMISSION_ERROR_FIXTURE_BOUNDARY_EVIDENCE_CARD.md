---
schema_id: hfo.gen133.s08.evidence_card.v1
seat: S08_RESEARCH_AND_CANDIDATE_SCOUT
carrier_task_id_expected: 6a526109ba348191b5f23ad3172ad568
carrier_task_id_observed: 6a526109ba348191b5f23ad3172ad568
carrier_task_id_match: true
wip: 1
lane: agent-runtime/COTS_capabilities
question_id: X13_GOOGLE_CALENDAR_FREEBUSY_NOTFOUND_VS_PERMISSION_ERROR_FIXTURE_001
valid_time_utc: 2026-08-05T03:31:37Z
transaction_time_utc: SEE_GIT_COMMIT_METADATA
canonical_repository: TTaoGaming/hfo-gen-133
canonical_branch: agent/gen133-bootstrap-20260730
repository_head_observed_before_write: UNKNOWN_NOT_DIRECTLY_EXPOSED
candidate: Google_Calendar.get_availability
candidate_upstream: Google Calendar API v3 freebusy.query
candidate_connector_version: NOT_EXPOSED
upstream_reference_last_updated_utc: 2026-05-12
calendar_error_guide_last_updated_utc: 2026-07-16
decision: REVISE
consumer: X13_GOOGLE_CALENDAR_GET_AVAILABILITY_READONLY_001_PHASE3_AND_ANY_FREEBUSY_WORKITEM
verifier: DISTINCT_GOOGLE_CALENDAR_FREEBUSY_RAW_API_AND_CONNECTOR_PARTIAL_ERROR_VERIFIER
expiry_utc: 2026-08-12T03:31:37Z
fitness: 0_PENDING_EXACT_WORKITEM_CONSUMPTION_AND_CONSUMER_ACK
sealed: false
---

# S08 evidence card — a nonexistent calendar is not a permission-denial fixture

## Bounded uncertainty

Does X13 phase 3's planned query of `primary` plus one **synthetic inaccessible calendar ID** validly establish Google Calendar FreeBusy per-calendar permission-failure behavior for `Google_Calendar.get_availability`?

## Decision

`REVISE`

The planned probe conflates at least three different conditions: a syntactically malformed identifier, a syntactically valid but nonexistent calendar, and an existing calendar that the authenticated principal cannot read. A fabricated identifier can test `notFound` or connector input handling; it cannot by itself establish permission-denial behavior.

Split the assay into separately typed fixtures. Under this seat's constraints, documentation can justify a bounded **nonexistent-ID** probe, but an **existing-unreadable** fixture remains blocked unless a pre-existing authorized synthetic calendar and distinct principal are available.

## Changed queue evidence read on 2026-08-05

X13 `CURRENT.md` v102 names phase 3 as one bounded read-only query containing `primary` and one synthetic inaccessible calendar ID, with the goal of observing per-calendar failure behavior. It currently labels failure behavior unprobed and does not assign a consumer or verifier.

Exact queue state:

- experiment: `X13_GOOGLE_CALENDAR_GET_AVAILABILITY_READONLY_001`
- current version: `102`
- last event: `20260805T024817Z_GOOGLE_CALENDAR_GET_AVAILABILITY_PHASE2_MICRO_USE.md`
- next phase: `PHASE3_FAILURE_PERMISSION_PORTABILITY_AND_CONNECTOR_VARIANCE_PROBE`

## Current primary evidence checked on 2026-08-05

1. Google Calendar API v3 `freebusy.query`, last updated 2026-05-12 UTC:
   https://developers.google.com/workspace/calendar/api/v3/reference/freebusy/query
2. Google Calendar API error guide, last updated 2026-07-16 UTC:
   https://developers.google.com/workspace/calendar/api/guides/errors
3. Runtime connector schema observed in this wake for `Google_Calendar.get_availability`: accepts one or more calendar IDs, returns busy windows only, and states that inaccessible calendars are reported as per-calendar errors. Connector build, upstream request mapping, OAuth principal, effective scope, and normalization version are not exposed.

## Supported claims

- Raw `freebusy.query` accepts multiple calendar or group identifiers in one request.
- A successful raw response contains a `calendars` object keyed by requested identifier; each calendar entry can contain `busy[]` and optional `errors[]` with `domain` and `reason`.
- Google's documented possible per-calendar reasons include `notFound` and `internalError`; the list is explicitly non-exhaustive and clients must tolerate additional reasons.
- Raw FreeBusy therefore has a representation for partial per-item failure inside an otherwise successful response.
- The exposed connector description claims that inaccessible calendars are reported as per-calendar errors.
- The generic Calendar error guide says a top-level 404 can mean either a resource never existed or the caller cannot access it, but that guide does not prove the exact FreeBusy per-calendar mapping for either case.

## Excluded claims

- Every fabricated or unknown calendar ID produces a successful response with `calendars[id].errors[].reason=notFound`.
- A nonexistent calendar is equivalent to an existing calendar denied by permissions.
- The connector preserves Google's exact per-calendar `domain` and `reason` fields rather than reducing them to a count or normalized error.
- A valid `primary` result is always returned when a second requested item fails.
- A malformed identifier, nonexistent identifier, inaccessible existing calendar, scope failure, and connector validation failure share one error surface.
- The connector performs exactly one upstream request, exposes the effective OAuth scope, or has no hidden retry/fallback behavior.
- A zero-busy result for any errored calendar is evidence of availability.

## Required phase-3 revision

Use explicit, non-interchangeable fixture labels:

1. `NONEXISTENT_SYNTACTICALLY_VALID_CALENDAR_ID`
   - Goal: observe whether the connector returns a partial per-calendar `notFound`-class result while preserving the `primary` result.
   - This tests lookup failure, not permission denial.
   - Retain only aggregate booleans/counts and normalized error class; do not retain calendar IDs or busy timestamps.

2. `EXISTING_BUT_UNREADABLE_AUTHORIZED_SYNTHETIC_CALENDAR_ID`
   - Goal: observe permission behavior using a pre-existing test calendar controlled by a distinct authorized principal.
   - Do not create an account or calendar in this WorkItem.
   - If no such fixture already exists, record `BLOCKED_FIXTURE_NOT_AVAILABLE`; do not substitute a fabricated ID and call it permission testing.

3. Keep malformed-ID input validation as a separate negative control, not part of the permission assay.

For either executed probe: explicit RFC3339 bounds, `primary` plus exactly one test calendar, zero retry/fallback, no event-content access, no ID/timestamp retention, and no unattended scheduling decision.

## License and terms uncertainty

- Google developer documentation is published under CC BY 4.0 unless otherwise stated; code samples are Apache 2.0.
- Calendar API use is subject to Google API/OAuth and user-data terms not evaluated in this card.
- Connector-specific terms, versioning, telemetry, quota debit, and data-retention behavior remain `UNKNOWN`.
- No documentation text or code is being redistributed as a product in this pass.

## Cost and operator-minute estimate

- This research pass: `$0` external spend; `0` operator minutes.
- Update the phase-3 experiment wording and typed result schema: `10–20` producer minutes.
- Nonexistent-ID connector fixture and sanitized receipt: `10–20` producer minutes plus `10–20` verifier minutes.
- Existing-unreadable raw/connector parity fixture: `20–45` producer minutes plus `20–45` distinct-verifier minutes **only if** a pre-existing authorized synthetic calendar/principal pair exists; otherwise blocked with no substitute.

## Strongest objection

The runtime connector schema already states that inaccessible calendars are returned as per-calendar errors, so a fabricated ID may seem sufficient to confirm the promised behavior cheaply. That verifies only one normalization path and may merely exercise `notFound`; it does not establish permission semantics, partial-result preservation, or parity with the raw API under the authenticated principal and effective scope.

## Falsifier

Revise this card toward `ADMIT` only if a distinct verifier can reproduce all of the following with exact sanitized request-class and response-class bindings:

1. a syntactically valid nonexistent ID yields a typed lookup-failure result;
2. a pre-existing authorized existing-but-unreadable calendar yields a separately typed permission result or a documented indistinguishable result;
3. the same request still returns the `primary` calendar's result without laundering the failed calendar into `busy=[]`;
4. raw `freebusy.query` and connector output agree on success-vs-whole-call-failure and per-calendar error class;
5. connector version/upstream mapping or an immutable runtime schema digest is bound;
6. no retries, fallback calls, calendar-ID retention, busy-timestamp retention, mutation, or downstream scheduling effect occurs.

If an existing-unreadable fixture cannot be obtained without account creation, private-data use, or terms acceptance, the permission claim remains `UNKNOWN`; the nonexistent-ID subtest may still be admitted only as lookup-failure behavior.

## Consumer gate

`X13_GOOGLE_CALENDAR_GET_AVAILABILITY_READONLY_001_PHASE3_AND_ANY_FREEBUSY_WORKITEM`

Consumer must rename the current phase-3 target from generic `inaccessible` to the exact fixture class used, preserve per-calendar errors separately from busy windows, and forbid interpreting an errored calendar's empty busy list as free time.

## Honest flaw

This pass inspected current official documentation, the current X13 queue artifact, and the exposed connector schema only. It did not call Google Calendar, inspect private calendars, create a fixture, observe an HTTP response, bind an OAuth principal/scope, or compare raw API bytes with connector output. The exact permission-denial reason may be intentionally indistinguishable from absence; only an authorized fixture can resolve the connector's actual behavior.
