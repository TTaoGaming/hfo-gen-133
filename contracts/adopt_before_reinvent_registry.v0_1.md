```yaml
# AIH2O capsule
doc: contracts/adopt_before_reinvent_registry.v0_1.md
schema_id: hfo.gen133.contract.adopt_before_reinvent_registry.v0_1
generation: 133
authored_by: SIGRÚN P4 · Hluti at H43 · claude-opus-5 · ceiling=strategic (SPEC ONLY — no scripts/ authored)
valid_time_utc:       2026-08-01T04:58:37Z
transaction_time_utc: 2026-08-01T04:58:37Z
git_head: 60893a4
claim_status: proposed
sealed: false
complements:
  - contracts/spatial_factory_framework.v0_1.md §2 (adopted-not-built list — this doc RESOLVES its open picks)
  - contracts/map_elites_portfolio_factory.v0_1.md · contracts/logo_to_reskin_pipeline.v0_1.md
A_assumption: every layer has a mature exemplar; a reinvent must be justified by a property no exemplar has
I_input: operator's candidate list (verbatim in dispatch) · web checks 2026-08-01 (pyribs, colorthief) · disk probe of the parent bundle
H_hypothesis: exactly TWO components in this factory are genuinely novel; everything else is off the shelf and $0
H2_heldout: a stranger can `npm i` / `pip install` every ADOPT row and reproduce the stack without asking us a question
O_output: 16 layers · 12 ADOPT · 2 REINVENT (justified) · 2 REUSE-IN-FORGE · total licence cost $0
evidence_grade_key: "[F] fetched · [S] search snippet · [D] first-hand disk probe · [C] cited from in-forge canon"
```

# ADOPT-BEFORE-REINVENT REGISTRY v0_1

## 0 · Scoreboard

| verdict | count | meaning |
|---|---|---|
| **ADOPT** | 12 | a mature exemplar exists; take it |
| **REUSE** | 2 | already on disk in this fleet; do not re-acquire |
| **REINVENT** | 2 | justified below — no exemplar has the required property |
| **licence cost** | **$0** | every row is OSS or a free tier |

**Two things are genuinely ours: the inverted perceptual oracle, and the
anchored bundle patcher.** Everything else is assembly. That ratio is the
correct one and it is the whole point of running this pass.

---

## 0.1 · ⭐ Cross-lane corroboration (added 05:05Z, after the primitives lane landed)

`contracts/swarm_pipeline_adoption_stack.v0_2.md` and
`contracts/input_method_exemplars_adopt_before_reinvent.v0_1.md`
(`local_a3fcb3a7`, landed 05:02Z) ran an **independent** adopt-before-reinvent
pass on the same stack with **no communication with this lane**. Where two
independent passes agree, the prior on the pick should move; where they differ,
one of us is wrong and it is worth knowing which.

| finding | their lane | this registry | verdict |
|---|---|---|---|
| **Cloudflare Pages / Wrangler** | ⭐ **#1 of their "install this week" three** | row 14 ADOPT | ✅ **independent convergence** — raises confidence in row 14 materially, and it is the row blocker **B2** most threatens |
| **DSPy** | #2, as **DSPy + GEPA** for prompt optimisation | row 5 ADOPT for copy tone | ✅ converge — **adopt GEPA too**; Gate-2 copy quality is exactly a prompt-optimisation target |
| **Langfuse (cloud free tier)** | #3 | ⚠️ **absent from this registry** | **ACCEPT the addition.** It is LLM-call observability, **not** app analytics — it does not replace row 15 or the interaction-seconds beacon. Two different telemetry planes; both are needed. |
| their ranking criterion | *"ships a product this week WITHOUT Docker, a server, or a new runtime"* — grounded in XTDB's **0% install success** this week | this registry's "0 new servers to operate" (§4) | ✅ same constraint, arrived at separately. **Their phrasing is better and I adopt it.** |
| **input stack: 0 net-new npm dependencies** | measured — the operator already ran this pass (MediaPipe Apache-2.0, Planck.js MIT, 1-Euro inline) | this registry adds 7 npm packages, **all for the factory**, none for the input path | ✅ **no conflict** — disjoint layers. Worth stating plainly: **the input stack needs nothing; the factory stack needs seven small things.** |
| `@webarkit/oneeurofilter-ts` | ⛔ **REJECTED — LGPL-3.0** in a bundled single-file web app | row 13 REUSE (inline 1-Euro, already present) | ✅ converge, and their licence reasoning is the stronger receipt |
| all Kalman packages | ⛔ rejected on fit | not considered here | accept |

