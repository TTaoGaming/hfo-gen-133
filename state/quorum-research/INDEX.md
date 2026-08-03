```yaml
schema_id: hfo.quorum_research.index.v0_1
callsign: quorum_research_organizer
generation: 133
substrate: claude_code_sonnet5
cycle_utc: 2026-08-02T01:15:00Z
clock_source: host_read
claim_status: wired_with_receipts
effect_ceiling: T1_LOCAL_FILE_ONLY
```

# Quorum Research Index — Solo Dev Income Lanes, 2026-08-01/02

Cross-family research on "where should a solo dev (operator) make money" consolidated
under `state/quorum-research/`. Three families targeted: Anthropic (Claude, this forge),
Google (Gemini Deep Research), OpenAI (ChatGPT Deep Research — **not yet landed**).

Rehydration read-order-0: `state/operator_voice/OPERATOR_FRUSTRATION_20260801T2005Z.md`
if picking this up cold.

---

## Per-family inventory

### Anthropic / Claude — `claude/` (10 files)

| file | model | timestamp | key finding (one line) |
|---|---|---|---|
| SPATIAL_INCOME_CASE_STUDIES_20260801.md | sonnet-5 | 2026-08-01 | No documented solo dev makes a living purely from webcam-gesture consumer apps; generic indie-SaaS build-in-public is the proven mechanic, not spatial-specific. |
| MICROSAAS_INCOME_CASE_STUDIES_20260801.md | sonnet-5 | 2026-08-01 | Top solo-SaaS winners (Photo AI, Marc Lou, Plausible) all rode a pre-built audience or years of SEO — not a fast path from zero. |
| GRANTS_PIPELINE_20260801.md | sonnet-5 | 2026-08-01 | SBIR/STTR reauthorized 2026-04-13 through 2031; NSF HCI topic explicitly covers spatial/wearable interfaces — real non-dilutive lane, slow (months). |
| CONTRACT_INCOME_PATHS_20260801.md | sonnet-5 | 2026-08-01 | Fastest path to first dollar: reactivate existing Upwork account this week — zero entry cost vs. weeks of unpaid vetting on gated marketplaces. |
| MOBILE_APP_INCOME_CASE_STUDIES_20260801.md | sonnet-5 | 2026-08-01 | Getting to $1K/mo is ~1-in-6; past $10K/mo is ~1-in-30 conditional on shipping at all — every case study is survivorship-selected. |
| INDIE_GAME_INCOME_CASE_STUDIES_20260801.md | sonnet-5 | 2026-08-01 | Web games (Poki/CrazyGames) realistic first-title range $500–3,000/mo; no named solo gesture-game case surfaced despite targeted search. |
| AI_AGENT_COMMERCIAL_CASE_STUDIES_20260801.md | sonnet-5 | 2026-08-01 | Multi-agent orchestration is investable but not yet a proven high-revenue solo business; money concentrates in single-agent coding assistants (Cursor, Devin), not swarms. |
| PARETO_FRONTIER_SOLO_DEV_20260801.md | opus-5 (SIGRÚN) | 2026-08-02 | The 80% subset — one supervised apex + app factory + distribution lane — is ~0.75 probable solo/90-days; full unattended autonomy is ~0.02. Recommends 5 spatial demos + 40 personalized emails this week. |
| INCOME_PARETO_SOLO_DEV_20260801.md | opus-5 (SIGRÚN) | 2026-08-02 | Apps/micro-SaaS: honest median under $1,000/mo, 12–18 months to $10k MRR — slowest measured path despite feeling most achievable. |
| INTERSECTION_POSITIONING_STANDARD_HARNESS_20260801.md | opus-5 (SIGRÚN) | 2026-08-02 | **Already runs a live Claude×Gemini cross-family comparison** (§G–§I) — concurs mobile B2C is not viable solo, dissents from Gemini on Vision Pro, and resolves the Poki-gesture finding as the strongest cross-family discovery of the day. |

### Google / Gemini — `gemini/` (1 file)

