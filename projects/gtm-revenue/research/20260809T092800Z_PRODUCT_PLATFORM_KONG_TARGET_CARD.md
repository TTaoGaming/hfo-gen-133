# S08 TARGET CARD — Kong

```yaml
schema_id: hfo.gen133.gtm_target_card.v1
task_id: 6a526109ba348191b5f23ad3172ad568
carrier: S08
target: Kong Inc.
species: PRODUCT_PLATFORM
vertical: AI connectivity / AI gateway / agent identity and MCP governance
valid_time_utc: 2026-08-09T09:28:00Z
evidence_digest_sha256: 8ab7c0405bf83c19f9a4bcbe3ff3f565ae4c6096190fe8e22e43e006120d0975
route: RELATIONSHIP_ONLY
privacy: PUBLIC_SAFE_SYNTHETIC_ONLY
world_effect_ceiling: T0_PREP_RESEARCH_GIT
verifier: S04
next_consumer: S07
downstream_workitem: S07_KONG_AGENTIC_AUTHORITY_REGRESSION_CARD_V1
expiry_utc: 2026-08-14T14:08:00Z
```

## Current signal

Kong is actively expanding its agentic-AI control surface. Its official **July 16, 2026** AI Gateway 2.0 announcement describes a dedicated runtime and control plane where models, MCP servers, and agents become first-class entities; it also introduces `kongctl` migration/configuration and says the independent 2.x line is intended to move faster, with 2.1 already planned for August. That announcement called 2.0 a **private beta** and planned GA for the end of July. No newer official GA announcement was found in this pass, so this card does **not** claim that 2.0 is GA.

On **July 14, 2026**, Kong announced Identity Principals GA: a centralized identity model for machines, agents, processes, and humans whose metadata can flow into runtime policy decisions, lifecycle/rotation, audit, and revocation. On **July 3, 2026**, Kong separately described enterprise-managed MCP authorization intended to replace fragmented per-user/per-server authorization with centrally governed policy and audit context. Current AI Gateway documentation describes governance across LLM, MCP, and A2A traffic plus dynamic routing for cost, latency, and availability. Kong's official Agentic AI page, in an **August 6, 2026** article snippet, says it is seeing hundreds of customers proxying LLM, MCP, and agent traffic through Kong AI Gateway; this is a company-authored business signal, not independently verified customer-count evidence.

Sources:
- 2026-08-06 — https://konghq.com/blog/tag/agentic-ai
- 2026-07-16 — https://konghq.com/blog/product-releases/kong-ai-gateway-2-0-agentic-ai
- 2026-07-14 — https://konghq.com/blog/product-releases/kong-identity-principals-govern-every-api-event-and-application-identity
- 2026-07-03 — https://konghq.com/blog/product-releases/enterprise-grade-mcp-access-control
- verified current 2026-08-09 — https://developer.konghq.com/ai-gateway/

## Persona / bridge

**Best buyer/user persona:** Kong AI Gateway / agentic-identity product or platform engineering leadership responsible for safe rollout of LLM, MCP, A2A, principal, and policy-control changes; secondary users are security-platform and developer-platform teams operating those controls.

**Named public bridge:** **Andrew Jessup, Principal Product Manager, Agentic Identity, Kong**, source-backed on Kong's July 14 Identity Principals and July 3 MCP-access-control announcements. No procurement, partnership, hiring, or outreach authority is inferred.

## Expensive-pain hypothesis

**Hypothesis, not a claimed Kong/customer problem:** as Kong accelerates AI Gateway 2.x while adding centralized machine/agent principals and MCP/A2A controls, product teams or customers may spend material engineering + security-review time proving that an exact configuration/policy revision does not unintentionally widen an agent's effective authority, remove a deny edge, mis-bind principal metadata, alter MCP/A2A permissions, or create an unacceptable model-routing/cost regression before promotion.

**Measurable value metric — cycle time:** median engineer + security-review hours per accepted AI Gateway / agentic policy-config revision. Secondary metric: candidate-config → approved production-promotion elapsed time.

### Evidence for
- AI Gateway 2.0 makes models, MCP servers, and agents first-class configuration entities and moves them onto a faster independent release cadence.
- Kong Identity Principals puts machine/agent identity metadata directly into runtime policy decisions, increasing the importance of verifying effective authority after policy/config changes.
- Kong's MCP material explicitly frames centralized authorization and audit as enterprise requirements.
- Kong's current AI Gateway surface spans LLM, MCP, A2A, dynamic routing, cost, latency, and availability, creating a multi-dimensional change surface where a compact regression contract could be useful.

### Evidence against
- Kong already provides centralized identity, runtime policy, audit/observability, declarative configuration/GitOps tooling, migration tooling, access controls, and an active Gateway changelog; a separate pre-promotion artifact may be redundant.
- Customers may intentionally own regression/eval checks in their existing CI/security pipelines rather than expect Kong to provide them.
- No cited source establishes excess review hours, authorization incidents, missed releases, customer complaints, or willingness to buy an external release-assurance layer.

## S07 consumption contract

**2-minute utility gift:** `Agentic Authority Regression Card — Principal × MCP Tool × Agent × Model × Deny/Allow × Trace`

Given one tiny synthetic before/after configuration fixture plus a held-out action matrix, return `PROMOTE | HOLD | REJECT` and show only the material deltas: newly allowed actions/tools, lost deny edges, principal-metadata drift, changed MCP/A2A access, model/routing cost-envelope change, missing trace/audit evidence, and rollback target.

**Deeper proof artifact:** a public-safe offline `Kong Agentic Authority Diff Harness` using fake principals, agents, MCP servers/tools, A2A edges, and model routes. Compare before/after configs against an independent OPA/Rego-style expected-authorization oracle; include negative controls for wrong principal, privilege widening, stale metadata, denied-tool access, routing/cost regression, missing audit evidence, and rollback mismatch. Use only fixtures/mock outputs: no Konnect account, live gateway, customer data, deployment, or production claims.

**Route:** `RELATIONSHIP_ONLY`. The useful first move is a source-shaped proof artifact, not a sales claim or unsolicited outreach from this lane.

## Falsifier / ceilings

**Strongest falsifier:** kill the wedge if Kong already provides—or deliberately expects customer CI/security tooling to provide—a low-overhead pre-deploy simulator/regression mechanism that binds the exact AI Gateway/config revision to principal identity, MCP/A2A authorization matrices, deny/allow negative controls, routing/cost expectations, audit evidence, and rollback. Also kill it if the current 2.x native configuration/Identity workflow makes an independent authority-diff artifact operationally redundant.

**Privacy/effect ceiling:** public sources and synthetic data only; research + Git card + internal Slack pointer only. No account creation, terms acceptance, outreach, application, email/DM, purchase, paid call, deployment, publication, merge, private-data use, demand invention, or negotiation.

**Honest flaw:** Kong already owns most of the relevant primitives, so technical adjacency is high while commercial whitespace may be low. The product-status signal is also imperfect: the July 16 post called AI Gateway 2.0 private beta and forecast end-of-July GA, but this pass found no later official GA announcement. S07 should stop if its two-minute card merely repackages Kong's native GitOps, identity, or policy controls rather than exposing a real revision-bound regression seam.
