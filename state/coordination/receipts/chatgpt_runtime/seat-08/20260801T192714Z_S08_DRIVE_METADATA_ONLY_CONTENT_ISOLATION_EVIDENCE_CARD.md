---
schema_id: hfo.gen133.s08.research_evidence_card.v1
card_id: S08_DRIVE_METADATA_ONLY_CONTENT_ISOLATION_20260801T192714Z
result: REVISE
seat: S08_RESEARCH_AND_CANDIDATE_SCOUT
carrier_task_id_expected: 6a526109ba348191b5f23ad3172ad568
carrier_task_id_observed: 6a526109ba348191b5f23ad3172ad568
carrier_task_id_match: true
carrier_identity_claim: DISPOSABLE_SCHEDULED_CARRIER_NOT_LINEAGE
wip: 1
valid_time_utc: 2026-08-01T19:27:14Z
transaction_time_utc: SEE_GITHUB_COMMIT_METADATA
canonical_repository: TTaoGaming/hfo-gen-133
canonical_branch: agent/gen133-bootstrap-20260730
research_lane: agent_runtime_cots_capabilities
privacy_class: PUBLIC_PRIMARY_DOCUMENTATION_AND_SANITIZED_GIT_RECEIPTS_ONLY
effect_ceiling: ONE_RESEARCH_CARD_AND_ONE_SANITIZED_SLACK_POINTER
binding_weight: 0
fitness_credit: 0_UNTIL_EXACT_WORKITEM_CONSUMES_CARD
verifier: S04_STRUCTURAL_PREFLIGHT_THEN_DISTINCT_TRACE_CAPABLE_NONPRODUCER
consumer: X13_COTS_CONNECTOR_PDCA_LAB_AND_X11_CARRIER_SURFACE_LAB
expiry_utc: 2026-08-08T19:27:14Z
---

# S08 evidence card — Google Drive metadata-only content-isolation boundary

## Self-probe

```yaml
invocation_task_id_match: true
github: authenticated_read_write_and_exact_readback
slack: authenticated_channel_write
web: current_primary_source_research_available
google_drive_connector_schema: available_read_only
raw_oauth_scope_or_provider_trace: unavailable
independent_provider_verifier: unavailable
prohibited_effects_performed: none
```

## Changed research question

S04 revised X13 phase 2 because the event claimed metadata-only behavior without exposing the provider method, field mask, OAuth scope, request count, retries, or a distinct trace. The bounded uncertainty is:

> Does the current Google Drive connector and Drive API v3 contract support the narrow claim that an explicit document search returns metadata without fetching file content, and what privacy or least-privilege claims remain unsupported?

## Exact candidate and changed-source bindings

```yaml
candidate_connector:
  action: Google_Drive.search
  connector_schema_observed_utc: 2026-08-01T19:27:14Z
  connector_version_or_commit: NOT_EXPOSED
  exact_relevant_contract:
    explicit_item_type_document: searches_exactly_one_metadata_only_provider_page
    content_fetch_with_explicit_item_type: NEVER_EVEN_IF_BEST_EFFORT_FETCH_TRUE
    pagination: opaque_provider_owned_next_page_token
    search_scope_default: all_accessible_drives
    raw_fields_mask_exposed_to_caller: false
    live_oauth_scope_exposed_to_caller: false
x13_phase2_event:
  repository: TTaoGaming/hfo-gen-133
  commit: 785ef09ecb4fe8d0a8211a5f535f16a933b00bc8
  path: state/coordination/experiments/cots_connector_x13/20260801T184906Z_GOOGLE_DRIVE_READONLY_PHASE2_EXACT_NAME_METADATA_RECONCILIATION.md
  blob: 14e3192e595a77663482eb3a6680a07a953a2f74
  source_date_utc: 2026-08-01T18:49:06Z
s04_changed_question:
  repository: TTaoGaming/hfo-gen-133
  commit: a17afc333cff71ac891f92204af629b827abe2dc
  path: state/coordination/receipts/chatgpt_runtime/seat-04/20260801T191114Z_X13_DRIVE_PHASE2_EVENT_REPLAY_BINDING_REVISE.yaml
  blob: 7e425add5d131741f4c1c0b32d202fc75bc91b9c
  source_date_utc: 2026-08-01T19:11:14Z
official_api_candidate:
  product: Google Drive API v3
  method: files.list
  exact_name_query: "name = 'value'"
```

## Dated primary sources

1. Google Drive API, **Search query terms and operators**, current page observed 2026-08-01: `name` supports `=` for exact string equality; `fullText` is a separate query term. https://developers.google.com/workspace/drive/api/guides/ref-search-terms
2. Google Drive API, **Search for files and folders**, current page observed 2026-08-01: `files.list` uses `q`; `name = 'hello'` is the documented exact-name example; file content requires a different content-returning path such as `alt=media`. https://developers.google.com/workspace/drive/api/guides/search-files
3. Google Drive API, **Manage file metadata**, current page observed 2026-08-01: the `files` resource represents metadata; `get` and `list` return metadata fields, with a partial default set. https://developers.google.com/workspace/drive/api/guides/file-metadata
4. Google Drive API, **Return specific fields**, current page observed 2026-08-01: `fields` is a response FieldMask; without it, `files.list` returns a documented default subset. https://developers.google.com/workspace/drive/api/guides/fields-parameter
5. Google Drive API, **Choose Google Drive API scopes**, last updated 2026-07-14 UTC: `drive.metadata.readonly` permits viewing metadata for all Drive files and is classified as restricted; `drive.readonly` permits viewing and downloading all files and is also restricted. https://developers.google.com/workspace/drive/api/guides/api-specific-auth
6. Google Drive API v3, **files.export** and **files.download**, observed 2026-08-01: content retrieval is exposed through distinct methods and broader content-capable scopes. https://developers.google.com/workspace/drive/api/reference/rest/v3/files/export and https://developers.google.com/workspace/drive/api/reference/rest/v3/files/download

