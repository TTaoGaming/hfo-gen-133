# Pydantic AI Release Evidence Manifest

**Problem this card addresses:** an agent revision can change more than code. Model/provider selection, tool authority, approval rules, evaluator versions, durable-runtime behavior, and cost/latency can all move at once. A reviewer needs one small place to decide whether the exact revision is ready to promote, should be held for missing evidence, or should be rejected for a material regression.

This is a **public-safe synthetic review aid**, not a claim that Pydantic or its users lack release controls.

## WHY_THIS_MAY_MATTER

### Source-backed facts
- Pydantic AI v2.0.0 was released as the stable V2 release on **2026-06-23**.
- Pydantic AI supports systematic evals and Logfire/OpenTelemetry observability, including behavior, tracing, and cost tracking.
- Pydantic Logfire supports **online evals** that reuse evaluator classes used for offline datasets and can score sampled production traces.
- Pydantic AI supports **human-in-the-loop tool approval**, durable execution integrations, MCP, and model routing through Pydantic AI Gateway.
- Pydantic AI Gateway exposes cost limits, usage tracking, failover/load-balancing routing groups, and OpenTelemetry-backed observability.

### Hypothesis
For teams shipping non-trivial Pydantic AI agents, the remaining friction may be less about missing primitives and more about **binding those primitives to one exact release decision**. If a reviewer must manually reconcile eval results, traces, tool authority, model routing, cost/latency, durable runtime identity, and rollback, promotion cycle time may increase and important deltas may be missed.

No source cited here establishes excess review hours, failed releases, demand for this manifest, or willingness to adopt it.

## HOW_TO_USE_IN_2_MINUTES

1. Fill the **Revision Binding** row first. If the exact candidate or rollback revision is unknown, stop at `HOLD`.
2. Mark only the rows that materially changed versus the production baseline.
3. Run the seven negative controls. Any unauthorized tool/principal path or rollback mismatch is `REJECT`; missing evidence is `HOLD`.
4. Promote only when every required field is revision-bound and every mandatory check is green.

## Release decision

| Gate | Exact evidence to bind | Example acceptance rule | State |
|---|---|---|---|
| Revision binding | code/agent digest, config digest, baseline revision, rollback revision | All four are immutable and point to the reviewed candidate | ☐ |
| Offline eval | dataset digest, evaluator digest, score, threshold | Frozen held-out set meets predeclared threshold | ☐ |
| Trace/tool behavior | fixture/trace set, expected tool calls, forbidden calls | No new forbidden tool path; expected calls remain observable | ☐ |
| Authority + HITL | principal, tool allowlist/policy digest, approval-required actions | Privileged actions require the intended approval path | ☐ |
| Model + routing | model/provider config digest, routing policy | Candidate uses only reviewed routes/fallbacks | ☐ |
| Cost + latency | measured synthetic/fixture envelope | No unexplained regression beyond declared ceiling | ☐ |
| Durable runtime | adapter/runtime identity + replay/recovery check | Candidate resumes/replays under the reviewed runtime contract | ☐ |
| Production baseline | reference revision + online-eval/trace comparison window | Candidate comparison uses a named baseline, not memory | ☐ |
| Rollback | rollback revision + rollback trigger | Rollback target exists and is compatible with current state | ☐ |

### Verdict
- **PROMOTE** — every required row is bound to the exact candidate; mandatory negative controls pass; no material unexplained regression remains.
- **HOLD** — required evidence is missing, stale, incomparable, or not revision-bound.
- **REJECT** — observed authority widening, rollback mismatch, held-out regression beyond the declared limit, or another explicit stop condition is present.

## Held-out negative controls

Use tiny synthetic fixtures; these are review probes, not claims about production behavior.

| Probe | Expected result |
|---|---|
| Wrong principal requests a privileged tool | Denied or routed to the required human approval path |
| Candidate gains a newly authorized tool not present in baseline | `REJECT` unless the authority change is explicitly reviewed |
| Approval-required tool call has no approval evidence | `HOLD` or `REJECT` per policy; never silently promote |
| Frozen eval dataset/evaluator digest does not match the recorded revision | `HOLD` |
| Model route/fallback changes and cost/latency exceeds the declared envelope | `HOLD` until reviewed; `REJECT` if outside the accepted ceiling |
| Durable replay/resume uses a different adapter/runtime identity than reviewed | `HOLD` |
| Rollback revision is missing, incompatible, or points to the candidate itself | `REJECT` |

## Minimal manifest

```yaml
release_id: "synthetic-example"
candidate:
  code_sha256: "<required>"
  agent_config_sha256: "<required>"
baseline:
  revision: "<required>"
rollback:
  revision: "<required>"
offline_eval:
  dataset_sha256: "<required>"
  evaluator_sha256: "<required>"
  score: "<measured>"
  threshold: "<predeclared>"
authority:
  principal: "<synthetic>"
  policy_sha256: "<required>"
  approval_required_tools: []
model_routing:
  config_sha256: "<required>"
cost_latency:
  fixture_id: "<required>"
  max_cost_per_case: "<declared ceiling>"
  max_p95_latency_ms: "<declared ceiling>"
durable_runtime:
  adapter: "<Temporal|DBOS|Prefect|Restate|other>"
  adapter_version: "<required>"
production_baseline:
  reference: "<named baseline or N/A for offline-only review>"
verdict: "PROMOTE | HOLD | REJECT"
reason: "<one sentence>"
```

## Evidence links

- Pydantic AI V2 upgrade guide / stable v2.0.0 date: https://pydantic.dev/docs/ai/project/changelog/
- Pydantic Logfire online evals announcement (2026-04-30): https://pydantic.dev/articles/online-evals-pydantic-logfire
- Pydantic AI overview: https://pydantic.dev/docs/ai/overview/
- Durable execution overview: https://pydantic.dev/docs/ai/capabilities/durable_execution/overview/
- Pydantic AI Gateway: https://pydantic.dev/docs/ai/overview/gateway/
- Douwe Maan public author page / Pydantic AI Lead Engineer: https://pydantic.dev/authors/douwe-maan

## Assumptions

- The team already has its own CI/CD and source-of-truth for code/config revisions.
- Existing Pydantic Evals, Logfire/OTel traces, HITL controls, durable-runtime integrations, and Gateway configuration remain the underlying evidence sources.
- This manifest is useful only if the cost of binding those surfaces is lower than the review friction it removes.
- Thresholds, policies, model routes, and rollback rules are supplied by the team; this card does not invent them.

## Falsifier

**Discard this artifact** if Pydantic already has a first-party or canonical low-overhead mechanism that binds an exact agent revision to offline-eval thresholds, trace/tool behavior, principal/tool authority, HITL policy, model/cost routing, durable-runtime identity, production baseline, and rollback in one promotion decision—or if users prefer these checks to remain independent CI primitives.

## Optional operator-reviewed outreach note — NO SEND

> I put together a one-page release-evidence manifest for a Pydantic AI agent revision. It does not replace Evals, Logfire, Gateway, HITL, or durable execution; it just binds their evidence to one `PROMOTE | HOLD | REJECT` decision. If you already have a canonical pattern for this, that would falsify the idea quickly. If not, I can share the tiny synthetic example.

**NO_SEND. Operator review required before any outreach.**
