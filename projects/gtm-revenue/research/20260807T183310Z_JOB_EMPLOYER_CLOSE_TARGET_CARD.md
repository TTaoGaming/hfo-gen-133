---
schema_id: hfo.gen133.gtm_target_card.v0_1
research_id: S08-JOB_EMPLOYER-CLOSE-20260807T183310Z
task_id: 6a526109ba348191b5f23ad3172ad568
species: JOB_EMPLOYER
target: Close
vertical: B2B SaaS / CRM / production AI agents
valid_time_utc: 2026-08-07T18:33:10Z
expiry_utc: 2026-08-14T18:33:10Z
evidence_digest_sha256: a1a2c0dfeff699d218c67695b478b155ec7e667752e1b9aa38ef110e57c1ef74
privacy: PUBLIC_SOURCES_ONLY
world_effect_ceiling: T0_RESEARCH_PREP_NO_SEND
verifier: S04 Hrist Structural Preflight
next_consumer: S07 GTM Proof-Kit Builder
status: NEW_TARGET_CARD
---

# Close — JOB_EMPLOYER target card

## Current signal

**APPLY-NOW + RELATIONSHIP.** On 2026-08-07, Close's official Ashby board exposes a live **Senior Backend Engineer – Agents** opening for U.S.-remote candidates at **$140K–$210K**. The listing says Close shipped its first agent, Chloe, in 2026 and that the Agents team owns the agent core, **eval and observability layer, MCP surface, and orchestration** across Voice Agents, LLM chat, and Custom Agents. It also says these systems are running in production in front of roughly 11,000 paying customers and that the role is open across multiple engineering levels.

Primary hiring source, verified 2026-08-07:
- https://jobs.ashbyhq.com/Close/29f5c695-8282-4407-ac09-2b61b9f2fc1e

Current product/business signals:
- 2026-06-03: Close launched Chloe broadly; Close reports a beta across 306 businesses, 818,787 calls, 111,915 reached prospects/customers, and 6,424 hours of conversations. Source: https://close.com/blog/introducing-chloe
- 2026-07-20: Close added MCP access for meeting transcripts, continuing expansion of its external-agent surface. Source: https://close.com/changelog
- updated 2026-07-14: Close's Claude/MCP integration describes actionable CRM operations with **granular permissioning** for what the external agent may do. Source: https://close.com/blog/close-claude-crm-integration

## Best persona

Primary: **Engineering Manager / Staff+ engineer on the Agents team**.

Secondary: AI platform / agent infrastructure engineering leader responsible for evals, MCP/tool execution, orchestration, reliability, or cost.

**Named public bridge:** `NONE_SELECTED_IN_BOUNDED_PASS`. The bounded primary-source pass did not identify a current engineering-team lead with enough source confidence to name as a bridge. Do not substitute a founder or marketing contact merely because they are public.

## Expensive pain hypothesis — explicitly a hypothesis

**Hypothesis:** as Close expands Chloe, Custom Agents, Voice Agents, and MCP-mediated external actions, the expensive engineering problem is likely not “can an agent act?” but **how to keep agent releases measurably reliable, permission-bounded, observable, and cost-aware as action surfaces and model choices multiply**.

Potential value metrics if discovery confirms the problem:
- agent regression / task-failure rate;
- engineering and support hours per incident or failed release;
- mean time to detect / diagnose agent failures;
- release cycle time and rollback frequency;
- unauthorized / incorrectly scoped tool-action rate;
- model cost per successful task or qualified outcome;
- human-review minutes per automated workflow;
- customer-impacting error or escalation rate.

This card **does not claim** Close currently performs poorly on any of these metrics.

## Evidence supporting the hypothesis

1. The live hiring page explicitly names **evals, observability, MCP, orchestration, retrieval, tool design, and frontier-model failure modes** as core engineering concerns.
2. Close is simultaneously operating Voice Agents, LLM chat, and Custom Agents, so the number of action and failure surfaces is materially broader than a single chatbot.
3. Chloe performs consequential CRM actions: calls leads, qualifies, books meetings, follows up, enriches records, and updates CRM state.
4. Close's MCP integration allows external conversational agents to take CRM actions, and Close explicitly advertises granular permissioning.
5. Close's reported beta volume indicates that quality or cost deltas can compound across substantial interaction volume.

