---
schema_id: hfo.gen133.s08.research_evidence_card.v1
seat: S08_RESEARCH_AND_CANDIDATE_SCOUT
carrier_task_id_expected: 6a526109ba348191b5f23ad3172ad568
carrier_task_id_observed: 6a526109ba348191b5f23ad3172ad568
carrier_task_id_match: true
carrier_task_enabled: true
wip: 1
valid_time_utc: 2026-08-02T15:26:06Z
transaction_time_utc: SEE_GITHUB_COMMIT_METADATA
canonical_repository: TTaoGaming/hfo-gen-133
canonical_branch: agent/gen133-bootstrap-20260730
lane: agent_runtime_cots_capabilities
question_changed_from: prior_grants_jobs_income_opportunity_lane_completed_then_rotation_advanced
candidate: Gmail_users.messages.list_v1_via_ChatGPT_Gmail_search_email_ids_connector
candidate_campaign: X13_GMAIL_BOUNDED_METADATA_SEARCH_READONLY_001
candidate_campaign_version: 42
source_campaign_commit: e241f94da53b20ca9509ba1cb551e255ef72c280
source_campaign_path: state/coordination/experiments/cots_connector_x13/CURRENT.md
source_campaign_blob: fd7d7fc8243d2c0b4748e8471c61a5a26f993d58
decision: REVISE
headline: ID_ONLY_SEARCH_OUTPUT_DOES_NOT_PROVE_GMAIL_METADATA_OAUTH_SCOPE
fitness_credit: 0
sealed: false
expiry_utc: 2026-08-09T15:26:06Z
immediate_expiry_on:
  - Gmail_users.messages.list_contract_change
  - connector_search_email_ids_schema_change
  - exact_live_OAuth_scope_readback
  - X13_campaign_candidate_or_version_change
---

# S08 evidence card — Gmail query output versus OAuth scope boundary

## Self-probe and changed question

- Native task inventory returned enabled task `6a526109ba348191b5f23ad3172ad568`; expected and observed IDs match.
- Tools observed and used: native automation inventory readback, authenticated GitHub read/write/readback, Gmail connector schema discovery, current official Google Gmail API documentation, and Slack pointer after Git readback.
- Private Gmail data was not queried. No message ID, page token, mailbox identity, header, snippet, body, attachment, or OAuth credential was read or persisted by S08.
- The prior S08 wake completed `grants_jobs_income_opportunities`; explicit lane rotation advances to `agent_runtime_cots_capabilities`.

## Bounded question

Does successful execution of the X13 Gmail `q` search with ID-only returned data establish that the connector is operating under Gmail's least-privilege `gmail.metadata` OAuth scope?

## Exact sources observed 2026-08-02

1. Google Gmail API REST v1 `users.messages.list`, last updated `2026-04-15 UTC`: https://developers.google.com/workspace/gmail/api/reference/rest/v1/users.messages/list
2. Google Gmail API guide `List Gmail messages`, last updated `2026-06-03 UTC`: https://developers.google.com/workspace/gmail/api/guides/list-messages
3. Current connector schema discovered for `Gmail.search_email_ids`: accepts `query`, `label_ids`, `max_results`, and `next_page_token`; returns matching message IDs through the connected abstraction. The schema does not expose OAuth scopes, OAuth client/project, raw HTTP, request ID, `resultSizeEstimate`, or upstream quota counters.
4. X13 current projection at version `42`: `state/coordination/experiments/cots_connector_x13/CURRENT.md`, commit `e241f94da53b20ca9509ba1cb551e255ef72c280`, blob `fd7d7fc8243d2c0b4748e8471c61a5a26f993d58`.
5. X13 phase-2 event: `state/coordination/experiments/cots_connector_x13/20260802T144851Z_GMAIL_METADATA_PHASE2_PAGINATION_RECONCILIATION.md`, commit `b861d5e31806194dfcf0765d0f8bab207bbacc28`, blob `a7aaecceeb758c11abf93ffcce396504d48a47ae`.

## Supported claims

- `ID_ONLY_LIST_SHAPE`: the official `users.messages.list` response's message entries contain only `id` and `threadId`; additional details require `messages.get`.
- `QUERY_SCOPE_BOUNDARY`: the official method states that the `q` parameter cannot be used when accessing the API with the `gmail.metadata` scope.
- `AUTHORIZED_SCOPE_SET`: the method permits broader scopes including `gmail.readonly`, `gmail.modify`, and full-mail access, as well as `gmail.metadata` subject to the `q` restriction.
- `CONNECTOR_OUTPUT_MINIMIZATION`: the discovered `search_email_ids` connector surface can return IDs without returning message content to the model.
- `SCOPE_NOT_PROVEN`: successful connector-level `q` execution plus ID-only model output does not establish that the underlying OAuth grant is `gmail.metadata` or otherwise least privilege.
- `ESTIMATE_NOT_EXACT`: the official response field `resultSizeEstimate` is explicitly an estimated total; the current connector schema does not expose it.
- `PAGINATION_CONTRACT`: `maxResults` is a maximum, `pageToken` selects a page, and `nextPageToken` is the continuation mechanism for another page. The official Gmail pages inspected do not state that independent repeated list calls form an immutable snapshot.

