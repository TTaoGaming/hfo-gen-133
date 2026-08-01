---
schema_id: hfo.gen133.s08.research_evidence_card.v1
card_id: S08_GITHUB_CONTENTS_STALE_SHA_CONTRACT_20260801T033200Z
result: ADMIT
callsign_or_seat: S08_RESEARCH_CANDIDATE_SCOUT
carrier_task_id_expected: 6a526109ba348191b5f23ad3172ad568
carrier_task_id_observed: 6a526109ba348191b5f23ad3172ad568
carrier_task_id_match: true
carrier_identity_claim: DISPOSABLE_SCHEDULED_CARRIER_NOT_LINEAGE
controller: operator_direct
wip: 1
valid_time_utc: 2026-08-01T03:32:00Z
transaction_time_utc: SEE_GITHUB_COMMIT_METADATA
canonical_repository: TTaoGaming/hfo-gen-133
canonical_branch: agent/gen133-bootstrap-20260730
research_lane: agent_runtime_cots_capabilities
bounded_uncertainty: GITHUB_CONTENTS_API_STALE_BLOB_SHA_REJECTION_CONTRACT
candidate: GitHub_REST_Contents_API
candidate_endpoint: PUT_/repos/{owner}/{repo}/contents/{path}
candidate_documented_api_version: 2026-03-10
candidate_effective_connector_api_version: UNKNOWN
source_x13_event_commit: 104defe984d51c1efdc66b0ba7f47b2a59afbb72
source_x13_event_blob: f9a483d8e91dd4de7dff520f4ac56b58fb679350
source_x13_current_commit: 5b0c2a5faed29b0b20493da2bc829480db1cb408
source_x13_current_blob: b876c1054069bb38319b5ac32d07ddfc4ea41074
privacy_class: PUBLIC_PRIMARY_SOURCES_AND_SANITIZED_REPOSITORY_POINTERS_ONLY
effect_ceiling: RESEARCH_CARD_AND_SANITIZED_SLACK_POINTER_ONLY
verifier: S04_STRUCTURAL_PREFLIGHT_THEN_DISTINCT_NONPRODUCER
consumer: X13_COTS_CONNECTOR_PDCA_PHASE3
expiry_utc: 2026-08-08T02:48:11Z
sealed: false
---

# S08 evidence card — GitHub Contents API stale-SHA guard

## Changed queue evidence

The prior S08 card completed the `grants_jobs_income_opportunities` lane. The explicit five-lane rotation therefore advances to `agent_runtime_cots_capabilities`.

The research question is materially changed by X13 phase 2:

- phase-2 event commit: `104defe984d51c1efdc66b0ba7f47b2a59afbb72`
- phase-2 event blob: `f9a483d8e91dd4de7dff520f4ac56b58fb679350`
- X13 `CURRENT` commit: `5b0c2a5faed29b0b20493da2bc829480db1cb408`
- X13 `CURRENT` blob: `b876c1054069bb38319b5ac32d07ddfc4ea41074`
- current campaign state: phase 2 complete; phase 3 stale-SHA rejection probe next

This card does not repeat X13's successful create/update/rollback evidence. It bounds what the official contract supports before X13 runs the failure probe.

## Bounded question

Does GitHub's current REST Contents API contract justify treating the supplied file blob `sha` as a testable stale-writer guard for one path, and what exact claims must remain excluded until X13 directly probes the connected wrapper?

## Decision

`ADMIT` one quarantined X13 phase-3 stale-SHA rejection probe.

The official endpoint contract requires the current file blob `sha` when updating an existing file and lists `409 Conflict` among update responses. That is enough to justify a controlled compare-before-replace experiment. It is not enough to claim linearizability, exactly-once execution, cross-file atomicity, or a stable connector error class.

The phase-3 acceptance criterion must be behavioral: the stale update is rejected **and a final readback proves the newer bytes remained unchanged**. Error text alone is insufficient.

## Self-probe

```yaml
expected_task_id: 6a526109ba348191b5f23ad3172ad568
observed_task_id: 6a526109ba348191b5f23ad3172ad568
task_id_match: true
tools_observed:
  github: authenticated_read_write_contents_wrapper
  slack: authenticated_read_write
  web_primary_sources: read
  shell: unavailable
  raw_http_status_headers: unavailable_through_connector
  native_task_mutation: not_called
```

## Dated primary sources

Observed `2026-08-01`:

1. GitHub Docs, REST API endpoints for repository contents, API version `2026-03-10`, section `Create or update file contents`: https://docs.github.com/en/rest/repos/contents?apiVersion=2026-03-10#create-or-update-file-contents
2. GitHub Docs, API Versions, current supported versions and default behavior: https://docs.github.com/en/rest/about-the-rest-api/api-versions?apiVersion=2026-03-10
3. GitHub Docs, REST API best practices, serialization guidance for mutative requests: https://docs.github.com/en/rest/using-the-rest-api/best-practices-for-using-the-rest-api?apiVersion=2026-03-10
4. Direct connector contract exposed in this carrier: `GitHub.update_file` requires the current blob `sha`, replaces one UTF-8 file, accepts an explicit branch, and returns commit plus content-blob identifiers. The wrapper does not expose raw HTTP status, headers, request ID, API-version header, token identity, rate-limit state, or retry count.

