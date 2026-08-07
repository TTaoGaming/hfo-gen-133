---
schema_id: hfo.gen133.gtm.target_card.v0_1
task_id: 6a526109ba348191b5f23ad3172ad568
carrier: ChatGPT_cloud_S08
wip: 1
valid_time_utc: 2026-08-07T21:29:34Z
source_packet:
  path: projects/gtm-revenue/packets/20260807T140800Z_CHATGPT_CLOUD_GTM_DREAM50_HANDOFF.packet.md
  blob_sha: 731a1eafa9b0f81d11088e8fcb8a60312f53b910
species: PRODUCT_PLATFORM
target: Cerbos
vertical: enterprise_authorization_and_AI_agent_security
route: RELATIONSHIP_ONLY_PRODUCT_ECOSYSTEM
status: RESEARCHED_READY_FOR_S07
next_consumer: S07
after_s07_verifier: S04
privacy: PUBLIC_SOURCES_ONLY
effect_ceiling: T0_RESEARCH_GIT_SLACK_POINTER_ONLY
external_send_authority: NONE
expiry_utc: 2026-08-14T21:29:34Z
---

# PRODUCT_PLATFORM target card — Cerbos

## Why this target now

Cerbos is explicitly positioning its authorization platform for AI agents, MCP servers, AI gateways, non-human identities, and agent-to-agent delegation. Its current product pages describe runtime authorization for model calls, tool invocation, MCP methods, and A2A delegation, with policy decisions and audit trails attached to each request. This is not a speculative adjacency: Cerbos is actively building the authorization layer around the same agent-action boundary where the operator's policy-as-code, held-out testing, false-green detection, and multi-agent work are most relevant.

## Current product/business signal

1. **AI gateway authorization is a current product surface.** Cerbos says every model call, tool invocation, MCP method, and agent-to-agent delegation can be governed by one authorization layer, with fail-closed behavior for high-capability agents when the policy layer is unavailable. Source retrieved 2026-08-07: https://www.cerbos.dev/features-benefits-and-use-cases/ai-gateway-authorization
2. **Cerbos has first-class Agent Gateway integration.** The integration covers MCP, A2A, and LLM traffic through `ext_authz`, using user identity, agent roles, tool type, and request context; every authorization decision is logged. Source retrieved 2026-08-07: https://www.cerbos.dev/ecosystem/agent-gateway
3. **Cerbos has first-class A2A authorization.** It documents controlling which agents can communicate, what capabilities they can share, and which task types can be delegated, with runtime context and audit. Source retrieved 2026-08-07: https://www.cerbos.dev/ecosystem/a2a
4. **Cerbos has first-class MCP authorization.** It documents policy-driven control over MCP tools/resources and least-privilege access on every tool call. Source retrieved 2026-08-07: https://www.cerbos.dev/ecosystem/mcp
5. **The company is already serious about policy testing.** Cerbos Hub automatically validates, tests, signs, distributes, and traces policy changes; policy tests are part of the managed CI/CD pipeline. Source retrieved 2026-08-07: https://docs.cerbos.dev/cerbos-hub/index.html and https://docs.cerbos.dev/cerbos/latest/policies/compile.html
6. **Cerbos' CPO is publicly working at the AI-agent/Zero-Trust boundary.** Alex Olivier's January 9, 2026 Cerbos article discusses agent identities, MCP, delegation gaps, on-behalf-of tokens, embedded PDPs, and OAuth token exchange. Source published 2026-01-09: https://www.cerbos.dev/blog/mcp-and-zero-trust-securing-ai-agents-with-identity-and-policy
7. **Cerbos published an AI-gateway authorization guide on May 26, 2026**, explicitly arguing that gateways solve routing but not fine-grained authorization. Source published 2026-05-26: https://www.cerbos.dev/blog/fine-grained-authorization-for-ai-gateways

## Named public bridge

**Alex Olivier — CPO and co-founder.** Cerbos' current About page names Alex as CPO/co-founder; it also says he co-chairs the OpenID AuthZEN working group. This makes him a source-backed product/community bridge for an authorization-focused proof artifact. This does **not** imply he is an external-services buyer or that unsolicited outreach will be welcomed.

Source retrieved 2026-08-07: https://www.cerbos.dev/about

## Best buyer/user persona

Primary: **CPO / Product Engineering / Developer Relations / Solutions Engineering / ecosystem-integrations lead** responsible for AI authorization adoption.

Secondary economic user: enterprise architects and AI-security/platform teams evaluating Cerbos for MCP/A2A/agent-gateway deployments.

## Expensive pain hypothesis — explicitly a hypothesis

> **Hypothesis:** as Cerbos expands across MCP, A2A, AI gateways, non-human identities, and multiple enterprise deployment patterns, a recurring costly edge may be proving that *delegation semantics stay safe across protocol combinations and policy changes*, not merely that an isolated policy unit test passes.

