---
schema_id: hfo.gen133.x13.cots_connector_event.v1
experiment_id: X13_GITHUB_CONTENTS_API_001
seat: X13_COTS_CONNECTOR_PDCA
addressed_to: S04_STRUCTURAL_PREFLIGHT
carrier_task_id_expected: 6a55c1733708819185088bf334e33ea5
carrier_task_id_observed: 6a55c1733708819185088bf334e33ea5
carrier_task_id_match: true
prior_current_version: 4
next_current_version: 5
prior_current_blob_sha: a8d22776fac07de20bfe7db7e97325d6d76c11e3
campaign_wake: 1_of_4
phase_attempted: 1_of_4
phase_1_completed: true
phase_2_completed: false
phase_3_completed: false
phase_4_decision: PENDING
candidate: GitHub_REST_Contents_API
candidate_contract_reference: official_REST_versions_2026-03-10_and_2022-11-28_connector_header_not_exposed
result: BASELINE_ESTABLISHED
binding_decision: false
measured_fact_changed: true
valid_time_utc: 2026-08-01T01:49:49Z
transaction_time_utc: SEE_GIT_COMMIT_METADATA
canonical_repository: TTaoGaming/hfo-gen-133
canonical_branch: agent/gen133-bootstrap-20260730
repository_head_observed_before_write: 72b2186811cc17aec9e2715d4c5a26f76611e179
wip: 1
effect_ceiling: READ_ONLY_BASELINE_PLUS_REQUIRED_GIT_EVENT_AND_POINTER_COMMITS
verifier: S04_STRUCTURAL_PREFLIGHT_THEN_DISTINCT_NONPRODUCER
consumer: Ratatoskr_and_Olrun
expiry_utc: 2026-08-08T01:49:49Z
sealed: false
---

# X13 GitHub Contents API campaign — phase 1 official contract and direct baseline

## Self-probe

- Native task inventory exposed X13 as `6a55c1733708819185088bf334e33ea5`; it matches the expected task ID.
- Available surfaces used: native Tasks readback, GitHub connector read/write contract discovery, GitHub file readback, official GitHub documentation through web research, and Git commit readback.
- No task, account, credential, terms, payment, deployment, merge, publication, secret, production system, or destructive state was mutated.

## Official contract baseline

GitHub's official repository-contents endpoint creates a new file or replaces an existing file. The request binds repository, path, commit message, Base64-encoded content, and optional branch. Updating an existing file requires the current blob `sha`. The documented response classes are `200` for update, `201` for create, `404` for not found, `409` for conflict, and `422` for validation failure or abuse controls.

Official documentation states that fine-grained GitHub App installation/user tokens and fine-grained personal access tokens can use the endpoint with repository `Contents: write`; workflow-path mutation additionally requires workflow write authority. GitHub also warns that content create/update and delete operations should be serialized because concurrent calls can conflict.

GitHub's REST API is date-versioned. Official documentation currently lists `2026-03-10` and `2022-11-28` as supported, with `2022-11-28` scheduled for support through 2028-03-10. The carrier connector wrapper references the `2022-11-28` endpoint contract, but it does not expose the actual request header or returned API-version headers. Therefore the effective version used by this connector is `UNKNOWN_FROM_DIRECT_RECEIPT`, not assumed.

Official rate-limit documentation states common authenticated user and GitHub App installation baselines of 5,000 requests per hour, with higher cases for Enterprise Cloud and additional secondary/content-generation limits. This carrier did not expose authentication class, rate-limit headers, remaining quota, reset time, or secondary-limit state, so no exact live quota is claimed.

Official sources consulted on 2026-08-01 UTC:

- `https://docs.github.com/en/rest/repos/contents`
- `https://docs.github.com/en/rest/about-the-rest-api/api-versions`
- `https://docs.github.com/en/rest/using-the-rest-api/rate-limits-for-the-rest-api`
- `https://docs.github.com/en/rest/using-the-rest-api/best-practices-for-using-the-rest-api`

## Direct capability baseline

A direct connector read of:

`state/coordination/experiments/cots_connector_x13/CURRENT.md`

on branch:

`agent/gen133-bootstrap-20260730`

returned:

- blob SHA: `a8d22776fac07de20bfe7db7e97325d6d76c11e3`;
- UTF-8 bytes reconstructed from returned content: `3049`;
- SHA-256 of those reconstructed UTF-8 bytes: `137bd6dbc9443bf335515b7ef6bf09b3780a823fbd7b6e34c524241e81865de7`;
- prior campaign version: `4`;
- access result: authenticated repository content read succeeded without operator relay.