| file | model | timestamp | key finding (one line) |
|---|---|---|---|
| GEMINI_DEEP_RESEARCH_solo_dev_revenue_playbook_20260801.md | gemini_deep_research | 2026-08-01 | Mobile app-store dev is **NOT Pareto-positive** in Q3 2026 (AI supply shock + post-ATT economics); recommends Web Micro-SaaS/Poki → Vision Pro/WebXR → native-wrapper cross-sell, in that order. |

### OpenAI — `openai/` (0 files)

**Missing.** Operator's ChatGPT Deep Research output (PROMPT 1) has not landed yet.

### Synthesis — `synthesis/` (0 files, reserved for future cross-family rollups)

---

## Cross-family agreement table

Sourced primarily from `claude/INTERSECTION_POSITIONING_STANDARD_HARNESS_20260801.md` §G
(Sigrún's own Claude×Gemini comparison, done same-day) plus direct read of the Gemini
verbatim file and Claude's `INCOME_PARETO_SOLO_DEV_20260801.md`.

| # | question | Claude (Anthropic) | Gemini (Google) | OpenAI | agreement |
|---|---|---|---|---|---|
| 1 | Is solo mobile app dev Pareto-positive in 2026? | **NO** — median <$1k/mo, 12–18 mo to $10k MRR (P≈0.1 in 90d) | **NO** — explicit "NOT Pareto-positive" verdict, cites RevenueCat 115k-app dataset | *pending* | **Y** — but flagged as weak evidence (shared training-data narrative, not independent confirmation) |
| 2 | Median time-to-first-$1k for solo mobile? | ~1-in-6 shot at $1k/mo at all; honest median <$1,000/mo, 12–18 mo to $10k MRR | Top-20% median 4.5 mo (iOS)/7.2 mo (Android) to $1k *cumulative*; 83% of all apps never reach it | *pending* | **PARTIAL** — same order of magnitude, Gemini's numbers are sourced to an external audited-scale dataset (RevenueCat), Claude's are aggregator-sourced |
| 3 | Are Poki/CrazyGames web games viable for solo? | Realistic first-title range $500–3,000/mo; no named solo *gesture*-game case found (3 empty searches) | **YES, high** — names 5 solo/small-team case studies ($300k–$3M total), 50/50 revshare, zero CAC via platform placement | *pending* | **PARTIAL→Y** — Sigrún explicitly calls this "Gemini's best find," dissolves her own dead end on gesture-as-differentiator (§H) |
| 4 | Is Vision Pro spatial a high-ARPU frontier? | **NO / DEFER** — <500k units, 75% enterprise, developer adoption stalling, $3,499 entry consumes operator's whole budget | **YES** — "early App Store era" analog, low competition, $10–50 upfront willingness-to-pay | *pending* | **N — explicit disagreement.** Sigrún records this as the one place she thinks a peer family is wrong rather than averaging it away (§H.2) |
| 5 | Verdict on B2B micro-SaaS vs B2C mobile? | Model is right (recurring > one-shot) but timing is wrong for month-1 cash; resolves to sequence: $4–8k one-shot engagement now funds discovery for a $49–99/mo product later | **B2B micro-SaaS $29–99/mo** recommended as Tier-3 of the Web-to-Spatial-AI pipeline | *pending* | **PARTIAL** — agree on the model, Claude adds a sequencing correction Gemini's report doesn't address |

**Reading note:** rows 1–2 concurrence should be *down-weighted*, not up-weighted — both
families likely trained on the same "mobile app stores are saturated" public narrative
(Sigrún's own caveat, §G). Row 4's *disagreement* is the more information-dense row: it's
a genuine cross-family split on a falsifiable claim (Vision Pro installed base, enterprise
mix), not two models echoing a shared prior.

---

## What's still missing

- **OpenAI / ChatGPT Deep Research output** (operator's PROMPT 1) — not yet pasted/landed.
  Once it arrives: save verbatim to `openai/`, extend the agreement table's OpenAI column,
  re-run the down-weighting note above now that a 3rd independent family is in.
- No independent verification of Gemini's RevenueCat/case-study figures, or of Claude's
  aggregator-sourced mobile figures — both flagged unverified-class in their source files.
- `synthesis/` directory created but empty — reserved for a future rollup once 3 families
  are in.
