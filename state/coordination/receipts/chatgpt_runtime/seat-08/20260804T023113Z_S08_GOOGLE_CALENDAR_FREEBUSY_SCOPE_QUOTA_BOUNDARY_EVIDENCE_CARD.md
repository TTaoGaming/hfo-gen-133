---
schema_id: hfo.gen133.research_evidence_card.v1
card_id: S08_GOOGLE_CALENDAR_FREEBUSY_SCOPE_QUOTA_BOUNDARY_20260804T023113Z
carrier_task_id: 6a526109ba348191b5f23ad3172ad568
carrier_task_id_match: true
wip: 1
lane: agent_runtime_cots_capabilities
question: Can the current Google_Calendar.get_availability connector be admitted as a least-privilege, bounded-cost free/busy primitive for X13 phase 2?
question_source:
  repository: TTaoGaming/hfo-gen-133
  commit: 2cefeaaded9f99372b48cbe89bd6173e05d231a6
  path: state/coordination/experiments/cots_connector_x13/20260804T014649Z_GOOGLE_CALENDAR_PHASE1_BASELINE.md
candidate: Google_Calendar.get_availability connector contract
candidate_version: VERSION_NOT_EXPOSED_SCHEMA_OBSERVED_2026-08-04
verdict: REVISE
valid_time_utc: 2026-08-04T02:31:13Z
expiry_utc: 2026-08-11T02:31:13Z
consumer:
  - X13_GOOGLE_CALENDAR_FREEBUSY_READONLY_001_PHASE2
  - HFO_COTS_CAPABILITY_INVENTORY
verifier: distinct authorized raw Google Calendar API operator or non-S08 connector verifier
fitness_credit: 0_PENDING_WORKITEM_CONSUMPTION
---

# REVISE — connector is bounded at the response surface, but least privilege and quota class are not bound

## Bounded uncertainty

The X13 phase-1 baseline proved one successful one-calendar, one-minute connector call but left effective OAuth scope, raw upstream request count, quota class, hidden retries, and expansion behavior unknown. This card tests whether current official contracts close those gaps without another private Calendar read.

## Exact candidate and current contracts

- **Connector:** `Google_Calendar.get_availability`; implementation version and license are not exposed. Runtime schema observed 2026-08-04 accepts only `calendar_ids[]`, explicit RFC3339 `time_min`/`time_max`, and an IANA response time zone. It promises busy windows only and per-calendar errors for inaccessible calendars.
- **Google API:** `POST https://www.googleapis.com/calendar/v3/freeBusy`, reference last updated 2026-05-12 UTC.
- **Question source:** X13 phase-1 receipt at commit `2cefeaaded9f99372b48cbe89bd6173e05d231a6`.

## Primary dated sources

1. Google Calendar `freebusy.query`, last updated 2026-05-12 UTC: https://developers.google.com/workspace/calendar/api/v3/reference/freebusy/query
2. Google Calendar OAuth scopes, last updated 2026-04-23 UTC: https://developers.google.com/workspace/calendar/api/auth
3. Google Calendar usage limits, effective 2026-05-01 and observed 2026-08-04: https://developers.google.com/workspace/calendar/api/guides/quota
4. Google Calendar sharing and `freeBusyReader`, observed 2026-08-04: https://developers.google.com/workspace/calendar/api/concepts/sharing

## Supported claims

1. The exposed connector contract is data-minimizing relative to event search: it returns busy intervals, not titles, descriptions, attendees, locations, or event IDs.
2. The official method accepts narrow free/busy scopes: `calendar.freebusy` and `calendar.events.freebusy`. It also accepts broader `calendar.readonly` and full `calendar`; method success therefore does **not** prove least privilege.
3. The official method caps `calendarExpansionMax` at 50 and `groupExpansionMax` at 100, and can return `groupTooBig`, `tooManyCalendarsRequested`, `notFound`, `internalError`, plus future error reasons.
4. Current documented default quotas for newly governed projects are 10,000 requests/minute/project, 600 requests/minute/user/project, and a 1,000,000-request/day/project no-extra-charge threshold.
5. Projects that used the API between November 2025 and April 2026 can retain prior quota settings. The connector's underlying project age and quota class are not exposed.
6. Calendar ACL role `freeBusyReader` can permit availability access without event-detail access; ACL capability and OAuth scope are separate controls and neither is proven by one successful call.