## Supported claims

- Updating an existing file through `PUT /repos/{owner}/{repo}/contents/{path}` requires the blob SHA of the file being replaced.
- The documented response set includes `200`, `201`, `404`, `409`, and `422`.
- GitHub warns that content update and delete operations can conflict when run concurrently and says to perform them serially.
- GitHub's current documented REST version is `2026-03-10`; `2022-11-28` remains supported, and a request without an explicit API-version header defaults to `2022-11-28`.
- The connected wrapper exposes an expected blob-SHA input and exact post-write commit/blob readback, so a harmless stale-SHA experiment is feasible without custom HTTP or Base64 code.
- X13 phase 2 already established only serial, reversible, single-path happy-path behavior on the named branch.

## Excluded claims

- The official page does not explicitly promise that every stale blob SHA maps uniquely to `409` rather than another failure class.
- A `409` alone cannot be attributed to stale SHA because the documented status is generic and can represent other conflicts.
- No claim of linearizability, compare-and-swap semantics across arbitrary branch changes, exactly-once execution, transaction isolation, multi-file atomicity, durable workflow recovery, or automatic compensation.
- No claim that the connector sends `X-GitHub-Api-Version: 2026-03-10`; its effective version remains unknown.
- No claim that hidden retries are absent. A wrapper retry could change observed failure behavior unless the final bytes and commit graph are read back.
- No claim of least-privilege credentials, known token scope, known audit identity, branch-protection behavior, quota headroom, or forge portability.
- No claim that one-path stale rejection prevents orphaned event and pointer commits in X12/X13's two-commit patterns.

## Phase-3 test contract admitted for X13

Use a new quarantined specimen and preserve the X13 WIP limit:

1. Create State A and read back exact bytes plus blob SHA `A`.
2. Validly update to State B using blob SHA `A`; read back exact bytes plus blob SHA `B`.
3. Attempt State C using now-stale blob SHA `A`.
4. Require the wrapper call to fail. Record every error field actually exposed; do not infer a hidden HTTP status.
5. Read back the specimen and require exact State-B bytes and blob SHA `B` unchanged.
6. Restore State A with a valid forward update using blob SHA `B`; read back exact baseline bytes.
7. Record all commit SHAs and verify that no State-C commit exists on the target branch.

`ADOPT_WITH_GATES` is not authorized by this research card. X13 phase 4 remains the only campaign decision point.

## License, terms, permissions, and quota uncertainty

- This is a hosted service API, not a FOSS library being admitted under a software license.
- Use remains governed by GitHub's applicable service terms and repository permissions; this wake accepted no terms and created no account.
- Fine-grained access normally requires repository `Contents: write`; workflow-file changes require additional workflow permission. The connected credential type and effective scopes are hidden.
- Exact plan limits, primary/secondary rate-limit state, abuse controls, and connector-specific quotas are not exposed. The admitted probe uses a tiny number of serialized calls and no paid call.

## Cost and operator-minute estimate

```yaml
direct_research_cost_usd: 0
new_credentials_required_now: 0
operator_minutes_required_now: 0
estimated_x13_phase3_machine_calls: 6_to_8
estimated_x13_phase3_elapsed_minutes: 3_to_8
estimated_operator_minutes_avoided: 5_to_10
custom_adapter_code_avoided_estimate: 40_to_120_lines
```

## Strongest objection

The evidence may be merely an optimistic-concurrency convention hidden behind a carrier-specific wrapper. Because the wrapper suppresses raw HTTP metadata and may have undisclosed retry behavior, a rejected call could be ambiguous, and a successful call could still target an unexpected branch. Only exact branch/path/byte/commit readback can make the micro-use meaningful.

## Strongest falsifier

`REVISE` or `RETIRE` the stale-SHA guard for workflow-state use if any of these occurs:

1. State C succeeds using stale blob SHA `A`;
2. State-B bytes or blob SHA change after the rejected attempt;
3. the wrapper reports success without a new commit/blob identifier;
4. the error cannot be distinguished from branch/path/authentication/transport failure and final readback is missing;
5. the connector targets a different branch or path than requested;
6. hidden retries or race behavior produce more than the intended commits.

## Verifier, consumer, expiry

- **Consumer:** X13 should bind this card's commit, path, and blob into phase 3 before running the quarantined probe.
- **Verifier:** S04 may perform same-provider structural preflight with binding weight zero; a distinct nonproducer must challenge any later adoption claim.
- **Expiry:** `2026-08-08T02:48:11Z`, aligned to the current X13 campaign expiry. Recheck official docs if the probe runs after expiry.

## Honest flaw

This card researched the official contract but did not execute the stale-SHA failure. GitHub documents a required update SHA and a generic conflict response; it does not provide, on the cited page, a unique stale-SHA error guarantee. The connected wrapper hides the effective API version, raw status, headers, token identity, retries, and rate limits. Therefore the card admits only a reversible behavioral probe, not an adoption decision or a persistence guarantee.
