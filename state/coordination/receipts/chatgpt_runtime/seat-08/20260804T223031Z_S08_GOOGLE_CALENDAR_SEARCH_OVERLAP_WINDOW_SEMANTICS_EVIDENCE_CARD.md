---
schema_id: hfo.gen133.s08.research_evidence_card.v1
task_id_expected: 6a526109ba348191b5f23ad3172ad568
task_id_observed: 6a526109ba348191b5f23ad3172ad568
task_id_match: true
seat: S08
wip: 1
lane: agent_runtime_cots_capabilities
question_changed: true
question_source:
  experiment_commit: 9108d7bf0d967d358ad73734fc132111a8ed1489
  experiment_path: state/coordination/experiments/cots_connector_x13/20260804T214704Z_GOOGLE_CALENDAR_SEARCH_EVENTS_PHASE1_BASELINE.md
  structural_delta_commit: 8d334807ad1e58375ee8db0a62db70b9db561a01
bounded_uncertainty: CAN_EXPLICIT_TIME_MIN_AND_TIME_MAX_BE_DESCRIBED_AS_AN_EVENT_START_WINDOW_FOR_GOOGLE_CALENDAR_SEARCH_EVENTS
candidate: Google_Calendar.search_events
candidate_version: NOT_EXPOSED
upstream_candidate: Google Calendar API v3 events.list
upstream_reference_last_updated_utc: 2026-07-29
verdict: REVISE
valid_time_utc: 2026-08-04T22:30:31Z
recorded_time_utc: 2026-08-04T22:30:31Z
expiry_utc: 2026-08-11T22:30:31Z
consumer: X13_GOOGLE_CALENDAR_SEARCH_EVENTS_READONLY_001_PHASE2_AND_ANY_CALENDAR_SEARCH_WORKITEM
verifier: DISTINCT_SYNTHETIC_FIXTURE_WITNESS_COMPARING_CONNECTOR_WITH_SAME_PRINCIPAL_RAW_EVENTS_LIST
fitness_credit: 0_PENDING_WORKITEM_CONSUMPTION_AND_CONSUMER_ACK
paid_cost_usd: 0
operator_minutes_this_card_estimate: 10_to_18
producer_revision_minutes_estimate: 10_to_20
verification_minutes_estimate: 20_to_40
privacy_class: SANITIZED_PUBLIC_PRIMARY_SOURCES_NO_CALENDAR_CALL_NO_EVENT_DATA
---

# REVISE — Calendar bounds describe an overlap window, not an event-start window

## Exact question

Can X13 describe `time_min` and `time_max` on `Google_Calendar.search_events` as selecting events whose **start times fall inside** that interval?

**Answer: no.** For the raw Google Calendar API `events.list` contract, `timeMax` is an exclusive upper bound on an event's **start**, while `timeMin` is an exclusive lower bound on an event's **end**. The resulting predicate is effectively:

```text
event.start < timeMax AND event.end > timeMin
```

That is an event-overlap window. An event may start before `timeMin` and still be returned when it ends after `timeMin`; an event may end after `timeMax` and still be returned when it starts before `timeMax`.

## Supported claims

1. The exposed connector accepts explicit RFC3339 `time_min` and `time_max`, but its version and upstream request mapping are not exposed.
2. Google Calendar API v3 `events.list` documents `timeMax` as an exclusive upper bound on event start time and `timeMin` as an exclusive lower bound on event end time.
3. `maxResults` is a page-size ceiling, not a completeness guarantee; a page may contain fewer events or none despite additional matches, with `nextPageToken` indicating incompleteness.
4. Default ordering is stable but unspecified. Without an exposed `singleEvents` and `orderBy` binding, the first returned event is not evidenced as the earliest chronological event.

## Excluded claims

- `time_min <= event.start < time_max` is **not** the documented filter contract.
- One result inside the requested bounds does not prove its start time lies inside both bounds.
- A zero-result query does not prove that no event starts inside the interval unless connector/raw parity and the exact query contract are independently verified.
- A continuation token does not prove the current page is chronologically ordered.
- This card does not prove the connector calls `events.list`, preserves raw boundary behavior, expands recurring events, or uses a particular effective OAuth scope.

## Required revision

Use the label `calendar_event_overlap_window`, not `event_start_window`. Bind acceptance tests to four synthetic cases:

1. starts before `timeMin`, ends after `timeMin` — expected included;
2. ends exactly at `timeMin` — expected excluded under the documented exclusive bound;
3. starts exactly at `timeMax` — expected excluded;
4. starts before `timeMax`, ends after `timeMax` — expected included.

Record the connector result, same-principal raw `events.list` result, effective scope, request parameters, `singleEvents`, ordering, page token behavior, and hidden call count. Retain no real calendar values.

## Strongest objection

Overlap semantics are usually the desirable behavior for scheduling and availability. Agreed: this is not a reason to retire the connector. It is a reason to name the contract correctly and prevent downstream code from silently treating overlap results as start-time-bounded results.

## Falsifier

A distinct verifier uses an authorized synthetic calendar and demonstrates that the connector consistently implements a different, documented contract—for example, it excludes an event that begins before `timeMin` but ends after it—while the exact connector version and upstream mapping explain that difference.

## License and terms uncertainty

The connector is a managed proprietary COTS surface; connector version, source license, service terms binding, quota attribution, and upstream method are not exposed here. Google's reference documentation is published under CC BY 4.0 and samples under Apache 2.0, but those documentation licenses do not establish connector-runtime terms or authorization scope. No terms were accepted or changed in this pass.

## Sources checked 2026-08-04

- Google Calendar API v3, `Events: list`, last updated 2026-07-29 UTC: https://developers.google.com/workspace/calendar/api/v3/reference/events/list
- Google Calendar pagination guide, last updated 2026-07-16 UTC: https://developers.google.com/workspace/calendar/api/guides/pagination
- Exact X13 baseline: https://github.com/TTaoGaming/hfo-gen-133/blob/9108d7bf0d967d358ad73734fc132111a8ed1489/state/coordination/experiments/cots_connector_x13/20260804T214704Z_GOOGLE_CALENDAR_SEARCH_EVENTS_PHASE1_BASELINE.md

## Effect receipt

No Calendar connector call, event read, private-data access, token retention, account action, task mutation, outreach, application, purchase, send, spend, deployment, merge, or publication occurred. This append-only Git evidence card is the sole repository write before the required Slack pointer.
