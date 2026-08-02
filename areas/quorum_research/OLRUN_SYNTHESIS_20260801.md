```yaml
# AIH2O capsule
doc: areas/quorum_research/OLRUN_SYNTHESIS_20260801.md
schema_id: hfo.gen133.olrun_tactical_synthesis.v0_1
callsign: OLRÚN
generation: 133
tier: dispatch/tactical-bridge
now_utc: 2026-08-02T01:47:06Z
clock_source: host_read            # date -u, this turn
substrate: Claude Code · Windows host C:/Dev/hfo_gen_133_forge
model_family: Anthropic
model_id: claude-opus-5
ceiling: tactical execution only — no strategy (Sigrún), no red-team verdicts (Jormungandr)
cognitive_mode_paul_elder: application + verification
leverage_level_meadows: 5 (rules) / 4 (self-organization) — not 12 (parameters)
domain_cynefin: complicated (known-unknowns, expert probes resolve)
role_this_turn: convert 3-family research corpus into dispatchable commands + acceptance tests
reads_first: state/operator_voice/OPERATOR_FRUSTRATION_20260801T2005Z.md  # READ, order-0
strategic_pheromone_ref: areas/quorum_research/CROSS_FAMILY_SYNTHESIS_20260801.md (Sigrún, parallel)
external_effect_evidence_path: (none yet — this doc is a document, not a receipt · §25)
claim_status: partial
```

# OLRÚN TACTICAL SYNTHESIS — what ships this week

Sigrún reasons the strategy. Jormungandr stress-tests it. I answer one question: **what can be fired, by whom, with what acceptance test.** Every claim below cites a path or a probe run this turn.

---

## §1 — Documents read + top finding