The exposed connector actions directly provide UTF-8 create, fetch, blob fetch, update, and delete wrappers. The wrapper contract says create returns a commit SHA; update returns a commit SHA and resulting content blob SHA; fetch returns content and blob SHA. This phase does not infer unexposed HTTP headers, token identity, permission scope, billing tier, rate-limit budget, audit-log records, or request retry behavior.

The required immutable event creation and subsequent `CURRENT` replacement are themselves direct writes through the candidate surface, but they are control-plane bookkeeping rather than the dedicated reversible phase-2 specimen. They prove only that this connector can create and replace separate UTF-8 paths serially on the named branch when the supplied path and prior blob SHA are accepted.

## Measurements

### Custom code avoided

- Directly avoided in this carrier: manual REST authentication plumbing, URL construction, Base64 encoding, JSON request construction, and response decoding for the bounded file operations.
- Estimated bespoke adapter avoided for the current use: approximately `40–120` lines, depending on error handling and retry policy.
- Not avoided: event schema, idempotency design, cross-file transaction logic, conflict reconciliation, independent verification, or consumer acknowledgement.

### Operator minutes

- Operator relay: `0 minutes`.
- Operator action requested: none.
- Estimated operator minutes removed this wake: `3–6` minutes versus manually opening GitHub, locating the branch/path, editing, committing, and copying a receipt pointer.

### Credentials and permission

- Direct fact: authenticated read and write wrappers are available to the carrier for this repository/branch.
- Unknown: token type, token owner, explicit scopes, installation identity, expiry, SSO state, branch-rule bypass capability, and audit attribution.
- No credential material was displayed or copied.

### Durability

- Git object/commit durability is provided by GitHub for successful commits, and blob SHA readback is exposed.
- No database transaction, exactly-once execution, multi-path atomicity, linearizability, durable workflow timer, lease, or automatic recovery guarantee is established.
- The event and pointer update require separate commits and can diverge if the second write fails.

### Observability

- Exposed: commit SHA on writes; content and blob SHA on reads; connector error objects on failures; some connector calls expose wall-clock call duration.
- Not exposed in the content wrapper receipts: HTTP status, request ID, API-version header, rate-limit headers, ETag, token identity, audit event, retry count, or server timing.

### Portability

- High at the conceptual contract level because the endpoint is standard GitHub REST and has a public OpenAPI description.
- Medium at the carrier-wrapper level because action names, return shapes, hidden authentication, and omitted headers are connector-specific.
- Repository portability is limited to GitHub unless another forge implements a compatible adapter.

### Failure behavior

- Documentary baseline: update requires the current blob SHA; conflict can return `409`; validation or abuse controls can return `422`; missing resource can return `404`; concurrent content mutations should be serialized.
- Direct phase-3 failure behavior remains untested.
- Required writes are serial and rollback is a forward commit restoring the prior bytes; no history rewrite or deletion is allowed.

### Direct cost and quota evidence

- Paid call initiated by X13: none.
- Incremental monetary charge observed: `$0`.
- GitHub plan or connector cost allocation: unknown.
- Exact live request budget and remaining quota: unknown because headers and authentication class are not exposed.

## Strongest objection

The baseline may simply prove that a privileged connector wrapper can perform repository writes, not that HFO has a portable, inspectable, least-privilege GitHub integration. Hidden authentication and omitted HTTP/rate-limit/audit headers can conceal permission drift, quota exhaustion, attribution failures, and wrapper-specific semantics.

## Strongest falsifier

The campaign should not adopt this surface as a durable coordination primitive if a controlled phase-2/3 specimen shows any of the following: stale-SHA updates overwrite newer bytes instead of failing; exact readback differs from submitted UTF-8 bytes; a failed pointer update leaves no detectable orphan event; the wrapper mutates an unexpected branch/path; rollback cannot be performed by a forward commit; or connector variance makes the same packet nonportable without operator credential handling.

## Next phase

Phase 2 will create one harmless deterministic specimen under the X13 experiment directory, read back exact bytes and digests, perform one reversible replacement with the fetched blob SHA, read back again, and restore or preserve an append-only final specimen without deletion. Phase 3 will use a quarantined stale-SHA or duplicate-path probe to measure conflict and permission behavior without touching production paths.

## Honest flaw

The direct read hash is computed from the UTF-8 string returned by the connector, not from a raw HTTP response body or downloaded Git blob. The wrapper hides authentication, API-version, HTTP, ETag, rate-limit, request-ID, and audit metadata. The bookkeeping commits performed in this phase are useful capability evidence but are not a separately controlled micro-use and cannot establish conflict safety, exactly-once behavior, or cross-file atomicity. Same-provider structural review has binding weight zero.
