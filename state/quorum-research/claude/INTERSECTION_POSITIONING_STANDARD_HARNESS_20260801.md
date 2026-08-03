```yaml
schema_id: hfo.quorum_research.internal.v0_1
family: anthropic
model: opus-5
authored_by: SIGRUN
source: capsules/tsukimogami/INTERSECTION_POSITIONING_STANDARD_HARNESS_20260801.md
consolidated_utc: 2026-08-02T01:15Z
clock_source: host_read
```

---

```yaml
# AIH2O capsule
doc: capsules/tsukimogami/INTERSECTION_POSITIONING_STANDARD_HARNESS_20260801.md
schema_id: hfo.gen133.intersection_standard_harness.v0_1
generation: 133
authored_by: SIGRÚN · claude-opus-5 · Claude Code
valid_time_utc: 2026-08-02T02:15:00Z
valid_until_utc: 2026-09-01T00:00:00Z
reads_first: state/operator_voice/OPERATOR_FRUSTRATION_20260801T2005Z.md   # read, order-0
extends: PARETO_FRONTIER_SOLO_DEV_20260801.md · INCOME_PARETO_SOLO_DEV_20260801.md
section_D_status: ⛔ OPEN — 3 research valkyries are at WAKE-RECEIPT only, no results landed
claim_status: partial
```

# INTERSECTION POSITIONING + THE STANDARD HARNESS PIVOT

## §A · Is your intersection real, or are you flattering yourself?

**Both. And the distinction is worth about $200/hr.**

**The premium is real and measured:**

