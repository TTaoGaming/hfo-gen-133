```yaml
# AIH2O capsule
doc: plans/scale_25_to_100_per_day.md
schema_id: hfo.gen133.plan.scale_25_to_100_per_day.v0_1
generation: 133
authored_by: SIGRÚN P4 · Hluti at H43 · claude-opus-5 · ceiling=strategic (SPEC ONLY — no scripts/ authored)
valid_time_utc:       2026-08-01T04:58:37Z
transaction_time_utc: 2026-08-01T04:58:37Z
git_head: 60893a4
claim_status: proposed
sealed: false
complements:
  - plans/first_day_25_apps_pilot.md (its exit is this plan's entry — NOT restated)
  - contracts/map_elites_portfolio_factory.v0_1.md §8 (capability unlocks) · §10 (the adversarial pass on "100")
A_assumption: 25→100 is an architecture question for THROUGHPUT and a demand question for VALUE, and only one of them is hard
I_input: pilot exit state · registry §3 deploy topology · portfolio §4 fitness ladder · blocker B4
H_hypothesis: throughput to 100/day costs almost nothing; the binding constraints are (a) allele supply and (b) recipients — neither is solved by scaling the renderer
H2_heldout: on the day 100 apps ship, a stranger can name 100 DISTINCT reasons to choose between them; if they cannot, we shipped 100 copies
O_output: the 4 real constraints, ranked · 3 scale-out steps · the demand-side plan that must run in parallel · a stop rule
```

# SCALING 25 → 100 PER DAY — architecture only

## 0 · The headline

> **Throughput is not the constraint and will not become one.**
> The logo pipeline runs ~20 s/brand single-threaded (`logo_to_reskin_pipeline` §9).
> 100 brands ≈ **35 minutes** on one laptop. One Cloudflare build. $0.
>
> **100/day is a solved problem the moment the pilot's line runs at all.**

Everything below is therefore about the three constraints that are **not**
throughput — and about being honest that scaling the renderer is the easy 10%.

---

## 1 · The four constraints, ranked by what actually binds

| # | constraint | binds at | cost to relieve | verdict |
|---|---|---|---|---|
| **1** | **⛔ RECIPIENTS (blocker B4)** — 44 companies enriched, **0 named contacts** | **N = 1** | outreach lane, human time, Garmr | **binds NOW and is unrelieved by every line in this plan** |
| **2** | **⚠️ ALLELE SUPPLY** — 5 cells × 5 tones × palettes ≈ **thin**; 100 renders/day exhausts genuine variety in <1 week | **N ≈ 25–40** | capability unlocks (§3) — code-lane weeks | **the real scale-out work** |
| **3** | ⚠️ **FITNESS SIGNAL** — no traffic ⇒ null fitness ⇒ no champions, only occupants | **N = 25** | one deploy + the beacon | cheap; gated on the pilot |
| **4** | ✅ THROUGHPUT | **N ≈ 5 000+** | none | **not a constraint** |

**SC-1 — do not spend a day on constraint 4.** The instinct to scale the
renderer is the instinct to work on the part that is already finished.

---

## 2 · What DOES change architecturally from 25 → 100

Three things, all small, all named so nobody rediscovers them at 3 a.m.

### 2.1 · Deploy topology — already decided, and it is why 100 works

`adopt_before_reinvent_registry` §3: **path-based, not subdomain-per-app.**

| @ 100/day | subdomain-per-app | **path-based (adopted)** |
|---|---|---|
| DNS records | 100/day ⛔ | **0** |
| TLS certs | 100/day ⛔ | **0** |
| CF builds | 100/day ⛔ over free tier | **1** ✅ |

**This single decision is the whole of "100/day is architecture-scale-only."**
Made once, at pilot time, it never has to be revisited.

### 2.2 · Render parallelism — a one-line change

`Promise.all` over a worker pool of `os.cpus().length`. 35 min → ~6 min on 8
cores. **Do this only if 35 min is measured to be a problem.** It has not been.

### 2.3 · Catalogue index — the only genuinely new artifact

