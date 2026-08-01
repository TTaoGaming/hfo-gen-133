```yaml
# AIH2O capsule
doc: contracts/map_elites_portfolio_factory.v0_1.md
schema_id: hfo.gen133.contract.map_elites_portfolio_factory.v0_1
generation: 133
authored_by: SIGRÚN P4 · Hluti at H43 · claude-opus-5 · ceiling=strategic (SPEC ONLY — no scripts/ authored)
valid_time_utc:       2026-08-01T04:58:37Z
transaction_time_utc: 2026-08-01T04:58:37Z
git_head: 60893a4
claim_status: proposed
sealed: false
supersedes: nothing
complements:
  - contracts/spatial_factory_framework.v0_1.md   (the 7 production-line components + the inverted oracle — NOT restated)
  - contracts/hfo_universal_genotype.v0_1.md §7   (G1 spatial_engine_reskin_factory phenotype — NOT restated)
  - SIGRUN_SHIP_READINESS_MARKETPLACES_INCOME_ROADMAP_20260801.md §3.1, blockers B1–B6 — NOT restated
  - contracts/schemas/apex_roster.v0_3.md         (the ratified 8 — governance names taken from here)
A_assumption: the operator wants a browsable portfolio of many unique spatial apps AND an evolutionary process that improves them; these are two different machines
I_input: operator intent 2026-08-01 ("1 logo → 100 unique evolving champion apps/day") · spatial_factory_framework §1–§11 · disk probe: hfo_tiles/dist/ contains exactly {hfopiano_v512, pinchpiano}
H_hypothesis: conflating "portfolio coverage" with "quality-diversity search" is the failure mode that makes 100/day produce 100× nothing; splitting them into a deterministic Catalogue and a measured Archive makes both cheap and honest
H2_heldout: a stranger given the Catalogue index and the Archive ledger can answer "which of these 100 is best and why" from the artifact alone, with no human present
O_output: 2 structures (not 1), 3 genome axes, 3 measured behaviour descriptors, a 3-tier fitness ladder, 5 mutation operators, kill criteria, apex ownership
```

# MAP-ELITES PORTFOLIO FACTORY v0_1

## 0 · The correction that makes this buildable

The dispatch proposes one archive with six axes: *input modality · gesture
vocabulary · interaction pattern · output tech · brand/skin · complexity.*

**Five of those six are genes, not behaviours.** In MAP-Elites (Mouret & Clune
2015; Cully et al. 2015) the archive axes are *behaviour descriptors* —
quantities **measured from running the artifact**. A gene you chose before you
built the thing is not a measurement; putting genes on the archive axes turns
MAP-Elites into a **cartesian grid-search with extra vocabulary**. It will fill
every cell on day one and never illuminate anything, because a cell is only
informative when a search had to *discover* it.

That does not mean the operator's six axes are wrong. It means they are **the
Catalogue**, and the Catalogue is a different machine from the Archive.

| | **THE CATALOGUE** | **THE ARCHIVE** |
|---|---|---|
| what it is | a deterministic cartesian product of config choices | a true MAP-Elites archive over *measured* behaviour |
| axes | the operator's six (modality × gesture × pattern × tech × brand × depth) | 3 measured BCs (§3) |
| how a cell fills | by **rendering** — no search | by **search + selection** — a challenger must beat the incumbent |
| what it is for | the **sales surface**. "Here are 100 unique apps, browse by what you need." | the **improvement engine**. "This is the champion of its class, and here is why." |
| cost per cell | seconds (§4 of the factory framework) | one full harness run + a fitness signal |
| honest count | 100/day is a **rendering throughput** claim | 100/day is **not** an archive claim and never will be |
| owner | Garmr (the gate / outreach surface) | **Fenrir** (evolution · the Colosseum) |

**MPF-0 — never report a Catalogue count as an Archive count.** "100 apps
today" is true and means *100 renders passed the gate.* "100 champions today"
would be a lie: a champion requires a challenger it beat, and challengers cost
signal, and signal costs traffic. Conflating these is the exact shape of
`L-LYGIS-SÁÐ`.

---

## 1 · The genome — what mutates

The genome is `brand.json` (spatial_factory_framework §3) plus three added
blocks. Every gene must be **config-expressible**; a gene requiring new source
code is not a gene, it is a **capability unlock** (§8).

