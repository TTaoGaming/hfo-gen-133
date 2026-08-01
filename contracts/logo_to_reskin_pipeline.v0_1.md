```yaml
# AIH2O capsule
doc: contracts/logo_to_reskin_pipeline.v0_1.md
schema_id: hfo.gen133.contract.logo_to_reskin_pipeline.v0_1
generation: 133
authored_by: SIGRÚN P4 · Hluti at H43 · claude-opus-5 · ceiling=strategic (SPEC ONLY — no scripts/ authored)
valid_time_utc:       2026-08-01T04:58:37Z
transaction_time_utc: 2026-08-01T04:58:37Z
git_head: 60893a4
claim_status: proposed
sealed: false
complements:
  - contracts/spatial_factory_framework.v0_1.md §3 (brand.json schema — this doc FILLS it, does not redefine it)
  - contracts/map_elites_portfolio_factory.v0_1.md §5 (MU1 logo re-seed is this pipeline's entry point)
  - contracts/adopt_before_reinvent_registry.v0_1.md (exemplar choices justified there, cited here)
A_assumption: the operator's entry point is literally a logo file; everything else about a brand can be derived or generated at $0
I_input: operator intent "we can input a logo" · measured config surface §3.1 · colorthief WCAG/OKLCH capability (web, 2026-08-01) · local Ollama mesh
H_hypothesis: logo → a WCAG-valid, DTO-neutral brand.json is a pure function with exactly one irreducible human decision (the name)
H2_heldout: two different operators running the pipeline on the SAME logo file get byte-identical brand.json except the name field
O_output: 6 stages, 1 determinism rule, 3 gates, 1 named failure mode per stage
```

# LOGO → RESKIN PIPELINE v0_1

## 0 · The shape

```
logo.(svg|png)
   │
   ├─▶ [S1] ingest + normalise ──────────────▶ logo.norm.png (512², sRGB) + logo.sha256
   ├─▶ [S2] palette extract (colorthief) ────▶ 6 semantic swatches + WCAG ratios  ⛔ GATE 1
   ├─▶ [S3] token map ───────────────────────▶ BLACK_CHROMA + OVERLAYS + theme_color
   ├─▶ [S4] typography select (rule table) ──▶ font stack (self-hosted, no CDN)
   ├─▶ [S5] copy tone (Ollama + DSPy) ───────▶ i18n_overrides + cta + disclaimer  ⛔ GATE 2
   ├─▶ [S6] icon derive (sharp) ─────────────▶ 192² + 512² maskable PNGs         ⛔ GATE 3
   │
   └─▶ brand.json  ──▶ reskin.mjs (framework §4) ──▶ dist/<brand_id>/ ──▶ Oracle A/B ──▶ ledger
```

**LR-0 — the pipeline touches only `brand.json`.** It never emits code, never
touches the parent bundle, and every field it writes is a **skin gene**
(`map_elites_portfolio_factory` §2), so Oracle A stays byte-identical-blocking
for the whole path. That property is what makes 100 renders/day safe.

---

## 1 · [S1] Ingest + normalise

| in | out | tool |
|---|---|---|
| `.svg`, `.png`, `.jpg`, `.webp` | `logo.norm.png` @ 512×512, sRGB, alpha preserved, transparent→`#ffffff` composite copy for extraction | **sharp** (`librsvg` path for SVG) |

- `logo.sha256` is computed here and carried into `brand.json.provenance` — the
  archive's lineage key for MU1 (`logo re-seed`).
- **Named failure mode `LOGO_UNRENDERABLE`:** SVG with external refs, CMYK JPEG,
  >8 MB, or 0 opaque pixels ⇒ **abort at ingest**, do not degrade silently.
- **LR-1 — a logo is never uploaded anywhere.** All of S1–S6 run on the local
  host. There is no third-party image API in this pipeline; a prospect's mark
  leaving the machine is an unforced disclosure.

## 2 · [S2] Palette extract ⛔ GATE 1

