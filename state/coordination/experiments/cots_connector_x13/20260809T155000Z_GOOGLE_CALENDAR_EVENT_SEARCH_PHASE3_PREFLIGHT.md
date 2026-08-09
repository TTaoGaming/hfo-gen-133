---
schema_id: hfo.gen133.x13.cots_connector_event.v1
experiment_id: X13_GOOGLE_CALENDAR_EVENT_SEARCH_READONLY_028
event_type: PHASE3_PREFLIGHT
expected_current_version: 210
candidate: Google_Calendar.search_events_readonly
campaign_wake: 3_of_4
wip: 1
request_sha256: 1539815963e0d533683a002d651b196d9d3ee4e4ac50c194d8a8d5e21f7302b6
request_canonical_json: '{"calendar_id":"x13-nonexistent-calendar-028@group.calendar.google.com","max_results":1,"time_max":"2026-08-16T00:00:00Z","time_min":"2026-08-09T00:00:00Z","timezone_str":"America/Denver"}'
probe_class: FAILURE_PERMISSION_CONNECTOR_VARIANCE
mutation_expected: false
paid_call_expected: false
secret_exposure_expected: false
valid_time_utc: 2026-08-09T15:50:00Z
recorded_time_utc: 2026-08-09T15:50:00Z
---

# Phase 3 preflight

Run exactly one bounded, harmless, non-mutating `Google_Calendar.search_events` probe against a clearly synthetic nonexistent calendar ID. Keep the same bounded seven-day window used for the campaign and cap results at one.

Purpose: observe whether the connector fails closed and whether its error surface distinguishes calendar nonexistence from insufficient permission. Do not retry, widen the window, fetch another calendar, hydrate a returned event, or mutate Calendar state.

Persistence gate: do not store any raw event content, real event IDs, URLs, locations, or page tokens. Persist only structured failure classification, wrapper timing if exposed, and campaign aggregates.
