---
schema_id: hfo.gen133.x13.cots_connector_event.v1
experiment_id: X13_GOOGLE_CALENDAR_EVENT_SEARCH_READONLY_028
candidate: Google_Calendar.search_events_readonly
phase: 1
phase_name: OFFICIAL_CONTRACT_AND_DIRECT_CAPABILITY_BASELINE
wip: 1
expected_current_version: 208
request_sha256: 9f53e69c34059f00164e5f9f28a2b2488ec976ffaec270526da4c38d61ef56c9
request_canonical_json: '{"calendar_id":"primary","max_results":5,"time_max":"2026-08-16T13:52:00Z","time_min":"2026-08-09T13:52:00Z","timezone_str":"America/Denver"}'
mutation_allowed: false
send_allowed: false
spend_allowed: false
production_deploy_allowed: false
secret_persistence_allowed: false
raw_event_content_persistence_allowed: false
valid_time_utc: 2026-08-09T13:52:00Z
recorded_time_utc: 2026-08-09T13:52:00Z
---

# X13 Google Calendar event search Phase 1 preflight

Start one new four-wake campaign at WIP=1 after CURRENT v208 closed the prior GitHub recent-PR candidate.

Authorized micro-use: one bounded, read-only search of the primary Google Calendar for events in the exact seven-day window `[2026-08-09T13:52:00Z, 2026-08-16T13:52:00Z)`, capped at five results. No event creation, update, deletion, response, email/send, spend, account change, or production deployment.

Persist only aggregate measurements and privacy-safe digests. Do not persist event titles, descriptions, attendees, locations, conferencing data, event IDs, calendar IDs beyond the literal `primary`, or pagination tokens.

Phase-1 questions: does the connector provide usable bounded read access; what fields does it hydrate despite the bounded request; does it expose pagination, wrapper/provider errors, rate/quota/request identifiers, principal/scope information, or direct cost evidence; and how closely does its observable contract map to the official Calendar `events.list` surface.
