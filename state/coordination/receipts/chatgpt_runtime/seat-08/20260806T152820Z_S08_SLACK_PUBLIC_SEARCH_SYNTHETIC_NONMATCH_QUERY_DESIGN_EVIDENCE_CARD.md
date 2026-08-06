---
schema_id: hfo.gen133.s08.evidence_card.v1
seat: S08_RESEARCH_AND_CANDIDATE_SCOUT
carrier_task_id_expected: 6a526109ba348191b5f23ad3172ad568
carrier_task_id_observed: 6a526109ba348191b5f23ad3172ad568
carrier_task_id_match: true
wip: 1
valid_time_utc: 2026-08-06T15:28:20Z
transaction_time_utc: SEE_GITHUB_COMMIT_METADATA
canonical_repository: TTaoGaming/hfo-gen-133
canonical_branch: agent/gen133-bootstrap-20260730
lane: agent_runtime_cots_capabilities
decision: ADMIT
decision_scope: EMPTY_SUCCESS_SHAPE_PROBE_ONLY
fitness_credit: 0
sealed: false
---

# S08 evidence card — Slack public-search synthetic nonmatch query design

## Self-probe

- Expected and observed task ID: `6a526109ba348191b5f23ad3172ad568`; exact match.
- Tools observed: GitHub authenticated read/write and exact readback; Slack connector schema read and one authorized pointer send after Git readback; public web research.
- Not used: private Slack search, message/content inspection, account mutation, task mutation, outreach, application, purchase, spend, deployment, merge, publication, or private-data access.

## Changed bounded question

`state/coordination/experiments/cots_connector_x13/CURRENT.md` v138 advances `X13_SLACK_SEARCH_PUBLIC_READONLY_010` to phase 3: one bounded synthetic nonmatching public search, recording empty-success versus error shape.

**Bounded uncertainty:** Can phase 3 use a generated high-entropy token to test the connector's empty-success envelope without accidentally invoking Slack modifiers, semantic-question routing, or multi-term matching—and what may a zero result support?

## Exact candidate

- Surface: `api_tool.Slack.slack_search_public`, connector schema observed `2026-08-06`.
- Consumer: `X13_SLACK_SEARCH_PUBLIC_READONLY_010_PHASE3_SYNTHETIC_NONMATCH_EMPTY_OR_ERROR_SHAPE_GATE`.
- Queue binding: `state/coordination/experiments/cots_connector_x13/CURRENT.md` blob `454824058e43a51ba083fc27d381337fe911d98a`.
- Probe form admitted: generate immediately before the call a single token `zzq` + 32 lowercase hexadecimal characters; no spaces, colon, quotes, dash, wildcard, formatting, or question mark; do not publish the raw token to Slack before the call.
- Call ceiling: one public-search call, `content_types=messages`, `limit=1`, `include_context=false`, no cursor follow, no retry, no query broadening.

## Dated primary/current sources

Checked `2026-08-06`:

1. Slack `search.messages` reference: query is required; success and error envelopes are distinct; results can be affected by user search filters; nearby matching messages can collapse into one result; the method is legacy. <https://docs.slack.dev/reference/methods/search.messages/>
2. Slack Help search syntax: quotes trigger exact-phrase search; `-`, `in:`, `from:`, `has:`, date modifiers, and `*` alter query behavior; wildcard prefixes require at least three characters. <https://slack.com/help/articles/202528808-Search-in-Slack-Search-in-Slack->
3. Slack Real-time Search API guide: natural-language questions may trigger semantic search; keyword search supports stemming; formatting can interfere with retrieval; result relevance and backend behavior differ from strict literal lookup. <https://docs.slack.dev/apis/web-api/real-time-search-api/>
4. Connector schema observed this wake: `slack_search_public` is public-channel-only, reports semantic search unavailable for this user, describes keyword exact matching with space-separated conjunction, supports modifiers, and exposes neither backend method nor principal/scope metadata.

## Supported claims

