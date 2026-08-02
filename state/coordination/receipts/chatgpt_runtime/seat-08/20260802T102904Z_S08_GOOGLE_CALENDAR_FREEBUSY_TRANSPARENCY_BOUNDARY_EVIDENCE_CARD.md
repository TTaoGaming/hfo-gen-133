---
schema_id: hfo.gen133.s08.evidence_card.v0_1
seat: S08
callsign: Research and Candidate Scout
expected_task_id: 6a526109ba348191b5f23ad3172ad568
wip: 1
created_utc: 2026-08-02T10:29:04Z
canonical_repo: TTaoGaming/hfo-gen-133
canonical_branch: agent/gen133-bootstrap-20260730
lane: agent_runtime_cots_capabilities
question: Does an empty Google Calendar FreeBusy result prove that no calendar events or obligations exist in the queried interval?
result: REVISE
fitness_credit: 0
consumer:
  - X13_GOOGLE_CALENDAR_FREEBUSY_READONLY_001 phase 2
  - HFO scheduling and executive-assistant planning logic
verifier: distinct nonproducer official-contract review plus controlled non-private transparent-event comparison
expiry: 2026-08-09T10:29:04Z or immediately on Google Calendar API contract or connector-schema change
privacy_class: SANITIZED_PUBLIC
world_effect_ceiling: official public-source read + Git evidence card + one short Slack pointer; no calendar query
---

# S08 evidence card — Google Calendar FreeBusy transparency boundary

## Self-probe

- Carrier identity: S08 Research and Candidate Scout; expected task ID `6a526109ba348191b5f23ad3172ad568` came from the wake packet and was not independently exposed by the connector surface.
- Tools available/used: GitHub exact-branch search/read/write/readback; public web reads of official Google Calendar API documentation; connector-schema inspection for `Google_Calendar.get_availability`; one bounded Slack pointer after Git readback.
- Connector action observed: `Google_Calendar.get_availability`; connector implementation/version, OAuth scope, raw HTTP response, and internal request count are not exposed.
- Duplicate check: no exact Gen-133 evidence card matched the `transparent event versus FreeBusy empty-result` boundary. Prior Calendar cards already excluded least-privilege and completeness claims but did not bind this exact event-transparency semantic.

## Exact candidate and current queue binding

- Candidate surface: `Google_Calendar.get_availability`.
- Upstream contract: Google Calendar API v3 `POST /calendar/v3/freeBusy`.
- Connector version: `UNKNOWN_NOT_EXPOSED`.
- Current experiment: `X13_GOOGLE_CALENDAR_FREEBUSY_READONLY_001`, version `37`, phase `1/4`, at branch path `state/coordination/experiments/cots_connector_x13/CURRENT.md`.
- Current phase-1 receipt: `3a0f163229a9c145373923ce369ccde39420985d` / blob `ea366c0b6657e3f166160996124f708dc90431ae`.

## Bounded finding

**REVISE the interpretation of an empty FreeBusy result from `NO_CALENDAR_OBLIGATIONS` to `NO_BUSY_BLOCKS_RETURNED_FOR_THIS_SOURCE_AND_INTERVAL`.**

Google's FreeBusy contract returns time ranges during which a calendar should be regarded as busy. Separately, the Events resource defines `transparency` as whether an event blocks time: `opaque` blocks time and `transparent` does not. Google requires working-location events to be transparent, while focus-time and out-of-office status events are opaque.

Therefore, as a contract-level inference, an empty `busy[]` array does **not** prove that the interval contains no events, statuses, reminders, working-location records, birthdays, or operator obligations. It proves only that this call returned no blocking busy ranges for the queried calendar selector and interval, subject to permissions and connector completeness.

This distinction is material for X13 phase 2: FreeBusy is appropriate for finding potentially bookable time, but it must not be used alone to reconcile whether every calendar obligation or status record is absent.

## Dated primary/current sources

1. Google Calendar API v3, `Freebusy: query`, last updated 2026-05-12 UTC; read 2026-08-02. The response `busy[]` is defined as ranges during which the calendar should be regarded as busy. https://developers.google.com/workspace/calendar/api/v3/reference/freebusy/query
2. Google Calendar API v3, `Events` resource, last updated 2026-07-07 UTC; read 2026-08-02. `transparency=opaque` blocks time; `transparency=transparent` does not. https://developers.google.com/workspace/calendar/api/v3/reference/events
3. Google Calendar API guide, `Manage focus time, out of office, and working location events`, last updated 2026-04-20 UTC; read 2026-08-02. Focus time and out of office require opaque transparency; working location requires transparent transparency. https://developers.google.com/workspace/calendar/api/guides/calendar-status
4. Live connector schema inspected 2026-08-02: `Google_Calendar.get_availability` returns busy windows only, not event titles/details, and exposes inaccessible calendars as per-calendar errors. Connector version and raw upstream contract binding are not exposed.
5. Gen-133 X13 current experiment version 37, read on canonical branch 2026-08-02: one empty one-hour primary-alias result is already bounded as not proving completeness or scheduling authority.

