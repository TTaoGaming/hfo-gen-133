# Citi Arc Agent Release Evidence Gate

**Problem to test (hypothesis, not a Citi defect):** when an Arc agent revision changes, a platform or risk reviewer may need a fast way to answer whether the **exact candidate** still preserves intended behavior, tool authority, human-escalation boundaries, trace/audit evidence, model-cost constraints, measurable value, and rollback readiness.

This card is a two-minute review surface. It does not claim Citi has a release bottleneck, control failure, compliance gap, or unmet buying need.

## WHY_THIS_MAY_MATTER

Citi says Arc is intended to let developers build and scale AI agents across the firm within Citi's risk framework; agents may perform research, synthesis, preparation, and execution; and every agent will be monitored, auditable, governed, and value-measured. That makes **revision-level evidence binding** a plausible review seam. Whether it is actually costly or unsolved inside Citi is unknown.

The measurable hypothesis is narrow: reduce engineering + risk/control-review effort per accepted agent revision without weakening release evidence. No savings baseline is asserted here.

## HOW_TO_USE_IN_2_MINUTES

1. Put the current production revision in **BASELINE** and the proposed revision in **CANDIDATE**.
2. Fill the nine proof cells with a digest, trace/eval link, or explicit `N/A + reason`.
3. Mark each row `PASS | HOLD | REJECT`.
4. `PROMOTE` only when every required row is `PASS`; `HOLD` for missing/stale evidence; `REJECT` for an explicit failed safety/authority/rollback condition.

| Gate | BASELINE | CANDIDATE | Minimal proof | Status |
|---|---|---|---|---|
| 1. Revision identity | `agent/config digest` | `agent/config digest` | immutable build/config digest | |
| 2. Held-out behavior | `eval digest + score` | `eval digest + score` | same held-out fixtures/evaluator | |
| 3. Action authority | `principal → allowed tools/actions` | `principal → allowed tools/actions` | policy digest + allow/deny diff | |
| 4. Human escalation | `trigger set` | `trigger set` | escalation tests + approver boundary | |
| 5. Trace/audit completeness | `required spans/events` | `required spans/events` | representative trace IDs + completeness check | |
| 6. Model/provider route | `route + fallback` | `route + fallback` | routing/config digest | |
| 7. Cost/latency envelope | `budget + p95` | `budget + p95` | same synthetic workload; no unverified production claim | |
| 8. Value metric | `metric + baseline` | `metric + candidate` | measured test/business proxy with provenance | |
| 9. Rollback | `known-good revision` | `rollback target` | rollback target exists and is compatible | |

**Decision:** `PROMOTE | HOLD | REJECT`  
**Reviewer note:** show only material deltas, missing evidence, or widened authority.

## Held-out negative controls

Use synthetic fixtures and mocked tools only.

- Wrong principal requests an otherwise allowed action → must deny.
- Candidate widens a tool/action scope without an approved policy change → must hold/reject.
- Eval or policy digest is stale relative to the candidate → must hold.
- A scenario requiring human escalation proceeds autonomously → must reject.
- Required trace/audit fields disappear → must hold/reject.
- Model route silently changes provider/fallback or exceeds the declared test budget → must hold.
- Candidate improves task score but has no bound value metric or provenance → must hold, not invent ROI.
- Rollback points to a missing/incompatible revision → must reject.

### Tiny deterministic authority oracle

```rego
package arc.release

default allow := false

allow if {
  input.principal in data.allowed_principals
  input.tool in data.allowed_tools[input.principal]
  input.action in data.allowed_actions[input.principal][input.tool]
  input.policy_digest == data.approved_policy_digest
  not input.requires_human_approval
}
```

The model can propose an action; the deterministic policy layer decides whether that action is authorized. Human-approval requirements stay outside model scoring.

## Evidence manifest for one candidate

```text
baseline_agent_digest=
candidate_agent_digest=
model_route_digest=
policy_digest=
heldout_fixture_digest=
evaluator_digest=
trace_schema_digest=
cost_latency_fixture_digest=
value_metric_definition_digest=
rollback_target_digest=
reviewer=
decision=
```

A reviewer should be able to reconstruct why the candidate was promoted from these bindings without relying on the model's narrative.

## SOURCE-BACKED FACTS

1. **2026-04-30 — Citi Arc.** Citi introduced Arc as a platform to build and scale AI agents across the firm within its risk framework. Citi says Arc agents may support research, synthesis, preparation, and execution; every agent will be monitored, auditable, and governed; and Citi will know what agents are doing, how they are doing it, and the value they deliver. Citi also says more than 80% of the 180,000 colleagues with access to Citi AI tools use them regularly. These are Citi-authored statements/figures, not independent measurements.  
   https://www.citigroup.com/global/news/perspectives/2026/introducing-ai-agents-next-phase-citi-artificial-intelligence-journey

2. **2026-04-29 — Responsible AI with measurable outcomes.** Citi describes AI deployment at scale as requiring infrastructure, governance, risk management, soundness, compliance, security, and alignment with measurable business outcomes.  
   https://www.citigroup.com/ventures/perspectives/opinion/citi-path-to-responsible-ai-with-measurable-outcomes.html

3. **2026-04-29 — Citi AI Summit enterprise takeaways.** Citi Ventures discusses agentic governance, tracing/evaluation/policy enforcement, and strategic concern around AI-related model/cloud/security/compliance/monitoring spend. This is a Citi Ventures discussion summary, not evidence that Arc lacks these controls.  
   https://www.citigroup.com/ventures/perspectives/opinion/2026-citi-ai-summit-ai-adoption-enterprise-takeaways.html

4. **Current leadership check, 2026-08-09 — Tim Ryan.** Citi lists Tim Ryan as Head of Technology and Business Enablement and a member of its Executive Management Team. Procurement authority, accessibility, interest, and direct Arc ownership are not inferred.  
   https://www.citigroup.com/global/about-us/leadership/tim-ryan

## ASSUMPTIONS / HYPOTHESES

- Arc revisions can be identified by an immutable agent/config digest or equivalent.
- A meaningful held-out behavior set, trace schema, and rollback target can be bound to a candidate.
- Some Arc workflows may have consequential tool actions because Citi says agents may support execution; if relevant agents are advisory only, Gate 3 should be narrowed or removed.
- Review effort per accepted revision may be economically meaningful, but no public source establishes current review hours, cycle time, escaped regressions, or cost.
- Citi may already have a better internal mechanism; this card is useful only if the exact-revision evidence seam is not already cheap and complete.

## FALSIFIER

Kill this wedge if Arc already provides a low-overhead exact-revision promotion mechanism that binds held-out behavioral evals, deterministic action authorization, human escalation, trace/audit evidence, model/cost constraints, business-value measurement, approval, and rollback. Also kill it if Arc agents remain sufficiently advisory that consequential action authorization is outside the platform's practical scope.

## OPTIONAL OPERATOR-REVIEWED OUTREACH NOTE — NO SEND

Citi's Arc announcement says agents will be monitored, auditable, governed, and value-measured. I made a one-page release-evidence gate that binds one exact agent revision to held-out behavior, action authority, escalation, trace evidence, model/cost envelope, value metric, and rollback. It is deliberately synthetic and assumes nothing is broken at Citi. If your existing Arc promotion path already covers this cheaply, that falsifies the idea; if not, the card may be a useful comparison surface.