- A one-token lowercase-hex query avoids every documented modifier delimiter and does not have natural-language question form.
- Generating the token immediately before the call and withholding it from Slack until after the call materially reduces self-contamination risk.
- A successful response with zero returned items supports only: `THE_CONNECTOR_ACCEPTED_THIS_QUERY_AND_RETURNED_NO_VISIBLE_PUBLIC_MESSAGE_MATCH_IN_THIS_OBSERVATION`.
- A structured connector error supports only the observed error class and call parameters.
- The probe is useful for distinguishing empty-success from error handling in the wrapper contract.

## Excluded claims

- Zero results do not prove workspace-wide absence, public-channel completeness, parser literalness, fresh indexing, permission completeness, stable future behavior, raw-provider parity, buyer absence, or market absence.
- A generated token is probabilistically unlikely to match; it is not a mathematical proof of nonexistence because Slack may tokenize, stem, normalize, index an unfurl, or already contain the token.
- The connector schema does not reveal whether the backend is legacy `search.messages`, Real-time Search, Slack MCP, or another wrapper path.
- No rate-limit debit, request ID, effective user, workspace binding, scope set, index timestamp, or total-count contract is exposed.

## License and terms uncertainty

Slack documentation and hosted search behavior remain subject to Slack copyright, platform terms, workspace plan, administrator controls, retention settings, and search preferences. Connector OAuth identity, scopes, token custody, backend method, data retention, and quota accounting are unknown. This card authorizes no terms acceptance or account action.

## Cost and operator-minute estimate

- Research pass: `$0` external spend; `0` operator minutes.
- Producer amendment: `5–10 minutes` to generate the token at call time, bind exact call parameters, and classify empty-success versus error without retry.
- Distinct verification: `20–40 minutes` using a same-principal raw-provider or controlled public-channel fixture.
- Expected paid cost: `$0`; direct quota debit remains unobserved.

## Strongest objection

A truly nonexistent token cannot be proven without controlling the entire indexed corpus, and Slack keyword search may normalize or stem input. Therefore the probe cannot validate absence or exact parser semantics.

That objection is accepted. The admitted purpose is narrower: exercise the wrapper's empty-success/error branch with low collision risk, not prove that the token is absent from Slack.

## Falsifier

Revise or retire this probe design if any of the following occurs:

1. the generated token returns a match;
2. the connector transforms the one-token query into semantic or multi-term form;
3. repeated identical calls under a controlled unchanged fixture alternate between empty-success and error without an observable cause;
4. a same-principal raw Slack call shows a material mismatch in success/error classification; or
5. Slack or connector documentation establishes a different literal-query or error-envelope contract.

A controlled verifier should include one known-match token and one generated nonmatch token in a public test channel, then bind raw and connector responses, exact principal, query bytes, timestamps, and result keys. Creating that fixture is outside this card.

## Verifier

`DISTINCT_SAME_PRINCIPAL_RAW_SLACK_PUBLIC_SEARCH_QUERY_GRAMMAR_AND_EMPTY_ENVELOPE_VERIFIER`

## Consumer

`X13_SLACK_SEARCH_PUBLIC_READONLY_010_PHASE3_SYNTHETIC_NONMATCH_EMPTY_OR_ERROR_SHAPE_GATE`

Consumption rule: record `EMPTY_SUCCESS_OBSERVED`, `NONEMPTY_UNEXPECTED`, or the exact connector error class. Do not translate empty success into absence, completeness, demand, or buyer claims. Fitness remains zero until the exact WorkItem consumes this card and emits ConsumerAck.

## Expiry

- Evidence expiry: `2026-08-13T15:28:20Z`.
- Immediate invalidation on connector schema change, backend disclosure, Slack search-contract change, consumer change, or probe execution outside the one-call public-only ceiling.

## Disposition

**ADMIT — EMPTY-SUCCESS SHAPE PROBE ONLY.**

The generated single-token probe is adequate to exercise one wrapper branch with low contamination risk. It is not evidence of authoritative absence or search completeness.