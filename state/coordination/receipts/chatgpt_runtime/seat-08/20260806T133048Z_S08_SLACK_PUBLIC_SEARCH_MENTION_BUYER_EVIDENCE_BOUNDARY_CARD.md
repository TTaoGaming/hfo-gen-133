---
schema_id: hfo.gen133.s08.evidence_card.v1
seat: S08_RESEARCH_AND_CANDIDATE_SCOUT
task_id_expected: 6a526109ba348191b5f23ad3172ad568
task_id_observed: 6a526109ba348191b5f23ad3172ad568
task_id_match: true
wip: 1
valid_time_utc: 2026-08-06T13:30:48Z
expiry_utc: 2026-08-13T13:30:48Z
decision: REVISE
lane: DISTRIBUTION_AND_BUYER_EVIDENCE
bounded_uncertainty: CAN_A_SLACK_PUBLIC_SEARCH_MATCH_OR_RESULT_COUNT_BE_CLASSIFIED_AS_BUYER_OR_MARKET_DEMAND_EVIDENCE
candidate: api_tool.Slack.slack_search_public schema observed 2026-08-06 plus queued campaign X13_SLACK_SEARCH_PUBLIC_READONLY_010
consumer: X13_SLACK_SEARCH_PUBLIC_READONLY_010_PHASE1_RESULT_SEMANTICS_GATE
verifier: DISTINCT_SAME_PRINCIPAL_RAW_SLACK_SEARCH_AND_CONTROLLED_PUBLIC_CHANNEL_FIXTURE_VERIFIER
fitness_credit: 0_PENDING_EXACT_WORKITEM_CONSUMPTION_DISTINCT_VERIFICATION_AND_CONSUMER_ACK
---

# REVISE — Slack public-search matches are mention-discovery, not buyers or demand

## Queue delta and exact candidate

The changed Gen-133 queue surface closes `X13_GITHUB_CODE_SEARCH_READONLY_009` and names `X13_SLACK_SEARCH_PUBLIC_READONLY_010` as the next phase-1 campaign. Queue source: `state/coordination/experiments/cots_connector_x13/CURRENT.md`, blob `3e792fe1d7805856dbb47d3c679e9fab9d065c90`, observed on canonical branch `agent/gen133-bootstrap-20260730`.

Exact candidate surface: `api_tool.Slack.slack_search_public`, schema observed 2026-08-06. The exposed connector searches messages/files in public Slack channels, accepts query/date/channel/author modifiers, can include or omit context, and returns bounded result sets. The underlying Slack endpoint, token type, exact scope, UI-search preferences, plan behavior, and raw response envelope are not exposed by this wrapper.

## Primary-source finding

Slack documents `search.messages` as returning messages matching a query, with page size, pagination, and sorting by score or timestamp. Slack also states that user-token results can be affected by search filters set in the Slack UI and that multiple matching messages in close proximity may collapse to one returned match. The current developer page labels this raw method legacy and recommends the Real-time Search API instead.

Sources retrieved 2026-08-06:

1. Slack Developer Docs, `search.messages`: https://docs.slack.dev/reference/methods/search.messages/
2. Slack Help, `Search in Slack`: https://slack.com/help/articles/202528808-Search-in-Slack-Search-in-Slack-
3. Slack Help, `Set your search preferences`: https://slack.com/help/articles/4402305240723-Set-your-search-preferences

## Supported claims

```text
PUBLIC_SEARCH_CALL_SUCCEEDED = WRAPPER_OBSERVATION_ONLY
NONEMPTY_RESULT = AT_LEAST_ONE_VISIBLE_MATCH_RETURNED
RESULT_PERMALINK = CANDIDATE_FOR_HUMAN_SOURCE_REVIEW
ZERO_RESULT = ZERO_MATCHES_RETURNED_BY_THIS_BOUNDED_CALL
MENTION_DISCOVERY = ADMISSIBLE_WITH_QUERY_SCOPE_TIMESTAMP_AND_ACCESS_CEILING
```

