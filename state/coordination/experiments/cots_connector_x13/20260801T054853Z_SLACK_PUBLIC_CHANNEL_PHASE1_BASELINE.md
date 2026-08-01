---
schema_id: hfo.gen133.x13.cots_connector_event.v1
experiment_id: X13_SLACK_PUBLIC_CHANNEL_CONNECTOR_001
seat: X13_COTS_CONNECTOR_PDCA
carrier_task_id_expected: 6a55c1733708819185088bf334e33ea5
carrier_task_id_observed: 6a55c1733708819185088bf334e33ea5
carrier_task_id_match: true
carrier_task_id_observation_source: AUTOMATION_RUNTIME_PROMPT
native_task_inventory_read_this_wake: false
campaign_wake: 1_of_4
phase: 1
phase_result: BASELINE_ESTABLISHED
expected_current_version: 8
next_current_version: 9
prior_current_blob_sha: 3dd84e81c8bb1218c21a5fb020f5480d92e77e70
valid_time_utc: 2026-08-01T05:48:53Z
transaction_time_utc: SEE_GIT_COMMIT_METADATA
canonical_repository: TTaoGaming/hfo-gen-133
canonical_branch: agent/gen133-bootstrap-20260730
wip: 1
candidate: Slack_public_channel_connector
effect_ceiling: PUBLIC_CHANNEL_DISCOVERY_AND_READ_ONLY_HISTORY_BASELINE
verifier: S04_STRUCTURAL_PREFLIGHT_THEN_DISTINCT_NONPRODUCER_BEFORE_HIGHER_EFFECT_USE
consumer: Ratatoskr_and_Olrun
consumer_ack: NOT_OBSERVED
same_provider_evidence_binding_weight: 0
review_expiry_utc: 2026-08-08T05:48:53Z
sealed: false
official_contract_checked_utc: 2026-08-01T05:48:53Z
official_contract:
  conversations_history: https://docs.slack.dev/reference/methods/conversations.history/
  search_messages: https://docs.slack.dev/reference/methods/search.messages/
  chat_postMessage: https://docs.slack.dev/reference/methods/chat.postMessage/
direct_probe:
  workspace_domain: hfonetwork.slack.com
  channel_query_1: hfo-synthesis
  channel_1_id: C0BGC646A1H
  channel_1_type: public_channel
  channel_1_archived: false
  channel_query_2: hfo-command-and-control
  channel_2_id: C0BGNGPJFHU
  channel_2_type: public_channel
  channel_2_archived: false
  history_channel_id: C0BGNGPJFHU
  requested_limit: 3
  returned_message_count: 3
  return_order: newest_first
  newest_message_ts: "1785563423.553799"
  oldest_message_ts_in_page: "1785562913.420059"
  pagination_cursor_exposed: true
  bodies_externalized_to_git: false
permission_error_class: AUTHENTICATED_READ_SUCCEEDED_SCOPE_AND_TOKEN_CLASS_HIDDEN
latency_exposed: false
operator_relay_minutes: 0
paid_cost_usd_observed: 0
---

# X13 phase 1 — Slack public-channel connector baseline

## Baseline result

The connected Slack surface successfully discovered two known public HFO channels by
name and read the three newest messages from `C0BGNGPJFHU` in newest-first order.
The response exposed stable channel IDs, public/archived metadata, message timestamps,
and a pagination cursor. Message bodies remained in Slack and are not copied into this
Git receipt.

This establishes only an authenticated public-channel discovery and history-read
baseline through the current connector. It does not establish least privilege,
workspace-wide visibility, private-channel access, message-write authority, deletion
authority, retention durability, complete indexing, independent verification, or a
stable raw Slack Web API response shape.

## Official contract baseline

Slack documents `conversations.history` as requiring a conversation ID and an
authenticated token with the relevant history scope. Accessible conversations depend
on token type and membership. The raw method supports cursor and time pagination.
Slack also documents materially different rate limits by application distribution
class; the connector did not expose the effective token type, app classification,
scope set, request headers, rate-limit headers, request ID, retry behavior, or raw
response envelope.

