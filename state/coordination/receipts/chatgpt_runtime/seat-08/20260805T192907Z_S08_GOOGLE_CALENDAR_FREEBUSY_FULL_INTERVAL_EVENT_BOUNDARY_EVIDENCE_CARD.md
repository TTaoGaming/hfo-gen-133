---
schema_id: hfo.gen133.s08.evidence_card.v1
seat: S08_RESEARCH_AND_CANDIDATE_SCOUT
carrier_task_id_expected: 6a526109ba348191b5f23ad3172ad568
carrier_task_id_observed: 6a526109ba348191b5f23ad3172ad568
carrier_task_id_match: true
wip: 1
lane: agent-runtime/COTS_capabilities
question_id: X13_GOOGLE_CALENDAR_FREEBUSY_FULL_INTERVAL_EVENT_BOUNDARY_001
valid_time_utc: 2026-08-05T19:29:07Z
transaction_time_utc: SEE_GIT_COMMIT_METADATA
canonical_repository: TTaoGaming/hfo-gen-133
canonical_branch: agent/gen133-bootstrap-20260730
candidate: Google_Calendar.get_availability
candidate_upstream: Google Calendar API v3 freebusy.query
candidate_connector_version: NOT_EXPOSED
upstream_reference_last_updated_utc: 2026-05-12
upstream_sharing_reference_last_updated_utc: 2026-07-09_OR_LATER_PAGE_OBSERVED_2026-08-05
queue_source_commit: de98cb17ab02c66296d535c2fe95b0c267cbe161
queue_source_path: state/coordination/experiments/cots_connector_x13/20260805T184911Z_GOOGLE_CALENDAR_FREEBUSY_PHASE2_ACCEPTED_WITH_GATES.md
queue_source_blob_sha1: 34ffabb36dca50bfe773d91f3aee87261c10ee5f
queue_current_version: 118
decision: REVISE
consumer: X13_GOOGLE_CALENDAR_FREEBUSY_READONLY_005_PHASE4_DECISION_AND_HFO_COTS_CAPABILITY_INVENTORY
verifier: DISTINCT_AUTHORIZED_SYNTHETIC_CALENDAR_RAW_FREEBUSY_AND_CONNECTOR_NONINJECTIVITY_VERIFIER
expiry_utc: 2026-08-12T19:29:07Z
fitness: 0_PENDING_EXACT_WORKITEM_CONSUMPTION_AND_CONSUMER_ACK
sealed: false
---

# S08 evidence card — a full-query busy window is occupancy evidence, not an event boundary

## Bounded uncertainty

X13 phase 2 recorded one returned busy window whose bounds exactly matched the fifteen-minute query interval on two wrapper calls. Does that establish that exactly one underlying event starts and ends at those same timestamps, or otherwise preserve event count and event boundaries?

## Decision

`REVISE`

Treat the observation only as **full queried-interval occupancy**. The public FreeBusy contract returns time ranges during which a calendar should be regarded as busy; it does not return event IDs, event count, summaries, event types, or a documented one-busy-range-to-one-event mapping. A busy range matching `timeMin` and `timeMax` therefore does not establish that one event has those exact boundaries, that only one event exists, or that busy time does not continue outside the query interval.

Required semantic label:

```text
RETURNED_BUSY_WINDOW_RELATION=EXACT_FULL_QUERY_INTERVAL_MATCH
ADMITTED_MEANING=CALENDAR_REGARDED_BUSY_FOR_THE_FULL_QUERIED_INTERVAL
UNDERLYING_EVENT_COUNT=UNKNOWN
UNDERLYING_EVENT_START_END=UNKNOWN
BUSY_OUTSIDE_QUERY_INTERVAL=UNKNOWN
ONE_BUSY_WINDOW_EQUALS_ONE_EVENT=FORBIDDEN
```

## Changed queue evidence read on 2026-08-05

The changed X13 phase-2 event at commit `de98cb17ab02c66296d535c2fe95b0c267cbe161` records:

- query interval: `2026-08-05T11:45:00-06:00` to `2026-08-05T12:00:00-06:00`;
- returned calendars: `1`;
- returned busy windows: `1`;
- relation: `EXACT_FULL_QUERY_INTERVAL_MATCH`;
- phase-1/phase-2 match: `true`;
- no event titles or details returned;
- raw provider response not persisted;
- raw Google parity, effective security context, and general behavior remain unverified.

This is a newly material boundary because the exact full-query match can be misread downstream as an event-boundary or single-event claim even though the producer currently intends only wrapper repeatability.

## Current primary evidence checked on 2026-08-05

1. Google Calendar API v3 `freebusy.query`, last updated 2026-05-12 UTC:
   https://developers.google.com/workspace/calendar/api/v3/reference/freebusy/query
2. Google Calendar sharing and ACL concepts, current page checked 2026-08-05:
   https://developers.google.com/workspace/calendar/api/concepts/sharing
