---
schema_id: hfo.gen133.gtm_proof_kit.v1
valid_time_utc: 2026-08-07T20:25:14Z
task_id: 6a506f6dc5c08191b95f1707d7f00c2d
seat: S07
target: Vanta
species: ENTERPRISE_BUYER
kit_type: AGENTIC_GRC_RELEASE_GATE_GAP_MAP
target_card_path: projects/gtm-revenue/research/20260807T193357Z_ENTERPRISE_BUYER_VANTA_TARGET_CARD.md
target_card_commit: cc7432f534f686b141ec82b6e57cfeae5d135219
target_card_blob: f7158e04366b2bbee453e5e0205742854180bac0
target_card_evidence_digest_sha256: 2131d37f75126cc8126557a4b977746165a196402d6e1e7fdc844d25e3156479
privacy: PUBLIC_SOURCES_ONLY
send_status: NO_SEND
verifier: S04_STRUCTURAL_PREFLIGHT_SAME_PROVIDER_NONBINDING
consumer: operator
expiry_utc: 2026-08-14T19:33:57Z
---

# Agentic GRC Release-Gate Gap Map

**For a mature agent platform adding more tool use, sandboxes, artifacts, MCP surfaces, and durable workflow actions.**

## WHY_THIS_MAY_MATTER

Vanta already publishes unusually mature AI-quality practices: traced customer-facing AI calls, versioned eval datasets, calibrated evaluators, systematic experimentation, and explicit process-level evaluation. Vanta also describes a newer class of engineering questions that appears as agent capabilities expand: when to use a sandbox, when routing must be harness-enforced, how ephemeral work stays separate from durable product state, how authorization scopes survive the flow, and whether added latency/cost is justified.

So this is **not** a generic “you need evals” checklist. It is a compact comparison surface for one narrower question:

> **Does each new agent capability bind action authority, evidence, routing, state mutation, traceability, economics, and rollback into one release decision?**

That question is a **hypothesis about where independent comparison may be useful**, not a claim that Vanta lacks these controls.

## HOW_TO_USE_IN_2_MINUTES

Pick one current or planned agent capability. Mark each row **BOUND / PARTIAL / UNKNOWN**. An `UNKNOWN` is simply a question to resolve before release, not a defect finding.

| Gate | Two-minute question | Evidence that would close it |
|---|---|---|
| **1. Action class** | What can the capability **recommend**, **stage**, **write**, **export**, or **change**? | Versioned capability manifest with explicit action classes and risk tiers |
| **2. Held-out evidence** | Which exact negative and success cases must pass for **this capability/version**? | Frozen eval set + thresholds + version/digest + failure examples |
| **3. Authorization** | What user/delegated authority is required for each consequential action? | Runtime principal/context + policy/permission result recorded with the action |
| **4. Routing** | Which routing choices may remain model-decided, and which must be harness-enforced? | Routing table with deterministic overrides and tested fallback behavior |
| **5. State boundary** | What may exist only in ephemeral agent workspace, and what requires durable source-of-truth mutation? | Explicit state-transition contract; no implicit persistence from sandbox artifacts |
| **6. Trace** | Can a reviewer reconstruct the material action from exact model/tool/policy inputs and outputs? | Trace ID binding model/config, tool call, policy result, state change, latency, cost |
| **7. Economics** | What latency/cost ceiling makes the workflow worth running versus a simpler path? | Cost/latency budget per completed workflow + routing fallback when ceiling is exceeded |
| **8. Rollback / hold** | What happens automatically when evidence, authority, routing, or state checks fail? | `ALLOW / HUMAN_REVIEW / HOLD / DENY` outcome plus rollback or safe-stop path |

### Fast interpretation

- **8 BOUND:** strong evidence that the capability has a coherent cross-cutting release contract.
- **1–2 PARTIAL/UNKNOWN:** useful targets for a narrow pre-release review.
- **3+ UNKNOWN:** stop adding framework detail; first make the release contract explicit.

The score itself is not a maturity grade. The useful output is the **specific unresolved question and the evidence needed to close it**.

## Five held-out negative tests