**Adopt `colorthief`** (see registry §2 for why over `node-vibrant`): it returns
semantic swatches (`Vibrant`, `Muted`, `DarkVibrant`, `DarkMuted`,
`LightVibrant`, `LightMuted`) with **OKLCH** and **built-in WCAG contrast**
(`color.contrast.white`, `.black`, `.foreground`). The WCAG method being *in the
library* is the whole reason to adopt rather than compute ratios ourselves.

```
extract(logo.norm.png) → swatches[6]
  candidate_bg     = DarkMuted   ?? DarkVibrant   ?? "#0b0d12"
  candidate_accent = Vibrant     ?? LightVibrant  ?? Muted
  candidate_dim    = darken(candidate_bg, ΔL = -0.06 OKLCH)
```

**GATE 1 — WCAG AA or repair, then abort.**

```
if contrast(accent, bg) < brand.quality.contrast_ratio_min (default 4.5):
    repair: walk accent OKLCH lightness ±0.02 (≤12 steps, hue+chroma FROZEN)
    if still < min → ABORT with named failure mode PALETTE_INACCESSIBLE
```

**LR-2 — hue is never repaired, only lightness.** Shifting hue to pass contrast
produces a palette that is no longer the customer's brand, which is the one
thing the logo was supposed to guarantee. A logo whose mark cannot yield an
accessible pair is a **real finding to report to the prospect**, not a defect to
paper over.

- **FALSIFIER (§2):** run S1–S2 over 20 well-known marks; if >30% hit
  `PALETTE_INACCESSIBLE`, the repair walk is too narrow and needs a designated
  neutral-accent fallback rather than an abort.
- **cost_of_delay: MEDIUM.** Gate 1 is the difference between a portfolio and a
  portfolio of accessibility violations shipped at 100/day.

## 3 · [S3] Token map — the only place brand meets the bundle

Straight into the **measured** offsets (`SIGRUN_SHIP_READINESS…` §3.1), anchored
by token not line number (framework **RF-1**):

| brand token | anchor in `hfopiano_v512/index.html` | source |
|---|---|---|
| `palette.black_chroma` | `BLACK_CHROMA` (~:2741) | `candidate_bg` |
| `palette.overlays.accent` | `OVERLAYS` (~:2850) | `candidate_accent` (post-gate) |
| `palette.overlays.dim` | `OVERLAYS` (~:2850) | `candidate_dim` |
| `assets.manifest_overrides.theme_color` | `manifest.webmanifest` | `candidate_bg` |
| `brand_name` | `APP_LINEAGE_LABEL` (~:886-888) | **§7 — the human decision** |

**LR-3 — five tokens. That is the entire visual surface.** This is not a
simplification; it is what §3.1 measured. The smallness is the asset.

## 4 · [S4] Typography — a rule table, not a model

No font inference from a logo. That is a hard vision problem with a low ceiling
and a licensing minefield.

| logo mark character (measured) | stack | licence |
|---|---|---|
| geometric / high circularity | Inter · system-ui | OFL ✅ |
| humanist / low stroke-contrast | Source Sans 3 | OFL ✅ |
| serif detected (stroke-contrast > τ) | Source Serif 4 | OFL ✅ |
| monospace / technical | JetBrains Mono | OFL ✅ |
| **unclassified (default)** | **system-ui stack** | none needed ✅ |

**LR-4 — self-host or use system-ui; never a font CDN.** A Google Fonts link in
a demo sent to an enterprise prospect is a third-party request their security
review will flag, and it breaks the offline PWA guarantee the parent already
ships (`sw.js`).

## 5 · [S5] Copy tone ⛔ GATE 2 — the $0 mesh

**Adopt DSPy signatures over the local Ollama mesh** (`contracts/dollar_zero_mesh_activation.v0_1.md`).
Cost: $0. Latency: irrelevant, this is a batch job.

```
Signature: BrandCopy
  in : brand_name, vertical, tone ∈ {plain|technical|playful|clinical|sales}, mark_description
  out: app_title(≤32ch), tagline(≤64ch), cta_primary(≤28ch), three_bullets[3]
```

**GATE 2 — three deterministic checks, no model grades itself:**

