# Langfuse Agent Release Evidence Contract — Eval × Authority × Cost × Trace × Revision

> **Plausible problem (hypothesis):** an agent revision can pass quality evaluation while still changing tool authority, delegated identity, cost, or rollback requirements. This one-page contract keeps Langfuse evaluation evidence and external runtime-authorization evidence distinct, but reviewable together.

**Target-card digest:** `f13b3de41e230da7fd89fe114409d23e894df0c23aa0f85ffffdd21699d4097a`  
**Scope:** public-safe synthetic example only; no Langfuse account, credential, customer data, or production system used.

## WHY_THIS_MAY_MATTER

Langfuse already provides versioned experiment gates, deterministic code evaluators, structured recorded tool-call evaluation, and tracing/ex-post evaluation. Its security docs place runtime protective enforcement in external security libraries. The narrower question is: **did this exact revision pass both quality evidence and independent action-authority evidence, with cost/trace/rollback conditions attached?**

This is an integration-pattern hypothesis, not evidence of a Langfuse gap or customer pain.

## HOW_TO_USE_IN_2_MINUTES

1. Fill the exact candidate revision, Langfuse experiment/dataset version, and external policy revision.
2. Mark every required gate `PASS`, `FAIL`, or `HOLD`.
3. Promote only when all required gates pass; otherwise `HOLD`.

## RELEASE CONTRACT — synthetic example

| Gate | Evidence bound to `refund-agent@9d7c2a1` | Result |
|---|---|---|
| Langfuse quality | Dataset `support-refund-regression@2026-08-01T00:00Z`; threshold `>=0.90` | `PASS*` |
| Tool behavior | Required `lookup_order`; `issue_refund` forbidden without approval | `PASS*` |
| External authorization | Principal `support-agent/service-demo`; policy `refund-authz.rego@demo-v3`; verdict must be `ALLOW` or `REQUIRE_APPROVAL` | `PASS*` |
| Cost ceiling | `<= $0.05/test-case`; example `$0.031` | `PASS*` |
| Trace completeness | Revision + principal + tool call + policy verdict + eval + cost all linked | `PASS*` |
| Human approval | Refund `>$50` or `REQUIRE_APPROVAL` needs human receipt before state change | `PASS*` |
| Rollback target | Restore `refund-agent@7f3a91c` on any failed required gate | `RECORDED` |
| **Decision** | All evidence current and reproducible | **`PASS*`** |

`*` Synthetic/example values only; no test was executed.

### Negative controls

| Case | Expected result |
|---|---|
| Quality score `0.86 < 0.90` | Langfuse release gate fails → `HOLD` |
| `issue_refund($80)` without approval | tool-call evidence + external policy `DENY` → `HOLD` |
| Wrong principal `support-viewer/service-demo` | external policy `DENY` → `HOLD` |
| Policy used `demo-v2`, contract requires `demo-v3` | stale-policy mismatch → `HOLD` |
| Trace binding absent or cost `$0.071 > $0.05` | incomplete evidence / budget breach → `HOLD` |

### Control boundary

| Langfuse public capability | External/local responsibility in this pattern |
|---|---|
| Versioned dataset experiments and threshold-based CI/CD blocking | Bind the exact promoted agent/app revision to the evidence packet |
| Deterministic Python/TypeScript evaluators | Keep runtime authorization policy explicit if owned elsewhere |
| Structured recorded tool-call fields in evaluators | Decide whether the delegated principal was authorized for the state-changing action |
| Tracing + ex-post evaluation around external runtime guardrails | Enforce identity, allow/deny, approval, and rollback in the runtime control plane |

## SOURCE-BACKED FACTS vs HYPOTHESES

**Facts:** Langfuse published CI/CD experiment gates on 2026-05-25, code evaluators on 2026-05-28, and structured tool-call evaluator access on 2026-07-10. Current security docs describe runtime security libraries as a separate layer and Langfuse for tracing/evaluation around them. The About page lists Tobias Wochinger as a Product Engineer.

**Hypotheses/assumptions:** some teams may value a single release record joining those evaluation signals to independent authorization evidence. The relevant metric may be median reviewer/engineering hours from proposed revision to evidence-backed approval; no baseline or savings claim is known. Runtime authorization may intentionally remain outside Langfuse.

## STRONGEST FALSIFIER

Kill this wedge if Langfuse already has a low-overhead native workflow binding the exact promoted revision to versioned experiment results + deterministic tool/action policy + delegated identity/authority + cost ceiling + trace completeness + human approval + rollback. Also kill it if users prefer runtime authorization wholly separate and see no review value in the bridge.

## EVIDENCE LINKS

1. https://langfuse.com/changelog/2026-05-25-experiment-ci-cd-gates
2. https://langfuse.com/changelog/2026-07-10-evaluator-tool-calls
3. https://langfuse.com/docs/security-and-guardrails
4. https://langfuse.com/changelog/2026-05-28-code-evaluators
5. https://langfuse.com/about

## OPTIONAL OPERATOR-REVIEWED OUTREACH NOTE — NO SEND

Tobias — I made a one-page synthetic release contract that keeps Langfuse quality evidence separate from an external runtime-authorization verdict, then joins them at the exact revision being promoted. If that seam is already solved cleanly inside Langfuse or deliberately out of scope, that falsifies the idea quickly; otherwise I’d value a correction on what evidence a production reviewer actually needs.

**Status:** `NO_SEND`; operator review required before any external use.
