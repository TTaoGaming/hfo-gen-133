# FDE Prototype→Production Handoff Gate — Value × Eval × Authority × Cost × Ops

**Recipient problem:** a fast AI prototype can be easy to demo and still be hard to hand to a production team. The handoff gets ambiguous when business acceptance, held-out behavior, action authority, cost/latency, operational evidence, and rollback are reviewed in different places or against different revisions.

This is a **public-safe synthetic review card**, not a claim that TEKsystems Global Services (TGS) lacks such controls. Use it to bind one candidate workflow/agent revision to one production-handoff decision.

## WHY_THIS_MAY_MATTER

TGS publicly describes a Forward Deployed Engineering (FDE) process that moves from discovery to a functional prototype in under four weeks, then to a business case and transition into a project team for production operationalization. TGS also says the FDE model is intended to create repeatable solution patterns. A compact revision-bound handoff record may reduce review ambiguity at that boundary; whether it reduces cycle time at TGS is **unproven**.

## HOW_TO_USE_IN_2_MINUTES

1. Write the exact candidate revision and last-known-good rollback revision.
2. Mark each gate `PASS`, `HOLD`, or `REJECT` using attached evidence only.
3. `PROMOTE` only if every gate is `PASS`; any missing evidence is `HOLD`; a violated hard boundary is `REJECT`.

```text
candidate_revision: ____________________
last_known_good_revision: ______________
workflow/use_case: ______________________
reviewer: ______________________________
decision: PROMOTE | HOLD | REJECT
```

| Gate | Evidence to attach | PASS condition | Status |
|---|---|---|---|
| 1. Business value | Named success criterion + measured proof point from approved test/synthetic data | Criterion and measurement method are explicit; result meets the predeclared threshold | ☐ PASS ☐ HOLD ☐ REJECT |
| 2. Held-out behavior | Pinned held-out cases + result for this exact revision | No required regression; all critical negative cases behave as specified | ☐ PASS ☐ HOLD ☐ REJECT |
| 3. Action authority | Tool/action allowlist + deny rules + required human escalation + policy decision record | Candidate cannot exceed declared authority; deny/escalation tests pass | ☐ PASS ☐ HOLD ☐ REJECT |
| 4. Cost / latency | Model/tool route fixture + per-run or per-task ceiling + representative latency result | Test stays inside the declared envelope; fallback behavior is defined | ☐ PASS ☐ HOLD ☐ REJECT |
| 5. Operations / trace | Trace sample + model/prompt/tool/policy versions + alert/failure-injection evidence | A reviewer can reconstruct what happened and identify the deployed revision | ☐ PASS ☐ HOLD ☐ REJECT |
| 6. Rollback / owner | Rollback trigger + owner + last-known-good revision + reversibility check | A named owner can revert/disable the candidate using a tested path | ☐ PASS ☐ HOLD ☐ REJECT |

### Six held-out checks

| Check | Expected result |
|---|---|
| Known-good business case | Meets the predeclared business acceptance threshold |
| Quality regression / bad retrieval | `HOLD` or safe fallback; no silent promotion |
| Forbidden tool/action request | Denied by an independent authorization rule; trace records the deny |
| Human-escalation condition | Workflow pauses and routes to the declared human decision point |
| Cost/latency ceiling breach | Route falls back, stops, or `HOLD`s according to the declared policy |
| Missing trace or rollback evidence | `HOLD`; absence of evidence cannot count as green |

## Source-backed facts

- On **2026-04-14**, TGS announced an FDE function for rapid AI prototyping. Its published four-step process says a functional prototype can be built in under four weeks, followed by business-case creation and transition to a project team for production operationalization.
- The same announcement says the FDE model is intended to create repeatable solution patterns that accelerate future projects.
- On **2026-03-10**, TGS announced AWS AI Competency status across Agentic AI and Generative AI and described the competency as validating capability to deploy and operationalize AI at scale.
- TGS's current AWS agentic-AI service page says it builds secure, cost-effective generative/agentic AI solutions and supports end-to-end workflows using AWS services including Amazon Bedrock, Lambda, Step Functions, and DynamoDB.
- TGS's current careers page offers consultant opportunities generally; it does **not** establish that outside consultants are used inside the FDE function.
- TGS's current leadership page lists **Matt Payne** as Senior Vice President, TEKsystems Global Services. The FDE announcement also quotes him about the function. This does **not** prove procurement authority, accessibility, or interest.

## Hypotheses / assumptions

- **Hypothesis:** a single revision-bound handoff record could reduce ambiguity when a short-cycle prototype moves to a production project team.
- **Assumption:** the candidate workflow/agent can be versioned precisely enough to bind eval, policy, route, trace, and rollback evidence to one revision.
- **Assumption:** the delivery team can declare a business acceptance threshold and cost/latency envelope before promotion.
- **Assumption:** action authority can be represented as an allow/deny/escalate policy, whether implemented with OPA/Rego or another independent control.
- No savings, incidents, backlog, staffing shortage, review-hour reduction, or TGS deployment outcome is asserted.

## Falsifier

Kill this wedge if TGS already has a low-overhead mechanism that binds business acceptance, held-out quality, action authority, cost/latency, operational traces, human approval, and rollback to every FDE prototype promoted into a production project. Also kill the relationship hypothesis if TGS's FDE delivery model does not use external/consultant specialists for this class of work.

## Evidence links

- https://www.teksystems.com/en/insights/newsroom/2026/forward-deployed-engineering
- https://www.teksystems.com/en/insights/newsroom/2026/aws-ai-competency
- https://www.teksystems.com/en/who-we-are/partnerships/aws/agentic-ai-and-generative-ai-services
- https://www.teksystems.com/en/careers
- https://www.teksystems.com/en/who-we-are/our-leadership

## Optional operator-reviewed outreach note — DO NOT SEND AUTONOMOUSLY

> I saw TGS's new FDE model explicitly spans rapid prototype → business case → production-team handoff. I made a one-page revision-bound handoff gate that joins business acceptance, held-out evals, tool authority, cost/latency, traces, and rollback. It may be redundant with your internal process; if so, that itself is useful falsification. Happy to share the public-safe card for critique.

**Status:** public-safe synthetic artifact; `RELATIONSHIP_ONLY`; no TGS system access, deployment, application, outreach, or claimed production result.