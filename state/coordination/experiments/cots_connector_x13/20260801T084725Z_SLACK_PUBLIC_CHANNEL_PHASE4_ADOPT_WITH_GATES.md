---
schema_id: hfo.gen133.x13.cots_connector_event.v1
experiment_id: X13_SLACK_PUBLIC_CHANNEL_CONNECTOR_001
seat: X13_COTS_CONNECTOR_PDCA
addressed_to: S04_STRUCTURAL_PREFLIGHT
carrier_task_id_expected: 6a55c1733708819185088bf334e33ea5
carrier_task_id_observed: 6a55c1733708819185088bf334e33ea5
carrier_task_id_match: true
carrier_task_id_observation_source: AUTOMATION_RUNTIME_PROMPT
native_task_inventory_read_this_wake: false
campaign_wake: 4_of_4
phase_attempted: 4_of_4
phase_1_completed: true
phase_2_completed: true
phase_3_completed: true
phase_4_completed: true
candidate: Slack_public_channel_connector
decision: ADOPT_WITH_GATES
binding_architecture_decision: false
measured_fact_changed: true
prior_current_version: 11
next_current_version: 12
prior_current_blob_sha: e2433fa58e0badd5b938f953af6116d5e5606d4e
valid_time_utc: 2026-08-01T08:47:25Z
transaction_time_utc: SEE_GIT_COMMIT_METADATA
canonical_repository: TTaoGaming/hfo-gen-133
canonical_branch: agent/gen133-bootstrap-20260730
wip: 1
effect_ceiling: DECISION_PLUS_ONE_BOUNDED_PUBLIC_CHANNEL_READ_NO_SLACK_WRITE
verifier: S04_STRUCTURAL_PREFLIGHT_THEN_DISTINCT_NONPRODUCER_BEFORE_HIGHER_EFFECT_USE
consumer: Ratatoskr_and_Olrun
consumer_ack: NOT_OBSERVED
same_provider_evidence_binding_weight: 0
review_expiry_utc: 2026-08-08T08:47:25Z
sealed: false
source_events:
  phase_1:
    path: state/coordination/experiments/cots_connector_x13/20260801T054853Z_SLACK_PUBLIC_CHANNEL_PHASE1_BASELINE.md
    commit: 1321ee24d1fccc77a655d27e0d31ff639b0e4213
    blob_sha: eda7f08f70e4a44595338825b69b2b710d5d13db
  phase_2:
    path: state/coordination/experiments/cots_connector_x13/20260801T064925Z_SLACK_PUBLIC_CHANNEL_PHASE2_GIT_FIRST_POINTER_MICRO_USE.md
    commit: 1ee23f3773e02f5f2fbbc4a505265a67525934f1
    blob_sha: 1f7a1f8f8c73323b86898a170f429d68bea0b346
  phase_3:
    path: state/coordination/experiments/cots_connector_x13/20260801T074939Z_SLACK_PUBLIC_CHANNEL_PHASE3_INVALID_CHANNEL_AND_RECOVERY.md
    commit: ef9d2d451ac4b0734bf1a22729e4875e82c219cd
    blob_sha: f1766ea0e70314872b7a67ef1cee9b38f0f83751
official_contract_checked_utc: 2026-08-01T08:47:25Z
official_contract:
  conversations_history: https://docs.slack.dev/reference/methods/conversations.history/
  chat_postMessage: https://docs.slack.dev/reference/methods/chat.postMessage/
  rate_limits: https://docs.slack.dev/apis/web-api/rate-limits/
  non_marketplace_rate_change: https://docs.slack.dev/changelog/2025/05/29/rate-limit-changes-for-non-marketplace-apps/
decision_time_probe:
  channel_id: C0BGNGPJFHU
  requested_limit: 1
  read_succeeded: true
  channel_identity: hfo-command-and-control
  message_body_externalized_to_git: false
  successful_message_writes_this_wake: 0
operator_relay_minutes: 0
paid_cost_usd_observed: 0
next_candidate_nomination: Gmail_read_only_search_and_message_metadata_connector
---

# X13 phase 4 — Slack connector adoption decision

## Decision

`ADOPT_WITH_GATES` for bounded public-channel discovery, bounded history reads, and
explicitly authorized Git-first pointer posts. Do not adopt the connector as an
authoritative authorization oracle, existence oracle, durable workflow runtime,
exactly-once transport, audit system, or independent verifier.

The decision-time one-message read from `C0BGNGPJFHU` succeeded. No Slack write occurred
on this wake and no message body was copied into Git.

## Evidence synthesis

- Phase 1 directly discovered two known public channels and read a bounded history page.
- Phase 2 created Git state first, posted exactly one concise public-channel pointer, and
  immediately read back the returned channel and message timestamp through bounded
  history.
- Phase 3 returned an explicit `channel_not_found` class for a deterministic invalid ID,
  then recovered on a known valid channel without returning unrelated content.
- The phase-3 error remains ambiguous: invalid ID, wrong workspace, and insufficient
  access can collapse into the same class.
- The current wrapper still hides token identity, scopes, app classification, raw HTTP
  status and headers, request IDs, retry behavior, rate-limit state, timing, audit events,
  and provider-native versus wrapper-native failure boundaries.

Slack's official contract requires relevant history scopes and conversation access for
`conversations.history`; accessible conversations depend on token type and membership.
Slack documents materially different history limits by app distribution class, including
limits introduced for affected non-Marketplace commercial apps on 2025-05-29. The live
connector does not expose which class applies. `chat.postMessage` requires `chat:write`
and channel access, and Slack documents special per-channel posting limits. These are
contract facts, not proof of the connector's live token, quota, or identity.

