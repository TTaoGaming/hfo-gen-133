# 1Password Agent Authority Drift Gate

**Plausible problem:** an agent integration can still “work” after a revision while effective authority changes: a different principal is trusted, credential scope widens, approval becomes optional, session lifetime changes, or audit/revocation evidence weakens.

> **Not a finding about 1Password.** Public sources show active work on agent identity, credential brokering, scoped delegated access, and auditability. They do not show a control failure, incident, slow release process, or unmet need.

## WHY_THIS_MAY_MATTER

1Password now supports several authority shapes: per-task human-approved browser access, workload-identity credential brokering, and a published delegated-local-agent architecture. A narrow release question follows:

**Did this exact integration revision widen or ambiguously change who/what can use which credential, for what action, under whose authority, for how long, and with what evidence?**

Hypothesis only: a compact revision-level authority diff may reduce engineering/security-review effort per accepted integration revision. No public source establishes current review hours, defect rates, or savings.

## HOW_TO_USE_IN_2_MINUTES

Fill one synthetic baseline and candidate. Any unexplained widening, missing evidence, or weaker revocation is `HOLD`; clearly unauthorized widening is `REJECT`.

| Gate | Baseline → Candidate | Pass condition |
|---|---|---|
| Principal | human/workload identity → ___ | intended principal remains bound |
| Agent | runtime/agent identity → ___ | intended runtime remains bound |
| Credential | credential/token class → ___ | no broader class without approval |
| Scope | audience + action + TTL/session → ___ | no unexplained widening |
| Evidence | approval/attestation + audit fields → ___ | attribution remains provable |
| Revoke | cancel/expiry/revocation → ___ | stale/revoked authority fails closed |

**Verdict:** `PROMOTE | HOLD | REJECT`  
**Baseline:** `sha256:____` · **Candidate:** `sha256:____` · **Policy/fixture:** `sha256:____` · **Rollback:** `____`

### Fast decision rule

`PROMOTE` only if every changed authority edge is intentional, attributable, bounded, negative-tested, and reversible.

`HOLD` if principal binding, scope, approval/attestation, provenance, expiry, or revocation cannot be proven.

`REJECT` if a wrong principal, wrong audience, stale session, missing approval/attestation, or revoked credential still obtains authority.

## Deterministic policy starter

```rego
package agent_authority
default allow := false

allow if {
  input.principal == data.expected.principal
  input.agent == data.expected.agent
  input.credential == data.expected.credential
  input.audience == data.expected.audience
  input.action in data.expected.actions
  input.approval_or_attestation == true
  input.session_active == true
  input.revoked == false
  input.audit_principal_present == true
  input.audit_agent_present == true
}
```

This does **not** model 1Password internals or claim 1Password uses OPA/Rego. It is an offline synthetic acceptance oracle.

## Held-out negative controls

Fail closed on: wrong principal; wrong agent/runtime; widened audience; added write/admin action; missing approval/attestation; replay after expiry; revoked/cancelled authority reuse; missing principal/agent audit attribution.

## Source-backed facts

- **2026-03-17:** Unified Access Pro GA was announced for discovering, securing, continuously authorizing, and auditing human, machine, and AI-agent access; scoped runtime credentials were described as a later-2026 expansion.
- **2026-06-15:** Credential Broker private beta was announced; its initial flow verifies GitHub Actions workload identity before delivering an approved credential and records delivery context.
- **2026-07-16:** 1Password for Claude launched with per-task user-approved credential access, session-scoped approved items, Agentic Mode, and secrets kept outside model context; 1Password says the framework is intended to extend to other browser agents/platforms.
- **2026-07-21:** 1Password published a delegated local-agent architecture separating human and agent identity, recommending scope attenuation and short-lived authority, with policy enforcement outside model reasoning.

## Evidence links

https://1password.com/press/2026/mar/1password-unified-access  
https://1password.com/press/2026/june/credential-broker  
https://1password.com/press/2026/july/1password-for-claude  
https://1password.com/blog/ai-agent-identity-delegated-local

## Assumptions

The wedge exists only if heterogeneous integrations create meaningful authority drift and existing first-party tests do not already bind exact revisions to principal, scope, approval/attestation, provenance, expiry, revocation, negative controls, and rollback. No savings, incidents, compliance failures, production defects, or deployment outcomes are asserted.

## Falsifier

**Kill this wedge** if 1Password already has a low-overhead first-party mechanism that provides that exact revision-level authority evidence across supported agent platforms, or if downstream action authorization is intentionally outside its integration-acceptance responsibility.

## Optional operator-reviewed outreach note — NO SEND

> Your public agent-security work spans per-task delegated browser access, workload-identity credential brokering, and a delegated local-agent architecture. I made a tiny synthetic release card for one narrow question: “did this exact integration revision widen effective agent authority?” If that check is already solved internally, the card’s falsifier says to discard it.

**Public-safe synthetic utility only. No account access, real credentials, private data, paid calls, deployment, vulnerability claim, compliance claim, or external send.**
