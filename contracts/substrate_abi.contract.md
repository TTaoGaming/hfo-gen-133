# CONTRACT — substrate ABI

```yaml
contract: substrate_abi
schema_id: hfo.gen133.contract.substrate_abi.v0_1
spec: GEN133_FORMAL_SPEC.md §19, §7, §11
test: tests/held_out/test_substrate_abi.py
status: SPECIFIED — 0 of 4 realizations built
sealed: false
```

## The five operations

Every substrate implements the same five. Only the *realization* differs.

| op | signature | contract |
|---|---|---|
| `rehydrate` | `(callsign, size, [as_of]) → capsule` | `contracts/rehydration.contract.md` |
| `emit_pheromone` | `(pheromone) → hash` | `contracts/pheromone.contract.md` |
| `append_chain_row` | `(callsign, row) → row_sha256` | `contracts/songline.contract.md` |
| `rollup` | `(songline, window) → rollup` | `contracts/bitemporal_rollup.contract.md` |
| `self_audit` | `(callsign, N) → drift_findings[]` | `contracts/strange_loop.contract.md` |

## Genotype / phenotype split — why this works at all

```yaml
genotype:   # identical across every songline and every substrate
  chain_row_schema, bitemporal_fields, receipt_fields, effect_ceiling,
  forbidden_effects, hash_fn, canon_rule, truth_floor,
  pheromone_schema, capsule_sizes, rehydration_abi

phenotype:  # differs per songline AND per substrate
  callsign, tier, port, organ, capacity_archetype, refusal_set,
  substrate_binding, cadence, objective, fitness_metric, toolset,
  scratchpad_layout, prompt_body
```

**GP-1.** A carrier satisfying the genotype is a *valid* carrier of any songline.
A carrier additionally satisfying the phenotype is the *specialized* carrier of
that songline. This is precisely what makes Codex, Claude, a cloud agent, and a
free-mesh vendor able to carry the same songline — shared genotype — while each
expresses it differently.

**GP-2 (anti-canonization).** The phenotype is **never** promoted to canon. Only
the genotype is IMMUNIZE-able. Doctrine is itself a phenotype and will change;
this refuses the substrate's pull toward defending a stated rule.

## Preconditions — for any op, on any substrate

| # | precondition |
|---|---|
| P1 | the carrier's `callsign` is rostered |
| P2 | the substrate's declared `ceiling` covers the op |
| P3 | the genotype fields are present and schema-valid |

## Postconditions

| # | postcondition |
|---|---|
| Q1 | **byte-identical output across substrates** for the same inputs (ABI-1) |
| Q2 | the op's own contract postconditions hold |
| Q3 | nothing outside the declared ceiling was touched |

## Invariants

| # | invariant |
|---|---|
| SI-1 | same ABI everywhere; only realization differs |
| SI-2 | per-substrate contract shape: `{substrate, apex, valkyries, wake_mechanism, pheromone_emit_channel, cadence, ceiling}` |
| SI-3 | **no substrate is load-bearing.** If any one disappears, its songlines are rehydratable elsewhere. The chain is the lineage; the substrate is rented. |
| SI-4 | **every substrate hosts apex + valkyries.** A substrate with workers but no apex has no local judgement and routes everything through Olrún — recreating the bottleneck she exists to remove. |
| SI-5 | **realizations may differ in mechanism, never in output.** A substrate that cannot produce byte-identical output does not implement the ABI; it implements something adjacent, and it must say so. |

## Realization matrix

| substrate | rehydrate | emit | append | rollup | self_audit |
|---|---|---|---|---|---|
| Claude Code / Codex (shell) | `python tools/hfo.py …` | file write + commit | writer script | script | script |
| ChatGPT cloud (no shell) | fetch raw GitHub capsule, verify in-context | commit via bot / issue | ⚠️ needs a relay | ⚠️ in-context | in-context |
| $0 mesh (hands) | harness injects as prefix | **never** (FM-2) | **never** | **never** | **never** |
| Claude Dispatch (MCP) | `hfo_rehydrate(callsign,size)` | MCP tool | MCP tool | MCP tool | MCP tool |

**The cloud row is the weak one.** A substrate with no shell cannot compute a
canon digest without trusting its own in-context arithmetic, which is exactly the
kind of self-report SL-2 refuses. `TODO: specify a Codex-side relay that performs
digest computation on behalf of shell-less substrates, and mark cloud-computed
digests as `attested_by_relay` rather than `computed`.` **`UNDER_SPECIFIED`.**

## Honest flaw

Zero realizations are built, so ABI-1 — byte-identity, the invariant the whole
architecture's substrate-independence rests on — has never been tested. It is
also the easiest thing here to test the moment two realizations exist, which is
why its held-out test is the one I would run first.
