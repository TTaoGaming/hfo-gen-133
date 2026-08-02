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
candidate_version: connector_schema_and_live_result_observed_2026-08-02
bounded_uncertainty: DOES_THE_SEND_SURFACE_RETURN_A_STABLE_MACHINE_ADDRESSABLE_CHANNEL_ID_AND_PARENT_MESSAGE_TS_SUFFICIENT_FOR_EXACT_PARENT_READBACK
decision: ADMIT
admitted_scope: STRUCTURED_MESSAGE_RECEIPT_PAIR_PLUS_EXACT_PARENT_BODY_READBACK
valid_time_utc: 2026-08-02T05:29:00Z
last_evidence_time_utc: 2026-08-02T05:31:10Z
transaction_time_utc: SEE_GIT_COMMIT_METADATA
review_expiry_utc: 2026-08-09T05:29:00Z
consumer:
  - X13_SLACK_NATIVE_MESSAGE_RECEIPT_001_PHASE1
verifier:
  - S04_EXACT_CARD_STRUCTURAL_PREFLIGHT
  - X13_DISTINCT_NONPRODUCER_OR_COMMIT_PINNED_READER
fitness_credit: 0_PENDING_EXACT_WORKITEM_CONSUMPTION
privacy_class: SANITIZED_INTERNAL
world_effect_ceiling: ONE_REQUIRED_SANITIZED_SLACK_POINTER_PLUS_READ_ONLY_EXACT_PARENT_READBACK
sealed: true
---

# S08 evidence card — Slack structured message receipt and parent readback

## Decision

`ADMIT` the current connected Slack surface for the narrow capability: one sent message returns a structured `(channel_id, message_ts)` receipt pair, and `slack_read_thread(channel_id, message_ts)` reads back the exact parent body.

Do not expand this admission to thread replies, exactly-once delivery, idempotency, independent verification, authorship identity, durable workflow state, or ConsumerAck.

## One bounded question

Does the current connected Slack send surface return the exact `channel_id` and parent `message_ts` needed for deterministic readback of the same parent message?

## Dated evidence

1. **Gen-133 queue, observed 2026-08-02:** X13 `CURRENT.md` version 32 marks the GitHub Contents campaign complete and plans `X13_SLACK_NATIVE_MESSAGE_RECEIPT_001`, phase 1/4. Exact source: `state/coordination/experiments/cots_connector_x13/CURRENT.md`, blob `875567dc20a1e59a1697ed0ae19d52444b69f6d7`.
2. **Connected Slack tool contract, observed 2026-08-02:** `Slack.slack_send_message` accepts `channel_id`, optional `thread_ts`, and promises a message link. `Slack.slack_read_thread` requires `channel_id` and parent `message_ts`.
3. **Live send receipt, 2026-08-02T05:31:10Z:** the required sanitized Git pointer post returned:
   - `message_link`: `https://hfonetwork.slack.com/archives/C0BGNGPJFHU/p1785648670384069`
   - `message_context.channel_id`: `C0BGNGPJFHU`
   - `message_context.message_ts`: `1785648670.384069`
4. **Live exact parent readback, 2026-08-02 immediately after send:** `Slack.slack_read_thread(channel_id="C0BGNGPJFHU", message_ts="1785648670.384069")` returned the parent message with the same timestamp and exact material body; no replies were present.
5. **Slack official `chat.postMessage` contract, checked 2026-08-02:** successful underlying API responses include conversation `channel` and timestamp ID `ts`; thread replies use the parent `ts` via `thread_ts`. Source: https://api.slack.com/methods/chat.postMessage
6. **Slack official `conversations.replies` contract, checked 2026-08-02:** deterministic thread retrieval requires conversation `channel` plus message `ts`. Source: https://api.slack.com/methods/conversations.replies
7. **Slack official `chat.getPermalink` contract, checked 2026-08-02:** Slack documents forward conversion from `channel + message_ts` to a permalink. Source: https://api.slack.com/methods/chat.getPermalink

## Supported claims

- This live connector result exposes structured `message_context.channel_id` and `message_context.message_ts` in addition to a human permalink.
- The returned pair can be passed directly to the connected thread reader.
- The exact parent body and timestamp were read back once from the same channel.
- X13 phase 1 can classify this result as `STRUCTURED_RECEIPT_WITH_EXACT_PARENT_READBACK`.
- Retaining the structured pair avoids relying on permalink inversion for this bounded path.

## Excluded claims

- A thread reply was posted or read back.
- A reply's returned timestamp is correctly distinguished from its parent timestamp in every wrapper path.
- Delivery is exactly once, idempotent, transactional with Git, independently verified, or durable across workspace deletion/retention changes.
- The live token identity, token type, granted scopes, app membership, workspace plan, retries, underlying request count, rate-limit headers, or Slack Connect status are known.
- The displayed sender identity proves a stable bot/user authorship contract.
- One readback is a ConsumerAck or an external outcome.

## Required X13 phase-1 claim ceiling

`CONNECTED_SLACK_SEND_RETURNED_STRUCTURED_CHANNEL_AND_PARENT_TS_AND_SAME_CONNECTOR_THREAD_READER_RETURNED_THE_EXACT_PARENT_BODY_ONCE.`

Before phase 2 or a thread-reply claim, X13 should separately test one harmless reply using the returned parent `message_ts`, retain both parent and reply timestamps, and read back both without broadcasting.

## License / terms uncertainty

- Slack API documentation is public; live use remains governed by workspace policy, app installation, permissions, Slack platform terms, retention, and plan limits.
- No new account, app, scope grant, installation, terms acceptance, or Slack Connect action was performed.
- Exact live credential custody and least-privilege scope remain unknown.

## Cost and operator-minute estimate

- Direct paid cost surfaced: `$0`.
- Measured operator relay minutes: `0`; the scheduled carrier performed the send and readback directly.
- Estimated manual equivalent avoided for copying a link, extracting identifiers, and confirming the parent: `1–3 minutes`, unvalidated and not credited.
- Potential custom parsing/reconciliation avoided by structured receipt fields: `10–35 LOC`, unvalidated and not credited.

## Strongest objection

The send and readback used the same connector and authenticated context, so this proves a functional round trip, not independent verification or cross-client portability. Workspace retention, hidden retries, or wrapper changes could still invalidate durability claims.

## Falsifier

A repeat on the same connector version omits `message_context`, returns a mismatched timestamp/channel, or `slack_read_thread` returns a different parent body for the recorded pair. Any such result revises this admission to `UNKNOWN` or `REVISE`.

## Honest flaw

The exact readback confirms one parent message only. No thread reply, cross-client check, permission failure, retry, rate-limit, deletion, retention, or Slack Connect path was tested.
