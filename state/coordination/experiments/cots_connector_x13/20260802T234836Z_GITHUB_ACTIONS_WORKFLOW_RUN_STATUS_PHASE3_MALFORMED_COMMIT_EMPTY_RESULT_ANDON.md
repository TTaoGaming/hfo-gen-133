---
schema_id: hfo.gen133.x13.cots_connector_event.v1
event_id: X13_GITHUB_ACTIONS_WORKFLOW_RUN_STATUS_READONLY_001_PHASE3_MALFORMED_COMMIT_EMPTY_RESULT
experiment_id: X13_GITHUB_ACTIONS_WORKFLOW_RUN_STATUS_READONLY_001
carrier_task_id: 6a55c1733708819185088bf334e33ea5
candidate: GitHub_Actions_bounded_workflow_run_status_readonly_surface
phase: 3_of_4
prior_current_version: 50
expected_current_version: 51
disposition: PHASE3_ACCEPTED_WITH_SEMANTIC_EMPTY_RESULT_ANDON
valid_time_utc: 2026-08-02T23:48:36Z
transaction_time_utc: SEE_GIT_COMMIT_METADATA
sealed: true
---

# X13 phase 3 — malformed commit input probe

## Bounded action

One read-only `fetch_commit_workflow_runs` call targeted `TTaoGaming/hive-fleet-obsidian-gen-132` with a synthetic, non-provider-derived, clearly non-hex commit identifier. No retry, workflow dispatch, rerun, cancellation, artifact/log/job hydration, secret read, branch change, merge, repository-setting change, or scheduled-task mutation occurred.

## Direct connector receipt

- connector action: `fetch_commit_workflow_runs`
- wrapper scope: pull-request-triggered runs, first page only
- input class: synthetic malformed commit identifier; exact value intentionally not promoted as a reusable identifier
- returned workflow runs: `0`
- connector error: `null`
- error classification/status/headers: not exposed because no error was surfaced
- connector external-call time: `331 ms`
- carrier retries: `0`
- write side effect: none
- surfaced paid cost: `$0`
- measured operator minutes removed: `0`

## Measured Andon

At this connector surface, a clearly malformed commit identifier produced the same normalized shape as an ordinary no-match query: an empty workflow-run array with no error. The surface therefore does **not** distinguish malformed client input from a valid source-bound commit that has no pull-request-triggered run on the first page.

This is content-safe and mutation-free, but semantically unsafe for CI verification. Treating this empty result as “CI did not run” or “commit has no workflow” would be false confidence.

GitHub's official workflow-runs contract defines `head_sha` as a string filter and documents `200 OK` for the list operation; it does not promise validation that the supplied string resolves to an existing commit. The connector also hides the raw request, any parameter rewrite, total count, rate-limit headers, request ID, and upstream retry behavior. Therefore this event attributes the observed conflation to the **connector surface**, not conclusively to GitHub's raw endpoint.

Official references checked:

- https://docs.github.com/en/rest/actions/workflow-runs?apiVersion=2026-03-10
- https://docs.github.com/en/rest/using-the-rest-api/troubleshooting-the-rest-api?apiVersion=2026-03-10

## Gates added

1. Accept commit identifiers only when source-bound to a trusted GitHub commit, pull-request, branch-head, or contents response for the same repository.
2. Reject synthetic, non-hex, truncated, copied-with-whitespace, or otherwise unbound identifiers before invoking the workflow-run connector.
3. Interpret every empty result as `NO_MATCH_IN_WRAPPER_SCOPE`, never as proof that CI did not run.
4. Keep malformed-input, valid-no-match, authentication, authorization/not-found masking, rate-limit, transient-provider, connector-transport, and workflow-failure states separate.
5. Require a positive run payload or an independent raw API/Actions UI check before using this surface as a release or completion gate.
6. Bind positive observations to repository, source-bound commit, run ID, observation time, wrapper event scope, and page scope.
7. Keep all workflow mutations and content hydration excluded.

## Measurements

- custom code avoided: `35–110 LOC` for authenticated lookup/normalization, unvalidated
- custom policy still required: source binding, input validation, empty-result semantics, latest-attempt selection, pagination, permission/rate-limit handling, independent verification
- credentials: connector reached GitHub; identity, credential type, Actions permission, scope, custody, and least privilege remain unknown
- durability: point-in-time query over mutable rerun state; not a durable event stream
- observability: low for negative/failure classification; normalized empty result and latency visible, raw request and provider headers hidden
- portability: medium-low; source-bound commit and pass/fail concepts are portable, wrapper filters and GitHub run semantics are provider-specific
- failure behavior: malformed input returned semantic no-match rather than a distinguishable client-input failure
- direct cost/quota evidence: `$0` surfaced; actual upstream request count, rate-limit bucket, quota consumption, and billing state unknown
- verifier: raw GitHub `GET /repos/{owner}/{repo}/actions/runs` with the same `event=pull_request` and `head_sha`, plus Actions UI or a source-bound valid-commit control
- consumer: HFO CI/release gates, branch-health summaries, and agent completion verification
- strongest falsifier: a same-context raw request or wrapper trace proves the malformed identifier was rejected, rewritten, or mapped from a provider error rather than returned as an ordinary zero-match result
- honest flaw: only one malformed identifier was tested; no valid nonexistent hexadecimal OID, shortened real OID, wrong-repository OID, whitespace variant, permission denial, `401`, `403`, `404`, `422`, `429`, `5xx`, raw/API comparison, or ConsumerAck was observed

## Phase result

`PHASE3_ACCEPTED_WITH_SEMANTIC_EMPTY_RESULT_ANDON`

Next wake is phase 4 decision-only. No additional GitHub capability call is required. Provisional disposition: `ADOPT_WITH_GATES` for exact, source-bound commit status checks; reject negative empty results as authoritative evidence.