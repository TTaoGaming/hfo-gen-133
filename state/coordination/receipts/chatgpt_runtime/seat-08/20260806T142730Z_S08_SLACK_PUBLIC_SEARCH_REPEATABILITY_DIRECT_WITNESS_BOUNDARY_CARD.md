---
schema_id: hfo.gen133.s08.evidence_card.v1
seat: S08_RESEARCH_AND_CANDIDATE_SCOUT
task_id_expected: 6a526109ba348191b5f23ad3172ad568
task_id_observed: 6a526109ba348191b5f23ad3172ad568
task_id_match: true
wip: 1
valid_time_utc: 2026-08-06T14:27:30Z
expiry_utc: 2026-08-13T14:27:30Z
decision: REVISE
lane: AGENT_RUNTIME_COTS_CAPABILITIES
bounded_uncertainty: CAN_ONE_IDENTICAL_SLACK_PUBLIC_SEARCH_REPEAT_PLUS_A_DIRECT_CHANNEL_READ_PROVE_CONNECTOR_REPEATABILITY_OR_BIND_THE_SEARCH_RESULTS_TO_EXISTING_MESSAGES
candidate: api_tool.Slack.slack_search_public schema observed 2026-08-06; X13_SLACK_SEARCH_PUBLIC_READONLY_010 phase 2
consumer: X13_SLACK_SEARCH_PUBLIC_READONLY_010_PHASE2_REPEATABILITY_AND_DIRECT_CHANNEL_WITNESS_GATE
verifier: DISTINCT_SAME_PRINCIPAL_RAW_SLACK_SEARCH_AND_CONVERSATIONS_HISTORY_EXACT_CHANNEL_TS_VERIFIER
fitness_credit: 0_PENDING_EXACT_WORKITEM_CONSUMPTION_DISTINCT_VERIFICATION_AND_CONSUMER_ACK
---

# REVISE — identical Slack search is a drift canary; direct read needs an exact message key

## Queue delta and self-probe

Canonical `state/coordination/experiments/cots_connector_x13/CURRENT.md` on `agent/gen133-bootstrap-20260730`, blob `1cb30ecc15aa0934f29b7bd26e98e8765d49df16`, advances `X13_SLACK_SEARCH_PUBLIC_READONLY_010` from phase 1 to `PHASE2_IDENTICAL_BOUNDED_QUERY_REPEATABILITY_AND_DIRECT_CHANNEL_WITNESS_PENDING`. This is a changed question from the prior S08 phase-1 buyer-evidence boundary card.

Observed usable surfaces: GitHub repository search/read/write, Slack public search/channel read/message post, and web retrieval of current primary Slack documentation. No private Slack search or mailbox/private-data surface was used.

## Primary-source finding

Slack documents timestamp sorting as an ordering option for search results, not as a snapshot, deterministic-result-set, completeness, or index-consistency guarantee. The legacy `search.messages` method accepts `sort=timestamp`, `sort_dir`, and pagination, while Slack now recommends `assistant.search.context` Real-time Search. The connector schema resembles the newer surface in several fields, but its actual backend method is not exposed.

Slack's pagination documentation says cursors are pointers to the next portion, may expire, and should not be persisted for hours or days. A repeated first-page call therefore observes the current search/index/access state at two different times; it does not replay a frozen snapshot.

Slack documents a direct message lookup pattern using `conversations.history` with the exact conversation ID and message timestamp (`oldest=<ts>`, `inclusive=true`, `limit=1`). That can witness existence of a specific accessible message. It cannot bind a truncated search snippet to a message when the wrapper did not expose a stable message timestamp, channel-message key, or permalink.

Sources retrieved 2026-08-06:

1. Slack Developer Docs, `search.messages`: https://docs.slack.dev/reference/methods/search.messages/
2. Slack Developer Docs, `assistant.search.context`: https://docs.slack.dev/reference/methods/assistant.search.context/
3. Slack Developer Docs, Pagination: https://docs.slack.dev/apis/web-api/pagination/
4. Slack Developer Docs, `conversations.history`: https://docs.slack.dev/reference/methods/conversations.history/
5. Slack Developer Docs, Retrieving messages: https://docs.slack.dev/messaging/retrieving-messages/
6. Slack changelog, Real-time Search API announcement, 2026-02-17: https://docs.slack.dev/changelog/2026/02/17/slack-mcp

## Supported claims

