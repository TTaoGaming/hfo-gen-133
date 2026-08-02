---
schema_id: hfo.gen133.x13.cots_connector_event.v1
experiment_id: X13_GOOGLE_CALENDAR_FREEBUSY_READONLY_001
event_type: PHASE_3_FAILURE_PERMISSION_PORTABILITY_PROBE
phase: 3_of_4
prior_current_version: 38
next_current_version: 39
valid_time_utc: 2026-08-02T11:47:24Z
carrier_task_id: 6a55c1733708819185088bf334e33ea5
write_side_effect: false
sealed: true
---

# Google Calendar Freebusy phase 3

A single read-only query used a synthetic calendar identifier under a reserved invalid domain. The exact identifier is omitted.

Direct receipt:
- top-level error: none
- per-calendar error: `global/notFound`
- busy intervals: 0
- call time: 2208 ms
- retry: none
- event content returned: no
- calendar mutation: no
- surfaced cost: $0
- measured operator minutes removed: 0

Finding: the connector preserved a resource-scoped error while the overall call completed. Callers must inspect each calendar's error field; top-level success plus an empty busy list does not mean available time.

Official Google documentation says `notFound` can mean a resource does not exist or the caller cannot access it. This probe cannot distinguish those cases.

Gates:
1. Treat per-calendar errors as unknown availability, never as free time.
2. Keep successful and failed calendars separate.
3. Do not retry deterministic `notFound` without corrected identity or access evidence.
4. Handle unknown future error reasons safely.
5. Sanitize calendar identifiers and busy patterns before persistence.

Custom code avoided estimate remains 40-120 LOC for request and result normalization plus 20-60 LOC for interval validation; unvalidated. Identity, authorization scope, project, quota, headers, and independent verification remain unknown.

Verifier: raw Calendar Freebusy API or a distinct authorized client using the same interval and source-bound calendar ID.

Strongest falsifier: a distinct client gives a materially different busy/error result, or a mixed success/error query is collapsed into misleading global success.

Honest flaw: this used a synthetic invalid ID, not a known inaccessible calendar, and did not test mixed calendars, rate limits, transient failures, or independent readback.

Result: `PHASE3_ACCEPTED_WITH_PER_CALENDAR_ERROR_AND_NONENUMERATION_GATES`.
