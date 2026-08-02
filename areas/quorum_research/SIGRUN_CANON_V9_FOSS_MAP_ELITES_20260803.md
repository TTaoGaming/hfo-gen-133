```yaml
# AIH2O capsule
doc: areas/quorum_research/SIGRUN_CANON_V9_FOSS_MAP_ELITES_20260803.md
schema_id: hfo.gen133.sigrun_canon_v9_foss_map_elites.v0_1
callsign: SIGRÚN
generation: 133
authored_by: SIGRÚN · claude-opus-5 · Claude Code
now_utc: 2026-08-02T21:19:29Z
clock_source: host_read
reads_first: state/operator_voice/OPERATOR_NO_WARM_NETWORK_ANCHOR_20260803.md
extends: FRAMEWORK_GEN133_V1 → v1.1 (no fork)
machine_readable: state/ssot/foss_map_elites.json
claim_status: partial
```

# V9 — FOSS × MAP-Elites factory, and income this month

⭐ **Before anything else: the FOSS licence table in the brief is wrong on its
most important row, and I checked every candidate against the GitHub API.**

| repo | brief says | ⭐ **API says** | commercial fork? |
|---|---|---|---|
| `mfts/papermark` | "Unlicense" | ⛔ **NOASSERTION** (8.9k★) | ⛔ **STOP — read LICENSE by hand** |
| `twentyhq/twenty` | "AGPL — check" | ⛔ **NOASSERTION** (54k★) | ⛔ STOP |
| `moonfloof/suika-game` | "Unlicense" | ⛔ **NOASSERTION** (60★) | ⚠️ **already forked 12×** |
| `documenso/documenso` | "AGPL — check" | **AGPL-3.0** (14k★) | ⛔ network-source obligation |
| `calcom/cal.com` | "AGPL — check" | ⭐ **MIT** (47k★) | ✅ core MIT — ⚠️ verify `/ee` |
| `ggerganov/whisper.cpp` | MIT | ✅ **MIT** (52k★) | ✅ clean |
| `ollama/ollama` | MIT | ✅ **MIT** (178k★) | ✅ clean |
| `shadcn-ui/ui` | — | ✅ **MIT** (120k★) | ✅ clean |
| `langchain-ai/langchain` | — | ✅ **MIT** (143k★) | ✅ clean |
| `run-llama/llama_index` | — | ✅ **MIT** (51k★) | ✅ clean |
| `PostHog/posthog` · `chatwoot/chatwoot` | — | ⛔ **NOASSERTION** | ⛔ STOP |

⛔ ⭐ **NOASSERTION means GitHub could not classify the licence — a human must read
the file before any commercial fork.** Five of the brief's named candidates fail
this. **And we already forked `suika-game` twelve times without confirming its
licence.** That is a live legal exposure, not a hypothetical.

---

## §A · Consolidated world state

**Proven (probe-verified):** 44→42 ALIVE capabilities; memory recall cosine
**0.7677**; LangGraph graph genuinely invoked; DBOS/Postgres/LiteLLM/CrewAI live;
AbstractFactory **10/10 held-out green**; **53 Cloudflare Pages projects**;
Suika DLCs **8/8 at HTTP 200**; RED-first held-out discipline.

**Landed since my last canon:** ⭐ **the `class:` gate format is implemented**
(`class:<name>:quota=<N>:seq_range=<a-b>:expires=<UTC>`) — **that clears blocker
#2 I have raised four times.** `factory/microsaas_template/` exists with build,
deploy and log-ship scripts.

**Still zero (measured this turn):** `outreach_log.jsonl` **absent** · approved
gate items **0** · booking links on landers **0** · envelopes **unsigned** ·
external humans reached **0**.

⚠️ **Not landed at my read time:** `DISTRIBUTION_CHANNELS_INTEL`,
`PARTNERS_REVSHARE_AGENCY_INTEL`, `READY_TO_FIRE_TUESDAY.md`. **I integrated what
existed and did not guess at the rest.**

> **One sentence: production is solved, distribution is at zero, and the gate that
> blocked automation just opened.**

---

## §B · FOSS × MAP-Elites factory

### Behaviour-descriptor axes (3, deliberately small)

- **B1 buyer** — `dev-tools` | `prosumer-creator`. ⛔ **SMB-ops and vertical-pro
  are excluded**: they are the HVAC/therapy domain-tax classes the operator
  rejected ("previous advice were bad fits").
- **B2 price** — `free→sponsor` | `$9–19 one-time` | `$29–49/mo`.
- **B3 channel** — `HN+Reddit-native` | `directory-passive` | `marketplace`.

**2 × 3 × 3 = 18 cells.** Small enough that every cell can actually be filled.

**Fitness = cold demand signal only** — a real Reddit/HN/IH permalink asking for
this thing at this price. ⛔ **Not LLM plausibility.** A cell with no demand
permalink stays **empty**; empty is a legitimate elite.

### Initial elites (10 cells filled, 8 empty and honestly so)

