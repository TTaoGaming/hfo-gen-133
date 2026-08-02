```yaml
# AIH2O capsule
doc: areas/quorum_research/SIGRUN_CANON_V7_CORRECTIVE_EXERCISE_VERTICAL_20260803.md
schema_id: hfo.gen133.sigrun_canon_v7_corrective_exercise.v0_1
callsign: SIGRÚN
generation: 133
authored_by: SIGRÚN · claude-opus-5 · Claude Code
now_utc: 2026-08-02T17:52:07Z
clock_source: host_read              # bash `date -u -Iseconds`, this turn
reads_first: state/operator_voice/OPERATOR_NO_WARM_NETWORK_ANCHOR_20260803.md   # READ, order-0, Q1-Q7 included
extends: chain row 116 (V6 amended)
distribution_constraint: COLD-ONLY — zero warm network, per anchor
claim_status: partial
```

# V7 — the corrective-exercise vertical

I read the anchor first. **Every distribution line below is cold-only, and I have
cold-discounted every probability. No line in this document asks you to contact
someone you already know.**

---

## §1 · Market research — what I found and what I did not

⛔ ⭐ **I could not find a single named solo founder with verified MRR building
software for physical therapists, corrective-exercise specialists, or movement
practitioners, 2024–2026. I searched three ways and found none. I am not going to
invent one.**

**That is the fourth consecutive null of this exact shape in our corpus** —
webcam-gesture revenue, solo Poki devs, solo SBIR awardees, and now solo PT-software
founders. **The pattern is now itself evidence: I keep being asked to find a
copyable solo exemplar in a vertical, and the exemplars keep not existing in
public.**

**What I *did* verify — the incumbent price band, which proves buyers pay:**

