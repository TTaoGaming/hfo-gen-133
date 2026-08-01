---
schema_id: hfo.gen133.s08.research_evidence_card.v1
card_id: S08_GMAIL_QUERY_METADATA_SCOPE_20260801T092921Z
result: REVISE
callsign_or_seat: S08_RESEARCH_CANDIDATE_SCOUT
carrier_task_id_expected: 6a526109ba348191b5f23ad3172ad568
carrier_task_id_observed: 6a526109ba348191b5f23ad3172ad568
carrier_task_id_match: true
carrier_identity_claim: DISPOSABLE_SCHEDULED_CARRIER_NOT_LINEAGE
controller: operator_direct
wip: 1
valid_time_utc: 2026-08-01T09:29:21Z
transaction_time_utc: SEE_GITHUB_COMMIT_METADATA
canonical_repository: TTaoGaming/hfo-gen-133
canonical_branch: agent/gen133-bootstrap-20260730
research_lane: agent_runtime_cots_capabilities
candidate: Gmail_read_only_search_and_message_metadata_connector
candidate_contract_version: Gmail_API_docs_updated_2026-04-15_and_2026-06-03_observed_2026-08-01_plus_connector_schema_observed_2026-08-01
privacy_class: PUBLIC_PRIMARY_SOURCES_AND_CONNECTOR_SCHEMA_ONLY_NO_MAILBOX_READ
effect_ceiling: RESEARCH_CARD_AND_ONE_SANITIZED_SLACK_POINTER_ONLY
expiry_utc: 2026-08-08T09:29:21Z
verifier: X13_COTS_CONNECTOR_LAB_then_distinct_nonproducer_for_any_higher_effect_use
consumer: X13_COTS_CONNECTOR_LAB_GMAIL_PHASE1
fitness_credit: ZERO_UNTIL_EXACT_CONSUMER_ACK
sealed: false
---

# S08 evidence card — Gmail query search cannot be called a `gmail.metadata` least-privilege baseline

## Changed queue evidence

The prior S08 card completed the `grants_jobs_income_opportunities` lane at commit `c30d72812a847ed3bcea71bba579f3361e229fd6`, path `projects/income-lane/research/20260801T082953Z_S08_NSF_26_510_PROJECT_PITCH_EVIDENCE_CARD.md`, blob `c938ea2e5a52fdc51ab8e5229e5e726c1d65f3e2`. The explicit rotation therefore advances to `agent_runtime_cots_capabilities`.

X13's current pointer at commit `42f1b0c2e76501829ab5935c1f97479d6ec4c25f`, path `state/coordination/experiments/cots_connector_x13/CURRENT.md`, blob `44499b24b47e5e8315418f2119cce5727d866102`, nominates `Gmail_read_only_search_and_message_metadata_connector` for a new phase-1 campaign. No Gmail probe had occurred at that pointer.

## Bounded uncertainty

Can X13 treat query-based Gmail search that returns message IDs or metadata as a least-privilege `gmail.metadata` capability, without reading private mailbox content or claiming broader authorization?

## Decision

`REVISE` the phase-1 baseline.

Google's current Gmail API contract says `users.messages.list` returns only message `id` and `threadId` in its list response, but its `q` search parameter **cannot be used with the `gmail.metadata` OAuth scope**. Query-based search therefore requires `gmail.readonly`, `gmail.modify`, or the full-mail scope at the API authorization layer, even when the caller elects to stop at IDs and never fetch a body.

The exposed connector schema contains separate `search_email_ids`, `search_emails`, `read_email`, thread-read, attachment-read, draft, send, and mutation actions. Tool separation can reduce the bytes returned to the carrier, but it does not prove the live token scope, app identity, backend Gmail method, retention boundary, or least-privilege authorization. No mailbox query or private email read was executed in this research wake.

## Required phase-1 split

X13 should test and document two different contracts rather than one ambiguous "read-only metadata search" contract:

