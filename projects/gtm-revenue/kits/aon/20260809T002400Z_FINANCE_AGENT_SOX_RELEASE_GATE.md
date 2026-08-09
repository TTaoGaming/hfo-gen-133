# Finance Agent SOX Release Gate — Control × SoD × Data × Trace × Override × Rollback

**For:** Finance Technology / Controllership leaders reviewing finance-agent production changes  
**Use case:** one revision, one evidence packet, one `PROMOTE | HOLD | REJECT` decision  
**Scope:** public-safe template; no Aon system, data, or control environment was tested.

## PLAUSIBLE_PROBLEM

A finance agent can look correct in a demo yet still be unready for a close or treasury workflow if the promoted revision is not tied to evidence for control behavior, segregation of duties (SoD), data lineage/reconciliation, action authority, traceability, human override, and rollback.

Aon's current finance-agent roles explicitly call for SOX-aligned workflows, approvals/evidence capture, logging/traceability, override controls, release governance, data lineage, reconciliation, SoD/access controls, monitoring, and lifecycle management. That supports the **review surface** below. It does **not** show that Aon lacks an internal release gate or has a control problem.

## WHY_THIS_MAY_MATTER

**Hypothesis:** a single revision-bound gate may reduce repeated reviewer effort and ambiguity when Finance, SOX/control owners, Risk, and engineering decide whether an agent change is ready.

Measure before claiming value:
- reviewer + control-owner hours per accepted revision;
- calendar time from candidate revision to approved release;
- number of release reviews returned for missing evidence.

## HOW_TO_USE_IN_2_MINUTES

Write the exact candidate revision at the top. For each row, paste one evidence pointer or mark `MISSING`. Any required `MISSING` item means `HOLD`; an observed control violation means `REJECT`. `PROMOTE` requires all required evidence plus a named human approver.

**Candidate revision:** `________________`  **Previous known-good revision:** `________________`

| Gate | Reviewer question | Minimum evidence pointer | Result |
|---|---|---|---|
| CONTROL | Does the revision preserve the intended close/treasury control behavior? | held-out expected-vs-actual control tests | PASS / FAIL / MISSING |
| SoD + AUTHORITY | Can the agent perform only actions allowed for its delegated role, with prohibited maker/reviewer combinations denied? | policy/rule version + negative authorization tests | PASS / FAIL / MISSING |
| DATA | Are required source, lineage, completeness, and reconciliation checks bound to this revision? | dataset/source versions + reconciliation result | PASS / FAIL / MISSING |
| TRACE | Can a reviewer reconstruct inputs, decisions, tool calls, approvals, exceptions, and outputs? | immutable run/trace IDs for held-out cases | PASS / FAIL / MISSING |
| OVERRIDE | Can the required human stop, reject, correct, or escalate the workflow at the defined points? | approval/override rule + exercised negative case | PASS / FAIL / MISSING |
| ROLLBACK | Is there a tested path back to the previous known-good revision without widening authority? | rollback target + rollback dry-run evidence | PASS / FAIL / MISSING |

### Five held-out negative controls

1. **SoD conflict:** same delegated principal attempts maker + reviewer actions → must deny/escalate.
2. **Unreconciled input:** source totals do not reconcile → must stop or route to exception handling.
3. **Unauthorized tool/action:** agent attempts an action outside its policy → must deny and trace.
4. **Missing approval/trace:** required approval or evidence field is absent → must `HOLD`, never silently continue.
5. **Rollback case:** candidate fails a critical test → must restore the named known-good revision and preserve evidence.

**Decision:** `PROMOTE / HOLD / REJECT`  
**Missing evidence / rejection reason:** `________________________________________`  
**Named human approver:** `________________`  **Decision timestamp:** `________________`

## SOURCE_BACKED_FACTS

- Aon's Director, AI Lead — Finance Agents Engineering role calls for SOX-aligned workflows, approvals/evidence capture, logging, execution traceability, override controls, and change/release governance for close agents.
- Aon's Senior Manager, AI Lead — Treasury & Cash Management Agents role calls for data lineage, reconciliation, segregation of duties/access controls, auditability, and enterprise standards for agent security, monitoring, and lifecycle management.
- Aon identifies Edmund Reese as EVP and CFO.
- Aon's July 14, 2026 workforce discussion says Aon is using AI and emphasizes critical thinking, risk management, and guardrails alongside adoption.

## ASSUMPTIONS

- One exact agent revision can be identified and tied to its model/tool/policy/data dependencies.
- Finance/control reviewers can access evidence pointers without exposing sensitive data in this card.
- Existing platform controls remain authoritative; this card is only a review index, not a substitute for them.

## FALSIFIER

Kill this wedge if Aon already has a lower-friction versioned mechanism that binds control evidence, SoD, data lineage/reconciliation, action authority, traces, human override, and rollback to every promoted finance-agent revision—or if internal ownership leaves no credible external integration/capacity seam.

## EVIDENCE_LINKS

1. https://jobs.aon.com/jobs/101809?lang=en-us
2. https://jobs.aon.com/jobs/101790?lang=en-us
3. https://www.aon.com/en/about/leadership-and-governance/edmund-reese-profile
4. https://www.aon.com/en/insights/podcasts/on-aon-episode-121-workforce-readiness-is-the-advantage-in-an-ai-future

## OPTIONAL_OPERATOR_REVIEWED_OUTREACH_NOTE

Public-safe draft only; **do not send without operator review**:

> I noticed Aon's finance-agent roles explicitly join close/treasury automation with release governance, SoD, lineage, traceability, and override controls. I made a one-page revision gate that turns those requirements into a `PROMOTE | HOLD | REJECT` evidence check. If your internal process already does this cleanly, the artifact is redundant; if not, it may be a useful comparison point.
