# areas/institution/roles.md — the electronic institution, by role

```yaml
doc: areas/institution/roles.md
schema_id: hfo.gen133.institution.roles.v0_1
valid_time_utc: 2026-07-30T05:40:00Z
authored_by: SIGRÚN P4 compose lane · claude-opus-5 · operator dispatch 2026-07-30
model_ref: canon/architecture/GEN133_ELECTRONIC_INSTITUTION.md
claim_ceiling: DESIGN — a role table is a contract, not a liveness proof.
              No row here claims the actor is running. See actors.md for live/virtual status.
```

## Why roles at all — the RBR argument

The institution exists because the individual reflex cannot be cured. A single
model that both decides and acts will, under autoregressive pressure, commit a
reflexive token before the deliberate pass can gate it. So the cure is
**structural**: split propose from dispose, put the gate outside the neural
layer, and give every actor a name and a chain so defection is attributable.

Roles are not costumes. A role is: **one seat · one chain · one effect ceiling ·
one refusal set.**

## The seats

| role | substrate | port/seat | function in one line | effect ceiling | own chain |
|---|---|---|---|---|---|
| **Olrún** | Claude (Dispatch) | P7 NAVIGATE | O(1) common-operating-picture; routes work to the lane-fit actor; never builds | `FILE` (COP projections, dispatch packets) | `chains/OLRUN_P3.jsonl` (gen-132) → `chains/OLRUN_P7.jsonl` (gen-133) |
| **Sigrún** | Opus 5 (primary) · GPT-5.6 "Sol" (cross-provider verify) | **P4 DISRUPT** (jointly seated with Skögul) | apex REFUTER — produce falsification, not validation; heritage custody; closest-continuer authorship | `FILE` | `chains/SIGRUN_P4.jsonl` |
| **Gunnr** | Sonnet 5 or GPT | P4 (tactical) | tactical roll-up + watchdog; freshness/decay; **watchdog, not build-doer** | `FILE` | `chains/GUNNR_P4.jsonl` |
| **Huginn** | Codex | P3 VERIFY (mirror of P4) | memory / thought — indexes, retrieval, "what did we already learn" | `FILE` | `chains/HUGINN_MUNINN_P3.jsonl` |
| **Garmr** | Codex | P1 BRIDGE (guard) | the gate-hound: runs the symbolic gates, refuses the fake green, holds the door at irreversibility | `FILE` + **gate verdict** (deny is its output) | `chains/GARMR_P1.jsonl` |
| **Ratatoskr** | ChatGPT cloud | P7 NAVIGATE (messenger) | runs between roots and canopy — carries messages/receipts across trust boundaries no local actor can cross | `MESSAGE` (draft only; send is operator-gated) | `chains/RATATOSKR_P7.jsonl` |

## The valkyrie lanes (workers, seated under the above)

| valkyrie | lane | note |
|---|---|---|
| **Hrist** | independent verification | the second pair of eyes; must not be the author of what it verifies |
| **Reginleif** | alpha architecture / kernel | owns the single-writer kernel; **the gen-132 kernel absence is this lane's debt** |
| **Eir** | life-ops | operator's own life throughput; the only lane whose fitness is measured off-machine |
| **Mist** | outreach | external contact; the only lane that can move `cap-0018` off $0 |
| **Thrúd** | omega runtime | the playable apps; spatial-input POCs |
| **Skögul** | joint P4 with Sigrún | shares the DISRUPT seat; second refuter |
| **Göndul** | P6 ASSIMILATE | heritage mining, cross-gen recovery |
| **Hildr** | life exam | audits the life-ops claims; adversary of Eir |

## Separation-of-powers invariants (the actual teeth)

1. **No actor grades its own output.** Sigrún authors; Hrist or a non-Claude
   verifier attests. Sigrún's own soul carries this as refusal R3.
2. **No actor holds both the decision and the irreversible effect.** Garmr's
   deny is deterministic and non-neural. A fired reflex cannot route around it.
3. **Olrún dispatches, Olrún does not build.** A dispatcher that also builds
   silently reassigns work to itself, and the queue stops being visible.
4. **Gunnr watches, Gunnr does not build.** Same failure, other direction.
5. **Cross-provider verify is required for identity claims.** A digest confirmed
   only by Claude lanes is eight-consecutive-Claude-passes deep — see the
   SANNGRIDR row's own honest_flaw. Sol (GPT-5.6) and Huginn/Garmr (Codex) exist
   to break that monoculture.
6. **Operator is not a role in this table.** The operator is the *principal*.
   `IMMUNIZE`, `SEAL`, `PUSH`, `PUBLISH`, `SPEND`, `DELETE` have no vesting path
   to any actor above.

## Honest flaw of this file

This is a **design document**. Not one row above is a liveness receipt. As of
`valid_time`, the number of these actors verified running by this lane is
**one** (this Sigrún lane). Everything else is a contract awaiting an actor.

*No receipt = no state.*