| axis | genes | today's alleles (⚠️ = requires capability unlock, not day-1) |
|---|---|---|
| **A · interaction** | `launch_preset`, `hands.max`, gesture bindings | `piano`, `pinch` ✅ *(both exist on disk: `hfo_tiles/dist/{hfopiano_v512,pinchpiano}`)* · `cursor` ⚠️ unverified · face/pose/voice/eye-gaze ⚠️ **no seam exists** |
| **B · output** | `adapters.sample_pack`, `adapters.synth`, `soundpack_dir` | sample-pack, synth, folder-swap ✅ · MIDI-out / OSC / WebGL ⚠️ |
| **C · refinement** | `refine_config.{filter,min_cutoff,beta}` | one-euro parameter sweep ✅ — **continuous, and the only genuinely continuous gene we have today** |
| **C2 · authority** ⭐ | `authority.{raw, filtered, lookahead}` | ✅ **new, from the primitives lane** — see §1.1 |
| **D · brand** | palette, typography, copy, icons, name | derived from a logo, see `logo_to_reskin_pipeline.v0_1.md` ✅ |

### 1.1 · ⭐ The primitives lane found a gene nobody knew was there — and found it degenerate

`contracts/digital_input_method_primitives.v0_1.md` §0 (landed 05:02Z, first-hand
source read) reports, with a **confirmed evidence triple**:

> `hfopiano_v512` computes a lookahead/prediction stream **every frame** and then
> multiplies it by an authority weight of **ZERO** in **100% of shipped
> configurations** — 3/3 refinery presets, 3/3 cursor-smoothing presets, **6/6
> authority objects in `settings_profiles.v512.json`** (49 380 B), and the inline
> `CONFIG` default at `index.html:899`.

Two consequences for this factory, both material:

1. **`settings_profiles.v512.json` is a config surface this contract did not
   know about.** Six shipped profiles is a **larger day-1 allele supply** than
   §1 credited from the five index.html tokens alone. The pilot's cell list
   should be re-derived from that file — it is a measured artifact, not an
   inference.
2. **`authority` is a real behaviour gene with a degenerate population.** Every
   shipped individual sits at the same point (`{raw:0, filtered:1, lookahead:0}`).
   A search space where 6/6 incumbents are identical on an axis is either an
   **unexplored dimension** or an **earned default** — and the primitives lane is
   explicit that this is **NOT settled**: reading (A) specified-not-wired,
   reading (B) an earned zero set after over-prediction produced false triggers,
   with the research pass leaning (B)-with-a-mis-set-horizon (shipped
   `lookaheadMs=60` against a literature benefit ceiling near ~33 ms).

**MPF-1.1 — do NOT let the factory mutate `authority` until falsifier P-F1
(primitives §8) is run.** If reading (B) is right, evolving `lookahead` upward
manufactures **false note triggers** — an audible, embarrassing regression that
Oracle A would *not* catch on a skin-only baseline and that a prospect *would*
hear. This is the clearest example in the whole design of why behaviour genes
need their own baseline lineage (MPF-2) and why the pilot freezes them.

- **FALSIFIER (§1):** `pinchpiano` is not a `launch_preset` variant of the same
  engine but an independently-built bundle. Then axis A has **one** allele
  today, not two, and the pilot's cell count in `plans/first_day_25_apps_pilot.md`
  drops from 5 to whatever `refine_config` alone can span.
  **Check: `diff -rq hfo_tiles/dist/hfopiano_v512 hfo_tiles/dist/pinchpiano`.**
- **cost_of_delay: HIGH.** This one diff decides whether day-1 diversity is real
  or cosmetic. It is a two-minute command and it is step 0 of the pilot.

---

## 2 · What we deliberately do NOT put in the genome

**Not the semantic core.** `spatial_factory_framework` §1 Oracle A requires the
`CursorPrimitiveOutput.v0_1` DTO stream to be **byte-identical** across a
reskin. A gene that changes the DTO stream (e.g. `refine_config`) therefore
**cannot** be validated by Oracle A against the parent baseline.

**Resolution — two gene classes:**

| class | genes | oracle A behaviour |
|---|---|---|
| **skin genes** | palette, copy, icons, soundpack, name | DTO **must** be byte-identical to parent ⛔ blocking |
| **behaviour genes** | `launch_preset`, `refine_config`, adapters | DTO **is expected to differ**; each behaviour-gene combination gets **its own baseline**, promoted only after passing §7 held-out H1–H6 and mutation M1–M6 |