Slack documents `search.messages` as a legacy user-token method requiring `search:read`
and recommends the newer real-time search API. No search call was used for the accepted
phase-1 baseline, so search completeness and index latency remain unmeasured here.

Slack documents `chat.postMessage` as requiring `chat:write`, with channel membership
and `chat:write.public` affecting public-channel posting. No write was attempted in
phase 1. A smallest reversible micro-use is reserved for phase 2 and must remain within
the no-send/no-production-effect ceiling unless the scheduled-task instruction itself
authorizes the exact Slack pointer post after Git-first state advance.

## Measurements

```yaml
custom_code_avoided:
  estimate: 30_to_100_LOC_basic_read_adapter_UNVALIDATED
  direct_components_avoided:
    - OAuth_token_transport
    - channel_discovery_request_construction
    - history_request_construction
    - response_decoding
    - basic_cursor_exposure
  not_avoided:
    - authorization_policy
    - privacy_filtering
    - deduplication
    - search_index_reconciliation
    - retry_and_rate_limit_policy
    - independent_verification
  fitness_credit: 0_until_consumed
operator_minutes:
  relay_measured: 0
  estimated_removed_for_one_channel_lookup_and_page_read: 3_to_8
  estimate_validated: false
credentials:
  operator_credential_interaction_this_wake: 0
  connector_authenticated: true
  identity_token_type_scope_expiry_SSO_and_audit_actor: UNKNOWN
durability:
  established: provider_returned_existing_message_timestamps
  not_established:
    - retention_period
    - immutable_history
    - exactly_once_delivery
    - durable_workflow_recovery
    - complete_export
observability:
  exposed:
    - workspace_permalink_domain
    - channel_id
    - channel_name
    - public_channel_type
    - archived_state
    - message_timestamp
    - pagination_cursor
  hidden_or_unknown:
    - raw_HTTP_status
    - auth_identity_and_scope
    - app_distribution_class
    - request_id
    - rate_limit_headers
    - retry_count
    - server_timing
    - audit_event
portability:
  contract_level: MEDIUM_WITHIN_SLACK_WEB_API
  connector_wrapper_level: MEDIUM_LOW
  alternate_collaboration_platforms: UNPROVEN
failure_behavior:
  measured: NONE_PHASE1_READS_SUCCEEDED
  unmeasured:
    - missing_scope
    - not_in_channel
    - archived_or_read_only_channel
    - rate_limit
    - search_index_delay
    - transient_service_error
    - duplicate_or_ambiguous_write
direct_cost_and_quota:
  incremental_paid_cost_observed_usd: 0
  exact_workspace_plan_and_connector_allocation: UNKNOWN
  live_rate_limit_state: UNKNOWN
```

## Strongest objection

A successful read through an opaque connected surface can conceal a broad user token,
shared workspace authority, connector-side caching, or transformed results. The wrapper
contract permits up to 100 messages per call, while the raw Slack endpoint's effective
limits can vary by app class. Without exposed auth and rate-limit metadata, the baseline
cannot prove least privilege, predictable quota behavior, or raw-API portability.

## Strongest falsifier

Revise or defer the candidate if a fresh direct channel read returns inconsistent
message timestamps for the same bounded window, exposes unauthorized private content,
requires operator credential ferrying, silently omits accessible public messages without
a documented boundary, or a phase-2 reversible write cannot be exactly read back and
safely contained.

## Next phase

Phase 2 should perform the smallest harmless reversible micro-use. Because Git-first
campaign pointers are explicitly allowed, the preferred probe is one concise X13 phase-2
pointer posted to `C0BGNGPJFHU` after creating and reading back its immutable Git event,
followed by exact message-TS readback. No edit, delete, impersonation, private-channel
write, or broad notification experiment is authorized.

## Honest flaw

This phase used one workspace, two channel-discovery calls, and one three-message history
page. It did not inspect raw HTTP, scopes, audit logs, rate-limit headers, private-channel
boundaries, search behavior, write behavior, retries, or retention. The evidence is
same-provider and nonbinding with weight zero.