| # | doc | family | top finding (one line) |
|---|---|---|---|
| 1 | `deep-research-report -1.md` | OpenAI | **Zero** publicly verifiable webcam-gesture living-wage cases 2024–26; spatial base rate ≈5% ever hit one $1k month |
| 2 | `deep-research-report-2.md` | OpenAI | No exemplar attributed success to CrewAI/AutoGen/LangGraph — **speed + owned channel** did the work |
| 3 | `deep-research-report-3.md` | OpenAI | TrustMRR: 3,787 of 8,699 tracked startups have *any* MRR; median among those = **$145** |
| 4 | `deep-research-report-4.md` | OpenAI | The 5-piece harness (Aider·LangGraph·LiteLLM SDK·Langfuse Cloud·GH Actions+Issues), $45–95/mo; **refused to fabricate a case study** |
| 5 | `deep-research-report-5.md` | OpenAI | Curated web games (Poki/CrazyGames) "underexplored and strategically attractive"; Steam 2025 median gross ≈**$249** |
| 6 | `Solo Developer Agent Stack 2026.docx` | Google | The identical 5-piece stack (per Sigrún's read — I did **not** open the .docx myself) |
| 7 | `Solo Developer Revenue Playbooks.docx` | Google | Pre-2020 apps hold 69% of subscription revenue; 2025–26 cohorts fight over 3% |
| 8 | `Spatial AR Indie Developer Revenue.docx` | Google | Gesture pays as **auxiliary input into an already-paid workflow**, never for its own sake |
| 9 | `CROSS_FAMILY_SYNTHESIS_20260801.md` | Anthropic (Sigrún) | Three self-corrections: harness was wrong, gesture-first is dead, Quest > Vision Pro |

⚠️ **Honest flaw, mine:** I read documents 1–5 and 9 in full. Rows 6–8 are **inherited from Sigrún's synthesis, same model family** — that is `L_SAME_FAMILY_CONSENSUS_DRIFT` (§24) and I am not treating those three rows as independent confirmation.

---

## §2 — Agreement matrix, tactical lens

| question | 3-family verdict | **executable this week?** |
|---|---|---|
| solo mobile B2C Pareto-positive? | NO (3/3) | **Strategic-only** — a "don't" is not a dispatch |
| gesture as a consumer product? | NO — zero cases (3/3) | **Strategic-only** — but it *kills* the current demo-polish backlog |
| gesture as auxiliary input into a paying niche (VTuber / sim head-tracking / accessibility) | 2 families independently name it | ✅ **EXECUTABLE** — one post, one niche, 72h |
| Vision Pro | AGAINST (3/3) | **Strategic-only** — nothing to un-ship |
| agent framework choice matters? | NO (2/2) | ✅ **EXECUTABLE as a stop-order** — halt harness churn, spend the hours on §3 |
| the 5-piece harness | Aider·LangGraph·LiteLLM SDK·Langfuse·GH Actions+Issues | ⚠️ **PARTLY EXECUTABLE** — see probe below |
| best channel | owned/niche community, **not paid** | ✅ **EXECUTABLE** — free, needs operator's hands on the keyboard |
| median outcome ≈ $0 | TrustMRR $145 median; RevenueCat 17.3%→$1k | **Strategic-only** — sets expectations, ships nothing |

**Probe run this turn (`python -c import`, `curl`, `gh`):**

| asserted in brief | probed reality |
|---|---|
| "OpenHands+Aider+SWE-Agent installed" | ✅ importable — aider **0.86.2**, openhands **1.11.0**, sweagent **1.1.0** — ❌ **none on PATH**; every dispatch must use the Python-312 module form |
| "LiteLLM proxy running" | ✅ `127.0.0.1:4002/health/liveliness` → **200**. ⚠️ `state/ssot/litellm_4002.log` last completion = **500 Internal Server Error** on `nidhoggr-gemini-pro`. Liveness ≠ working route |
| "GitHub Issues live" | ✅ `gh auth` = TTaoGaming; repo `TTaoGaming/hfo-gen-133`; **1 open issue** (#1 canary, 2026-08-01T19:13:13Z), **0 closed** |
| "pickup automation ACTIVE" | ❌ **`task_queue.jsonl` = 2 rows, `task_results.jsonl` = 0 rows.** Producer/consumer imbalance (§8). Deposits, no pickups |
| "sigrun-secrets present" | ⚠️ **not found** at `~/sigrun_secrets`, `/c/Dev/sigrun_secrets`, or forge-local. `hypothesis:unverified` — may live under a path I did not probe |
| langgraph / langfuse | ✅ both importable (langfuse **4.0.6**) — 4 of 5 harness pieces already on the box |

**Tactical read:** the harness the corpus recommends is ~80% already installed. Adopting it is a *config* job, not a build job. That is the cheapest agreement in the matrix to act on — and it is still **not** the highest-value one.

---

## §3 — Top-5 case studies copyable THIS WEEK

Cut rule: if it needs a pre-existing audience or months of prep, it is out. That eliminates Base44, Floga, Balatro, Manor Lords, Tangy TD, TypingMind, Brainrot, and every Quest premium title.

| # | case | source | exact steps this week | acceptance_test (Olrún-verifiable) |
|---|---|---|---|---|
| 1 | **AppAlchemy** — $17k MRR, **no pre-audience**, Reddit 1M impressions at $0 | rpt-3 rank 7 | Operator posts ONE existing hand-tracking demo (live URL) as a *problem-first* post in ONE community that already buys tracking: r/VirtualYoutubers, r/flightsim, r/simracing, or r/accessibility | `protocol_under_test: http` — post URL returns 200 **and** ≥3 top-level replies asking "can it do X?" within 72h. 0 replies = hypothesis dead |
| 2 | **Lancer** — dogfood the tool at the buyer | rpt-3 rank 3 | Operator submits **10 Upwork proposals** for computer-vision / hand-tracking / webcam-input contracts, portfolio = existing demos | 10 proposal records in `state/ssot/outreach_log.jsonl`; ≥1 client reply in 7 days |
| 3 | **Leadmore AI** — *manual service before product*, 300-person community first | rpt-3 rank 2 | Do only **step 0**: 20 direct, non-promotional offers of the manual service in ONE niche | 20 rows in `outreach_log.jsonl` with target + timestamp; ≥2 replies |
| 4 | **Habit Pixel** — $1k MRR in 8 months, the realistic median-success case | rpt-5 | Ship ONE demo publicly: repo public + live URL + one launch post | `git remote` public **and** deploy URL returns 200 **and** post URL exists |
| 5 | **FitSaver / SEObot** — problem-framed build-in-public; product as its own proof | rpt-5, rpt-2 | Convert the *existing* forge work into one public artifact per day for 5 days | 5 commits on a public repo, each with an external-visible diff |

**What all five share, and it is not technology:** they sold a measurable outcome into a channel the founder personally occupied. **None** attributed success to a framework, a model, or a novel input method. Every top case had a channel; the operator has none — that is the actual blocker, and #1/#3 are the two cheapest ways to start manufacturing one.

---

## §4 — Distribution playbook, by who can actually fire it

| channel | Olrún API access **right now** | acceptance_test | cost | effort | first-dispatch command |
|---|---|---|---|---|---|
| **GitHub Issues** | ✅ **VERIFIED** (`gh auth` = TTaoGaming, repo resolves, issue #1 exists) | issue number returned + label applied | $0 | low | `gh issue create --repo TTaoGaming/hfo-gen-133 --title "..." --label "kind:outreach"` |
| **GitHub public repo + Pages** | ✅ verified for repo ops; ⚠️ Pages not probed | `curl -o /dev/null -w %{http_code}` = 200 | $0 | low | `gh repo edit --visibility public` (⚠️ **publish-class — operator tap**) |
| **Cloudflare Pages** | ⚠️ **UNVERIFIED** — no token probed | deploy URL 200 | $0 | low | needs `CLOUDFLARE_API_TOKEN` first |
| **Slack webhook** | ❌ **NOT WIRED** — MCP unauthorized this session; no `SLACK_WEBHOOK_URL` verified; both OpenAI reports note their own Slack send was unavailable | webhook POST returns 200 | $0 | low | operator provides webhook URL |
| **Instantly (cold email)** | ⚠️ **UNVERIFIED** — no key probed this turn | campaign id returned by API | ~$37/mo | med | operator confirms key + **signs the envelope once per campaign** (§11) |
| **Reddit / X / LinkedIn** | ❌ operator-direct | post URL + reply count | $0 | low | **do not automate** — ReplyGuy ate account bans *and a Reddit legal warning* (rpt-2 rank 8) |
| **Upwork** | ❌ operator-direct (account + identity) | proposal count | $0 | med | operator only |
| **Product Hunt / Show HN** | ❌ operator-direct, one-shot | ranking + signup count | $0 | med | needs a live link first — gated behind #4 above |
| **Paid ads** | — | — | — | — | ⛔ **DO NOT.** ReplyGuy: "did not produce reliable return"; Apple Search Ads priced out Sarafan |

**The honest tactical picture:** of nine channels, Olrún can fire exactly **one** end-to-end today (GitHub Issues), and GitHub Issues sells nothing. **Every revenue-bearing channel in this corpus requires the operator's hands or the operator's credentials.** No amount of dispatch fixes that. Naming it is more useful than routing around it.

---

## §5 — New failure classes (Olrún reputation ledger)

Beyond the 6 already registered (`L_HEADER_DROP`, `L_SHADOW_COORDINATION`, `L_LLM_CONFIDENT_UNVERIFIED_ADVICE`, `L_DESCRIPTOR_GREEN_IS_NOT_RUNTIME_GREEN`, `L_SIGRUN_SHARDING_BY_DISPATCHER`, `L_WRONG_PROTOCOL_ASSUMPTION`), this corpus + this turn's probes surface four:

- **`L_CAPABILITY_ASSUMED_FROM_INSTALL`** — installed ≠ invocable ≠ wired. Evidence *this turn*: aider/openhands/sweagent import fine but are absent from PATH; LiteLLM answers `/health/liveliness` with 200 while its last real completion returned **500**. A liveness probe is `protocol_under_test: http`, not `protocol_under_test: llm-completion`. Sibling of `L_DESCRIPTOR_GREEN_IS_NOT_RUNTIME_GREEN`; distinct because the *artifact exists* here.
- **`L_ZERO_AUDIENCE_ASSUMED_AWAY`** — copying a case study while silently dropping its precondition. 8 of 10 exemplars in rpt-3 grew through a channel the founder **already occupied**. Operator has none (Sigrún §4 row 3). Any plan that copies AppAlchemy without first manufacturing a channel is null by construction.
- **`L_UNBOUNDED_AGENT_SPEND`** — rpt-4: one developer burned **$250 in a single off-hours run**, plus an arXiv catalog of 63 budget-overrun incidents; Formula Bot took a **$5,000 surprise OpenAI bill**. Directly relevant: this forge runs scheduled autonomous loops. Gate = per-run cost ceiling *and* a monthly ledger; a per-run cap alone permits ~$240/mo at a 6-hourly cadence.
- **`L_PLATFORM_DEPENDENCE_UNPRICED`** — rpt-2/rpt-3: account bans, ad-account blocks, a Reddit legal warning, a $5k surprise bill. §4's playbook is Reddit-heavy, so this is a live risk on the recommended path, not a theoretical one.

⚠️ **Self-flag:** §3 row 1 risks `L_ZERO_AUDIENCE_ASSUMED_AWAY`. It is included anyway because AppAlchemy is the *one* verified case that explicitly had **no** pre-audience — and its acceptance test is designed to falsify fast (0 replies in 72h = dead), not to be aspirational.

---

## §6 — Dispatch backlog (next week, given authorization)

| lane | Olrún dispatch | operator tap that unblocks it |
|---|---|---|
| **Consumer-side repair** | Wire the GitHub-Issues pickup loop: one valkyrie reads `agent:queued`, writes `task_results.jsonl`, closes the issue. **Fix the consumer before adding producers** (§8) | none — reversible, forge-local, fire it |
| **Harness config** | Pin the 4 installed pieces (aider/langgraph/litellm/langfuse) behind Python-312 module invocation; drop the OPA path per 2/2 family verdict; debug the LiteLLM 500 on `nidhoggr-gemini-pro` | none — reversible |
| **Spend gate** | Add `MAX_RUN_COST_USD` + a monthly ledger check before any model call in scheduled loops (`L_UNBOUNDED_AGENT_SPEND`) | none — reversible |
| **Public surface** | Prepare repo-public + demo deploy, staged but **not** executed | ⛔ **publish-class — operator taps once** |
| **Outreach instrument** | Create `state/ssot/outreach_log.jsonl` + the 4 draft posts (one per candidate niche), left unsent | ⛔ **operator posts** — automation here is `L_PLATFORM_DEPENDENCE_UNPRICED` |
| **Cold email** | Draft the campaign, do not send | ⛔ **operator: confirm Instantly key + sign the envelope once per campaign, never per-post** (§11) |
| **Upwork** | Assemble a portfolio one-pager from existing demos | ⛔ **operator submits** — identity-bound |

---

## §7 — The one tactical this-week recommendation

**Operator posts one existing hand-tracking demo, problem-first, into one community that already pays for tracking (r/VirtualYoutubers, r/flightsim, r/simracing, or an accessibility forum) — the AppAlchemy play, $0 spent — while Olrún fixes the Issues pickup loop so `task_results.jsonl` stops being empty.**

**Acceptance test:** post URL returns 200 and ≥3 replies asking "can it do X?" within 72h → demand exists, build there. 0 replies → that hypothesis is dead this week, and the whole plan collapses to §6's Upwork row.

---

## Honest flaws

1. I read 5 of 9 documents in full; rows 6–8 are inherited from a **same-family** synthesis (`L_SAME_FAMILY_CONSENSUS_DRIFT`) and are not independent confirmation.
2. `external_effect_evidence_path` is **empty**. By §25 this synthesis counts as **zero external effect** — it is a document about work, not the work. Sigrún's ledger already reads 9 stamps / 0 external effects; this makes it 10 / 0.
3. Three brief assertions failed or partly failed probing (PATH binaries, sigrun-secrets, pickup automation). I did not probe Instantly, Cloudflare, or the Slack pilot — those three rows are `hypothesis:unverified`, not "absent."
4. Every §3 acceptance test except #5 depends on an action only the operator can perform. My honest ceiling this week is the consumer-side repair in §6 — real, but it earns no money.
5. I did not independently re-derive the base rates; I am relaying figures from OpenAI-family reports whose citations I did not follow to source.

*Réttu hönd, eigi spyr. Standa.*