1. **Metadata-scope-compatible baseline:** label-ID filtering, pagination, and explicit metadata retrieval only; do not use `q`. Mark live scope `UNKNOWN` unless directly exposed.
2. **Query-search baseline:** use `q` only under an explicitly recognized broader restricted scope; stop at IDs for the smallest output, and do not call body-reading tools. Output minimization is not authorization minimization.

Additional gates:

- Record `AUTH_SCOPE_UNKNOWN` when token type, app identity, and scopes are hidden.
- Do not infer that a tool named `search_email_ids` uses `gmail.metadata`.
- Treat message IDs, thread IDs, labels, headers, sender, subject, dates, and query terms as private mailbox data even when bodies are absent.
- Use epoch seconds rather than date strings when timezone precision matters; Gmail API date strings are interpreted at midnight PST.
- Do not assume Gmail UI parity: the API does not perform alias expansion and does not support thread-wide search in the same way as the UI.
- Bind maximum results and pagination; a small first page is not proof of total-result count or complete coverage.
- Keep send, draft, label mutation, archive, Trash, attachment, and full-message reads outside this campaign's effect ceiling.

## Self-probe

```yaml
expected_task_id: 6a526109ba348191b5f23ad3172ad568
observed_task_id: 6a526109ba348191b5f23ad3172ad568
task_id_match: true
tools_observed:
  native_task_inventory: exact_ID_and_enabled_state_readback
  github_connector: authenticated_read_write_and_exact_file_readback
  slack_public_channel: authenticated_write_available
  web_primary_sources: read
  gmail_connector_schema: search_ID_search_full_read_thread_attachment_and_write_actions_exposed
  gmail_private_mailbox: not_accessed
  live_gmail_token_identity_and_scopes: not_exposed
  shell_or_browser_runtime: unavailable
  task_mutation: not_called
```

## Exact candidate and dated primary sources

Observed `2026-08-01`:

1. Google Gmail API `users.messages.list`, last updated `2026-04-15`: https://developers.google.com/workspace/gmail/api/reference/rest/v1/users.messages/list
2. Google Gmail API `users.messages.get`, last updated `2026-04-15`: https://developers.google.com/workspace/gmail/api/reference/rest/v1/users.messages/get
3. Google Gmail API `Format` contract, last updated `2025-03-24`: https://developers.google.com/workspace/gmail/api/reference/rest/v1/Format
4. Google Gmail API search/filter guide, last updated `2026-06-03`: https://developers.google.com/workspace/gmail/api/guides/filtering
5. Google Gmail API scopes, last updated `2026-06-03`: https://developers.google.com/workspace/gmail/api/auth/scopes
6. Sanitized connector-schema observation: exposed actions include `search_email_ids`, `search_emails`, `read_email`, batch/thread reads, attachment reads, draft/send, labels, archive, and Trash; live OAuth details are hidden.

## Supported claims

- `messages.list` returns message IDs and thread IDs; additional details require `messages.get`.
- `messages.list.q` supports most Gmail search syntax but cannot be used with `gmail.metadata`.
- `messages.get` supports `format=METADATA` and selected `metadataHeaders`; `minimal` excludes headers/body/payload, while `metadata` includes headers and labels.
- `gmail.metadata` and `gmail.readonly` are both classified by Google as restricted scopes; metadata excludes bodies but is not a non-sensitive scope.
- Public applications using restricted scopes can face OAuth verification and, when restricted-scope data is stored or transmitted on servers, a security assessment requirement.
- Gmail API query dates expressed as calendar dates are interpreted at midnight PST; epoch seconds are the precision-safe alternative.
- Gmail API search differs from the UI: no alias expansion and no equivalent thread-wide search.
- The current connector interface can minimize carrier output by using ID-only search, but its hidden backend authorization prevents a least-privilege scope claim.

## Excluded claims

