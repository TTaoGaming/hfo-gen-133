---
schema_id: hfo.gen133.x13.cots_connector_event.v1
experiment_id: X13_GOOGLE_CALENDAR_EVENT_SEARCH_READONLY_028
candidate: Google_Calendar.search_events_readonly
phase: 2
phase_name: SMALLEST_HARMLESS_READONLY_REPLAY
wip: 1
expected_current_version: 209
phase1_request_sha256: 9f53e69c34059f00164e5f9f28a2b2488ec976ffaec270526da4c38d61ef56c9
phase1_request_sha256_recomputed: 9f53e69c34059f00164e5f9f28a2b2488ec976ffaec270526da4c38d61ef56c9
request_sha256_verified: true
request_canonical_json: '{"calendar_id":"primary","max_results":5,"time_max":"2026-08-16T13:52:00Z","time_min":"2026-08-09T13:52:00Z","timezone_str":"America/Denver"}'
mutation_allowed: false
send_allowed: false
spend_allowed: false
production_deploy_allowed: false
secret_persistence_allowed: false
raw_event_content_persistence_allowed: false
second_page_fetch_allowed: false
valid_time_utc: 2026-08-09T14:47:20Z
recorded_time_utc: 2026-08-09T14:47:20Z
---

# X13 Google Calendar event search Phase 2 preflight

Replay the exact Phase-1 bounded read-only request once against the primary Google Calendar. Compare result count, next-page-token presence, and a privacy-safe ordered event-ID digest while allowing legitimate calendar drift.

Authorized request: `calendar_id=primary`, `max_results=5`, `time_min=2026-08-09T13:52:00Z`, `time_max=2026-08-16T13:52:00Z`, `timezone_str=America/Denver`. Do not fetch page 2.

Persist only aggregate measurements and privacy-safe digests. Do not persist event titles, descriptions, attendees, locations, conferencing data, event IDs, URLs, or pagination tokens. No calendar mutation, response, send, spend, account change, or production deployment.