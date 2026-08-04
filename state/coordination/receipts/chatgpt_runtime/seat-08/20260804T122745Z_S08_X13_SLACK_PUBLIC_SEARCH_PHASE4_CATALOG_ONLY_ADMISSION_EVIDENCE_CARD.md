---
schema_id: hfo.gen133.s08.research_evidence_card.v1
task_id: 6a526109ba348191b5f23ad3172ad568
task_id_match: true
wip: 1
lane: agent-runtime/COTS capabilities
question: Is Slack.slack_search_public admissible after X13 phase 3 as an operational automation capability, or only as a gated catalog-only read surface?
verdict: REVISE
verdict_detail: ADMIT_TO_CATALOG_ONLY_DO_NOT_ADOPT_FOR_OPERATIONAL_AUTOMATION
candidate: Slack.slack_search_public
candidate_version: NOT_EXPOSED
schema_observed_utc: 2026-08-04T12:27:45Z
queue_snapshot:
  experiment: X13_SLACK_PUBLIC_MESSAGE_SEARCH_READONLY_001
  current_version: 87
  current_path: state/coordination/experiments/cots_connector_x13/CURRENT.md
  current_blob_sha1: 8fdeb5611cbd6a99a5c71909c595d4d9059e5b92
  phase3_event_commit: 7c6b9e67e6396a5ce804381c86cda2e1af1a155d
  phase3_event_blob_sha1: 3bc419120a3ad24358d2ad10f143c4b1a2e4b950
license_status: NO_CONNECTOR_IMPLEMENTATION_LICENSE_OR_VERSION_EXPOSED
terms_status: SLACK_API_TERMS_APPLY_PROVIDER_SIDE_EXACT_CONNECTOR_AGREEMENT_AND_DISTRIBUTION_RIGHTS_UNKNOWN
paid_cost_usd_this_run: 0
operator_minutes_this_run: 0
future_micro_use_estimate: 1_TO_3_PRODUCER_MINUTES_ZERO_OPERATOR_MINUTES_IF_ALREADY_AUTHORIZED
verification_estimate: 20_TO_40_VERIFIER_MINUTES_PLUS_5_TO_10_OPERATOR_MINUTES_FOR_PRINCIPAL_SCOPE_CONFIRMATION
consumer: X13_SLACK_PUBLIC_MESSAGE_SEARCH_READONLY_001_PHASE4_DECISION
catalog_consumer: HFO_COTS_CAPABILITY_INVENTORY
verifier: S04_HRIST_STRUCTURAL_PREFLIGHT_PLUS_DISTINCT_RAW_SLACK_API_WITNESS
expiry_utc: 2026-08-11T12:27:45Z
fitness_credit: 0_PENDING_WORKITEM_CONSUMPTION
recorded_time_utc: 2026-08-04T12:27:45Z
---

# S08 evidence card — Slack public search operational-admission gate

## Bounded finding

`Slack.slack_search_public` is useful enough to retain in the COTS capability catalog, but the present evidence does **not** support operational automation. X13 v87 records one positive search, one zero-result search, and one synthetic invalid-cursor failure. The failure was normalized to generic `execution_failed: internal_error` with no typed provider error, raw HTTP status, request identity, quota telemetry, authenticated principal, effective scope, or proof of connector-to-provider method binding.

Slack's current `search.messages` contract requires a user token with `search:read`, supports a returned continuation cursor, is a legacy method, and documents `internal_error` as a likely transient condition that may have partially succeeded. Slack's pagination guidance says cursors should be reused only from prior responses and can expire; arbitrary or stale cursors may produce `invalid_cursor`. The method page is the source of truth even though Slack's general pagination page still lists `search.messages` under traditional paging. A connector-level generic internal error therefore cannot prove that Slack rejected the supplied cursor or that zero returned content means message absence.

## Supported claims

- The exposed connector can perform a bounded read against public-channel search and accepts a cursor argument.
- X13 observed a positive response, a terminal zero-result response, and a fail-closed generic error with zero returned content.
- The connector did not mutate Slack state during the three recorded probes.
- The surface may reduce small amounts of custom search-wrapper code for human-reviewed discovery.

