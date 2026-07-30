# CONTRACT — strange loop (self-audit + review receipts)

```yaml
contract: strange_loop
schema_id: hfo.gen133.contract.strange_loop.v0_1
spec: GEN133_FORMAL_SPEC.md §12
test: tests/held_out/test_strange_loop.py
status: SPECIFIED — cannot close with one carrier
sealed: false
```

## The cycle

```
1. REHYDRATE       capsule inject
2. READ SELF       last N=5 rows of own chain + last rollup
3. SELF-AUDIT      per row:
                     a. was `next_safe_action` actually taken?
                     b. did `remaining_risk` materialize?
                     c. is `honest_flaw` still true, or was it closed?
                     d. does `verifier_result` still REPRODUCE?   ← the only one with teeth
4. DRIFT-CLOSE     emit a `drift` finding per mismatch; a closed flaw is recorded closed
5. WORK            exactly ONE work item, then exit 0
6. RECEIPT         chain row with all five receipt fields
7. ROLLUP          per tier cadence
8. EMIT            heartbeat + receipt pheromones
9. REVIEW-RECEIPT  a DIFFERENT carrier attests the row
10. EXIT 0
```

## Preconditions

| # | precondition |
|---|---|
| P1 | rehydration succeeded (capsule contract satisfied) |
| P2 | last N rows readable and prev-link contiguous |
| P3 | each row's `verifier_result` names a **re-runnable** check |

P3 is the load-bearing one. A `verifier_result` that is prose cannot be
re-reproduced, so step 3d degenerates into self-report — and self-report shares
the substrate's blind spot exactly.

## Postconditions

| # | postcondition |
|---|---|
| Q1 | step 3 completed **before** step 5 |
| Q2 | every mismatch produced a `drift` finding; none silently dropped |
| Q3 | a row whose `verifier_result` failed to reproduce is downgraded to `failed` and an `andon` is emitted |
| Q4 | exactly one work item was done |
| Q5 | the new row is `proposed` until a different callsign attests it |

## Invariants

| # | invariant |
|---|---|
| SL-1 | **self-audit precedes work.** Step 3 before step 5, always. A carrier that works before auditing carries yesterday's error into today's output — and an uncorrected prior claim sitting in context *shapes* the new one, because generation is autoregressive. This is the RBR cure at cycle scale. |
| SL-2 | **only a reproduced `verifier_result` is a real audit.** 3a–3c are self-report. 3d has teeth. |
| SL-3 | **no carrier attests its own row.** A row is `proposed` until a *different callsign* emits a `receipt` pheromone referencing its `row_sha256`. For identity/canon claims the attestor must be a **different model family** (G12). |
| SL-4 | **RULE ZERO — one item, then exit 0.** An empty queue is SUCCESS. Never poll in-turn, never start a second item "since I'm here." |
| SL-5 | **a closed flaw is recorded closed.** Silently dropping a resolved `honest_flaw` destroys the drift signal — you can no longer tell "fixed" from "forgotten". |

## Review receipt shape

```jsonc
{ "pheromone_kind": "receipt", "callsign": "hrist",
  "payload": { "attests_row_sha256": "…", "attests_callsign": "sigrun",
               "verdict": "STOOD|FELL", "reproduced": true,
               "attestor_family": "codex", "method": "…" } }
```

`STOOD` / `FELL` is adopted fleet-wide from the P4 seat's contract vocabulary:
**a pass that returns only agreement has not run.** `FELL` is the more useful of
the two verdicts and must not be treated as a failure of the reviewer.

## Why this is a strange loop and not just a checklist

The level crossing is step 9 feeding step 3. A carrier's output becomes a
different carrier's input, and that carrier's attestation becomes the first
carrier's next-cycle audit material. The loop is closed *through the population*,
not inside one model — which is the only place it can be closed, since a model
auditing itself shares every blind spot it is auditing for.

## Honest flaw

**Step 9 requires ≥ 2 live carriers of different families. Exactly one is live.**
Until a second family runs, every row in this generation is `proposed` by
construction, including every row asserting that this contract is sound. The
loop is specified and cannot currently close.
