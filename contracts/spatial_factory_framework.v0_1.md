```yaml
# AIH2O capsule
doc: contracts/spatial_factory_framework.v0_1.md
schema_id: hfo.gen133.contract.spatial_factory_framework.v0_1
generation: 133
authored_by: SIGRÚN P4 · Hluti at H43 · claude-opus-5 · ceiling=strategic (SPEC ONLY — I author no scripts/)
valid_time_utc:       2026-08-01T04:48:42Z
transaction_time_utc: 2026-08-01T04:48:42Z
git_head: 60893a4
claim_status: proposed
sealed: false
supersedes: nothing
complements:
  - contracts/hfo_universal_genotype.v0_1.md §7   (the G1 `spatial_engine_reskin_factory` phenotype + quality_gate — NOT restated)
  - SIGRUN_SHIP_READINESS_MARKETPLACES_INCOME_ROADMAP_20260801.md §3.1–§3.4 (the measured config surface + the 5-step ship path — NOT restated)
  - contracts/defunctionalization_adapter.v0_1.md (worker/adapter separation — NOT restated)
A_assumption: the operator wants N branded demos/week durably, not one demo; the bottleneck is a production line, not app-building skill
I_input: hfopiano_v512 measured config surface (§3.1) · 4 named injection seams · 79 certify scripts · ADR-0015 CursorPrimitiveOutput.v0_1 · ADR-0038 golden-master methodology · blockers B1/B2/B3/B6
H_hypothesis: a reskin factory needs exactly one new invariant — semantics must be byte-stable while pixels must change — and every other component is adoptable off the shelf
H2_heldout: brand demo #2, produced by config only, passes the UNMODIFIED golden-master suite; a stranger can load its URL and see a different brand
O_output: 7 components, 1 inverted-oracle design decision, 6 adopted exemplars, 1 ledger schema
```

# SPATIAL FACTORY FRAMEWORK v0_1 — the production line, not the product

## 0 · What this document is and is not

Sonnet-5 (`local_35e95836`) is executing **reskin #1** right now:
`hfopiano_v512` → `demo01.handpiano.com`. That is the *sonnet tier* — one unit
of output.

**This document is the line that makes unit #2 through #N cost a config file
instead of an afternoon.** It specifies; it builds nothing. Per the code-touch
policy I hold `ceiling=FILE/spec` and I have authored no `scripts/`. Blocker
**B3** already records that Claude's `code_authoring` gate has denied `scripts/`
writes **4×** — so the implementation owner named throughout is the **Codex
lane** (`sigrun_codex_gpt5.6sol` / Fenrir), which is also the only substrate with
a **proven 9h+ sustained loop** (CX-5) and therefore the only one that can run a
factory unattended (**B6**).

I did not self-grant `EMERGENCY_FORGE`. Nothing below requires it.

## 1 · The one thing that is genuinely new — and it is an inversion

Every visual-regression tool on the market (**Applitools Eyes**, **reg-suit**,
**BackstopJS**, **Chromatic**, **Percy**) encodes one assumption:

> *pixels should not change; a diff is a regression.*

**A reskin factory's core operation is a deliberate pixel change.** Point any of
those tools at reskin #2 and every test fails by design. This is why "adopt a
visual-regression tool" is not, by itself, the answer — and it is the single
place where the factory needs its own thinking.

The resolution is to **split the oracle in two and invert one of them**:

| oracle | asserts | on what | blocking? | adopted from |
|---|---|---|---|---|
| **A — semantic** (metamorphic) | `reskin(app)` produces a **byte-identical** `CursorPrimitiveOutput.v0_1` stream for a fixed input trace | the DTO stream, **not pixels** | ⛔ **BLOCKING** | ADR-0015 ABI + metamorphic testing |
| **B — perceptual** (inverted) | branded regions **DID** change (`diff > brand_floor`) **and** geometry/layout regions did **not** (`diff < layout_ceiling`) | rendered MP4 / frames | ⚠️ advisory | reg-suit + ffmpeg SSIM/VMAF, assertion inverted |

