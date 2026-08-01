```yaml
# AIH2O capsule
doc: plans/first_day_25_apps_pilot.md
schema_id: hfo.gen133.plan.first_day_25_apps_pilot.v0_1
generation: 133
authored_by: SIGRÚN P4 · Hluti at H43 · claude-opus-5 · ceiling=strategic (SPEC ONLY — no scripts/ authored)
valid_time_utc:       2026-08-01T04:58:37Z
transaction_time_utc: 2026-08-01T04:58:37Z
git_head: 60893a4
claim_status: proposed
sealed: false
complements:
  - contracts/map_elites_portfolio_factory.v0_1.md · contracts/logo_to_reskin_pipeline.v0_1.md
  - contracts/adopt_before_reinvent_registry.v0_1.md · contracts/spatial_factory_framework.v0_1.md
A_assumption: a 24h pilot that proves the LINE is worth more than 25 apps that prove nothing
I_input: operator's proposed 5 cells × 5 logos · disk probe dist/{hfopiano_v512,pinchpiano} · blockers B1/B2/B3
H_hypothesis: 25 apps is reachable in 24h ONLY if behaviour genes are frozen and all 5 cells are config-reachable today
H2_heldout: a stranger opens demos.handpiano.com, sees 25 visibly-different working apps, and can tell which 5 are the same app reskinned vs which 5 are behaviourally different
O_output: 6 phases · 3 hard gates · 5 real cells (NOT the 5 proposed) · explicit STOP conditions
```

# FIRST-DAY 25-APP PILOT — the 24h proof of the line

## 0 · What is being proven, and what is not

| proven if this works | **not** proven, do not claim it |
|---|---|
| the line runs unattended end-to-end | that anyone wants the apps |
| marginal cost of app #N+1 ≈ 0 | that 100/day is the right N |
| 5 tokens + 1 logo = a visibly distinct app | that the apps are *good* (fitness is `null` at T0) |
| **blocker B1 is cleared — a second URL exists** | that B4 is touched *(0 named recipients — unchanged)* |

**P-0 — this pilot's real deliverable is B1, not 25 apps.** One reskin has never
been put on the internet. Twenty-five is the *evidence that the line ran*; the
URL is the thing that changes the fleet's state.

---

## 1 · ⚠️ The 5 cells — corrected

The dispatch proposes: hand-piano · face-piano · voice-piano · hand-cursor ·
face-cursor.

**Face, voice, and cursor modalities do not exist in the parent bundle.** Per
`map_elites_portfolio_factory` §8: face/pose/voice require new MediaPipe task
graphs and new DTO producers — **weeks of code-lane work, not a config file.**
Three of the five proposed cells are capability unlocks. Naming that now costs
five minutes; discovering it at hour 6 costs the pilot.

**The 5 cells that are reachable today** (behaviour genes frozen per portfolio
§MPF-5, so Oracle A stays blocking-green throughout):

| cell | `launch_preset` | `adapters` / `soundpack` | source of confidence |
|---|---|---|---|
| **C1 · hand-piano · sample-pack** | `piano` | `HANDPIANO_SAMPLE_PACK_ADAPTER`, pack A | the shipped parent ✅ `[D]` |
| **C2 · hand-piano · synth** | `piano` | `HANDPIANO_SYNTH_ADAPTER` | adapter named at index.html ~:2558-2559 `[C]` |
| **C3 · hand-pinch** | `pinch` | sample-pack | `hfo_tiles/dist/pinchpiano` exists ✅ `[D]` — **pending §2 GATE 0** |
| **C4 · hand-piano · alt soundpack** | `piano` | `vendor/smplr-samples/` | soundpacks are directories `[C]` |
| **C5 · hand-piano · two-hand max** | `piano` | `hands.max = 2`, sample-pack | `CONFIG` at index.html ~:912 `[C]` |

**P-1 — C1/C2/C4/C5 differ by *output and config*; only C3 differs by
*interaction*.** That is honest day-1 diversity: **thin**. It is enough to prove
the line and not enough to call the portfolio diverse. Diversity arrives with
the §8 unlocks, and the pilot's job is to make those unlocks cheap, not to fake
them.

