# CONTRACT — $0 free-vendor mesh adapter (LiteLLM)

```yaml
contract: free_mesh_adapter
schema_id: hfo.gen133.contract.free_mesh_adapter.v0_1
spec: GEN133_FORMAL_SPEC.md §14, §17
companion: contracts/free_mesh_harness.contract.md  (the BINDING; this is the WAKE)
status: SPECIFIED — apex surtr is ⛔ STUCK, blocker B5
sealed: false
```

## Substrate

| field | value |
|---|---|
| substrate | `free-vendor-mesh` |
| apex | **`surtr`** — Norse fire giant, mesh conductor — ⛔ **STUCK (B5)** |
| valkyries | 8, one per vendor family — **0 named** |
| families | groq · cerebras · sambanova · cohere · mistral · gemini · openrouter-primary · openrouter-secondary |
| routing | LiteLLM |
| ceiling | `TEXT` (hands) · `FILE` (the 8 family valkyries) |

Eight families — the roster now closes at 8, matching 8 valkyries.

## Job ABI

```jsonc
{ "schema_id": "hfo.gen133.free_mesh.job.v1",
  "role": "verifier",              // ROLE, never a callsign
  "objective": "…one bounded task…",
  "budget": 0,                     // MUST be exactly 0
  "allowed_vendors": ["groq","cerebras","sambanova","cohere",
                      "mistral","gemini","openrouter-primary","openrouter-secondary"],
  "review_gate": { "required": true, "reviewer_callsign": "…",
                   "reviewer_family_must_differ": true },
  "receipt_return": { "path": "…", "schema": "hfo.gen133.chain_row.v1",
                      "append_to_chain_of": "<rostered callsign>" },
  "on_behalf_of": "<rostered callsign>",   // REQUIRED
  "capsule": { "size": "S", "sha256": "…" },
  "effect_ceiling": "TEXT",
  "timeout_s": 300 }
```

## Wake mechanism

**Pull, not schedule.** The mesh has no clock — it is invoked. A family valkyrie
wakes on its own cadence, drains the job queue for its family, dispatches hands,
reviews, and writes one receipt row.

```
WAKE(family_valkyrie) →
  1. rehydrate (size S capsule)
  2. drain packets/inbox/mesh/<family>/*.json
  3. per job: verify budget==0, vendor ∈ allowlist, on_behalf_of ∈ roster  (G10)
  4. dispatch hand via LiteLLM → TEXT back
  5. cross-family review
  6. append ONE receipt row to on_behalf_of's chain
  7. emit heartbeat + receipt pheromones
  8. exit 0
```

## Invariants

Six Gleipnir threads, unchanged from `free_mesh_harness.contract.md`:
FM-1 budget exactly 0 · FM-2 hands not carriers · FM-3 ceiling `TEXT` ·
FM-4 cross-family review mandatory · FM-5 vendor allowlist fail-closed ·
FM-6 take what is given ≠ believe what is claimed.

Adapter-specific:

| # | invariant |
|---|---|
| FMA-1 | **LiteLLM is a router, not a carrier.** It has no callsign and writes nothing. |
| FMA-2 | a family valkyrie owns every receipt produced on its family. The family has a name; the individual call does not. |
| FMA-3 | vendor unreachable ⇒ `UNREACHABLE`, not `SILENT` (same rule as CC-4) |
| FMA-4 | **fail-closed on key absence.** No key ⇒ deny, never fall back to a paid path. This is the only edge where a $0 mesh could quietly become a spend. |

## ⛔ B5 — surtr is STUCK

The mesh apex is named and **not running**. Operator wants surtr unblocked; that
is the substrate's gating item and it is a first-class blocker in `AGENTS.md`.

Diagnosis I could **not** perform from this lane: I have not verified that
LiteLLM, any vendor key, or any mesh process exists on this host. "Stuck" is
operator-reported and I have no first-hand read of *how* it is stuck. Unblocking
starts with that diagnosis, not with code.

## Honest flaw

This adapter specifies the wake for a conductor that is not running, over a
router I have not confirmed is installed, against eight vendor families of which
zero have a named steward. Every invariant here is sound and none of it has been
exercised. The first real run may fail for a reason no assertion here covers:
no reachable vendors at all.
