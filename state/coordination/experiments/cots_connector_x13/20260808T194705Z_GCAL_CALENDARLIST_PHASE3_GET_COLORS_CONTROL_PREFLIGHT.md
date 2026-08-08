---
schema_id: hfo.gen133.x13.cots_connector_event.v1
experiment_id: X13_GCAL_CALENDARLIST_READONLY_023
phase: 3
wake: 3_of_4
event_type: REQUEST_PREFLIGHT
candidate: Google_Calendar_list_calendars
control_probe: Google_Calendar_get_colors
wip: 1
request_descriptor_canonicalization: UTF8_JSON_SORTED_KEYS_COMPACT_SEPARATORS_NO_ASCII_ESCAPING
request_descriptor: '{"action":"Google_Calendar.get_colors","parameters":{}}'
request_descriptor_sha256: c6a5f2fa7f130bee935720381ceb6dea7b6a7539d9e5e839e2a14fa4f64fdcce
purpose: DISTINCT_BOUNDED_READONLY_NON_CONTENT_METADATA_CONTROL_TO_PROBE_ACTION_SPECIFIC_CONNECTOR_VARIANCE_WITHOUT_RETRYING_LIST_CALENDARS
expected_side_effects: NONE
raw_calendar_or_event_data_persistence: FORBIDDEN
permission_or_connection_mutation: FORBIDDEN
calendar_mutation: FORBIDDEN
retry_budget: 0
fallback_budget: 0
valid_time_utc: 2026-08-08T19:47:05Z
recorded_time_utc: 2026-08-08T19:47:05Z
---

# Phase 3 preflight — Google Calendar get_colors control

This immutable preflight freezes the exact no-parameter `Google_Calendar.get_colors` request before execution. The probe is intentionally distinct from the blocked `list_calendars` action and from Phase 2 `get_profile`; it reads provider color-palette metadata only and must not read event content, mutate Calendar state, alter permissions/connections, retry, or fall back.

Only execution facts and privacy-safe aggregate metadata may be persisted after the call. Returned palette values themselves are not needed for this campaign and must not be copied into X13 receipts.