## 2 · GATE 0 — three checks before anything is built (~30 min, do these first)

| # | check | command | if it fails |
|---|---|---|---|
| **G0.1** | is `pinchpiano` a preset variant or a separate build? | `diff -rq hfo_tiles/dist/hfopiano_v512 hfo_tiles/dist/pinchpiano` | **C3 drops.** Pilot becomes 4 cells × 5 = **20 apps**. Continue — do not invent a fifth. |
| **G0.2** | ⭐ **does the parent's own golden-master suite pass?** | `node hfo_tiles/tools/run_hfopiano_v511x_golden_master_suite.mjs` | ⛔ **STOP THE PILOT.** The week-move is a *repair*, not a reskin. Framework §10 step 0 has flagged this as never-run across three documents; it is 20 minutes and it re-plans everything if red. |
| **G0.3** | **is handpiano.com on Cloudflare?** (blocker **B2**) | operator checks the registrar/host dashboard, one look | deploy adapter re-plans; registry §3 falsifier fires |

**P-2 — G0.2 is the highest-information action in the entire programme.** Three
documents now rest on a green nobody has observed. Running it is cheaper than
any other step here and it is the only one that can invalidate the rest.

## 3 · The 5 brands — invented, not borrowed

Per `map_elites_portfolio_factory` §9: **the public Catalogue uses invented
brands only.** Applying real third-party marks to publicly-listed demos is
trademark use in commerce; at 100/day it is 100 exposures/day with an audit
trail we wrote ourselves.

| # | brand | vertical seed | logo source | tone gene (MU3) |
|---|---|---|---|---|
| B1 | *(operator-owned mark)* | — | operator supplies | plain |
| B2 | invented — music-ed | tutoring | Ollama name + generated mark | playful |
| B3 | invented — clinical/rehab | motion therapy | generated | clinical |
| B4 | invented — retail kiosk | signage | generated | sales |
| B5 | invented — dev-tool | technical demo | generated | technical |

**P-3 — B1 is the only real mark and it is the operator's own.** Prospect logos
go to unlisted `/_p/<opaque>/` 1:1 paths with a named recipient — which is
blocker **B4**, i.e. out of scope for a 24h pilot by construction.

## 4 · The 24h schedule

| phase | Δ | work | owner | exit criterion |
|---|---|---|---|---|
| **P0** | 0:00–0:30 | **GATE 0** (§2) | any lane, read-only | all three answers written down verbatim |
| **P1** | 0:30–1:00 | install the stack (registry §4) | Codex | `npx playwright --version` prints |
| **P2** | 1:00–4:00 | build the patcher (registry §2.1) + extract `brand.json` from the in-flight sonnet reskin (**blocker B3**) | **Codex** | `reskin(cfg)` reproduces the hand-made reskin **byte-for-byte** |
| **P3** | 4:00–6:00 | logo pipeline S1–S6 (`logo_to_reskin_pipeline`) | Codex | 5 `brand.json` files, all passing GATE 1/2/3 |
| **P4** | 6:00–8:00 | render 5 × 5 = 25 → one `dist/` tree + Catalogue index page | factory | 25 dirs + `index.html` listing them |
| **P5** | 8:00–10:00 | harness: Oracle A over all 25 (skin genes ⇒ **all 25 DTO streams must be byte-identical to their cell baseline**) | Codex | 25 `PASS`, or a named first-divergence frame |
| **P6** | 10:00–10:30 | `wrangler pages deploy --dry-run` → **operator publishes** | **operator** ⛔ | ✅ **B1 CLEARED — `demos.handpiano.com` returns 200** |
| **P7** | 10:30–11:00 | ledger rows ×25 + Archive occupancy snapshot | Fenrir | `spatial_reskin_ledger.jsonl` has 25 rows |
| **P8** | 11:00–24:00 | **let it sit.** Collect signal. | — | see §5 |

**P-4 — P6 is the only human step and it is a single command the operator
runs.** Everything before it is pre-authorized class. Publish is on the
conserved floor and stays there.

## 5 · Signal collection — what "one measurable signal per app" actually means

