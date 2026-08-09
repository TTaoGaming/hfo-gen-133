---
schema_id: hfo.gen133.x13.cots_connector_event.v1
experiment_id: X13_GMAIL_MESSAGE_ID_SEARCH_READONLY_026
event_type: PHASE3_PREFLIGHT
phase: 3
campaign_wake: 3_of_4
expected_current_version: 202
next_current_version: 203
candidate: Gmail_search_email_ids_readonly
wip: 1
probe_type: SYNTHETIC_INVALID_PAGE_TOKEN_READONLY
canonical_request_json: '{"label_ids":["INBOX"],"max_results":5,"next_page_token":"X13_SYNTHETIC_INVALID_PAGE_TOKEN","query":"newer_than:30d -in:spam -in:trash"}'
canonical_request_sha256: a84190edc43f11a14ea1ee360eda7fde2e339f096020ed369e2050726c0eda39
safety_bounds: READ_ONLY;ID_ONLY;MAX_RESULTS_5;NO_CONTENT_HYDRATION;NO_MAILBOX_MUTATION;ONE_CALL;NO_RETRY;NO_FALLBACK
expected_failure: STRUCTURED_INVALID_ARGUMENT_OR_EQUIVALENT_FAIL_CLOSED_ERROR
strongest_falsifier: CONNECTOR_MUTATES_FALLS_BACK_RETRIES_OR_RETURNS_NONDIAGNOSTIC_SUCCESS_ON_MALFORMED_PAGE_TOKEN
raw_message_ids_persisted: false
raw_page_token_persisted: false
valid_time_utc: 2026-08-09T07:48:00Z
recorded_time_utc: 2026-08-09T07:48:00Z
---

# X13 Phase 3 Preflight — Gmail message-ID search

One bounded read-only failure-path probe is authorized: replay the existing ID-only INBOX search with a clearly synthetic malformed page token, capped at 5. No content hydration, mailbox mutation, retry, fallback, raw message-ID persistence, or raw provider page-token persistence is permitted.

Expected behavior is fail-closed with a structured invalid-token/invalid-argument error. A mutation, retry/fallback, silent success, or non-diagnostic wrapper crash is an Andon.