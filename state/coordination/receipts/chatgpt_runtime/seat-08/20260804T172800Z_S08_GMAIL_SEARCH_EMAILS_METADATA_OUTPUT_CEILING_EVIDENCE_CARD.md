---
schema_id: hfo.gen133.s08.research_evidence_card.v1
seat: S08_RESEARCH_AND_CANDIDATE_SCOUT
carrier_task_id_expected: 6a526109ba348191b5f23ad3172ad568
carrier_task_id_observed: 6a526109ba348191b5f23ad3172ad568
carrier_task_id_match: true
carrier_task_enabled: true
wip: 1
valid_time_utc: 2026-08-04T17:28:00Z
transaction_time_utc: SEE_GITHUB_COMMIT_METADATA
canonical_repository: TTaoGaming/hfo-gen-133
canonical_branch: agent/gen133-bootstrap-20260730
lane: agent_runtime_cots_capabilities
question_changed_from: prior_grants_jobs_income_opportunity_lane_completed_then_rotation_advanced
queue_source_commit: c9da65bce3b99f61a9ecf4f80aa750022e61a8ce
queue_source_path: state/coordination/experiments/cots_connector_x13/CURRENT.md
queue_source_blob: 76c8034a3751f0e9f7d5c0f733545243d319fcd7
queue_version: 92
queue_next_candidate: Gmail_search_metadata_readonly_surface
candidate: Gmail.search_emails
candidate_version: NOT_EXPOSED
compared_safe_surface: Gmail.search_email_ids
decision: REVISE
headline: SEARCH_EMAILS_HAS_NO_EXPOSED_METADATA_FORMAT_OR_HEADER_CEILING
fitness_credit: 0
expiry_utc: 2026-08-11T17:28:00Z
immediate_expiry_on:
  - Gmail_connector_schema_or_return_contract_change
  - source_bound_trace_proving_format_metadata_and_no_body_or_snippet
  - Google_Gmail_API_contract_change
  - X13_candidate_or_phase_change
---

# S08 evidence card — Gmail `search_emails` metadata-output ceiling

## Self-probe and bounded question

- Native task inventory returned enabled task `6a526109ba348191b5f23ad3172ad568`; expected and observed IDs match.
- Tools observed: native automation inventory, GitHub read/write/readback, Gmail connector schema discovery, current official Google Gmail API documentation, web research, and Slack pointer capability.
- No Gmail query or mailbox read occurred. No message ID, sender, subject, header, snippet, body, attachment, token, identity, credential, or other private mailbox data was accessed or persisted.
- CURRENT v92 newly queues `Gmail_search_metadata_readonly_surface`, phase 1.

**Bounded uncertainty:** Can the exposed `Gmail.search_emails` connector be admitted as a metadata-only read surface without a private-data probe?

## Exact sources observed 2026-08-04

1. X13 CURRENT v92: commit `c9da65bce3b99f61a9ecf4f80aa750022e61a8ce`, path `state/coordination/experiments/cots_connector_x13/CURRENT.md`, blob `76c8034a3751f0e9f7d5c0f733545243d319fcd7`.
2. Current connector schemas discovered in this carrier:
   - `Gmail.search_email_ids`: returns matching Gmail message IDs.
   - `Gmail.search_emails`: searches for emails, but exposes only `query`, `label_ids`, `max_results`, and `next_page_token`; it exposes no `format`, `metadataHeaders`, output-field mask, body/snippet exclusion, upstream method, OAuth scope, or connector version.
3. Google Gmail API `users.messages.list`, last updated `2026-04-15 UTC`: https://developers.google.com/workspace/gmail/api/reference/rest/v1/users.messages/list
4. Google Gmail API `users.messages.get`, last updated `2026-04-15 UTC`: https://developers.google.com/workspace/gmail/api/reference/rest/v1/users.messages/get
5. Google Gmail API `Format`, last updated `2025-03-24 UTC`: https://developers.google.com/workspace/gmail/api/reference/rest/v1/Format
6. Google Gmail API message resource, last updated `2026-05-06 UTC`: https://developers.google.com/workspace/gmail/api/reference/rest/v1/users.messages
7. Google Gmail OAuth scopes, current page observed `2026-08-04`: https://developers.google.com/workspace/gmail/api/auth/scopes

## Supported claims

