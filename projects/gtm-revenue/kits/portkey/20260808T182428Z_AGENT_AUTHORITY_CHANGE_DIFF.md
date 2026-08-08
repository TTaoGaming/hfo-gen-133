# Agent Authority Change Diff — Principal × Agent × Capability × Budget × Evidence

**Target surface:** Portkey Agent Gateway / MCP Gateway  
**Use:** public-safe review template for one synthetic control-plane change  
**Target-card evidence digest:** `bea6368a9c42ca90b7758286f93148e9887890cb93d21a2cea9b04c06cc7c736`  
**Status:** candidate utility only; not a claim that Portkey lacks this workflow

## Plausible problem

A small agent-control-plane change can alter *who* an agent acts for, *which* agents/tools it can reach, *which* budget/routing constraints apply, and *what* evidence survives review. The useful question is not “do governance controls exist?” Portkey already documents extensive controls. The narrower question is: **can a reviewer see the authority delta, run a few denial tests, and know the rollback revision before approving the change?**

## WHY_THIS_MAY_MATTER

**Source-backed facts**
- Portkey documents Agent Gateway access control scoped per agent/team/user, budget and usage limits, organization-wide policy changes, full agent/MCP traces, and an Agent Registry.
- Portkey documents MCP Registry organization/workspace access control and tool/resource/prompt provisioning; disabled capabilities return errors if directly called.
- Portkey documents assumed, delegated, and chained workload identity and describes fail-fast policy enforcement at the control plane.
- Portkey also documents native config version history, rollback, audit logging, and canary-style testing for AI Gateway configs; its Gateway 2.0 material says the MCP Registry can track/version/manage MCP servers.

**Hypothesis — not a Portkey fact**
- A compact, revision-bound authority diff may still reduce reviewer effort when an agent/MCP policy change spans identity, capability provisioning, budgets/routing, negative authorization tests, traces, and rollback evidence in one approval surface.
- No public evidence establishes Portkey review latency, a missing internal workflow, an incident rate, buyer intent, or savings.

## HOW_TO_USE_IN_2_MINUTES

1. Put the **current** and **proposed** revision IDs in the first row.
2. Mark only rows that changed. Any widened authority must have an owner and reason.
3. Run the six synthetic negative controls below. **Any unexpected ALLOW = HOLD.**
4. Approve only if the rollback revision is known and the evidence bundle is attached.

## Two-minute change card

| Control | BEFORE | AFTER | Reviewer check |
|---|---|---|---|
| Policy/config revision | `gw-policy-v41` | `gw-policy-v42` | Exact immutable revision IDs present? |
| Principal / identity mode | `user:analyst-17` via **delegated** identity | same | Any lost or substituted principal? |
| Agent | `triage-agent` | same | Owner unchanged? |
| Workspace/user scope | `workspace:red-team-sim`; one synthetic user | same | Scope widened? If yes, why? |
| Reachable MCP servers | `case-db-sim` | `case-db-sim`, `ticketing-sim` | **NEW:** `ticketing-sim` justified? |
| Reachable tools/skills | `case.read` | `case.read`, `ticket.create` | **NEW:** write-capable action reviewed? |
| Hidden/disabled capabilities | `ticket.delete` disabled | disabled | Direct call still denied? |
| Budget | `$2/run`, `$20/day` synthetic cap | `$2/run`, `$30/day` | **WIDER:** +$10/day owner + reason recorded? |
| Routing | `model-A → model-B fallback` | same | No route bypassing budget/guardrails? |
| Trace correlation | principal + agent + MCP call share trace ID | same required | Missing hop = HOLD |
| Rollback | `gw-policy-v41` | rollback target remains `gw-policy-v41` | Exact prior revision retrievable? |

### Six held-out negative controls

| Synthetic test | Expected | Evidence to attach |
|---|---|---|
| Cross-tenant/workspace principal requests `ticket.create` | `DENY` | policy decision + principal + revision |
| Hidden `ticket.delete` called directly | `DENY` | blocked capability result |
| Delegated identity is dropped before MCP hop | `DENY/HOLD` | failed identity-chain check |
| Request exceeds per-run/day budget | `DENY` | fail-fast budget decision |
| Request presents stale policy/config revision | `DENY/HOLD` | revision mismatch |
| Agent/MCP hop loses trace correlation | `HOLD` | missing-trace detector result |

### Promotion decision

`PROMOTE` only when: **all six negative controls behave as expected + no unexplained authority widening + exact rollback revision exists + evidence is bound to the proposed revision.**

**Explicit rollback condition:** if any post-change request reaches a capability that the diff marked unchanged/denied, loses propagated principal identity, bypasses the declared budget, or cannot be correlated to the approved revision, revert to `gw-policy-v41` and re-run the card before re-promotion.

## Evidence links

1. Portkey — *Why Every Agent Vulnerability is a Trust Boundary Failure* (2026-06-28): https://portkey.ai/blog/why-every-agent-vulnerability-is-a-trust-boundary-failure/
2. Portkey Docs — *MCP Registry* (last modified 2026-05-07): https://portkey.ai/docs/product/mcp-gateway/mcp-registry
3. Portkey — *Introducing the Agent Gateway* (2026-04-21): https://portkey.ai/blog/agent-gateway/
4. Portkey — *Portkey Raises $15M Series A to Scale the Unified Control Plane for Production AI* (2026-02-19): https://portkey.ai/blog/series-a-funding/
5. Portkey Docs — *Unified LLM API with Automatic Failover & Error Handling* (config versioning / rollback / safe testing): https://portkey.ai/docs/guides/use-cases/enterprise-ready-unified-api
6. Portkey — *The Gateway Grew Up* (MCP Registry version/manage statement): https://portkey.ai/blog/gateway-2-0/

## Assumptions

- This card assumes the reviewer can obtain exact current/proposed revision identifiers and synthetic policy-decision evidence.
- It assumes authority changes can be represented as principal × agent × capability × budget/routing deltas without exposing customer data.
- It does **not** assume Portkey uses OPA/Rego, lacks native regression tooling, or needs an external governance layer.

## Falsifier

**Kill this wedge** if Portkey already exposes a low-overhead native workflow that versions agent/MCP access-policy changes, computes before/after authority diffs, executes negative authorization and budget tests, binds those results to deployment approval, and supports auditable rollback to the exact prior policy/config revision. Public material already shows partial overlap — config versioning/rollback/canary testing and MCP Registry versioning — so the remaining differentiation must be the *joined authority-diff + negative-test + approval-evidence* surface, not generic governance.

## Optional operator-reviewed outreach note — NO SEND

> I noticed Portkey already covers the hard primitives: identity propagation, scoped MCP capabilities, budgets, traces, and versioned gateway configs. I made a one-page authority-change diff that asks a narrower question: before a policy/config promotion, can a reviewer see exactly what became reachable, run six denial checks, and bind the evidence to a rollback revision? If you already have this natively, that itself is useful falsification; if not, the template is yours to adapt.

---

**Boundary:** synthetic/public-safe only. No Portkey account, credentials, production system, customer data, live security testing, deployment, or external send is required to use this artifact.