| signal | tool | tier | honest status |
|---|---|---|---|
| **pageviews / cell** | Cloudflare Web Analytics (cookieless, no banner) | — | ✅ free, one script tag, **but forbidden as fitness** (portfolio MPF-4b) |
| **interaction-seconds** — wall-time with hands tracked **and** DTO firing | ⚠️ **custom beacon, does not exist** | **T1 fitness** | ⛔ **must be built in P4** or the pilot produces no fitness at all |
| **install / add-to-home** | PWA `appinstalled` event → beacon | T1 secondary | cheap, add it |
| Oracle A / quality_gate / WCAG | the harness | **T0 fitness** | ✅ available day 1 |

**P-5 — the beacon is the difference between a pilot and a slideshow.** Without
interaction-seconds, 24h of traffic yields pageviews, and pageviews measure the
referral rather than the app. Beacon spec: `POST /_b` every 10 s while
`dto_events_in_window > 0`, body `{brand_id, cell, seconds, ts}`, no cookies, no
identifiers, no IP retention. **Privacy-preserving by construction, which also
means no consent banner and therefore no consent click for anyone.**

## 6 · Promotion at T+24h

| step | rule |
|---|---|
| 1 | compute BC1/BC2/BC3 for all 25 (portfolio §3) |
| 2 | place each into the 5×5×7 archive |
| 3 | **if ≥30 sessions in a cell** → fitness = median interaction-seconds → **promote a champion** |
| 4 | **if <30 sessions** (the overwhelmingly likely case) → fitness stays `null` → **occupants, not champions** |
| 5 | apply K2 (gate regression) and K4 (legal) unconditionally; K1/K3 need fitness and will not fire |

**P-6 — the honest expected outcome of day 1 is 25 occupants and zero
champions.** Publish that number as-is. A pilot that reports champions on a null
fitness has reward-hacked its own report, and the whole gate stack exists to
stop exactly that.

## 7 · STOP conditions

| # | condition | action |
|---|---|---|
| **S1** | G0.2 red — parent golden-master fails | ⛔ **STOP.** Repair the parent. Nothing downstream is valid. |
| **S2** | Oracle A red on a **skin-only** reskin | ⛔ **STOP.** Brand config leaks into the semantic path; framework §1 falsifier has fired; `brand.json` extraction is wrong. |
| **S3** | >1 of 5 logos hits `PALETTE_INACCESSIBLE` | ⚠️ pause pipeline §2; widen repair walk or add a neutral-accent fallback |
| **S4** | operator declines to publish at P6 | pilot completes as a **dry-run**; **B1 stays open** and the day is a build, not a proof |
| **S5** | any real third-party mark reaches the public index | ⛔ **unpublish within 24h** (K4), no vote, no appeal |

## 8 · Cost

| line | cost |
|---|---|
| software | **$0** (registry §4) |
| hosting | **$0** (CF Pages free, 1 build) |
| inference | **$0** (local Ollama) |
| **human time** | **~30 min operator** (G0.3 + the publish command) |
| **code-lane time** | **~8h Codex** (P1–P5, P7) |

## 9 · Honest flaw

1. **P2 depends on the in-flight sonnet reskin (`local_35e95836`) having
   produced a diff.** As of writing, no `demo01` directory exists anywhere under
   `C:\Dev` — probed, not assumed. If that session has not landed, P2 starts
   from the parent and costs 2–4h more (the §3.1 hand-edit estimate).
2. **Day-1 diversity is thin and I said so in §1** rather than padding the cell
   list to five with unlocks dressed as configs.
3. **The interaction-seconds beacon is unbuilt, unscoped beyond one line, and is
   the load-bearing piece of the fitness story.**
4. **8h of Codex time is an estimate with no prior calibration** — `L_BUDGET_WITHOUT_RECEIPT`.
   The cure is in the plan's own shape: **P0 (30 min) is the probe.** If GATE 0
   overruns, re-budget before P1 rather than pushing through.
5. **Zero of this touches B4.** Twenty-five URLs, zero named recipients. The
   pilot makes the comb faster and does not find the bees.

*Réttu hönd, eigi spyr. Standa.*
