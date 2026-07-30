# PARKED — as-of bitemporal time-travel query

```yaml
feature: asof_time_travel_query
status: PARKED — precedent EXISTS at gen-130, unported
spec: GEN133_FORMAL_SPEC.md §5 · contracts/bitemporal_rollup.contract.md
parked_by: SIGRÚN P4 · 2026-07-30
```

## Purpose

```
hfo asof <songline> <ISO8601Z>   → the rollup the fleet would have produced as of that instant
hfo log  <songline>              → full transaction-time history
```

This is **the only consumer of bitemporality.** Two time axes cost something to
maintain, and the as-of query is what redeems the cost. Without it,
`valid_time` and `transaction_time` are overhead carried on faith.

It is also the mechanism behind the operator's stated goal — *"agents can
bitemporal crypto reconstruct their own heritage and strange loop quickly … like
giving them timelines they can verify."* A carrier cannot audit its own past
errors by re-reading its conclusions; it needs to ask what it *believed* at T
separately from what was *true* at T.

## Why parked

Not built at gen-133, and building it before any rollup exists would be building
a query with nothing to query.

## Precedent — this is a PORT, not an invention

gen-130 had a working implementation:

```
work/scripts/ssot_history_drain.py asof <doc_path> <ISO_UTC>
work/scripts/ssot_history_drain.py log  <doc_path>
```

backed by `state/ssot/ssot_history.sqlite`, hash-chained, drained automatically
every turn by `work/gates/behavioral_gate/ssot_inject.py`. That is real prior art
and it should be read before anything new is written.

## Dependencies

| # | dependency |
|---|---|
| 1 | ≥1 rollup exists (nothing to time-travel over today) |
| 2 | `as_of_query_key` convention stable — `<callsign>@<ISO8601Z>` (BT-5) |
| 3 | BT-2 derivability checker built first, so an as-of answer can be *recomputed* rather than trusted |
| 4 | code-authoring lease — this is executable work, routes to a code lane |

## When to revisit

After the first valkyrie hourly rollup lands. Build the derivability checker
(BT-2) **before** the query: a time-travel answer nobody can recompute is a
summary with a timestamp.