**Oracle A is the whole factory.** It is possible only because `hfopiano_v512`
already ships four external injection seams —
`setVideoSource` · `injectRawLandmarks` · `injectNoisyLandmarks` ·
`injectCursorDTO` — which mean the app is **drivable and assertable without a
camera and without a human**. That ABI was shipped before anyone asked for a
reskin; it is the reason this factory is a week of work and not a quarter.

- **FALSIFIER (§1):** a reskin that changes only palette + soundpack produces a
  *different* DTO stream for the same input trace. Then brand config leaks into
  the semantic path, the config seam is not where §3.1 measured it, and
  `brand.json` extraction must precede any further reskin.
- **cost_of_delay: HIGH.** Without Oracle A, "did the reskin break it?" is
  answered by a human watching a video — which is the manual step that caps
  throughput at 1/week no matter how good the scripts get.

## 2 · Component map

```
brand.json ──▶ [2] reskin.mjs ──▶ dist/<brand>/ ──▶ [3] deploy adapter ──▶ public URL
                    │                    │                                     │
                    │                    ▼                                     │
                    │            [4] golden-master harness ◀── fixture traces  │
                    │                 (Playwright + ffmpeg)                    │
                    │                    │                                     │
                    │        ┌───────────┴───────────┐                         │
                    │        ▼                       ▼                         │
                    │   [5] held-out N traces   [6] mutation traces            │
                    │        │                       │                         │
                    └────────┴───────────┬───────────┴─────────────────────────┘
                                         ▼
                        [7] state/ssot/spatial_reskin_ledger.jsonl
```

Adopted, not built: **Cookiecutter/Copier** (template+config), **Playwright**
(browser driving + trace), **ffmpeg** (SSIM/VMAF frame diff), **fast-check /
Hypothesis** (property generation), **Stryker/mutmut** (mutation discipline),
**GitHub Actions** (matrix CI), **Cloudflare Pages / Wrangler** (deploy).
Built here: only the DTO oracle and the ledger.

## 3 · [1] Brand config schema — `brand.json`

Derived from the **measured** config surface (§3.1), not invented. Each field
maps to a real byte offset in `hfopiano_v512`.

```jsonc
{ "$schema": "hfo.gen133.brand_config.v0_1",
  "brand_id": "meridian-sound-lab",              // kebab; becomes dist dir + subdomain + ledger key
  "brand_name": "Meridian Sound Lab",            // → index.html:886-888 APP_LINEAGE_LABEL
  "app_version": "0.1.0",                        // → APP_VERSION
  "app_channel": "demo",                         // → APP_CHANNEL
  "palette": { "black_chroma": "#0b0d12",        // → index.html:2741 BLACK_CHROMA
               "overlays":    { "accent": "#4de0c0", "dim": "#1a2030" },  // → index.html:2850 OVERLAYS
               "contrast_ratio_min": 4.5 },      // WCAG AA — gate, not decoration
  "assets": { "icon_192": "assets/brand/m192.png",
              "icon_512": "assets/brand/m512.png",
              "manifest_overrides": { "name": "…", "short_name": "…", "theme_color": "#0b0d12" },
              "model_3d_url": null,              // ⚠️ NOT in v512's surface — see §3.1 note
              "soundpack_dir": "vendor/packs/meridian" },   // folder swap, per §3.1
  "copy": { "i18n_overrides": { "en": { "app.title": "…", "cta.primary": "…" } },
            "cta_copy": "Book a 15-minute build call",
            "capability_demo_disclaimer": "This is a capability demo, not a product." },
  "interaction_modality_config": {               // → index.html:912 CONFIG
      "launch_preset": "piano",                  // piano | pinch | cursor | <new>
      "hands": { "max": 2, "model_delegate": "GPU" },
      "adapters": { "sample_pack": "HANDPIANO_SAMPLE_PACK_ADAPTER",
                    "synth": "HANDPIANO_SYNTH_ADAPTER" } },   // → index.html:2558-2559
  "refine_config": { "filter": "one_euro", "min_cutoff": 1.0, "beta": 0.007 },  // signal_refinery.mjs
  "hosting": { "provider": "cloudflare-pages",   // cloudflare-pages | netlify | vercel | github-pages
               "subdomain": "demo01.handpiano.com",
               "project": "handpiano-demos" },
  "quality_gate": { "min_fps": 30, "max_p95_latency_ms": 50, "max_drift_30min_px": 8,
                    "named_failure_modes": ["occlusion_two_hand_crossover", "backlit_low_contrast"] },
  "provenance": { "requested_by": "operator|<prospect>", "parent": "hfopiano_v512",
                  "parent_sha256": "…" } }
```