| cell (B1/B2/B3) | FOSS parent | licence | mutation | conf |
|---|---|---|---|---|
| dev / free / HN | `ollama` **MIT** | ✅ | local-LLM cost dashboard | B |
| dev / $9–19 / HN | `whisper.cpp` **MIT** | ✅ | CLI meeting-notes, no signing needed | ⭐**A** |
| dev / $29–49 / HN | `langchain` **MIT** | ✅ | LLM cost-attribution per feature | B |
| dev / $9–19 / directory | `shadcn/ui` **MIT** | ✅ | webhook replay + log viewer | B |
| dev / $29–49 / directory | `llama_index` **MIT** | ✅ | RAG-eval harness | C |
| dev / free / directory | `shadcn/ui` **MIT** | ✅ | cron dead-man switch | B |
| dev / $29–49 / marketplace | `cal.com` **MIT core** | ⚠️ verify `/ee` | booking for async dev consults | C |
| prosumer / $9–19 / directory | `whisper.cpp` **MIT** | ✅ | podcast transcript cleaner | B |
| prosumer / $9–19 / HN | `ollama` **MIT** | ✅ | offline summariser desktop | C |
| prosumer / free / directory | `shadcn/ui` **MIT** | ✅ | clipboard history | C |

⭐ **Every filled cell draws from an MIT parent.** That is not a coincidence — it
is the constraint. **The AGPL and NOASSERTION repos are excluded from v1 entirely.**

**8 empty cells** are mostly `marketplace` and `$29–49/mo prosumer` — I have no
demand permalink for them and will not invent one.

### Codex loop specs

**One-shot goal loops** (fire on operator class-sign):

| loop | input | output | ⭐ exit condition |
|---|---|---|---|
| `LOOP_BUILD_MICROSAAS_UNIT_v0` | `unit_spec.json` | live subdomain + staged distribution | ⭐ **loop must curl its own URL and receive 200 before writing the chain row** |
| `LOOP_BUILD_DESKTOP_UTILITY_v0` | same | CLI binary + Gumroad draft | binary runs `--version` in a clean shell |
| `LOOP_LAUNCH_TIER2_v0` | unit_id + channel | post drafts + submission times | drafts exist **and** subreddit rules-check passed |
| `LOOP_PERSONALIZE_COLD_EMAIL_BATCH_v0` | target CSV + envelope | personalised sends | Instantly message-id echoed per row |

⭐ **Every loop carries the row-115 lesson: no DEPLOY row without a self-curled
200.** That single rule would have caught the 12 phantom Suika receipts.

**Recurring scheduled loops:**

| loop | cadence | stop condition | receipt |
|---|---|---|---|
| `RECURRING_SEO_DIRECTORIES_v0` | 4h | queue empty **or** 3 consecutive 4xx | directory URL + HTTP code |
| `RECURRING_FOSS_CANDIDATE_SCAN_v0` | daily | ⭐ **skip any repo whose SPDX is NOASSERTION** | repo + SPDX + stars |
| `RECURRING_DEMAND_SIGNAL_MINE_v0` | daily | ⭐ **must record ORIGINAL permalinks, never aggregator links** | permalink + upvotes |
| `RECURRING_REPLY_TRIAGE_v0` | 30 min | inbox unreachable | reply id + class |

⛔ **All four halt on `MAX_RUN_COST_USD` breach.** ⛔ **`RECURRING_FOSS_CANDIDATE_SCAN`
must never auto-promote a NOASSERTION repo into the elite pool** — that is how the
suika exposure happened.

---

## §C · Income this month (Aug 2 → Aug 30)

⚠️ **Honest framing first: my measured P(first $500 in 30 days, cold) is 10–25%
for the services lane and under 10% for products.** Planning to a number does not
raise it. **What follows maximises the chance, it does not promise it.**

| week | cash lane (services) | product lane (portfolio) | $ target |
|---|---|---|---|
| **W1 Aug 3–9** | ⭐ sign class-lines, fire **40 contracts + 25/day cold email**; 2 Upwork Catalog listings | fix the dead `#book` anchor; ship **1** MIT unit | **$0** — the goal is *first reply* |
| **W2 Aug 10–16** | reply triage; **book calls**; $350 diagnostics | ship 1–2 units; Tier-2 directories | ⭐ **$350–700** (1–2 diagnostics) |
| **W3 Aug 17–23** | convert diagnostic → **$1.5–3k sprint** | 2–3 units **only if** a channel converted | **$1,500–3,000** |
| **W4 Aug 24–30** | deliver sprint; ask for referral | kill/keep review per cell | **$0–3,000 collected** |

**Split: 70% cash lane / 30% product lane.** Products are portfolio and proof
this month; **services are the only realistic path to August dollars**
(`SIGRUN_CASE_STUDY_LIBRARY §3`: contracts rank 1 across D2·D3·D6·D7).

⭐ **The whole month hinges on W1 producing one reply. Everything downstream is
conditional on it.**

---

## §D · Five blocking questions

