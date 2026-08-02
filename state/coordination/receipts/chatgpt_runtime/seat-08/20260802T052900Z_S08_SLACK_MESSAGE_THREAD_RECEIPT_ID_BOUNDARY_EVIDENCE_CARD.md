---
schema_id: hfo.gen133.s08.evidence_card.v1
callsign: S08_Research_Candidate_Scout
carrier_task_id_expected: 6a526109ba348191b5f23ad3172ad568
carrier_task_id_observed: 6a526109ba348191b5f23ad3172ad568
carrier_task_id_match: true
wip: 1
lane: agent_runtime_cots_capabilities
question_status: CHANGED
question_source:
  path: state/coordination/experiments/cots_connector_x13/CURRENT.md
  observed_blob_sha: 875567dc20a1e59a1697ed0ae19d52444b69f6d7
  next_campaign: X13_SLACK_NATIVE_MESSAGE_RECEIPT_001
candidate: Slack.slack_send_message_plus_Slack.slack_read_thread_connector_surface
candidate_version: connector_schema_observed_2026-08-02
bounded_uncertainty: DOES_THE_SEND_SURFACE_RETURN_A_STABLE_MACHINE_ADDRESSABLE_CHANNEL_ID_AND_PARENT_MESSAGE_TS_SUFFICIENT_FOR_DETERMINISTIC_THREAD_READBACK_OR_ONLY_A_HUMAN_PERMALINK
decision: REVISE
valid_time_utc: 2026-08-02T05:29:00Z
transaction_time_utc: SEE_GIT_COMMIT_METADATA
review_expiry_utc: 2026-08-09T05:29:00Z
consumer:
  - X13_SLACK_NATIVE_MESSAGE_RECEIPT_001_PHASE1
verifier:
  - S04_EXACT_CARD_STRUCTURAL_PREFLIGHT
  - X13_DISTINCT_NONPRODUCER_OR_COMMIT_PINNED_READER
fitness_credit: 0_PENDING_EXACT_WORKITEM_CONSUMPTION
privacy_class: SANITIZED_INTERNAL
world_effect_ceiling: RESEARCH_CARD_PLUS_REQUIRED_SANITIZED_SLACK_POINTER_ONLY
sealed: true
---

# S08 evidence card — Slack message/thread receipt identifier boundary

## Decision

`REVISE` the planned X13 Slack-native message receipt campaign before treating a successful send or returned permalink as a durable machine receipt.

## One bounded question

Does the current connected Slack send surface return the exact `channel_id` and parent `message_ts` needed to reply to and read back the same thread deterministically, or does its public connector contract guarantee only a human-facing message link?

## Dated evidence

1. **Gen-133 queue, observed 2026-08-02:** X13 `CURRENT.md` version 32 marks the GitHub Contents campaign complete and plans `X13_SLACK_NATIVE_MESSAGE_RECEIPT_001`, phase 1/4. Exact source: `state/coordination/experiments/cots_connector_x13/CURRENT.md`, blob `875567dc20a1e59a1697ed0ae19d52444b69f6d7`.
2. **Connected Slack tool contract, observed 2026-08-02:** `Slack.slack_send_message` accepts `channel_id`, optional `thread_ts`, and promises to return a message link. Its exposed contract does not promise structured `channel_id` or `message_ts` fields. `Slack.slack_read_thread` separately requires both `channel_id` and a parent `message_ts` in Slack timestamp format.
3. **Slack official `chat.postMessage` contract, checked 2026-08-02:** the underlying API success response normally includes `channel` and timestamp ID `ts`; replies require the parent message `ts` through `thread_ts`. Source: https://api.slack.com/methods/chat.postMessage
4. **Slack official `conversations.replies` contract, checked 2026-08-02:** deterministic thread retrieval requires both conversation `channel` and message `ts`. Source: https://api.slack.com/methods/conversations.replies
5. **Slack official `chat.getPermalink` contract, checked 2026-08-02:** Slack documents conversion from `channel + message_ts` to a permalink. It does not document the permalink as a stable inverse API or contractual replacement for retaining the original identifiers. Source: https://api.slack.com/methods/chat.getPermalink

## Supported claims

- Slack's underlying Web API has a machine-addressable receipt pair: conversation/channel ID plus message timestamp `ts`.
- Thread replies must use the parent message timestamp, not an arbitrary reply timestamp.
- The connected send wrapper can be invoked with `thread_ts`, and the connected thread reader requires `channel_id + message_ts`.
- The wrapper's exposed contract guarantees a returned message link, but does not explicitly guarantee structured raw identifiers.
- Therefore a successful wrapper call or permalink alone is not yet proof of deterministic thread round-trip capability.

## Excluded claims

- The wrapper definitely suppresses raw `channel` and `ts` in its live result.
- A Slack permalink can always be safely and losslessly inverted into the exact API identifiers.
- One successful send proves readback, thread reply, idempotency, deduplication, authorship, durability, or ConsumerAck.
- The live token identity, token type, granted scopes, app membership, workspace plan, retry behavior, request count, rate-limit headers, or Slack Connect status are known.
- Message delivery is exactly once or transactionally coupled to the Git receipt.

## Required X13 phase-1 revision

For the smallest harmless message probe, preserve the exact live wrapper result and classify it as one of:

1. `STRUCTURED_RECEIPT`: returned `channel_id/channel` and `message_ts/ts` are directly exposed;
2. `LINK_ONLY_VERIFIED`: only a link is returned, but a separately recorded and reproducible derivation yields the exact pair and `slack_read_thread(channel_id, message_ts)` reads back the exact body;
3. `LINK_ONLY_UNVERIFIED`: a link exists but the exact pair or readback cannot be established;
4. `SEND_FAILED`: record the normalized permission/error class without retry inflation.

A permalink may be retained as a human pointer, but the campaign should not call it a durable machine receipt unless the exact identifier pair and body readback are bound.

## License / terms uncertainty

- Slack API documentation is public; live use remains governed by the workspace, app installation, permissions, Slack platform terms, and plan limits.
- No new account, app, scope grant, installation, terms acceptance, or Slack Connect action was performed.
- Exact live credential custody and least-privilege scope remain unknown.

## Cost and operator-minute estimate

- Direct paid cost observed for this research card: `$0` surfaced.
- X13 phase-1 operator burden estimate: `1–3 minutes` to inspect and retain returned fields, then perform one exact readback; unvalidated until measured.
- Custom code avoided if structured IDs are exposed: approximately `10–35 LOC` of permalink parsing and reconciliation logic, unvalidated and not credited.

## Strongest objection

X13 can answer this directly with one harmless live message, making documentation analysis secondary. That objection is valid; this card earns value only if it prevents the campaign from laundering a human permalink into a machine-round-trip claim.

## Falsifier

A live call on the same connector version returns structured `channel_id/channel` and parent `message_ts/ts`, followed by exact `slack_read_thread` body readback using those fields. That would falsify the concern that only a human link is exposed and permit `ADMIT` for the bounded receipt pair.

## Honest flaw

No new Slack probe was executed for this card. The connector schema is a contract observation, not a live response census. Official Slack API behavior does not guarantee wrapper field preservation.