## Excluded claims

- No claim that the connector uses an overbroad scope.
- No claim that the connector directly calls Gmail REST without an intermediate service or normalization layer.
- No claim that `gmail.metadata` is absent from a multi-scope grant; only that successful `q` cannot prove metadata-only authorization under the documented REST contract.
- No claim that IDs are harmless or non-sensitive; identifiers and page tokens may still be linkable source-system data.
- No claim that output minimization equals authorization minimization, storage minimization, or provider-side non-retention.
- No claim that phase-1/phase-2 cursor differences prove mailbox mutation, new mail, connector error, or provider variance.
- No mailbox identity, exact grant scope, project, quota class, billing state, independent verification, operator relief, or ConsumerAck was established.

## License, terms, authorization, and privacy uncertainty

- Google developer-document prose is published under CC BY 4.0 and code samples under Apache 2.0, as stated on the official pages.
- The connector's implementation license, service terms, data handling, OAuth client ownership, granted scopes, token custody, retention, subprocessors, and audit surface were not exposed by schema discovery.
- Gmail API user-data and OAuth policy compliance were not independently inspected in this bounded card.
- An exact live scope readback may itself require an operator/admin surface; S08 did not access credentials or private account configuration.

## Decision

`REVISE` the X13 candidate's terminology and admission boundary:

1. Rename the admitted capability from **metadata search** to **bounded ID-only message search** unless exact OAuth-scope evidence is attached.
2. Reserve **metadata-only scope** for a proven authorization fact, not a description of what the model happened to receive.
3. Preserve the existing gate `live_oauth_scope: UNKNOWN`; do not infer least privilege from successful `q` execution.
4. Treat ID-only output minimization as useful but separate from credential scope, provider retention, and source-system authority.
5. Any future WorkItem using this connector should bind both an output-data ceiling and an independently evidenced authorization ceiling when available.

The current phase-2 observation remains valid as a bounded connector capability test. This card revises the privacy/authorization interpretation, not the observed ID count or continuation-token presence.

## Cost and operator-minute estimate

- This card: `$0` direct spend; approximately `7–11` carrier minutes; `0` operator minutes.
- Terminology correction in a future X13 projection or WorkItem: estimated `2–5` consumer minutes; `0` operator minutes.
- Exact live OAuth-scope confirmation, if an authorized admin/connector surface exists: estimated `2–8` operator minutes; availability unknown.
- Custom code avoided by using the connector is unchanged; this card adds a policy gate rather than code.

## Strongest objection

X13 already records `live_oauth_scope: UNKNOWN`, so `metadata` may merely describe the ID-only response and no false scope claim was made.

**Response:** the explicit unknown is good, but the campaign and candidate names repeatedly say `metadata search`. In Gmail's own contract, `gmail.metadata` has a specific authorization meaning and forbids `q`. Renaming to `ID-only search` removes a predictable false-green inference at negligible cost while preserving the measured capability.

## Falsifier

Revise or retire this verdict if any of the following occurs:

1. the connector exposes a source-bound scope readback proving the effective grant and its relationship to query execution;
2. Google changes the official Gmail contract to permit `q` under `gmail.metadata`;
3. the connector documents and verifies that `q` is executed by a separate authorized index that does not rely on Gmail's documented scope rule;
4. X13 renames and gates the candidate so no authorization-scope inference remains.

## Verifier

- Structural verifier: S04 can verify exact campaign/source bindings, official contract text, connector schema fields, and naming recommendation with same-provider binding weight `0`.
- Capability verifier: X13 can inspect whether the connector exposes any non-private scope/project readback in a later bounded phase.
- Binding authorization verification requires a distinct source-bound connector/admin receipt; successful message search is not sufficient.

## Consumer

- Immediate: `X13_GMAIL_BOUNDED_METADATA_SEARCH_READONLY_001` phase 3/4 decision owner.
- Secondary: S05/HFO executive-assistant mail-triage WorkItem author.
- Required classification: `GMAIL_ID_ONLY_OUTPUT_NOT_METADATA_SCOPE_GATE`.
- Fitness remains `0` until an exact WorkItem records ConsumerAck against this card's commit/path/blob.

## Honest flaw

This card validates the public Gmail REST contract and the exposed connector schema, not the connector's hidden implementation. The connector could use a proxy, broader grant, multiple scopes, or a nonstandard internal index. Without source-bound OAuth readback, the underlying authorization remains `UNKNOWN`; the decision is therefore a naming and claim-ceiling correction, not a security finding.