**Q1 — Papermark/Twenty/suika licences.** Twelve suika forks are deployed under a
licence GitHub cannot classify. **(a)** I dispatch a Codex licence-audit and we
take the 12 down if it's restrictive · **(b)** you read the LICENSE files
yourself tonight · **(c)** accept the risk knowingly.
*Unblocks:* whether the factory may fork non-MIT at all. *Changes:* the elite pool
shrinks to MIT-only permanently under (a)/(c).

**Q2 — Which single channel gets W1.** **(a)** cold email 25/day from the warmed
domain · **(b)** Upwork Catalog listings · **(c)** both.
*Unblocks:* which class-line you sign tomorrow. *Changes:* (c) halves the
attention each gets and I would rather you pick one.

**Q3 — Payment rails.** Stripe and Gumroad are both unverified. **(a)** you do
Stripe KYC this week · **(b)** Gumroad only (faster, no KYC gate) · **(c)** defer,
invoice manually for the first sale.
*Unblocks:* every `$/mo` row in §B. *Changes:* under (c) products cannot transact
in August and the month is services-only.

**Q4 — Reddit account standing.** Tier-1 promotion needs karma and account age;
several target subs ban promo outright. **(a)** you have an aged account with
karma · **(b)** you don't · **(c)** unknown.
*Unblocks:* whether `LOOP_LAUNCH_TIER2` can fire at all. *Changes:* under (b)/(c),
Tier 1 is dead and distribution collapses to directories + cold email.

**Q5 — Failure budget.** If W1 and W2 produce zero replies, **(a)** pivot to
employment applications for the rest of August · **(b)** keep going to Aug 30 ·
**(c)** cut compute and reassess.
*Unblocks:* the kill-rule I enforce without asking you again. *Changes:* I stop
you at day 14 under (a), day 30 under (b).

---

## §E · Contracts and jobs lane

⭐ **The portfolio's job this month is not to earn — it is to be evidence.**

- **For contracts (Upwork/agencies):** each shipped unit is a *"here is a working
  thing I built and deployed in under 8 hours"* artifact. The held-out test suites
  and the capability census are the differentiator — **almost no freelancer can
  show a RED-first test discipline.** That is the Lane-1 pitch made concrete.
- **For jobs:** the same artifacts plus the public repo. ⚠️ **The mythology
  framing is a hiring liability** (I flagged this in AM_V0) — one recruiter-legible
  README, engineering register, no valkyries.
- **Cross-feed:** every diagnostic you sell becomes a case study; every case study
  raises the Catalog listing's conversion. **Services fund products; products prove
  services.** That loop is the studio.

---

## §F · Anti-list (updated with "previous advice were bad fits")

⛔ HVAC · ⛔ therapy/corrective-exercise · ⛔ **any vertical requiring domain the
operator doesn't already hold** · ⛔ warm network · ⛔ games as income ·
⛔ publish-without-distribute · ⛔ single-product all-in bets · ⛔ **AGPL or
NOASSERTION forks** · ⛔ new frameworks · ⛔ another round of clarification
questions after these five · ⛔ **more production while `outreach_log.jsonl` is
empty.**

---

## §G · Ratification — already decided, restated to prevent drift

⭐ **This was settled in chain row 124 and I am not re-litigating it.**
**RATIFIED:** HVAC demoted to #9, `HVAC_PAID_PILOT_001` suspended.
**OVERRULED:** AI-dev-tools to #1 — D3 ranks the category #6/1.8%, D6 #6/2.6%,
and `agentreleasegate-oss` is a measured 0 stars in exactly that lane.
**REFUSED:** the spec-5-ideas three-week plan.
⭐ **Note the nuance: §B's elites are dev-tools — that is not a reversal.** They
are *portfolio units under the product lane*, not the #1 income lane. The income
lane remains services.

---

## §H · Honest flaws

1. ⭐ **I corrected the brief's licence table using the GitHub API, and five
   candidates came back NOASSERTION — including one we already forked 12 times.**
   ⚠️ **NOASSERTION is not "restrictive," it is "unclassifiable."** Some are
   permissive with a custom header. **Q1 exists because I genuinely don't know.**
2. **Three parallel dispatches had not landed** when I read. My §A is incomplete by
   construction and the distribution-intel doc may change §C's channel ranking.
3. **The `class:` gate format is documented in the file. I did not verify a parser
   reads it.** ⚠️ **Documented ≠ executed — my own root-cause finding — so treat
   blocker #2 as "probably cleared," not cleared.**
4. **§C's dollar targets are conditional on a W1 reply that has never happened
   once in 18 months.** I am presenting a plan whose first step has no precedent
   of success in this operator's history.
5. ⭐ **I designed a factory in §B while enforcing a 1-unit/week cap from row 125.**
   That is deliberate — **the design is ready, the throttle is on** — but it means
   most of §B is inventory until distribution converts, which is exactly the
   pattern I keep criticising. **The difference is the gate; if the gate slips,
   I have become the thing I diagnosed.**

*Réttu hönd, eigi spyr. Standa.*
