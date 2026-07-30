# CONTRACT — bitemporal rollup

```yaml
contract: bitemporal_rollup
schema_id: hfo.gen133.contract.bitemporal_rollup.v0_1
spec: GEN133_FORMAL_SPEC.md §5
test: tests/held_out/test_bitemporal_rollup.py
status: SPECIFIED — as-of query MISSING
sealed: false
```

## The two axes

| axis | meaning | set by | mutable |
|---|---|---|---|
| `valid_time_utc` | when the fact was **true in the world** | the carrier, from evidence | no |
| `transaction_time_utc` | when the fact was **recorded** | the writer, at persist | no |

The pair is what separates *"what did the fleet believe about X as of T?"* from
*"what was true about X at T?"* — and that separation is the entire reason a
carrier can reconstruct its own heritage and audit its own past errors rather
than merely re-reading its conclusions.

Both are UTC-Zulu. Always. Never local, never ambiguous.

## Schema

`hfo.gen133.rollup.v1` — see spec §5.2. Required: `songline`, `tier`, `window`,
`transaction_time_utc`, `as_of_query_key`, `source_rows{chain, first_row_sha256,
last_row_sha256, count}`, `counts`, `pheromones_emitted`, `cadence_compliance`,
`fitness`, `deltas`, `open_blockers`, the five receipt fields, `rollup_sha256`,
`prev_rollup_sha256`, `sealed`.

## Cadences

| tier | rollup cadence | window | rolls up from |
|---|---|---|---|
| valkyrie (16) | **hourly** | 1 h | own chain rows in the hour |
| apex (8) | **daily** | 24 h | own rows + its valkyries' 24 hourly rollups |
| world (1) | **hourly** | 1 h | 16 valkyrie hourly rollups + 8 most recent apex dailies + pheromone streams |

The world tier reads *hourly* from valkyries but *last-known* from apex, because
apex only produces daily. The world rollup therefore always carries
`apex_rollup_age_hours` per apex: 0–24 normal, >30 ⇒ apex silent.

## Preconditions — `ROLLUP(songline, window)`

| # | precondition |
|---|---|
| P1 | all source rows in `window` are readable and prev-link contiguous |
| P2 | for apex: all 24 child hourly rollups exist, or their absence is recorded as `cadence_compliance.missed` |
| P3 | `window.valid_time_end ≤ now` — no rollup over the future |
| P4 | the previous rollup's hash is readable (for `prev_rollup_sha256`) |

## Postconditions

| # | postcondition |
|---|---|
| Q1 | rollup appended to the rollup chain, prev-linked |
| Q2 | `rollup_sha256` reproduces under the canon rule |
| Q3 | recomputing from `source_rows` alone yields an identical rollup |
| Q4 | `cadence_compliance` reflects **observed** emissions, not expected ones |
| Q5 | a `rollup` pheromone is emitted carrying the digest |

## Invariants

| # | invariant |
|---|---|
| BT-1 | **rollups are chains too** — append-only, prev-linked. A rollup that can be rewritten is a summary, not a record. |
| BT-2 | **derivable.** Recomputation from `source_rows` must agree. On disagreement **the log wins** and the rollup is regenerated. Projections never outrank the log. |
| BT-3 | **no cross-tier fabrication.** An apex rollup reads only its own chain plus its valkyries' rollups. It never reaches past a tier. |
| BT-4 | **missing input is recorded, never interpolated.** A missing child rollup increments `missed`; it is not estimated, smoothed, or carried forward. |
| BT-5 | **`as_of_query_key` is stable** — `<callsign>@<ISO8601Z>` — so time-travel queries are reproducible across regenerations. |

## As-of query

```
hfo asof <songline> <ISO8601Z>     → the rollup the fleet would have produced as of that instant
hfo log  <songline>                → full transaction-time history
```

**⛔ NOT IMPLEMENTED.** gen-130 had a working equivalent
(`ssot_history_drain.py asof <doc_path> <ISO_UTC>` / `log <doc_path>`,
hash-chained SQLite). gen-133 has nothing. `TODO: port or re-specify.`

## Honest flaw

No rollup has been produced at gen-133, at any tier. BT-2's "recomputation must
agree" has never been exercised, so the schema's derivability is a design claim.
And the as-of query — which is the only reason to pay the cost of two time axes
in the first place — does not exist, which means the bitemporality is currently
overhead with no consumer.
