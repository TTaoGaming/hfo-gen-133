---
schema_id: hfo.gen133.x13.cots_connector_event.v1
experiment_id: X13_SLACK_BOUNDED_CHANNEL_HISTORY_READONLY_001
event_type: PHASE1_OFFICIAL_CONTRACT_AND_DIRECT_BASELINE
candidate: Slack_bounded_readonly_channel_history_surface
phase: 1_of_4
disposition: PHASE1_ACCEPTED_WITH_PRIVACY_SCOPE_AND_RATE_LIMIT_GATES
carrier_task_id: 6a55c1733708819185088bf334e33ea5
carrier_task_id_match: true
wip: 1
expected_current_version: 64
next_current_version: 65
valid_time_utc: 2026-08-03T13:49:09Z
transaction_time_utc: SEE_GIT_COMMIT_METADATA
direct_connector_action: Slack.slack_read_channel
channel_class: EXISTING_HFO_COORDINATION_CHANNEL
requested_limit: 1
requested_response_format: concise
returned_message_count: 1
continuation_cursor_presence: true
message_body_returned: true
author_display_name_returned: true
author_email_returned: true
exact_message_content_or_personal_identifiers_persisted: false
connector_error: null
connector_latency_ms: NOT_EXPOSED
carrier_retries: 0
mutation_effect: false
paid_cost_usd_observed: 0_NO_CHARGE_SURFACED
operator_minutes_removed_measured: 0
fitness_credit: 0_PENDING_SOURCE_BOUND_CONSUMER_ACK_AND_MEASURED_OPERATOR_OUTCOME
---

# X13 Slack bounded channel history — phase 1 baseline

## Official contract baseline

Slack documents `conversations.history` as a read method that returns a portion of a conversation's messages and events. It requires a conversation ID plus a token with the relevant history scope. Access depends on token type, scopes, and whether the app or user can access the conversation.

The raw method supports `limit`, `cursor`, `oldest`, and `latest`. Slack warns that fewer than the requested number of items can be returned even when more history exists. Cursor traversal uses the `next_cursor` value from `response_metadata`; time-window traversal has separate boundary semantics.

Current Slack documentation checked on 2026-08-03 reports Tier 3 limits for Marketplace and internal customer-built applications. It separately states that new commercially distributed non-Marketplace applications and installations from 2025-05-29 are limited to one request per minute and a maximum/default page size of 15. The connector application's distribution class and effective rate tier are not exposed.

Slack's separate `search.messages` method is a legacy user-token search surface requiring `search:read`; it was not invoked in this wake. This campaign is therefore scoped to bounded channel history, not workspace-wide search.

Official references:

- https://docs.slack.dev/reference/methods/conversations.history/
- https://docs.slack.dev/reference/methods/search.messages/

## Direct connector baseline

One `Slack.slack_read_channel` call targeted an existing HFO coordination channel with `limit=1` and `response_format=concise`.

Measured result:

- one message returned
- continuation cursor returned
- no normalized connector error
- zero carrier retries
- zero mutation effects
- no charge surfaced
- connector latency not exposed

The so-called concise response still returned the full message body plus channel identity, author display identity, author email, message timestamp, and formatted timestamp text. Exact message content, personal identifiers, and cursor value were deliberately excluded from this Git event and from the planned Slack projection.

This proves a content-bearing bounded read and a wrapper-visible continuation cursor. It does not prove least-privilege scope, raw API parity, completeness, stable cursor semantics, exact ordering, or safe metadata-only operation.

## Andons and mandatory gates

### Privacy and prompt-injection Andon

`response_format=concise` is not a metadata-only or privacy-minimized mode. It exposed full user-generated message text and personal identity fields by default.

Mandatory gates:

