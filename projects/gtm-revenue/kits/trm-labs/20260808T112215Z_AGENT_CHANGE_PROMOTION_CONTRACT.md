# TRM Agent Change Promotion Contract — Quality × Authority × Evidence

**Problem this is meant to help with:** when an agent changes quickly across model, prompt, tool, policy, or framework revisions, reviewers need one place to decide whether the **exact candidate** is ready to promote without re-assembling quality, authority, trace, and rollback evidence from separate systems.

This is a public-safe work sample aligned to TRM Labs' published engineering practices. It is **not** a diagnosis, audit, claim of a missing control, or claim that TRM wants outside help.

## WHY_THIS_MAY_MATTER

TRM publicly describes AI output making quality, prioritization, and verification the bottleneck, while also describing a shared agent platform with permissions, audit logs, evals, feedback loops, explicit human-only decisions, and a credential-broker process with acceptance criteria and adversarial review. The narrow hypothesis here is that a compact cross-control promotion contract may reduce reviewer reconstruction work **if** these controls are not already bound to one exact candidate revision.

## HOW_TO_USE_IN_2_MINUTES

1. Fill the candidate identity once.
2. Mark each of the seven gates `PASS`, `HOLD`, or `N/A` and paste one evidence pointer.
3. A human owner makes the only promotion decision. Any required `HOLD` means do not promote.

### Candidate identity

| Field | Exact value |
|---|---|
| Agent/workflow revision | `__________` |
| Model + version/route | `__________` |
| Prompt/config digest | `__________` |
| Tool/MCP set digest | `__________` |
| Policy/authority digest | `__________` |
| Eval dataset/version | `__________` |
| Evidence bundle digest | `__________` |

### Seven release gates

| Gate | PASS evidence | HOLD condition |
|---|---|---|
| **1. Held-out task success** | Predeclared held-out suite passes the candidate's required success threshold; failures are attached, not hidden. | Threshold missed, test set changed after seeing results, or evidence is not candidate-bound. |
| **2. Hallucination bound** | Predeclared unsupported-claim/error metric is within its allowed bound on held-out cases. | Bound missed, scoring rule changed post hoc, or evaluator disagreement is unresolved. |
| **3. Latency** | Candidate meets the declared latency/SLO threshold on the intended route and workload class. | Threshold missed or measurement excludes retries/fallbacks that occur in production-like execution. |
| **4. Credential isolation** | Agent receives placeholders/scoped handles rather than raw reusable secrets; negative control confirms the candidate cannot read the underlying credential. | Raw credential is agent-visible, isolation test fails, or the credential path is untested. |
| **5. Tool/action authority** | Allowed tools/actions are explicit and candidate-bound; disallowed-action negative controls fail closed; human-only decisions remain human-only. | Authority is broader than declared, stale approval is accepted, or a disallowed action succeeds. |
| **6. Trace completeness** | One trace reconstructs candidate revision, model route, tool calls, policy decision, key inputs/outputs, eval result, and human decision without relying on agent self-report. | Missing revision/policy/tool identity, unlinked evidence, or materially incomplete trace. |
| **7. Rollback** | Named owner can disable/revert the candidate to a known prior revision; rollback path is recorded before promotion. | No known-good target, no owner, rollback requires improvisation, or rollback evidence is stale. |

### Human promotion decision

`PROMOTE` / `HOLD`

Human owner: `__________`  
Decision time: `__________`  
Evidence bundle digest: `__________`  
Known accepted exceptions: `__________`

**Rule:** this sheet organizes evidence; it does not grant authority. Promotion remains a human decision.

## SOURCE-BACKED FACTS

- TRM's live **AI Agent Engineer - US Remote** role says the AI Engineering team builds infrastructure and operational tooling for AI systems deployed with speed, safety, and scale, with observability and governance for production readiness.
- TRM's May 22, 2026 engineering article says AI-assisted output had outpaced absorption, PR review queues lengthened, and quality/prioritization/verification became the bottleneck. The same article says AskNickiBot centralizes OAuth, per-tool permissions, audit logs, retrieval, evals, and feedback loops, and that important decisions remain human-owned.
- TRM's June 23, 2026 credential-broker article describes acceptance criteria, repeatable demo/test evidence, adversarial review by agents that did not author the code, and explicit human decision ownership.
- TRM's March 27, 2026 observability article reports an observability migration that reduced costs by over 80%; this is counterevidence against pitching TRM a generic observability-cost fix.

## HYPOTHESIS — NOT A COMPANY FACT

TRM's AI Engineering team **may** benefit from a compact candidate-bound promotion packet if reviewers currently reconstruct quality, authority, latency, trace, and rollback evidence across multiple surfaces. No current promotion-cycle baseline, backlog, savings amount, missing control, or deployment defect is asserted.

**Value metric if measured:** median candidate-to-production promotion cycle time, from eval-ready candidate to human-approved production release. Baseline and target are intentionally blank until measured.

## ASSUMPTIONS

- Each gate has a predeclared threshold or policy owned by the team; this artifact does not invent thresholds.
- Evidence pointers refer to the exact candidate identity above.
- Human-only decisions and existing TRM authority boundaries remain unchanged.

## STRONGEST FALSIFIER

Kill this artifact as redundant if TRM already has a low-overhead, versioned promotion contract that binds held-out quality thresholds, credential/action policy, latency/cost evidence, trace completeness, explicit human approval, and rollback to the exact promoted agent/model/tool revision.

## Evidence links

1. https://jobs.ashbyhq.com/trm-labs/828b60b2-ac8f-407d-92a0-8b794c8cf391
2. https://www.trmlabs.com/trm-tech-blog/building-an-agentic-software-factory-how-trm-re-architected-engineering-for-ai-leverage
3. https://www.trmlabs.com/trm-tech-blog/ebpf-at-scale-how-trm-labs-modernized-its-observability-stack-with-groundcover
4. https://www.trmlabs.com/trm-tech-blog/never-give-an-ai-agent-a-credential-a-broker-and-the-process-we-trusted-to-build-one

## OPTIONAL_OPERATOR_REVIEWED_OUTREACH_NOTE — NO SEND

I saw the AI Agent Engineer role and TRM's public work on shared agent infrastructure, eval discipline, credential isolation, and human-owned decisions. I made a one-page candidate-bound promotion contract as a work sample: seven checks tying quality, authority, trace, and rollback evidence to the exact agent revision. It may be redundant with your internal process; if so, that itself is useful falsification.