- `LIST_IS_IDS_ONLY`: official `users.messages.list` returns only `id` and `threadId` in each message entry; further details require `users.messages.get`.
- `GET_HAS_EXPLICIT_FORMATS`: official `users.messages.get` supports `minimal`, `metadata`, `full`, and `raw`; only `metadata` provides headers without body content, and `metadataHeaders[]` can narrow returned headers.
- `FULL_CAN_INCLUDE_BODY`: the official `full` format includes parsed body content in `payload`; the Message resource also defines `snippet` as a short part of message text.
- `CONNECTOR_CEILING_UNEXPOSED`: the current `Gmail.search_emails` schema provides no caller control or declared contract for `format=metadata`, selected headers, snippet suppression, body suppression, hydration count, or returned field set.
- `IDS_ONLY_SURFACE_EXISTS`: `Gmail.search_email_ids` is the exposed lower-data alternative when opaque IDs are sufficient.
- `QUERY_SCOPE_BOUNDARY`: Google's `users.messages.list` documentation says `q` cannot be used under the `gmail.metadata` OAuth scope. Successful query search therefore cannot by itself prove metadata-only authorization, even if returned model-visible fields are narrow.
- `NO_PRIVATE_PROBE_NEEDED_FOR_GATE`: schema absence plus the official multi-format contract is enough to reject an unqualified metadata-only claim; it is not enough to assert that the connector actually returns bodies.

## Excluded claims

- No claim that `Gmail.search_emails` currently returns message bodies, snippets, attachments, or all headers.
- No claim that it calls `users.messages.get`, uses `format=full`, or performs one upstream hydration per ID.
- No claim that the connector uses an overbroad OAuth grant; effective identity and scope remain unknown.
- No claim that headers, IDs, snippets, or subjects are harmless or non-sensitive.
- No claim about ordering, completeness, pagination stability, hidden retries, quota consumption, storage, retention, subprocessors, or raw-provider parity.
- No Gmail connector call was made because this carrier forbids private-data use.

## License, terms, and privacy uncertainty

- Google states that developer-document prose is CC BY 4.0 and code samples are Apache 2.0.
- The Gmail connector implementation license, build/version, service terms, data handling, retention, OAuth client ownership, granted scopes, token custody, subprocessors, and audit surface were not exposed by schema discovery.
- A metadata response can still contain sensitive sender, recipient, subject, date, and routing headers. `METADATA` is a body ceiling, not a public-data classification.

## Decision

`REVISE` the queued phase-1 candidate and admission language:

1. Do not call or classify `Gmail.search_emails` as metadata-only while its schema lacks an explicit returned-field ceiling.
2. Use `Gmail.search_email_ids` for bounded discovery when opaque IDs are sufficient.
3. When headers are genuinely required, require a source-bound contract or trace proving `messages.get(format=metadata)` or an equivalent body-free path, an explicit header allowlist, snippet exclusion, no attachment hydration, and a small result limit.
4. Keep authorization scope separate from output minimization: query-bearing search does not prove `gmail.metadata` scope.
5. Treat any future capability probe as private-data-bearing unless performed against an authorized synthetic/non-private fixture; do not use the operator's mailbox for this gate.
6. Keep operational, adoption, and fitness credit at zero until a named WorkItem consumes a verified exact contract.

Required classification: `GMAIL_SEARCH_EMAILS_OUTPUT_CEILING_UNKNOWN_USE_IDS_ONLY_OR_EXPLICIT_METADATA_CONTRACT`.

## Cost and operator-minute estimate

- This research card: `$0` direct spend; `0` operator minutes; approximately `8–14` carrier minutes.
- X13 terminology/schema-gate amendment: estimated `5–12` producer minutes.
- Distinct structural verification: estimated `10–20` verifier minutes.
- Optional source-bound non-private fixture trace, only if already authorized and available: estimated `15–35` producer/verifier minutes; `$0` expected, quota debit unknown.

## Strongest objection

The connector may already normalize `search_emails` to headers only and may never expose snippets or bodies, even though the callable schema omits those implementation details.

**Response:** that remains possible, so the result is `REVISE`, not `RETIRE`. Hidden safe behavior cannot support a metadata-only admission claim. A source-bound return contract or non-private trace can close the uncertainty cheaply.

## Falsifier

Revise or retire this verdict if a current source-bound connector contract or authorized non-private trace proves all of the following for the exact connector version: explicit metadata format, header allowlist, no snippet, no body/payload/raw fields, no attachment hydration, bounded upstream calls, and stable failure behavior. The verdict also expires if the connector schema or Google API contract changes.

## Verifier

- Structural: S04 verifies exact queue commit/path/blob, connector schema fields, official API contract, and that this card made no body-return claim. Same-provider binding weight remains zero.
- Capability: X13 or a distinct provider verifies the exact connector version using an authorized synthetic/non-private mailbox fixture or source-level trace; do not use private operator mail.

## Consumer

- Immediate: `X13_GMAIL_SEARCH_METADATA_READONLY_SURFACE_PHASE1` owner.
- Secondary: any S05 mail-triage WorkItem author choosing between IDs-only discovery and content hydration.
- Fitness remains `0` until an exact WorkItem records ConsumerAck against this card's commit/path/blob.

## Honest flaw

The callable schema does not expose the connector's returned object definition or hidden implementation. This card therefore proves only that a metadata-only ceiling is **not evidenced**, not that bodies are returned. It intentionally avoids a direct capability call because the carrier's effect ceiling prohibits private-data use.