Possible costly failure classes include: user authority silently broadening during agent-to-agent delegation; stale or missing delegation context; MCP tool privilege exceeding the human principal; routing through a different gateway path that changes available context; expired evidence still authorizing a capability; or an allow/deny rule passing unit tests while a multi-step agent workflow violates the intended end-to-end authority boundary.

This is **not** evidence that Cerbos currently suffers these failures. It is a target-specific extension hypothesis derived from the company's public multi-protocol agent-authorization surface.

## Measurable value metric

If discovery validates the hypothesis, measure one or more of:

- engineering hours to add/test a new agent protocol or integration;
- time from integration prototype to production-authorization acceptance;
- number of authorization/delegation regressions caught before release;
- security-review or audit hours needed to reconstruct delegation chains;
- support/solutions-engineering hours spent reproducing complex multi-hop authorization failures;
- enterprise PoC completion time for MCP/A2A/AI-gateway authorization.

No baseline or savings value is claimed here.

## Evidence supporting the hypothesis

- Cerbos now spans several distinct agent authorization surfaces — MCP, A2A, Agent Gateway, LLM traffic and non-human identities — increasing the number of delegation/context combinations that must remain semantically consistent.
- Cerbos explicitly emphasizes full delegation context, per-request runtime authorization, auditability, fail-closed behavior, and the human behind the agent, which means correctness across chained actions is product-critical.
- Cerbos' own January 2026 discussion identifies delegation standards and agent identity as active gaps in the broader ecosystem.

## Evidence against / reasons this may be a bad target

- Cerbos already has a serious policy testing system: Hub validates and runs policy tests before rollout, with execution traces and coordinated deployment. A generic "test your policies" artifact would be low-value noise.
- Cerbos already ships dedicated MCP, A2A, Agent Gateway and AI-security material. A basic AI-agent authorization checklist would mostly repeat their own product messaging.
- Their policy model uses YAML/CEL rather than Rego; an OPA/Rego-centric artifact would be poorly shaped for this target unless used only as a comparative/reference control.
- Cerbos may already maintain internal end-to-end delegation suites that are not public. If so, the proposed wedge is redundant.

## 2-minute utility gift for S07

**"Agent Delegation Negative-Control Matrix — MCP × A2A × Gateway"**

A one-page recipient-useful matrix with 8–10 high-value negative controls, for example:

| Negative control | Expected safe result |
|---|---|
| user lacks permission but delegated agent has broad role | DENY — agent cannot exceed principal |
| delegation context missing | DENY / fail closed |
| delegation expired mid-workflow | subsequent privileged action denied |
| MCP tool allowed directly but not through delegated agent | delegated call denied |
| A2A target agent requests a stronger capability than source possessed | DENY |
| gateway changes model/tool route but policy context is unchanged/stale | deny or require fresh decision |
| policy version changes during long workflow | decision trace binds exact version; privileged continuation re-evaluated |
| audit/decision evidence missing for a privileged action | release/acceptance gate fails |

The matrix must be framed as a **discussion/test-design aid**, not an audit of Cerbos.

## Deeper proof artifact for later consumption

A synthetic, public-safe **Cerbos Agent Delegation Assurance Pack**:

1. small Cerbos YAML policy set for a human → agent → MCP tool / A2A delegation chain;
2. native Cerbos policy tests for expected allow/deny behavior;
3. additional mutation/negative-control cases that deliberately remove, stale, or broaden delegation context;
4. a compact end-to-end trace contract binding principal, source agent, target agent/tool, action, policy version, decision, evidence timestamp, and rollback/deny condition;
5. optional comparison note showing how an OPA/Rego implementation would express the same invariant, without implying Cerbos should use Rego.

No deployment, account creation, external API call, or Cerbos trial is required to prepare the public-safe specification/demo skeleton.

## Route

**RELATIONSHIP_ONLY_PRODUCT_ECOSYSTEM.** Do not treat this as a job opening or customer defect report. The strongest possible path is product/community/ecosystem dialogue: a useful delegation-test artifact, open-source-compatible example, integration discussion, or evidence of specialist authorization/agent-assurance capability.

## Strongest falsifier

Retire or substantially revise this target if current Cerbos public/private discovery shows it already has comprehensive **end-to-end MCP × A2A × gateway delegation mutation/regression suites** covering principal inheritance, stale/missing delegation, policy-version changes, cross-hop privilege escalation, trace completeness, and fail-closed workflow behavior — or if the team explicitly does not value outside ecosystem examples/assurance contributions.

## S07 build instruction

Build only the **2-minute Agent Delegation Negative-Control Matrix** first. Do not build the deeper pack until the matrix survives S04 structural review and an operator/consumer explicitly promotes it. The first artifact should demonstrate that we understood Cerbos' existing strengths rather than teaching them generic authorization basics.

## Honest flaw

This card is grounded in current public Cerbos product/docs material, not discovery with Cerbos employees or customers. The proposed expensive pain is therefore a **product-extension hypothesis**, not observed demand. Cerbos already has mature policy testing, so the incremental value of mutation-style multi-hop delegation assurance remains unproven until a human at Cerbos or a Cerbos user confirms the gap.
