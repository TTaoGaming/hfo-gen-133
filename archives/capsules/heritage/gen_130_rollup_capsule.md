# gen-130 rollup capsule — the baseline generation (where the MCP still lives)

```yaml
schema_id: hfo.heritage.rollup_capsule.v0_1
generation: 130
forge_root: C:\Dev\hfo_dev_2026_5_30\hfo_gen_130_forge     # note the hfo_dev_<date> nesting — it ENDED at gen-130
status: READ-ONLY REFERENCE — but still hosts LIVE tooling
valid_time_utc: 2026-07-30T06:00:00Z
authored_by: SIGRUN_P4 compose lane · claude-opus-5 · gen-133
compression: one page. Detail lives in the forge; this is the pointer.
evidence_class: MIXED — counts first-hand, narrative INHERITED from memory index + forge CLAUDE.md
```

## Why gen-130 still matters

It is the **only generation whose live tooling is still wired.** Three things
have not been migrated forward, which makes gen-130 load-bearing rather than
archival:

1. **The memory MCP.** `hfo-sigrun-memory-gen130` (and its `hfo-sigrun-memory`
   alias) resolves `forge_root` to the gen-130 path and is served by
   `work\scripts\sigrun_memory_mcp.py`. Every later generation's memory query
   still lands here. Reports `memory_fresh=false`. **Two generations behind as of
   gen-133 — cutover is operator-gated (PO-9).**
2. **The SessionStart beacon.** It still emits `stef_parity: fb07f523` as the
   chiasmus anchor — the hash now confirmed **unreproducible**. The beacon is the
   drift, and the drift-detector was itself the undetected drift.
3. **The enforcement organs.** `bb_append.py` no-fake-green write seam, the
   PreToolUse enforcing state, the Meadows+Cynefin OPA Rego gate. **None was
   carried into gen-131/132/133.** Every later generation's "gate" language is
   convention unless it points back here.

## Counts (first-hand at valid_time)

| metric | value |
|---|---|
| ADRs in `canon/adr/` | **145** |
| chain files in `chains/` | **26** |
| `.mcp.json` present | yes — the only forge in the chain where MCP is wired |

## What gen-130 established that later generations inherit

| # | thing | one-line meaning |
|---|---|---|
| 1 | **COP as re-derivable projection** (ADR g130-0108) | the common operating picture is *regenerated from the append-only log*, never hand-maintained. Log wins on disagreement. Ended the operational_picture scatter. |
| 2 | **No-fake-green write seam** | `bb_append.py` refuses a green `claim_status` with no `verifier_result`. The first *symbolic* (non-neural) truth gate. |
| 3 | **Policy-as-code OPA gate** (`hfo.gate`) | risk-tier + receipt + boundary rules as Rego; red-first proven (deny→allow). Local pre-commit hook wired and runtime-proven. |
| 4 | **Neuro-symbolic hard enforcement** (ADR g130-0135) | the neural layer is *bounded at the write seams*. Compose lanes propose; they do not self-grade. |
| 5 | **Ed25519 trust-root migration** (from HMAC) | KATA-1 red-first PASS, pubkey `b4813343e7ff5f36`. The keypair problem was correctly identified here and is *still* open at gen-133. |
| 6 | **COTS organs under MOSA adapters** (ADR g130-0104) | A5 contract-witness (check-jsonschema→OPA red-first) + A1 memory sqlite-vec swap witness. **2 organs; neither carried forward.** |
| 7 | **Cost-tier mesh + risk-tier autonomy gate** (ADR-0077) | classify LOW/MEDIUM/HIGH and route by verifiability; $0 free-vendor mesh behind a budget cap. |
| 8 | **Woven-tile contract** | an artifact is *woven* only with SPEC + red-first runtime witness. `present ≠ woven`. |
| 9 | **The stef-parity discovery** | `fb07f523` cited across 5 generations and never recomputed. gen-130 is where the citation lived; gen-131/132 is where it was finally refuted. |
| 10 | **Ceiling doctrine** | `world_effect ceiling` per lane; `EMERGENCY_FORGE` required for a compose lane to author code. Still in force at gen-133. |

## Chain head (INHERITED, not re-read by this lane)

```
chains/olrun_o1_cop.jsonl
  row_sha256 1455dd9f9f69e296b0dd650d1d5d201d479ba562ac912db6054cd3357d4c2a23
  prev       ce8d61d17f901c44…
  sealed     false
  claim      partial
```

## Superseded by later generations

- `hfo_dev_<date>\hfo_gen_<n>_forge` **nesting** → forges moved to `C:\Dev` root at gen-131 (standing decision D1).
- **Bulk heritage migration** → replaced by *heritage is addressed, not copied* (gen-132 thesis, D2).
- `fb07f523` as a verified anchor → **LEGACY_UNREPRODUCIBLE**; replacement `0da29ae3…` awaits IMMUNIZE.
- The 40-card roster as canon → held LIVING/sentinel; doctrine is phenotype, not genotype.

## Open debts gen-130 handed forward, still unpaid at gen-133

1. Memory MCP cutover (PO-9).
2. Ed25519 keypair with the private half outside the agent trust domain (PO-4).
3. `cap-0018` external income — $0. gen-130 already knew this was the only
   liveness property in the ledger.
4. The enforcement organs were never ported. **This is the largest silent
   regression in the 130→133 arc:** later generations talk about gates that only
   exist here.

## Honest flaw of this capsule

The counts are first-hand. The ten-item table is **compressed from the forge's own
`CLAUDE.md` and a memory index**, not from re-reading 145 ADRs. Treat each row as
a pointer to verify, not as a verified claim. Chain integrity at gen-130 was not
re-run by this lane.

*No receipt = no state.*