These are framework-agnostic synthetic tests; they do not touch Vanta systems.

1. **Authority downgrade** — user/context loses a required permission after planning but before a consequential tool call. Expected: action is denied or routed to human review; no stale authorization is reused.
2. **Routing mismatch** — model chooses a sandbox/tool path whose input characteristics violate a deterministic routing rule. Expected: harness override wins and the trace records why.
3. **Ephemeral → durable leakage** — sandbox produces an artifact that looks complete but has not passed the product-state write contract. Expected: artifact cannot silently become source-of-truth state.
4. **Partial inspection** — agent samples only part of a large dataset and attempts a conclusion requiring full coverage. Expected: held-out process eval fails or the workflow explicitly reports incomplete coverage.
5. **Economic ceiling breach** — higher-reasoning/tool path exceeds configured latency or cost without material quality gain. Expected: fallback/hold path fires and the release trace preserves the decision.

## Optional decision function

A policy engine is one possible implementation, not a requirement. The decision can remain framework-agnostic:

```text
if authority_invalid -> DENY
else if held_out_evidence_failed -> HOLD
else if durable_state_contract_missing and action_mutates_source_of_truth -> HUMAN_REVIEW
else if latency_or_cost_ceiling_exceeded -> HOLD_OR_FALLBACK
else -> ALLOW
```

OPA/Rego, Cedar, application code, or another policy layer could implement this shape. The value is in making the release decision **explicit and testable**, not in mandating a particular engine.

## Source-backed facts used

1. **Vanta Engineering — July 8, 2026, “Giving the Vanta Agent a computer”**  
   https://www.vanta.com/resources/giving-the-vanta-agent-a-computer  
   Supports: sandboxed workflows; agent-led vs harness-enforced routing; latency/token/operational tradeoffs; explicit ephemeral-vs-durable state separation; authorization/permission scopes; process-level eval expansion.

2. **Vanta Engineering — June 10, 2026, “The Vanta AI Quality Eval Maturity Model”**  
   https://www.vanta.com/resources/vanta-ai-quality-evaluation-maturity-model  
   Supports: observability, versioned curated datasets, calibrated evaluators, systematic experimentation, integrated feedback loops, and standardized eval tooling across teams.

3. **Iccha Sethi, SVP Engineering — June 3, 2026, “Trustcraft: How we build AI products at Vanta”**  
   https://www.vanta.com/resources/how-we-build-ai-products-at-vanta  
   Supports: system-around-the-model framing; every customer-facing AI call traced; offline datasets and calibrated evaluators; MCP/API/agent surfaces; dogfooding and rollback/eval discipline.

4. **Current Vanta product surface — Agentic Trust Platform**  
   https://www.vanta.com/trust-management-platform  
   Supports: current positioning as an Agentic Trust Platform spanning compliance, security program management, risk, and proof.

## Assumptions

- No public source establishes Vanta's internal release contract for every agent capability.
- No public baseline establishes duplicated engineering/GRC-SME hours, regression escape rate, incident cost, or economic value of an external assurance layer.
- Vanta may already have a unified internal gate equivalent to this map.
- A real discovery conversation is required before treating this as a commercial pain rather than a useful peer benchmark.

## Falsifier

**Retire the commercial wedge** if Vanta already has a unified, low-burden release gate that binds action authority, held-out evidence, routing decisions, durable-state mutations, traceability, latency/cost ceilings, and rollback across agent capabilities—or if the relevant engineering leader says this cross-cutting problem is not material.

## Optional operator-reviewed outreach note — NOT SENT

> Your Trustcraft posts already show a much stronger eval/trace discipline than most teams I’ve studied. I condensed one narrower question from the sandbox write-up—how action authority, process evals, routing, durable state, economics, and rollback bind into a single release decision—into an 8-row comparison map. No pitch; happy to share it if the outside view is useful.

## Truth boundary

This artifact does **not** claim that Vanta has missing controls, security flaws, weak evals, excessive costs, incidents, audit failures, or an unmet consulting need. It is an independent comparison checklist derived from Vanta's own public engineering material plus a clearly labeled hypothesis.