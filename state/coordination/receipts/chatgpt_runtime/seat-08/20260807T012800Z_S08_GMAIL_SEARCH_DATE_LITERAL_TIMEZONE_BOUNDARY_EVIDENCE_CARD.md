---
schema_id: hfo.gen133.s08.research_evidence_card.v1
seat: S08_RESEARCH_AND_CANDIDATE_SCOUT
carrier_task_id_expected: 6a526109ba348191b5f23ad3172ad568
carrier_task_id_observed: 6a526109ba348191b5f23ad3172ad568
carrier_task_id_match: true
carrier_task_enabled: true
wip: 1
valid_time_utc: 2026-08-07T01:28:00Z
canonical_repository: TTaoGaming/hfo-gen-133
canonical_branch: agent/gen133-bootstrap-20260730
lane: agent_runtime_cots_capabilities
queue_source_commit: 1046129a53cf3ee32901a46a7ae73ba528b0b9ea
queue_source_path: state/coordination/experiments/cots_connector_x13/CURRENT.md
queue_source_blob: e318df1859ff546b098c6013cc30e7cf495a3bad
queue_version: 148
queue_next_candidate: Gmail_readonly_search_or_list_surface
queue_next_phase: PHASE1_OFFICIAL_CONTRACT_AND_BOUNDED_DIRECT_BASELINE
candidate: Gmail.search_email_ids
candidate_version: NOT_EXPOSED
upstream_candidate: Google_Gmail_API_v1_users.messages.list
bounded_uncertainty: CAN_GMAIL_DATE_LITERALS_IN_Q_BE_USED_AS_EXACT_TIMEZONE_AWARE_BOUNDS_FOR_X13_PHASE1
decision: REVISE
headline: USE_EPOCH_SECONDS_FOR_EXACT_AFTER_BEFORE_BOUNDS_DATE_LITERALS_ARE_PST_MIDNIGHT
fitness_credit: 0
expiry_utc: 2026-08-14T01:28:00Z
---

# S08 evidence card — Gmail search date-literal timezone boundary

## Self-probe and changed question

- Native task inventory returned enabled S08 task `6a526109ba348191b5f23ad3172ad568`; expected and observed IDs match.
- Current X13 pointer is `CURRENT v148`, which closes Calendar search and newly queues `Gmail_readonly_search_or_list_surface` for phase 1.
- Prior S08 Gmail card `20260804T172800Z_S08_GMAIL_SEARCH_EMAILS_METADATA_OUTPUT_CEILING_EVIDENCE_CARD.md` already covered output-hydration risk. This card is intentionally different: it tests only the time-bound semantics of Gmail `q` date filters.
- Tools observed this wake: native task inventory, GitHub read/write/readback, Gmail connector schema discovery, public web research, Slack write capability. No Gmail mailbox query or private-data read occurred.

**Bounded uncertainty:** Can X13 use human-readable Gmail search date literals such as `after:2026/08/06 before:2026/08/07` as exact bounds for a Mountain-time or UTC phase-1 baseline?

## Primary/current sources observed 2026-08-07

1. Google, **Search and filter messages**, last updated `2026-06-03 UTC`: https://developers.google.com/workspace/gmail/api/guides/filtering
   - Google states that dates in Gmail API search queries are interpreted as midnight in PST.
   - Google recommends passing epoch seconds when accurate dates for other time zones are required.
   - Google also documents search differences between Gmail UI and API, including alias expansion and thread-wide search behavior.
2. Google, **Method: users.messages.list**, last updated `2026-04-15 UTC`: https://developers.google.com/workspace/gmail/api/reference/rest/v1/users.messages/list
   - `q` uses Gmail search-box syntax.
   - `maxResults` is a cap; `pageToken` supports pagination; `resultSizeEstimate` is an estimate.
   - `q` cannot be used with the `gmail.metadata` OAuth scope.
   - each returned message entry contains only `id` and `threadId`; details require `messages.get`.
3. Google, **Gmail API usage limits**, current page observed 2026-08-07: https://developers.google.com/workspace/gmail/api/reference/quota
   - nominal raw-provider cost is `5` quota units for `messages.list`; connector mapping and actual debit are not exposed.
4. Google Workspace API user-data/developer policy, current page observed 2026-08-07: https://developers.google.com/workspace/workspace-api-user-data-developer-policy
   - Gmail-reading scopes are restricted and subject to data-minimization/use constraints; effective connector scope and principal remain unknown.

## Connector contract observed this wake

`Gmail.search_email_ids` exposes only `query`, `label_ids`, `max_results`, and `next_page_token`. It exposes no timezone, `time_min`, `time_max`, returned-field selector, effective OAuth scope, upstream request, connector version, or quota receipt.

## Supported claims