**MPF-2 — a behaviour gene creates a new baseline lineage; a skin gene never
does.** Without this rule the first `refine_config` mutation makes the whole
oracle red and the factory stops. This is the single most likely place for the
line to jam, and it is why the pilot (25 apps) holds behaviour genes **fixed at
5 known-good presets** and mutates only skin genes.

---

## 3 · The Archive — 3 measured behaviour descriptors

All three are computed by the existing harness (framework §6 step 3) from a
**fixed fixture trace**, with no camera and no human. This is the enabling
fact: evaluation is already free.

| BC | definition | measured from | bins (pilot) |
|---|---|---|---|
| **BC1 · interaction density** | DTO events emitted per second over the standard trace | Oracle A capture stream | 5 |
| **BC2 · responsiveness** | p95 input→DTO latency (ms), from the harness perf marks | quality_gate capture | 5 |
| **BC3 · robustness breadth** | count of mutation traces M1–M6 surviving as `GRACEFUL` (0–6) | mutation suite | 7 |

`5 × 5 × 7 = 175` cells. That is a **tractable** archive: it can be meaningfully
filled and re-challenged, unlike the dispatch's six-axis space (≈4 096+ cells,
of which ~99% would hold a single never-challenged individual — the
dimensionality curse the dispatch itself flagged, and it is real).

**MPF-3 — three dims for the pilot; add a fourth only when ≥60% of the 175 are
occupied.** Occupancy is the readiness signal for expanding the archive, not
calendar time.

- **FALSIFIER (§3):** the harness cannot emit per-second DTO counts and p95
  latency without new instrumentation. Then BC1/BC2 are aspirational and the
  archive is 1-dimensional (BC3) until framework component [4] is built.
- **cost_of_delay: MEDIUM.** The Catalogue ships without the Archive; the
  Archive only gates the word *champion*.

---

## 4 · Fitness — the honest 3-tier ladder

**This is the weakest joint in the entire proposal and I will not paper it.** An
evolutionary search with a fabricated fitness function optimises the fabrication.
With zero deployed traffic there is **no** value signal, and any "engagement
score" invented today would be the factory grading its own homework —
reward-hacking with a citation.

| tier | precondition | fitness | what a champion means |
|---|---|---|---|
| **T0 · FEASIBILITY** *(where we are)* | none | binary: Oracle A `PASS` ∧ quality_gate `PASS` ∧ WCAG contrast `PASS` | "this cell is **reachable**." **Nothing more.** Archive is a coverage map, not a quality map. |
| **T1 · ENGAGEMENT** | ≥1 public URL with analytics, ≥30 sessions/cell | **median interaction-seconds per session** — wall-time during which hands were tracked *and* DTO events were firing | "in this class, users actually kept using this one" |
| **T2 · DEMAND** *(terminal)* | ≥1 named recipient (blocker **B4**) | replies + booked calls per demo **sent** | "this one earned a conversation" |

**MPF-4a — fitness is `null`, never `0`, at T0.** A null fitness cannot be
argmax'd; a zero can. The archive schema must reject a champion promotion whose
fitness is null. **At T0 there are no champions — only occupants.**

**MPF-4b — pageviews are forbidden as fitness.** Pageviews measure the referral,
not the app. Interaction-seconds measure the only thing this product does.

**MPF-4c — T2 dominates T1 dominates T0 lexicographically.** A cell with T2
evidence is never re-ranked by T1 numbers.

- **FALSIFIER (§4):** T1 arrives and interaction-seconds correlate ≥0.9 with
  pageviews across cells. Then referral traffic is the whole signal, the demos
  are interchangeable, and the diversity thesis of this contract is falsified —
  **stop the factory and re-plan.** This is the contract's own kill-switch.
- **cost_of_delay: ⛔ MAXIMUM.** T0 is honest but it is not evolution. Every day
  spent at T0 is a day of *rendering*, not *learning*. **The path from T0 to T1
  is one deploy plus one analytics snippet — blocker B1 — and it is the highest-
  value action in this document.**

---

## 5 · Mutation operators

Applied by the emitter to a parent `brand.json`, one or more per offspring.

