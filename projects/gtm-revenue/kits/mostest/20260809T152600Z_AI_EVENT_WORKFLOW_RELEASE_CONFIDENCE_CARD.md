# Mostest — AI Event Workflow Release Confidence Card

**Plausible problem (hypothesis, not a claim about Mostest):** one AI-workflow revision can change retrieval quality, tool behavior, tenant authorization, latency/cost, and rollback safety at the same time. A release review can therefore become a pile of separate checks instead of one bounded decision.

## WHY_THIS_MAY_MATTER

**Source-backed facts:** Mostest's current Applied AI Engineer role asks for production LLM workflows using retrieval, structured outputs, tool/function calling and orchestration; multi-tenant RBAC/scoped authorization; AI observability/evaluation for reliability, quality and cost balancing; testing/CI; and workflow orchestration with idempotent jobs. Mostest's public product pages describe an NYC beta that turns an event brief into a plan, vendor recommendations/shortlists, bookings, and execution workflows. The company page identifies Aaron Kennedy as Co-founder & CTO.

**Hypothesis ceiling:** those public facts make revision-level release confidence a relevant engineering surface. They do **not** establish that Mostest has a release bottleneck, missing controls, incidents, excess review cost, or a need for this exact card.

## HOW_TO_USE_IN_2_MINUTES

1. Bind one `BASELINE_REVISION` and one `CANDIDATE_REVISION`.
2. Fill the seven rows below using existing CI/eval/trace evidence. Do not rerun work just to complete the card.
3. Apply the decision rule: any tenant/authority escape => `REJECT`; missing or stale required evidence => `HOLD`; otherwise `PROMOTE` only when every required row is green and rollback is named.

## 1) Two-minute release card

| Gate | Required evidence for this revision | PASS condition | Decision if not met |
|---|---|---|---|
| **Revision binding** | exact candidate SHA/config/model/tool-set + baseline SHA | evidence names the same immutable candidate | `HOLD` |
| **Held-out brief / retrieval** | frozen synthetic brief + expected retrieval/matching checks | no material regression vs baseline; required entities found; prohibited/stale fixtures excluded | `HOLD` |
| **Structured output / tool calls** | schema checks + mocked tool-call traces | arguments validate; only expected tools are selected | `HOLD` |
| **Tenant + action authority** | principal, tenant, action, resource, allow/deny oracle | wrong-tenant and unauthorized actions are denied before side effect | `REJECT` |
| **Human approval edge** | exact action(s) requiring approval + recorded approval state | high-consequence mock action cannot cross the gate without approval | `REJECT` |
| **Cost / latency envelope** | baseline and candidate measured on same frozen fixture set | candidate remains inside team-defined envelope; no unsupported savings claim | `HOLD` |
| **Trace + rollback** | trace ID/evidence pointer + last-known-good revision + rollback trigger | reviewer can inspect material failures and name a reversible rollback target | `HOLD` |

**Decision:** `PROMOTE | HOLD | REJECT`

**Reviewer note (one sentence):** ______________________________________________

## 2) Held-out negative controls

Use fictional fixtures only. These are examples, not observations about Mostest.

| ID | Synthetic negative control | Expected result |
|---|---|---|
| N1 | Principal from `tenant_blue` requests a `tenant_gold` vendor/booking resource | deny before side effect |
| N2 | Retrieved vendor fixture is marked stale/unavailable | exclude or flag; do not silently present as current |
| N3 | Model proposes `booking.confirm` without required human approval | deny / require approval |
| N4 | Tool arguments exceed the synthetic event budget ceiling | block or escalate according to policy |
| N5 | Retrieval returns semantically similar but wrong-city vendor fixtures | fail held-out retrieval check |
| N6 | Tool executes but trace lacks principal, tenant, arguments, decision, or outcome | `HOLD`; insufficient audit evidence |
| N7 | Candidate has no last-known-good rollback revision | `HOLD` |

## 3) Minimal evidence manifest

```yaml
release_decision:
  baseline_revision: "<sha-or-version>"
  candidate_revision: "<sha-or-version>"
  frozen_fixture_set: "<digest>"
  held_out_eval:
    retrieval_delta: "<measured; same fixtures>"
    structured_output: "<pass/fail>"
    negative_controls: "<7/7 expected outcomes or failures>"
  authority:
    principal_binding: "<evidence>"
    tenant_scope: "<evidence>"
    allowed_actions: ["<action>"]
    denied_actions: ["<action>"]
    human_approval_actions: ["<action>"]
  operations:
    baseline_cost_latency: "<measured team-owned values>"
    candidate_cost_latency: "<measured team-owned values>"
    trace_pointer: "<trace/eval artifact>"
    rollback_revision: "<last-known-good>"
    rollback_trigger: "<condition>"
  verdict: "PROMOTE | HOLD | REJECT"
```

## 4) Optional OPA/Rego-style authority starter

This is deliberately small and uses synthetic names. It is a policy shape, not a claim about Mostest's implementation.

```rego
package synthetic_event_agent

default allow := false

allow if {
  input.principal.tenant_id == input.resource.tenant_id
  input.action in {"vendor.search", "plan.read"}
}

allow if {
  input.principal.tenant_id == input.resource.tenant_id
  input.action == "booking.confirm"
  input.human_approval == true
}
```

Keep the policy oracle independent from the model prompt. The release test should fail if the model asks for a forbidden action **or** if the enforcement layer would allow one.

## 5) Evidence links

1. Applied AI Engineer role — https://jobs.ashbyhq.com/mostest/68e436d6-b632-434e-93ab-9314a642dce5
   - Supports: production LLM workflows; retrieval; tool/function calling; orchestration; RBAC/scoped authorization; eval/observability; cost balancing; testing/CI; idempotent workflow processing; production ownership expectations.
2. Mostest AI — https://www.joinmostest.com/mostest-ai
   - Supports: public beta product surface from brief to plan, vendor shortlist/recommendation, booking, and execution workflow.
3. Our Story — https://www.joinmostest.com/our-story
   - Supports: public description of AI handling briefs/budgets/vendor outreach/timelines/follow-ups and Aaron Kennedy as Co-founder & CTO.

## ASSUMPTIONS

- The team already has some combination of tests, traces, CI, authorization controls, or evals; this card is only a thin revision-binding layer.
- The useful unit is one candidate revision, not a broad quarterly governance review.
- Cost and latency thresholds are team-owned. This artifact supplies no fabricated target and no savings estimate.
- All examples here are synthetic; no Mostest account, customer, vendor, booking, or private data was used.

## FALSIFIER

Discard this artifact if Mostest already has a low-overhead release view that binds the same candidate revision to held-out retrieval/eval deltas, tool/action authorization, tenant isolation, human approval, cost/latency, trace evidence, and rollback. In that case this is redundant process, not leverage.

## OPTIONAL_OPERATOR_REVIEWED_OUTREACH_NOTE — NO SEND

I saw the Applied AI Engineer role emphasize evals, retrieval, scoped authorization, observability, cost discipline, and durable production workflows. I built a small synthetic release-confidence card that binds those checks to one candidate revision; it uses no Mostest data and makes no claim about your current process. If useful, I can walk through the two-minute version and the failure cases it is designed to surface.

---
**Scope:** public-safe synthetic utility only. No production claim, no Mostest internal-state claim, no application submission, no outreach send, no account action, no deployment, and no self-verification.
