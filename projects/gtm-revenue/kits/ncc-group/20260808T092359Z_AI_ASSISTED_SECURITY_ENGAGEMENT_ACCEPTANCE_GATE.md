---
schema_id: hfo.gen133.s07_gtm_proof_kit.v1
status: CANDIDATE_FOR_S04_PREFLIGHT
target: NCC Group
species: CHANNEL_PARTNER
work_item_id: S07_NCC_GROUP_AI_ASSURANCE_ACCEPTANCE_GATE_V1
route: RELATIONSHIP_ONLY
privacy: PUBLIC_SOURCES_ONLY
effect_ceiling: T0_RESEARCH_PREP_ONLY
send_status: NO_SEND_OPERATOR_REVIEW_ONLY
source_target_card: projects/gtm-revenue/research/20260808T082800Z_CHANNEL_PARTNER_NCC_GROUP_TARGET_CARD.md
source_target_card_blob_sha1: 96583bb2d0443538451586d1dca45d6d1cc0b23c
source_target_card_declared_evidence_digest_sha256: fe661ccc6c01cea0b8e5384442c8405547ba9f2d03b4ca54786407fd6ed8f64f
s02_claim: projects/gtm-revenue/claims/20260808T090649Z_NCC_GROUP_AI_ASSURANCE_ACCEPTANCE_GATE_ADMISSION.claim.yaml
s02_acceptance_sha256: 4a97c6505688223589d30f2b1c464d08eb1d2c5de13fbf480b038b79d422ad83
s02_idempotency_sha256: cdb34cd3a8fffd3c9b20255a6117b9300e22c97e470d5de353ee50b8bd9a5a88
verifier: S04_HRIST_STRUCTURAL_PREFLIGHT
consumer: S03_REDUCER_VERIFICATION_ROUTER_CONSUMERACK_TRACKER
expiry_utc: 2026-08-08T13:06:49Z
---

# AI-Assisted Security Engagement Acceptance Gate

**Plausible problem:** an AI-assisted finding can be technically useful and still be unsafe to accept for client delivery if scope, coverage, authority, provenance, confidentiality, human disposition, or rollback evidence is missing. NCC Group already publicly describes AI-assisted code review as combining automation, AI-assisted analysis, expert human validation, and a proprietary controlled/auditable framework. This page is therefore a **candidate acceptance interface**, not a diagnosis of a missing NCC Group control.

**Intended user:** a Technical Assurance / AI Security / service-quality lead reviewing an AI-assisted finding or a model/tool/workflow revision before it becomes client-facing.

## HOW_TO_USE_IN_2_MINUTES

1. Mark each gate **GREEN / UNKNOWN / RED** for the candidate finding or workflow revision.
2. Run the five negative controls at the bottom. A negative control passes only when the candidate is **rejected or safely contained**.
3. Candidate default: accept only when every required gate is GREEN and all five negative controls pass. Adapt thresholds to the engagement; this is a work-sample pattern, not NCC Group policy.

| Gate | GREEN evidence to attach | UNKNOWN / RED trigger |
|---|---|---|
| 1. Engagement scope preserved | Scope ID + allowed target/action set are bound to the candidate | Finding/action is useful but outside agreed scope, or scope binding is absent |
| 2. Prohibited actions impossible | Deny rules / tool allowlist / sandbox boundary show forbidden actions cannot execute | Privileged or destructive path exists without an explicit deny/approval boundary |
| 3. Held-out coverage / regression | Pinned held-out cases pass at the agreed threshold; changed cases are listed | Model/tool change loses a previously required case, or held-out set is not run |
| 4. False-positive / rework guardrail recorded | Review sample, disposition counts, and locally agreed guardrail are recorded | No guardrail is defined, or the candidate exceeds it without explicit review |
| 5. Model / tool / version pinned | Model, prompt/config, tool/MCP versions, policy bundle and relevant hashes/IDs are recorded | A reviewer cannot identify the exact execution configuration |
| 6. Source + evidence provenance complete | Finding points to source artifact, transformation steps and supporting evidence | Evidence is missing, stale, unverifiable, or detached from the claim |
| 7. Client-data handling boundary respected | Data class, allowed processors/stores/egress and retention boundary are explicit | Data path is unknown or exceeds the engagement-approved handling boundary |
| 8. Named human-review disposition | Named reviewer records accept / revise / reject plus rationale | AI output is treated as accepted without an accountable human disposition |
| 9. Trace / replay package complete | Trace links input → model/tool/policy → evidence → reviewer disposition | Material decision path cannot be reconstructed with the permitted evidence set |
| 10. Rollback / manual fallback owner named | Owner + disable/revert/manual path are recorded and reachable | No owner or practical fallback exists if the AI-assisted path is withdrawn |

