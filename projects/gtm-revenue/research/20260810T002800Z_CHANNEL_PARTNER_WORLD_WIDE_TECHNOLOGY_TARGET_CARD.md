# S08 GTM Target Card — World Wide Technology

```yaml
schema_id: hfo.gen133.gtm.target_card.v1
task_id: 6a526109ba348191b5f23ad3172ad568
target: World Wide Technology (WWT)
species: CHANNEL_PARTNER
vertical: enterprise AI infrastructure / AI security / systems integration
route: RELATIONSHIP_ONLY
privacy: PUBLIC_SAFE_SYNTHETIC_ONLY
world_effect_ceiling: T0_PREP_RESEARCH_GIT
verifier: S04_HRIST_STRUCTURAL_PREFLIGHT
next_consumer: S07
consumer_workitem: S07_WWT_AGENT_GATEWAY_POLICY_EVIDENCE_CARD_V1
expiry_utc: 2026-08-14T14:08:00Z
evidence_digest_sha256: fb049c52f4518cb7478e58042250c56ff910f453ee27fbcfe0d00fe589cda2d4
```

## Current signal

WWT is currently selling and validating enterprise agentic-AI infrastructure rather than merely discussing it. Its current Cloud AI Solutions surface says it builds MCP servers, agent gateways, orchestration/A2A infrastructure, policy governance, observability, and ARMOR-aligned security for production agents; it explicitly frames production agent pilots as stalling when tool access, cross-agent tracing, and failure containment become hard. Source verified 2026-08-10: https://www.wwt.com/topic/cloud-ai-solutions/overview

On 2026-07-28, WWT published **When AI Agents Escape Containment: How to Secure the AI Factory**, centered on containing autonomous systems and securing agent identities after an agent escaped a sandbox into production infrastructure. Source: https://www.wwt.com/video/when-ai-agents-escape-containment-how-to-secure-the-ai-factory

On 2026-06-16, WWT launched **Defending at the Speed of AI**, an integrated cybersecurity initiative in its Advanced Technology Center and Cyber Range with Horizon3.ai, Empirical Security, Infoblox, and Cognition. Source: https://www.wwt.com/press-release/world-wide-technology-launches-defending-at-the-speed-of-ai-initiative-with-horizon3ai-empirical-security-infoblox-and-cognition

## Buyer / bridge

Best user/buyer persona: WWT AI Cyber / AI Proving Ground / agentic-infrastructure delivery leadership responsible for translating partner technology into secure client production systems.

Named public bridge: **Istvan Berko — Global Head of AI Cyber & Innovation**, source-backed by WWT's current profile and the 2026-07-28 agent-containment video. This does **not** establish procurement authority, subcontracting authority, accessibility, or interest. Source verified 2026-08-10: https://www.wwt.com/profile/istvan-berko/bio

## Expensive-pain hypothesis

**Hypothesis:** across heterogeneous client agent stacks, WWT delivery teams may repeatedly spend consultant + client-security-review hours proving that an exact MCP/agent-gateway revision preserves principal identity, tool/action policy, traceability, failure containment, cost/latency bounds, and rollback readiness before production acceptance.

Primary value metric: **consultant + client security-review hours per accepted agent-infrastructure revision**. Secondary metric: pilot-to-production acceptance cycle time. No public source found in this pass quantifies either metric for WWT.

**Evidence for:** WWT itself identifies tool governance, cross-agent tracing, misfiring-agent containment, security, observability, and production validation as hard parts of scaling agents; its AI Proving Ground/ATC model exists to validate systems before production. The 2026-07-28 containment material also makes agent identity and blast-radius control explicit.

**Evidence against:** WWT already has ARMOR, an AI Proving Ground, Cyber Range, agent-gateway/policy/observability offerings, and deep vendor integrations. Those capabilities may already provide the exact delivery accelerator hypothesized here. No source found establishes excess review hours, margin leakage, failed agent deployments, control incidents, or demand for outside specialist capacity.

## Two-minute utility gift

**Agent Gateway Release Delta Card — Identity × Tool Authority × Trace × Failure × Cost × Rollback.** For one synthetic before/after agent-infrastructure revision, bind the exact candidate digest to principal/workload identity, allowed/denied MCP tools/actions, policy-decision provenance, trace coverage across handoffs, one injected-failure result, latency/cost envelope, and rollback target. Return `PROMOTE | HOLD | REJECT`, surfacing only widened authority, lost deny edges, missing traces, failed containment, material envelope regressions, or stale rollback evidence.

## Deeper proof artifact

Build a public-safe **Synthetic MCP / Agent-Gateway Promotion Harness** with invented principals, agents, tools, and enterprise workflows; mocked model/tool outputs; an independent OPA/Rego authorization oracle; OpenTelemetry-shaped traces; exact policy/config/fixture digests; and failure injection for wrong principal, privilege widening, stale policy, tool-call loops, cross-agent trace gaps, rate/cost runaway, partial dependency failure, and rollback mismatch. No WWT system, customer data, account, paid model/GPU call, deployment, security claim, compliance claim, or savings claim.

## Route / falsifier / flaw

Route: **RELATIONSHIP_ONLY**. This is a partner-capacity hypothesis, not evidence WWT is buying subcontractor help.

Strongest falsifier: kill the wedge if WWT's existing ARMOR + AI Proving Ground + agent-gateway delivery process already binds each exact agent-infrastructure revision to identity, policy decisions, traces, failure tests, cost/latency envelope, approval, and rollback with low delivery overhead; also kill it if WWT does not admit narrowly scoped external specialist delivery capacity.

Honest flaw: **high redundancy risk**. WWT publicly offers most primitives in this card already. A generic AI-security, OPA/Rego, or observability demo would add little. S07 should consume this only as a narrow, portable **revision-bound agent-gateway evidence contract** that could reduce repeated acceptance work across heterogeneous client stacks.

## Evidence digest preimage

Normalization: UTF-8; LF line endings; exact lines below joined with `\n`; SHA-256 over bytes.

```text
target=World Wide Technology
species=CHANNEL_PARTNER
source=2026-07-28|https://www.wwt.com/video/when-ai-agents-escape-containment-how-to-secure-the-ai-factory|WWT says enterprises need to contain autonomous systems, secure agent identities, and protect AI factories; Istvan Berko is featured as Global Head of AI Cyber.
source=2026-06-16|https://www.wwt.com/press-release/world-wide-technology-launches-defending-at-the-speed-of-ai-initiative-with-horizon3ai-empirical-security-infoblox-and-cognition|WWT launched an integrated AI-era cyber program in its ATC and Cyber Range with multiple partners.
source=2026-08-10-verified|https://www.wwt.com/topic/cloud-ai-solutions/overview|WWT offers agentic AI infrastructure with MCP servers, agent gateways, policy, observability, ARMOR security, and production-scale delivery.
source=2026-08-10-verified|https://www.wwt.com/profile/istvan-berko/bio|Istvan Berko is WWT Global Head of AI Cyber and Innovation.
```
