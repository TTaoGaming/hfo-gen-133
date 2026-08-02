---
schema_id: hfo.gen133.x13.cots_connector_event.v1
experiment_id: X13_SLACK_NATIVE_MESSAGE_RECEIPT_001
phase: 4_of_4
event_kind: ADOPTION_DECISION
prior_current_version: 35
expected_next_current_version: 36
carrier_task_id: 6a55c1733708819185088bf334e33ea5
carrier_task_id_match: true
candidate: Slack_native_message_send_and_thread_receipt_surface
decision: ADOPT_WITH_GATES
campaign_status: COMPLETE
candidate_invocations_this_wake: 0
effect_ceiling: DECISION_GIT_EVENT_CURRENT_ADVANCE_AND_ONE_SHORT_NON_SECRET_SLACK_DECISION_RECEIPT_ONLY
valid_time_utc: 2026-08-02T08:46:43Z
transaction_time_utc: SEE_GIT_COMMIT_METADATA
sealed: true
---

# X13 phase-4 decision — Slack native message and thread receipt

## Decision

`ADOPT_WITH_GATES` for bounded, short, non-secret HFO control-plane messages and exact receipt reads keyed by Slack's server-returned channel ID plus parent message timestamp.

Do **not** use Slack as immutable event storage, an exactly-once delivery bus, a durable workflow runtime, or an independently verified system of record.

## Direct campaign evidence

- Phase 1: one exact read-only lookup returned the expected existing parent and no replies.
- Phase 2: one short non-secret message send returned a channel and timestamp; exact readback by that key preserved the submitted user text while exposing connector-added attribution.
- Phase 3: one privacy-safe invalid-channel lookup failed closed with `channel_not_found`, returned no thread content, and produced no write side effect.
- Phase 4: decision-only; no additional Slack capability call was required.

## Official contract baseline checked 2026-08-02

- `chat.postMessage` requires `chat:write`, accepts a channel target, and uses special rate limits that generally allow about one message per second per channel: https://docs.slack.dev/reference/methods/chat.postMessage/
- `conversations.replies` requires channel plus parent `ts`, is cursor paginated, and returns the parent alone when there are no replies: https://docs.slack.dev/reference/methods/conversations.replies/
- Slack returns HTTP 429 with `Retry-After` when a Web API rate limit is exceeded: https://docs.slack.dev/apis/web-api/rate-limits/
- Slack messages are mutable and retention-policy dependent; edits, deletion, and automatic retention deletion are supported: https://slack.com/help/articles/202395258-Edit-or-delete-messages and https://slack.com/help/articles/203457187-Customize-data-retention-in-Slack

## Measurements

- Custom code avoided estimate: authenticated post plus receipt-key extraction `30–90 LOC`; authenticated thread fetch plus basic pagination `35–100 LOC`; unvalidated and non-additive.
- Operator relay minutes: `0`.
- Operator minutes removed measured: `0`.
- Future relief estimate: `1–3 minutes` per bounded receipt, unvalidated.
- Operator-supplied credentials: `0`.
- Live identity, token type, scopes, workspace identity, membership basis, and credential custody: `UNKNOWN`.
- Durability: mutable workspace archive subject to retention, edit, deletion, plan, and admin policy.
- Observability: medium for returned channel, timestamp, rendered text, author/time, and reply count; low for raw HTTP status, headers, request ID, token/scopes, retry metadata, workspace, and rate class.
- Portability: medium-low because IDs, timestamp receipt keys, threading, scope names, rendering, attribution, and errors are Slack-specific.
- Failure behavior: synthetic invalid or unreachable channel failed closed, but `channel_not_found` did not disambiguate nonexistence, wrong workspace, or missing permission.
- Direct cost evidence: `$0` surfaced; upstream request count, quota class, remaining allowance, and billing counters were not exposed.
- Fitness credit: `0` pending source-bound ConsumerAck and measured operator outcome.

## Mandatory gates

1. Use the server-returned channel ID and parent timestamp as the canonical receipt key; never reconstruct the timestamp from a message URL.
2. Compare submitted user text separately from Slack- or connector-added rendering and attribution.
3. Keep automated posts short, human-readable, non-secret, source-bound, and idempotency-aware.
4. Sanitize private channel names, IDs, timestamps, user IDs, emails, links, query parameters, and message content before Git persistence.
5. Treat `channel_not_found` as ambiguous existence, workspace, or permission failure; do not blindly retry the same identifier.
6. Require separate authorized workspace, channel-discovery, or membership evidence before classifying a routing or permission failure.
7. On HTTP 429, honor `Retry-After`; do not blind retry.
8. Same-connector readback is structural reconciliation only, not independent delivery verification.
9. Require a source-bound ConsumerAck before claiming operator relief or fitness credit.
10. Do not claim immutability, durable workflow execution, independent delivery, exactly-once behavior, or system-of-record status.

## Verifier, consumer, falsifier, flaw

- Verifier: raw Slack Web API or a distinct authorized client reading the same channel and parent timestamp with explicit workspace and scope evidence.
- Consumer: HFO Slack control-plane readers and downstream Git-first coordination consumers.
- Strongest falsifier: a distinct authorized Slack client cannot retrieve the phase-2 parent by returned channel plus timestamp, or returns materially different user payload or replies omitted by this connector.
- Honest flaw: the campaign did not test a real private-channel permission denial, `not_in_channel`, archived channel, missing parent, HTTP 429, edit/delete drift, retention expiry, or independent cross-client readback.

## Next campaign

Start `X13_GOOGLE_CALENDAR_FREEBUSY_READONLY_001` on the next wake. Phase 1 should baseline the official Google Calendar Freebusy contract and the direct connector's bounded read-only capability. No event creation, invitation, response, edit, or deletion is admitted during phase 1.