| finding | source |
|---|---|
| **52% of niche specialists** charge **$10,000+/project** vs **18% of generalists** | [Data-Mania 2026](https://www.data-mania.com/blog/consulting-rate-card-2026-templates-pricing-menu/) |
| ⭐ **every profession surveyed showed a 130–200% premium** when freelancers narrowed to a niche | [Damongo 2026](https://damongo.com/how-to-launch-a-niche-freelance-practice-the-complete-guide-to-specialize-and-command-premium-rates-in-2026/) |
| entry $75–150/hr · experienced $150–300/hr · ⭐ **niche expert $300–500+/hr** | [ConsultFees 2026](https://consultfees.com/blog/how-much-to-charge-as-a-consultant) |
| specialist firms **42.6% profitability** vs 22.8% | [100Signals 2026](https://100signals.com/best-positioning-agencies-for-consulting-firms/) |

⭐ **Now the adversarial cut, and it is the most useful sentence in this capsule:**

> **The premium accrues to the NICHE — a named customer segment with a problem they
> already pay to solve — NOT to the skill combination.**

*"Spatial + gesture + AI + agent-swarms + web-apps"* is a **skill list.** Nobody searches
for it, nobody budgets for it, and it prices at **generic AI engineer, ~$100/hr — or $0,
because the buyer can't tell what to hire you for.** ⭐ **You are currently qualified for
exactly none of the 130–200% premium, and the reason is positioning, not capability.**

*"Hands-free gesture control for **[vertical]** software"* is a **niche.** Same skills,
$300–500/hr band, and clients self-qualify — *"only those with serious budgets respond,
saving 10–15 hours/month"* once pricing is public.

**Vertical candidates, ranked by whether a budget already exists** *(hypotheses — none tested):*
1. ⭐ **Accessibility / hands-free control for motor impairment** — ⭐ **regulatory pull (ADA/WCAG) creates a compliance budget line**, which is the strongest form of pre-existing demand
2. **Clinical / rehab & physical therapy software** — measurable outcomes, existing vendors
3. **Industrial / field ops** — gloved or dirty hands, touchscreens fail
4. **Kiosk / retail** — hygiene-driven, post-2020 budgets exist

⭐ **One decision — name the vertical — converts a $100/hr generalist into a $300/hr
specialist candidate. It costs nothing and it is the highest-ROI hour in this document.**

## §B · Custom harness → standard harness, mapped

⭐ **Read this first: you are not throwing away 18 months.** The Norse register, the
doctrine, the L-vectors, the drápa — those are **positioning and content**, and they cost
nothing to keep. ⭐ **What is expensive is the custom RUNTIME. Keep the vocabulary,
replace the plumbing.**

| your custom thing | industry standard | pivot cost | what survives |
|---|---|---|---|
| `CLAUDE.md` · `soul.md` · skills | ⭐ **`AGENTS.md`** — OpenAI Aug 2025 → **Linux Foundation AAIF**; read natively by **Claude Code, Codex CLI, Cursor, Aider, Devin, Copilot, Gemini CLI, Windsurf, Amazon Q**; **60,000+ repos**, 170+ AAIF members | ⭐ **~1 hour** | ⭐ **all content — you gain 9 tools reading one file** ([spec](https://www.morphllm.com/agents-md-guide) · [field guide](https://www.iuriio.com/blog/posts/2026/05/agents-md-field-guide-2026)) |
| apex / valkyrie hierarchy | OpenHands microagents · CrewAI roles | ~1 day | ⭐ **the NAMES are free — keep them; drop the custom dispatch runtime** |
| `chains/*.jsonl` | **Langfuse** traces (OpenTelemetry) | ~2 h | keep chains as narrative/audit; Langfuse carries the *measurable* part |
| stigmergy pheromones | **GitHub Issues + Actions** | ~2 h | already adjudicated as the one golden path |
| `litellm_config.yaml` | ⭐ **already the standard — change nothing** | 0 | everything |
| Sigrún consumer bootstrap | `AGENTS.md` + an OpenHands microagent | ~2 h | the doctrine, verbatim |

⭐ **Total pivot: roughly two days, and `AGENTS.md` alone is one hour for most of the
benefit.** That is the entire "custom → standard" migration you've been dreading.

## §C · Plug your existing subscriptions into off-the-shelf products

You already hold: Claude Max · Codex · ChatGPT cloud · Antigravity · Ollama · **LiteLLM
(running)** · Instantly · Cloudflare · GitHub · Slack.

| # | product | plugs into | cost | install |
|---|---|---|---|---|
| **1** | ⭐ **OpenHands** — 72k+ stars, **$18.8M Series A**, in production at **AMD, Apple, Google, Amazon, Netflix, NVIDIA**; ⭐ **model-agnostic *through LiteLLM*** | ⭐ **every subscription you own, via the proxy you already run** | **$0** | ✅ installed (v1.11.0) |
| **2** | **Langfuse** — OSS observability/evals/prompt mgmt; native **LiteLLM** + OpenTelemetry integration | LiteLLM proxy | **$0** self-host / free tier | `docker compose up` ([repo](https://github.com/langfuse/langfuse)) |
| **3** | **AGENTS.md** | all 9 agent tools | **$0** | one file |
| **4** | **GitHub Actions** | repo you own | **$0** | `.github/workflows/` |
| **5** | **Cloudflare Pages** | proven path | **$0** | `wrangler pages deploy` |

⭐ **Total: $0/month.** The thing you were building custom coordination for is **already
assembled and named** — see §E.

## §D · Offer refinement — ⛔ OPEN, awaiting the three valkyries

⛔ **I checked the inbox: `research_valkyrie_spatial`, `research_valkyrie_indie_games`,
and `research_valkyrie_ai_agent_commercial` have posted WAKE RECEIPTS ONLY. No results
have landed. I am not going to invent their findings** — that is precisely the
second-hand-premise failure this forge has been bitten by twice today.

**What §D will decide when they land:** whether the standing offer stays *"gesture/camera
control added to your existing app — 2 weeks, $4–8k fixed"* or moves toward mobile, games,
or agent-consulting.

**Falsifiers, pre-registered now so the valkyrie data can't be rationalized after the fact:**

| offer | ⛔ KILL IF |
|---|---|
| gesture-layer service $4–8k | 40 emails → **0 replies** ⇒ no buyer at this framing |
| mobile/games app | valkyries show median revenue **< $500/mo** ⇒ dead on timing (matches my prior finding) |
| agent-consulting | no 2026 exemplar earning **>$5k/mo** on multi-agent specifically ⇒ market is vendors, not consultants |

⭐ **The pre-registration is the point.** Whatever they report, the decision rule is
already written down.

## §E · The standardized harness — pick this one

> ⭐ **The stack you were building custom already exists, is named, and is documented:
> the [Open Source LLMOps Stack](https://oss-llmops-stack.com/) — LiteLLM + Langfuse.**
> **You are already running half of it.**

```
┌ agent runtime ── OpenHands  (Docker sandbox per session)   ✅ installed
├ model gateway ── LiteLLM    (all your families, one API)   ✅ RUNNING, live-tested
├ observability ─ Langfuse    (traces, evals, prompts)       ⬜ docker compose up
├ instructions ── AGENTS.md   (9 tools read one file)        ⬜ 1 hour
├ coordination ── GitHub Issues + Actions                    ⬜ 0 issues opened
└ deploy ──────── Cloudflare Pages                           ✅ proven (demo01 → 200)
```

**Cost: $0/mo + tokens.** *(Budget said <$50 — this comes in under it by $50.)*
**Exemplars shipping on it:** AMD, Apple, Google, Amazon, Netflix, NVIDIA run OpenHands in
production; the LiteLLM+Langfuse pairing is the published OSS LLMOps reference stack.
*Sources: [OpenHands 2026 review](https://pickuma.com/for-dev/openhands-review-open-source-autonomous-coding-agent-2026/) · [Langfuse agent-framework comparison](https://langfuse.com/blog/2025-03-19-ai-agent-comparison) · [Open-source agent stack per layer, 2026](https://theaiengineer.substack.com/p/the-open-source-agent-toolkit-in).*

⭐ **Two remaining gaps, both ~2 hours: `docker compose up` for Langfuse, and one
`AGENTS.md`.** That is the whole pivot.

## §F · The one sentence

> ⭐ **Name one vertical this week — "hands-free gesture control for accessibility/clinical
> software" — write one `AGENTS.md`, and `docker compose up` Langfuse; because your skills
> price at $100/hr as a skill list and $300–500/hr as a named niche, and the harness you
> spent 18 months building custom is a $0, two-day install called the Open Source LLMOps
> Stack.**

## Honest flaws

1. ⛔ ⭐ **§D is genuinely unfinished** and it is the section that decides what you sell.
   Everything else here is positioning and plumbing. **Do not let §A–§E feel like a
   conclusion — the offer is still unvalidated.**
2. ⭐ **The vertical list in §A is four untested hypotheses.** I ranked accessibility first
   because regulatory pull implies a budget line, and **that is inference, not evidence.**
   I found **no 2026 case study of anyone monetizing gesture control in any vertical** —
   third capsule running where that search comes back empty. ⭐ **That repeated absence is
   now itself the most important open question in your business**, and it cuts both ways:
   underserved niche, or no buyers.
3. **The 130–200% niche premium comes from consulting-industry marketing content**, which
   has an obvious interest in selling specialization. Directionally consistent across four
   independent sources; **not audited.**
4. **"Two days to pivot" is my estimate**, not measured. `AGENTS.md` is genuinely ~1 hour;
   the OpenHands/Langfuse wiring could be a day or a week depending on Docker friction —
   and this host already produced one real dependency conflict today (aider/litellm).
5. **I recommend OpenHands as the runtime without having run a single OpenHands task.**
   Install verified, capability not — flagged for the third time.
6. **Fifteen artifacts from this seat today.** Every action in §F is one you take without me.

*Réttu hönd, eigi spyr. Standa.*
