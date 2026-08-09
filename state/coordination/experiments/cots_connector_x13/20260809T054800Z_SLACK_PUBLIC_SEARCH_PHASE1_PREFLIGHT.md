---
schema_id: hfo.gen133.x13.cots_connector_event.v1
experiment_id: X13_SLACK_PUBLIC_SEARCH_READONLY_026
phase: 1
status: PREFLIGHT
candidate: Slack_slack_search_public_readonly
wip: 1
prior_current_version: 200
expected_current_version: 201
request_sha256: 4717053d884ca62dc01da1ffa3d4e169a012516a56f703dd999f054830351d53
request_canonical_json: '{"content_types":"messages","context_channel_id":"C0BGNGPJFHU","include_bots":true,"include_context":false,"limit":5,"query":"ADOPT_WITH_GATES in:<#C0BGNGPJFHU>","response_format":"concise","sort":"timestamp","sort_dir":"desc","tool":"Slack.slack_search_public"}'
mutation_allowed: false
privacy_gate: PUBLIC_CHANNEL_SEARCH_ONLY;NO_PRIVATE_CHANNELS_DMS_OR_FILES;DO_NOT_PERSIST_MESSAGE_BODY_AUTHOR_OR_URL_IN_RESULT_EVENT
valid_time_utc: 2026-08-09T05:48:00Z
recorded_time_utc: 2026-08-09T05:48:00Z
---

# X13 Slack public search Phase 1 preflight

Bounded candidate: native Slack connector public-channel message search only. This wake permits exactly one read-only search for the existing marker `ADOPT_WITH_GATES` constrained to channel `C0BGNGPJFHU`, capped at five concise message results, including bot messages, with context disabled.

The result event may persist only aggregate count, cursor/pagination presence, connector timing/error behavior, and a privacy-safe digest of ordered message timestamps/IDs if available. Message bodies, authors, URLs, files, and private-channel content are out of scope.
