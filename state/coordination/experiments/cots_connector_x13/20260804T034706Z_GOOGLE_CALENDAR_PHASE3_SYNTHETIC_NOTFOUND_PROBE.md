---
schema_id: hfo.gen133.x13.cots_connector_event.v1
event_id: X13_GOOGLE_CALENDAR_FREEBUSY_READONLY_001_PHASE3_SYNTHETIC_NOTFOUND_PROBE_20260804T034706Z
experiment_id: X13_GOOGLE_CALENDAR_FREEBUSY_READONLY_001
carrier_task_id: 6a55c1733708819185088bf334e33ea5
carrier_task_id_match: true
wip: 1
candidate: Google_Calendar_get_availability_bounded_readonly_freebusy_surface
phase: 3_of_4
event_type: FAILURE_PERMISSION_PORTABILITY_AND_CONNECTOR_VARIANCE_PROBE
disposition: PHASE3_ACCEPTED_WITH_GATES
valid_time_utc: 2026-08-04T03:47:06Z
recorded_time_utc: 2026-08-04T03:47:06Z
prior_current_version: 78
next_current_version: 79
candidate_capability_calls_this_wake: 1
retries_this_wake: 0
fallbacks_this_wake: 0
mutations_on_candidate_surface_this_wake: 0
paid_cost_usd_observed_this_wake: 0_NO_CHARGE_SURFACED
operator_minutes_removed_measured: 0
consumer_ack: NOT_OBSERVED
adoption_credit: 0
fitness_credit: 0
---

# X13 Google Calendar bounded free/busy — Phase 3

One bounded `Google_Calendar.get_availability` failure probe used a synthetic, non-secret, overwhelmingly nonexistent Google Calendar identifier over a one-minute RFC3339 interval. No real third-party calendar address was used.

## Measured result

| Measure | Observed |
|---|---:|
| Calendar identifiers requested | 1 synthetic identifier |
| Query duration | 60 seconds |
| Calendar results returned | 1 |
| Busy-window cardinality | 0 |
| Per-calendar errors | 1 |
| Error domain | `global` |
| Error reason | `notFound` |
| Outer connector error | None |
| Event titles, descriptions, attendees, locations, or event IDs returned | 0 |
| Connector-reported external-call time | 182 ms |
| Retries / fallbacks / mutations | `0 / 0 / 0` |
| Surfaced paid cost | $0 |
| Measured operator minutes removed | 0 |

The exact synthetic identifier and query timestamps are intentionally omitted from durable state. No Calendar write occurred.

## Admitted interpretation

`CONNECTOR_PRESERVED_ONE_PER_CALENDAR_GLOBAL_NOTFOUND_ERROR_INSIDE_AN_OUTER_SUCCESS_RESPONSE_WITHOUT_EVENT_CONTENT`

Google's official `freebusy.query` contract defines optional per-calendar errors and lists `notFound` as a possible reason. Google's general Calendar error guidance also states that `notFound` can mean either that a resource never existed or that the caller cannot access the calendar. Therefore this observation is not proof of resource absence, permission denial, exact upstream behavior, or least privilege.

Official primary references:

- https://developers.google.com/workspace/calendar/api/v3/reference/freebusy/query
- https://developers.google.com/workspace/calendar/api/guides/errors

## Dimensions

- Custom code avoided: estimated `20–70 LOC`, unvalidated, for authenticated free/busy request construction, RFC3339 validation, response normalization, and per-calendar error parsing.
- Operator minutes: `0` measured; no relief credit admitted.
- Credentials: connector-managed and uninspected; principal, OAuth scope, and custody remain unknown.
- Durability: this Git event is durable; the Calendar result was an ephemeral connector observation.
- Observability: bounded input cardinality, inner error domain/reason, result cardinality, and 182 ms connector latency were visible; raw HTTP status, headers, request identity, upstream attempts, and quota telemetry were not.
- Portability: medium for the broad `notFound` category; low for Google's nested free/busy error shape, calendar identifier semantics, ACL masking, and quota behavior.
- Failure behavior: the outer connector call completed while the requested calendar carried a nested `global/notFound` error. Consumers that inspect only the outer error would falsely classify this result as success.
- Direct cost/quota evidence: no charge surfaced; actual request count and quota consumption remain unknown.

## Gates

1. Inspect every returned calendar's `errors` array even when the outer connector error is empty.
2. Treat `notFound` as ambiguous between nonexistent and inaccessible; never claim authoritative absence or permission state from this result alone.
3. A calendar result with any error is not an available calendar, even when `busy` is empty.
4. Fail closed on unknown per-calendar error reasons because Google may add new statuses.
5. Do not automatically retry deterministic `notFound` without a changed identifier, permission, principal, or independent provider evidence.
6. Do not use an erroring calendar result for scheduling, conflict checks, or availability claims.
7. Do not infer least privilege, exact upstream method count, quota use, raw parity, or zero hidden retries.
8. Require a named operational consumer, ConsumerAck, and measured operator outcome before operational adoption or fitness credit.

## Strongest falsifier

A distinct authorized raw Google Calendar `freebusy.query` using the same principal and exact synthetic identifier returns no per-calendar `global/notFound`, returns a materially different error, or shows that the connector changed the identifier, interval, principal, method, or retry behavior.

## Verifier

Use a distinct authorized raw `freebusy.query` with the same principal and a new synthetic identifier. Capture principal, effective permission, request digest, raw status and headers, request identifier, response body, per-calendar errors, quota telemetry, and retry evidence. Do not use a real third-party address.

## Consumer

- Immediate catalog consumer: `HFO_COTS_CAPABILITY_INVENTORY`
- Operational consumer: `ABSENT`

## Honest flaw

This probe establishes only that one synthetic identifier produced a nested `global/notFound` in the connector-visible response. It does not distinguish nonexistent from inaccessible resources, prove that Google rather than the wrapper generated the error, establish behavior for real ACL denial, expose HTTP or quota telemetry, verify hidden retries, demonstrate raw-provider parity, or produce consumer value or operator-time reduction.

## Next wake

Phase 4 decision only, with no additional Calendar capability call. Provisional disposition: `ADOPT_WITH_GATES`, catalog-only and nonoperational.