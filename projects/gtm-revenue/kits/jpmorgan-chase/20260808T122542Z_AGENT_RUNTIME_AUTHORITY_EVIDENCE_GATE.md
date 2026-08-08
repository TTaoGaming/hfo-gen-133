# Agent Runtime Authority & Evidence Gate
## Risk × Identity × Action × Evidence

**Plausible problem — hypothesis, not a JPMorganChase diagnosis:** when an agent revision is ready for production, reviewers may need to reconcile risk, delegated identity, tool/action authority, runtime controls, safety evidence, economic limits, audit evidence, human override, and rollback for the **same exact revision**. Public JPMorganChase material proves these control domains matter; it does **not** prove a backlog, missing control, or external buying need.

### WHY_THIS_MAY_MATTER

JPMorganChase says agent autonomy and controls should grow together, and separately emphasizes runtime authorization, traceability, stronger safeguards for higher-risk actions, and economic guardrails. A compact promotion contract is useful only if the decision currently requires assembling these facts across separate surfaces.

**Metric if tested:** median `eval-ready candidate → approved production release` cycle time. Baseline, target, savings, and headcount impact are **unknown**.

### HOW_TO_USE_IN_2_MINUTES

Write the exact agent/workflow revision, model route, prompt/config digest, tool-set digest, policy digest, and evidence-bundle digest. Mark each row `PASS | HOLD | N/A + reason`. `PROMOTE` only when every required row passes and the named human owner approves the exact evidence bundle. Any model/tool/policy change reopens affected gates.

> Illustrative control contract only; these are not claimed to be JPMorganChase's internal tiers or process.

| Gate | PASS when | HOLD when |
|---|---|---|
| **Exact revision** | Agent, model, prompts/config, tools, policy, and evidence identify one immutable candidate. | Any reviewed component changed or is ambiguous. |
| **Risk** | Named owner classifies data sensitivity, external authority, reversibility, and blast radius. | Higher-risk paths are unclassified. |
| **Delegated principal** | Each privileged action binds to an accountable principal, scope, and expiry. | Ambient/shared/stale authority. |
| **Allowed tools/data/actions** | Exact resources and action verbs are allowlisted. | Tool/data/action scope can widen without review. |
| **Runtime authorization** | Action-time decision checks principal + resource + action + current context/policy. | Build-time approval can bypass current denial. |
| **Economic guardrail** | Route has bounded cost/usage, escalation, and stop rules. | Silent retries/escalation or unbounded route drift. |
| **Held-out evidence** | Versioned task + safety tests bind to this exact candidate. | Dev examples only, mutable evals, or evidence from another revision. |
| **Trace/audit evidence** | Material actions reconstruct who/what acted under which policy/model/tools. | Missing or non-attributable action chain. |
| **Human stop** | Named role can pause/deny higher-risk actions before irreversible effect. | Approval is ceremonial or too late. |
| **Rollback/recovery** | Reversible effects have compensation; irreversible effects have a pre-action stop rule. | “Rollback” restores only the model, not external state. |

**Five negative controls:** expired delegation must fail closed; an added tool must invalidate promotion; a model/fallback change must reopen affected quality/cost/authority gates; budget breach must stop/escalate; one missing material trace record must fail the evidence gate.

### SOURCE-BACKED FACTS

- **2026-06-15:** JPMorganChase says agent autonomy and controls should grow together and highlights context, economic guardrails, disciplined governance, AI in workflows, and model-to-task balancing.
- **2026-03-23:** its agent-security guidance calls for runtime controls, delegated authority boundaries, identity/authorization, auditable actions, tamper-evident runtime records, and stronger safeguards for higher-risk operations.
- **2026-04-02:** JPMorganChase says its Fence framework performs use-case-specific synthetic guardrail testing for hallucination, topic drift, prompt injection, and related risks.
- **2026-07-02:** JPMorganChase says teams use AI for routine automation, cloud migrations, modernization/upgrades, and decision support.
- **Observed 2026-08-08:** JPMorganChase's Lori Beer page reports a $19.8B technology budget and approximately 65,000 technologists. This is scale evidence only.

### ASSUMPTIONS

The only wedge is that a candidate-bound cross-control gate **may** reduce review ambiguity if equivalent internal machinery is not already low-overhead. Public sources do not establish slow approvals, deficient controls, demand for outside help, or Pat Opet as a buyer.

### FALSIFIER

**Kill this wedge** if JPMorganChase already has a low-overhead internal release contract/control plane binding risk tier, delegated identity, per-action authorization, held-out quality/safety evidence, economic guardrails, tamper-evident records, human override, rollback, and the exact promoted agent/model/tool revision.

### Evidence links

https://www.jpmorganchase.com/about/technology/blog/key-takeaways-from-innovation-week-2026  
https://www.jpmorganchase.com/about/technology/blog/securing-agentic-ai  
https://www.jpmorganchase.com/about/technology/blog/fence-framework  
https://www.jpmorganchase.com/about/technology/blog/scaling-community-led-learning-at-enterprise-level-in-the-age-of-ai  
https://www.jpmorganchase.com/about/leadership/lori-beer

### Optional relationship note — `OPERATOR_REVIEWED_NO_SEND`

JPMorganChase's recent agent-security writing is unusually concrete about runtime authority, identity, traceability, safeguards, and economic guardrails. I turned those public principles into a one-page candidate-bound promotion gate. It may already be redundant with your internal control plane; if so, that is the strongest falsifier.

**Effect ceiling:** public-safe thought tool only; no audit, defect, compliance, incident, savings, deployment-outcome, or buying-intent claim.
