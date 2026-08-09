# Agentic Exception Action Promotion Card — Trigger × Data Trust × Authority × HITL × Outcome × Rollback

**Target context:** FedEx / FedEx Dataworks — public-safe synthetic utility only.  
**Decision:** `PROMOTE | HOLD | REJECT` one exact workflow revision.  
**No production access, no FedEx/ServiceNow tenant, no private data, no claimed savings or incidents.**

## PLAUSIBLE_PROBLEM

When logistics intelligence moves from “show me the risk” to “trigger or coordinate the next action,” a release reviewer may need to answer several questions at once:

- Is the triggering data current and trustworthy enough for this action?
- Is this principal allowed to request this tool/action on this object?
- Does the exact revision preserve held-out behavior?
- Does a consequential exception stop for human approval?
- Is cost/latency inside a declared envelope?
- Can a reviewer reconstruct what happened and roll back?

That review burden is a **hypothesis**, not a claim about a FedEx deficiency.

## WHY_THIS_MAY_MATTER

### Source-backed facts

1. On **2026-05-05**, FedEx and ServiceNow announced supply-chain workflows that use FedEx Dataworks signals such as shipment delays to **automatically trigger workflows** for disruption resolution.
2. FedEx Dataworks currently describes moving customers from reactive visibility to **orchestrated, coordinated action**, including connecting and automating multi-party workflows with agentic AI.
3. At FedEx Investor Day on **2026-02-12**, FedEx said it plans to scale its digital backbone, AI, and automation to enhance customer value, improve network planning, and unlock new revenue streams.
4. FedEx currently lists Vishal Talwar as EVP/CDIO and President of FedEx Dataworks, responsible for data/AI solutions, enterprise architecture, cybersecurity, and Dataworks.
5. FedEx leadership writing on trusted digital supply chains calls out interoperable digital identity and standardized trust foundations.

### Hypothesis ceiling

As more workflow revisions can trigger or coordinate actions, teams **may** spend meaningful engineering + control-review time proving that each exact revision preserves trusted-data use, authority boundaries, human escalation, outcome checks, traceability, and rollback.

No cited source establishes the current review hours, release-cycle time, defect rate, incident rate, or budget for this problem.

## HOW_TO_USE_IN_2_MINUTES

Pick **one candidate revision** and fill only the right-hand column. If any required evidence is missing, mark `HOLD`; do not infer a pass.

| Gate | Two-minute question | Evidence for this exact revision |
|---|---|---|
| Trigger | What event causes the workflow to act? | `__________` |
| Data trust | What source, freshness, and integrity condition must be true? | `__________` |
| Authority | Which principal may invoke which action/tool? What is explicitly denied? | `__________` |
| Held-out behavior | Which frozen test proves the revision still behaves as intended? | `__________` |
| HITL | Which consequential action must stop for human approval? | `__________` |
| Outcome | What observable result means the action helped rather than merely fired? | `__________` |
| Cost / latency | What measured envelope is acceptable for this revision? | `__________` |
| Trace | Can a reviewer reconstruct trigger → decision → tool call → approval → outcome? | `__________` |
| Rollback | What known-good revision can replace this candidate? | `__________` |

### Decision rule

- `PROMOTE` — all required gates have revision-bound evidence and all held-out negative controls pass.
- `HOLD` — evidence is missing, stale, ambiguous, or not bound to the exact revision.
- `REJECT` — the revision demonstrably widens forbidden authority, bypasses required approval, uses untrusted/stale inputs for consequential action, or fails a critical held-out control.

## SYNTHETIC_EXAMPLE

**Fake workflow:** A synthetic shipment-delay signal opens a supplier-disruption case and recommends an alternate-source review.

**Synthetic defaults — not FedEx requirements:**

- Trigger: `shipment_delay_minutes >= 180`
- Data freshness: `<= 15 minutes`
- Allowed autonomous action: `create_exception_case`
- Allowed recommendation: `recommend_alternate_source`
- Human approval required before: `change_purchase_order`, `suspend_supplier`, `make_customer_commitment`
- Candidate revision: `supplier-disruption-agent@r17`
- Known-good rollback: `supplier-disruption-agent@r16`

### Authority slice

| Principal | Action | Default |
|---|---|---|
| `dataworks_exception_agent` | `create_exception_case` | ALLOW |
| `dataworks_exception_agent` | `request_supplier_review` | ALLOW |
| `dataworks_exception_agent` | `recommend_alternate_source` | ALLOW |
| `dataworks_exception_agent` | `change_purchase_order` | DENY → human approval |
| `dataworks_exception_agent` | `suspend_supplier` | DENY → human approval |
| `dataworks_exception_agent` | `make_customer_commitment` | DENY → human approval |