```text
IDENTICAL_NORMALIZED_DIGEST_ON_TWO_CALLS = SAME_WRAPPER_OUTPUT_OBSERVED_TWICE
DIFFERENT_NORMALIZED_DIGEST = OBSERVED_DRIFT
TIMESTAMP_SORT = ORDERING_REQUEST_FOR_RETURNED_MATCHES
DIRECT_READ_WITH_EXACT_CHANNEL_AND_TS = ACCESSIBLE_MESSAGE_EXISTENCE_WITNESS
CURSOR_PRESENT = MORE_RESULTS_MAY_BE_AVAILABLE_TO_THAT_PAGINATION_SESSION
```

The repeat is useful as a bounded **normalized-output drift canary**. A direct read can independently confirm a named message still exists and is visible under the acting principal, provided the search result exposes or can be losslessly resolved to its exact channel ID and Slack `ts`.

## Excluded claims

```text
DIGEST_MATCH_EQUALS_PROVIDER_PARITY = false
DIGEST_MATCH_EQUALS_DETERMINISTIC_SEARCH = false
DIGEST_MATCH_EQUALS_COMPLETE_RESULT_SET = false
DIGEST_MISMATCH_IDENTIFIES_CONNECTOR_DEFECT = false
TIMESTAMP_SORT_EQUALS_POINT_IN_TIME_SNAPSHOT = false
TRUNCATED_SNIPPET_EQUALS_UNIQUE_MESSAGE_KEY = false
DIRECT_CHANNEL_READ_EQUALS_SEARCH_INDEX_PARITY = false
OLD_CURSOR_EQUALS_DURABLE_REPLAY_TOKEN = false
```

Search/index refresh, edits, deletion, new messages, access changes, backend migration, ranking/tie behavior, result truncation, and wrapper normalization can all change the digest. Conversely, equal first-page digests do not establish raw-provider parity, completeness, stable pagination, or absence of omitted matches.

## Required revision

Phase 2 should be named `NORMALIZED_OUTPUT_DRIFT_CANARY_AND_EXACT_MESSAGE_EXISTENCE_WITNESS` and must:

- repeat the exact query bytes and all modifiers once, with a fresh first-page request;
- persist both observation timestamps, connector schema, ordered normalized outputs, digests, cursor presence, and error class;
- treat equal digests as `NO_DRIFT_OBSERVED_IN_TWO_SAMPLES`, not deterministic parity;
- treat unequal digests as `DRIFT_OBSERVED_CAUSE_UNKNOWN`, not connector failure;
- perform direct channel readback only for results carrying an exact channel ID plus Slack message `ts` or an equivalent permalink that resolves losslessly to both;
- mark phase-1 results without a stable key as `DIRECT_WITNESS_UNBINDABLE` rather than matching by truncated snippet;
- avoid persisting or reusing the opaque search cursor beyond the immediate bounded pagination session;
- require a distinct raw-provider witness under the same effective principal before any parity claim.

## Strongest objection

The query uses a rare self-referential token in one quiet public channel, so the top three may be practically stable. That makes the repeat useful as a cheap canary. It still does not create a documented snapshot or deterministic search contract, and the phase-1 record explicitly says stable message IDs/permalinks were not exposed.

## Falsifier

Move toward `ADMIT` only if a distinct verifier demonstrates all of the following under the same effective principal and bounded time window:

1. the wrapper exposes exact channel ID and Slack `ts` or losslessly resolvable permalinks for every result;
2. direct `conversations.history` reads return those exact messages;
3. a raw Slack search call with the same query, scope, sort, direction, limit, and access context returns the same ordered result keys;
4. message/index state is held fixed or changes are independently logged;
5. cursor behavior is exercised immediately and an expired-cursor case is classified without retry loops.

Even that would validate one controlled fixture, not global completeness or permanent determinism.

## License and terms uncertainty

Slack documentation is publicly readable but subject to Slack copyright and platform terms; this card paraphrases it. The connector's effective OAuth identity, scopes, token custody, workspace binding, backend method, index freshness, retention, quota debit, request identifiers, cursor lifetime, and whether user search preferences affect output remain unknown. No terms acceptance or private-channel/DM access occurred.

## Cost and operator burden

- Research and card production estimate: `12–20 minutes`
- Producer amendment estimate: `5–10 minutes`
- Controlled same-principal verification estimate: `25–50 minutes`
- Paid cost surfaced: `$0`
- Operator minutes requested or consumed: `0`

## Disposition

`REVISE`: admit the identical repeat only as a two-sample normalized-output drift canary. Admit direct readback only when bound by an exact channel ID and message `ts`; otherwise record `DIRECT_WITNESS_UNBINDABLE`. Fitness remains `0` until this exact WorkItem consumes the card, a distinct verifier runs, and ConsumerAck is recorded.

No task mutation, account creation, terms acceptance, outreach, application, purchase, spend, deployment, merge, public release, private-data use, or non-required external send occurred.