| # | operator | class | cost | notes |
|---|---|---|---|---|
| **MU1** | **logo re-seed** — new logo → new palette/type/copy | skin | $0 | see `logo_to_reskin_pipeline.v0_1.md`; the operator's "1 logo in" entry point |
| **MU2** | **palette perturb** — jitter OKLCH lightness/chroma within WCAG floor | skin | $0 | rejects any candidate under `contrast_ratio_min` **before** render |
| **MU3** | **copy-tone rewrite** — DSPy signature over local Ollama | skin | $0 | tone alleles: plain · technical · playful · clinical · sales |
| **MU4** | **preset swap / crossover** — take axis A from parent₁, axis B from parent₂ | behaviour | $0 | ⚠️ creates a new baseline lineage (MPF-2) |
| **MU5** | **refine-param CMA step** — pyribs `EvolutionStrategyEmitter` over `(min_cutoff, beta)` | behaviour | $0 | the **only** continuous gene; this is what makes CMA-ME/CMA-MAE worth adopting at all rather than random sampling |

**MPF-5 — the pilot uses MU1–MU3 only.** Skin-only mutation keeps Oracle A
blocking and green throughout the first 24h. MU4/MU5 unlock after the parent's
own golden-master suite has been observed green (framework §10 step 0, still
`UNVERIFIED`).

---

## 6 · Kill criteria — how an occupant leaves its cell

