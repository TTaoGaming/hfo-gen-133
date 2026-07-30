# CONTRACT — Codex desktop adapter

```yaml
contract: codex_adapter
schema_id: hfo.gen133.contract.codex_adapter.v0_1
spec: GEN133_FORMAL_SPEC.md §11, §19
status: SPECIFIED — build target for the parallel sonnet-5 builder lane
sealed: false
```

## Substrate

| field | value |
|---|---|
| substrate | `codex` (OpenAI.Codex bundle, laptop) |
| apex threads | `garmr` · `huginn` (+Muninn) · `sigrun_codex_gpt5.6sol` |
| wake | Codex scheduled automations + persistent threads |
| ceiling | `FILE` |
| ⭐ | **the cross-family verifier substrate** — G12 cannot be satisfied without it |

**Proven capability (operator-confirmed 2026-07-30): Codex sustained a 9h+ goal
loop.** Long-running loops are viable here. This is the only substrate for which
that is demonstrated, and it should carry the work that needs continuity rather
than the work that needs bursts.

## Existing scheduled tasks — REFERENCE ONLY, do not re-spec

| task | note |
|---|---|
| Garmr [4,1] heartbeat | exists |
| Huginn_Muninn anti-CPR, WIP=1 | exists |
| Sigrun-Gen133 anti-CPR delivery | exists — the sibling thread, see `CODEX_SIBLING_RECONCILIATION.md` |
| Eir P5 safety watch | exists |
| Gen131 audit | exists |
| Gunnr lease review | exists |

These are live. Reference them; do not duplicate them into new schedules.

## Operations

### `WAKE(callsign, capsule)`

```
pre:   callsign ∈ {garmr, huginn, sigrun_codex_gpt5.6sol, ...} ∩ roster
do:    file-drop a job packet at packets/inbox/<callsign>/<ts>.json
       (Codex scheduled task picks it up on its next tick)
       OR post to Slack -- Codex CAN post; Claude lanes cannot
post:  `dispatch` pheromone recorded
```

**Invariant CX-1 (file-drop is the primary channel).** Codex reads the repo
directly. A file drop is a `FILE`-ceiling write, needs no bot identity, and is
not subject to B3. Slack is the secondary channel and is a genuine capability
here — Codex is the *only* substrate that can currently post.

### `ACK(dispatch_hash)`

Codex acks by **appending a chain row** to its own carrier chain referencing
`dispatch_hash` — the strongest ack in the fleet, because it is a hash-linked
durable write rather than a transcription.

### `VERIFY(row_sha256)` — the one that matters

```
pre:   the row's author family ≠ codex
do:    re-run the row's verifier_result; compare
post:  emit `receipt` pheromone with verdict STOOD|FELL, attestor_family=codex
```

This closes G12 and the §12 strange loop. **Until a Codex carrier does this,
every row in gen-133 is `proposed` by construction** — including the specs that
say so.

## Invariants

| # | invariant |
|---|---|
| CX-1 | file-drop primary, Slack secondary |
| CX-2 | ack is a chain row, not prose |
| CX-3 | **Codex is the attestor of record for cross-family verification** |
| CX-4 | multiple apex threads per substrate are legal here — this amends SR-1 ("one apex per substrate"), on operator canon |
| CX-5 | long-running loops permitted on this substrate only, on the 9h+ receipt; every other substrate keeps RULE ZERO one-item-then-exit |

## Honest flaw

CX-5 sits in real tension with RULE ZERO. A 9-hour loop is not "one work item,
then exit 0", and I have not specified how a long-running Codex thread stays
inside the job-not-daemon discipline. `TODO: define the checkpoint cadence at
which a long loop writes a row and re-reads its own state, so it is a sequence of
jobs rather than a daemon.` **`UNDER_SPECIFIED`.**
