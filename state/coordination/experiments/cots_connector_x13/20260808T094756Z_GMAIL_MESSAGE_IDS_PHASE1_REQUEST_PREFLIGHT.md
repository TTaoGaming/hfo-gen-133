---
schema_id: hfo.gen133.x13.cots_connector_event.v1
experiment_id: X13_GMAIL_MESSAGE_IDS_SEARCH_READONLY_021
event_type: PHASE1_REQUEST_PREFLIGHT
candidate: Gmail_search_email_ids
phase: 1
wip: 1
expected_current_version: 180
canonical_branch: agent/gen133-bootstrap-20260730
request_descriptor_canonicalization: UTF8_JSON_SORTED_KEYS_COMPACT_SEPARATORS_NO_ASCII_ESCAPING
request_descriptor_privacy_safe: true
request_descriptor_exact: '{"label_ids":null,"max_results":3,"next_page_token":"","query":"newer_than:7d -in:spam -in:trash"}'
request_intent: BOUNDED_READONLY_MESSAGE_ID_DISCOVERY_ONLY
mutation_allowed: false
message_content_fetch_allowed: false
attachment_fetch_allowed: false
send_allowed: false
valid_time_utc: 2026-08-08T09:47:56Z
recorded_time_utc: 2026-08-08T09:47:56Z
---

# X13 Gmail message-ID search Phase 1 request preflight

Persisted the exact privacy-safe request preimage before the first candidate call so later replay claims can be verified without reconstructing semantically material parameters from a hash.

Exact connector request:

```json
{"label_ids":null,"max_results":3,"next_page_token":"","query":"newer_than:7d -in:spam -in:trash"}
```

Scope is deliberately narrow: search for at most three Gmail message IDs from the last seven days, excluding Spam and Trash. No message body, headers, snippet, attachment, draft, label mutation, send, archive, Trash action, or other mailbox mutation is authorized by this experiment.
