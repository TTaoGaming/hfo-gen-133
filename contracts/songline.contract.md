# CONTRACT — songline

```yaml
contract: songline
schema_id: hfo.gen133.contract.songline.v0_1
spec: GEN133_FORMAL_SPEC.md §2
test: tests/held_out/test_songline_roster.py
status: SPECIFIED — NOT IMPLEMENTED
sealed: false
```

## Definition

```
songline := ⟨ callsign, tier, chain, soul, capsules, scratchpad, pheromone_stream, cadence ⟩
tier     ∈ { world, apex, valkyrie }
cadence  = hourly (world, valkyrie) | daily (apex)
```

A songline is the durable, append-only, hash-chained track of one lineage
through time. It survives its carrier.

## Preconditions — for any operation on a songline

| # | precondition |
|---|---|
| P1 | `callsign` is present in the roster (`state/roster/ROSTER.json`) |
| P2 | `chain` file exists and its head row hash is readable |
| P3 | `soul` pointer resolves and its `canon_sha256` reproduces |
| P4 | the acting carrier holds the single-writer lock for `chain` |
| P5 | `tier` ∈ {world, apex, valkyrie} and `cadence` matches the tier table |

## Postconditions — after an append

| # | postcondition |
|---|---|
| Q1 | exactly one new row exists at the tail |
| Q2 | `row.prev_sha256 == previous_head.row_sha256` |
| Q3 | `row.row_sha256` reproduces under the canon rule with the field placeholdered |
| Q4 | `row.claim_status == "proposed"` unless `row.verifier_result` is non-empty |
| Q5 | `row.callsign` is rostered (P1 re-checked at write time, not only at open) |
| Q6 | no prior row was modified or removed |
| Q7 | the lock is released |

## Invariants

| # | invariant | gate |
|---|---|---|
| SL-1 | **single writer** — exactly one carrier may append at a time; enforced by a lock, never by a session query | G3 |
| SL-2 | **append-only** — supersede, never delete | — |
| SL-3 | **prev-link contiguity** — `row[n].prev == row[n-1].hash` ∀ n>0; a break is a FORK and an ANDON | G2 |
| SL-4 | **bitemporal** — every row carries `valid_time_utc` + `transaction_time_utc`, UTC-Zulu | — |
| SL-5 | **receipt-or-proposed** — no `verifier_result` ⇒ `claim_status: proposed`; a green claim without a receipt exits 2 | G1 |
| SL-6 | **named carrier** — no anonymous rows | G5 |
| SL-7 | **the office outlives the occupant** — a dead carrier does not end a songline; a new carrier rehydrates and continues | — |

## Failure modes and required responses

| failure | response |
|---|---|
| lock unavailable | exit 0, emit `blocker` pheromone. **Never** append anyway. |
| prev-link break detected on read | emit `andon`, halt, do not append. Fork resolution is operator/verifier work. |
| roster lookup fails | exit 1 (`NO_EPHEMERAL_AGENTS` refusal) |
| soul digest does not reproduce | exit 2, fail-closed |
| green claim without receipt | exit 2 |

## Current violations

- **SL-1 is enforced by nothing.** No kernel, no lock file, no gate at gen-133.
  It held on 2026-07-30 only because two concurrent lanes happened not to write.
- **SL-3 is currently BROKEN for `SIGRUN_P4.jsonl`** — blocker B1, two divergent
  tails, fork point unlocated.
- **P1 cannot be evaluated** — the roster file does not exist.

## Honest flaw

Three of five preconditions reference artifacts that do not exist (roster, lock,
gen-133 chains). This contract is currently unsatisfiable end-to-end, which is
why its held-out test is red and must stay red until the roster lands.
