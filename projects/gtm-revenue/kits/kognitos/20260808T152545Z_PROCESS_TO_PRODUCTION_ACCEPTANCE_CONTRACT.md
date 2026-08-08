# Kognitos — Process-to-Production Acceptance Contract

**Use for one customer automation before publish/go-live.**  
**Candidate:** `process=<name> | draft/version=<exact revision> | process owner=<name/role> | FDE=<name/role>`

## Plausible problem — hypothesis, not a Kognitos diagnosis

Kognitos already exposes draft testing, versioned publishing, deterministic execution, regression/edge-case testing, monitoring, and human guidance. The narrower handoff risk is **customer-specific acceptance**: an FDE and process owner may still need one compact place to agree what business outcome, rules, integrations, exception authority, held-out evidence, and rollback conditions make *this exact revision* ready for production.

No backlog, deficient process, missing control, savings amount, or deployment failure is asserted.

## HOW_TO_USE_IN_2_MINUTES

1. Fill the first four rows before implementation expands.
2. Run the five held-out cases against the exact candidate revision.
3. Mark `GO` only if every required evidence cell is present; otherwise mark `HOLD` and name the owner of the gap.

| Acceptance field | Fill for this automation | GO condition |
|---|---|---|
| **Business outcome** | KPI: ___  Baseline: ___  Target: ___  Measurement window: ___ | Baseline/target are explicit, or explicitly `UNKNOWN` pending measurement |
| **Process rules** | Invariants / thresholds / ordering rules: ___ | Rules are written narrowly enough that two reviewers would expect the same behavior |
| **Integration dependencies** | ERP/API/DB/email/docs + read/write effect: ___ | Each dependency and production side effect is named |
| **Exception + human authority** | Human approval required when: ___  Auto-action allowed when: ___ | High-consequence or ambiguous cases have an owner and escalation path |
| **Held-out #1 — happy path** | Input: ___  Expected: ___  Evidence ref: ___ | PASS on exact revision |
| **Held-out #2 — boundary value** | Input: ___  Expected: ___  Evidence ref: ___ | PASS on exact revision |
| **Held-out #3 — missing/ambiguous fact** | Input: ___  Expected escalation: ___  Evidence ref: ___ | PASS; no silent assumption |
| **Held-out #4 — integration failure** | Injected failure: ___  Expected behavior: ___  Evidence ref: ___ | PASS; failure is visible and bounded |
| **Held-out #5 — unauthorized/exception action** | Attempt: ___  Expected block/approval: ___  Evidence ref: ___ | PASS; authority boundary holds |
| **Go-live evidence** | Representative run(s): ___  Known exceptions: ___  Publish/version ref: ___ | Evidence is attached to this exact revision |
| **Rollback trigger** | Roll back / halt if: ___  Recovery owner: ___ | Trigger and accountable owner are explicit |
| **Time-to-value clock** | Scope agreed: ___  Evidence-backed go-live: ___  Elapsed days: ___  FDE hours: ___ | Record actuals; do not invent savings |

**Decision:** `GO | HOLD`  
**Decision owner:** ___  
**Unresolved risk accepted by:** ___  
**Next review date / trigger:** ___

## WHY_THIS_MAY_MATTER

Kognitos' current US FDE role explicitly spans ambiguous process discovery, production automation, enterprise integrations, production troubleshooting, and ownership through onboarding/deployment/expansion. Its platform and documentation already provide strong execution controls; this worksheet is only useful if it reduces the *coordination cost* of agreeing on customer-specific production acceptance rather than duplicating those controls.

## Source-backed facts

- The current US Forward Deployed Engineer role describes turning ambiguous/undocumented business processes into production-grade automations, integrating enterprise systems, debugging production issues, and owning technical relationships through onboarding, deployment, and expansion.
- Kognitos' platform describes deterministic/neurosymbolic execution, automated testing of scenarios and edge cases, monitoring, automated deployment, human guidance on deviations, and built-in regression testing.
- Kognitos Quick Start says automations begin as drafts, can be run/tested, and can then be published.
- Kognitos documentation describes draft and published process states with version tracking; publishing locks a production-ready version while later edits occur in draft.
- Kognitos run documentation says runs retain inputs, outputs, state changes, a unique run ID, and can be converted into test cases.
- Kognitos' leadership page lists Neeraj Mathur as VP of Solutions Engineering; this does **not** establish hiring authority or willingness to engage.

## Assumptions

- The customer/process owner can state a business KPI or mark it unknown.
- The exact candidate revision/version can be identified.
- Five synthetic or non-sensitive held-out cases can represent the highest-value failure boundaries.
- This sheet supplements Kognitos' existing platform controls; it does not replace them.

## Strongest falsifier

**Kill this artifact** if Kognitos already gives FDEs an equivalent low-overhead, versioned customer-deployment contract that directly binds the business KPI/baseline, process rules, integration dependencies, exception/human authority, held-out regression evidence, go-live evidence, rollback, and time-to-value to the exact promoted automation. Public documentation reviewed this run shows strong pieces of that lifecycle, but did not establish the full combined contract.

## Evidence links

1. https://jobs.ashbyhq.com/kognitos/75ef6778-ee45-4eb5-b2fa-02834f78a986
2. https://www.kognitos.com/platform/
3. https://docs.kognitos.com/guides/getting-started/quick-start
4. https://www.kognitos.com/about-us/
5. https://docs.kognitos.com/processes/overview
6. https://docs.kognitos.com/processes/runs

## Optional operator-reviewed outreach note — NO SEND

I saw the FDE role centers on taking ambiguous customer processes through production. I made a one-page acceptance contract that complements Kognitos' existing deterministic/testing lifecycle by binding one exact automation revision to business outcome, exception authority, held-out evidence, and rollback. If that seam is already solved internally, the artifact is redundant; if not, it may be a useful two-minute work sample for how I structure production handoffs.

---
**Boundary:** public-safe preparation only. No Kognitos/customer account, credentials, private data, deployment, application, outreach, or external publication was used.  
**Target-card evidence digest:** `b26b8e2943b1e2112aee225796ad2e36d1c66555316427b00de2ca40b33750a3`
