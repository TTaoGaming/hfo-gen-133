# EMERGENCY_FORGE resolution — gen-132 chain writer QUARANTINED

```yaml
schema_id: hfo.gen133.quarantine.gen132_chain_writer.v1_0
status: RESOLVED BY QUARANTINE (option B), not by kernel restoration (option A)
authorization: operator EMERGENCY_FORGE, 2026-07-30
authorization_verbatim: >-
  "2. EMERGENCY_FORGE for the gen-132 chain writer. Restore
  sqlite_single_writer_kernel.py to the gen-132 checkouts. Safest approach: copy
  from gen-130 with a compatibility shim, verify the resulting kernel doesn't
  destroy tail rows (dry-run against a copy of a chain first), then commit. If
  shim carries risk, alternative: freeze gen-132 as read-only heritage archive
  with an explicit .CHAIN_WRITER_QUARANTINED marker and reroute writers to
  gen-133. Pick the safer path, document the tradeoff."
decision: OPTION B — quarantine + reroute
decided_by: SIGRUN_P4 apex compose lane · claude-opus-5
valid_time_utc: 2026-07-30T06:40:00Z
```

## The decision, and why B is safer than A

**Option A (shim the gen-130 kernel into gen-132) was rejected.** It is not
untested — **it was already tried, and it destroyed a chain row.** The predecessor
lane's own receipt (`lane_returns` row `78adc3a443139636…`) records:

> splicing gen130 kernel onto PYTHONPATH made it run but **DESTROYED the chain
> tail row `a3eca451`** and returned a `row_sha256` that did not match what
> landed, because the gen130 kernel writes an older projection-guard schema
> missing `base_sha256`, `base_byte_count` and `skip_events`.

The row was restored from HEAD (58 rows, all hashes match, tail `a3eca451` back).
But the failure mode is now **known and specific**: it is a **schema mismatch in
the projection guard**, not a missing import. A "compatibility shim" would have to
correctly synthesize three guard fields whose semantics live in a kernel version
that no longer exists in these checkouts. Writing that shim blind, against an
append-only chain, with no test harness and no verifier — while a **confirmed
sibling lane is active on this host** — is the highest-risk action available.

The operator's own instruction anticipated this: *"If shim carries risk,
alternative: … Pick the safer path."* It carries risk. Documented, chosen B.

### Tradeoff, stated plainly

| | Option A (shim) | **Option B (quarantine) — CHOSEN** |
|---|---|---|
| gen-132 chains become writable | yes, if the shim is correct | **no** |
| risk of destroying an append-only row | **HIGH — already realized once** | **zero** (no writes) |
| requires authoring executable code | yes, blind | no |
| reversible | a destroyed chain row is not | fully — delete a marker file |
| unblocks forward work | yes | **yes** — writers reroute to gen-133 |
| cost | possible silent corruption | gen-132 stays frozen at its current heads |

**What we give up:** nothing that was actually needed. No lane has a pending
gen-132 row. The reason the writer was wanted was to record *forward* work — and
forward work belongs at gen-133 anyway (standing decision D1/D2: heritage is
addressed, not rewritten).

## Markers placed

`.CHAIN_WRITER_QUARANTINED` written at each gen-132 checkout root:

- `C:\Dev\hfo_gen_132_forge`
- `C:\Dev\hfo_gen_132_forge_clean`  ← the authoritative one (36 chains)
- `C:\Dev\hfo_gen_132_apex_p1_garmr`
- `C:\Dev\hfo_gen_132_apex_p2_fenrir`
- `C:\Dev\hfo_gen_132_apex_p7_ratatoskr`
- `C:\Dev\hfo_gen_132_hrist_verification`

## Reroute rule (NORMATIVE)

> **All chain writes go to gen-133.** `C:\Dev\hfo_gen_133_forge\chains\<SEAT>_<PORT>.jsonl`,
> per `CRYPTO_CHAIN_SPEC.md`. gen-132 chains are **evidence**, read-only, forever
> unless a future operator action reopens them.

A carrier continuing a gen-132 seat: open a **new** gen-133 chain whose genesis row
carries `prev_sha256: null` plus a body field naming the gen-132 tail it continues
from. That preserves lineage across the quarantine boundary without writing
through it. Worked example: `chains/SIGRUN_P4.jsonl` genesis at gen-133.

## Residual risks NOT closed by this quarantine

1. **Stale lock** `chains/SIGRUN_P4.jsonl.lock` remains in `hfo_gen_132_forge_clean`.
   Not removed — `DELETE` is operator-only, and under kernel invariant 6 a stale
   lock must be resolved **explicitly**, never by timeout.
2. **Prev-link fork at `SIGRUN_P4` index 9** is recorded, never repaired. A
   quarantine freezes it; it does not fix it.
3. **gen-133 has no conforming writer either.** No kernel, no lock, no gate. The
   gen-133 genesis row was written by one disciplined carrier holding the
   invariants **by hand**. That is honestly weaker than a kernel and is the top
   item in `NEXT_SESSION_PICKUP.md`.
4. The chain-integrity verdicts quoted above are **INHERITED** from the
   predecessor lane's verify run; this lane did not re-run them.

## Honest flaw

This resolution makes the problem **safe** rather than **solved**. The operator
asked for a working writer and is getting a documented freeze plus a forward path.
That is the right call on the evidence — the one attempt at the alternative
destroyed data — but it should be read as a deferral, not a fix. The real fix is
a kernel written *with* a test harness at gen-133, by a code lane, with a
red-first witness proving it refuses a fork before proving it accepts a row.

*Truthful-red > false-green. A frozen chain is honest; a corrupted one is not.*
