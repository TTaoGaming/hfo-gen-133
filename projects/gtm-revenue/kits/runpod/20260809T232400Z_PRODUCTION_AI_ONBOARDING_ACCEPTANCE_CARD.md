# Runpod Production AI Onboarding Acceptance Card

**Use case:** one customer-facing AI workload moving from a working POC to an accepted production revision.

A POC can be technically functional while still leaving the handoff team to reconstruct whether the new revision preserved performance, cost bounds, observability, failure behavior, and rollback. This card makes those deltas explicit. It does **not** assert that Runpod currently lacks such a mechanism.

## WHY_THIS_MAY_MATTER

**Source-backed facts**

- Runpod's live Forward Deployed Engineer US role owns architectural recommendations, POCs for potential high-spending customers, onboarding, complex escalations, log/code analysis, testing, product feedback, and documentation.
- Runpod Serverless exposes autoscaling controls, worker bounds, endpoint metrics, job states, cold-start metrics, logs, and production-oriented deployment paths.
- Runpod states that more than one million developers use the platform and that many use it for production environments. Runpod also says it crossed one million developers and raised a $100M Series A in 2026. These are company-authored claims.

**Hypothesis, not fact**

As workload revisions change model/container/configuration/scaling choices, an FDE or customer engineer may benefit from a compact acceptance record that shows only the material baseline→candidate deltas. No public source establishes that Runpod has excessive onboarding time, support load, reliability problems, or demand for an external release-gate product.

## HOW_TO_USE_IN_2_MINUTES

1. Fill the **identity row** with exact baseline and candidate digests.
2. Enter observed or agreed envelopes for the six checks below.
3. Mark each row `PASS`, `HOLD`, or `FAIL`; attach one evidence pointer.
4. Run one or more held-out negative controls.
5. Promote only if all required rows pass and the rollback target is exact and available.

### Identity

| Field | Baseline | Candidate |
|---|---|---|
| workload / endpoint |  |  |
| model digest or immutable version |  |  |
| container / code digest |  |  |
| dependency lock digest |  |  |
| endpoint/config digest |  |  |
| fixture-set digest |  |  |
| evaluator version/digest |  |  |
| rollback target digest |  |  |

### Acceptance checks

| Gate | What to compare | Suggested evidence | Verdict |
|---|---|---|---|
| 1. Functional outcome | success/error semantics on the same representative fixture set | request result summary + fixture digest |  |
| 2. Latency / throughput | agreed percentiles or throughput envelope, including cold-start behavior when relevant | measured execution, delay, cold-start, throughput summary |  |
| 3. Scaling / concurrency | min/max workers, autoscaling rule, concurrency assumptions, throttling or queue behavior | config diff + worker/job metrics |  |
| 4. Cost envelope | compute cost per successful request/job under the same workload definition | observed billable worker time or operator-supplied rate × billable seconds ÷ successful requests |  |
| 5. Observability | required logs/metrics are present and attributable to the exact candidate revision | log/metric pointers + revision identifier |  |
| 6. Failure + rollback | injected failure produces bounded behavior; rollback target restores the accepted baseline | failure fixture result + rollback rehearsal/pointer |  |

**Decision rule**

- `PROMOTE`: all required gates pass; candidate identity and rollback target are exact; no held-out control escapes.
- `HOLD`: evidence is missing, stale, non-comparable, or an assumption has not been validated.
- `REJECT`: a required gate fails, a safety/cost bound is exceeded, or rollback identity is invalid.

Do not convert `HOLD` into `PROMOTE` by dropping a row, loosening an envelope after seeing the result, or replacing the held-out fixture set with an easier one.

## Held-out negative controls

Use synthetic or authorized test data only.

| Control | Injected condition | Expected gate behavior |
|---|---|---|
| NC-01 cold start | startup exceeds the accepted cold-start envelope | `REJECT` or explicit approved exception |
| NC-02 latency regression | candidate violates the agreed latency/throughput envelope | `REJECT` |
| NC-03 runaway scale/cost | worker/concurrency configuration exceeds the approved bound | `REJECT` |
| NC-04 blind revision | candidate emits insufficient logs/metrics to attribute failure to the exact revision | `HOLD` |
| NC-05 dependency mismatch | container/dependency fixture is incompatible with the accepted runtime assumptions | `REJECT` |
| NC-06 partial failure | a subset of requests fail, time out, or return malformed results | `REJECT` unless the agreed contract explicitly permits it |
| NC-07 stale baseline | baseline/config/fixture digest does not match the accepted reference | `HOLD` |
| NC-08 rollback mismatch | recorded rollback target is missing, mutable, or does not restore the accepted reference | `REJECT` |

## Compact evidence record

```yaml
workload_id:
baseline_digest:
candidate_digest:
fixture_set_digest:
evaluator_digest:
required_gates: [functional, performance, scaling, cost, observability, failure_rollback]
verdicts:
  functional:
  performance:
  scaling:
  cost:
  observability:
  failure_rollback:
negative_controls_run: []
rollback_target_digest:
overall: HOLD
reviewer:
evidence_pointers: []
```

The default is `HOLD` until evidence is filled. This is a review aid, not a benchmark, certification, warranty, or production claim.

## Evidence links

Public sources verified for this card:

1. Runpod — Forward Deployed Engineer US: https://jobs.ashbyhq.com/runpod/24b589d4-1868-4e6e-8e79-9a81c50db282
2. Runpod — One Million Developers on Runpod, and the Cloud We're Building Next: https://www.runpod.io/blog/one-million-developers
3. Runpod — What's new in Runpod Serverless: Faster cold starts, batch inference, and no-Docker deploys: https://www.runpod.io/blog/whats-new-in-runpod-serverless-faster-cold-starts-batch-inference-and-no-docker-deploys
4. Runpod — About: https://www.runpod.io/about
5. Runpod Docs — Job states and metrics: https://docs.runpod.io/serverless/endpoints/job-states
6. Runpod Docs — Endpoint settings: https://docs.runpod.io/serverless/endpoints/endpoint-configurations
7. Runpod Docs — Monitor logs: https://docs.runpod.io/serverless/development/logs

## Assumptions

- The same representative fixture set can be run against baseline and candidate.
- The reviewer can identify immutable or sufficiently stable workload/config/code/model versions.
- Performance and cost envelopes are supplied by the customer/team; this card does not invent them.
- "Cost per successful request/job" is calculated from observed billing data or an operator-supplied compute rate, not a fabricated Runpod price.
- Synthetic negative controls can be exercised without customer or production data.

## Falsifier

Discard this wedge if Runpod already has a low-overhead standard handoff that binds representative fixtures, workload/config revision, performance and cost envelopes, observability, failure injection, acceptance verdicts, and exact rollback evidence for each POC→production transition. Also downgrade the employment route if the PST-region requirement cannot be truthfully satisfied.

## Optional operator-reviewed outreach note — NO SEND

I noticed the Runpod FDE role spans POCs, onboarding, performance/debugging, testing, and production handoffs. I made a one-page synthetic POC→production acceptance card that binds workload revision to performance, cost, observability, failure behavior, and rollback. It may be redundant with your internal process; if it is, that itself is useful feedback.

**Status:** public-safe preparation only. No application, outreach, account action, paid compute, deployment, benchmark, or production claim.