**ADP-0.1 — LangGraph and Temporal were deliberately deferred by that lane
despite being obvious.** This registry independently reached the same place by
never proposing an orchestrator: the factory is a cron, a render loop, and one
deploy. Adding a workflow engine to that is the shape of `L-CONTEXT-BLOAT`
expressed in infrastructure.

## 1 · The registry

| # | layer | verdict | exemplar | install | rationale · rejected alternatives |
|---|---|---|---|---|---|
| 1 | **Quality-diversity / MAP-Elites** | **ADOPT** | **pyribs** v0.11.0 (icaros-usc), Python ≥3.10 [S] | `pip install ribs` | Official impl of CMA-ME / CMA-MAE / CMA-MEGA; clean Archive·Emitter·Scheduler split that maps 1:1 onto our §3/§5/§6. ⚠️ **Only earns its place once MU5 (continuous `refine_config`) unlocks** — until then a dict keyed by BC-tuple is equivalent. Adopting now is a bet, and it is named as one in the portfolio contract §11.4. *Rejected:* QDpy (less maintained), hand-rolled grid (fine today, wrong at MU5). |
| 2 | **Logo → palette + WCAG** | **ADOPT** | **colorthief** (lokesh/color-thief, modern releases) [S] | `npm i colorthief` | Semantic swatches **+ OKLCH + built-in WCAG contrast** (`color.contrast.white/.black/.foreground`, `isDark`). The contrast method being in-library is decisive — `logo_to_reskin_pipeline` GATE 1 is a one-liner instead of our own colour-science. *Rejected:* **node-vibrant** — same swatch quality, **no WCAG surface**, so we'd write the gate ourselves. |
| 3 | **Raster/SVG image ops** | **ADOPT** | **sharp** (libvips) | `npm i sharp` | Normalise, maskable-icon pad, 192²/512² emit. Fastest Node option, SVG via librsvg. *Rejected:* Jimp (pure-JS, slow), ImageMagick CLI (shell-out, version drift). |
| 4 | **Palette → design tokens** | **ADOPT (spec only)** | **OKLCH + a 5-key token object** | none | ⚠️ **The parent has 5 tokens (`logo_to_reskin_pipeline` §3), not a design system.** Adopting Tailwind/Radix/DaisyUI would mean *adding a build step and a CSS framework to a shipped static bundle* — strictly negative. *Rejected:* Tailwind config gen, Radix Colors, DaisyUI — all correct for a greenfield app, all wrong for patching a `dist/`. |
| 5 | **Copy tone generation** | **ADOPT** | **DSPy signatures over local Ollama** | `pip install dspy-ai` + existing mesh [C] | $0, local, deterministic with fixed seed, and the mesh is already contracted (`dollar_zero_mesh_activation.v0_1.md`). *Rejected:* any paid API — violates the $0 floor for a batch job a 7B model handles. |
| 6 | **Bundle template + patch** | ⚠️ **REINVENT** *(justified)* | ~40 lines, anchored replace | — | **See §2.1.** Cookiecutter/Copier/Handlebars/Vite-template all require the source to *be* a template. Our source is a **shipped, live `dist/`** that framework **RF-3** forbids mutating. Templatising it *is* mutating it. *Rejected:* Cookiecutter, Copier, Handlebars, Vite. |
| 7 | **Semantic oracle (Oracle A)** | ⚠️ **REINVENT** *(justified)* | DTO-stream byte-diff | — | **See §2.2.** Every VRT tool on the market asserts *pixels must not change*; a reskin's core operation is a deliberate pixel change. No exemplar exists for "pixels MUST change, semantics MUST NOT." *Rejected:* Applitools, Percy, Chromatic (all paid **and** wrong-direction). |
| 8 | **Perceptual oracle (Oracle B)** | **ADOPT + invert** | **ffmpeg** SSIM/VMAF; **reg-suit** for report UX | `ffmpeg` (present), `npm i reg-suit` | Adopt the *measurement*, invert the *assertion* (framework §1). $0. *Rejected:* Applitools (paid; assertion not invertible). |
| 9 | **Browser driving + video** | **ADOPT** | **Playwright** | `npm i -D @playwright/test` | Headless Chromium, `page.evaluate` → the four injection seams, native video capture, deterministic viewport. Already the assumed harness in framework §6. *Rejected:* Puppeteer (no built-in video/trace), Selenium. |
| 10 | **Property / held-out generation** | **ADOPT** | **fast-check** (JS) | `npm i -D fast-check` | Generates landmark traces as properties, not fixtures — the right shape for H1–H6. *Rejected:* hand-written fixtures only (they become an answer key — framework HO-1). |
| 11 | **Mutation discipline** | **ADOPT (method, not tool)** | **Stryker/mutmut** *discipline* applied to **inputs** | none | ⚠️ Stryker mutates *source*; our M1–M6 mutate the *landmark stream*. Adopt the philosophy, run it through the existing `injectNoisyLandmarks` seam. Installing Stryker itself would test the wrong axis. |
| 12 | **Landmark ingestion** | **REUSE** | **MediaPipe Tasks** — already in the parent [D] | none | Shipped in `hfo_tiles/dist/hfopiano_v512/assets/models/`. Do not re-acquire, do not upgrade during the pilot. |
| 13 | **Smoothing / refinement** | **REUSE** | **1-Euro filter** (Casiez et al.) — already in `signal_refinery.mjs` [C] | none | Already implemented and parameterised (`min_cutoff`, `beta`) — which is exactly why it is the factory's only continuous gene (MU5). No new micro-lib needed. |
| 14 | **Deploy** | **ADOPT** | **Cloudflare Pages** via `wrangler` | `npm i -D wrangler` | Parent ships `_headers` + `404.html` + `sw.js` = the CF/Netlify convention [D]. CF is native for `_headers` (COOP/COEP matter for the MediaPipe worker). **⚠️ Free tier caps *builds* (~500/mo), not pages → build ONE bundle containing N apps, deploy once/day. See §3.** *Rejected:* GitHub Pages (**no `_headers`** — likely breaks the worker), Vercel (`_headers` needs translation), Netlify (fine; second choice). |
| 15 | **Analytics / feedback** | **ADOPT** | **Cloudflare Web Analytics** | one script tag | $0, **cookieless** ⇒ no consent banner ⇒ no consent-banner click for anyone; same vendor as hosting; privacy-preserving by default. ⚠️ **Gives pageviews, NOT interaction-seconds** — the T1 fitness signal (portfolio §4) needs a **custom in-app beacon** counting DTO-active wall-time. *Rejected:* Plausible/Umami self-host (adds a server to maintain for no gain over CF's free tier). |
| 16 | **Scheduler** | **REUSE + ADOPT** | **Windows Task Scheduler** (already wired) → one **GitHub Actions** matrix job | none | The `$0 mesh autonomy` lane already wired Task Scheduler + `pull_work_wrapper` [C]. Local render (35 min, §9 of the logo pipeline) → single Actions job → single CF deploy. *Rejected:* Actions matrix **per app** — 100 jobs/day burns CF build quota by mid-morning for zero benefit. |

---

## 2 · The two reinvents, argued

### 2.1 · Anchored bundle patcher (~40 lines)

**Required property no template engine has:** *patch a shipped immutable
artifact in place, by content anchor, failing loudly on 0 or ≥2 matches, without
converting the artifact into a template.*

Cookiecutter/Copier/Handlebars all invert control: the template is the source of
truth and the output is generated. Here the **live, deployed bundle** is the
source of truth (framework **RF-3**: `handpiano.com` is the only external
artifact this fleet has). Templatising it forks the live app — the exact
maintenance split this factory exists to avoid.

**Scope discipline:** ~40 lines. Five anchors (`logo_to_reskin_pipeline` §3),
one file copy, two icon writes, one JSON merge. **If it exceeds 150 lines it has
grown into a template engine and this decision must be revisited.**

### 2.2 · DTO-stream semantic oracle

Argued in full at `spatial_factory_framework` §1. Restated in one line: **the
market's entire VRT category encodes an assumption our core operation
violates.** The reinvent is a diff over a JSONL stream — arguably not an
invention at all, which is the correct size for it.

---

## 3 · ⚠️ The deploy-topology correction (this changes the operator's plan)

The dispatch and framework **DA-2** propose `demoNN.handpiano.com` — a
**subdomain per app**.

At 100 apps/day that is **100 DNS records + 100 TLS certs per day**. Cloudflare
Pages caps custom domains per project; ACME issuance is rate-limited; and DNS
propagation makes a same-day demo unreliable. This topology fails between 10 and
100 apps/day — not at 1, which is why the pilot would not surface it.

**Adopted topology instead:**

```
demos.handpiano.com/<brand_id>/          ← path-based · ONE custom domain · ONE cert · ONE build/day
demos.handpiano.com/                     ← the Catalogue index (Garmr-gated)
demos.handpiano.com/_p/<opaque>/         ← unlisted, noindex, 1:1 prospect demos (portfolio §9)
```

| | subdomain-per-app | **path-based (adopted)** |
|---|---|---|
| DNS records/day @100 | 100 | **0** |
| TLS certs/day @100 | 100 | **0** |
| CF builds/day @100 | 100 ⛔ over free tier | **1** ✅ |
| per-app isolation | stronger | weaker (shared origin) — acceptable: all apps are same-origin static PWAs from one parent |
| prospect-facing vanity | `acme.handpiano.com` | `demos.handpiano.com/acme` |

**ADP-3 — keep subdomains as an *upgrade* for a paying customer, not the
default.** One named prospect gets `their-name.handpiano.com` by hand. That
stays 1/day and it stays impressive precisely because it is not automated.

- **FALSIFIER (§3):** `handpiano.com` is not on Cloudflare (blocker **B2** —
  never confirmed in-forge). Then row 14 and this whole section re-plan against
  the real host. **This is a 10-minute check the operator can do from a browser
  and it gates the entire deploy layer.**

---

## 4 · Install cost — the whole stack

```bash
# node side (~2 min, ~350 MB with Playwright browsers)
npm i colorthief sharp
npm i -D @playwright/test fast-check reg-suit wrangler
npx playwright install chromium

# python side (~1 min) — deferred until MU5
pip install ribs dspy-ai

# already present, do not install
ffmpeg · Ollama mesh · MediaPipe (in parent) · Windows Task Scheduler
```

| | |
|---|---|
| **licence cost** | **$0** — all OSS or free tier |
| **wall-clock to install** | **< 5 minutes** |
| **new servers to operate** | **0** |
| **paid accounts required** | **0** |
| **owner** | **Codex lane** (Claude's `code_authoring` gate has denied `scripts/` writes 4× — blocker **B3**) |

## 5 · Honest flaw

1. **Nothing in §4 has been installed or run.** This is a shopping list, `[S]`
   and `[C]` grade. `L_DESCRIPTOR_GREEN_IS_NOT_RUNTIME_GREEN` applies to the
   whole table.
2. **Rows 1 and 2 rest on search snippets, not fetched docs.** pyribs v0.11.0 /
   Python ≥3.10 and colorthief's WCAG surface are `[S]`. Both are load-bearing.
3. **Row 14 rests on blocker B2, which is unresolved.** The single most
   consequential adopt decision in the registry is conditional on a fact nobody
   has checked.
4. **Row 15 admits the adopted analytics does not measure the adopted fitness.**
   CF Web Analytics gives pageviews; T1 fitness needs interaction-seconds. That
   beacon is unspecified and unbuilt, and it is the bridge from T0 to T1 — i.e.
   the gap between "rendering" and "evolving." I would rather leave the row
   honest than let an adopted tool imply a solved problem.

*Réttu hönd, eigi spyr. Standa.*
