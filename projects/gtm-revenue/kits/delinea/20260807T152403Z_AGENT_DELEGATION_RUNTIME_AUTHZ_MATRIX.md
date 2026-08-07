# Delinea — Agent Delegation & Runtime Authorization Decision Matrix

```yaml
schema_id: hfo.gen133.gtm_proof_kit.v1
kit_id: GTM-S07-DELINEA-AUTHZ-MATRIX-20260807T152403Z
target: Delinea
source_target_card: projects/gtm-revenue/research/20260807T142821Z_JOB_EMPLOYER_DELINEA_TARGET_CARD.md
source_target_digest_sha256: c3d748ce794c195875ad98bfa8d94f8688ed5592a7e77412bbe50069a5a389e4
status: CANDIDATE_PENDING_S04
privacy: PUBLIC_SOURCES_ONLY
external_send_authority: NONE
verifier: S04
consumer: operator
expiry_utc: 2026-08-14T14:28:21Z
```

## WHY_THIS_MAY_MATTER

Delinea publicly says its AI-agent controls authorize actions **at runtime, action by action**, rather than treating successful authentication as sufficient. Its current Staff Software Engineer role for **Agent Identity and Authorization** is described as foundational and explicitly names **OPA, Cedar, and AuthZEN** among relevant authorization technologies.

The useful design question is therefore not “which tool wins?” It is: **which responsibilities belong in the policy language/engine, which belong in the authorization API boundary, and what evidence must survive every delegated agent action?**

This matrix is a neutral design aid. It does **not** claim Delinea lacks these capabilities or reveal Delinea's internal implementation.

## HOW_TO_USE_IN_2_MINUTES

Take one risky agent action — for example, “agent acting for Alice updates a production resource” — and scan the ten rows below. Mark each row **defined / unclear / test missing**. Any `unclear` row becomes a design question; any `test missing` row becomes a held-out negative test.

| Decision question | OPA / Rego | Cedar | AuthZEN |
|---|---|---|---|
| **1. What is this thing?** | General-purpose policy engine + declarative Rego policy language over structured input/data. | Authorization-focused policy language + authorizer built around principal, action, resource, context. | Interoperability specifications / API patterns for communication between authorization components; **not** another runtime policy language. |
| **2. Actor vs represented principal** | Model explicitly in input/data (`actor`, `principal`, delegation evidence, scopes). Flexible, but the application owns the schema/semantics. | Model through principal/entities/schema plus request context or related entities. Do not assume delegation semantics are automatic. | Normalize the decision request/response boundary; underlying engine still owns policy semantics. |
| **3. Delegated/composite actions** | Natural when custom structured data and derived decisions are needed; write the rules explicitly. | Strong fit when the problem can be expressed cleanly as principal → action → resource → context with typed entities/schema. | Useful when multiple policy engines/services must expose a common authorization interface. |
| **4. Decision vs enforcement separation** | Explicit design goal: application/enforcement point queries OPA for a policy decision. | Application invokes the Cedar authorizer before performing the protected operation. | Core purpose is standardized communication among authorization components, including externalized-authorization patterns. |
| **5. Runtime context** | Arbitrary structured JSON input supports task, session, risk, device, delegation, approval and other signals. | Request `context` is first-class and intended for request-specific information; entities carry principal/resource facts. | Carries authorization request/response information across a standardized API surface; exact policy inputs depend on profile/implementation. |
| **6. Decision shape** | Can return allow/deny **or arbitrary structured decision data**. | Produces Allow/Deny plus diagnostics/determining-policy information. | Standardizes decision exchange; does not by itself decide the organization's policy semantics. |
| **7. Policy validation / testability** | Rego policies can be unit-tested; held-out negative cases can exercise exact structured inputs. | Schema validation checks policy/entity/action structure; authorization requests are deterministic test fixtures. | Best tested as interoperability/conformance plus end-to-end policy-engine tests behind the interface. |
| **8. Explain / audit evidence** | Application should persist request facts, policy/bundle version, decision and relevant structured output. OPA does not create the surrounding audit system for you. | Persist PARC inputs, policy/schema version and authorization diagnostics needed for the audit trail. | Good boundary for consistent request/decision records across heterogeneous engines; audit completeness remains an implementation responsibility. |
| **9. Continuous re-evaluation** | Re-query on every consequential action or whenever relevant context changes; caching/freshness policy is architectural. | Re-authorize each protected operation with current entities/context; caching/freshness is architectural. | Standardizes repeated decision calls, but frequency, caching and enforcement timing are implementation choices. |
| **10. Where it is strongest in a mixed architecture** | Policy engine when flexible structured policy/data and custom decision outputs matter. | Authorization engine/language when explicit authorization semantics, typed entities/schema and analyzability matter. | **Protocol/interface layer** when interoperability across authorization products/engines matters. It can complement OPA or Cedar rather than replace them. |