- `DATE_LITERAL_BOUND_IS_PST_BASED`: Gmail API date literals inside `q` are not caller-timezone-aware exact bounds; Google documents PST-midnight interpretation.
- `EPOCH_SECONDS_ARE_THE_PROVIDER_DOCUMENTED_ESCAPE_HATCH`: when exact bounds for another timezone are required, use `after:<unix_seconds>` and `before:<unix_seconds>`.
- `X13_PHASE1_SHOULD_NOT_USE_DATE_LITERALS_FOR_EXACT_MOUNTAIN_OR_UTC_WINDOWS`: doing so silently changes the intended boundary. On 2026-08-06, Denver is MDT (UTC-6), while documented PST midnight is UTC-8; the nominal midnight boundary differs by two hours.
- `IDS_ONLY_IS_THE_LOWER_DATA_DISCOVERY_SURFACE`: the exposed `search_email_ids` surface is consistent with the provider `messages.list` result ceiling of message/thread identifiers, while message details require a separate read.
- `RESULT_COUNT_IS_NOT_COMPLETENESS`: `maxResults` is only a cap and `resultSizeEstimate` is explicitly an estimate; pagination must be treated separately.

## Excluded claims

- No claim that the connector maps 1:1 to raw `users.messages.list`; upstream implementation is hidden.
- No claim that connector ordering is deterministic or newest-first for every filtered query.
- No claim that epoch-second filtering creates a snapshot, authoritative absence, complete result set, stable pagination, or raw-provider parity.
- No claim that successful `q` search proves a particular OAuth scope. In fact, Google documents that `q` is unavailable under `gmail.metadata`.
- No claim about private mailbox contents, matching messages, senders, subjects, labels, snippets, bodies, attachments, or counts; no Gmail call was made.
- No claim that the provider's PST wording implies daylight-saving conversion behavior beyond the documented search contract.

## Decision

`REVISE` the queued X13 phase-1 baseline contract:

1. Prefer `Gmail.search_email_ids` over content-hydrating search when opaque IDs are sufficient.
2. For any exact bounded time window, encode `after:` and `before:` with Unix epoch seconds computed from the intended UTC or named-zone instants; do not use `YYYY/MM/DD` date literals as exact Mountain-time or UTC boundaries.
3. Record the exact epoch seconds and corresponding ISO-8601 instants in the experiment receipt so replay intent is auditable.
4. Keep `max_results` small; record `next_page_token` separately; never promote a capped first page or `resultSizeEstimate` to completeness.
5. Keep authorization claims separate from output minimization: a query-bearing search does not prove `gmail.metadata` scope.
6. Do not use the operator's mailbox merely to validate this query-construction rule; public provider documentation is sufficient for the gate.

Required classification: `GMAIL_Q_EXACT_TIME_BOUND_USE_EPOCH_SECONDS_DATE_LITERALS_ARE_PST_BASED`.

## License / terms / privacy uncertainty

- Google developer-document prose is generally licensed CC BY 4.0 and code samples Apache 2.0 under the cited developer pages.
- Gmail API use is additionally governed by Google API terms and Workspace user-data/developer policy. Gmail read scopes can be restricted and subject to verification/security requirements.
- The connector implementation license, version, OAuth client ownership, effective principal/scopes, token custody, retention, subprocessors, hidden retries, search translation, and actual quota debit are not exposed by the callable schema.
- Message IDs are still user-data identifiers; lower-data is not equivalent to public or non-sensitive.

## Cost and operator-minute estimate

- This research card: `$0` direct spend; `0` operator minutes removed; approximately `8–15` carrier minutes.
- X13 query-contract amendment: estimated `2–5` producer minutes.
- Distinct structural verification: estimated `5–10` verifier minutes.
- If X13 later performs an authorized raw-provider `messages.list` baseline, nominal provider cost is `5` Gmail quota units per call under current docs; connector debit remains unknown.

## Strongest objection

For a broad day-scale experiment, a two-hour boundary shift may not change the returned sample, so date literals are simpler and operationally adequate.

**Response:** that may be true for a deliberately coarse window, but X13 labels the next phase a bounded direct baseline. A silently timezone-shifted boundary makes replay and absence/coverage interpretation ambiguous. Epoch seconds cost almost nothing and remove that ambiguity.

## Falsifier

Revise or retire this verdict if any of the following becomes true for the exact connector version: (a) the connector exposes explicit timezone-aware `time_min`/`time_max` parameters independent of Gmail `q`; (b) a source-bound connector contract proves it converts date literals into the caller's intended timezone before issuing the provider request; or (c) Google changes the documented date-query semantics.

## Verifier

- Structural: S04 recomputes queue commit/path/blob, confirms the exposed `search_email_ids` parameter surface, and checks the cited Google documentation and epoch-bound rule. Same-provider binding weight remains zero.
- Capability: X13 may later verify an exact query against an authorized synthetic/non-private mailbox fixture or matched raw-provider trace. Do not use private operator mail solely for this gate.

## Consumer

`X13_GMAIL_READONLY_SEARCH_OR_LIST_SURFACE_PHASE1_OFFICIAL_CONTRACT_AND_BOUNDED_DIRECT_BASELINE`.

Fitness remains `0` until a named WorkItem consumes this exact card and records ConsumerAck.

## Honest flaw

This card does not execute Gmail search and therefore does not prove connector-side translation, ordering, pagination, authorization, or return shape. It establishes only the provider-documented timezone boundary and the safer query-construction rule for the newly queued baseline.
