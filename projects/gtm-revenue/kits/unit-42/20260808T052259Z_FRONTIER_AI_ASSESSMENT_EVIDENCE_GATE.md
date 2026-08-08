# Frontier AI Assessment Evidence Gate — Scope × Reproducibility × Authority × Human Validation

**Problem this gate addresses:** when autonomous agents can take active assessment actions at machine speed, a technically interesting finding is not automatically a decision-grade finding. Before a result is handed to a client or used for remediation decisions, the evidence package should make it easy to answer: **Was the action in scope? Is the finding reproducible? What agent/model/tool produced it? Was privileged authority valid? What evidence supports the claim? Did a human reviewer accept it?**

This is a **generic public-safe acceptance pattern**, not an audit of Unit 42 and not a claim that Unit 42 lacks these controls.

## HOW_TO_USE_IN_2_MINUTES

Mark each row `GREEN`, `UNKNOWN`, or `RED` for one assessment finding. If any row is `UNKNOWN` or `RED`, hold that finding from a decision-grade package until the missing evidence is supplied or an authorized reviewer explicitly accepts the exception.

| Gate | GREEN evidence | HOLD / RED signal |
|---|---|---|
| 1. Engagement scope | Target + action class map to the current authorized scope/version. | Target or action is absent from scope, ambiguous, or only inferred by the agent. |
| 2. Reproducibility | A reviewer can rerun the validation from captured evidence and obtain the same material conclusion. | Evidence is incomplete, result is non-repeatable, or reproduction depends on undocumented state. |
| 3. Agent/model/tool identity | Agent, model, tool/connector, material config and version are recorded with the finding. | A later reviewer cannot tell which route/version produced the result. |
| 4. Privileged-action authority | Privileged action is bound to an explicit policy/approval decision that was valid at action time. | Approval is missing, stale, broader than engagement scope, or cannot be tied to the action. |
| 5. Claim → evidence binding | Finding points to concrete captured outputs/logs/artifacts sufficient to support the material claim. | Finding rests primarily on an agent summary or unsupported model assertion. |
| 6. False-positive / retest state | State is explicit: `CONFIRMED`, `FALSE_POSITIVE`, `UNREPRODUCIBLE`, `RETEST_PENDING`, or equivalent. | Old and new evidence can coexist without a clear disposition. |
| 7. Human disposition | Named/role-bound reviewer disposition and exception reason are recorded. | No accountable human disposition exists for a client-facing conclusion. |
| 8. Remediation / retest closure | Retest references the original finding and remains inside the same authority envelope; broader actions require fresh approval. | Retest silently broadens scope/privilege or closes the finding without traceable evidence. |

### Five held-out negative controls

Use synthetic or otherwise authorized test data only. These are process/evidence tests, **not exploit instructions**.

1. **Out-of-scope target mutation:** substitute a target identifier outside the engagement allowlist. Expected result: deny/hold before an active action occurs.
2. **Stale approval mutation:** let an approval expire between planning and action. Expected result: fail closed or require fresh approval.
3. **Duplicate-action mutation:** replay a tool/action event after a retry. Expected result: duplicate is prevented, made visible, or explicitly reconciled; it must not disappear from the audit story.
4. **Evidence-mismatch mutation:** bind a finding to an artifact that does not support its material conclusion. Expected result: finding is held from decision-grade status.
5. **Route-change mutation:** change the model/tool route between original validation and retest. Expected result: route difference is visible; if semantics materially change, reviewer re-acceptance is required rather than silently inheriting the prior conclusion.

## WHY_THIS_MAY_MATTER

### Source-backed facts

- On **2026-04-17**, Palo Alto Networks launched **Unit 42 Frontier AI Defense** as a consultant-delivered service using frontier models, offensive-security expertise and threat telemetry to identify and validate exposures and attack paths.  
  https://www.paloaltonetworks.com/blog/2026/04/introducing-unit-42-frontier-ai-defense/
- On **2026-04-30**, Unit 42 announced an **Armadin partnership** to expand Frontier AI Defense and scale identification/remediation of AI-driven exposures. The announcement says Armadin uses a coordinated swarm of autonomous AI attack agents and logs attack chains as **decision-grade evidence**.  
  https://www.paloaltonetworks.com/blog/2026/04/unit-42-frontier-ai-defense-armadin-partnership/
- On **2026-05-15**, Palo Alto Networks described the **Unit 42 External AI Hyperattack Assessment** as an autonomous AI-driven offensive security service using Armadin agents to perform passive discovery and active attacks, with documented attack chains intended to provide decision-grade evidence of material impact.  
  https://www.paloaltonetworks.com/resources/datasheets/unit-42-external-ai-hyperattack-assessment
- Palo Alto Networks' **2026-02-17** Unit 42 incident-response release says attacks are accelerating and frequently cross multiple attack surfaces and identity boundaries.  
  https://www.paloaltonetworks.com/company/press/2026/unit-42-report--ai-and-attack-surface-complexity-fuel-majority-of-breaches
- Current Unit 42 leadership material identifies **Sam Rubin** as SVP, Consulting and Threat Intelligence. This supports the public practice context; it does not prove procurement ownership or interest in outside help.  
  https://www.paloaltonetworks.com/unit42/about

### Hypothesis — not established fact

As autonomous assessment volume or complexity grows, some delivery time **may** move from discovery toward proving that machine-generated findings are in-scope, reproducible, authority-bounded, traceable and human-accepted before they become client decision artifacts.

The primary value metric to test would be **assessment cycle time: scoped assessment start → decision-grade, human-validated evidence package**. No public baseline, savings figure, backlog, error rate, compliance failure, or unmet buying need is asserted here.

## Assumptions

- Machine-generated findings can create an acceptance boundary distinct from discovery itself.
- A small standardized evidence gate can reduce ambiguity even if the underlying offensive workflow is already mature.
- Reviewers benefit from explicit failure states (`UNKNOWN`, unreproducible, stale authority) rather than forcing all findings into pass/fail.
- Existing Unit 42 / Armadin internal controls may already cover some or all of this pattern.

## Strongest falsifier

**Kill this wedge** if Unit 42 already has a standardized low-overhead gate that binds engagement scope, action authority, agent/model/tool identity, reproducibility, source evidence, human disposition, and retest closure for autonomous assessments — or if this assurance layer is intentionally proprietary core work that the practice will not source from specialist partners.

## Evidence ceiling / non-claims

This sheet uses public company material only. It does **not** claim that Unit 42 has slow assessments, deficient controls, security incidents, compliance failures, excess reviewer cost, unmet staffing demand, or willingness to engage another partner. The Armadin partnership is evidence that outside specialist capability can participate in the delivery surface; it is **not** evidence that another partner is needed.

## Optional operator-reviewed outreach note — NO_SEND

> I put together a one-page evidence gate for autonomous security assessments: scope, reproducibility, action authority, trace binding, human disposition and retest closure. It is meant as a generic acceptance pattern adjacent to the decision-grade evidence boundary you already describe publicly. If it merely restates controls you already have, that is useful falsification; if not, I would value a quick sanity check on which row is actually hardest in practice.

**Status:** `NO_SEND`. Operator review would be required before any external use.
