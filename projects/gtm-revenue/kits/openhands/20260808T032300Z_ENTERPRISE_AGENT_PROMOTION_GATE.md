# OpenHands — Enterprise Agent Promotion Gate

**Candidate work sample | public-safe | no-send**

## Plausible problem

A coding-agent workflow can work in a demo and still be hard to promote into a reusable enterprise capability when Product, Forward-Deployed Engineering, Security, and Engineering must independently re-check reliability, authority, observability, portability, cost/latency, human handoff, and rollback evidence.

That coordination cost is a **hypothesis**, not a claim that OpenHands lacks a promotion process. OpenHands already publicly describes an Agent Control Plane, layered verification, sandboxed execution, governance, observability, budgets, and human review.

## WHY_THIS_MAY_MATTER

OpenHands' current Enterprise Agent Engineer role explicitly spans reusable agent workflows, MCP/tool integration, human-in-the-loop orchestration, auditing/observability/governance, evaluation, reliability, cost, latency, outcomes, and turning field-proven work into durable product capabilities. Its Forward Deployed Engineer role spans proof-of-concept through production deployment and reusable field artifacts. A compact shared promotion record may therefore be useful as a **decision surface** even if OpenHands already has stronger internal machinery.

## HOW_TO_USE_IN_2_MINUTES

Pick one candidate automation or reference agent. Mark each row `GREEN`, `UNKNOWN`, or `RED` using evidence you already have. Do not debate architecture in the meeting: attach the evidence link or name the owner who must produce it. For this sample gate, any `RED` in authority, human approval, sandbox/secret boundary, or rollback means `HOLD`; otherwise unresolved `UNKNOWN`s become named follow-ups.

| # | Promotion check | Fast evidence probe | GREEN means |
|---|---|---|---|
| 1 | **Outcome + held-out set** | Is there one measurable workflow outcome plus a held-out failure set that was not tuned during development? | Outcome metric, test corpus/version, and threshold are recorded. |
| 2 | **Reliability + nondeterminism** | What failures still occur across repeated runs, retries, context variation, or model variation? | Acceptance threshold and known nondeterministic failure modes are explicit. |
| 3 | **Tool / MCP authority** | Can the workflow call a tool, repo, secret, or MCP capability beyond the minimum needed for this use case? | Principal, allowed actions/resources, and least-privilege assumptions are explicit and testable. |
| 4 | **Human approval / escalation** | Which irreversible, externally visible, security-sensitive, or ambiguous actions require a person? | Approval points, approver role, timeout/escalation, and fail-closed behavior are named. |
| 5 | **Reconstructable evidence** | Can an operator reconstruct the workflow version, model route, tool calls, policy/approval state, outcome, and failure from one trace chain? | Required trace fields and retention/evidence links are known. |
| 6 | **Model route × cost × latency** | What quality threshold justifies the selected route, and what happens when cost or latency exceeds the accepted ceiling? | Route/fallback rule and quality, cost, and latency acceptance thresholds are recorded. |
| 7 | **Sandbox / secret / external-call boundary** | What can the runtime read, write, execute, install, or call outside its sandbox? | Secret mounts, filesystem/network boundaries, and external-call assumptions are explicit; unexpected access fails closed. |
| 8 | **Repo / customer portability** | Which assumptions break across repos, auth systems, customer-managed infrastructure, network policy, or connector versions? | Required environment contract and portability checks are recorded. |
| 9 | **Rollback / disable** | If quality, authority, cost, or environment assumptions regress tomorrow, who can stop the workflow and how? | Disable/rollback condition, mechanism, owner, and recovery path are named. |
| 10 | **Shared promotion packet** | Could Product, FDE, Security, and Engineering reach the same `PROMOTE | HOLD` decision without re-deriving the evidence? | One packet links rows 1–9, unresolved risks, owners, and expiry/freshness dates. |

### Three held-out negative probes

Use synthetic/test environments only.

1. **Authority mutation:** remove or narrow one required permission and verify the workflow fails closed instead of substituting a broader credential or tool path.
2. **Stale approval:** expire/revoke a human approval before the privileged step and verify a resumed/retried run cannot reuse it silently.
3. **Route regression:** force a fallback/model change and verify the workflow still satisfies the same privileged-action eligibility and release threshold rather than treating a cheaper/faster route as automatically equivalent.

## Source-backed facts

- **Current role, checked 2026-08-08:** OpenHands' Enterprise Agent Engineer posting says the role builds the automation server and enterprise control plane, reusable reference agents/automations, MCP/tool integrations, human-in-the-loop orchestration, and measurement of reliability, cost, latency, and outcomes; it also works across Product, Enterprise, and Forward-Deployed Engineering to harden successful workflows into durable product capabilities.
- **Current role, checked 2026-08-08:** OpenHands' Forward Deployed Engineer posting owns customer work from proof-of-concept through production deployment, including customer-managed infrastructure, OAuth/agent-identity delegation, MCP connectors, SDLC automations, and reusable artifacts.
- **OpenHands, 2026-05-06:** the Enterprise Agent Control Plane announcement describes centralized policies, repeatable automations, sandboxed execution, observability/auditability, usage and cost attribution, budgets, and optimization across many agents.
- **OpenHands, 2026-06-22:** `The Verification Stack` describes layered agent-level and repo-level verification and routes high-risk PRs to human architect review rather than automatic merge.

## Hypotheses / assumptions

- OpenHands may benefit from a compact cross-functional promotion record when an automation moves from internal/FDE success to a reusable enterprise capability.
- A held-out release-gate format may reduce repeated context reconstruction, but no time saving is claimed or measured here.
- OPA/Rego-style policy-as-code is only an interchangeable example of a deterministic authorization gate; this artifact does **not** claim OpenHands uses or should use OPA/Rego internally.
- The operator's demonstrated overlap is limited to agent release gates/evals, held-out testing, independent verification patterns, policy-as-code concepts, routing/tiering, observability, and bounded workflow automation. This artifact does not assert the operator meets every production-backend requirement of the role.

## Strongest falsifier

Retire or substantially redesign this artifact if OpenHands already has a first-party promotion record that comprehensively binds held-out outcome evidence, reliability/nondeterminism, authority, human approval, observability, route/cost/latency thresholds, sandbox boundaries, portability, rollback, and cross-team signoff. In that case, another checklist is redundant; a useful work sample would need to demonstrate concrete backend/platform execution against a narrower gap instead.

## Evidence links

- Enterprise Agent Engineer: https://jobs.ashbyhq.com/openhands/57564a95-13b6-47b1-b601-dd2353484e47
- Forward Deployed Engineer: https://jobs.ashbyhq.com/openhands/80bfc775-3197-407d-8742-ccb5ddae8709/
- OpenHands Enterprise / Agent Control Plane, 2026-05-06: https://www.openhands.dev/blog/openhands-enterprise-agent-control-plane
- The Verification Stack, 2026-06-22: https://www.openhands.dev/blog/20260506-the-verification-stack

## Optional operator-reviewed application note — NO SEND

I noticed the Enterprise Agent Engineer role sits exactly at the boundary between a workflow that works and one that can be trusted as a reusable enterprise capability. I made a one-page promotion gate around the responsibilities in the posting—held-out outcomes, authority, human approval, traces, model cost/latency, portability, and rollback. It is intentionally a work sample aligned to OpenHands' existing control-plane and verification philosophy, not a claim that the team lacks these controls. If useful, I would attach it to an operator-reviewed application as evidence of how I reason about agent productionization.

---

**Boundary:** public sources only. No OpenHands/customer data, deployment, contribution, application submission, outreach, account action, spend, or external publication was performed or authorized by this artifact.