# PARKED — operator-minutes baseline instrumentation

```yaml
feature: operator_minutes_baseline
status: PARKED — UNDER_SPECIFIED · blocks the generation's own success claim
spec: GEN133_FORMAL_SPEC.md §1 · CANALIZATION.md §4
parked_by: SIGRÚN P4 · 2026-07-30
```

## Purpose

Count how many manual interventions the operator performs per day **today**,
before anything is built that claims to reduce them.

## Why this matters more than it looks

The stated liveness goal of gen-133 is *"removing me from manual cpr loops … near
-zero operator minutes for routine ops."*

**There is no baseline.** Nobody has counted today's operator minutes. Without
one, "near-zero" is unfalsifiable and every future claim of improvement is a
story rather than a result — which is precisely `L_BUDGET_WITHOUT_RECEIPT`: do not
size on heuristic; probe first, validate empirically, then scale.

This is the cheapest high-value action available in the entire specification and
it requires **no code, no gate, and no lease.**

## Method sketch

For one week, log a line per operator intervention:

```jsonc
{ "ts_utc": "…", "kind": "routine|decision",
  "what": "…one line…", "minutes": 3,
  "would_gen133_have_handled_it": true }
```

`kind` is the load-bearing field. `CANALIZATION.md` §3 splits the world into rows
where the operator **should** be paged (decisions, authorizations, namings,
irreversible effects) and rows where they should not (heartbeats, rollups, green
cycles). Only the second set is the target. **Decision minutes are the right
work and are not to be minimized.**

## Dependencies

None. This is the one item in `parking_lot/` with no blocker but the operator's
willingness to keep a tally for a week.

## When to revisit

**Now, or as close to now as the operator will tolerate.** Every day of building
before the baseline exists is a day of work whose value cannot afterwards be
demonstrated.

## Honest note

I am the one asking for this, and it costs the operator time to produce — which
is faintly absurd for a measure of *saving* operator time. It is still the right
call: a week of tallies buys the ability to ever say the rest worked.
