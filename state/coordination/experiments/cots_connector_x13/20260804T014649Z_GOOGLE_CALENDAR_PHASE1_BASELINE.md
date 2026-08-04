---
schema_id: hfo.gen133.x13.cots_connector_event.v1
event_id: X13_GOOGLE_CALENDAR_FREEBUSY_READONLY_001_PHASE1_BASELINE_20260804T014649Z
experiment_id: X13_GOOGLE_CALENDAR_FREEBUSY_READONLY_001
carrier_task_id: 6a55c1733708819185088bf334e33ea5
carrier_task_id_match: true
wip: 1
candidate: Google_Calendar_get_availability_bounded_readonly_freebusy_surface
phase: 1_of_4
event_type: OFFICIAL_CONTRACT_AND_DIRECT_CAPABILITY_BASELINE
disposition: PHASE1_ACCEPTED_WITH_GATES
valid_time_utc: 2026-08-04T01:46:49Z
recorded_time_utc: 2026-08-04T01:46:49Z
prior_current_version: 76
next_current_version: 77
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

# X13 Google Calendar bounded free/busy — Phase 1

One `Google_Calendar.get_availability` call completed for `primary` over a one-minute RFC3339 interval, with response timestamps requested in `America/Denver`.

## Measured result

| Measure | Observed |
|---|---:|
| Calendar identifiers requested | 1 |
| Query duration | 60 seconds |
| Calendar results returned | 1 |
| Busy-window cardinality | 1 |
| Per-calendar errors | 0 |
| Event titles, descriptions, attendees, locations, or event IDs returned | 0 |
| Connector-visible error | None |
| Connector-reported external-call time | 149 ms |
| Retries / fallbacks / mutations | `0 / 0 / 0` |
| Surfaced paid cost | $0 |
| Measured operator minutes removed | 0 |

Exact query and busy timestamps are intentionally omitted from this durable receipt. No Calendar write occurred.

## Official contract

Google documents `freebusy.query` as `POST /calendar/v3/freeBusy` with RFC3339 bounds, optional response time zone, calendar/group identifiers, per-calendar busy intervals, and per-calendar errors such as `notFound` and `internalError`. The method supports narrow free/busy authorization as well as broader Calendar read or full access.

Primary references:
- https://developers.google.com/workspace/calendar/api/v3/reference/freebusy/query
- https://developers.google.com/workspace/calendar/api/auth
- https://developers.google.com/workspace/calendar/api/guides/quota

Google's 2026-05-01 quota page lists per-minute project and per-user/project limits and says standard use has no additional cost below the published daily threshold. This connector exposed no raw request status, headers, request identifier, effective authorization, project allocation, quota counters, or upstream attempt count.

## Dimensions

- Custom code avoided: estimated `20–70 LOC`, unvalidated, for authenticated request construction, RFC3339 validation, response normalization, and per-calendar error parsing.
- Operator minutes: `0` measured; any future `1–3 minute` estimate remains unvalidated.
- Credentials: connector-managed and uninspected; principal and effective permission remain unknown.
- Durability: Git receipt durable; provider response was an ephemeral observation with no raw provider receipt.
- Observability: bounded inputs, result count, busy cardinality, errors, and 149 ms connector latency visible; raw transport and quota telemetry hidden.
- Portability: medium for abstract free/busy and RFC3339; lower across providers for identifiers, ACLs, error shapes, time zones, and quotas.
- Failure behavior: not directly probed. Official responses may carry per-calendar errors inside an otherwise completed request.
- Direct cost/quota evidence: no charge surfaced; actual request count and quota consumption unknown.

## Gates

1. Prefer free/busy over event search when only availability is needed.
2. Require explicit small RFC3339 bounds and explicit response time zone.
3. Query the minimum calendar set; one known calendar for probes.
4. Inspect each calendar's error field even when the outer call succeeds.
5. Do not durably log exact busy timestamps or calendar identifiers without a named consumer and retention need.
6. Do not infer event content or cause from a busy interval.
7. Do not infer least privilege, exact upstream method count, quota use, or absence of hidden retries from success.
8. Require consumer acknowledgment and measured outcome before operational or fitness credit.

## Strongest falsifier

A distinct authorized raw `freebusy.query` for the same principal and a contemporaneous one-minute interval returns materially different busy cardinality or per-calendar errors, or shows that the connector widened the interval, changed calendar identity, substituted another method, retried invisibly, or used a different quota class.

## Verifier

Run a distinct authorized raw `freebusy.query` with one known calendar and a new one-minute interval. Capture principal, effective permission, exact request body, raw status and headers, request identifier, response bounds, per-calendar cardinality and errors, quota telemetry, and zero-retry evidence. Discard exact busy timestamps after comparison.

## Consumer

- Immediate: `HFO_COTS_CAPABILITY_INVENTORY`
- Future operational consumer: must be named in a new work item.

## Honest flaw

Only one primary-calendar, one-minute query succeeded. Exact-time parity was not independently verified. Identity, least privilege, inaccessible-calendar behavior, time-zone edge cases, per-calendar error preservation, raw API parity, actual quota use, hidden retries, consumer acknowledgment, and operator-time reduction remain unverified.

## Next wake

Phase 2: one separately bounded one-minute free/busy micro-use, without event-content hydration, retry, window widening, or mutation.