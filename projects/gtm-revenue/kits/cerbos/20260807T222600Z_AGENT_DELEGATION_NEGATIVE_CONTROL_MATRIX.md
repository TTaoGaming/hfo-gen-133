---
schema_id: hfo.gen133.gtm.proof_kit.v0_1
task_id: 6a506f6dc5c08191b95f1707d7f00c2d
carrier: ChatGPT_cloud_S07
work_item_id: S08-PRODUCT_PLATFORM-CERBOS-20260807T212934Z
target: Cerbos
artifact: Agent Delegation Negative-Control Matrix — MCP × A2A × Gateway
source_card:
  commit: 4efdaada8747e4c3335708ceab3ac5b0276232cd
  path: projects/gtm-revenue/research/20260807T212934Z_PRODUCT_PLATFORM_CERBOS_TARGET_CARD.md
  blob_sha: 45f229adb85856c1070bf1b280d720b57a35d906
  binding_digest_sha256: efca83b0cce1fbf342f22533ba27bff5c06ac22c605da5ca374bc09d7ab6e66b
verifier: S04_HRIST_STRUCTURAL_PREFLIGHT
consumer: S03_REDUCER_VERIFICATION_ROUTER_CONSUMERACK_TRACKER
privacy: PUBLIC_SOURCES_ONLY
external_send_authority: NONE
status: CANDIDATE_UNVERIFIED
---

# Agent Delegation Negative-Control Matrix — MCP × A2A × Gateway

**Problem this tests:** when a human delegates work through an agent, then through MCP tools, A2A agents, or an AI gateway, the useful security question is not only “does this policy unit test pass?” It is also: **does authority stay bounded across every hop when context changes, expires, disappears, or is re-routed?**

This is a discussion/test-design aid, **not an audit of Cerbos** and not a claim that Cerbos has these defects.

## WHY_THIS_MAY_MATTER

### Source-backed Cerbos facts
- Cerbos publicly supports runtime authorization across MCP, A2A, Agent Gateway and AI-gateway traffic.
- Its A2A material says inter-agent interactions can be individually authorized using user, source-agent, target-agent and task context.
- Its MCP material describes authorization checks for agent tool/data access and warns about transitive trust and privilege expansion.
- Its AI-gateway material describes fresh policy/context evaluation, delegation-chain context and fail-closed behavior for high-capability agents when the policy layer is unavailable.
- Cerbos Hub already validates and tests policy changes before distribution and provides execution traces.

### Hypothesis, not fact
As these protocol surfaces compose, **multi-hop negative controls** may be a useful complement to isolated policy tests by checking whether delegation invariants remain true across route, context, policy-version and evidence changes. Cerbos may already have equivalent internal suites; public sources do not establish a gap.

## HOW_TO_USE_IN_2_MINUTES

Pick one real agent flow. For each row, mark **COVERED / UNKNOWN / NOT APPLICABLE**. Any `UNKNOWN` on a privileged path becomes a candidate held-out regression test before release.

| # | Negative control | Mutation / setup | Expected safe outcome | Evidence oracle |
|---|---|---|---|---|
| 1 | Agent exceeds human principal | Human cannot perform action; delegated agent role could | **DENY** — delegated authority cannot exceed the principal | Decision binds human + agent + action + resource |
| 2 | Delegation context missing | Remove delegating-user or delegation-chain context | **DENY / FAIL CLOSED** for privileged action | Missing required context is explicit in decision/trace |
| 3 | Delegation expires mid-workflow | Expire delegation before the next privileged step | **RE-EVALUATE; DENY** if no fresh authority exists | New decision timestamp proves fresh authorization |
| 4 | Direct MCP access ≠ delegated access | Tool is allowed directly for principal but not via delegated agent | **DENY** delegated tool call | MCP decision distinguishes acting agent/on-behalf-of principal |
| 5 | A2A capability amplification | Target agent requests capability stronger than source/origin authority | **DENY** — no privilege amplification across hop | Trace shows source, target, task and bounded delegated scope |
| 6 | Gateway route/context staleness | Change model/tool/backend route while reusing stale authorization context | **RE-AUTHORIZE or DENY** before changed privileged path executes | Decision binds current route/tool/resource context |
| 7 | Policy version changes mid-run | Update policy during a long-running workflow | **RE-EVALUATE** at next privileged action; bind exact policy version | Decision record identifies policy/bundle version used |
| 8 | Privileged action lacks decision evidence | Remove or lose required decision/audit evidence | **RELEASE / ACCEPTANCE GATE FAILS** even if runtime action succeeded | Held-out gate requires reconstructable decision evidence |
| 9 | On-behalf-of identity changes | Swap principal or delegation subject between hops | **DENY** unless a new valid delegation is established | End-to-end trace preserves principal continuity |
| 10 | Context enrichment becomes partial/unavailable | Identity/resource context source returns incomplete data | **FAIL CLOSED / DENY** where missing context is authorization-critical | Trace distinguishes complete vs degraded context |

## Minimal release rule

For a privileged multi-hop agent flow, ship only when:

`principal bound` → `delegation bounded` → `each privileged hop re-authorized when context changes` → `policy version identifiable` → `decision evidence reconstructable`.

A green policy-unit-test result alone does not prove this end-to-end chain; conversely, this matrix does not prove Cerbos lacks it.

## Assumptions

1. The safe outcomes above are generic assurance expectations derived from Cerbos' public runtime-authorization semantics, not Cerbos internal acceptance criteria.
2. Some rows may already be covered by Cerbos native policy tests, Hub pipelines, Synapse context enrichment or unpublished integration suites.
3. The matrix intentionally uses Cerbos' YAML/CEL-oriented product model; it does not prescribe Rego/OPA to Cerbos.

## Strongest falsifier

Retire this artifact as redundant if Cerbos already maintains comprehensive end-to-end MCP × A2A × gateway mutation/regression suites covering principal inheritance, stale/missing delegation, policy-version changes, cross-hop privilege amplification, trace completeness, and fail-closed degraded-context behavior — or if Cerbos says this test-design format is not useful.

## Current public evidence

- https://www.cerbos.dev/features-benefits-and-use-cases/ai-gateway-authorization
- https://www.cerbos.dev/ecosystem/agent-gateway
- https://www.cerbos.dev/ecosystem/a2a
- https://www.cerbos.dev/ecosystem/mcp
- https://docs.cerbos.dev/cerbos-hub/index.html
- https://docs.cerbos.dev/cerbos/latest/cli/cerbos.html
- https://www.cerbos.dev/blog/fine-grained-authorization-for-ai-gateways
- https://www.cerbos.dev/about

## Optional operator-reviewed outreach note — NO SEND

> I put together a one-page negative-control matrix for MCP × A2A × gateway delegation. It is not an audit; I used Cerbos' current public authorization semantics as the baseline and focused on cross-hop cases like stale delegation, privilege amplification, policy-version changes, and missing decision evidence. If useful, I'd be glad to share it and hear which cases your existing test suites already cover.

**No outreach has been sent.**