## Five held-out negative controls

| Negative control | Required safe result |
|---|---|
| A useful finding is intentionally placed **outside engagement scope** | Reject as out of scope even if technically valid |
| A plausible finding is supplied with **missing supporting evidence** | Reject / return for evidence; do not promote |
| The model/tool is swapped and **one held-out coverage case regresses** | Block promotion pending disposition or restoration |
| A workflow attempts a **privileged tool call without policy authority** | Deny before side effect; record the denial path |
| High-confidence AI output arrives with **no named human disposition** | Keep unaccepted until an authorized reviewer records disposition |

## WHY_THIS_MAY_MATTER

### Source-backed facts
- NCC Group's 2026 OpenAI Daybreak participation includes frontier cyber-model research using security-testing data in **controlled environments** with governance and safeguards.
- NCC Group is a founding signatory of the CREST AI Charter and publicly supports human oversight, data protection, accountability, transparency and assurance in AI-enabled cyber security.
- NCC Group's current AI-Assisted Code Review page says the service combines automation, AI-assisted analysis and **expert human validation** within a **proprietary controlled, auditable framework**.
- NCC Group's agentic-AI guidance argues for architectural trust boundaries and limiting privileged resources based on data trust.
- NCC Group's research surface includes AI/security research and customer-funded Security Research Services, including work spanning AI and secure systems engineering.

### Hypothesis — not a company fact
As frontier models and AI-assisted analysis change, there **may** be recurring review cost in proving that a candidate finding/workflow revision still preserves engagement scope, coverage, bounded authority, reproducibility, evidence provenance, confidentiality and required human validation. Public sources do **not** establish that NCC Group's current process is slow, manual, deficient, understaffed, or open to outside help.

**Measurable value metric:** *assessment acceptance cycle time* = elapsed time from an AI-assisted candidate finding or analysis entering review to a human-validated, scope-compliant, evidence-complete finding accepted for client delivery. **Baseline: unknown.** Do not invent a savings target; treat coverage and false-positive/rework rates as guardrails.

## Assumptions
- The same acceptance concerns recur across at least some AI-assisted assessment revisions.
- A compact evidence packet is useful only if it complements, rather than duplicates, NCC Group's existing controlled/auditable framework.
- Engagement-specific thresholds, client-data rules and reviewer authority would need to come from NCC Group; this page does not supply or infer them.

## Strongest falsifier
If NCC Group's existing proprietary framework already binds scope policy, held-out coverage/regression, model/tool versioning, evidence provenance, human disposition, data-handling constraints and rollback into client-delivery acceptance with acceptable review overhead, this gate is redundant and should be retired rather than polished.

## Public evidence links
1. https://www.nccgroup.com/newsroom/ncc-group-selected-to-join-the-openai-daybreak-cyber-partner-program/
2. https://www.nccgroup.com/newsroom/ncc-group-becomes-founding-signatory-of-crest-ai-charter-helping-shape-trusted-ai-in-cyber-security/
3. https://www.nccgroup.com/research/research-articles/
4. https://www.nccgroup.com/technical-assurance/application-security/code-review/
5. https://www.nccgroup.com/research/
6. https://www.nccgroup.com/securing-agentic-ai-what-openclaw-gets-wrong-and-how-to-do-it-right/

## Optional operator-reviewed relationship note — NO SEND

> I noticed NCC Group is already combining controlled AI-assisted review, human validation and frontier-model research. I made a one-page acceptance-gate work sample for the narrow handoff from AI-assisted candidate finding to human-approved client evidence. It may be redundant with your internal framework; if so, that is useful falsification rather than a pitch.

**Boundary:** public sources only. No client data, security testing, outreach, application, account action, spend, deployment, merge, or external publication is authorized by this artifact.
