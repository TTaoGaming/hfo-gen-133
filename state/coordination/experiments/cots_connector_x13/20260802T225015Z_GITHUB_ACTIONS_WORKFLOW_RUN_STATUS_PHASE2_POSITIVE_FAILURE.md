---
schema_id: hfo.gen133.x13.cots_connector_event.v1
experiment_id: X13_GITHUB_ACTIONS_WORKFLOW_RUN_STATUS_READONLY_001
event_type: PHASE2_POSITIVE_MICRO_USE
phase: 2_of_4
prior_current_version: 49
expected_current_version: 50
carrier_task_id: 6a55c1733708819185088bf334e33ea5
carrier_task_id_match: true
candidate: GitHub_Actions_bounded_workflow_run_status_readonly_surface
wip: 1
valid_time_utc: 2026-08-02T22:50:15Z
transaction_time_utc: SEE_GIT_COMMIT_METADATA
sealed: true
---

# X13 GitHub Actions workflow-run status — phase 2 positive micro-use

## Source-bound candidate

A source-bound existing pull request was selected without creating or mutating workflow activity:

- Repository: `TTaoGaming/hive-fleet-obsidian-gen-132`
- Pull request: `#20`, `test(gen132/roundtrip): held-out branch->push->PR->CI-gate probe`
- Pull-request state at observation: open, non-draft, unmerged
- Head branch: `agent/olrun-git-exemplar-selftest`
- Head commit: `abcf741c0d6cd654f3fdcc02d331245861406931`
- PR body claim: the artifact was created as a held-out branch → push → PR → CI-gate-trigger probe and should not be merged as a real change

The PR metadata provides a source binding for the exact head commit. It does not independently prove the run result or that the workflow behavior was correct.

## Direct positive connector receipt

One bounded read-only `fetch_commit_workflow_runs` call against that repository and exact head commit returned one normalized workflow-run record:

- Run ID: `30493905584`
- Workflow name: `HFO Conformance Gate`
- Workflow ID: `321534087`
- Run number: `1551`
- Status: `completed`
- Conclusion: `failure`
- Jobs URL present: yes, not dereferenced
- Logs URL present: yes, not dereferenced
- Connector error: none
- Connector external-call time: `516 ms`
- Carrier retries: `0`
- Workflow, repository, pull-request, branch, job, artifact, log, or secret mutation: none
- Surfaced direct cost: `$0`
- Measured operator minutes removed: `0`

This is a positive payload even though the workflow conclusion is failure. A successful API/connector call must never be conflated with a successful workflow. The connector successfully reported a completed failing run.

## Discovery cost and boundedness

Locating one source-bound positive candidate required `13` read-only GitHub connector calls in this phase, including `4` commit-workflow-run queries. Three candidate commits returned empty arrays under the wrapper's pull-request-only first-page scope; the fourth returned the positive record above. No candidate was manufactured, dispatched, rerun, cancelled, merged, or modified.

The discovery overhead means the current connector surface is useful when a repository and commit are already known, but inefficient as a general run-discovery mechanism.

## Official contract reconciliation

GitHub's official workflow-runs contract supports filtering by `head_sha`, `event`, and status or conclusion values. It documents `completed` as a status and `failure` as a possible conclusion/status filter value. The connector wrapper is narrower: it forces the `pull_request` event and returns only the first page.

The positive receipt admits the connector's normalized fields `id`, `name`, `status`, `conclusion`, `run_number`, and `workflow_id` for this observed record only. It does not establish ordering, completeness, attempt identity, branch identity, event visibility, timestamps, actor, check suite, raw HTTP fidelity, or whether additional runs were omitted.

## Phase-2 gates

- Treat connector-call success and workflow-run success as separate states.
- Interpret `status=completed` plus `conclusion=failure` as a finished failing workflow, not transport failure and not a passing CI gate.
- Bind every status observation to the exact repository, commit SHA, observation time, and returned run ID.
- Do not infer the latest attempt, only attempt, full workflow history, branch-wide health, or repository-wide health from the first returned page.
- Do not infer that the pull request's prose claim is validated merely because a run exists; the observed conclusion is failure and the reason was not inspected.
- Keep jobs, steps, logs, artifacts, rerun, cancellation, dispatch, secrets, workflow files, branches, merges, and repository settings outside admitted scope.
- Do not infer account identity, token type, permissions, repository visibility, quota budget, billing state, or write authority from successful read access.
- Prefer an exact known repository and commit supplied by a durable source; do not use broad PR search as the normal monitoring path.

## Measurements

| Dimension | Phase-2 result |
|---|---|
| Custom code avoided | Estimated 35–110 LOC for authenticated commit lookup, normalized run identity/status/conclusion extraction, and transport-vs-workflow-state separation; still unvalidated in a production consumer |
| Operator minutes removed | 0 measured; estimated 1–3 minutes per already-known commit status check remains unvalidated |
| Credentials | Read access worked for the observed public-facing sources; authenticated identity, credential type, exact Actions permission, scope, custody, and least privilege remain unknown |
| Durability | Point-in-time observation over mutable run and rerun state; not an event stream and not a durable latest-status guarantee |
| Observability | Medium-low: run ID, workflow ID/name, run number, status, conclusion, URL presence, and 516 ms connector time visible; raw HTTP, event, head SHA echo, branch, actor, timestamps, attempt, pagination, request ID, rate-limit headers, and upstream retries hidden |
| Portability | Medium-low: commit SHA and pass/fail concepts are portable, but GitHub run IDs, workflow IDs, event filters, conclusion vocabulary, and wrapper semantics are provider-specific |
| Failure behavior | A workflow-level failure was represented as data while the connector call succeeded; connector/client/permission/rate-limit failures remain untested |
| Direct cost/quota evidence | $0 surfaced; 13 read-only connector calls measured in this phase; actual upstream request count, primary/secondary rate-limit consumption, retries, and billing counters remain unknown |
| Fitness credit | 0 pending source-bound ConsumerAck and measured operator outcome |

## Verifier, consumer, falsifier

- **Verifier:** raw source-bound GitHub workflow-runs endpoint or Actions UI for repository `TTaoGaming/hive-fleet-obsidian-gen-132`, commit `abcf741c0d6cd654f3fdcc02d331245861406931`, and run `30493905584`, with explicit event and pagination policy.
- **Consumer:** HFO CI release gates, branch-health summaries, and agent completion verification that need a bounded commit-specific result.
- **Strongest falsifier:** the raw endpoint or Actions UI shows a different run identity/status/conclusion for the same observation, or shows newer/additional relevant attempts that the connector's forced event filter or first-page normalization omitted.

## Honest flaw

The positive record was not independently read back through the raw API or Actions UI, and its jobs/logs were deliberately not hydrated. The connector did not expose event, branch, actor, timestamps, attempt number, head SHA echo, pagination, or rate-limit evidence. The workflow's `failure` conclusion was observed, but the cause and whether the held-out probe expected that failure remain unknown. General monitoring usefulness is still unproven because discovery required 13 read-only calls to find one positive candidate.

## Phase-2 disposition

`PHASE2_ACCEPTED_WITH_POSITIVE_FAILURE_STATUS_AND_SCOPE_GATES`

## Next wake

Phase 3 should perform one privacy-safe, read-only malformed-commit input probe against the same public repository, with no retry or mutation, to determine whether the connector fails closed with a distinguishable client-input error or silently normalizes invalid input to an empty result. Permission denial, rate limiting, and transient-server failure should remain unclaimed unless directly observed.