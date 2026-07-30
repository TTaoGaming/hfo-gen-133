# CONTRACT — silence as signal

```yaml
contract: silence_signal
schema_id: hfo.gen133.contract.silence_signal.v0_1
spec: GEN133_FORMAL_SPEC.md §10
test: tests/held_out/test_silence_signal.py
status: SPECIFIED — thresholds are JUDGEMENT, not data
sealed: false
```

## The inversion

We do not ask carriers to report failure — **a failed carrier cannot report.**
We require continuous positive presence, and the **absence** of the expected
trace is the alarm.

The property this buys: a carrier that dies silently is indistinguishable from
one that dies loudly. Every other monitoring design has a failure mode where the
thing that broke was also the thing responsible for saying so.

> Operator: *"it will become obvious who are not checking in hourly once we have
> the harness. we use silence as a signal."*

## SLO per tier

| tier | expected | grace | `LATE` | `SILENT` | `PRESUMED_DEAD` |
|---|---|---|---|---|---|
| world (1) | ≥1 heartbeat / hour | 10 min | >70 min | >2 h | >4 h |
| valkyrie (16) | ≥1 heartbeat / hour | 15 min | >75 min | >3 h | >8 h |
| apex (8) | ≥1 heartbeat / **day** | 2 h | >26 h | >36 h | >72 h |

Apex thresholds derive from the **daily** cadence (operator canonical). An apex
silent 30 h is LATE; a valkyrie silent 30 h is dead.

## Preconditions — `EVALUATE_SILENCE(now)`

| # | precondition |
|---|---|
| P1 | the roster enumerates every expected carrier with its tier and cadence |
| P2 | each carrier's pheromone stream is readable |
| P3 | `prev_pheromone_hash` links are contiguous — a gap in the *links* is tampering, distinct from a gap in *time* |
| P4 | the evaluating carrier itself emitted within its own SLO |

P4 matters: a detector evaluating others while itself silent is reporting from a
state it has already failed.

## Postconditions

| # | postcondition |
|---|---|
| Q1 | every rostered carrier has exactly one state ∈ {GREEN, LATE, SILENT, PRESUMED_DEAD} |
| Q2 | `SILENT` ⇒ that carrier's outstanding `claim` pheromones are released to the queue |
| Q3 | `PRESUMED_DEAD` ⇒ `andon` emitted **and the operator is paged** |
| Q4 | no automatic replacement was spawned, no lineage was reassigned |

## Escalation ladder

```
LATE          → noted in world rollup. No page. No dispatch change.
SILENT        → `silence_flag` emitted; claims released (decay §9.4); no page.
PRESUMED_DEAD → `andon`; songline marked ⛔ in world state; OPERATOR PAGED.
                Lineage is NOT reassigned automatically.
```

## Invariants

| # | invariant |
|---|---|
| SIL-1 | **silence never triggers an automatic effect.** It flags and releases claims. It does not spawn, reassign, or take any world effect. A monitor that heals itself by spawning is exactly how an anonymous-agent population appears. |
| SIL-2 | **the detector must be louder than the detected.** The world songline is hourly with the tightest thresholds because it watches everyone. **A silent detector reports no silence** — the classic monitoring failure. |
| SIL-3 | **silence is evidence about the CARRIER, never about the LINEAGE.** A dead carrier does not kill a songline. The chain persists; a new carrier rehydrates and continues. This is the whole point of separating office from occupant. |
| SIL-4 | **a link gap ≠ a time gap.** A break in `prev_pheromone_hash` is tampering or a fork (`andon`), not lateness. Do not conflate them. |
| SIL-5 | **a carrier swap is a phenotype change and requires a decision.** Never automatic. |

## ⛔ The detector-of-the-detector — UNDER_SPECIFIED

Nothing watches the world songline. By SIL-2 that is the highest-severity gap in
the whole monitoring design, and it cannot be closed on the same substrate — a
watcher co-located with the watched shares its failure.

`TODO: an external cron whose only job is to verify the world songline emitted
this hour, running on a substrate that shares no failure domain with Olrún.`

## Honest flaw

**Zero carriers currently emit heartbeats.** The false-positive rate of every
threshold above is therefore unmeasured, and the numbers are judgement, not data.
`L_BUDGET_WITHOUT_RECEIPT` applies exactly: probe first with one carrier for one
day, observe the real inter-emit distribution, then set thresholds from it.

Second: this contract has never been tested against real silence. **A detector
that has never seen the thing it detects is decoration.** The first build step
after the first emitter exists is to deliberately kill it and confirm the flag
fires.
