---
schema_id: hfo.gen133.x13.cots_connector_event.v1
experiment_id: X13_GCAL_FREEBUSY_READONLY_020
event_type: PHASE3_REQUEST_PREFLIGHT
phase: 3_of_4
candidate: Google_Calendar_get_availability_busy_only
wip: 1
request_descriptor_canonicalization: UTF8_JSON_SORTED_KEYS_COMPACT_SEPARATORS_NO_ASCII_ESCAPING
request_descriptor_sha256: fa8a64dcaf6b49ed8103916e4bc1ee155c49b8da4794250358be86a190d6c5aa
calendar_ids:
  - x13-nonexistent-20260808T0748Z@example.invalid
time_min: 2026-08-08T01:48:00-06:00
time_max: 2026-08-08T02:03:00-06:00
response_timezone_str: America/Denver
expected_probe: SYNTHETIC_NONEXISTENT_OR_INACCESSIBLE_CALENDAR
mutation_allowed: false
retry_allowed: false
event_detail_fetch_allowed: false
interpretation_gate: ONLY_DISTINGUISH_PER_CALENDAR_ERROR_OR_EMPTY_SUCCESS_FROM_TRANSPORT_OR_CONNECTOR_ERROR;NO_AUTHORIZATION_COMPLETENESS_OR_CORPUS_WIDE_CLAIM
valid_time_utc: 2026-08-08T07:48:00Z
recorded_time_utc: 2026-08-08T07:48:00Z
---

# X13 Calendar FreeBusy Phase 3 Request Preflight

Exact privacy-safe request preimage persisted before issuing the candidate call.

Canonical request JSON:

```json
{"calendar_ids":["x13-nonexistent-20260808T0748Z@example.invalid"],"response_timezone_str":"America/Denver","time_max":"2026-08-08T02:03:00-06:00","time_min":"2026-08-08T01:48:00-06:00"}
```

This is a bounded, read-only failure/permission probe. No retry, event-detail fetch, send, mutation, or fallback is authorized.