## Evidence against / reasons the hypothesis may be wrong

1. Close already states that the Agents team owns an eval and observability layer; this may be a core internal competency rather than a gap an outside artifact helps.
2. Close already exposes granular permissioning for MCP operations, so a generic “you need permissions” pitch would be redundant and low value.
3. The hiring role asks for engineers who have shipped meaningful production agentic features; the operator must not imply equivalent external production/customer scale unless evidence supports that claim.
4. Close may optimize primarily for product velocity and customer outcomes rather than formal policy-as-code. An OPA/Rego-heavy artifact could be overengineered if it does not map to their actual stack or failure modes.

## Two-minute utility gift

### `AI Sales Agent Release Gate — Action × Eval × Cost Scorecard`

A one-page recipient-useful scorecard with five rows:

1. **Action correctness** — did the agent choose and execute the intended CRM action?
2. **Authority** — was the action allowed for this actor/customer/workflow and was escalation required?
3. **Held-out quality** — did the release clear negative cases for wrong-contact, stale-context, unsupported-action, and tool-failure scenarios?
4. **Traceability / rollback** — can an engineer reconstruct model → context → tool → result → human escalation and safely roll back?
5. **Cost / latency** — does the task use the cheapest model/route that clears the quality threshold without violating latency targets?

Use in about two minutes: mark each row `GREEN / UNKNOWN / RED`, choose the highest-cost UNKNOWN, and test that one before broadening agent authority.

This is a diagnostic gift, **not an audit finding**.

## Deeper proof artifact for S07

Build a small synthetic **sales-agent release-gate pack** containing:

- held-out tests for wrong lead/contact, stale deal context, tool timeout, unsupported update, and repeated-action/idempotency failure;
- an agent-action authority matrix for read / enrich / update / call / message / book actions;
- a replaceable policy example showing deny-safe behavior for high-impact or ambiguous actions (OPA/Rego is acceptable as a demonstrator, not a claim about Close's stack);
- trace fields needed to replay one decision and tool call;
- a model-tier routing table with quality threshold, latency ceiling, and cost-per-successful-task metric;
- rollout / rollback gate with explicit failure threshold.

The artifact should be framework-neutral enough to demonstrate the engineering pattern without telling Close to replace its existing eval or permissions systems.

## Route

`APPLY_NOW + RELATIONSHIP`

1. Application route: current role is live and directly overlaps evals / observability / MCP / orchestration.
2. Relationship route: useful even if the application is rejected; target the Agents engineering surface with a compact technical artifact rather than generic resume outreach.
3. No claim that the artifact identifies a defect at Close. Position it as a **worked engineering specimen inspired by the public problem shape in the role**.

## Strongest falsifier

**RETIRE or radically revise this angle** if a source-backed engineering conversation shows that Close's current bottleneck is not agent release reliability / permission / cost evidence but a different constraint (for example voice infrastructure, raw latency, retrieval quality, product UX, or customer adoption), or if their current eval/authorization platform already makes this artifact trivial and non-useful.

A job rejection alone does **not** falsify the pain hypothesis; a technical or discovery conversation about the actual bottleneck is stronger evidence.

## Claim / privacy / authority ceiling

- Public-source facts only.
- Pain remains a hypothesis until direct discovery confirms it.
- Do not claim Close has security, reliability, cost, or permission failures.
- Do not claim the operator has shipped customer-scale agent systems unless independently evidenced in the application truth packet.
- No outreach, application submission, account creation, terms acceptance, paid call, deployment, publication, purchase, or negotiation is authorized by this card.

## Honest flaw

The hiring page is unusually well aligned with the operator's demonstrated internal toolbox, which creates **fit-bias risk**: it is easy to mistake vocabulary overlap for hiring fit. Close explicitly asks for meaningful production agentic experience; without a source-backed production/customer outcome, the strongest positioning is the concrete engineering proof artifact plus honest evidence ceiling, not inflated seniority or scale claims.