**Three fields are gates, not settings.** `contrast_ratio_min`,
`quality_gate.*`, and `capability_demo_disclaimer` — the last one because
shipping an unsolicited branded demo without saying it is a demo is the legal
risk §3.4 already named.

⚠️ **`model_3d_url` is `null` and honestly so.** The dispatch asked for a 3D-model
field; §3.1's measurement of `hfopiano_v512` found **no 3D-model seam** (it found
`assets/models/` = *ML* models, i.e. MediaPipe task files, not geometry). The
field is reserved, not wired. Populating it does nothing until someone adds the
seam.

- **FALSIFIER (§3):** any of the 11 mapped offsets does not exist at the cited
  line in the real bundle. Then the config surface was mis-measured and step 2
  of the ship path is a hand-edit again.
- **cost_of_delay: HIGH.** `brand.json` is **B3**, the blocker between "one
  reskin" and "N per week." Until it exists, every unit costs 2–4h of hand-editing.

## 4 · [2] Reskin script — `tools/spatial_factory/reskin.mjs` (SPEC · Codex builds)

Node, ~200 lines, **pure function of `brand.json`**. Exemplar: **Cookiecutter /
Copier** — a template directory plus a config file, with the template kept
byte-identical to the shipped parent.

```
reskin(brand.json, parent=dist/hfopiano_v512/) →
  0. verify parent_sha256 (manifest of 30 files)      ⇒ abort on drift
  1. cp -r parent  dist/<brand_id>/                    ⇒ never mutate the parent
  2. patch index.html: 886-888, 912, 2558-2559, 2741, 2850   (AST/anchored, not line-numbered — see below)
  3. swap icons ×2 + merge manifest.webmanifest overrides
  4. swap vendor/<soundpack_dir>
  5. merge i18n overrides into i18n.mjs strings
  6. emit dist/<brand_id>/brand.lock.json  { brand_sha256, parent_sha256, patch_receipts[] }
  7. RETURN a receipt, not a boolean
```

**RF-1 — anchor on content, never on line numbers.** §3.1's offsets (886, 912,
2558, 2741, 2850) are true of *this* build and will drift on the next parent
bump. The script must locate each site by a unique anchoring token
(`APP_LINEAGE_LABEL =`, `const BLACK_CHROMA`, …) and **fail loudly on 0 or ≥2
matches**. A line-numbered patcher silently corrupts on the first parent update
— that is how template factories rot.

**RF-2 — idempotent.** `reskin(cfg)` twice ⇒ identical `brand_sha256`. No
timestamps, no build ids, no nondeterminism in the artifact. Without this,
Oracle A can never be byte-stable.

**RF-3 — the parent is read-only.** The factory never edits `hfopiano_v512`.
handpiano.com is live and is the only external artifact this fleet has.

## 5 · [3] Deploy adapters — one thin wrapper per host

`hfopiano_v512` ships `_headers` + `404.html` + `sw.js` — **the Cloudflare Pages
/ Netlify convention**, which is strong evidence the existing host is one of
those two (**B2**: the deploy script and account were not located in-forge; I
will not assert which).

