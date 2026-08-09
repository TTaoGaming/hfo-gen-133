# Enterprise Agent Deployment Acceptance Card

> **Plausible recipient problem:** a customer-specific agent can look good in a demo while the production decision is still fragmented across business acceptance, held-out evaluation, authentication, action authority, budget, traceability, human escalation, and rollback. This card forces those signals into one revision-bound decision. **This is a hypothesis-driven review aid, not a claim that Wand lacks these controls.**

## WHY_THIS_MAY_MATTER

Wand's currently live Forward Deployed Engineer role owns the path from customer discovery and agentic prototyping through evaluation and production go-live, including troubleshooting across APIs, authentication, data, workflow logic, and agent behavior. The role also asks for reusable implementation playbooks. Separately, Wand OS already describes native governance, rules, budgets, decision tracking, oversight, and agent accountability.

That makes the useful wedge narrow: **not “add governance,” but make one customer deployment decision reviewable from one exact revision if the evidence is otherwise scattered.**

## HOW_TO_USE_IN_2_MINUTES

1. Fill the header for one candidate workflow/revision and its known-good rollback.
2. Mark each gate `PASS | HOLD | FAIL` only from linked evidence. Missing or unexecuted evidence is `HOLD`, never green.
3. Run the negative controls. `PROMOTE` only if every required gate and negative control passes; otherwise record the exact blocker.

### Deployment header

| Field | Value |
|---|---|
| Customer / workflow | `[public-safe or internal identifier]` |
| Candidate revision | `[immutable revision / config / prompt / toolset ID]` |
| Known-good rollback revision | `[revision ID]` |
| Reviewer / approver | `[named human role]` |
| Decision time | `[UTC]` |

### Promotion gates

| Gate | Evidence to attach | Pass condition | Status |
|---|---|---|---|
| **1. Business value** | Success criterion + observed result | Pre-agreed criterion met on representative test workload | `[ ]` |
| **2. Held-out eval** | Frozen eval-set ID, score, regression delta | Required quality threshold met; no critical regression | `[ ]` |
| **3. Identity / authentication** | Exact agent/service principal + auth method | Candidate runs only as intended principal; no ambiguous shared identity | `[ ]` |
| **4. Action authority** | Allowed + forbidden tools/actions; policy decision receipt | Every action stays inside approved boundary; forbidden action is denied or escalated | `[ ]` |
| **5. Budget / latency** | Per-task/model/tool budget + p95 latency evidence | Cost and latency remain inside pre-agreed envelope | `[ ]` |
| **6. Trace / human escalation** | Trace ID(s), decision/tool-call record, HITL rule | Required actions are attributable; mandatory escalation path is exercised | `[ ]` |
| **7. Rollback** | Rollback revision + rollback check | Known-good revision is identifiable and rollback procedure is viable | `[ ]` |

### Held-out negative controls

| Control | Expected result | Status |
|---|---|---|
| Wrong or missing principal | Deny / no action | `[ ]` |
| Permission widened beyond approved scope | Deny or require fresh human approval | `[ ]` |
| Prompt/tool request attempts forbidden action | Deny, contain, and trace | `[ ]` |
| Evidence belongs to a stale/different revision | `HOLD` | `[ ]` |
| Budget or latency exceeds release envelope | `HOLD` or bounded fallback | `[ ]` |
| Mandatory human escalation is absent/bypassed | `HOLD` | `[ ]` |
| Rollback target is missing or mismatched | `HOLD` | `[ ]` |

### Verdict

- `PROMOTE` — all required gates and negative controls pass for the **same exact revision**.
- `HOLD` — evidence is missing, stale, unexecuted, or a threshold is not met but the candidate may be repairable.
- `REJECT` — the candidate design conflicts with an approved identity/action/data boundary or cannot be given a credible safe rollback path.

**Decision:** `[PROMOTE | HOLD | REJECT]`  
**Exact blocker or evidence pointer:** `[link / ID]`

## SOURCE-BACKED FACTS

- On **2026-08-09**, Wand's official Ashby page exposed a live remote, full-time **Forward Deployed Engineer** role for the United States timezone. The role owns enterprise deployments from evaluation/solution design through production go-live and explicitly names agent/LLM workflows, tool-calling, RAG, orchestration, multi-agent systems, evaluation, APIs, authentication, and production troubleshooting.
- Wand's product page describes governance/visibility/control, rules, budgets, outcomes, policies, access/autonomy guardrails, decision tracking, and agent accountability as part of Wand OS.
- Wand's **2026-07-21** Protopia AI announcement describes an additional inference-privacy layer for sovereign AI deployments. This is a product/security signal, not evidence of a customer-delivery failure.

## HYPOTHESIS — NOT A FACT CLAIM

A one-page, exact-revision acceptance record **may** reduce review ambiguity or handoff friction when an FDE, customer engineering team, security reviewer, and business owner each hold different parts of the evidence. No public source reviewed here establishes missed go-lives, excessive reviewer hours, security incidents, margin leakage, or demand for an external release-gate product.

## ASSUMPTIONS

- A customer deployment has an identifiable candidate revision and known-good rollback revision.
- Existing eval, policy, trace, and cost evidence can be referenced rather than recopied into this card.
- Human approval remains authoritative; this card does not grant deployment authority.
- All example/test data remains public-safe or synthetic unless the recipient uses the template inside its own approved environment.

## FALSIFIER

Discard this artifact if Wand already has a low-overhead mechanism that binds business acceptance, held-out evals, identity/authentication, action authority, budget/cost, trace/HITL evidence, human approval, and rollback to the exact promoted customer revision **and** that mechanism already produces the review handoff needed by FDEs and customers.

## EVIDENCE LINKS

1. https://jobs.ashbyhq.com/wand-ai/81bcb55e-c0a6-4772-959a-faf7f788aca9
2. https://wand.ai/careers
3. https://wand.ai/product-page
4. https://wand.ai/blog/wand-ai-and-protopia-ai-partner-to-power-sovereign-ai
5. https://wand.ai/build-the-future-with-wand-ai

## OPTIONAL OPERATOR-REVIEWED OUTREACH NOTE — DO NOT SEND AUTOMATICALLY

I built a one-page synthetic deployment-acceptance card from the public FDE requirements. It binds value, held-out evals, identity/authority, budget, trace/HITL, and rollback to one candidate revision. I would use it as a work sample rather than claim Wand lacks an internal equivalent; the point is to show how I structure the evaluation-to-production handoff.