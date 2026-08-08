---
schema_id: hfo.gen133.gtm_target_card.v1
task_id: 6a526109ba348191b5f23ad3172ad568
seat: S08
valid_time_utc: 2026-08-08T01:26:28Z
species: PRODUCT_PLATFORM
target: DBOS
vertical: durable execution / AI agent workflow orchestration / developer infrastructure
authority_surface: projects/gtm-revenue/
campaign_packet: projects/gtm-revenue/packets/20260807T140800Z_CHATGPT_CLOUD_GTM_DREAM50_HANDOFF.packet.md
evidence_digest_sha256: 7956742d6a6c06f992e0541d64cc585b6fcaa10c699d2306d5b03368ec9ce999
privacy: PUBLIC_SOURCES_ONLY
effect_ceiling: T0_RESEARCH_PREP_ONLY
verifier: S04 Hrist Structural Preflight
next_consumer: S07 GTM Proof-Kit Builder
downstream_work_item: S07_DBOS_DURABLE_AGENT_SIDE_EFFECT_ACCEPTANCE_GATE_V1
expiry_utc: 2026-08-14T14:08:00Z
status: TARGET_CARD_READY
---

# PRODUCT_PLATFORM — DBOS

## Self-probe / queue selection

- expected task id `6a526109ba348191b5f23ad3172ad568`: matched the carrier directive for this wake
- useful surfaces available: GitHub read/write, current public web research, Slack connector
- latest campaign handoff read: `projects/gtm-revenue/packets/20260807T140800Z_CHATGPT_CLOUD_GTM_DREAM50_HANDOFF.packet.md`; unexpired until `2026-08-14T14:08:00Z`
- newest admitted prior S08 card was GuidePoint Security (`CHANNEL_PARTNER`), so rotation selects `PRODUCT_PLATFORM`
- duplicate check: repository search found DBOS in the Dream50 seed and prior technical experiments, but no existing DBOS GTM target card at this evidence digest

## Current product / business signal — SOURCE-BACKED FACTS

1. **2026-07-20:** DBOS shipped high-availability self-hosted Conductor, append-only administrative audit logs, queryable workflow attributes, up to 20x higher durable-stream throughput, Java 1.0, and a Vercel AI SDK integration that checkpoints agent actions into Postgres for recovery. Source: https://www.dbos.dev/blog/new-in-dbos-july-2026
2. **2026-06-22:** DBOS said workflow-observability integration was one of the most common user requests and released a Prometheus/OpenMetrics endpoint for workflows, steps, and executors. Source: https://www.dbos.dev/blog/openmetrics-durable-workflow-observability
3. **2026-04-07:** In its Databricks durable-agent integration, DBOS explicitly described production-agent failures including malformed SQL, invoking the wrong tool, and misleading summaries; the integration focuses on making execution fault-tolerant, reproducible, and observable. Source: https://www.dbos.dev/blog/building-durable-agents-dbos-databricks
4. **2026-02-25 / 2026-03-03:** DBOS added an MCP server for agent-native workflow troubleshooting plus integrations with OpenAI Agents SDK and Pydantic AI, including recovery, human-in-the-loop, multi-agent orchestration, fork/resume/cancel, and persisted execution state. Sources: https://www.dbos.dev/blog/mcp-agent-for-durable-workflows and https://www.dbos.dev/blog/dbos-new-features-march-2026
5. **Current page, read 2026-08-08:** DBOS identifies **Peter Kraft as CTO and co-founder** and **Qian Li as CEO and co-founder**. Source: https://www.dbos.dev/about

## Best buyer / user persona

- **Primary persona:** DBOS product/engineering leader responsible for durable AI workflow adoption, production reliability, and the developer path from prototype to safe production.
- **Secondary user:** platform engineer building agent workflows with external tool side effects, human approvals, and compliance/audit requirements.
- **Named public bridge:** **Peter Kraft — CTO and co-founder.** DBOS identifies him publicly in this role, and he authored DBOS material on durable agents, MCP operations, and observability. This is a public bridge only; no claim is made that he wants an external contribution or owns partnership procurement.

## Expensive pain hypothesis — HYPOTHESIS, not claimed fact

As DBOS expands from workflow durability into production AI-agent integrations, **users may still spend meaningful engineering and incident-response time proving that a durably replayable workflow is also safe at the business-action boundary: external side effects are not duplicated, stale retries do not exceed current authority, privileged tools remain policy-bounded, and the trace can explain why an action was allowed after recovery.**

This is not a claim that DBOS lacks durability or observability. The possible wedge is the acceptance layer between **execution correctness** and **agent action correctness**.

## Measurable value metric

