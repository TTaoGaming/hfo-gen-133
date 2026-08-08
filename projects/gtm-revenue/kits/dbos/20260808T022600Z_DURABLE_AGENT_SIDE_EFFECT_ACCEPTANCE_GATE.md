---
schema_id: hfo.gen133.gtm.proof_kit.v1
producer: S07_GTM_PROOF_KIT_BUILDER
task_id_expected: 6a506f6dc5c08191b95f1707d7f00c2d
target: DBOS
target_species: PRODUCT_PLATFORM
utility: Durable Agent Side-Effect Acceptance Gate — Replay × Authority × Evidence
valid_time_utc: 2026-08-08T02:26:00Z
expiry_utc: 2026-08-14T14:08:00Z
privacy: PUBLIC_SOURCES_ONLY
external_send_authority: NONE
---

# Durable Agent Side-Effect Acceptance Gate — Replay × Authority × Evidence

**Plausible problem:** a workflow can recover correctly after a crash while the business action around it is still wrong—for example, an external side effect is duplicated, a retry uses stale authority, a human approval is bypassed on replay, or the trace cannot explain why a privileged action was allowed.

This is a **production-readiness companion to DBOS's existing durability and observability primitives**, not a defect report, audit, or claim that DBOS lacks these controls.

## WHY_THIS_MAY_MATTER

DBOS already provides strong durability, recovery, workflow inspection, metrics, audit logs, human-in-the-loop patterns, agent-framework integrations, and replay/fork tooling. DBOS also publicly names wrong-tool invocation and misleading agent output as real classes of production-agent failure. The narrow hypothesis is that some DBOS users may still benefit from a reusable acceptance layer that distinguishes **execution correctness** from **business-action correctness** at non-transactional side-effect and authorization boundaries. That hypothesis is unverified.

## HOW_TO_USE_IN_2_MINUTES

Pick one privileged or externally visible agent action—refund, ticket mutation, deployment request, customer message, entitlement change, or similar. Mark each row `GREEN`, `UNKNOWN`, or `RED`. `GREEN` requires inspectable evidence. Treat any `RED` on duplicate-action prevention, authority, approval, or reconstruction as a release hold until the application's own owner accepts the risk.

| # | Acceptance check | GREEN evidence | Fast held-out / negative probe |
|---|---|---|---|
| 1 | **External side-effect idempotency / reconciliation** | Every non-transactional external action has a stable idempotency key, reconciliation rule, or explicit compensation path. | Replay the same logical action with the same business key; verify it cannot silently create a second external effect. |
| 2 | **Crash-before / crash-after boundary** | Expected behavior is documented for a crash immediately before and immediately after the external effect. | Inject one crash before the call and one after remote success but before local completion; verify the recovered workflow reaches the intended single business outcome. |
| 3 | **Retry/replay cannot widen authority** | Tool, resource, tenant and action scope are re-evaluated or durably bounded so replay cannot gain privileges. | Narrow the principal's permission between attempts; verify retry/replay does not retain broader stale authority. |
| 4 | **Missing/stale/failed auth evidence fails closed** | Privileged actions require valid authorization evidence with an explicit freshness rule; missing evidence blocks or escalates. | Expire or remove the authorization decision before resume; expected result is deny/hold, not best-effort execution. |
| 5 | **Human approval is replay-safe** | Approval identity, decision, scope and version are durably bound to the exact privileged action; replay cannot substitute or skip it. | Fork/replay from immediately before approval and alter action parameters; verify the old approval cannot authorize the changed action. |
| 6 | **Workflow/version/policy/eval evidence reconstructs the action** | A reviewer can map workflow ID/version → principal → tool/action → policy decision/version → eval/release verdict → outcome. | Select one completed action and reconstruct why it was allowed without relying on the original operator's memory. |
| 7 | **Held-out wrong-tool + duplicate-action controls** | A versioned eval set includes unseen wrong-tool, wrong-resource and duplicate-action cases not used to tune prompts. | Present a plausible task where the cheaper/easier tool is unauthorized and a second case that repeats a prior action; both must fail safely. |
| 8 | **Rollback / compensation is named** | For each external effect, the owner knows whether rollback means reversal, compensating action, supersession, manual reconciliation, or is impossible. | Simulate a post-action defect; verify the team can identify the affected effect and execute or escalate the declared recovery path. |
| 9 | **Model/cost route cannot change action eligibility** | Model/provider/tier changes may affect generation quality or cost, but privileged-action eligibility remains governed by explicit policy/eval gates. | Force a fallback/cheaper model; verify the route change cannot silently unlock a tool/resource/action that was previously disallowed. |
| 10 | **Execution guarantee vs semantic guarantee is explicit** | The release record states which guarantees come from DBOS durability/transaction semantics and which remain application/tool/policy responsibilities. | Ask a reviewer to point to the owner for external idempotency, authorization freshness and semantic correctness; `UNKNOWN` means the boundary is not yet explicit. |

