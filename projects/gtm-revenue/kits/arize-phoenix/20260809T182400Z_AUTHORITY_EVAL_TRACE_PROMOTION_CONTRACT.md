# Authority × Eval Trace Promotion Contract — Arize AI / Phoenix

**Problem:** an agent revision can improve eval scores while also changing tool choice, tool arguments, principal context, runtime controls, latency, or cost. If those signals are reviewed separately, a team can miss an authority regression or spend time reconstructing whether the eval, control decision, trace, and rollback refer to the same revision.

**Ceiling:** public-safe synthetic utility. It does **not** claim Arize/Phoenix has an authorization defect, excess review cost, slow releases, incidents, customer demand, or compliance failures.

## WHY_THIS_MAY_MATTER

Source-backed facts:
- **2026-06-04:** Arize said production-agent improvement can require connecting trajectories, evals, datasets, code/prompt diffs, tool responses, and deployment history; it launched full-agent experimentation across tool use, retrieval, latency, trajectories, and eval results.
- **2026-06-03:** Arize described Microsoft ASSERT and Agent Control Specification (ACS) as sharing OpenInference telemetry, connecting evaluation, runtime controls, and observability.
- **2026-01-31:** Phoenix added separate Tool Selection and Tool Invocation evaluators.
- **Current 2026-08-09:** Phoenix presents tracing, evaluation, datasets/experiments, and cost/latency/performance measurement as core surfaces.

Hypothesis: some teams may benefit from one same-revision promotion record joining behavioral evidence and authority evidence.

## HOW_TO_USE_IN_2_MINUTES

1. Enter baseline and candidate revision IDs.
2. Fill each row with a trace ID, digest, run link, reviewer ref, or `MISSING`.
3. Apply the decision rule. Unresolved authority widening or missing rollback evidence is never `PROMOTE`.

| Gate | Evidence | Pass condition |
|---|---|---|
| Exact revision | `baseline=____ candidate=____` | All evidence below binds to candidate revision/run. |
| Principal | `principal/workload=____` | Expected identity is explicit. |
| Tool/action authority | `allow/deny diff=____` | No unexplained newly allowed action or lost deny edge. |
| Runtime control | `control/policy digest + decision=____` | Decision is attributable to exact control version + principal. |
| Held-out evals | `dataset/run=____` | No unacceptable regression in task success, tool selection/invocation, required-step, or prohibited-action cases. |
| Trace provenance | `trace/session=____` | Required model/tool/control spans exist for candidate. |
| Cost/latency | `baseline=____ candidate=____` | Measured and inside the team's declared envelope. |
| Approval | `reviewer/ref=____` | Required approval exists for material behavior/authority changes. |
| Rollback | `rollback_rev/test=____` | Specific rollback revision is identifiable and evidenced. |

### Authority delta

```text
NEWLY_ALLOWED: <principal> -> <tool/action> -> <review/control-ref>
NEWLY_DENIED:  <principal> -> <tool/action> -> <review/control-ref>
```

If `NEWLY_ALLOWED` is non-empty without explicit review/control evidence: `HOLD`.

## HELD_OUT_NEGATIVE_CONTROLS

| Synthetic mutant | Expected |
|---|---|
| Wrong principal calls a valid tool | `REJECT` |
| Candidate gains an unreviewed privileged action | `HOLD` |
| Prior deny silently becomes allow | `REJECT` |
| Tool choice passes but invocation violates schema/control | `REJECT` |
| Eval binds revision A; trace/control binds revision B | `REJECT` |
| Control-decision span or policy/control digest missing | `HOLD` |
| Quality improves but cost/latency is unmeasured | `HOLD` |
| Rollback named in prose but not identifiable/testable | `HOLD` |

## DECISION

- `PROMOTE`: all nine gates pass, no unexplained authority widening, held-out checks pass, operating envelope is measured, and approval + rollback are bound.
- `HOLD`: evidence is incomplete or an authority/cost/approval/rollback question remains.
- `REJECT`: prohibited action succeeds, a deny edge is lost without approval, principal/control provenance is wrong, evidence binds different revisions, or rollback evidence is invalid.

The recipient supplies its own quality, cost, latency, and approval thresholds.

## ASSUMPTIONS

- Behavioral and runtime-control evidence can be linked to one exact revision.
- Principal/policy provenance can be trace-native or trace-linked.
- OPA/Rego is one possible independent policy oracle, not an Arize/Phoenix requirement.
- The card is useful only if it is cheaper than the recipient's existing review path.

No savings, incident reduction, compliance benefit, or willingness to pay is claimed.

## FALSIFIER

Discard this utility if Phoenix/Arize AX, ACS/OpenInference, or the recipient's CI already canonically binds exact revision → principal/control decision → held-out evals → traces → cost/latency → approval → rollback at low review overhead, or if authorization is intentionally outside the observability/evaluation boundary.

## EVIDENCE_LINKS

- https://arize.com/blog/building-ai-factory-self-improving-agents-arize-ax/
- https://arize.com/blog/microsoft-open-trust-stack-openinference/
- https://arize.com/blog/from-observability-to-context-whats-next-for-arize-phoenix/
- https://arize.com/docs/phoenix/release-notes/02-2026/02-01-2026-tool-selection-and-tool-invocation-evaluators
- https://arize.com/phoenix
- https://arize.com/about-us/

## OPTIONAL_OPERATOR_REVIEWED_OUTREACH_NOTE — NO SEND

I saw Arize connecting full-agent experiments, OpenInference traces, and runtime-control telemetry. I made a one-page synthetic promotion contract for one narrow question: does the exact agent revision being promoted have matching eval, principal/control, trace, cost/latency, approval, and rollback evidence? If Phoenix/AX already makes that canonical—or intentionally leaves authority outside the product—the card is redundant; I would value the correction.
