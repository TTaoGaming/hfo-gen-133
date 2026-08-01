```yaml
# AIH2O capsule
doc: contracts/spatial_factory_evo_search.v0_1.md
schema_id: hfo.gen133.contract.spatial_factory_evo_search.v0_1
generation: 133
authored_by: SIGRÚN P4 · claude-opus-5 · ceiling=strategic
valid_time_utc:       2026-08-01T04:48:42Z
transaction_time_utc: 2026-08-01T04:48:42Z
git_head: 60893a4
claim_status: proposed
sealed: false
supersedes: nothing
complements:
  - contracts/spatial_factory_framework.v0_1.md §9 (the ledger = the population — NOT restated)
  - contracts/rehydration_via_github_slack.v0_1.md §1.1 (Fenrir's measured queue contract — REUSED VERBATIM)
A_assumption: the operator wants selection pressure over a population of demos, and wants it to run on the loop that already runs
I_input: Fenrir's live lane_return row (queue path, schema, next_safe_action, effect_ceiling) · spatial_reskin_ledger schema · quality_gate from genotype §7 · blockers B1/B4
H_hypothesis: evo-search does not need to be built — it needs to be FED. A disciplined selector has been idling hourly for 38h on a missing queue file.
H2_heldout: one schema-valid row lands in state/ssot/fenrir_evo_queue.jsonl on the authorized branch, and Fenrir's next hourly cycle returns status != target_queue_empty
O_output: the queue binding · a deliberately SMALL MAP-Elites grid · a fitness function that refuses to score what it cannot measure
```

# SPATIAL FACTORY EVO-SEARCH v0_1 — feed the selector that already runs

## 0 · This contract is 90% adoption and 10% design

The dispatch asks me to *"design MAP-Elites over the population."* **A MAP-Elites
selector is already running.** `fenrir/evo-*` — 26 hourly cycles, hash-chained,
honest-flawed, and idle. Its blocker, in its own words:

```jsonc
"queue":            { "observation": "missing", "path": "state/ssot/fenrir_evo_queue.jsonl" },
"next_safe_action": "Land one schema-valid target row and its runnable held-out
                     benchmark on agent/gen133-bootstrap-20260730.",
"effect_ceiling":   "local_commit+one_slack_pheromone+read_only_git_refresh"
```

**Designing a second evo-search would be the unindexed-capability failure** — the
same error that produced four harness specs for a $0 mesh that already worked.
So this contract does one thing: **it defines the population, the descriptors,
and the fitness so that a queue row can be written**, and it binds every one of
them to Fenrir's existing interface rather than a new one.

- **FALSIFIER (§0):** Fenrir's queue consumer expects a schema this contract does
  not produce. **Its schema is unread — `state/ssot/fenrir_evo_queue.jsonl` does
  not exist, so there is no schema to read, only `lane_return.v1`'s shape to
  infer from.** §4's seed row is a best-effort inference and Fenrir's next cycle
  is the test.
- **cost_of_delay: ⛔ HIGH.** Each idle hour is one wasted scheduled cycle of the
  fleet's only proven durable loop.

## 1 · Population — the ledger IS the population

One individual = one row of `state/ssot/spatial_reskin_ledger.jsonl` (spatial
factory §9, LG-2). Genome = `brand.json`. Phenotype = the built `dist/<brand_id>/`
plus its measured behaviour. **Current population size: 0 built, 1 in flight.**

## 2 · Behaviour descriptors — start with TWO, not four

The dispatch names four descriptor axes (interaction modality × brand vertical ×
visual style × complexity). At 3 bins each that is **81 cells for a population of
one.**

> **MAP-Elites with more cells than individuals is not selection — it is a list
> with extra steps.** Every individual is trivially the elite of its own empty
> niche, illumination is vacuous, and the archive reports 100% novelty forever.
> This is the classic QD failure mode (Mouret & Clune 2015 warn about exactly it:
> descriptor dimensionality must be paid for in evaluations).

**EV-1 — grid size is earned, not chosen.** Open a descriptor axis only when the
archive is ≥50% filled at the current dimensionality.

| phase | population | descriptors | cells |
|---|---|---|---|
| **P1 — now** | 1–8 | `interaction_modality` (piano / pinch / cursor) × `visual_density` (minimal / standard / rich) | **9** |
| P2 | 9–30 | + `brand_vertical` (music / retail / fitness / kiosk) | 36 |
| P3 | 30+ | + `complexity` (single-hand / two-hand / multi-user) | 108 |

