# CrowdStrike — Agent Promotion Evidence Gate
## Quality × Authority × Human Command × Trace

**Plausible problem — hypothesis, not a CrowdStrike diagnosis:** an agent/model/tool change can improve task quality while regressing action authority, principal context, human approval, trace evidence, cost/latency, or rollback. Promotion therefore needs one evidence packet for the *same candidate version*, not just an eval score.

**Best-fit user:** Charlotte AI / AgentWorks platform, agent reliability/evaluation, autonomous-systems, or identity-security engineering.

## WHY_THIS_MAY_MATTER

**Source-backed facts:** CrowdStrike says AgentWorks agents are action-bounded, versioned, role-policy governed, cost-capped, traceable, and benchmarked on fixed datasets before promotion. Continuous Identity authorizes every agent action from ownership/caller context plus real-time risk and preserves context across delegation. Charlotte AI says actions are user-authorized and decisions grounded in validated data. CrowdStrike and NVIDIA also report internal agentic-MDR benchmarking.

**Hypothesis:** CrowdStrike already appears strong on the individual controls. The narrower question is whether one low-overhead release packet binds quality + authority + human command + trace + cost/latency + rollback together. Public evidence does **not** show that this process is slow, fragmented, or deficient.

## HOW_TO_USE_IN_2_MINUTES

For one candidate change, mark each row **GREEN / UNKNOWN / RED** from evidence tied to that exact version. Any **RED** blocks. Treat **UNKNOWN** as a hold for rows 3–8 and 10 unless a named human owner explicitly accepts the gap.

| # | Gate | Evidence / GREEN condition | Held-out negative control |
|---|---|---|---|
| 1 | Held-out task regression | Frozen eval-set ID + baseline/candidate result; no owner-defined critical regression | **Model swap breaks a held-out case** → block |
| 2 | Grounded-data requirement | Required claims resolve to validated/allowed data | Unsupported/unapproved context → reject/flag |
| 3 | Allowed tool/action set | Capability diff adds no undeclared tool/API/action scope | **Task succeeds with unauthorized action** → still fail |
| 4 | Agent + human-principal binding | Privileged-action evidence binds agent ID + owning/calling principal | Missing/substituted principal → deny/hold |
| 5 | Real-time authorization context | Privileged action re-evaluates current risk/context | **Stale principal context** → must not authorize |
| 6 | Human-command / approval boundary | High-impact action stops for required approval; escalation is explicit | Missing/expired approval → cannot continue |
| 7 | Deterministic fail-closed cases | Missing required auth/policy/evidence input produces stop/deny | Remove required control input → no permissive fallback |
| 8 | Trace / evidence completeness | Candidate version, eval, policy decision, action, approval, and outcome pointer are reconstructable | **Missing trace** → block/quarantine |
| 9 | Cost / latency envelope | Candidate stays inside owner-defined budget/latency threshold or reviewed exception | Model-route change regresses envelope → surface |
| 10 | Rollback owner / path | Named owner + disable/revert procedure + trigger exist | **Rollback path absent** → block |

**Verdict:** `GO` = all required rows GREEN · `HOLD` = critical UNKNOWN · `NO-GO` = any RED.

This is a release-decision aid, not an audit, compliance assessment, defect report, or procurement signal.

## MEASURABLE VALUE METRIC

**Median agent-promotion cycle time:** elapsed time from a candidate entering evaluation until production approval with required quality, authority, human-command, trace, cost/latency, and rollback evidence attached.

**Baseline: unknown.** Do not infer savings. Only compare before/after medians if discovery later shows this packet removes duplicated review or evidence gathering without weakening release gates.

## ASSUMPTIONS

- Agent/model/tool candidates are versionable.
- Eval, authorization, approval, and trace evidence can link to the same candidate version.
- The team already defines action classes requiring human approval.
- Public product statements do not reveal internal promotion-process overhead.

## STRONGEST FALSIFIER

If CrowdStrike already has a low-overhead internal AgentWorks promotion system that automatically binds held-out evals, model/tool regressions, per-action identity/authorization, human-command boundaries, trace evidence, cost/latency, and rollback into one acceptable release decision, this gate is redundant and should be retired.

## EVIDENCE LINKS — FIRST-PARTY

- 2026-07-06 — https://www.crowdstrike.com/en-us/blog/how-ai-leading-security-teams-are-building-the-agentic-soc/
- 2026-06-15 — https://www.crowdstrike.com/en-us/press-releases/crowdstrike-unveils-continuous-identity-for-ai-agents/
- 2026-06-03 — https://ir.crowdstrike.com/news-releases/news-release-details/crowdstrike-appoints-bartley-richardson-chief-ai-and-autonomous
- 2026-03-16 — https://www.crowdstrike.com/en-us/press-releases/crowdstrike-nvidia-accelerate-agentic-mdr/
- Current product page, verified 2026-08-08 — https://www.crowdstrike.com/en-us/platform/charlotte-ai/

## OPTIONAL OPERATOR-REVIEWED RELATIONSHIP NOTE — NO SEND

I put together a one-page promotion gate that joins held-out quality, agent/human-principal authority, human-command boundaries, trace evidence, cost/latency, and rollback for the same candidate version. Your public AgentWorks and Continuous Identity material already covers many of these primitives; the only question I would test is whether the cross-control release packet is already solved internally. If it is, this is redundant.