| adapter | command surface | cost | notes |
|---|---|---|---|
| `cloudflare-pages` | `wrangler pages deploy dist/<brand> --project-name=<p>` | $0 | ✅ **default** — `_headers` is native; subdomains free on an owned apex domain |
| `netlify` | `netlify deploy --dir=dist/<brand> --prod` | $0 tier | `_headers` also native |
| `vercel` | `vercel deploy dist/<brand> --prod` | $0 tier | `_headers` needs translation to `vercel.json` |
| `github-pages` | Actions `upload-pages-artifact` + `deploy-pages` | $0 | ⚠️ no `_headers` support — COOP/COEP headers may break the MediaPipe worker |

**DA-1 — deploy is a world-effect gate.** Every adapter's `--dry-run` path is
free and unattended; the **publish** step is operator-gated (`publish` is on the
conserved floor). The factory produces a *ready-to-publish artifact plus a
one-line command*, and stops there.

**DA-2 — subdomain, not new domain.** `demoNN.handpiano.com` costs $0, needs no
purchase decision, no DNS wait — and demonstrates the exact thing being sold:
*"here is your brand on it, delivered in a day."*

- **FALSIFIER (§5):** handpiano.com is not on Cloudflare/Netlify. Then the
  default adapter is wrong and B2 is a real 1–2h investigation, not 10 minutes.
- **cost_of_delay: ⛔ MAXIMUM — this is B1.** One reskin has never been put on
  the internet. A second URL is the entire difference between *a portfolio* and
  *a product line*.

## 6 · [4] Golden-master harness — Playwright + ffmpeg

**Do not re-spec what exists.** `hfo_tiles/tools/run_hfopiano_v511x_golden_master_suite.mjs`,
79 certify scripts, and golden-MP4 baseline locks with numeric thresholds are
already on disk at gen-130. **Status: never run this session — `UNVERIFIED`.**

> **⭐ The highest-information-per-minute action in this entire framework is to
> run that suite once and record the output verbatim.** Three documents rest on
> the assumption that it is green. If it is red, the week-move is a *repair*, not
> a reskin, and everything below re-plans.

```
harness(dist/<brand>, fixture_trace.jsonl) →
  1. Playwright launches dist/<brand>/index.html (headless chromium, fixed viewport, fixed seed)
  2. page.evaluate → window.HandPiano.injectRawLandmarks(frame.hands, frame.ts) for each frame
     ── deterministic clock: no wall-time, no rAF jitter; drive ts from the fixture
  3. capture: (a) the CursorPrimitiveOutput.v0_1 DTO stream  → oracle A
              (b) Playwright video → out.mp4                 → oracle B
              (c) perf marks: fps, p50/p95 latency           → quality_gate
  4. ORACLE A: diff DTO stream vs baselines/<parent>.dto.jsonl  ⇒ MUST be identical (or within ADR-0038 numeric tolerance)
  5. ORACLE B: ffmpeg SSIM/VMAF vs baselines/<parent>.mp4
       brand regions  : score < (1 - brand_floor)      ⇒ it actually got reskinned
       layout regions : score > layout_ceiling         ⇒ geometry unchanged
  6. GATE: fps ≥ 30 · p95 ≤ 50ms · drift ≤ 8px/30min
  7. emit a receipt row (§9), pass or fail
```

**GM-1 — Oracle A blocks; Oracle B advises.** A pixel oracle that can block a
reskin will block every reskin.

**GM-2 — the fixture is the product.** `injectRawLandmarks` with a recorded trace
removes the camera, the human, the lighting, and the wall clock from the test.
Anything left nondeterministic is a bug in the app, not in the test.

## 7 · [5] Held-out suite · [6] Mutation suite