`interaction_modality` maps to `brand.json.interaction_modality_config.launch_preset`;
`visual_density` to the palette/overlay block. **Both are config-only** — a
mutation is a JSON edit, which is what makes the search cheap.

## 3 · Fitness — and the half I refuse to score

The dispatch names four fitness terms: click-through rate, dwell time,
conversion to inquiry, technical performance.

**Three of the four require traffic. There is none.** B1: no second property has
ever been deployed. B4: 44 companies enriched, **0 named contacts**. A
click-through rate over zero visitors is not a low score — it is `null`, and
scoring `null` as `0.0` would silently rank every demo identically while looking
like measurement.

**EV-2 — an unmeasurable term is `null`, never zero.** Fitness is a **weighted
sum over non-null terms only**, and the row records which terms were live.

| term | phase | source | weight (P1) |
|---|---|---|---|
| `technical.fps_p50` ≥ 30 | ✅ **live now** | golden-master harness | 0.30 |
| `technical.latency_p95_ms` ≤ 50 | ✅ **live now** | harness | 0.30 |
| `technical.drift_30min_px` ≤ 8 | ✅ **live now** | harness | 0.20 |
| `robustness.mutation_graceful_rate` (M1–M6) | ✅ **live now** | mutation suite | 0.20 |
| `market.ctr` | ⛔ `null` until B1 | analytics | 0.00 |
| `market.dwell_p50_s` | ⛔ `null` until B1 | analytics | 0.00 |
| `market.inquiries` | ⛔ `null` until B4 | inbox | 0.00 |

**So P1 evo-search is a technical-quality tournament, and I am saying that
plainly rather than dressing it as market selection.** That is still worth
running: it answers *which interaction modality survives noisy input best*, which
is a real question with a real answer, obtainable today, with no buyer.

**EV-3 — when traffic exists, market terms take 0.70 and technical drops to
0.30, and the archive is re-scored, not restarted.** Technical quality becomes a
*gate* (pass/fail) rather than a *score*: a 60fps demo nobody enquires about is
worse than a 31fps demo that books a call.

**EV-4 — traffic allocation is a bandit, not a split.** Once ≥2 demos are live,
allocate by Thompson sampling over inquiry-rate, not by even split. Even splits
spend the most traffic on the worst demo.

## 4 · The queue row — what actually unblocks Fenrir

Seeded at `state/ssot/fenrir_evo_queue.SEED.jsonl` in this branch. **It must be
landed on `agent/gen133-bootstrap-20260730` as `state/ssot/fenrir_evo_queue.jsonl`
and pushed**, because Fenrir reads the *remote* commit of that branch
(`source.authority_refresh: "git ls-remote + named-ref fetch"`). A row on this
branch is invisible to it.

I did not switch branches or push. That is a cross-branch world-effect and it is
the operator's or Codex's to perform — one command, named in §6.

```jsonc
{ "schema_id": "hfo.gen133.fenrir_evo_target.v0_1",
  "target_id": "spatial-modality-robustness-p1",
  "generation": 133, "priority": 1, "status": "queued",
  "objective": "Which interaction_modality survives degraded landmark input best?",
  "population_source": "state/ssot/spatial_reskin_ledger.jsonl",
  "descriptors": { "interaction_modality": ["piano","pinch","cursor"],
                   "visual_density": ["minimal","standard","rich"] },      // 9 cells (EV-1)
  "fitness": { "live_terms": ["technical.fps_p50","technical.latency_p95_ms",
                              "technical.drift_30min_px","robustness.mutation_graceful_rate"],
               "null_terms": ["market.ctr","market.dwell_p50_s","market.inquiries"],  // EV-2
               "weights": { "technical.fps_p50":0.30, "technical.latency_p95_ms":0.30,
                            "technical.drift_30min_px":0.20, "robustness.mutation_graceful_rate":0.20 } },
  "mutation_operators": ["palette_shift","launch_preset_swap","refine_config_perturb"],  // all config-only
  "benchmark": { "root": "tests/held_out/",
                 "command": "node tools/spatial_factory/harness.mjs --held-out --brand=<brand_id>",
                 "survivor_rule": "oracle_a PASS AND quality_gate PASS" },
  "elite_rule": "one elite per cell, replaced only on strictly greater weighted fitness",
  "honest_precondition": "⛔ population size is 0. This target is VALID but will
     return elites=[] until the factory produces ≥1 built brand. That is a correct
     empty result, NOT a target_queue_empty no-op — Fenrir should report
     population_empty, which is a different and more useful signal." }
```

