---
schema_id: hfo.gen133.x13.cots_connector_preflight.v1
experiment_id: X13_SLACK_CHANNEL_SEARCH_READONLY_022
expected_current_version: 186
phase: 3
wip: 1
candidate: Slack_slack_search_channels
probe_kind: SYNTHETIC_INVALID_CURSOR_FAILURE_PROBE
request_descriptor_canonicalization: UTF8_JSON_SORTED_KEYS_COMPACT_SEPARATORS_NO_ASCII_ESCAPING
request_descriptor_sha256: 19faa1ea2d883968c55ce663fd779517908369c20f52d2b3e321c3b32d545f58
exact_privacy_safe_request_descriptor_persisted_before_call: true
request_hash_recomputed_before_candidate_call: true
request_hash_match_before_candidate_call: true
result_persistence_policy: DO_NOT_PERSIST_RETURNED_SLACK_CHANNEL_METADATA_OR_IDENTIFIERS;PERSIST_ONLY_ERROR_CLASS_COUNTS_FIELD_PRESENCE_AND_PROVIDER_AGNOSTIC_EXECUTION_FACTS
candidate_mutation_allowed: false
retry_allowed: false
valid_time_utc: 2026-08-08T15:47:03Z
recorded_time_utc: 2026-08-08T15:47:03Z
---

# X13 Slack channel search — Phase 3 synthetic invalid-cursor preflight

Exact privacy-safe request descriptor, persisted and hash-verified before the candidate call:

```json
{"candidate":"Slack_slack_search_channels","channel_types":"public_channel","cursor":"X13_INVALID_CURSOR_DO_NOT_RETRY","include_archived":false,"limit":1,"query":"hfo","response_format":"concise"}
```

This authorizes exactly one bounded read-only failure-semantics probe using a deliberately invalid pagination cursor. No retry is authorized. No private-channel search, message/file read, join, send, draft, edit, schedule, canvas operation, or other Slack mutation is authorized.

Expected contract signal if the wrapper maps to a Slack cursor-paginated native method: an explicit invalid-cursor failure. Any returned channel data must not be persisted in X13 receipts while the wrapper's native mapping and applicable retention contract remain unresolved.