**Held-out (N traces the reskin was never tuned against).** Exemplar:
property-based testing (**fast-check** / **Hypothesis**) — generate/collect
traces, assert an invariant, not an output.

| # | trace | invariant |
|---|---|---|
| H1 | single hand, slow scale sweep | DTO stream identical to parent |
| H2 | two hands, crossover | identical — including the crossover resolution |
| H3 | rapid pinch train (>8 Hz) | identical; p95 ≤ 50 ms |
| H4 | hands enter/exit frame edge | identical; no NaN in DTO |
| H5 | 30-minute idle-then-active | drift ≤ 8 px; no memory growth trend |
| H6 | a trace recorded from a **different** camera/lighting | identical **or** a *named* failure mode from `quality_gate` |

**HO-1 — held-out means held out.** Traces used to debug a reskin are burned and
replaced. A suite you tuned against is a memorised answer key.

**Mutation (corrupt the input, assert graceful degradation).** Exemplar:
**Stryker/mutmut** discipline, applied to the *input* rather than the source —
which is the right axis for a signal-processing app.

| # | mutation | required behaviour |
|---|---|---|
| M1 | drop 10% / 30% / 60% of frames | degrade smoothly; **no crash, no NaN, no frozen cursor**; `injectNoisyLandmarks` path exercised |
| M2 | occlude one hand mid-gesture | emit a named failure mode, recover within 500 ms |
| M3 | inject ±3σ landmark jitter | one-euro filter absorbs it; DTO stays inside tolerance |
| M4 | reorder / duplicate timestamps | reject or clamp; **never** emit a negative-dt DTO |
| M5 | truncate the soundpack dir | app loads and reports missing audio; **does not white-screen** |
| M6 | malformed `brand.json` field | `reskin.mjs` **fails at build**, not at runtime in front of a prospect |

**MU-1 — the mutation suite's output is a *named failure mode*, not a pass.** Per
§7 of the genotype contract: a spatial product emits accuracy, latency, drift and
a named failure mode, **or it is not a product — it is a demo video.**

- **FALSIFIER (§7):** the parent `hfopiano_v512` itself fails H1–H6 or M1–M6.
  Then the baseline is not golden and the factory is replicating a defect N times.
  **Run the suite against the parent FIRST.**
- **cost_of_delay: MEDIUM now, CRITICAL at N>3.** One bad demo is an apology;
  the same defect on twelve prospect URLs is a reputation.

## 8 · CI/CD wiring — GitHub Actions

```yaml
# .github/workflows/spatial-factory.yml   (SPEC — Codex authors)
on: { push: { paths: ['brands/**/brand.json'] }, workflow_dispatch: {}, schedule: [{cron: '0 6 * * *'}] }
jobs:
  factory:
    strategy: { matrix: { brand: ${{ fromJson(needs.discover.outputs.brands) }} } }   # ← N per week is a matrix row
    steps:
      - reskin.mjs brands/${{matrix.brand}}/brand.json      # [2]
      - harness  (oracle A blocking, oracle B advisory)     # [4][5][6]
      - upload out.mp4 + dto.jsonl + receipt as artifacts
      - append spatial_reskin_ledger.jsonl                  # [7]
      - deploy --dry-run                                    # [3] — PUBLISH stays operator-gated (DA-1)
```

**"N branded demos per week" is literally a matrix length.** That is the whole
claim of this framework: once [1]–[7] exist, adding a brand is adding a
directory with one JSON file in it.

## 9 · [7] Ledger — `state/ssot/spatial_reskin_ledger.jsonl`

Append-only, one row per factory run. Bitemporal, per the forge's SSOT convention.