## Five held-out negative tests worth keeping engine-independent

1. **Missing delegation evidence → deny/fail closed.** An agent claims to act for a principal but no valid delegation/attribution evidence is present.
2. **No privilege inheritance by accident.** A human/service principal has broad access; the agent receives only the explicitly delegated subset.
3. **Action outside delegated scope → deny.** Correct principal, wrong tool/action/resource combination.
4. **High-impact action without approval → deny.** A policy-defined action class requires a fresh human-approval fact; stale or absent approval fails.
5. **Expired/revoked delegation → deny immediately.** A valid earlier grant must not survive revocation or expiry because of stale cached authorization state.

For every test, retain enough decision evidence to answer: **who/what acted, for whom, on what resource, doing what action, under which context, policy version, and result?**

## A compact architecture seam

```text
agent/tool call
   ↓
enforcement point
   ↓
normalized authorization request
(actor + represented principal + action + resource + context + delegation evidence)
   ↓
[ optional AuthZEN-compatible API boundary ]
   ↓
policy decision engine
[ OPA/Rego | Cedar | another engine ]
   ↓
allow / deny + decision evidence
   ↓
enforce → log → re-evaluate on the next consequential action
```

The important seam is **not** the brand name. It is keeping identity/delegation facts, policy evaluation, enforcement, and audit evidence separate enough that each can be tested and replaced.

## Assumptions

- The current Delinea role and June 2026 public product direction are still representative as of 2026-08-07.
- This artifact treats OPA and Cedar as policy/decision-engine technologies and AuthZEN primarily as an interoperability/API standardization effort; it does not treat them as three identical substitutes.
- No statement here describes Delinea's undisclosed internal architecture, incidents, regressions, latency, costs, or customer problems.
- The operator can credibly discuss OPA/Rego and held-out agent gates only at the level supported by existing public-safe proof; deeper identity-protocol expertise must not be implied.

## Falsifier

Retire this artifact if Delinea's current engineering requirements show that the OPA/Cedar/AuthZEN choice is already fixed and the matrix adds no useful design question, if the open role closes and there is no adjacent relationship target, or if technical review finds material inaccuracies in the comparison. External feedback that the matrix is irrelevant is stronger evidence than internal confidence.

## Evidence links

- Delinea role — Staff Software Engineer: Agent Identity and Authorization (accessed 2026-08-07): https://jobs.ashbyhq.com/delinea/9cae4086-3927-4cff-979f-f6fe4a446eda/?workplaceType=Remote
- Delinea — “AI agent authorization: Why access at the door is not enough,” published June 2026: https://delinea.com/blog/ai-agent-authorization
- Delinea Platform: https://delinea.com/products
- Open Policy Agent documentation: https://www.openpolicyagent.org/docs
- Cedar Policy Language reference: https://docs.cedarpolicy.com/
- OpenID Foundation AuthZEN Working Group: https://openid.net/wg/authzen/

## OPTIONAL — OPERATOR-REVIEWED OUTREACH NOTE — NO SEND

I noticed Delinea's current Agent Identity and Authorization role calls out delegated/composite agent actions and OPA, Cedar, and AuthZEN. I made a one-page decision matrix that separates policy-engine choices from the interoperability boundary and turns the design questions into five held-out negative tests. It is not a recommendation for a particular engine; if useful, I'd value a technical correction on what the matrix gets wrong.