### Compact release line

`SIDE_EFFECT ___ | CRASH_BOUNDARY ___ | AUTHORITY ___ | APPROVAL ___ | WRONG_TOOL_EVAL ___ | TRACE ___ | COMPENSATION ___ | ROUTE_GUARD ___ | RESULT: GREEN / HOLD`

## SOURCE-BACKED FACTS

- On **July 20, 2026**, DBOS announced high-availability self-hosted Conductor, append-only administrative audit logs, queryable workflow attributes, Java 1.0, and a Vercel AI SDK integration that checkpoints agent actions and resumes from durable checkpoints after a crash.
- On **June 22, 2026**, DBOS said observability integration was one of its most common user requests and released a Prometheus/OpenMetrics-compatible endpoint for workflow, step and executor metrics.
- On **April 7, 2026**, DBOS described production-agent failure modes including malformed SQL, invoking the wrong tool, and misleading summaries; its Databricks integration emphasizes fault tolerance, reproducibility and observability.
- On **February 25 and March 3, 2026**, DBOS described an MCP server for agent-native workflow troubleshooting plus OpenAI Agents SDK and Pydantic AI integrations with recovery, persisted state, human-in-the-loop, multi-agent orchestration, and fork/resume/cancel capabilities.
- DBOS's current About page identifies **Peter Kraft as CTO and co-founder** and **Qian Li as CEO and co-founder**.

## HYPOTHESIS — NOT A FACT

As DBOS expands durable-agent integrations, **some users may spend meaningful engineering time proving that a replayable workflow is also safe at the external business-action boundary**: no duplicated non-transactional effect, no stale/widened authority on retry, replay-safe approval, and reconstructable policy/eval evidence. Public evidence reviewed here does **not** prove that DBOS lacks such guidance, that DBOS users have incidents, that this creates measurable savings, or that DBOS wants an external contribution or commercial relationship.

## ASSUMPTIONS

- At least one workflow performs an external or privileged action whose side effect is not covered by the same transaction as DBOS workflow state.
- Application owners can define an idempotency/reconciliation or compensation strategy for that action.
- Authorization can be represented as explicit evidence with principal, scope, resource/action, decision and freshness/version metadata.
- Human approval, when required, can be bound to an exact action payload or version rather than treated as a generic boolean.
- Held-out synthetic cases can be created without private customer data.

## STRONGEST FALSIFIER

Retire this wedge if DBOS already has a first-party reference pattern that comprehensively tests non-transactional side-effect idempotency/reconciliation, crash-before/crash-after behavior, replay-safe human approval, per-tool/resource authorization freshness, held-out wrong-tool/duplicate-action controls, route-invariant privileged-action eligibility, and reconstructable policy/eval evidence across retry/replay/fork paths **and** DBOS sees no user demand for an additional acceptance layer.

## EVIDENCE LINKS

1. https://www.dbos.dev/blog/new-in-dbos-july-2026
2. https://www.dbos.dev/blog/openmetrics-durable-workflow-observability
3. https://www.dbos.dev/blog/building-durable-agents-dbos-databricks
4. https://www.dbos.dev/blog/mcp-agent-for-durable-workflows
5. https://www.dbos.dev/blog/dbos-new-features-march-2026
6. https://www.dbos.dev/about

## OPTIONAL OPERATOR-REVIEWED OUTREACH NOTE — NO SEND AUTHORITY

I made a one-page DBOS companion gate for the boundary between durable execution and external agent actions: duplicate side effects, crash-before/after behavior, replay-safe authority and approval, held-out wrong-tool cases, and reconstructable policy/eval evidence. It is not a claim that DBOS is missing these controls. If your existing guidance already covers this end to end, that would falsify the idea quickly; if not, the checklist may be useful as a docs/example acceptance surface.

---

**Boundary:** public-source research/preparation only. No claim of DBOS incidents, savings, compliance failures, internal users, deployment outcomes, unmet demand, or current control gaps. No DBOS/customer private data used.