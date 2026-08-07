---
name: hfo-revenue-problem-discovery
version: 0.1.0
status: proposed
claim_ceiling: T0 research and conversation preparation only
send_authority: none
---

# Revenue Problem Discovery

## Trigger
Use when selecting a market, preparing a discovery conversation, or deciding whether a technical capability maps to an expensive business problem.

## Input
- one company/team/persona
- current public evidence or a warm-contact context
- operator capability evidence

## Procedure
1. Name the workflow before the technology.
2. Ask where headcount, cycle time, margin, risk, AI spend, error/rework, or revenue is materially affected.
3. Establish what is known versus hypothesized.
4. Ask for baseline: volume, time/case, error/rework, loaded labor, cost, loss, or conversion.
5. Define target condition and an unacceptable-failure condition.
6. Estimate value only from recipient/source-backed inputs.
7. Map at most two operator capabilities to the problem.
8. Propose the smallest reversible experiment with an acceptance metric.
9. Record falsifier and next learning action.

## Output
```yaml
workflow:
problem_signal:
baseline:
value_metric:
target_condition:
credible_annual_value:
capability_bridge:
smallest_experiment:
falsifier:
next_action:
claim_status: HYPOTHESIS|SOURCE_BACKED|DISCOVERY_VALIDATED
```

## Stop rules
- No invented pain.
- No pricing claim without baseline/value logic.
- No generic "AI transformation" as the problem.
- No outreach/send.

## Fitness
Qualified pain discovered; buyer consequence identified; external person confirms/contradicts the hypothesis.