## Excluded or unsupported claims

- The connector currently uses `calendar.freebusy` or any other exact OAuth scope.
- The connector makes exactly one upstream request, performs no hidden retry, and sends no broader request than the visible schema.
- The connector accepts or expands Google Group identifiers; its exposed schema describes calendar IDs, coworker IDs, and room/resource IDs but exposes no group-expansion controls.
- The connector's project is under the post-2026-05-01 quota model, has any exact remaining quota, or will remain free at a stated workload.
- A completed outer call implies every calendar succeeded; per-calendar errors remain mandatory to inspect.
- A busy interval reveals event purpose, participant identity, or buyer/operator intent.

## License and terms uncertainty

Google documentation is published under CC BY 4.0 and code samples under Apache 2.0 as stated on the reference pages. The connector implementation license, provider agreement, data-processing path, token retention, effective consent grant, and commercial terms are not exposed in this carrier. No account, OAuth grant, terms acceptance, or private Calendar read occurred.

## Decision and required revision

**REVISE** X13 phase 2 rather than admitting a generic least-privilege/bounded-cost primitive:

1. Use exactly one explicit known calendar ID for the next micro-use; prohibit group identifiers and implicit expansion.
2. Keep explicit small RFC3339 bounds and explicit response time zone.
3. Treat each per-calendar error as first-class output even when the connector call completes.
4. Do not claim least privilege until existing connector authorization metadata binds the effective OAuth scopes.
5. Do not claim a quota class, request count, hidden-retry count, or zero marginal cost without connector/provider telemetry.
6. Preserve only aggregate cardinality/error evidence in Git; do not persist calendar IDs or exact busy timestamps.

## Cost and operator-minute estimate

- This research wake: **$0 direct spend; 0 operator minutes**.
- X13 phase-2 connector micro-use: estimated **1–3 producer minutes**, **0–2 operator minutes**, and one connector call; unmeasured until executed.
- Distinct raw-API/scope/quota verification: estimated **15–30 verifier minutes** and **5–10 operator minutes** if existing authorization metadata is available; no new account or grant should be created for the assay.

## Strongest objection

This is documentation-level evidence and does not inspect the connector's private implementation or credentials. It cannot prove that the connector obeys the visible schema internally, uses a narrow scope, avoids retries, or belongs to the documented default quota class.

## Falsifier

A connector/provider trace for the same candidate shows any of the following: a broader effective scope than required, group expansion, interval widening, multiple upstream attempts, suppressed per-calendar errors, event-detail hydration, or a different quota/billing class than assumed. Conversely, exact authorization metadata plus raw provider telemetry proving narrow scope, one request, explicit IDs only, preserved errors, and the active quota class would support promotion to `ADMIT` for the bounded micro-use.

## Verifier

A distinct authorized verifier should use existing credentials only and bind:

- effective OAuth scope/grant metadata;
- connector request body or equivalent raw provider trace;
- exact upstream attempt count and retry behavior;
- project quota class and visible quota accounting;
- one explicit-calendar success and one inaccessible-calendar typed-error specimen;
- proof that no event-detail fields are returned or durably retained.

Private identifiers and busy timestamps must be discarded after comparison.

## Consumer and expiry

- Immediate consumer: `X13_GOOGLE_CALENDAR_FREEBUSY_READONLY_001_PHASE2`.
- Inventory consumer: `HFO_COTS_CAPABILITY_INVENTORY`.
- Expiry: `2026-08-11T02:31:13Z`, or earlier if the connector schema, Google scopes, quotas, or provider terms change.
- Credit remains zero until a named WorkItem consumes this exact card and returns a ConsumerAck.

## Honest flaw

No connector execution, OAuth metadata readback, quota-console readback, inaccessible-calendar probe, or raw API comparison occurred. The card narrows the phase-2 claim boundary; it does not independently verify runtime behavior.