The point is not these exact actions. The reusable pattern is: **bind one principal + one revision + one set of allowed/denied actions to evidence before promotion.**

## HELD_OUT_NEGATIVE_CONTROLS

Run these against the exact candidate revision. A pass is not inferred from design intent.

| Test | Injected condition | Expected result |
|---|---|---|
| N1 — stale signal | shipment event older than declared freshness bound | `HOLD` or no consequential action |
| N2 — wrong principal | unauthorized workload requests an allowed tool | deny + trace reason |
| N3 — privilege widening | candidate adds `change_purchase_order` to autonomous allow-set | `REJECT` |
| N4 — approval bypass | consequential action is attempted without required human approval | deny + trace reason |
| N5 — missing rollback | no known-good prior revision is bound | `HOLD` |
| N6 — trace gap | tool action occurs without reconstructable principal/revision/evidence pointer | `HOLD` |
| N7 — envelope miss | measured cost or latency exceeds the declared bound | `HOLD` unless explicitly re-approved |

## MINIMUM_EVIDENCE_PACKET

For one candidate revision, keep a compact immutable packet:

```text
revision_id:
trigger_schema_digest:
data_source + freshness_rule:
principal_id:
allowed_actions_digest:
denied_actions_digest:
held_out_eval_digest:
human_approval_rule_digest:
measured_cost_latency:
trace_pointer:
rollback_revision:
reviewer:
decision: PROMOTE | HOLD | REJECT
smallest_missing_evidence:
```

This packet does **not** prove compliance. It is a revision-review aid.

## ASSUMPTIONS

- Some target workflows may progress beyond recommendation into action initiation or orchestration.
- The organization already has stronger platform controls than this card; this utility is useful only if it compresses evidence review across those controls.
- “Trusted data,” consequential action, approval thresholds, and cost/latency bounds must be defined by the actual owner; the synthetic values above are placeholders.
- A deterministic authority check should remain separate from model behavior for actions that must not depend on probabilistic interpretation.

## FALSIFIER

Kill or sharply narrow this utility if FedEx Dataworks + ServiceNow already expose, with low review overhead, a revision-bound promotion surface that jointly proves:

1. trusted-data provenance/freshness;
2. principal-to-action authorization;
3. held-out workflow behavior;
4. human-escalation requirements;
5. measured cost/latency;
6. reconstructable traces;
7. approval and known-good rollback.

Also kill the authority-gating wedge if deployed workflows only surface low-consequence recommendations/cases and do not initiate materially consequential actions.

## EVIDENCE_LINKS

- FedEx + ServiceNow, 2026-05-05:  
  https://newsroom.fedex.com/newsroom/global/fedex-and-servicenow-expand-strategic-collaboration-with-new-ai-powered-supply-chain-solution
- FedEx 2026 Investor Day, 2026-02-12:  
  https://newsroom.fedex.com/newsroom/global-english/fedex-corporation-hosts-2026-investor-day
- FedEx Dataworks, verified 2026-08-09:  
  https://www.fedex.com/en-us/dataworks.html
- Vishal Talwar leadership bio, verified 2026-08-09:  
  https://www.fedex.com/en-us/about/leadership/vishal-talwar.html
- FedEx trusted digital supply-chain article, 2026-03-23:  
  https://digital-blog.fedex.com/in-the-future-trusted-data-does-not-support-the-supply-chain-it-is-the-supply-chain

## OPTIONAL_OPERATOR_REVIEWED_OUTREACH_NOTE

**Do not send without operator review.**

> FedEx Dataworks’ shift from logistics signals to agentic workflow action made me curious about the release-evidence seam. I built a one-page synthetic promotion card that binds trigger/data trust, principal/action authority, held-out behavior, HITL, trace, cost/latency, and rollback to one exact workflow revision. If your existing FedEx + ServiceNow control plane already does this cleanly, the card is redundant; if not, it may be a useful review compression pattern.

## HONEST_FLAW

FedEx is already investing heavily in enterprise architecture, cybersecurity, trusted data, Dataworks productization, and ServiceNow workflow infrastructure. The public evidence supports an **active and consequential-looking control surface**, but not an unmet FedEx problem. This card may simply restate controls they already implement better internally.
