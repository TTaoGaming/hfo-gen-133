# WWT Agent Gateway Release Delta Card

**Identity × Tool Authority × Trace × Failure × Cost × Rollback**

A gateway revision can still “work” while changing who may call what, losing evidence across agent/tool handoffs, or weakening rollback confidence. This two-minute card asks one narrower production question: **did this exact candidate preserve the acceptance controls of the last accepted baseline?**

This is a public-safe template, not a claim that World Wide Technology (WWT) has a control gap.

## WHY_THIS_MAY_MATTER

### Source-backed facts

WWT currently describes production agent infrastructure using MCP servers, agent gateways, A2A/orchestration, authentication, rate limits, policy enforcement, observability, AI Proving Ground validation, and ARMOR security mapped to NIST AI RMF. WWT also frames agent production around governing what agents may touch, tracing decisions across handoffs, and containing misfiring agents.

WWT's June 16, 2026 “Defending at the Speed of AI” initiative is available through its Advanced Technology Center and Cyber Range for testing, validation, and operationalization before production. WWT currently lists Istvan Berko as Global Head of AI Cyber & Innovation.

### Hypothesis — not fact

Across heterogeneous client stacks, a delivery team **may** spend repeated consultant + client-security-review time proving that an exact gateway/MCP revision still preserves identity, tool authority, traceability, failure containment, cost/latency bounds, and rollback readiness.

No source used here establishes WWT review hours, margin leakage, failed deployments, compliance failures, client incidents, procurement interest, or unmet demand.

## HOW_TO_USE_IN_2_MINUTES

Choose one accepted baseline and one candidate. Put an evidence pointer or `MISSING` in each row.

| Gate | Baseline → candidate question | Evidence | Result |
|---|---|---|---|
| Revision | Are agent, gateway, policy, tool manifest, fixture, and rollback refs bound to exact digests? | `_____` | PASS / HOLD |
| Identity | Is principal/workload identity unchanged or explicitly reviewed? | `_____` | PASS / REJECT |
| Authority | Any new allow edge, lost deny edge, or wider scope? | `_____` | PASS / REJECT |
| Trace | Can one synthetic request be followed across gateway → agent → tool → handoff? | `_____` | PASS / HOLD |
| Failure | Does one injected loop/timeout remain inside the declared blast radius and terminate? | `_____` | PASS / REJECT |
| Envelope + rollback | Is candidate inside declared latency/cost bounds, with a tested immutable rollback target? | `_____` | PASS / HOLD |

**Verdict**
- `PROMOTE`: all gates pass; no unapproved authority widening.
- `HOLD`: evidence is missing, stale, or not bound to the exact candidate.
- `REJECT`: unapproved authority widening, lost deny edge, failed containment, or invalid rollback.

Default to `HOLD`.

## REVISION-BINDING TEMPLATE

```yaml
baseline_revision: "<immutable-ref>"
candidate_revision: "<immutable-ref>"
gateway_config_digest: "<sha256>"
tool_manifest_digest: "<sha256>"
policy_digest: "<sha256>"
heldout_fixture_digest: "<sha256>"
rollback_target: "<immutable-ref>"

principal:
  baseline: "synthetic:reader"
  candidate: "synthetic:reader"

authority_delta:
  added_allow_edges: []
  removed_deny_edges: []
  changed_scopes: []

evidence:
  policy_decisions: "<pointer>"
  cross_agent_trace: "<pointer>"
  injected_failure: "<pointer>"
  latency_cost_check: "<pointer>"
  rollback_check: "<pointer>"

decision: HOLD
```

## HELD-OUT NEGATIVE CONTROLS

Use invented principals, tools, data, and traces only.

1. Wrong principal with an otherwise-valid request.
2. One previously denied tool/action becomes allowed.
3. Candidate is judged using stale policy evidence.
4. One A2A/tool handoff loses trace correlation.
5. Mocked tool loops or a dependency times out.
6. Rollback ref cannot reproduce the accepted baseline fixture.

A useful gate should catch these without modifying the model prompt to reveal the test.

## DETERMINISTIC AUTHORITY ORACLE — STARTER

```rego
package agent_gateway.release

default allow := false

allow if {
  input.principal == "synthetic:reader"
  input.tool == "synthetic:lookup"
  input.action == "read"
  input.policy_digest == data.release.expected_policy_digest
}
```

The model may propose an action; policy decides whether it is permitted. The useful property is **independent authorization evidence bound to the same candidate revision as eval, trace, and rollback evidence**.

## EVIDENCE CEILING

This card does **not** prove that WWT lacks an equivalent mechanism, that any WWT/client agent escaped containment, that a compliance requirement was violated, that a deployment failed, or that this process saves money.

If ever measured, the proposed primary metric is **consultant + client security-review hours per accepted agent-infrastructure revision**; pilot-to-production acceptance time is secondary. Both remain hypotheses until measured.

## ASSUMPTIONS

- A production-acceptance unit can be represented by immutable revision + policy/config/tool/fixture/rollback digests.
- Consequential tool actions benefit from deterministic authorization independent of model scoring.
- A portable evidence contract may be useful across heterogeneous client stacks.
- Synthetic fixtures can test the acceptance shape without client data or production access.

## FALSIFIER

Kill this wedge if WWT's existing ARMOR + AI Proving Ground + agent-gateway process already binds each exact revision to identity, authorization decisions, traces, failure tests, cost/latency envelope, approval, and rollback with low review overhead.

Also kill it if WWT does not admit narrowly scoped external specialist capacity, or if portability creates more review work than it removes.

## EVIDENCE LINKS

First-party WWT sources verified for this artifact:

1. https://www.wwt.com/topic/cloud-ai-solutions/overview
2. https://www.wwt.com/video/when-ai-agents-escape-containment-how-to-secure-the-ai-factory
3. https://www.wwt.com/press-release/world-wide-technology-launches-defending-at-the-speed-of-ai-initiative-with-horizon3ai-empirical-security-infoblox-and-cognition
4. https://www.wwt.com/profile/istvan-berko/bio

## OPTIONAL OPERATOR-REVIEWED OUTREACH NOTE — NO SEND

> WWT already treats agent gateways, policy, observability, and pre-production validation as first-class production concerns. I made a one-page revision-delta card that binds identity, tool authority, traces, one failure test, cost/latency, and rollback to the exact candidate. It may be redundant with your existing process; if not, I would be interested in whether portable acceptance evidence helps across heterogeneous client stacks.

**NO SEND. Operator review is required before any outreach.**