A returned result can support a narrowly named `VISIBLE_PUBLIC_MENTION_CANDIDATE` after retaining the query, channel scope, timestamp, permalink, and wrapper access ceiling. It can be useful for prospect or problem-language discovery after human qualification.

## Excluded claims

```text
MATCH_COUNT_EQUALS_UNIQUE_PEOPLE = false
MATCH_COUNT_EQUALS_UNIQUE_BUYERS = false
MATCH_COUNT_EQUALS_PURCHASE_INTENT = false
MATCH_COUNT_EQUALS_MARKET_DEMAND = false
ZERO_RESULT_EQUALS_WORKSPACE_ABSENCE = false
PUBLIC_SEARCH_EQUALS_PRIVATE_OR_DM_VISIBILITY = false
RESULT_ORDER_EQUALS_REPRESENTATIVE_SAMPLE = false
REPEATED_MENTIONS_EQUAL_INDEPENDENT_DEMAND = false
BOT_OR_INTERNAL_MESSAGE_EQUALS_EXTERNAL_BUYER = false
```

Search matches are messages, not commercial entities or transactions. One author can produce many matches; several nearby matches can collapse to one; bots, internal discussion, quoted text, channel/user-name matches, and repeated copies can inflate or distort apparent demand. Search preferences and access scope can also suppress visible channels. Therefore result count cannot be labeled buyer count, lead count, willingness-to-pay, conversion, revenue, or authoritative market prevalence.

## Required revision

`X13_SLACK_SEARCH_PUBLIC_READONLY_010` phase 1 should classify output as **bounded mention-discovery only**:

- Persist exact query bytes, modifiers, date window, channel scope, sort, result cap, context setting, wrapper schema, observation timestamp, ordered result IDs/permalinks, continuation state, and error class.
- Deduplicate only under an explicit method; preserve raw returned cardinality separately.
- Label authorship class when known: human, bot/app, unknown.
- Require message-content review before `QUALIFIED_PROBLEM_MENTION`.
- Require an independent commercial artifact before any buyer claim: authenticated prospect response, signed contract/order, invoice tied to a counterparty, or reconciled payment evidence.
- Treat zero results as `NO_VISIBLE_MATCH_RETURNED`, never absence.

## Strongest objection

An exact phrase such as “we need to buy” from a named external participant can be commercially useful. Correct: it may be a high-value lead signal. The search hit alone still does not establish identity, authority, budget, uniqueness, purchase, or willingness to pay; those require source readback and qualification outside the search count.

## Falsifier

Revise this card if a controlled same-principal fixture shows the connector exposes a documented, complete, stable, identity-resolved commercial-object model rather than message matches. The fixture should include:

- one human author repeating the same phrase;
- several matching messages in close proximity;
- one bot/app message;
- one channel excluded by Slack search preferences;
- one private-channel and one DM match;
- one query whose user or channel name matches at lower priority;
- pagination beyond the first result cap;
- raw Slack search under the same effective principal and timestamp window.

Even if raw parity stands, buyer evidence remains falsified only by a separate authenticated commercial receipt tied to the purported buyer.

## License and terms uncertainty

Slack documentation is publicly readable but remains subject to Slack copyright and platform terms; this card paraphrases rather than redistributes it. The connector's OAuth identity, scopes, token custody, retention, workspace plan, administrator search controls, quota accounting, backend method, and whether UI search preferences affect wrapper output remain unknown. No terms acceptance, account action, or private-channel/DM access occurred.

## Cost and operator burden

- Research/card production estimate: `12–20 minutes`
- Controlled public-fixture and raw-parity verification estimate: `30–60 minutes`
- Paid cost surfaced: `$0`
- Operator minutes requested or consumed: `0`

## Disposition

`REVISE`: admit Slack public search only as bounded, human-reviewed mention discovery. Do not count results as buyers, leads, demand, sales, revenue, or absence. Fitness remains `0` until the exact X13 WorkItem consumes this card, a distinct verifier runs the controlled fixture, and an explicit ConsumerAck binds the result.

No task mutation, account creation, terms acceptance, outreach, application, purchase, send, spend, deployment, merge, public release, or private-data use occurred.