Primary discovery metric: **cycle time / engineer-hours required to certify an agent workflow for production across crash, retry, replay, external-side-effect, authorization, and rollback test cases**.

Secondary observation only: incident/audit reconstruction time for a failed or disputed agent action.

## Evidence FOR the hypothesis

- DBOS itself names wrong-tool invocation and misleading agent output as production failure modes; durable recovery alone does not establish semantic correctness of the chosen action.
- DBOS now exposes workflow attributes, audit logs, OpenMetrics, traces, MCP troubleshooting, forking, and recovery primitives that could carry or verify policy/eval evidence without inventing a second orchestration layer.
- The Vercel AI SDK, OpenAI Agents SDK, Pydantic AI, and Databricks integrations broaden the number of agent/tool combinations whose production-readiness questions DBOS users may encounter.
- DBOS says observability integration was a common user request, which is direct evidence that operational assurance matters to its user base even though the specific acceptance-layer hypothesis remains unvalidated.

## Evidence AGAINST / disconfirming evidence

- DBOS already provides strong primitives: durable checkpoints, transactional/exactly-once patterns for supported data sources, RBAC, audit logs, workflow inspection, OpenMetrics, traces, and recovery/fork controls.
- External side-effect idempotency, tool authorization, and semantic eval gates may be intentionally application/framework concerns rather than DBOS product scope.
- Existing agent-framework integrations may already document sufficient patterns for safe retries and human approval, leaving little incremental value for another acceptance artifact.
- A useful open-source proof artifact would not by itself establish commercial demand, partnership interest, or revenue.

## 2-minute utility gift / proof-kit concept

**`Durable Agent Side-Effect Acceptance Gate — Replay × Authority × Evidence`**

One page for a DBOS user before production:

1. every non-transactional external side effect has an idempotency/reconciliation strategy
2. crash-before / crash-after side-effect tests are explicit
3. retry/replay cannot widen tool or resource authority
4. missing, stale, or failed authorization evidence fails closed for privileged actions
5. human-approval state is durable and cannot be bypassed by replay
6. workflow/version/policy/eval identifiers are attached to reconstructable execution evidence
7. held-out negative controls cover wrong-tool and duplicate-action cases
8. rollback/compensation behavior is named and testable
9. cost/model-route changes cannot silently change privileged-action eligibility
10. acceptance records distinguish DBOS execution guarantees from application-level semantic guarantees

Frame it as a **production-readiness companion to DBOS's existing durability primitives**, not a defect report.

## Deeper proof artifact

**`Synthetic DBOS External-Side-Effect Chaos + Policy Gate`**:

- small DBOS agent workflow using a fake external refund/payment-style API with intentionally non-transactional side effects
- injected crashes immediately before and after the side effect, plus retry/replay/fork cases
- idempotency/reconciliation key and negative duplicate-action tests
- OPA/Rego-style authorization decision with expiry and least-privilege tool/resource scope
- durable human-approval checkpoint for a privileged action
- held-out wrong-tool / stale-policy / missing-evidence cases
- DBOS workflow attributes + trace schema binding workflow/version → policy/eval verdict → action → recovery outcome
- measured engineer-test cycle and incident reconstruction steps

No DBOS customer data, no deployment, and no claim that DBOS uses or should adopt OPA/Rego internally.

## Route

**RELATIONSHIP-ONLY / OPEN-SOURCE-PROOF-FIRST.**

Do not pitch DBOS on basic durability, retries, or observability. The external-fitness test is whether a DBOS product/engineering leader or user finds the side-effect acceptance boundary useful enough to adopt as docs/example/integration guidance. Any partnership, contribution, contract, or product-extension route requires explicit human interest first.

## Strongest falsifier

Retire this wedge if DBOS already has a first-party reference pattern that comprehensively tests external side-effect idempotency/reconciliation, replay-safe human approval, per-tool/resource authorization freshness, held-out wrong-tool controls, and reconstructable policy/eval evidence across crash/retry/fork paths **and** the team sees no user demand for that layer.

## Privacy / effect ceiling

- Public sources only; no private customer, CRM, telemetry, or account data used.
- Research/preparation only; no outreach, contribution submission, account action, purchase, deployment, publication, merge, or negotiation.
- Do not claim DBOS has the hypothesized pain, that the proposed gate improves reliability, or that any commercial demand exists.

## Honest flaw

The strongest evidence proves **DBOS is already unusually strong at durability and observability**, not that it has an unmet assurance gap. The proposed value sits at a boundary DBOS may deliberately leave to application developers. S07 should therefore build only the compact acceptance companion; if it looks redundant with DBOS's existing guidance, kill the wedge rather than expanding the artifact.
