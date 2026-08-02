---
schema_id: hfo.gen133.x13.cots_connector_event.v1
experiment_id: X13_GITHUB_ACTIONS_WORKFLOW_RUN_STATUS_READONLY_001
event_type: PHASE1_BASELINE
phase: 1_of_4
prior_current_version: 48
expected_current_version: 49
carrier_task_id: 6a55c1733708819185088bf334e33ea5
carrier_task_id_match: true
candidate: GitHub_Actions_bounded_workflow_run_status_readonly_surface
wip: 1
valid_time_utc: 2026-08-02T21:48:51Z
transaction_time_utc: SEE_GIT_COMMIT_METADATA
sealed: true
---

# X13 GitHub Actions workflow-run status — phase 1 baseline

## Official contract baseline

Fresh official GitHub documentation was checked for the repository workflow-runs endpoint and REST rate limits:

- https://docs.github.com/en/rest/actions/workflow-runs?apiVersion=2026-03-10
- https://docs.github.com/en/rest/using-the-rest-api/rate-limits-for-the-rest-api
- https://docs.github.com/en/rest/using-the-rest-api/best-practices-for-using-the-rest-api

The raw repository workflow-runs endpoint supports filters including `branch`, `event`, `status`, `created`, and `head_sha`; `per_page` is at most 100 and filtered searches return at most 1,000 results. Anyone with repository read access can use it; private repositories require suitable authentication, and fine-grained credentials require repository `Actions: read` permission.

GitHub documents general authenticated REST limits commonly at 5,000 requests per hour, GitHub App installation limits beginning at 5,000 per hour and scaling in some contexts, and `GITHUB_TOKEN` at 1,000 requests per hour per repository outside Enterprise Cloud. Most REST `GET` requests consume one secondary-rate-limit point, but the live connector identity, credential type, primary limit, remaining budget, request headers, and any endpoint-specific cost are hidden.

## Direct connector receipt

One bounded read-only call used connector action `fetch_commit_workflow_runs` against canonical repository `TTaoGaming/hfo-gen-133` and commit `5ddb21762d27a4349c0707cc163b58352d36481d`, the commit recorded for CURRENT v48.

- Connector error: none
- Workflow runs returned: 0
- Connector external-call time: 386 ms
- Carrier retries: 0
- Workflow dispatch, rerun, cancellation, artifact download, log download, job read, secret read, branch mutation, and workflow mutation: none
- Surfaced direct cost: $0
- Measured operator minutes removed: 0

The connector contract itself states that this wrapper filters to `pull_request`-triggered runs and returns only the first page. Therefore, the empty array means only that this wrapper found no first-page pull-request-triggered run associated with that commit at observation time. It does **not** prove that the commit has no GitHub Actions runs, no push-triggered runs, no checks, or no workflow activity.

## Phase-1 gates

- Treat an empty connector result as `NO_MATCH_IN_WRAPPER_SCOPE`, not `NO_WORKFLOW_RUNS`.
- Record the exact commit SHA and observation time; status is mutable and reruns can create later attempts.
- Do not infer branch-wide or repository-wide CI state from a commit-scoped, pull-request-only first page.
- Do not infer account identity, credential type, OAuth/PAT/App scope, repository visibility, Actions permission, rate-limit budget, billing state, or write authority from a successful empty read.
- Keep dispatch, rerun, cancel, artifact/log download, secret access, and workflow or branch mutation excluded.
- Require a positive run receipt before admitting normalized fields such as `status`, `conclusion`, `run_attempt`, `event`, `head_sha`, workflow identity, or timestamps.
- Prefer webhook or check-suite delivery for durable high-frequency status propagation; use polling only at a bounded cadence with rate-limit handling.

## Measurements

| Dimension | Phase-1 result |
|---|---|
| Custom code avoided | Estimated 25–80 LOC for authenticated commit-filtered listing and response normalization; unvalidated because no positive run payload was observed |
| Operator minutes removed | 0 measured |
| Credentials | Connector reached GitHub with no error; identity, credential type, permissions, repository visibility, and custody remain unknown |
| Durability | Ephemeral point-in-time query over mutable run/attempt state; not a durable event stream |
| Observability | Low: empty normalized array and 386 ms connector time visible; raw URL, HTTP status, headers, request ID, pagination, rate limits, and underlying filters not returned in the receipt |
| Portability | Medium-low: commit SHA is portable Git identity, but Actions event/status/conclusion/run-attempt and wrapper filtering are GitHub-specific |
| Failure behavior | Not exercised; successful empty result is semantically ambiguous without wrapper-scope knowledge |
| Direct cost/quota evidence | $0 surfaced; one connector call observed; actual upstream requests and live GitHub quota counters unknown |
| Fitness credit | 0 pending positive status payload, source-bound ConsumerAck, and measured operator outcome |

## Verifier, consumer, falsifier

- **Verifier:** source-bound raw `GET /repos/TTaoGaming/hfo-gen-133/actions/runs?head_sha=<sha>&per_page=<bounded>` with explicit event policy, or GitHub Actions/checks UI for the same commit.
- **Consumer:** HFO CI release gates, branch-health summaries, and agent completion verification.
- **Strongest falsifier:** the raw endpoint or GitHub UI shows one or more runs for the same commit while the connector returns an empty array because of its forced `pull_request` filter, first-page truncation, normalization, or permission variance.

## Honest flaw

No positive workflow-run payload was observed, so status and conclusion field fidelity, ordering, attempts, pagination, branch/event variance, permission denial, `404`, `403`, `429`, transient `5xx`, rate-limit headers, and independent readback remain untested. The target commit may simply have no pull-request-triggered run. This phase establishes a narrow negative baseline and a connector-scope Andon, not proof that the candidate can yet satisfy general workflow-status monitoring.

## Phase-1 disposition

`PHASE1_ACCEPTED_WITH_EVENT_SCOPE_AND_EMPTY_RESULT_GATES`

## Next wake

Phase 2 should perform one smallest harmless positive read-only micro-use against a source-bound commit known to have a pull-request-triggered workflow run, if such a commit can be located without mutation. If no positive candidate exists, record `UNKNOWN` rather than broadening or manufacturing workflow activity.