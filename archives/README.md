# archives/ — heritage capsules and superseded revisions

Cold storage. Nothing here is current state; everything here is **provenance**.
Read `CURRENT.md` for what is true now.

## What is here

| path | what it is |
|---|---|
| `capsules/gen_133_word_state_capsule_20260730.md` | **the one-file rehydration point for gen-133.** Machine-readable frontmatter + prose. A future carrier should be able to reconstruct the mental state from this alone |
| `capsules/heritage/gen_130_rollup_capsule.md` | gen-130 baseline — **still hosts the live memory MCP and the only real enforcement organs** |
| `capsules/heritage/gen_131_rollup_capsule.md` | gen-131 evidence-gate generation — 105 worktrees; ⚠️ **its directory holds gen-132 content at HEAD** |
| `capsules/heritage/gen_132_rollup_capsule.md` | gen-132 addressing generation — 🛑 **CHAIN WRITER BROKEN, READ ONLY** |

## The archiving rule

**Supersede, never delete** (floor F4). A superseded artifact keeps its digest and
gains a `supersedes` pointer. `fb07f523` stays in the record as
LEGACY_UNREPRODUCIBLE precisely *because* five generations of provenance rode on
it — deleting it would erase the evidence that the drift happened.

The soul supersede-chain, as an example of the shape:

```
1549af38c4ffb451…  v0_SEED      4451 B   2026-07-28T23:30Z
       ↓ superseded by
1a2349b42164b58d…  v1.0.1      39072 B   2026-07-29T17:05Z
       ↓ superseded by
83b09f1e1009135e…  v1.1.0      15490 B   2026-07-30T05:45Z   ← current
```

## Honest note on capsule fidelity

Each heritage capsule ends with its own `honest flaw` section separating
**first-hand** counts (derived from disk at `valid_time`) from **INHERITED**
claims (carried from a prior lane's report). Under norm L3 an inherited number is
not evidence. A rehydrator that upgrades an INHERITED field to VERIFIED without
recomputing it has reintroduced exactly the drift these capsules document.