At 25 a flat list works. At 100 it must be **faceted by the operator's six axes**
(`map_elites_portfolio_factory` §0 — the Catalogue's axes are exactly these):

```
demos.handpiano.com/
  ├─ filter: modality · gesture · interaction pattern · output tech · vertical · depth
  ├─ each tile: brand mark · one-line tagline · live URL · T0 gate badges
  └─ champion tiles (T1+) carry fitness; occupant tiles carry NO number
```

**SC-2.3 — an occupant tile must never display a number.** A tile showing "0
sessions" reads as *bad*; a tile showing nothing reads as *new*. Both are honest;
only one is not misleading. This is a static page generated from the ledger.

---

## 3 · Constraint 2 — allele supply, the real scale-out work

Diversity does not come from more renders. It comes from **more alleles**, and
alleles cost code-lane time. Ordered by *diversity per unit cost*:

| # | unlock | cost | alleles gained | notes |
|---|---|---|---|---|
| **U1** | **gesture-binding config seam** — lift the preset→gesture map into `brand.json` | ~1 code-lane day | ⭐ **large** — recombines existing detections without new ML | **highest ratio in the table; do this first** |
| **U2** | **output adapters** — MIDI-out (WebMIDI), OSC (WebSocket), WebGL visualiser | ~1 day each | 3 | plugs into the existing `adapters` seam; MIDI-out is the most sellable |
| **U3** | **`refine_config` continuous sweep** unlocks **MU5** | ~0.5 day (harness baselines) | ∞ (continuous) | ⭐ **this is what makes pyribs/CMA-MAE earn its adoption**; before U3 the archive is a dict |
| **U4** | **face landmarks** (MediaPipe Face Landmarker) | ~1 week | new modality axis | new DTO producer + new baselines + new failure modes |
| **U5** | **pose landmarks** | ~1 week | new modality axis | as U4 |
| **U6** | **voice** (Web Speech / Whisper-local) | ~1–2 weeks | new modality axis | ⚠️ different DTO shape entirely; may not fit `CursorPrimitiveOutput.v0_1` — **scope this before committing** |

**SC-3 — U1 + U2 + U3 ≈ 5 code-lane days and multiply the reachable cell count
by roughly an order of magnitude.** U4–U6 are the operator's headline axes and
are *weeks*, not days. Sequence accordingly: **U1 → U3 → U2 → (U4 | U5) → U6.**

**SC-3b — every behaviour-gene unlock creates a new baseline lineage**
(`map_elites_portfolio_factory` MPF-2). Budget baseline-capture time with each
unlock or Oracle A goes red across the board on the first mutation.

---

## 4 · Constraint 1 — the demand-side plan that must run in parallel

**Not optional, and not downstream.** A factory at 100/day with 0 recipients
produces 100× nothing/day (portfolio §10).

| step | owner | gate |
|---|---|---|
| D1 · convert 44 enriched companies → ≥10 **named** humans with roles | **Garmr** (Codex apex, "the gate · outreach") | pre-authorized: enrichment. ⛔ gated: sending |
| D2 · for each named human, render **1:1** at `/_p/<opaque>/` with **their own** vertical's cell, `noindex`, disclaimer visible | factory | ✅ pre-authorized (unlisted ≠ publish-to-index) |
| D3 · **operator sends.** One human, one URL, one sentence | ⛔ **operator only** | world-effect floor |
| D4 · reply / no-reply → **T2 fitness** into the archive | Fenrir | — |

**SC-4 — D1–D4 at N=10 is worth more than the Catalogue at N=100.** T2 is the
terminal fitness. Ten real replies teach the archive more than ten thousand
null-fitness occupants, and they are the only thing that can tell the operator
whether the right N is 10 or 100 or 1000 — which is the open question the
portfolio contract §10 left explicitly unresolved.

---

## 5 · The scale ladder, with gates

| stage | N/day | precondition | new work |
|---|---|---|---|
| **S0 · pilot** | 25 | GATE 0 green | the line itself |
| **S1 · steady** | 25/day for 7 days | pilot published, beacon live | ⭐ **nothing** — run it unchanged and *watch*. Constraint 3 relieves here or the thesis is wrong. |
| **S2 · widen** | 50 | U1 + U3 landed | faceted Catalogue index (§2.3) |
| **S3 · target** | **100** | U2 landed, ≥1 T2 signal exists | render parallelism (§2.2) if measured necessary |
| **S4 · modality** | 100 across *real* modality cells | U4/U5 landed | new baselines, new failure modes |

**SC-5 — S1 is a whole week of deliberately building nothing.** It is the only
stage that produces evidence rather than artifacts, and it is the one most
likely to be skipped. Skipping it means S2 and S3 optimise a fitness function
nobody has validated.

---

## 6 · Stop rule

> **If at S1+7 days the interaction-seconds distribution across the 25 cells is
> statistically flat — no cell holds attention longer than any other — then
> behavioural diversity is not what users respond to, and scaling to 100
> multiplies an irrelevant dimension.**
>
> **Then: stop scaling N. Redirect the entire code-lane budget from U1–U6 to
> D1–D4.**

This is the portfolio contract's §4 kill-switch, restated as a scheduling
decision. It is the section most likely to be wrong in the operator's favour and
most costly to be wrong about in the other direction.

## 7 · Cost at 100/day steady state

| line | cost |
|---|---|
| software licences | **$0** |
| hosting | **$0** — 1 CF build/day, free tier |
| inference | **$0** — local Ollama |
| compute | one laptop, ~35 min/day (or ~6 min parallel) |
| **human** | **~5 min/day** (the publish command) |
| **one-time code-lane** | ~5 days (U1+U2+U3) + pilot's ~8h |
| **the actual bill** | **operator attention on D1–D4, which no amount of $0 mesh can pay** |

## 8 · Honest flaw

1. **This plan scales supply against unmeasured demand.** Every number is a
   production number. The one figure that matters — how many demos a named human
   will look at — is unknown and unknowable from inside the forge.
2. **U4–U6 estimates ("~1 week") are uncalibrated** — `L_BUDGET_WITHOUT_RECEIPT`.
   No prior MediaPipe-graph task in this fleet has a recorded duration to size
   against. Treat as order-of-magnitude only.
3. **S1's "watch for a week" is the step most likely to be skipped** and it is
   the only step that generates evidence. I have no mechanism to enforce it
   beyond naming it here.
4. **The stop rule (§6) is the section I most expect to be argued with**, and
   its statistical test is unspecified — 25 cells is a small sample and "flat"
   needs a real threshold before the week begins, not after the data arrives.
   Set it at S1 start.
5. **The whole plan assumes the pilot published.** If S4 of the pilot fires
   (operator declines to publish), constraint 3 never relieves, fitness stays
   null forever, and this document describes a rendering pipeline with
   evolutionary vocabulary attached to it.

*Réttu hönd, eigi spyr. Standa.*