```jsonc
{ "schema_id": "hfo.gen133.spatial_reskin_ledger.v0_1",
  "valid_time_utc": "…", "transaction_time_utc": "…",
  "brand_id": "meridian-sound-lab", "run_id": "…", "parent": "hfopiano_v512",
  "parent_sha256": "…", "brand_sha256": "…", "config_sha256": "…",
  "requested_by": { "kind": "operator|prospect|factory_cron", "name": "…", "company": "…" },
  "build":   { "reskin_ms": 0, "patch_receipts": [ /* one per anchored site */ ] },
  "oracle_a": { "verdict": "PASS|FAIL", "dto_frames": 0, "first_divergence_frame": null },
  "oracle_b": { "verdict": "PASS|ADVISORY_FAIL", "brand_delta_ssim": 0.0, "layout_ssim": 0.0 },
  "held_out": { "H1": "PASS", "…": "…" },
  "mutation": { "M1": "GRACEFUL", "…": "…", "named_failure_modes_observed": [ ] },
  "quality_gate": { "fps_p50": 0, "latency_p95_ms": 0, "drift_30min_px": 0, "verdict": "PASS|FAIL" },
  "deploy": { "adapter": "cloudflare-pages", "url": null, "state": "DRY_RUN|PUBLISHED",
              "published_by": null, "published_at_utc": null },   // world-effect: operator only
  "claim_status": "wired_with_receipts|proposed|partial|failed",
  "honest_flaw": "…", "next_safe_action": "…" }
```

**LG-1 — `deploy.url` is `null` until a human published it.** The factory may
never write a URL it did not watch a human authorize. This is the
`publish` gate expressed as a schema constraint rather than a norm.

**LG-2 — the ledger is the evo-search population.** Every row is one individual;
`brand_id` × `interaction_modality_config.launch_preset` × vertical is its
behaviour descriptor. See `contracts/spatial_factory_evo_search.v0_1.md`.

## 10 · Build order (each step's exit is the next step's input)

| # | step | owner | gate | exit criterion |
|---|---|---|---|---|
| 0 | **run the existing golden-master suite against the parent, record verbatim** | any lane, read-only | none | red/green known — **do this first, it is 20 minutes and it re-plans everything if red** |
| 1 | reskin #1 by hand; record the exact diff | sonnet-5 (**in flight**) | none | `demo01` artifact exists |
| 2 | extract `brand.json` from that diff | **Codex** (B3) | code lane | `reskin(cfg)` reproduces #1 byte-for-byte |
| 3 | Oracle A harness | **Codex** | code lane | parent passes H1–H6 |
| 4 | deploy adapter (cloudflare-pages) | **Codex** | ⚠️ operator publishes | **B1 cleared — a second URL exists** |
| 5 | demo #2 by config only | factory | none | ✅ **the framework is proven** |
| 6 | Actions matrix + ledger | **Codex** | none | N/week is a directory add |

## 11 · Honest flaw

1. **The parent's own golden-master suite has never been run.** Steps 3–6 assume
   a green baseline that nobody has observed. This is `L_DESCRIPTOR_GREEN_IS_NOT_RUNTIME_GREEN`
   sitting at the root of a seven-component design, and I am specifying on top of
   it rather than under it.
2. **I have not read `hfopiano_v512`.** Every byte offset, seam name and file in
   §3 is transcribed from `SIGRUN_SHIP_READINESS_..._20260801.md` §3.1, which is
   itself one lane's measurement. The bundle lives in the **gen-130** forge, not
   this one. A single stale offset breaks §4 step 2 — mitigated by RF-1
   (content anchoring), which is why RF-1 exists.
3. **Nothing here is built.** This is the eighth specification document produced
   against zero external artifacts (genotype F5's honest prior). The framework's
   own falsifier is F5's: **30 days, no implemented phenotype ⇒ this was
   philosophy.**
4. **The factory scales output, not demand.** B4 remains unaddressed by this
   entire document: *44 companies enriched, 0 named contacts.* Twelve branded
   URLs and zero recipients is a faster way to produce comb, not honey. The
   factory is necessary and it is **not** sufficient, and I would rather say that
   here than let the matrix length feel like progress.

*Réttu hönd, eigi spyr. Standa.*