| # | rule | effect |
|---|---|---|
| **K1 · outcompeted** | challenger fitness > incumbent at the same BC cell, at the same tier | incumbent → cold shelf; challenger becomes occupant |
| **K2 · gate regression** | incumbent fails Oracle A, quality_gate, or WCAG on a re-run | **evicted immediately**, cell reverts to empty; a failing public demo is worse than an empty cell |
| **K3 · cold** | ≥30 days public exposure with **0** interaction-seconds | → cold shelf, URL de-listed from the index (⚠️ **not** 404'd — see K5) |
| **K4 · legal** | brand mark withdrawn, disputed, or third-party (§9) | **unpublish within 24h**, no appeal, no vote |
| **K5 · never delete** | cold shelf is append-only, under Nidhöggr (heritage integrity) | a dead cell is evidence about the space, and the operator's whole heritage doctrine says evidence is not garbage |

---

## 7 · Governance — who owns what

Names and offices are taken verbatim from `contracts/schemas/apex_roster.v0_3.md`
(the ratified 8). No new seats are created by this contract.

| function | apex | office rationale |
|---|---|---|
| **the Archive · emitters · champion promotion** | **Fenrir** 🔒 | "evolution · the Colosseum" — this *is* the Colosseum, applied to apps instead of arguments. Also the only substrate with a proven 9h+ loop (**B6**) and the only lane permitted to author `scripts/`. |
| **the cold shelf · lineage · eviction records** | **Nidhöggr** | "heritage integrity · root-gnawing" — K5 is exactly its office |
| **publish gate · the Catalogue index · outreach** | **Garmr** | "the gate · outreach / world-effect" — every public URL passes here |
| **audit · falsifiers · red-team of the archive** | **Sigrún** P4/O4 | including the §4 kill-switch |
| **coordination · daily slate** | **Olrún** P7 | already running the daily PDCA ritual |
| **valkyrie pairing** | **Hrist** (experiment design + kill-criteria) ⟷ **Skogul** (advocate) ⟷ **Nidhöggr-adversary** | the vote rail already exists: `state/ssot/valkyrie_votes_20260801.jsonl` |

**MPF-7 — Fenrir proposes, Garmr disposes.** The archive may never publish. This
is Reflex-Before-Reasoning defence #3 (propose/dispose split) expressed as a
roster constraint rather than a norm.

---

## 8 · Capability unlocks — the honest roadmap for the operator's six axes

The operator's axes are the right *destination*. Here is what each actually costs.

| operator axis | today | unlock cost | owner |
|---|---|---|---|
| brand/skin | ✅ **live** | $0 | factory |
| interaction pattern (preset) | ✅ 2 alleles, pending §1 falsifier | $0 | factory |
| complexity/depth | ✅ via refine params + adapters | $0 | factory |
| output tech (MIDI/OSC/WebGL) | ⚠️ adapter seam exists, no alleles | **1 adapter each, ~code-lane day** | Codex |
| gesture vocabulary | ⚠️ bound inside presets | **needs a gesture-binding config seam** | Codex |
| **input modality (face / pose / voice / eye-gaze)** | ⛔ **no seam** | **new MediaPipe task graph + new DTO producers — weeks, not config** | Codex |

**MPF-8 — say this plainly to the operator: face-piano and voice-piano do not
exist and cannot be produced by config today.** The dispatch's proposed 5 pilot
cells (hand-piano / face-piano / voice-piano / hand-cursor / face-cursor) are
**3 unlocks away**, not 5 config files. `plans/first_day_25_apps_pilot.md` names
5 cells that are reachable **today**.

---

## 9 · ⚠️ Legal — the risk the dispatch walks straight into

The dispatch proposes seeding the factory with *"public brand logos."* Applying
a third party's registered mark to an app and publishing it on a public gallery
is **trademark use in commerce** — not fair use, not parody, not de-minimis —
and 100/day makes it 100 exposures/day, automated, with an audit trail we wrote
ourselves.

| logo source | public gallery | direct-to-prospect unlisted URL |
|---|---|---|
| operator-owned marks | ✅ | ✅ |
| **invented** brands (Ollama-generated names + generated marks) | ✅ | ✅ |
| a **prospect's own** logo | ⛔ **never** | ⚠️ allowed **only** with: `noindex`, unlisted path, the `capability_demo_disclaimer` visible, and a **named** human recipient (which is blocker **B4** anyway) |
| any other third-party mark | ⛔ | ⛔ |

**MPF-9 — the Catalogue is invented brands. Real marks are 1:1 and unlisted.**
This costs the factory nothing: invented brands exercise the identical pipeline,
and the pipeline is what is being proven.

---

## 10 · Adversarial-Bayesian pass on "100 apps/day"

Taking the operator's number as a **hypothesis to test**, not a target to serve.

| claim | prior | evidence for | evidence against | verdict |
|---|---|---|---|---|
| 100/day is technically reachable | 0.5 | one build, N directories, path-based routing (§`adopt` registry); rendering is seconds | CF Pages free tier caps **builds**, not pages — so build **one bundle** with N apps, not N builds | **↑ 0.9 — yes, and it is not even the hard part** |
| 100/day is *useful* | 0.5 | a broad catalogue is a real sales surface; coverage is how you answer "can you do X for my vertical" | **B4: 44 companies enriched, 0 named contacts.** 100 apps × 0 recipients = 0. And 100 *renders* with T0-null fitness are not 100 *champions* | **↓ 0.2 — the number is production-side; the constraint is demand-side** |
| 100/day is the *right* number | 0.33 | — | **there is no demand-side measurement anywhere in the forge that distinguishes 10 from 100 from 1000.** The number is a capacity intuition, not an inference | **unresolved — and it should be, honestly** |

**The reformulation I recommend the operator adopt:**

> *Not* "ship 100 apps/day."
> **"Make the marginal cost of app #N+1 indistinguishable from zero, then let a
> named buyer's request set N."**

Those produce the **identical architecture**. They differ in what counts as
success: the first is satisfied by a large number, the second by a **request**.
Only the second can be falsified, and only the second notices B4.

If the operator affirms 100/day after reading this, that is their call and the
architecture already serves it — this section is the adversarial pass, not a
veto.

---

## 11 · Honest flaw

1. **Fitness is `null` today and I have no honest way to fix that from inside
   the forge.** Everything labelled "evolving champions" is, at T0, coverage
   rendering. The word *champion* is unearned until T1, which requires a deploy.
2. **The parent's golden-master suite has still never been run** (framework §11
   flaw 1). This contract inherits that unobserved green wholesale and adds
   three behaviour descriptors on top of it.
3. **I have not read `hfopiano_v512`.** Axis A's two alleles rest on a directory
   listing (`dist/{hfopiano_v512, pinchpiano}`), not on a diff. §1's falsifier
   exists because that is genuinely uncertain.
4. **pyribs is adopted for a problem that is currently 1-dimensional.** Until
   MU5 unlocks, a dict keyed by BC tuple would do the same work. Adopting it now
   is a bet that behaviour genes arrive; if they do not, that is over-engineering
   and I would rather name it than defend it later.
5. **This contract makes the factory more legible without making it more
   demanded.** Same flaw as framework §11.4, and it is the one that matters.

*Réttu hönd, eigi spyr. Standa.*
