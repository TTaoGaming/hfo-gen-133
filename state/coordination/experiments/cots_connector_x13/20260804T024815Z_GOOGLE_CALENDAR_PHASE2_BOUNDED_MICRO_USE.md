---
schema_id: hfo.gen133.x13.cots_connector_event.v1
event_id: X13_GOOGLE_CALENDAR_FREEBUSY_READONLY_001_PHASE2_BOUNDED_MICRO_USE_20260804T024815Z
experiment_id: X13_GOOGLE_CALENDAR_FREEBUSY_READONLY_001
carrier_task_id: 6a55c1733708819185088bf334e33ea5
carrier_task_id_match: true
wip: 1
candidate: Google_Calendar_get_availability_bounded_readonly_freebusy_surface
phase: 2_of_4
event_type: SMALLEST_HARMLESS_READONLY_MICRO_USE
disposition: PHASE2_ACCEPTED_WITH_GATES
valid_time_utc: 2026-08-04T02:48:15Z
recorded_time_utc: 2026-08-04T02:48:15Z
prior_current_version: 77
next_current_version: 78
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

# X13 Google Calendar bounded free/busy — Phase 2

One separately bounded `Google_Calendar.get_availability` call completed for `primary` over a one-minute RFC3339 interval, with response timestamps requested in `UTC`.

## Measured result

| Measure | Observed |
|---|---:|
| Calendar identifiers requested | 1 |
| Query duration | 60 seconds |
| Calendar results returned | 1 |
| Busy-window cardinality | 0 |
| Per-calendar errors | 0 |
| Event titles, descriptions, attendees, locations, or event IDs returned | 0 |
| Connector-visible error | None |
| Connector-reported external-call time | 244 ms |
| Retries / fallbacks / mutations | `0 / 0 / 0` |
| Surfaced paid cost | $0 |
| Measured operator minutes removed | 0 |

Exact query timestamps are intentionally omitted from this durable receipt. No Calendar write occurred.

## Admitted interpretation

`CONNECTOR_RETURNED_ONE_BOUNDED_EMPTY_FREEBUSY_RESULT_WITHOUT_EVENT_CONTENT`

This does not establish authoritative availability, exact request forwarding, least privilege, completeness, raw-provider parity, quota consumption, absence of hidden retries, or consumer value.

## Dimensions

- Custom code avoided: estimated `20–70 LOC`, unvalidated, for authenticated free/busy request construction, RFC3339 validation, response normalization, and per-calendar error parsing.
- Operator minutes: `0` measured; no relief credit admitted.
- Credentials: connector-managed and uninspected; principal, OAuth scope, and custody remain unknown.
- Durability: this Git event is durable; the Calendar result was an ephemeral connector observation.
- Observability: bounded input cardinality, result cardinality, error count, and 244 ms connector latency were visible; raw HTTP, request identity, upstream attempts, and quota telemetry were not.
- Portability: medium for RFC3339 free/busy semantics; lower for provider-specific calendar IDs, ACL behavior, error shapes, time zones, and quota classes.
- Failure behavior: not directly probed in this wake. Empty busy cardinality is a valid completed response, not a failure.
- Direct cost/quota evidence: no charge surfaced; actual request count and quota consumption remain unknown.

## Governance dissent consumed

The advisory S09 vote at `state/coordination/votes/20260804T023252Z_S09_X13_CALENDAR_PHASE2_PURPOSE_BOUND_REVISE.vote.md` recommended avoiding another synthetic read absent a real operational consumer. Its binding weight is recorded as zero. This wake proceeded only within the already-authorized catalog-only phase-2 contract, preserved zero adoption/fitness/operator-relief credit, and did not treat the result as operational evidence.

## Gates

1. Prefer free/busy over event search when only availability is needed.
2. Require explicit small RFC3339 bounds and response time zone.
3. Query the minimum calendar set.
4. Inspect per-calendar errors independently of outer-call success.
5. Treat an empty busy list only as an observation for the exact requested scope and time.
6. Do not durably log exact timestamps or identifiers without a named retention need.
7. Do not infer event content, authoritative availability, least privilege, quota use, raw parity, or zero hidden retries.
8. Require a named operational consumer, ConsumerAck, and measured operator outcome before operational adoption or fitness credit.

## Strongest falsifier

A distinct authorized raw Google Calendar `freebusy.query` using the same principal and contemporaneous bounded interval returns a materially different busy cardinality or error, or shows connector interval widening, calendar identity substitution, hidden retry, broader method use, or a different quota/billing class.

## Verifier

Use a distinct authorized raw `freebusy.query` with one known calendar and a new bounded interval. Capture principal, effective permission, request digest, raw status and headers, request identifier, response bounds, per-calendar cardinality and errors, quota telemetry, and retry evidence. Discard exact timestamps after comparison.

## Consumer

- Immediate catalog consumer: `HFO_COTS_CAPABILITY_INVENTORY`
- Operational consumer: `ABSENT`

## Honest flaw

Two one-minute primary-calendar calls have now completed, but they used different intervals and response time zones and therefore do not establish repeatability. Identity, effective permission, inaccessible-calendar behavior, daylight-saving and timezone edge cases, per-calendar error preservation, raw API parity, actual quota use, hidden retries, consumer acknowledgment, and operator-time reduction remain unverified.

## Next wake

Phase 3: one bounded failure, permission, or connector-variance probe with no retry, fallback, event hydration, interval widening, or mutation. Prefer a synthetic inaccessible or nonexistent calendar identifier only if it does not expose a real third-party address.