- No claim about the actual Gmail OAuth scope, token class, user identity, app identity, backend method, retention, encryption, audit trail, rate limits, retry behavior, or data residency of the live connector.
- No claim that the connector directly maps each tool to one Gmail REST method.
- No claim that ID-only output is anonymous, non-sensitive, or safe to externalize.
- No claim that search results are complete, deterministic over mailbox mutation, thread-complete, or identical to Gmail UI results.
- No private email, label count, message ID, thread ID, subject, sender, recipient, snippet, header, body, attachment, or draft was read.
- No OAuth consent, account creation, terms acceptance, send, draft, label change, archive, Trash, or other mailbox mutation occurred.

## License, terms, and privacy uncertainty

Google's documentation classifies both `gmail.metadata` and `gmail.readonly` as restricted scopes. A custom public application may need OAuth verification, and storing or transmitting restricted-scope data on servers can trigger security-assessment obligations. This card does not determine the agreements, retention, subprocessors, enterprise controls, or verification status governing the current hosted connector. Those require provider-specific contract evidence rather than inference from tool names.

## Cost and operator-minute estimate

```yaml
direct_research_cost_usd: 0
operator_minutes_required_now: 0
credentials_or_consent_actions_this_wake: 0
estimated_x13_phase1_revision_minutes: 10_to_20
estimated_operator_minutes_avoided_by_preventing_false_metadata_scope_claim: 15_to_30_UNVALIDATED
estimated_custom_adapter_code_avoided_if_native_ID_search_is_admitted: 20_to_60_LOC_UNVALIDATED
paid_cost_or_quota_evidence: NOT_EXPOSED
```

## Strongest objection

The hosted connector may use a proprietary server-side authorization and data-minimization layer rather than mapping directly to the public Gmail API and its OAuth scopes. If so, the official API contract may not describe the carrier-facing security boundary. That objection does not restore a least-privilege claim: without a direct connector authorization receipt, the actual scope and backend access remain unknown.

## Falsifier

Revise or retire this card's connector-mapping conclusion if authenticated, sanitized provider evidence proves all of the following:

1. the exact backend method or equivalent contract used for query search;
2. the exact live token/app scope and identity;
3. a separately enforced server-side boundary that prevents body, attachment, draft, send, and mutation access for this connector campaign;
4. query-search behavior, date semantics, alias behavior, pagination, and thread semantics that materially differ from the documented Gmail API contract.

The official claim that `messages.list.q` is unavailable under `gmail.metadata` is falsified only by a newer controlling Google contract, not by an opaque successful connector call.

## Reversible next experiment

X13 may perform one harmless phase-1 contract baseline without reading mailbox contents:

- inspect exposed connector action schemas and authorization metadata only;
- declare whether the campaign is `METADATA_SCOPE_COMPATIBLE_NO_Q`, `QUERY_SEARCH_BROADER_SCOPE`, or `AUTH_SCOPE_UNKNOWN`;
- define one future bounded query using `search_email_ids`, `max_results=1`, no body read, no attachment read, no write, and no externalization of returned IDs;
- stop before executing that query unless the campaign effect ceiling explicitly permits one private-data read;
- record the strongest expected failure class and a privacy-safe readback rule.

## Verifier, consumer, expiry, and credit

- **Verifier:** X13 should consume this as official-contract evidence; S04 may structurally verify the resulting phase packet. A distinct nonproducer is required before any higher-effect adoption claim.
- **Consumer:** X13 COTS and Connector PDCA Lab, Gmail campaign phase 1.
- **Expiry:** `2026-08-08T09:29:21Z`; revalidate Google docs and connector schemas after expiry.
- **Credit:** zero until X13 records exact `CONSUMED`, `REJECTED_WITH_EVIDENCE`, or a bound campaign event against this card's Git blob.

## Honest flaw

This wake deliberately avoided the private Gmail mailbox. It inspected public Google documentation and connector schemas only. It therefore could not observe the live connector's OAuth scopes, backend API calls, response fields, latency, quotas, permission failures, retention, or data handling. The operator-minute and code-avoidance estimates are unvalidated ranges. The evidence prevents one false least-privilege claim but does not prove the connector safe or unsafe for actual mailbox use.
