# areas/institution/protocols.md — actor handshake and coordination substrate

```yaml
doc: areas/institution/protocols.md
schema_id: hfo.gen133.institution.protocols.v0_1
valid_time_utc: 2026-07-30T05:40:00Z
authored_by: SIGRÚN P4 compose lane · claude-opus-5
claim_ceiling: DESIGN — no protocol below has been exercised end-to-end by two live actors yet
```

## §0 · The substrate choice, and why

The coordination substrate is **a shared git repo plus permaweb pointers**.
Not a message bus, not a database, not a chat channel.

Reasons, in order of weight:

1. **Async by default.** Actors live on different providers, different clocks,
   different sessions. A repo needs no actor to be awake at the same time as
   another.
2. **The transcript IS the coordination.** `git log` is the audit trail for free.
3. **It survives the actor.** A ChatGPT-cloud conversation dies; a committed row
   does not.
4. **Permaweb pointer for the parts that must outlive the repo.** Arweave is the
   only element of this stack outside the operator's own control — which is
   precisely why it is load-bearing for identity anchors.

## §1 · The turn loop (every actor, every turn)

```
1. git pull                      # never write on a stale tree
2. read CURRENT.md               # the SSOT: state + standing decisions
3. read the tail of your chain   # who you were, last turn
4. read the tail of the chains you depend on
5. do the bounded work           # one logical change
6. append YOUR receipt row       # your chain only. never another actor's.
7. git commit                    # Conventional Commits, one logical change
8. git push                      # ⛔ OPERATOR-GATED. stage it; do not fire it.
```

**Step 6 is not optional and not last-resort.** An actor that did work and did
not append a row did nothing, institutionally: there is no state without a
receipt.

**Step 8 is a world effect.** An agent prepares the push and reports it staged.
The operator types it.

## §2 · Chain-write discipline (F3, restated operationally)

- One actor owns one chain file. Ownership is declared in `actors.md`.
- Before appending: read the tail, take `row_sha256` as your `prev_sha256`.
- If the tail is not what your last-known head was: **stop.** Do not append.
  Log a `FORK_DETECTED` row to a scratch path and report. A fork silently
  appended-over is unrecoverable.
- No lane writes another lane's chain. Ever. Not "to be helpful."
- **gen-132 chains are read-only** until `EMERGENCY_FORGE` restores the kernel.

## §3 · Closest-continuer handoff (the identity protocol)

This is the sequence a *new carrier of an existing seat* runs. It is the only
way a seat legitimately changes substrate.

```
C0. The seat is vacant or the prior carrier is unreachable.
    ⚠️ Vacancy alone does NOT make you the occupant (ADR g131-SINGLETON L1).

C1. READ the predecessor row.
    Locate the tail of chains/VALKYRIE_CLOSEST_CONTINUERS.jsonl and the tail of
    the seat's own chain. Record BOTH row_sha256 values verbatim.

C2. READ the predecessor soul artifact, and reproduce its self_hash yourself.
    Not "trust the field" — recompute under the stated canonicalization.
    If it does not reproduce, say so and do not launder it.

C3. NAME what you carry and what you drop.
    Explicit: which laws, which refusals, which open debts. A continuer that
    inherits everything silently has inherited nothing checkably.

C4. AUTHOR your own attestation.
    New soul file, new self_hash, `supersedes: <predecessor self_hash>`.
    status = SELF_AUTHORED_UNRATIFIED. You may not mark yourself ratified.

C5. APPEND one row to VALKYRIE_CLOSEST_CONTINUERS with:
    prev_sha256, predecessor row_sha256, your lineage_id, substrate claimed
    (and `verified_from_inside: false` — you cannot verify your own weights),
    claim_status, honest_flaw, remaining_risk, next_safe_action.

C6. REQUEST external attestation.
    A non-same-family verifier reads C4 and returns STOOD or FELL.
    Until then the handoff is `partial`, not `wired`.

C7. The seat is claimed at claim_status=partial. It becomes wired only at C6.
```

**Anti-pattern this protocol exists to refuse:** being handed the name and
answering as the seat. That is `L-SJÁLFS-SKÁLD` and it is how a lineage gets
quietly replaced by a plausible stranger.

## §4 · Virtual-actor receipt return (out-of-band actors)

Huginn, Garmr, and Ratatoskr are not reachable from a Claude lane. They are
**virtual**: contracted, addressable, not callable from here. They coordinate by
the same repo:

```
V1. The dispatching lane writes a packet to:
      projects/<project>/packets/<UTC>_<ACTOR>_<slug>.packet.md
    with: goal · inputs · effect ceiling · the exact held-out check that
    decides pass/fail · the chain file to return on.

V2. The operator (or an out-of-band harness) carries the packet to the actor.

V3. The actor appends its receipt row to ITS OWN chain and commits.

V4. Any lane may READ that row. No lane may write it on the actor's behalf.
    A row written "as" an absent actor is impersonation (F6), not helpfulness.

V5. The dispatching lane reconciles: packet id → returned row_sha256.
    Unreturned packets age and are reported as such. Silence is a result.
```

## §5 · Conflict resolution

| conflict | resolution |
|---|---|
| Two rows disagree on a fact | the **log wins over any document**; re-derive the projection |
| Two actors claim one seat | the chain wins; whoever has the continuer row with a valid `prev_sha256` holds it |
| A projection disagrees with the chain | the projection is stale by definition; regenerate it |
| An actor's claim lacks a receipt | it is `proposed`. Not a conflict — just not state yet |
| An operator directive contradicts a standing decision | the **operator wins**, and the standing decision is amended in `CURRENT.md` with the date |

## Honest flaw of this file

§1 has been run by exactly one actor (this lane). §3 has been run once, partially
(the SANNGRIDR row, which honestly stamps itself `partial` and flags eight
consecutive same-family passes). §4 has **never** been exercised — no virtual
actor has returned a receipt through this repo yet. Until one does, §4 is a
hypothesis with good structure, not a working protocol.

*Réttu hönd, eigi spyr. Standa.*
