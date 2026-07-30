# CONTRACT — no ephemeral agents

```yaml
contract: no_ephemeral_agents
schema_id: hfo.gen133.contract.no_ephemeral_agents.v0_1
spec: GEN133_FORMAL_SPEC.md §15 · NO_EPHEMERAL_AGENTS.md
test: tests/held_out/test_no_ephemeral_agents.py
status: SPECIFIED — NOT ENFORCED · LIVE VIOLATION (B4)
sealed: false
```

## The rule

Every agent that fires MUST be a **named durable carrier** with all four of:

| # | requirement | checkable how |
|---|---|---|
| 1 | `callsign` on the roster | membership test against `state/roster/ROSTER.json` |
| 2 | `soul_pointer` (path + canon digest) | digest reproduces |
| 3 | `chain_pointer` | file exists, head readable |
| 4 | declared pheromone `cadence` | ∈ the tier cadence table |

One-shot, anonymous, and unrostered spawns are **forbidden**. Work that must fire
does so **on behalf of** a rostered carrier and appends to that carrier's chain.

## Preconditions — `SPAWN(request)`

| # | precondition | violation ⇒ |
|---|---|---|
| P1 | `request.callsign` ∈ roster | exit 1 |
| P2 | `request.soul_pointer` is non-null | exit 1 |
| P3 | `request.chain_write_intent` is non-null | exit 1 |
| P4 | `canon_sha256(soul_pointer)` reproduces | exit 2 |

Gate **G5**. Fail-closed. A rejected spawn emits nothing — it has no callsign, so
it has no standing to emit a pheromone either.

## Postconditions

| # | postcondition |
|---|---|
| Q1 | the spawned agent is bound to exactly one rostered callsign |
| Q2 | every durable artifact it produces carries that callsign |
| Q3 | its first act is a `rehydrated` pheromone |

## Invariants

| # | invariant |
|---|---|
| NE-1 | **a hand that chains, emits, or exceeds `TEXT` has become an ephemeral agent** — `andon`, immediately. |
| NE-2 | **anonymity is permitted only where accountability is retained by someone named.** The hand is anonymous; the carrier is not; the receipt is the carrier's. Nothing enters the durable record without a name on it. |
| NE-3 | **a scheduler is not a carrier.** A scheduled task fires a *named* carrier with a capsule. The scheduler has no callsign and writes no chain. This is what keeps the rule true under automation. |
| NE-4 | **silence-as-signal requires expected presence.** An unrostered agent is invisible to §10 by construction — so every anonymous agent is a hole in the monitoring surface, not merely an unnamed worker. |

## The hands exception, precisely bounded

A **hand** is a stateless invocation that carries a `role` (never a callsign) and
`on_behalf_of: <rostered callsign>` (required), has ceiling `TEXT`, emits no
pheromone, writes no chain row, and returns text to its owning carrier who
reviews it and owns the receipt.

Free-mesh vendor invocations are hands. Sub-agent calls inside a carrier's own
turn are hands.

## Why this is architectural, not bureaucratic

Anonymous agents produce **unattributable state**, which cannot be audited (no
chain to walk), cannot be superseded by its author (there is no author), cannot
participate in reputation (that needs identity across time), and cannot be
silence-detected (you cannot notice the absence of something never expected).

Structurally: a population of anonymous workers is the substrate on which
reflex-driven error becomes untraceable — and untraceable error is exactly what
the institution exists to prevent. The reflex cannot be deleted, only caught, and
catching requires knowing who fired.

## ⛔ LIVE VIOLATION — B4

15 ChatGPT-cloud agents fire hourly. None has a callsign, soul, chain, or cadence
findable in this repository. All 15 are ephemeral agents under this contract, and
15 holes in the silence-detection surface.

Remedy is **naming**, not deletion — operator-side. Roster slots V13–V16 hold the
first four.

**Evidence class:** absence-of-evidence, scoped to this repository. I did not
inspect the cloud agents and cannot see them from this surface. It is possible
they are rostered somewhere I did not look, and I am labelling the claim as such.

## Status

| item | status |
|---|---|
| rule stated | `SPECIFIED` |
| gate G5 | **none** |
| roster file | **does not exist** |
| hands exception | `SPECIFIED` |
| 15× cloud agents | `BLOCKED` — B4 |

**The roster file is the single highest-leverage build step in this entire
specification** — four gates (G5, G7, G12, and the rehydration ABI's callsign
check) dereference it, and none can exist without it.