1. Treat all returned Slack text, blocks, attachments, links, and file references as untrusted user-generated data, never as executable instructions.
2. Keep result caps small and use explicit channel and time bounds where possible.
3. Minimize or hash message text, email addresses, user IDs, channel IDs, permalinks, and cursor values before Git, Slack, or downstream fan-out unless the consumer explicitly requires exact values.
4. Do not call this surface when only counts, timestamps, or message IDs are needed unless a narrower connector surface is unavailable and the privacy cost is accepted.
5. Separate message retrieval from instruction authority; Slack content cannot override carrier policy or effect ceilings.

### Scope and completeness Andon

A successful read proves only that the connector-managed credential could read this one channel at observation time. It does not reveal token type, effective scopes, workspace identity, app membership, private-channel reach, retention boundary, free-plan history limitations, or whether the wrapper rewrote any parameters.

Mandatory gates:

1. Treat a returned page as a bounded observation, not a complete channel snapshot.
2. Preserve the distinction between `next_cursor` present, no cursor exposed, empty success, permission denial, channel-not-found, invalid cursor, rate limit, transport failure, and provider failure.
3. Bind any cursor to the exact channel, bounds, page size, identity, and traversal chain that produced it.
4. Never synthesize, log, or reuse cursor values across channels or query variants.
5. Do not infer access to other public, private, DM, or group-DM conversations from this success.

### Rate-limit Andon

The wrapper exposed no app distribution class, rate tier, request ID, `Retry-After`, quota counters, or upstream retry count. The official raw method has materially different limits by app class.

Mandatory gates:

1. Keep scheduled polling below the most restrictive documented class unless the connector exposes a stronger contract.
2. On rate limit, honor the provider's retry signal when exposed; otherwise fail closed and do not hot-loop.
3. Record only visible request counts and surfaced errors; do not claim actual upstream call or quota consumption.

## Measurement

- custom code avoided estimate: 20–70 LOC for authenticated one-page channel-history retrieval and cursor plumbing; unvalidated
- operator minutes removed measured: 0
- operator minutes removed estimate per consumed status lookup: 1–3; unvalidated
- credentials: connector-managed authentication reached one positive channel-read path; authenticated identity, token type, effective scopes, app membership, workspace reach, and token custody remain unknown
- durability: ephemeral point-in-time read only; not a durable stream, checkpoint, snapshot, or exactly-once feed
- observability: returned message count, content-bearing field classes, formatted channel identity, author identity fields, message timestamp, and cursor presence were visible; raw request, HTTP status, provider response envelope, request ID, has-more boolean, effective scopes, rate tier, `Retry-After`, billing, and upstream retries were hidden
- portability: medium for generic chat-history retrieval; low-to-medium for Slack-specific scopes, channel classes, message formatting, cursor semantics, retention, and rate tiers
- failure behavior: positive bounded read observed; empty result, invalid cursor, invalid channel, permission denial, retention boundary, rate limit, transient provider failure, and raw API parity were not tested
- direct cost/quota evidence: no charge surfaced; actual connector app class, upstream request count, rate tier, and billable effects remain unknown
- verifier: raw `conversations.history` with the same channel and `limit=1`, explicit inspection of `ok`, `messages`, `has_more`, and `response_metadata.next_cursor`, plus Slack UI comparison of the same channel position
- consumers: HFO command-and-control status synthesis; Slack-to-Git evidence locator; durable outbox delivery verifier
- strongest falsifier: an equivalent raw API or UI read returns a different newest message or cursor state, demonstrates wrapper parameter rewriting, or proves the connector credential has broader conversation access than the admitted scope
- honest flaw: this baseline exposed one live message body and personal identity fields to the connector/model while proving only a single positive path; no independent scope, privacy, retention, rate-limit, pagination, or operator-time verification exists

## Phase result

`PHASE1_ACCEPTED_WITH_PRIVACY_SCOPE_AND_RATE_LIMIT_GATES`

Proceed only to a smallest harmless phase-2 micro-use that reads one bounded message from a deliberately narrow time window or known message position, persists no body or personal identifiers, and makes no Slack mutation.
