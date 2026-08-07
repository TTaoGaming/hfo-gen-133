# LiteLLM — Eval → Policy → Routing Preflight

**Audience:** AI/ML platform engineers and LiteLLM product/engineering teams evaluating policy-aware routing or agent/MCP controls.

**Status:** public-safe utility artifact · hypothesis-driven · no claim that LiteLLM currently fails any check.

## WHY_THIS_MAY_MATTER

LiteLLM already exposes the important primitives: Router Plugins can enrich routing context and narrow `candidate_models`; AutoRouter is actively measuring quality/cost behavior; Microsoft ASSERT can turn organizational policy into agent-evaluation scenarios; and the AI Gateway exposes budgets, guardrails, RBAC, routing, MCP/agent traffic and observability.

**Narrow hypothesis — not a LiteLLM gap claim:** enterprise platform teams may still spend repeated engineering/review time connecting **held-out evaluation evidence + organizational policy + model/tool authority** into one auditable deployment decision.

A useful contract is:

`eval verdict → policy decision → allowed model/tool/agent route → trace evidence → rollback condition`

The checklist below tests that contract without adding another gateway.

## HOW_TO_USE_IN_2_MINUTES

For a routing/plugin change, mark each row **YES / NO / N/A**. Any **NO** in rows 2, 6, 7 or 9 is a **hold** until explicitly risk-accepted.

| # | Two-minute release check | Evidence to bind | Likely LiteLLM / adjacent primitive | Fail-safe default |
|---|---|---|---|---|
| 1 | **Business/quality target named?** | metric + owner + threshold | AutoRouter benchmark / application metric | do not promote without a measurable target |
| 2 | **Held-out eval version + pass threshold bound?** | eval-set ID/hash + verdict + timestamp | Microsoft ASSERT or another eval harness | missing verdict must not broaden access |
| 3 | **Candidate model pool explicit?** | model/deployment allowlist | Router / Router Plugin `candidate_models` | route only inside the declared pool |
| 4 | **Cost ceiling explicit?** | budget + expected route/classifier overhead | budgets/rate limits + AutoRouter cost visibility | stop or use pre-approved lower-cost route |
| 5 | **Tenant/data constraints explicit?** | tenant, region/residency, data class | Router Plugin signals + auth/guardrails | remove non-compliant candidates |
| 6 | **Agent/MCP authority scope explicit?** | actor, action/tool, resource, purpose | RBAC/custom auth/guardrails; optional external policy adapter | deny high-impact action when authority is absent |
| 7 | **Policy/eval evidence fresh enough?** | policy version + eval version + expiry | versioned external policy/eval inputs | expired/missing evidence = hold or conservative route |
| 8 | **Routing reason observable?** | selected route + signals + reason + cost class | Router Plugin signals + OTel/Datadog/logging | no silent policy bypass |
| 9 | **Rollback/default behavior defined and tested?** | rollback route + trigger + negative test | Router fallback/default configuration | known-safe route or explicit error, never silent broadening |
| 10 | **Audit record binds the decision inputs?** | router/plugin/policy/eval versions + trace ID | spend/logging/OTel + external deployment metadata | deployment is not "evidence-backed" until versions are reconstructable |

### Three held-out negative tests

1. **Missing eval evidence:** remove the held-out verdict. Expected: the candidate pool does **not** silently expand.
2. **Policy eliminates every candidate:** drive the policy/plugin to an empty model set. Expected: explicit failure/hold rather than bypassing policy. LiteLLM's Router Plugin documentation currently states that an empty plugin-filtered pool raises instead of falling back to the full pool.
3. **Expired policy/eval version:** present a stale evidence bundle. Expected: conservative route/hold according to the team's defined contract; this is a proposed operating rule, not a claim about LiteLLM's default behavior.

## Optional vendor-neutral policy seam

If a team needs deterministic authorization beyond gateway configuration, keep the adapter replaceable:

```text
routing_context
  + eval_verdict(version, threshold, expiry)
  + tenant/data/action context
        ↓
policy_adapter  # OPA/Rego, Cedar, custom PDP, etc.
        ↓
allow | deny | narrowed_candidate_models | required_human_review
        ↓
LiteLLM Router Plugin / gateway route + trace
```

**OPA/Rego is an example because the operator has demonstrated policy-as-code work; this artifact does not claim an official LiteLLM↔OPA integration or endorsement.**

## SOURCE-BACKED FACTS

- **Router Plugins — July 17, 2026:** LiteLLM says plugins receive routing context, can narrow `candidate_models`, can add downstream signals, and were requested for signals including tenant policy and budget caps. LiteLLM also says the design is still evolving and requests feedback.  
  https://docs.litellm.ai/blog/router-plugins-on-the-proxy
- **AutoRouter cost visibility — August 6, 2026:** LiteLLM added estimated savings/usage views and per-request classifier-cost reporting; the post invites design-partner feedback.  
  https://docs.litellm.ai/blog/auto-router-spend-visibility
- **Auto Router v1.97 — August 4, 2026:** LiteLLM published usage/quality routing changes and cost/usage benchmarking against a frontier-model baseline.  
  https://docs.litellm.ai/blog/auto-router-context-and-benchmarks
- **LiteLLM × Microsoft ASSERT — June 3, 2026:** LiteLLM describes policy-driven agent evaluation where organizational policies become targeted evaluation scenarios run through the gateway.  
  https://docs.litellm.ai/blog/litellm-microsoft-assert
- **AI Gateway — observed August 7, 2026:** LiteLLM publicly positions LLM, MCP and Agent gateways alongside budgets/rate limits, guardrails, RBAC, routing and Datadog/OpenTelemetry logging.  
  https://www.litellm.ai/ai-gateway

## ASSUMPTIONS

- The target user operates LiteLLM as shared platform infrastructure rather than a single developer proxy.
- The organization has policy/eval evidence worth versioning and enforcing at release/runtime boundaries.
- Some runtime decisions involve sufficiently different quality, cost, data or authority constraints to justify an explicit contract.
- The checklist's value is **coordination/audit clarity**, not replacement of LiteLLM's existing gateway, ASSERT, guardrails, RBAC or Router Plugins.

## FALSIFIER

Retire or materially revise this artifact if current LiteLLM/ASSERT functionality already binds eval verdict version/expiry directly to runtime model/tool authorization and auditable routing decisions with no recurring user implementation burden, or if real LiteLLM users consistently report a different higher-cost problem.

## OPTIONAL_OPERATOR_REVIEWED_OUTREACH_NOTE — DO NOT SEND AUTOMATICALLY

> LiteLLM already has most of the primitives I would normally suggest—Router Plugins, ASSERT-style policy evals, gateway auth/governance and increasingly measurable AutoRouter cost/quality behavior. I mapped one narrower question: how should a platform team bind a held-out eval verdict and policy version to the allowed model/tool route and its audit trace? I turned it into a 10-point two-minute preflight rather than another gateway proposal. If that boundary is useful, I'm happy to share the one-page checklist; if LiteLLM already solves it cleanly, that would be useful feedback too.

## Honest limitation

All cited product facts are first-party LiteLLM sources. That is strong evidence of the product surface but weak evidence of customer pain or willingness to pay. No customer baseline, savings figure, incident rate, deployment result or commercial demand is asserted here.