## Supported claims

- FreeBusy is an availability/blocking-time surface, not a complete event inventory.
- `opaque` events block time; `transparent` events do not block time under the documented Events resource contract.
- Working-location status events are explicitly transparent; focus-time and out-of-office status events are explicitly opaque.
- An empty FreeBusy response cannot honestly be relabeled as proof of `no events` or `no obligations`.
- The current connector schema is consistent with the lower-privacy availability use case because it returns busy windows rather than event content.

## Excluded claims

- No claim that every transparent event type is omitted in every live connector response; no controlled live comparison was run.
- No claim about declined, tentative, cancelled, private, all-day, birthday, recurring, secondary-calendar, delegated, or permission-limited event behavior beyond the cited contract.
- No claim that an empty result proves the user is actually free, willing, reachable, awake, or authorized to accept a meeting.
- No claim that FreeBusy sees every relevant calendar, account, task list, email obligation, or offline commitment.
- No claim of connector least privilege, exact OAuth scope, connector version, raw request count, quota use, billing safety, or independent accuracy.
- No calendar query, event read, event creation, account action, private-data use, outreach, or scheduling mutation occurred.

## License / terms uncertainty

- Google developer documentation states page content is licensed under Creative Commons Attribution 4.0 and code samples under Apache 2.0; this card paraphrases contract text and copies no sample implementation.
- Google API Terms of Service, Workspace customer terms, OAuth consent, data-processing obligations, retention rules, and connector-provider terms were not accepted or fully audited in this run.
- The live connector implementation, version, source license, and provider-to-Google contract are not exposed. This card admits only the observed schema plus official upstream semantics, not implementation equivalence.

## Cost and operator-minute estimate

- Surfaced paid cost for this research run: `$0`.
- Operator minutes required now: `0`.
- Potential operator-minute effect: applying the wording gate can prevent a false `no obligations` conclusion during a bounded availability check, plausibly avoiding `1-5 minutes` of mistaken rescheduling or follow-up per affected check. This is an S08 estimate and is unvalidated.
- A separate event-inventory or obligation-reconciliation path would add privacy review and operator time; estimate `2-10 minutes` per bounded reconciliation until measured. No aggregate savings claim is admitted.

## Strongest objection

For ordinary meeting scheduling, transparent events are intentionally marked available, so treating them as non-blocking is correct and an empty FreeBusy result may be exactly the desired answer.

**Answer:** agreed for the narrow question `is this interval reported as bookable?`. The objection fails only when the result is promoted to `there are no events or obligations`. Keep FreeBusy as the default low-privacy scheduling primitive, but bind its output to availability semantics only.

## Falsifier

This card should be revised or retired if either occurs:

1. An official Google Calendar source states that transparent events are included in FreeBusy busy ranges despite not blocking time; or
2. A controlled, non-private test calendar with one known transparent event shows `Google_Calendar.get_availability` returning that event as a busy interval, proving connector-specific transformation beyond the documented upstream semantics.

## Verification and consumption gate

- Verifier: a distinct nonproducer reopens the three official Google sources and confirms the busy-range and transparency semantics.
- Strong verifier: compare one known transparent event and one known opaque event in an authorized non-private test calendar using both the live connector and raw Google Calendar API for the exact same RFC3339 interval.
- Consumer: X13 phase 2 or HFO scheduling logic must explicitly consume this card.
- Suggested WorkItem: `X13_FREEBUSY_AVAILABILITY_NOT_OBLIGATION_GATE`.
- Required wording:
  - allowed: `No busy blocks were returned for this calendar selector and interval.`
  - forbidden without separate evidence: `There are no calendar events or obligations in this interval.`
- Fitness credit remains `0` until exact WorkItem consumption and ConsumerAck.

## Decision

`REVISE`

Admission ceiling: **use FreeBusy as a bounded, low-content availability signal; do not use an empty result as a complete event or obligation absence claim.**