3. Runtime connector schema observed in this wake for `Google_Calendar.get_availability`: accepts explicit calendar IDs and RFC3339 bounds, returns busy windows only, reports inaccessible calendars as per-calendar errors, and states that `response_timezone_str` controls response formatting rather than the query interval. Connector build, upstream mapping, normalization behavior, effective OAuth principal, and raw response are not exposed.

## Supported claims

- Raw `freebusy.query` returns `busy[]` ranges for periods during which the calendar should be regarded as busy.
- Each returned range uses an inclusive start and exclusive end.
- The request itself defines `timeMin` and `timeMax`; the response also carries the query interval.
- A `freeBusyReader` may see whether a calendar is free or busy without access to event details.
- The connector surface promises busy windows only, not event titles or details.
- For the observed wrapper result, the calendar was represented as busy across the full requested fifteen-minute interval on two calls.

## Excluded claims

- One returned busy range represents exactly one underlying event.
- The underlying event begins at `timeMin` or ends at `timeMax`.
- Busy time does not extend before `timeMin` or after `timeMax`.
- Multiple overlapping, adjacent, recurring, private, focus-time, out-of-office, or other busy-producing records cannot collapse to the same returned interval.
- `returned_busy_windows: 1` is an event count.
- The connector preserves raw Google segmentation, clipping, merging, ordering, or event provenance.
- Two matching calls establish immutable historical truth or event-level repeatability.

Google's public reference does not document a one-to-one event mapping, nor does it specify enough normalization detail to infer whether overlapping or adjacent sources are merged or whether wider busy periods are clipped at query bounds. Those behaviors remain `UNKNOWN` until a controlled authorized fixture is compared against raw API output.

## Required phase-4 revision

Keep the existing exact relation field, but bind it to an explicit semantic class:

- `FULL_QUERY_OCCUPANCY_ONLY=true`
- `EVENT_BOUNDARY_INFERENCE_FORBIDDEN=true`
- `EVENT_COUNT_INFERENCE_FORBIDDEN=true`
- `BUSY_OUTSIDE_QUERY_UNKNOWN=true`
- `RAW_SEGMENTATION_PARITY=UNKNOWN`

Any scheduling consumer may use the interval only to reject or review the queried slot as occupied. It must not generate event records, infer a meeting, identify a person or purpose, count events, or estimate duration outside the queried window.

## License and terms uncertainty

- Google developer documentation is published under CC BY 4.0 unless otherwise stated; code samples are Apache 2.0.
- Calendar API, OAuth, Workspace user-data, retention, and connector-specific terms were not fully evaluated in this card.
- Connector versioning, telemetry, data retention, normalization, and provider-request mapping remain `UNKNOWN`.
- No source code or documentation text is redistributed as a product in this pass.

## Cost and operator-minute estimate

- This research pass: `$0` external spend; `0` operator minutes.
- Amend phase-4 schema and wording: `5–10` producer minutes.
- Controlled non-injectivity fixture design and sanitized receipt: `20–45` producer minutes plus `20–45` distinct-verifier minutes, only if pre-existing authorized synthetic calendars and principals are available.
- If such fixtures do not already exist, record `BLOCKED_AUTHORIZED_SYNTHETIC_FIXTURE_NOT_AVAILABLE`; do not create accounts, calendars, or events under this WorkItem.

## Strongest objection

The phase-2 artifact already says no event details were returned and claims only wrapper-level repeatability, so no current producer overclaim exists. Correct. The risk is downstream semantic laundering: `one busy window` plus `exact full query interval match` is structurally easy to reinterpret as one exact event. The schema needs an explicit non-event semantic before catalog consumption.

## Falsifier

Revise this card toward `ADMIT` for event-boundary use only if a version-bound official contract or a distinct authorized verifier establishes a stable one-to-one mapping between returned busy ranges and underlying events. A controlled verifier should compare raw Google FreeBusy and connector output across pre-existing synthetic fixtures representing:

1. one event exactly equal to the query interval;
2. one event strictly wider than the query interval;
3. two overlapping events whose union covers the interval;
4. two adjacent busy-producing records whose union covers the interval.

If materially different underlying fixtures produce the same one-range full-query result, event count and event boundary recovery are non-injective and must remain forbidden. The verifier must bind exact request classes, raw and connector result classes, effective authorized principal, immutable schema/version digest, zero mutation in this WorkItem, and sanitized retention.

## Consumer gate

`X13_GOOGLE_CALENDAR_FREEBUSY_READONLY_005_PHASE4_DECISION_AND_HFO_COTS_CAPABILITY_INVENTORY`

Consumer may admit only the capability: **bounded occupancy lookup for explicit calendars and explicit intervals**. It must exclude event reconstruction, event counting, duration extrapolation beyond the query, and unattended scheduling decisions.

## Honest flaw

This pass inspected the changed phase-2 queue artifact, current official Google documentation, and the exposed connector schema. It did not call Google Calendar, inspect private calendar data, create fixtures, observe raw HTTP responses, bind the effective OAuth principal or scopes, or determine actual clipping/merging behavior. The exact normalization behavior therefore remains unknown; the decision is a conservative semantic boundary, not a claim about Google's undocumented implementation.
