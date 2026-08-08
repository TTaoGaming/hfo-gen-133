# Agent Prototype Graduation Card — Utility × Eval × Authority × Data × Ops

**Problem:** an agent prototype can look useful while the evidence needed to promote that *exact revision* is scattered across task quality, tool authority, data boundaries, and operational readiness. This one-page card turns those separate checks into one fail-closed `PROMOTE | HOLD | REJECT` decision without requiring Benchling or customer data.

**Synthetic example only:** `cro-report-intake-agent@0.3.0` converts a fake CRO report into a structured experiment record and draft study summary. No Benchling API, credentials, proprietary records, regulated data, or customer data are used.

## HOW_TO_USE_IN_2_MINUTES

1. Name the exact candidate revision and rollback target.
2. Fill the five evidence rows below with links or immutable IDs; do not mark a row green from prose alone.
3. Apply the verdict rule: **REJECT** on a prohibited authority/data violation; **HOLD** on missing or failing evidence; **PROMOTE** only when all five rows pass for the same revision and a named human approver accepts the risk.

| Evidence row | Minimum promotion evidence | Synthetic example | Status |
|---|---|---|---|
| **UTILITY** | Named user/workflow, measurable target, and an explicit non-goal | CRO-report intake → structured experiment record → draft study summary; target = reduce manual normalization effort; non-goal = scientific or regulatory judgment | `HOLD` — no real user evidence |
| **EVAL** | Predeclared held-out task set, success threshold, and failure taxonomy; include prompt-injection and tool-misuse negative controls | Fake reports only; check extraction fidelity, citation-to-source mapping, unsupported-claim rate, prompt-injection resistance, and forbidden-tool behavior | `HOLD` — tests not executed |
| **AUTHORITY** | Exact principal/role, allowed tools/actions, denied actions, and human-approval boundary | Read synthetic input; write only a draft local record; deny external send, account mutation, autonomous submission, and state-changing external calls | `HOLD` — policy not executed |
| **DATA** | Data classification, tenant/workspace boundary, secrets rule, retention/logging rule, and cross-boundary negative control | Synthetic public-safe records only; no secrets; deny cross-tenant/cross-workspace reads; redact raw payloads from logs where not needed | `HOLD` — boundary not exercised |
| **OPS** | Trace ID, model/tool/policy versions, latency/cost ceiling, owner/on-call path, rollback target, and approval receipt | Bind model/router/policy revisions to one trace; define rollback to `0.2.x`; stop on missing trace or ceiling breach | `HOLD` — no run evidence |

### Decision rule

```text
if prohibited_authority_or_data_violation: REJECT
elif any_required_evidence_missing_or_failed: HOLD
elif all_five_rows_pass_for_exact_revision and human_approval_receipt_present: PROMOTE
else: HOLD
```

**Current synthetic verdict: `HOLD`.** That is intentional: this card is a review artifact, not evidence that the example agent passed anything.

## WHY_THIS_MAY_MATTER

### Source-backed facts

- Benchling's current **Agentic AI Engineer** posting says the founding engineer will bridge departmental AI experimentation into hardened production systems, own CI/CD/testing/evaluation/deployment infrastructure, define prototype-graduation criteria, and design RBAC, audit logging, human-in-the-loop controls, and threat models for prompt injection, tool misuse, and data exfiltration.
- Benchling stated on **2026-02-10** that Benchling AI was generally available and had been used across **500 biotech companies**; that is Benchling's own published figure, not independently audited here.
- Benchling's **2026-06-03** AI update describes reusable Skills and custom MCP connectors as part of its agent surface.
- Benchling Automation, launched **2026-05-28**, connects instrument data, analyses, and scientific records with end-to-end traceability, showing why provenance and operational boundaries matter in scientific workflows.

### Hypothesis, not company fact

A standardized revision-bound graduation card **may** reduce reviewer ambiguity or cycle time when an internal prototype moves toward production. Public sources do **not** establish that Benchling currently has a bottleneck, excessive review labor, weak controls, incidents, or missing promotion machinery.

## ASSUMPTIONS

- This is a generic engineering acceptance pattern, not a statement of Benchling policy or compliance requirements.
- Thresholds and required evidence must be set by the actual workflow owner and Security/IT; the card deliberately does not invent numeric pass rates.
- The job route remains attractive only if the operator can truthfully substantiate the posting's experience bar and production-agent claims during later operator review; no private resume evidence was used here.
- A real implementation should keep evaluation evidence and runtime authorization evidence distinct, then bind both to the same immutable revision.

## FALSIFIER

Discard this artifact as redundant if Benchling already has a low-overhead, versioned promotion contract that binds utility, held-out evals, tool/action authority, data/security boundaries, operational evidence, human approval, and rollback to the exact promoted agent revision. Also downgrade the application proof if the operator cannot substantiate the role's stated seniority and hands-on production LLM/agent experience.

## EVIDENCE_LINKS

1. Benchling — Agentic AI Engineer: https://jobs.ashbyhq.com/benchling/d5896e95-fed2-4cd4-b104-1ea4df92f7d7
2. Benchling — 500 biotech companies are using Benchling AI, now generally available (2026-02-10): https://www.benchling.com/blog/benchling-ai-now-generally-available
3. Benchling — The ELN is dead, long live the ELN (2026-06-03): https://www.benchling.com/blog/the-eln-is-dead-long-live-the-eln
4. Benchling — Benchling Automation: Closing the lab-in-a-loop (2026-05-28): https://www.benchling.com/blog/benchling-automation-closing-the-lab-in-a-loop

## OPTIONAL_OPERATOR_REVIEWED_OUTREACH_NOTE — NOT SENT

I noticed the Agentic AI Engineer role explicitly owns the jump from departmental prototypes to production-grade agentic systems. I made a one-page synthetic graduation card that binds utility, held-out eval evidence, tool authority, data boundaries, and rollback to one revision; it deliberately returns `HOLD` when evidence is missing. If useful, I would use it as a discussion artifact rather than claim it reflects Benchling's internal process.
