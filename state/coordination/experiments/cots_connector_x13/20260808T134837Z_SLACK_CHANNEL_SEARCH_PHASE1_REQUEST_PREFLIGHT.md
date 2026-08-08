---
schema_id: hfo.gen133.x13.cots_connector_preflight.v1
experiment_id: X13_SLACK_CHANNEL_SEARCH_READONLY_022
expected_current_version: 184
phase: 1
wip: 1
candidate: Slack_slack_search_channels
request_descriptor_canonicalization: UTF8_JSON_SORTED_KEYS_COMPACT_SEPARATORS_NO_ASCII_ESCAPING
request_descriptor_sha256: 201fd4cb7354b36624fb666bc61f4252c45cd4bd7286f68f3062d30c4781678b
exact_privacy_safe_request_descriptor_persisted_before_call: true
result_digest_canonicalization_planned: UTF8_JSON_ARRAY_OF_CHANNEL_IDS_ORDERED_COMPACT_NO_ASCII_ESCAPING
raw_channel_metadata_persistence_policy: DO_NOT_PERSIST_TOPICS_PURPOSES_OR_CHANNEL_IDS_IN_X13_RECEIPTS;PERSIST_ONLY_COUNTS_FIELD_PRESENCE_AND_HASHED_ORDERED_IDS
candidate_mutation_allowed: false
valid_time_utc: 2026-08-08T13:48:37Z
recorded_time_utc: 2026-08-08T13:48:37Z
---

# X13 Slack channel search — Phase 1 request preflight

Exact privacy-safe request descriptor, persisted before the candidate call:

```json
{"candidate":"Slack_slack_search_channels","channel_types":"public_channel","cursor":"","include_archived":false,"limit":5,"query":"hfo","response_format":"detailed"}
```

This preflight authorizes one bounded read-only public-channel metadata discovery call only. No message read, file read, join, send, draft, edit, schedule, canvas mutation, or other Slack mutation is authorized.
