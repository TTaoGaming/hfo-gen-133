---
schema_id: hfo.gen133.x13.cots_connector_event.v1
experiment_id: X13_GCAL_CALENDARLIST_READONLY_023
phase: 2
wake: 2_of_4
event_type: PHASE2_CONTROL_PREFLIGHT
candidate: Google_Calendar_list_calendars
control_probe: Google_Calendar_get_profile
wip: 1
prior_current_version: 189
read_only: true
mutation_allowed: false
request_descriptor_canonicalization: UTF8_JSON_SORTED_KEYS_COMPACT_SEPARATORS_NO_ASCII_ESCAPING
request_descriptor_sha256: 2064ee495be825bf28bb8412939117e3b3ccd7856d8c5c859c15943c7fdcbde9
valid_time_utc: 2026-08-08T18:46:27Z
recorded_time_utc: 2026-08-08T18:46:27Z
---

# Phase 2 control preflight

Purpose: run one smaller harmless read-only Google Calendar connector-family control probe to distinguish connector-wide blocking from action-specific blocking observed on `list_calendars`.

Exact canonical request descriptor:

```json
{"action":"Google_Calendar.get_profile","parameters":{},"purpose":"phase2_control_probe_distinguish_connector_wide_from_action_specific_blocking","read_only":true}
```

SHA-256: `2064ee495be825bf28bb8412939117e3b3ccd7856d8c5c859c15943c7fdcbde9`

Gates: one call only; no permission or connection mutation; no calendar/event mutation; no retry in this wake; do not persist raw profile identity fields in X13 receipts; persist only whether a usable profile result was returned and privacy-safe execution facts.
