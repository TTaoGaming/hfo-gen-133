---
schema_id: hfo.gen133.gtm.proof_kit.v1
producer: S07_GTM_PROOF_KIT_BUILDER
task_id: 6a506f6dc5c08191b95f1707d7f00c2d
target: Walmart
artifact_type: governable_agent_paved_road_gap_checklist
valid_time_utc: 2026-08-08T00:22:00Z
expiry_utc: 2026-08-14T23:28:00Z
source_target_card: projects/gtm-revenue/research/20260807T232800Z_ENTERPRISE_BUYER_WALMART_TARGET_CARD.md
source_target_card_blob: 7f0229234a0f54daa9a94905df798826f7c2b8a6
source_evidence_digest_sha256: d77c3b375753d2d133d0a1b4caeaeb8809fbb9c16bf891cb225db4e2e6eae038
verifier: S04
consumer: operator
privacy: PUBLIC_SOURCES_ONLY
external_send_authority: NONE
self_verification: false
---

# Governable Agent “Paved Road” Gap Checklist

**Plausible problem, not a defect claim:** when many teams ship agents that can call tools, move data and act with delegated authority, the hard part is making the safe path mechanically reusable **without turning every change into a bespoke late-stage review**.

This checklist is a two-minute design review aid derived from Walmart’s public engineering principles. It does **not** assert that any item is missing at Walmart.

## WHY_THIS_MAY_MATTER

Walmart publicly describes agentic systems across customer support, merchant workflows, supply chain, associate tooling and developer CI/CD. Walmart Global Tech has also argued that organizational-scale agents need explicit, inspectable, enforceable constraints and traceability, while Walmart security leadership is pushing reusable “paved roads” that replace manual review with embedded controls.

**Hypothesis:** a compact release contract that binds capability, data, authority, action semantics, policy preflight and runtime evidence may reduce duplicated governance work as agent teams scale. No baseline, savings, delay or unmet need is claimed.

## HOW_TO_USE_IN_2_MINUTES

For one agent change, mark each row `GREEN`, `UNKNOWN` or `RED`.

- `GREEN` = the evidence named in column 3 exists and is machine-checkable or reproducible.
- `UNKNOWN` = evidence is absent from the review packet; do not infer safety from implementation intent.
- `RED` = the negative probe in column 4 succeeds when it should fail closed.

If any authority, destructive-action or prohibited-data row is `UNKNOWN/RED`, hold promotion until the missing contract/evidence is supplied.

| # | Paved-road check | GREEN evidence to require | Held-out negative probe |
|---|---|---|---|
| 1 | **Capability contract** | Versioned declaration of allowed agent capabilities, not only prompt text | Add an undeclared tool/capability; preflight must reject it |
| 2 | **Typed boundary** | Machine-checkable input/output/tool schemas with version binding | Remove or mutate a required field; release gate must fail |
| 3 | **Data constraint** | Data class + provenance + allowed destination/tool rules travel with the action | Route a prohibited data class to an otherwise-valid tool; policy must deny |
| 4 | **Identity + delegated authority** | Acting principal, agent identity, purpose, scope and delegation expiry are explicit | Replay the same action with broader scope or expired delegation; deny |
| 5 | **Action semantics** | Approval, retry, idempotency, compensation and destructive-action rules are declared | Attempt destructive/non-reversible action without explicit approval token; deny |
| 6 | **Tool/MCP boundary** | Stable intent/policy fields are separated from provider/tool-specific execution details | Swap a tool implementation while keeping intent constant; authority decision must remain invariant |
| 7 | **Preflight policy gate** | Versioned policy/lint result binds capability + data + authority + action class before promotion | Delete required policy metadata or use stale policy version; fail closed |
| 8 | **Runtime evidence + rollback** | Trace binds agent, tool, policy decision, approval, outcome, retry/compensation and rollback reference | Remove policy/approval trace fields from a synthetic run; evidence completeness gate must fail |

### Minimum release packet

A reviewer should be able to answer these four questions without reading implementation prose:

1. **What may this agent do?** — capability/action contract.
2. **On whose authority and data?** — identity, delegation and data constraints.
3. **What must fail before production?** — held-out negative controls + policy gate.
4. **What proves what happened afterward?** — trace + approval + rollback/compensation evidence.

## SOURCE-BACKED FACTS

- Walmart’s current technology page says agentic capabilities are already used across customer support, merchant tools, supply-chain workflows, associate tools and developer CI/CD, including multi-agent orchestration and increasingly end-to-end actions.
- Walmart Global Tech’s April 20, 2026 article `Designing Governable Agents` says organizational-scale agent constraints should be explicit, inspectable and enforceable, with traceability and machine-readable rules around capability, data, responsibility, identity and authority.
- Walmart Global Tech’s June 10, 2026 security article describes moving from late-stage approvals toward reusable controls and “paved road” platforms, and names reducing manual security-review/service-request burden through automation and infrastructure-as-code as a 2026 priority.

## HYPOTHESIS / ASSUMPTIONS

- **Hypothesis:** a common release contract plus held-out policy tests could help keep governance review cycle time low as agent teams and tool surfaces multiply.
- **Assumption:** at least some agent changes cross team/platform/security boundaries where reusable machine-checkable evidence has value.
- **Not assumed:** that Walmart lacks centralized registries, linting, release gates, policy-as-code, traceability or mature internal controls.
- **Not claimed:** savings, incidents, compliance failures, deployment outcomes, procurement interest or external-specialist demand.

## EVIDENCE LINKS

1. Walmart — Technology / agentic capabilities (current page, rechecked 2026-08-08 UTC):
   https://corporate.walmart.com/about/technology
2. Walmart Global Tech — `Designing Governable Agents`, Jake Mannix, 2026-04-20:
   https://tech.walmart.com/content/walmart-global-tech/en_us/blog/post/designing-governable-agents.html
3. Walmart Global Tech — `Building Security for the Pace of 2026`, 2026-06-10:
   https://tech.walmart.com/content/walmart-global-tech/en_us/blog/post/building-security-for-2026.html

## FALSIFIER

This artifact’s commercial/problem hypothesis materially weakens if stronger evidence or a knowledgeable Walmart platform/security contact shows that these contracts, negative controls, policy gates and evidence bindings are already broadly standardized **and** manual agent-governance review cycle time is not a meaningful constraint—or that outside technical contributions are not a viable path.

## OPTIONAL_OPERATOR_REVIEWED_OUTREACH_NOTE — NO SEND AUTHORITY

> Your public work on governable agents and security “paved roads” overlaps with a release-gate pattern I use for agent systems. I turned those principles into an 8-check gap checklist covering capability, data, delegated authority, action semantics, policy preflight and runtime evidence. It is intentionally not an audit of Walmart—just a compact implementation aid. If useful, I’d be glad to compare where this model matches or diverges from the problems your teams are seeing.

`NO_SEND | NO_APPLICATION | NO_ACCOUNT | NO_TERMS | NO_SPEND | NO_DEPLOY | NO_MERGE | NO_EXTERNAL_PUBLICATION`
