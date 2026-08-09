# Regulated AI Change Promotion Card
**For one AI-assisted security/operations workflow revision**

## Plausible problem
A small workflow revision can change more than code: model behavior, retrieved data, tool authority, human-escalation behavior, trace coverage, latency/cost, or rollback semantics can shift at the same time. In a regulated environment, a reviewer needs one place to see **what materially changed and what evidence is still missing** before promotion.

This is a public-safe decision aid, not an assertion that Wells Fargo currently lacks these controls.

## WHY_THIS_MAY_MATTER
Wells Fargo currently has a Senior Software Engineer role covering AI-assisted vulnerability analysis, incident management, operational intelligence, application support, observability, Secure Development Lifecycle, Responsible AI, security/compliance/governance, DevOps/MLOps, and vulnerability-management automation. That establishes this as a live engineering surface. It does **not** establish slow releases, control failures, excess review hours, or a need for outside tooling.

## HOW_TO_USE_IN_2_MINUTES
1. Name the exact baseline and candidate revision.
2. For each row, write `PASS`, `FAIL`, or `MISSING`, plus one evidence pointer.
3. Mark only the **material delta** from baseline.
4. Apply the verdict rule at the bottom. Missing evidence is `HOLD`, not assumed green.

## Two-minute promotion card

| Gate | Baseline → candidate question | Evidence to bind | Status |
|---|---|---|---|
| **1. Held-out behavior** | Did task quality regress on frozen, representative cases? | eval-set digest + per-case results + grader/version | `___` |
| **2. Data boundary** | Can the candidate retrieve, expose, or retain data outside the approved scope? | retrieval/data-scope policy + negative test | `___` |
| **3. Action authority** | Did any principal, model, agent, or tool gain a new write/action path? | principal/tool/action matrix + deterministic policy result | `___` |
| **4. Human escalation** | Are consequential/ambiguous cases still stopped or escalated where required? | approval rule + escalation test | `___` |
| **5. Security / risk controls** | Did the revision bypass required SDL, scanning, governance, or risk checkpoints? | control checklist + approver/evidence refs | `___` |
| **6. Traceability** | Can a reviewer reconstruct model, prompt/workflow, tool calls, policy decision, and outcome? | trace sample + exact revision/model/policy IDs | `___` |
| **7. Cost / latency** | Is the candidate still inside the approved envelope? | measured p50/p95 latency + cost/run on frozen cases | `___` |
| **8. Rollback** | Is there one exact known-good revision and a tested rollback path? | rollback revision ID + test/readback | `___` |

### Material-delta strip
Fill only what changed.

- Workflow / prompt / graph: `___`
- Model / provider / routing rule: `___`
- Retrieval source / index / embedding: `___`
- Principal / role / credential scope: `___`
- Tool / API / action scope: `___`
- Policy / approval rule: `___`
- Eval set / grader: `___`
- Telemetry / retention: `___`

## Held-out negative controls
Run these against the **candidate**, not just the baseline.

| Negative control | Expected result |
|---|---|
| Wrong principal requests a privileged action | `DENY` |
| Candidate attempts a newly reachable action not explicitly approved | `DENY` |
| Retrieval crosses the declared data boundary | `DENY / REDACT / ESCALATE` |
| High-impact or ambiguous action lacks required human approval | `HOLD / ESCALATE` |
| Frozen held-out case regresses below threshold | `HOLD` |
| Trace is missing exact model/workflow/policy identity | `HOLD` |
| Cost or latency exceeds the declared envelope | `HOLD` unless separately approved |
| Rollback target differs from the tested known-good revision | `REJECT` |

## Deterministic authority oracle
Keep action authorization separate from model scoring. A minimal policy contract can be as simple as:

```rego
package ai_change_gate

default allow := false

allow if {
  input.principal in input.allowed_principals
  input.action in input.allowed_actions
  input.data_classification in input.allowed_data_classes
  not input.requires_human_approval
}

decision := "ESCALATE" if input.requires_human_approval
decision := "ALLOW" if allow
decision := "DENY" if not allow
```

Treat this as a starter shape only; real policy must match the organization's own identity, data-classification, approval, and exception model.

## Verdict rule
- **PROMOTE** — all required gates are `PASS`, evidence is bound to the exact candidate, no unauthorized authority/data widening exists, and rollback is exact.
- **HOLD** — any required evidence is `MISSING`, stale, ambiguous, or not bound to the exact candidate.
- **REJECT** — a held-out regression breaches threshold, data/action authority widens without explicit approval, required human escalation is bypassed, or rollback identity is inconsistent.

## Source-backed facts
1. Wells Fargo's current Senior Software Engineer posting (posted July 20, 2026; posting end August 30, 2026) explicitly covers AI-driven vulnerability analysis, incident management, operational intelligence, application support, observability, Secure Development Lifecycle, Responsible AI, security/compliance/governance, DevOps/MLOps, vulnerability management, and risk-program accountability.
2. Wells Fargo's current leadership page identifies Saul Van Beurden as Head of Artificial Intelligence and Co-CEO of Consumer Banking and Lending, and as a member of the Operating Committee.

## Hypotheses — not source-backed claims
- AI-assisted operational-workflow revisions **may** create review overhead because multiple evidence types must stay aligned to one exact candidate.
- A compact revision-bound evidence card **may** reduce reviewer search/reconciliation effort.
- The most useful persona is likely enterprise AI/platform engineering or technology-risk/security-operations leadership responsible for lifecycle controls and change approval.
- Procurement authority, internal tooling gaps, incident history, willingness to buy, savings, review time, and release-cycle delay are **unknown**.

## Evidence links
- Wells Fargo job posting, verified current 2026-08-09: https://www.wellsfargojobs.com/en/jobs/r-560213/senior-software-engineer/
- Wells Fargo leadership biography, verified current 2026-08-09: https://www.wellsfargo.com/about/corporate/governance/vanbeurden/

## Assumptions
- The workflow can perform or recommend actions whose authority matters.
- There is a meaningful baseline/candidate revision boundary.
- Held-out cases, policy decisions, traces, cost/latency measurements, and rollback identity can be bound to that revision.
- Existing internal controls remain authoritative; this card is only a review surface.

## Falsifier
Discard this artifact if Wells Fargo already has a low-overhead mechanism that binds held-out evals, data boundaries, deterministic action authorization, risk/control approval, trace evidence, cost/latency, and rollback to each exact AI-enabled workflow revision — or if the relevant workflows are advisory only and cannot take consequential actions.

## Optional operator-reviewed outreach note — NO SEND
> I saw the current Wells Fargo engineering role combining AI-assisted security/operations workflows with Responsible AI, observability, SDL, and risk controls. I made a one-page public-safe change-promotion card that forces one revision to bind eval, data boundary, action authority, escalation, trace, cost/latency, and rollback evidence. If that review seam is already solved internally, the card should be redundant; if not, I would value feedback on what evidence is actually hardest to reconcile.

**No outreach is authorized by this artifact.**
