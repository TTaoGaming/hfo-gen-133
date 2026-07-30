# areas/ — ongoing responsibilities, no end state

An **area** is maintained, not completed. It has a standard to hold, not a
deadline. If it can be finished, it belongs in `projects/`.

| area | responsibility | standard to hold | state |
|---|---|---|---|
| `institution/` | the electronic institution: roles, norms, protocols, actors, virtual-actor stubs | every actor has a name, one chain, one effect ceiling, one refusal set | **design complete, 1 of ~14 actors live** |
| identity | souls, closest-continuer chain, seat integrity — legacy path `state/identity/` | every soul's `self_hash` reproduces from disk; supersede, never delete | ✅ gen-133 soul reproduces; ⛔ fails `HFO_SOUL_PHYLACTERY_v1_SPEC` |
| chains | append-only hash-chained receipts — legacy path `chains/` | one writer per file; every row carries receipt + honest_flaw | ⛔ **0 chain files at gen-133**; gen-132 chains READ-ONLY (kernel absent) |
| mesh | multi-provider / $0 vendor routing | cross-provider verify on every identity claim | ⛔ no non-Claude verifier appointed |
| world-effect ledger | `state/world/events/` | every world effect leaves an event row before and after | 2 event rows exist |

## Why `chains/` and `state/` are areas but live at legacy paths

Chain paths are load-bearing string literals — inside kernel guards, inside each
row's own `chain:` field, inside pointer packets in other generations. Moving them
would break readers this repo does not control. PARA is applied here as an
**overlay**, not a migration. See `resources/index.md`.

## The area whose standard is currently unmet

**chains.** There is no chain at gen-133 and no single-writer kernel to make one
safely. Until that exists, every claim in this forge is a document, not a receipt —
and the difference is the whole point of the machine.