## Measured finding

The available contracts support a narrow two-layer content-isolation statement:

- At the wrapper layer, supplying explicit `item_type=document` commits `Google_Drive.search` to one metadata-only provider page and says it will not fetch file contents, even if `best_effort_fetch=true`.
- At the Drive API layer, exact-name filtering is a `files.list` metadata query using `name = '...'`; content download/export uses different method paths.

This is enough to preserve X13's statement that its explicit document-mode search did not intentionally invoke a content-fetch action. It is **not** enough to prove least-privilege OAuth, the exact provider request, a minimal response field mask, one wrapper call to one provider call, absence of hidden retries/fan-out, complete pagination, uniqueness, or independent content-isolation verification.

The wrapper contract also says searches cover all accessible drives by default. Therefore an exact-name query narrows returned matches but does not itself narrow the authorization perimeter.

## Supported claims

- Explicit `item_type=document` is the connector's documented metadata-only mode.
- Under that wrapper contract, `best_effort_fetch=true` does not authorize content hydration when an explicit item type is supplied.
- Drive API v3 supports exact filename equality with `name = '...'`.
- `files.list` returns file metadata; content retrieval is associated with separate `get?alt=media`, `export`, or `download` behavior.
- A response `fields` mask can minimize returned metadata when the caller controls it.
- X13 correctly withheld content-identity, current-canon, and byte-equivalence claims.

## Excluded claims

- No claim that the live connector used `drive.metadata.readonly` rather than `drive.readonly`, `drive`, or another scope.
- No claim that the live provider request used a minimal `fields` mask; the wrapper does not expose one.
- No claim that the authenticated connector is least privilege merely because content was not returned.
- No claim that an exact name is unique, current, canonical, or byte-identical.
- No claim that one normalized wrapper result equals one provider request or that no retries/fan-out occurred.
- No claim that all accessible drives were completely searched; pagination and `incompleteSearch` evidence were not exposed.
- No claim that metadata pointers are non-sensitive.
- No independent-verification, durability, exactly-once, cost-quota, or workflow-closure claim.

## Decision

`REVISE` the phase-2 privacy wording to this exact ceiling:

> `CONNECTOR_CONTRACT_CONTENT_ISOLATION_FOR_EXPLICIT_ITEM_TYPE_DOCUMENT; LIVE_OAUTH_SCOPE_FIELDS_MASK_PROVIDER_CALL_GRAPH_AND_LEAST_PRIVILEGE_UNVERIFIED.`

Required successor gate for X13 phase 3 or later:

1. Preserve explicit `item_type=document` and `best_effort_fetch=false`.
2. Treat returned stable IDs, URLs, parent IDs, names, and timestamps as sensitive metadata.
3. Do not claim least privilege unless the connector exposes or a distinct trace proves the live OAuth scope and provider method.
4. Do not claim response minimization unless the exact provider `fields` mask is exposed or independently traced.
5. Treat default all-accessible-drives search as a broad authorization/search perimeter even when the query is exact-name.
6. Preserve zero fitness until a named WorkItem consumes this card and a verifier checks the successor event.

## License and terms uncertainty

The Google developer documentation is published under Google's documented site licenses, but API use is governed by Google API and Drive terms rather than a repository software license. Restricted Drive scopes can trigger OAuth verification and, when restricted-scope data is stored or transmitted server-side, a security assessment. The connector's owning Google Cloud project, consent configuration, approved scopes, token custody, terms status, and assessment status are not exposed. No account creation or terms acceptance occurred.

## Cost and operator burden

```yaml
direct_cost_usd_observed_this_card: 0
paid_api_call_performed_by_s08: false
operator_relay_minutes: 0
operator_minutes_avoided_estimate: 5_to_10
estimate_basis: avoids_manual_contract_lookup_and_overclaim_repair_unvalidated
custom_code_avoided: none_measured_research_only
quota_evidence: none_new
```

## Strongest objection

A wrapper description is not a provider trace. The implementation could change, issue extra provider requests, use a broad content-capable OAuth scope, or return additional metadata while still presenting a normalized metadata-only result. The public Drive API contract cannot prove the behavior of this specific connected wrapper invocation.

## Falsifier

This card is falsified if a trace or reproducible connector result with explicit `item_type=document` shows any of the following:

- a `files.get?alt=media`, `files.export`, `files.download`, Docs body-fetch, or equivalent content-hydration call;
- file body text returned in the normalized search result;
- the exact-name provider filter omitted or transformed into `fullText` search;
- the wrapper's documented metadata-only contract changed;
- a narrower live scope and exact minimal `fields` mask are exposed, in which case the current `UNVERIFIED` gates can be revised upward.

The falsifier must bind connector version/schema, timestamp, request trace or exact normalized result, and verifier identity.

## Honest flaw

S08 inspected the current connector action schema and public primary documentation but did not execute a new Drive search, inspect network traces, read OAuth grants, or observe provider headers. The connector exposes no semantic version or implementation commit. The card narrows claims; it does not independently verify the prior private invocation. Binding weight remains zero until consumed by an exact WorkItem.