**EV-5 — `population_empty` ≠ `target_queue_empty`.** The first says *I have work
and no material*; the second says *I have no work*. Fenrir has been reporting the
second for 38 hours. Landing this row converts it to the first — which points at
the factory instead of at the queue, and that is the correct place to point.

## 5 · Mutation and selection cadence

**Mutation** — all three operators edit `brand.json` only; none touches app code,
so every variant costs one `reskin.mjs` run:

| operator | edit | why config-only matters |
|---|---|---|
| `palette_shift` | perturb `palette.*`, re-check `contrast_ratio_min` | a variant costs seconds, not an afternoon |
| `launch_preset_swap` | `interaction_modality_config.launch_preset` | this is the descriptor axis itself — mutation moves cells |
| `refine_config_perturb` | `refine_config.{min_cutoff,beta}` (one-euro) | ⭐ the highest-value axis: it directly trades latency against jitter, which is the actual product |

**Selection cadence — hourly evaluation, quarterly *strategy* review.** The
dispatch says quarterly review of which niches produce inquiries; that is right
for the *market* axis and far too slow for the technical one. Split them:

| loop | period | decides |
|---|---|---|
| Fenrir hourly cycle | 1h | elite replacement within a cell |
| PDCA daily | 1d | open a descriptor axis? (EV-1) |
| **operator quarterly** | 90d | which niches get *human* effort — and this needs inquiries, so it cannot start before B4 clears |

## 6 · Build order

| # | step | owner | est. | exit |
|---|---|---|---|---|
| 0 | land the seed row on `agent/gen133-bootstrap-20260730` + `git push` | **operator or Codex** | **5 min** | ⭐ Fenrir's next cycle returns `population_empty`, not `target_queue_empty` |
| 1 | create `tests/held_out/` with ≥1 runnable benchmark | Codex | 1h | Fenrir's `benchmark.observation` stops saying `absent_on_authorized_branch` |
| 2 | factory produces ≥1 built brand into the ledger | factory (§10 of the framework) | — | population = 1; archive has 1 elite |
| 3 | 8 config-only variants across the 9 cells | factory | — | archive ≥50% filled ⇒ EV-1 permits P2 |
| 4 | deploy ≥2 → analytics → `market.*` terms go non-null | operator (publish gate) | — | EV-3 re-weighting activates |

**Step 0 is five minutes and it restarts a loop that has been idle for 38 hours.
Nothing else in this document matters until it is done.**

## 7 · Honest flaw

1. **The queue schema is inferred, not read.** `fenrir_evo_queue.jsonl` does not
   exist anywhere I can see, so §4's row is reverse-engineered from the *consumer's
   output* (`lane_return.v1`) rather than from its input contract. It may be
   rejected. Fenrir's next hourly cycle is a cheap, fast test — and its
   `honest_flaw` discipline suggests it will report the rejection clearly rather
   than silently no-op.
2. **This is evo-search over a population of zero.** Every cell is empty, every
   elite is `null`, and the archive's first useful output is at least two build
   steps away. I would rather queue a valid target that returns an honest empty
   than describe a search that cannot run.
3. **The market fitness half is unbuilt and unbuildable today**, and it is the
   half the operator actually wants. B4 (zero named contacts) is untouched by
   this document, by the factory framework, and by every other contract produced
   this session. **Selection pressure over demos nobody sees is a tournament with
   no audience** — technically informative, commercially inert. The factory and
   the Colosseum together still do not produce a customer.
4. **I inferred that Fenrir runs MAP-Elites.** Its row shows `elite_variant_hash`,
   `candidate_hashes`, `survivor_rule` — the vocabulary of a quality-diversity
   selector — but I have not read its implementation, which lives on the Codex
   substrate and not in this forge. If it is a different algorithm, §2's grid and
   §3's weights are the wrong shape and it will say so.

*Réttu hönd, eigi spyr. Standa.*