1. **length** — every field within its char budget, or regenerate (≤3 attempts, then fall back to a template).
2. **claim filter** — reject output containing any of: `best`, `#1`, `guaranteed`, `FDA`, `HIPAA`, `certified`, `clinically`, `patented`, or a numeric accuracy claim. **The factory must not manufacture claims it cannot evidence.**
3. **disclaimer present** — `capability_demo_disclaimer` is injected by the pipeline, **never** generated by the model, and never removable by a gene. Framework §3 already calls this a gate rather than a setting; this is where it is enforced.

**LR-5 — `tone` is a gene (MU3), so the same logo yields 5 legitimately
different apps.** This is the cheapest real diversity in the whole factory: $0,
no code, no new baseline lineage, and it varies the thing a human actually reads.

## 6 · [S6] Icons ⛔ GATE 3

`sharp`: `logo.norm.png` → 192² and 512² maskable PNGs with a **20% safe-area
pad** (Android maskable spec) on `candidate_bg`.

**GATE 3:** both files exist, are non-empty, are valid PNG, and
`manifest.webmanifest` references them. A PWA whose install icon 404s is the
most visible possible failure and it is trivially checkable.

## 7 · The one irreducible human decision — the name

Everything above is a pure function of the logo file. **The brand *name* is not
derivable from a mark**, and a wrong name is the single most embarrassing output
this factory can produce.

| logo source | name source | gate |
|---|---|---|
| operator-owned | operator supplies | none |
| **invented brand** (the Catalogue default) | **Ollama-generated**, from a seed vertical | ✅ **pre-authorized class** — invented names need no human |
| prospect's mark | **the prospect's own legal name, transcribed** — never generated, never abbreviated | ⛔ operator-gated, per `map_elites_portfolio_factory` §9 |

**LR-7 — this is the only human-in-loop step in S1–S6, and for invented brands
it is zero.** That is what makes 100/day possible: the Catalogue is invented
brands (§9 of the portfolio contract), so the pipeline is fully unattended right
up to the publish gate.

## 8 · Determinism

**LR-8 — `pipeline(logo, seed) → brand.json` must be byte-reproducible.**
Same logo + same seed ⇒ same JSON, including the Ollama copy (fixed seed,
`temperature` recorded in provenance). Without this, framework **RF-2**
(idempotent reskin) is unreachable and Oracle A can never be byte-stable —
determinism has to hold end-to-end or it holds nowhere.

`brand.json.provenance` carries: `logo_sha256`, `pipeline_version`, `seed`,
`ollama_model`, `temperature`, `colorthief_version`, `parent_sha256`.

## 9 · Cost + throughput

| stage | tool | cost | ~time/logo |
|---|---|---|---|
| S1 | sharp | $0 | <1 s |
| S2 | colorthief | $0 | <1 s |
| S3 | (pure) | $0 | ~0 |
| S4 | rule table | $0 | ~0 |
| S5 | Ollama local | **$0** | 3–15 s ← the only slow stage |
| S6 | sharp | $0 | <1 s |
| **total** | | **$0** | **~20 s/brand ⇒ 100 brands ≈ 35 min single-threaded** |

**100 brands/day is ~35 minutes of one local machine.** The throughput claim is
not the hard part and never was — see `map_elites_portfolio_factory` §10.

## 10 · Honest flaw

1. **Stages S1–S4 and S6 are unvalidated against a single real logo.** No logo
   has been run through this. Every timing above is an estimate.
2. **`colorthief`'s WCAG/OKLCH surface is taken from a search-result summary
   (`[S]` grade), not a fetched API doc.** If those methods are named differently
   the design holds and the call sites change.
3. **The typography rule table's "measured mark character" is hand-waved.**
   Circularity and stroke-contrast thresholds are not specified because I have
   not measured any. The **default row (system-ui) is the honest one** and the
   pilot should use it exclusively until someone measures.
4. **Gate 2's claim-filter is a denylist, and denylists leak.** A model can
   invent an unevidenced claim in words not on the list. Mitigation is that all
   copy is human-visible before the operator-gated publish — which means the
   publish gate is doing real work here, not ceremony.

*Réttu hönd, eigi spyr. Standa.*
