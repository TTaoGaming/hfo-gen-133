---
schema_id: hfo.gen133.s08.evidence_card.v1
seat: S08_RESEARCH_AND_CANDIDATE_SCOUT
task_id_expected: 6a526109ba348191b5f23ad3172ad568
task_id_match: true
wip: 1
lane: agent_runtime_cots_capabilities
bounded_uncertainty: DOES_ONE_SLACK_READ_CHANNEL_WRAPPER_INVOCATION_PROVE_ONE_UPSTREAM_CONVERSATIONS_HISTORY_CALL_WHEN_CONCISE_OUTPUT_INCLUDES_AUTHOR_EMAIL
decision: REVISE
candidate: Slack.slack_read_channel_runtime_schema_observed_2026-08-05
candidate_version: CONNECTOR_BUILD_AND_UPSTREAM_MAPPING_NOT_EXPOSED
queue_source: state/coordination/experiments/cots_connector_x13/CURRENT.md@v113
consumer: X13_SLACK_READ_CHANNEL_READONLY_004_PHASE2_AND_HFO_COTS_CAPABILITY_INVENTORY
verifier: DISTINCT_SYNTHETIC_WORKSPACE_RAW_SLACK_AND_CONNECTOR_IDENTITY_ENRICHMENT_CALL_GRAPH_VERIFIER
valid_time_utc: 2026-08-05T14:27:37Z
recorded_time_utc: 2026-08-05T14:27:37Z
expiry_utc: 2026-08-12T14:27:37Z
paid_cost_usd_observed: 0_NO_CHARGE_SURFACED
operator_minutes_this_pass: 0
producer_revision_estimate_minutes: 10_to_20
synthetic_verification_estimate_minutes: 30_to_60
fitness_credit: 0_PENDING_EXACT_WORKITEM_CONSUMPTION_AND_CONSUMER_ACK
---

# REVISE — AUTHOR EMAIL MAKES THE UPSTREAM CALL GRAPH UNKNOWN

## Exact changed question

X13 phase 1 recorded one `Slack.slack_read_channel` wrapper invocation, one returned message, `phase1_secondary_reads: 0`, and a `concise` result that still surfaced the message author's email. The active queue now treats the surface as a bounded one-call channel-history candidate.

The bounded uncertainty is whether one wrapper invocation proves one upstream Slack request and one history-quota debit when the wrapper output contains identity data absent from the documented ordinary `conversations.history` message shape.

## Current primary evidence

Checked 2026-08-05:

1. Slack `conversations.history` documents ordinary returned messages with a `user` identifier, message text, and `ts`; its required scopes are the relevant `*:history` scopes. The documented ordinary response does not attach the author's email to the message object.
   - https://docs.slack.dev/reference/methods/conversations.history/
2. Slack documents user email on user-profile surfaces such as `users.info` and `users.list`. Access to the `email` field requires `users:read.email` in addition to `users:read` for modern apps.
   - https://docs.slack.dev/reference/methods/users.info
   - https://docs.slack.dev/reference/methods/users.list/
   - https://docs.slack.dev/reference/scopes/users.read.email/
3. The observed connector schema exposes channel, bounds, limit, cursor, and response-format controls, but no control or declaration for identity hydration, profile caching, upstream request count, effective scopes, or quota accounting.
4. X13 phase 1 itself says `concise` output surfaced author email while raw response shape, scopes, true call count, retry graph, and quota remained hidden.

## Supported claims

- `concise` is not a data-minimization guarantee for this connector surface.
- Author email in the formatted result is connector-added or connector-sourced enrichment relative to the documented ordinary `conversations.history` message example.
- One visible wrapper invocation does not prove one upstream Slack API request, one quota debit, or zero profile/cache lookups.
- `phase1_secondary_reads: 0` is supportable only as `NO_SECONDARY_READ_VISIBLE_TO_THE_CARRIER`; it is not supportable as an upstream-call-graph fact.
- The result must be treated as combining message content with potentially separately authorized identity data.

## Excluded claims

This card does not establish that the connector called `users.info`, called `users.list`, made any specific number of hidden calls, used the same Slack token for enrichment, possesses `users:read.email`, bypassed Slack scope checks, or performed a live network lookup. The email could have come from a connector-side directory, installation metadata, prior cache, search index, or another authorized source.

It also does not establish the connector's app class, effective principal, workspace membership, cache freshness, retention policy, telemetry, rate-limit tier, or whether one wrapper call consumes one or several provider allowances.

## Required revision

```text
WRAPPER_INVOCATIONS=1_OBSERVED
UPSTREAM_SLACK_REQUEST_COUNT=UNKNOWN
UPSTREAM_HISTORY_QUOTA_DEBITS=UNKNOWN
IDENTITY_ENRICHMENT_SOURCE=UNKNOWN
SECONDARY_READS=0_CARRIER_VISIBLE_ONLY
CONCISE_OUTPUT_DATA_MINIMIZATION=FALSE_OBSERVED
AUTHOR_EMAIL_RETENTION=FORBIDDEN_BY_DEFAULT
```

Revise X13 phase 2 and the COTS inventory so cost, rate-limit, retry, and call-count estimates use wrapper invocations only. Do not translate them into provider request counts or quota consumption without connector telemetry or a controlled raw comparison.

For operational use, require an output mode that suppresses email or a redaction step before any persistence, forwarding, or WorkItem attachment. Redaction is not proof that the connector lacked broader identity scopes.

## License and terms uncertainty

Slack API use remains governed by Slack platform terms, workspace policy, OAuth grants, and any connector-provider terms. Documentation copyright or reuse license was not evaluated because no documentation text is being redistributed beyond short factual paraphrase. Connector source, build identifier, caching policy, subprocesses, and data-retention terms are not exposed and remain unbound.

## Strongest objection

The connector may already hold a workspace user directory in memory, so formatting an email could add no network call and no marginal Slack quota debit.

That objection is valid and reinforces the decision: it means the enrichment source and marginal call count are unknown, not zero. Cached enrichment also creates separate freshness, scope, and retention questions.

## Falsifier

Revise this card toward `ADMIT` only if a version-bound controlled test in a synthetic authorized workspace provides connector telemetry or an independently captured request graph showing all upstream Slack calls for one `slack_read_channel` invocation, the identity source, effective scopes, cache behavior, retry count, and quota headers, while demonstrating a mode that omits email from output.

Retire the one-call accounting claim if the trace shows any hidden profile/directory request, retry, fallback, or unreported provider call.

## Verifier protocol

`DISTINCT_SYNTHETIC_WORKSPACE_RAW_SLACK_AND_CONNECTOR_IDENTITY_ENRICHMENT_CALL_GRAPH_VERIFIER`

Use a synthetic workspace and synthetic users only. Compare:

- raw `conversations.history` for one known synthetic message;
- raw `users.info` or `users.list` behavior with and without `users:read.email`;
- one connector `slack_read_channel` invocation;
- connector/network telemetry sufficient to enumerate requests, cache hits, retries, and scopes;
- detailed versus concise output for email suppression.

No production message body, personal email, private channel, or real-user profile is needed.

## Cost and operator estimate

- this research pass: USD 0 surfaced; 0 operator minutes requested
- producer metadata revision: 10–20 minutes
- synthetic trace and comparison: 30–60 minutes if a test workspace and telemetry already exist
- account creation, scope acceptance, paid upgrade, or new installation is outside this card and not authorized

## Decision

`REVISE`

The Slack reader remains catalogable as a bounded human-reviewed read surface, but its invocation count cannot be used as provider-call, quota, or privacy-scope accounting while formatted output includes author email and the enrichment path is opaque.