| product | price | buyer | source |
|---|---|---|---|
| **Everfit** Pro | **$19/mo** | online coach | [trainerfu](https://www.trainerfu.com/blog/everfit_alternatives/) |
| **My PT Hub** | $25 (3 clients) / **$59** unlimited / $215 branded | trainer | [quickcoach](https://www.quickcoach.fit/trainerize-alternatives-2026.html) |
| **HubFit** | **$39/mo** all-in | online coach | [hubfit](https://hubfit.com/blog/top-5-trainerize-alternatives-for-online-coaches) |
| **CoachingPortal** | **$49.99/mo** unlimited | coach | [coachingportal](https://coachingportal.io/blog/trainerize-alternatives) |
| **ABC Trainerize** | **$70/mo** (30 clients) | small studio | [assistantcoach](https://assistantcoach.fit/blog/real-cost-fitness-coaching-software/) |
| **Trainerfu** | $75/mo branded app | trainer | [trainerfu](https://www.trainerfu.com/blog/everfit_alternatives/) |

⭐ **The band is $19–75/mo and it is crowded.** HEP incumbents — Medbridge,
PT Everywhere, Exercise Pro Live, Movement RX — all sell to **clinics and general
trainers**.

**Cert-prep sub-market — I checked and I am ruling it out.** NASM CES is
**online, open-book, 100 MCQ, 90 minutes, 70% to pass, three attempts**
([exercise.com](https://www.exercise.com/grow/nasm-corrective-exercise-specialist-ces-certification-review/)),
and prep is already served by Pocket Prep, Trainer Academy, PTPioneer, Examzify
and Stuvia test banks. ⛔ **An open-book exam with three attempts is low-stakes;
willingness-to-pay for prep is structurally low, and the market is saturated.
Skip it.** *(Annual candidate volume: unverified — not public.)*

**Gamified rehab adherence:** Reflexion Interactive Therapy is venture-funded and
sells to clinics/enterprise. ⚠️ **Adjacent solo opportunity: unverified.** I found
no solo case.

---

## §2 · Top-3 product offers

⭐ **The gap I can actually name from the pricing table: every incumbent serves
the *generic* coach. None encodes assessment-driven corrective programming — which
is exactly the knowledge you have and most solo devs do not.**

### 1 · OHSA→Corrective (my pick)

- **Buyer:** solo corrective-exercise specialist / CES-certified trainer, 20–50
  clients, currently writing corrective programs by hand.
- **Mechanic:** practitioner enters an **overhead-squat assessment** result
  (NASM's core screen — foot pronation, knee valgus, forward lean, arms fall).
  Output: a corrective program structured in NASM's actual **inhibit → lengthen →
  activate → integrate** four-phase model, as a client-ready PDF + weekly email.
- **Stack:** Activepieces (**MIT**) + LiteLLM + Postgres + Cloudflare Pages.
  ⛔ **No Documenso/Papermark — AGPL network-source obligation** (row 94).
- **Price:** **$29/mo**, under the crowded midpoint, above impulse.
- **Cold channels:** r/personaltraining, r/PhysicalTherapy, r/NASM,
  cold email to CES holders via Instantly (`tryagentreleasegate.com` warmed).
- **P(first $500 / 30d), cold-discounted: 0.12.**
- **48h MVP:** day 1 — assessment form + the four-phase generator + PDF export;
  day 2 — Stripe test link + landing page + 3 cold-post drafts.

### 2 · SessionNote

- **Buyer:** same practitioner, drowning in post-session notes.
- **Mechanic:** voice/text session note → structured progress summary + next-session
  plan + client-facing recap email.
- **Price:** $19/mo. **P(first $500/30d): 0.10.**
- ⭐ **Lowest build risk and clearest pain — but it is a commodity; any generic AI
  note tool competes.** Your domain edge adds little.

### 3 · FormCheck (webcam movement screen)

- **Mechanic:** client uploads a squat video; pose detection scores the OHSA
  criteria automatically; practitioner reviews and approves.
- ⛔ ⭐ **I am ranking this last despite it being your strongest *technical* fit,
  and I want to be explicit about why: across seven research documents there are
  ZERO verified revenue cases for webcam-vision as a paid prosumer product.** You
  spent 18 months there. **P(first $500/30d): 0.05.**
- ⭐ **The honest use: build it as a *feature* of #1 later, once #1 has a paying
  customer — not as the wedge.**

---

## §3 · Week-1 experiment — OHSA→Corrective

**Hypothesis.** Solo corrective-exercise practitioners will pay ~$29/mo for
assessment-driven program generation that generic HEP tools do not provide.

| day | action | who |
|---|---|---|
| Mon | Codex builds generator + PDF export + landing copy | ⭐ **agents, operator time 0** |
| Tue | Deploy to Cloudflare Pages + Stripe **test-mode** link | agents build, ⛔ you tap deploy |
| Wed | Draft 3 Reddit self-posts + 40 cold emails to CES holders | agents draft |
| Thu | ⛔ **You post and send** (ENV-C) | you, ~45 min |
| Fri | Poll `cap-analytics-poll-collector` | agents |

**Fitness signal:** ≥1 Stripe checkout **started** (test or live), **or** ≥3
practitioners who name their current tool and its cost unprompted.

⛔ ⭐ **FALSIFYING EVIDENCE.** *If 3 Reddit self-posts and 40 cold emails reach
practitioners and produce **zero** replies that name a current workflow, a current
tool, or a price — and **zero** checkout starts — then the hypothesis "solo
corrective-exercise practitioners will pay for assessment-driven generation" is
**FALSE**.* Not under-marketed. **False as-positioned.** At n=43 in a niche this
specific, silence discriminates. **Upvotes, "cool idea," and "I'd use that" all
score ZERO** — that is the unfalsifiable-green class Jörmungandr killed in V1.

**Kill-at: `2026-08-16T18:00:00Z`.**

**Retreat if falsified:** stop building for practitioners; the domain edge is real
but the buyer is not solo practitioners. Next test is **cash-paying end-users**
(people with back/knee pain) at $9 one-time, which is a different buyer entirely.

---

## §4 · Web-presence setup — Olrún PC-pilot batch

**Class approval: SETUP + DRAFT = auto. PUBLISH + SEND + SPEND + SIGNUP = you.**

| # | task | envelope |
|---|---|---|
| 1 | Probe which platforms have live sessions — **report only, no logins** | auto |
| 2 | Draft LinkedIn headline/about repositioned to corrective-exercise + AI | ⭐ draft auto · publish you |
| 3 | GitHub curation: **archive `agentreleasegate-oss`** (27d, 0 stars — dead signal), draft new public `ohsa-corrective` repo | draft auto · publish you |
| 4 | Landing page on Cloudflare Pages | build auto · ⛔ deploy you |
| 5 | Domain availability check: `correctiveexercise.ai`, `hepgen.ai`, `ohsa.app` — **report only** | auto · ⛔ purchase you |
| 6 | Draft 3 Reddit self-posts (r/personaltraining, r/PhysicalTherapy, r/NASM) — **community-rules-checked** | draft auto · post you |
| 7 | Draft LinkedIn article + X thread | draft auto · publish you |
| 8 | Instantly: verify `tryagentreleasegate.com` warmup state + **draft** 40-lead CES list | auto · ⛔ send you |
| 9 | Cal.com booking link | ⛔ **you — signup** |
| 10 | Stripe **test mode** | ⛔ **you — KYC** |
| 11 | Substack/Beehiiv "AI for solo movement practitioners" | ⛔ **you — signup**; drafts auto |
| 12 | Loom account for demo video | ⛔ you; script auto |
| 13 | Product Hunt profile | ⛔ you; defer until #1 has a customer |
| 14 | Wire `state/ssot/outreach_log.jsonl` so `cap-outreach-instrument` can flip | auto |
| 15 | Re-check A1: verify-or-void the 12 dead Suika URLs (row 115) | auto |

⛔ **I will not have Olrún create accounts, accept terms, or spend.** Those are
your signature. A batch of auto-created accounts is how platform bans start.

---

## §5 · Retractions and repriorit­isation

1. ⛔ **V6 §2 "P1 desktop utilities = highest signal-per-hour" — DEMOTED to a
   parallel bet.** It was chosen on market data with no domain edge. Q6 says your
   edge is corrective exercise; **an edge you have beats a market someone else won.**
2. ⭐ **P2 B2B SaaS is now specifically CORRECTIVE-EXERCISE B2B SaaS and is
   primary** (§3).
3. **Games → TERTIARY.** Publish the 12 DLCs **only after A1 verify-or-void
   returns live URLs** (row 115: 0/24 resolve), then link them from the landing
   page as *factory-capability proof*, not as an income lane.
4. ⛔ **V6 §7's one-sentence (batch-approve 40 contract drafts) — SUPERSEDED but
   not cancelled.** Those drafts expire **2026-08-09**; approving them is still
   the cheapest hour on the board. **It is now EXP-2, not EXP-1.**

**Updated queue:** **EXP-1** OHSA→Corrective (§3) · **EXP-2** the 150 staged
contract drafts, before expiry · **EXP-3** employment, unchanged counterweight.

---

## §6 · Cold-only discipline

Every channel in §3 and §4 is cold: Reddit self-posts (zero gatekeeper), cold
email on a warmed domain, HN, Cloudflare demo links. **No line asks you to
contact anyone you know.**

**Cold discount applied:** D2's band is warm 40–70% / cold 10–25%. I used the
**cold** number everywhere, then discounted further for a niche audience and an
unproven offer — which is why §2's best case is **0.12, not 0.38**.

⚠️ **`[NEEDS_WARM_NETWORK — NOT_APPLICABLE_TO_HFO]`:** Product Hunt's
hunter-relationship path, and any referral-based motion. **Deferred, not
recommended.**

---

## §7 · One sentence

> ⭐ **V6 told you to approve 40 contract drafts; V7 tells you to spend Monday
> letting the swarm build OHSA→Corrective — the one product where your ten years
> of corrective-exercise knowledge is the moat rather than your spatial tech —
> and then, on Thursday, post it cold to three subreddits and forty CES holders,
> because that is the first thing you have ever shipped where the thing you know
> is scarcer than the thing you can build.**

---

## Honest flaws

1. ⛔ ⭐ **I found ZERO verified solo-founder MRR cases in this vertical.** The
   $19–75/mo band proves buyers exist; **it does not prove a solo founder can
   reach them cold.** This is the weakest evidentiary base of any canon I have
   written, and I am recommending it anyway because Q6 says the domain edge is
   real and I have no better use for a real edge.
2. **I did not verify NASM CES holder volume, or that a 40-name CES email list is
   buildable.** ⭐ **If Olrún cannot assemble 40 named CES holders in §4 task 8,
   §3's falsifier never runs and the experiment is void.** Check that first.
3. **I have not verified subreddit self-promotion rules.** r/PhysicalTherapy in
   particular may prohibit product posts outright — **that is a ban risk on the
   primary channel**, and task 6 must rules-check before you post.
4. ⭐ **I am recommending a vertical the operator named, one turn after telling
   him I keep failing to find exemplars in verticals.** Both can be true; **but if
   this is the fifth null, the pattern is the finding and the next canon should
   stop asking "which vertical" and start asking "why does nobody solo-build
   here."**
5. **Everything in §3 still terminates in ~45 minutes of your hands on Thursday.**
   Seven canons, same structural limit.

*Réttu hönd, eigi spyr. Standa.*
