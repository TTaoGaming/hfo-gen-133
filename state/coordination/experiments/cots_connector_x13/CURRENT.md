---
schema_id: hfo.gen133.x13.cots_connector_current.v1
experiment_id: X13_SLACK_PUBLIC_CHANNEL_CONNECTOR_001
version: 9
prior_version: 8
candidate: Slack_public_channel_connector
candidate_contract_reference: official_Slack_conversations_history_search_messages_chat_postMessage_connector_auth_headers_hidden
campaign_wake: 1_of_4
phase_1_completed: true
phase_2_completed: false
phase_3_completed: false
phase_4_decision: PENDING
phase_status: PHASE1_AUTHENTICATED_PUBLIC_CHANNEL_DISCOVERY_AND_HISTORY_BASELINE_COMPLETE
binding_architecture_decision: false
last_event_commit: 1321ee24d1fccc77a655d27e0d31ff639b0e4213
last_event_path: state/coordination/experiments/cots_connector_x13/20260801T054853Z_SLACK_PUBLIC_CHANNEL_PHASE1_BASELINE.md
last_event_blob_sha: eda7f08f70e4a44595338825b69b2b710d5d13db
last_event_utf8_bytes: 7750
last_event_sha256: 7b8d5f27c000a5e6419888554df94797da5c0a663075271e9e05beddfb596f24
adoption_credit: 1
adoption_credit_basis: AUTHENTICATED_PUBLIC_CHANNEL_DISCOVERY_AND_THREE_MESSAGE_HISTORY_READ
fitness_credit: 0_UNTIL_CONSUMED_BY_WORKITEM
carrier_task_id: 6a55c1733708819185088bf334e33ea5
carrier_task_id_match: true
carrier_task_id_observation_source: AUTOMATION_RUNTIME_PROMPT
native_task_inventory_read_this_wake: false
effect_ceiling: PUBLIC_CHANNEL_DISCOVERY_AND_READ_ONLY_HISTORY_BASELINE
operator_relay_minutes: 0
operator_minutes_removed_estimate: 3_to_8_UNVALIDATED
custom_code_avoided_estimate: 30_to_100_LOC_UNVALIDATED
paid_cost_usd_observed: 0
connector_authenticated: true
live_authentication_identity: UNKNOWN
live_authentication_token_type: UNKNOWN
live_authentication_scope: UNKNOWN
live_rate_limit_headers: NOT_EXPOSED
direct_probe_channels:
  - C0BGC646A1H
  - C0BGNGPJFHU
history_probe_channel: C0BGNGPJFHU
history_probe_returned_message_count: 3
history_probe_newest_message_ts: "1785563423.553799"
history_probe_oldest_message_ts_in_page: "1785562913.420059"
history_probe_pagination_cursor_exposed: true
message_bodies_externalized_to_git: false
observed_failure_behavior: NONE_PHASE1_READS_SUCCEEDED
durability: PROVIDER_EXISTING_MESSAGE_TIMESTAMPS_ONLY_RETENTION_AND_IMMUTABILITY_UNPROVEN
observability: CHANNEL_METADATA_MESSAGE_TS_AND_CURSOR_EXPOSED_AUTH_QUOTA_REQUEST_RETRY_AUDIT_HIDDEN
portability: MEDIUM_SLACK_CONTRACT_MEDIUM_LOW_CONNECTOR_OTHER_PLATFORMS_UNPROVEN
verifier: S04_STRUCTURAL_PREFLIGHT_THEN_DISTINCT_NONPRODUCER_BEFORE_HIGHER_EFFECT_USE
consumer: Ratatoskr_and_Olrun
consumer_ack: NOT_OBSERVED
same_provider_binding_weight: 0
strongest_falsifier: INCONSISTENT_BOUNDED_READ_UNAUTHORIZED_PRIVATE_CONTENT_OPERATOR_CREDENTIAL_FERRY_OR_PHASE2_WRITE_NOT_EXACTLY_READ_BACK
review_expiry_utc: 2026-08-08T05:48:53Z
next_phase: PHASE2_SMALLEST_HARMLESS_REVERSIBLE_MICRO_USE
valid_time_utc: 2026-08-01T05:48:53Z
transaction_time_utc: SEE_GIT_COMMIT_METADATA
sealed: false
prior_campaign:
  experiment_id: X13_GITHUB_CONTENTS_API_001
  final_version: 8
  decision: ADOPT_WITH_GATES
  decision_commit: 9cb0a9368a7ccf3b6e4f1a5ae62cfada2e134db8
  current_commit: 1ee1e4c03b721d8397d4b719a4f4834b453ea4a5
---

# X13 current campaign

The Slack public-channel connector campaign has completed phase 1 of 4.

The connector discovered two known public HFO channels and read a bounded three-message
history page from `C0BGNGPJFHU`, exposing channel metadata, message timestamps, and a
pagination cursor. Message bodies remain in Slack and were not copied into Git.

This is a same-provider authenticated read baseline with binding weight zero. It does not
prove least privilege, complete search/index behavior, write authority, retention
durability, predictable rate limits, private-channel boundaries, independent
verification, or ConsumerAck. Authentication identity, token type, scopes, raw HTTP
status, request IDs, rate-limit headers, retries, server timing, and audit attribution
remain hidden.

Phase 2 should use one concise Git-first X13 pointer as the smallest harmless Slack
micro-use, then bind the returned message timestamp and exact direct history readback.
No edit, delete, impersonation, private-channel write, or broad notification is allowed.
