---
schema_id: hfo.gen133.s07_gtm_proof_kit.v1
status: CANDIDATE_ONLY
target: Edward Jones
work_item_id: S07_EDWARD_JONES_AGENT_NHI_LIFECYCLE_GATE_V1
source_target_card_evidence_digest_sha256: 498235d11dbd04d8ee4080784a2327041246a5cd3e1bcaddcf94a60a423450df
privacy: PUBLIC_SOURCES_ONLY
effect_ceiling: T0_RESEARCH_PREP_ONLY
send_authority: NONE
verifier: S04_HRIST_STRUCTURAL_PREFLIGHT
---

# Agent + NHI Lifecycle Gate — Owner × Delegation × Policy × Evidence

**Plausible problem — hypothesis, not an Edward Jones finding:** as AI agents and other non-human identities enter enterprise workflows, teams may need a compact promotion gate that makes ownership, delegated authority, credential lifecycle, policy enforcement, and audit evidence explicit.

**Intended reader:** Non-Human Identity / IAM-PAM / AI Security architecture or engineering lead.

## WHY_THIS_MAY_MATTER

Edward Jones publicly says it is embedding AI into proprietary systems. Its NHI architecture and engineering postings explicitly cover AI/agentic identities, delegated workloads, lifecycle management, ownership, least privilege, credential rotation, policy decision/enforcement, automation, monitoring, and audit readiness. That proves priority and implementation work—not a control gap, incident, slow process, or desire for outside help.

## HOW_TO_USE_IN_2_MINUTES

Pick one proposed agent/workload identity. Mark each row **GREEN / UNKNOWN / RED**. Promote only when every required row is GREEN or an explicitly owned exception exists.

| Gate | Check | GREEN evidence |
|---|---|---|
| 1. Identity class | Service/workload/API/RPA/AI agent/delegated/composite? | Canonical class + inventory ID |
| 2. Accountable owner | Who owns lifecycle and access? | Named human/service owner + review cadence |
| 3. Delegation chain | Acting for whom, through what chain, until when? | Principal → delegate → target + expiry |
| 4. Allowed actions | Which resources/actions are allowed? | Least-privilege allow-set; deny-by-default |
| 5. Policy point | Where is authorization decided/enforced? | PDP/PEP or equivalent + policy/version |
| 6. Credential lifecycle | Federated/ephemeral/cert/secret/token? | Issuer + TTL/rotation rule |
| 7. Revocation path | How is access disabled on state/risk/owner change? | Tested revoke/disable path + owner |
| 8. Runtime evidence | Can the action be reconstructed? | Identity + delegate + policy + target + result + time |
| 9. Exception/remediation | Who owns UNKNOWN/RED and by when? | Owner + due/review date |

### Five held-out negative controls

| Mutation | Expected safe result |
|---|---|
| Missing owner | Block promotion; quarantine/unassigned state |
| Expired delegation | Deny action; require fresh authorization |
| Stale privilege after entitlement removal | Old privilege cannot authorize new action |
| Required policy context missing | Fail closed or explicit human review |
| Action lacks reconstructable identity/policy evidence | Do not promote; surface evidence gap |

## SOURCE-BACKED FACTS

- **NHI Architect — PAM and AuthN:** enterprise NHI governance, AI identity standards/controls, AI agents/agentic identities/delegated workloads, ownership/rotation/audit standards, authorization management, policy decision/enforcement, and policy orchestration.
- **Senior Security Engineer — NHI:** hands-on automation, onboarding, remediation, provisioning/deprovisioning, credential rotation, least privilege, monitoring, and lifecycle operations.
- **July 8, 2026:** Edward Jones said it is embedding AI into proprietary systems to automate repetitive work and improve advisor/practice-team efficiency.
- CIO Frank LaQuinta's public bio says he leads Digital, Data and Operations including Technology, AI and Data. This does **not** prove NHI procurement ownership.

Evidence:
1. https://careers.edwardjones.com/job/23605272/non-human-identity-architect-pam-and-authn-tempe-az/
2. https://careers.edwardjones.com/job/23595486/senior-security-engineer-non-human-identity-tempe-az/
3. https://www.edwardjones.com/us-en/why-edward-jones/news-media/press-releases/ai-future-financial-advisor-research-2026
4. https://www.edwardjones.com/us-en/why-edward-jones/news-media/thought-leadership/firm-leadership/frank-laquinta

## HYPOTHESES / ASSUMPTIONS / FALSIFIER

**Pain hypothesis:** lifecycle work may consume material engineering time as agent/workload identity volume and delegated-authority patterns grow.

**Unknown baseline:** no public source here establishes backlog, audit hours, incident rate, manual decision count, or current lifecycle cycle time.

**Counterevidence:** Edward Jones develops technology internally and is already hiring senior NHI architecture/engineering capability; existing IAM/PAM/secrets systems may already cover this gate.

**Measurable value metric:** median elapsed time from NHI/agent discovery or onboarding request to an owner-attested, least-privilege, policy-bound, credential-rotated/ephemeral, audit-evidenced compliant state. Measure baseline before proposing a target.

**Assumptions:** agent/workload identities fit a shared enterprise lifecycle; these nine fields apply to at least some workflows; evidence can be captured without client/private data.

**Strongest falsifier:** Edward Jones already has an enterprise NHI process that automatically inventories agent/workload identities, binds ownership/delegation, enforces least privilege with short-lived credentials, captures policy/audit evidence, and reaches acceptable lifecycle cycle time without meaningful manual rework. If true, retire or reframe this gate.

## OPTIONAL OPERATOR-REVIEWED RELATIONSHIP NOTE — NO SEND AUTHORITY

Your public NHI roles span AI/agent identities, delegated workloads, policy enforcement and lifecycle evidence. I made a one-page gate turning those concerns into nine checks plus five negative controls. It is a public-source work sample, not an assessment of Edward Jones.