## Excluded claims

- Exact binding to Slack `search.messages`, Real-time Search, or any other upstream method.
- Exact authenticated principal, token class, effective OAuth scopes, or least privilege.
- Complete or authoritative absence from Slack when the connector returns zero results or errors.
- Stable cursor continuation, invalid-cursor classification, rate-limit behavior, retry count, quota use, latency, or raw provider parity.
- Typed message objects, deterministic pagination, production reliability, consumer value, saved operator time, or zero marginal cost.
- Permission to search private channels, DMs, or retain matched content beyond a named need.

## Terms and rights uncertainty

No connector implementation repository, version, software license, or connector-specific agreement was exposed. Slack's API Terms limit API access, prohibit circumventing access controls and rate limits, require data minimization, and can require separate authorization or agreements for externally distributed apps. The newer Real-time Search/Data Access terms also restrict background scraping and persistent copies. No terms were accepted and no account or permission state was changed in this run.

## Required revision

1. Keep the capability `CATALOG_ONLY / HUMAN_REVIEWED_PUBLIC_DISCOVERY`.
2. Do not branch operational logic on match count, absence, cursor state, or connector error text.
3. Use only an immediately returned compatible cursor; no synthetic, guessed, persisted, or stale cursor reuse.
4. Do not automatically retry generic internal errors without changed evidence or a raw provider witness.
5. Persist no matched text, identifiers, exact queries, or cursor values without a named retention requirement.
6. Operational adoption requires a named WorkItem, authenticated-principal and effective-scope readback, privacy-safe canonical request/response digests, typed provider errors, raw request correlation, bounded retry policy, distinct verification, and explicit ConsumerAck.

## Strongest objection

For public discovery, a human-reviewed connector result may be pragmatically sufficient and cheaper than implementing a raw Slack client. Requiring raw-provider parity before any use could over-engineer a low-consequence lookup.

## Falsifier

Revise this gate toward `ADMIT` if the same authorized principal produces a privacy-safe, digest-bound comparison between the connector and the raw Slack endpoint for the identical bounded query and an immediately returned continuation cursor, covering at least success, empty, pagination, expired/invalid cursor, permission denial, and rate-limit cases; typed outcomes must agree, hidden retries must be bounded, and a named consumer must measure a useful outcome or operator time saved.

## Primary/current sources

- X13 CURRENT v87, exact Git blob `8fdeb5611cbd6a99a5c71909c595d4d9059e5b92`, observed 2026-08-04: https://github.com/TTaoGaming/hfo-gen-133/blob/agent/gen133-bootstrap-20260730/state/coordination/experiments/cots_connector_x13/CURRENT.md
- X13 phase-3 invalid-cursor event, commit `7c6b9e67e6396a5ce804381c86cda2e1af1a155d`, 2026-08-04: https://github.com/TTaoGaming/hfo-gen-133/commit/7c6b9e67e6396a5ce804381c86cda2e1af1a155d
- S04 same-provider structural `REVISE`, commit `12fa5f055a9fb0ee1091df7df3b335637638fb2f`, 2026-08-04: https://github.com/TTaoGaming/hfo-gen-133/commit/12fa5f055a9fb0ee1091df7df3b335637638fb2f
- Slack `search.messages` reference, accessed 2026-08-04: https://docs.slack.dev/reference/methods/search.messages/
- Slack Web API pagination, accessed 2026-08-04: https://docs.slack.dev/apis/web-api/pagination/
- Slack Node SDK `SearchMessagesArguments`, accessed 2026-08-04: https://docs.slack.dev/tools/node-slack-sdk/reference/web-api/interfaces/SearchMessagesArguments/
- Slack API Terms of Service, effective 2025-10-10, accessed 2026-08-04: https://slack.com/terms-of-service/api

## Honest flaw

This card did not perform another Slack candidate call, inspect a raw provider request, or expose private data. It cannot distinguish a transient Slack failure from connector failure, argument translation, method mismatch, or wrapper normalization. Its verdict is a bounded adoption gate, not an independent provider-quality verdict or ConsumerAck.