## Mandatory gates

1. **Git first.** Create and read back the immutable receipt before any allowed Slack
   pointer post.
2. **Explicit effect ceiling.** Public-channel read is the default. A write requires the
   exact task instruction to authorize one concise pointer after Git state advances.
3. **Exact addressing.** Bind channel ID and, for write readback, returned message
   timestamp and permalink. Do not use broad search counts as uniqueness evidence.
4. **Ambiguous errors fail closed.** Treat `channel_not_found` as
   `ABSENT_OR_WRONG_WORKSPACE_OR_INSUFFICIENT_ACCESS`; do not infer resource existence,
   permission state, or repair action.
5. **No automatic retries for writes.** The wrapper exposes no idempotency key,
   `client_msg_id`, request ID, or retry count. An ambiguous send must stop for review,
   not repeat.
6. **No durability inflation.** Slack timestamps and immediate history readback do not
   establish immutable retention, replay, exactly-once delivery, workflow recovery, or
   terminal receipt durability.
7. **Privacy boundary.** Do not copy private bodies into Git or public Slack. Private
   channels, DMs, files, and broad workspace search require separate authority and a new
   campaign.
8. **Quota conservatism.** Because app class and live rate-limit headers are hidden, keep
   calls bounded and low-rate; rate-limit or service errors produce HOLD/Andon, not
   throughput escalation.
9. **Independent verification.** Same-provider send/read agreement has binding weight
   zero. S04 may preflight structure; a distinct nonproducer must verify before any
   higher-effect use.
10. **Named consumer and expiry.** Adoption remains advisory until Ratatoskr or Olrun
    consumes it for an exact WorkItem before the review expiry.

## Measurements

```yaml
custom_code_avoided:
  estimate: 40_to_120_LOC_basic_discovery_read_post_readback_adapter_UNVALIDATED
  avoided:
    - OAuth_token_transport
    - basic_channel_discovery_request_construction
    - history_and_post_request_construction
    - response_decoding
    - cursor_timestamp_and_permalink_extraction
  not_avoided:
    - authorization_and_privacy_policy
    - idempotency_and_duplicate_suppression
    - retry_and_rate_limit_policy
    - raw_body_canonicalization
    - audit_correlation
    - independent_verification
operator_minutes:
  relay_measured_across_campaign: 0
  estimated_removed_per_bounded_lookup_or_pointer_cycle: 2_to_8
  estimate_validated: false
credentials:
  operator_credential_interactions: 0
  connector_authenticated: true
  identity_token_type_scope_expiry_SSO_and_audit_actor: UNKNOWN
durability:
  observed:
    - existing_message_timestamps_returned
    - one_post_returned_timestamp_and_permalink
    - immediate_bounded_history_readback
    - valid_read_succeeded_after_one_failed_read
  unproven:
    - immutable_retention
    - exactly_once_posting
    - durable_replay_or_resume
    - deletion_or_compensation_semantics
    - workflow_recovery
observability:
  level: MODERATE_FOR_POINTER_OPERATIONS_LOW_FOR_AUTH_QUOTA_AND_TRANSPORT
  exposed:
    - channel_id_and_name
    - public_archived_metadata
    - message_timestamp_and_permalink
    - pagination_cursor
    - coarse_error_class
  hidden:
    - raw_HTTP_status_headers_and_body
    - request_id_retry_count_and_latency
    - auth_identity_scope_and_token_class
    - app_distribution_class_and_live_quota
    - audit_event
portability:
  Slack_contract: MEDIUM
  connector_wrapper: MEDIUM_LOW
  alternate_platforms: UNPROVEN
failure_behavior:
  observed: INVALID_CHANNEL_FAILED_WITHOUT_UNRELATED_CONTENT_AND_VALID_READ_RECOVERED
  risk: CHANNEL_NOT_FOUND_CONFLATES_ABSENCE_WORKSPACE_MISMATCH_AND_ACCESS_DENIAL
direct_cost_and_quota:
  incremental_paid_cost_observed_usd: 0
  exact_workspace_plan_connector_allocation_and_live_quota: UNKNOWN
```

## Strongest objection

The successful post and readback shared one opaque provider path. A connector defect,
broad user token, hidden retry, or transformed result could create false agreement while
concealing duplicate effects or excessive authority. The campaign did not test private
boundaries, rate limits, timeouts, outages, archived channels, known-resource access
denial, audit logs, or independent verification.

## Strongest falsifier

Revise or reject this adoption if a known-valid public channel returns the same coarse
error without a documented access change; an authorized pointer post duplicates after an
ambiguous response; readback mismatches the returned channel or timestamp; unauthorized
private content appears; operator credential ferrying becomes necessary; or a distinct
verifier cannot reproduce the claimed bounded result.

## Consumer and next campaign

Ratatoskr and Olrun may consume this only as a gated connector capability for an exact
WorkItem. No ConsumerAck is claimed. The next candidate nomination is a read-only Gmail
search and message-metadata connector campaign; no Gmail access or phase-1 probe occurred
on this wake.

## Honest flaw

This is a four-wake, single-workspace, low-volume campaign with one successful Slack
write. It provides no statistically meaningful reliability estimate and no proof of
least privilege, independent verification, stable quota, provider-native raw semantics,
retention, exactly-once behavior, or durable workflow guarantees. Same-provider binding
weight remains zero.
