```yaml
schema_id: hfo.quorum_research.internal.v0_1
family: anthropic
model: opus-5
authored_by: SIGRUN
source: capsules/tsukimogami/INCOME_PARETO_SOLO_DEV_20260801.md
consolidated_utc: 2026-08-02T01:15Z
clock_source: host_read
```

---

```yaml
# AIH2O capsule
doc: capsules/tsukimogami/INCOME_PARETO_SOLO_DEV_20260801.md
schema_id: hfo.gen133.income_pareto_solo_dev.v0_1
generation: 133
authored_by: SIGRÚN · claude-opus-5 · Claude Code
valid_time_utc: 2026-08-02T01:15:00Z
valid_until_utc: 2026-11-01T00:00:00Z
reads_first: state/operator_voice/OPERATOR_FRUSTRATION_20260801T2005Z.md   # read, order-0
extends: capsules/tsukimogami/PARETO_FRONTIER_SOLO_DEV_20260801.md        # does not duplicate
method: every case study web-searched 2026-08-01; unverified claims marked
claim_status: partial
```

# INCOME PARETO — solo dev, this month and this quarter

## §1 · Ranked income paths — and you've ranked yours upside-down

| # | path | time to $1 | P(income in 90d) | rate / size | source |
|---|---|---|---|---|---|
| **1** ⭐ | **Platform contract** (Toptal / Braintrust / Upwork) | ⭐ **5–7 days** (Toptal closes hires in 5–7 days) | **~0.6** | $60–200+/hr; Braintrust talent keeps **100%** of quoted rate, $100+/hr senior; Upwork US median **$100/hr** | [Second Talent 2026](https://www.secondtalent.com/resources/7-best-freelance-platforms-ai-developers/) · [Toptal vs Upwork](https://www.secondtalent.com/alternatives/toptal-vs-upwork/) |
| **2** ⭐ | ⭐ **A job — computer vision / spatial** | 4–10 weeks | ⭐ **~0.7, highest of any row** | ⭐ **$130k–$155k/yr**; Meta, Nvidia, Waymo hiring heavily for **hand tracking, spatial computing, AR interfaces** | [Built In 2026](https://builtin.com/articles/companies-hiring-computer-vision-engineers) |
| **3** | **Productized service** (fixed scope/price, e.g. "gesture demo for your product, 2 wks, $4k") | 2–6 weeks | ~0.45 | $2k–8k/engagement | [Assembly 2026](https://assembly.com/blog/productized-services) · [Indie Hackers](https://www.indiehackers.com/post/the-pros-and-cons-of-building-a-saas-vs-a-productized-service-business-eeaa6f3cca) |
| **4** | **Self-sourced consulting** (cold email, your own pipeline) | ⚠️ **3–6 months to first client** | ~0.3 | same rates, no platform cut | [Zen van Riel 2026](https://zenvanriel.com/job/how-to-become-ai-freelancer/) |
| **5** | **Grants (SBIR/NSF HCI)** | ⛔ **6–12 months to cash** | ~0.25 (submission ~0.9) | Phase I **$50k–$275k** | [OpenGrants 2026](https://opengrants.io/sbir-grants-2026-what-changed-whats-next/) |
| **6** ⛔ | **Apps / micro-SaaS** | ⛔ ⭐ **12–18 months median to $10k MRR** | ⛔ **~0.1 in 90d** | ⭐ **honest median: under $1,000/mo** | [BigIdeasDB 2026](https://bigideasdb.com/solo-developer-saas-monthly-revenue-examples) · [WhatToBuild](https://whattobuild.ai/blog/from-side-project-to-10k-mrr-patterns-from-successful-indie-makers) |

⭐ **The adversarial finding: your ranking is almost exactly inverted.** Apps are your
dream *and the slowest path measured* — median under $1,000/mo, 12–18 months to $10k MRR.
Meanwhile **your exact skill stack — hand tracking, gesture, MediaPipe, spatial input — is
what Meta, Nvidia and Waymo are hiring for at $130–155k right now.** You are sitting on a
scarce, in-demand specialization and building an agent swarm instead of selling it.

⭐ **The distinction that matters most in this table:** platform contracts close in **5–7
days**; self-sourced consulting takes **3–6 months**. Same work, same rate. **The
difference is who supplies the demand.** You have been building the self-sourced path —
the slow one — from scratch.

## §2 · How solo devs actually make money — 5 case studies

| who | built | monetization | scale | acquisition |
|---|---|---|---|---|
| **Nick Dobos** | 100+ small AI tools | paid apps/subs | ⭐ **~$733K/mo (~$8.8M ARR)** | ⭐ **volume + audience** — the closest published analogue to your factory | [CrazyBurst 2026](https://crazyburst.com/ai-saas-solo-founder-success-stories-2026/) |
| **Bhanu Teja — SiteGPT** | custom AI chatbots | SaaS sub | solo, significant MRR | solved one sharp pain a niche already paid to solve badly | *ibid.* |
| **TypingMind** | UI layer over LLMs | one-time + sub | single dev, significant MRR | build-in-public | *ibid.* |
| **Habit Pixel** | habit tracker | subscription | **$1K MRR in 8 months** | ⭐ **the realistic case, not the outlier** | [Indie Hackers](https://www.indiehackers.com/post/from-0-to-1k-mrr-in-8-months-bootstrapping-habit-pixel-as-a-solo-dev-53d8687d15) |
| **Lisbon solo founder** | micro-SaaS | subscription | **$10K MRR in 47 days** | ⛔ **extreme outlier — do not plan against this** | [WhatToBuild](https://whattobuild.ai/blog/from-side-project-to-10k-mrr-patterns-from-successful-indie-makers) |

⭐ **Survivorship warning, stated plainly:** rows 1 and 5 are the reason this category
*feels* achievable. **The honest median for an indie app is under $1,000/month**, and a
realistic top-quartile solo result is **$3k–$15k/mo after 12–18 months**. Nick Dobos is
not a plan; he is a lottery ticket with a good process.

**What every winner has in common** (and what you don't yet): *"the single factor that
predicts success is whether it solves a real, recurring, painful problem for a specific
niche"* — founders win when they build **something a defined group already pays to solve
badly.** ⭐ **Your demos are technically excellent and have no named buyer.** That is the
gap, not the code.

## §3 · Instantly — ⭐ KEEP, and for a reason you haven't used

**Verdict: KEEP. Do not swap.** [2026 comparisons](https://puzzleinbox.com/blog/smartlead-vs-instantly-vs-lemlist-2026-three-way) put it plainly: Smartlead wins on agency economics, Lemlist on multi-channel — ⭐ **"for founders running their own outbound with built-in lead sourcing, Instantly typically wins,"** and for solo/small teams doing email-only, **Instantly is the recommendation**. *(Pricing context: [Smartlead $39/$94/$174+](https://netpartners.marketing/cold-email-software-2026-smartlead-instantly-lemlist-comparison/), Lemlist $39/$69/$109+ per seat.)*

⭐ **The finding you should act on tonight: Instantly Growth includes a 160M-contact B2B
lead database.** Your measured critical-path blocker is **44 dossiers × 0 named humans.**
**You are already paying for the exact solution to your blocker and have not opened it.**

**Break-even:** $47/mo ÷ $100/hr = ⭐ **28 minutes of billable work.** One reply → one call
→ one 1-hour engagement pays for **two months**. At a 5–15% reply rate, 40 emails ≈ 2–6
conversations. **This tool is not the question. Using it is.**

⛔ **Add nothing.** Not Smartlead, not Lemlist, not Apollo — Instantly's included database
covers it.

## §4 · Distribution, ranked

| # | channel | evidence | failure mode |
|---|---|---|---|
| **1** ⭐ | ⭐ **Show HN** | *"can drive more high-intent traffic than any other channel for technical products"* | one shot; a weak title kills it; needs a working link, not a waitlist |
| **2** | **Build in public** — ⭐ 3–5 posts/wk, one platform, **sustained 90 days**; mix ≈ 40% real numbers, 30% lessons, 20% process, 10% asks | [SoftwareSeni 2026](https://www.softwareseni.com/building-in-public-the-10-year-distribution-strategy-behind-solo-founder-revenue/) · [Lishchuk 2026](https://lishchuk.com/blog/solo-founder-marketing-playbook-2026.html) | ⭐ **slow — compounds over months, pays nothing in week 1** |
| **3** | **Cold email (Instantly)** | 5–15% reply personalized; *43 emails → 17 replies → 1 paid* | generic templates → ~2/50; **needs a per-prospect signal note** |
| **4** | **Product Hunt** | ⭐ **earn it after 60–90 days of presence**; Top-5 ≈ **1,500 visits / 120 signups** | ⛔ launching cold on day 1 is the classic waste |
| **5** | **GitHub demo repos as marketing** | your demos are already this shape | discovery is passive |

⭐ **For income in 30 days, only #1 and #3 are fast enough.** #2 and #4 are quarter-scale
and should run in the background from now, because they take 90 days to turn on.
*(Launch mechanics: [Foundra 2026](https://www.foundra.ai/key-reads/product-hunt-playbook-first-time-founders-2026-after-algorithm-shift), [Beyond Product Hunt](https://dev.to/lightningdev123/beyond-product-hunt-a-technical-launch-guide-for-2026-i2j).)*

## §5 · Your braid — which half pays this quarter

- **(a) Agent swarm + continuity + factory** → ⛔ **pays nothing this quarter.** Prior capsule: **~2%** as stated. ⭐ **But it is not worthless — it is your build-in-public content and your differentiator in a contract pitch.** "I run a multi-agent factory that ships spatial demos" is a *credential*, not a product.
- **(b) Spatial input / tool virtualization, 2D first** → ⭐ **this is the income half — but NOT as apps.**

⭐ **The reframe that resolves the braid: your demos are not products. They are proof.**
Their income function is to win a **contract** or a **job**, not to earn $5/mo in
subscriptions. That's why the factory matters and why app-store monetization doesn't:
**five polished spatial demos are a portfolio that closes a $100/hr contract in a week;
the same five as paid apps earn under $1,000/mo in a year.**

Keep (a) alive as: a public repo, a weekly build-in-public post, and one line in every
pitch. **Do not let it consume a single billable hour this quarter.**

## §6 · Ranked action list — sequence, not options

**THIS WEEK** — in order, do not parallelize:
1. ⭐ **Open Instantly's lead database, export 40 named humans** in one niche (spatial/AR product teams, agencies with camera-input needs). ✅ `wc -l` ≥ 40 with name+role+company.
2. ⭐ **Apply to Toptal AND Braintrust** as an AI/computer-vision engineer. ✅ both applications submitted. **This is the 5–7-day path — it must start on day 1.**
3. **Ship 3–5 spatial demos to public URLs + one portfolio page.** ✅ each `curl -sI` → 200. *(This is your proof asset for #1 and #2, not a product.)*

**THIS MONTH:**
1. **Show HN** the portfolio page once ≥3 demos are live. ✅ post submitted, traffic measured.
2. **Send the 40 emails**, per-prospect signal note, pitching a **productized service** (fixed scope, fixed price). ✅ ≥2 replies.
3. ⭐ **Apply to 5 computer-vision / spatial roles** at companies hiring hand-tracking. ✅ 5 applications. **Highest-probability row in §1 and it costs a weekend.**

**THIS QUARTER:**
1. ⭐ **Close one $2k–8k contract or accept one role.** ✅ signed SOW or offer.
2. **Submit one SBIR/NSF HCI Phase I** (spatial/wearable interfaces is an explicit NSF topic). ✅ submission receipt. *Cash lands next year — submit anyway.*
3. **Build-in-public, 3–5 posts/wk for 90 days.** ✅ 40+ posts. *Turns on around month 3.*

---

> ⭐ **THE ONE SENTENCE: Apply to Toptal and Braintrust this week and export 40 named
> humans from the lead database you are already paying for — because your hand-tracking
> and spatial skills sell for $100+/hr in 5–7 days on a platform, while the same skills
> sold as apps take 12–18 months to reach a median under $1,000/month.**

## §7 · ⭐ Probability landscape — adversarial-Bayesian, with a budget of $1–3k

**Constraint update:** budget ≈ **few thousand $**, and you are a **heavy AI-tool power
user** with existing demos. Both change the table. Posteriors are P(**$2k+ in that
month**).

---

### **P1 · Platform contract** (Toptal / Braintrust / Upwork)
**Prior 0.40** — skilled dev, scarce niche, but platforms are a filter.
**FOR:** [Toptal closes hires in 5–7 days](https://www.secondtalent.com/alternatives/toptal-vs-upwork/); Braintrust talent keeps **100%** of quoted rate; US median **$100/hr**.
**AGAINST:** Toptal screening is selective and **no 2026 acceptance rate is published**; Upwork cold-start needs reviews before rates hold.
**Posterior: m1 0.30 · m3 0.60 · m12 0.80** · **EV $2k–12k/mo** (20–40 billable hrs)
⭐ **Budget unlock ($300–800):** portfolio domain + polished profile + Upwork Connects. **Mostly free — this path is gated on effort, not money.**
**Exemplar:** [Masato Hagiwara, first year freelance AI engineer](https://masatohagiwara.net/202002-my-first-year-as-a-freelance-ai-engineer.html) *(pre-2026, flagged)*

### **P2 · Job — computer vision / spatial**
**Prior 0.50.**
**FOR:** [$130k–155k; Meta, Nvidia, Waymo hiring hand-tracking + spatial](https://builtin.com/articles/companies-hiring-computer-vision-engineers) — your literal stack.
**AGAINST:** 4–10 week cycles; ⛔ **cannot produce month-1 cash**; ends the solo path.
**Posterior: m1 0.05 · m3 0.45 · m12 0.75** · **EV ~$11–13k/mo, lowest variance of any row**
**Budget unlock: ~$0.** Money does not accelerate this.

### **P3 · Productized AI/spatial service** ⭐
**Prior 0.35.**
**FOR:** [per-project **$2k–20k**, retainers **$500–5k/mo**](https://www.mindstudio.ai/blog/start-ai-automation-business-case-studies); solo productized operators land **$50k–300k ARR**; ⭐ *"niche-specific, deeply specialized automation businesses are not crowded."*
**AGAINST:** needs a named niche and a pipeline — **you have 0 named humans today.**
**Posterior: m1 0.20 · m3 0.50 · m12 0.70** · **EV $2k–18k/mo**
⭐ **Budget unlock ($600/qtr) — the best money-to-outcome ratio in this table:** [Apollo from **$49/mo**](https://medium.com/@AITools4Businesses/apollo-io-vs-linkedin-sales-navigator-which-prospecting-tool-is-worth-it-in-2026-39a43db8f205) (prospecting + outreach in one) + Instantly (owned) + a domain.
**Exemplars:** ⭐ **Chris Lee — AI automation freelancer, $6,000/mo on $20/mo of tools** · podcast-ops operator, **$3,000/mo × 6 clients = $18,000/mo** — [MindStudio 2026](https://www.mindstudio.ai/blog/start-ai-automation-business-case-studies)

### **P4 · Grants (SBIR / NSF HCI)**
**Prior 0.18** — [NSF Phase I funding rate ≈ **18%**](https://grantsights.com/blog/sbir-phase-1-grant-guide).
**FOR:** Phase I **$50k–275k**; NSF HCI explicitly covers spatial/wearable interfaces; reauthorized through 2031; ⭐ **a Project Pitch can be professionally written for [$349 (48-h SLA) to $495](https://fundunlocked.com/best-sbir-grant-writing-services-2026/)**.
**AGAINST:** ⛔ **6–12 months to cash** · a full NSF Phase I application runs **$5,995** · ⛔ **success/contingency fees are unallowable under FAR 31.205-33(f)** — anyone offering "pay only if you win" is out of compliance.
**Posterior (CASH): m1 ~0.00 · m3 ~0.02 · m12 0.15–0.20** · **EV ≈ 0.18 × $150k ≈ $27k, delayed**
⭐ **Budget unlock ($349–495): the single highest-leverage dollar in this entire landscape** — ~$400 buys a professionally-written pitch at the gate of a $50–275k award. **Do this even though it pays nothing this quarter.**

### **P5 · Apps / micro-SaaS**
**Prior 0.15.**
**FOR:** outliers real — [Nick Dobos ~$733K/mo](https://crazyburst.com/ai-saas-solo-founder-success-stories-2026/).
**AGAINST:** ⛔ [**median under $1,000/mo**](https://bigideasdb.com/solo-developer-saas-monthly-revenue-examples); 12–18 months to $10k MRR.
**Posterior: m1 0.03 · m3 0.08 · m12 0.30** · **EV $0–3k/mo, highest variance**
**Budget unlock: ~$20/mo.** ⭐ **Money cannot buy speed here — only time can.**

### **P6 · Content / audience**
**Prior 0.20.**
**FOR:** teach-as-you-learn converts followers into first customers; compounds indefinitely.
**AGAINST:** ⛔ **90 days minimum before it turns on**; monetization indirect.
**Posterior: m1 0.02 · m3 0.10 · m12 0.35** · **EV $0–4k/mo**
**Budget unlock: ~$0.** ⛔ **Do not buy ads.**

---

| | m1 | m3 | m12 | budget leverage |
|---|---|---|---|---|
| **P1 platform contract** | ⭐ **0.30** | 0.60 | 0.80 | low (effort-gated) |
| **P2 job** | 0.05 | 0.45 | ⭐ **0.75** | none |
| **P3 productized service** | 0.20 | 0.50 | 0.70 | ⭐ **highest** |
| **P4 grants** | 0.00 | 0.02 | 0.15–0.20 | ⭐ **$400 → $50–275k gate** |
| **P5 apps** | 0.03 | 0.08 | 0.30 | none |
| **P6 content** | 0.02 | 0.10 | 0.35 | none |

⭐ **Read the budget column, not the probability column.** Money moves **exactly two rows**:
P3 (~$600/qtr) and P4 (~$400 once). **Everything else is time and effort, which is why
having a few thousand dollars changes less than it feels like it should — and why spending
it on more tooling would be the single easiest way to waste it.**

⛔ **What NOT to buy:** [Sales Navigator at $119.99–159.99/mo](https://overloop.com/blog/linkedin-sales-navigator-pricing) — it **excludes emails and phone numbers on every tier**, has **no API**, caps CSV export at 2,500, and its real annual cost is **$2,880+** with enrichment. It only pays back if you close **one extra $5k+ deal per quarter**. ⭐ **Apollo at $49/mo does prospecting *and* outreach; Instantly's included database may cover it entirely. Skip Sales Nav.**

## §8 · Highest-EV actions, given the budget and your tool proficiency

⭐ **The insight that unifies your vision and your income:** *"spatial inputs into existing
apps for total tool virtualization"* **is not an app idea. It is a productized service** —
**"I add gesture/camera control to your existing product. Fixed scope, 2 weeks, $4–8k."**
That is simultaneously your stated long-term vision, income path **P3** (per-project
$2k–20k), and the thing your demos already prove you can do. ⭐ **Your demos stop being
unsold products and become the sales collateral for a service that is already priced by
the market.**

**THIS WEEK — highest EV, ~$400–900 total:**
1. **Apply to Toptal + Braintrust** *(free, 5–7 day path, must start day 1)*
2. ⭐ **Buy a $349–495 NSF SBIR Project Pitch write-up** — best dollar in the landscape
3. **Export 40 named humans** from Instantly's database *(owned)*; add Apollo $49 only if it's thin

**THIS QUARTER — highest EV:**
⭐ **Land 1–2 productized "gesture layer for your app" engagements at $4–8k**, using the 5
demos as proof. **Comparable: Chris Lee, $6,000/mo on $20/mo of tools.** Two retainers at
$3k/mo is the podcast operator's model at one-third scale — and it is **$72k/yr from a
service you can already deliver.**

---

> ⭐ **THE ONE SENTENCE (budget version): spend ~$400 on an NSF SBIR Project Pitch and ~$0
> applying to Toptal and Braintrust this week, then sell "gesture/camera control added to
> your existing app, 2 weeks, $4–8k fixed" — because that single offer is your tool-
> virtualization vision, the $2k–20k-per-project market rate, and the only use of your
> demos that pays inside 90 days.**

## Honest flaws

0. ⭐ **§7's posteriors are calibrated judgment anchored to sourced base rates — they are
   not computed, and I did not run a formal Bayesian update.** The priors are my estimates;
   only P4's 0.18 is an externally published rate. **Treat the ordering as the finding, not
   the decimals.** Also: the 41.2% Phase I success rate advertised by one consultancy is
   self-reported marketing against an 18% national baseline — **do not plan against it.**
1. ⭐ **I am telling you to take contracts or a job when you asked how to build a factory.**
   That is the honest read of the evidence and you may reasonably reject it — **but reject
   it knowing apps are a ~0.1 probability of income in 90 days and a job is ~0.7.**
2. **Probabilities are calibrated judgment**, anchored on sourced base rates. Not computed.
3. **Toptal's "5–7 day" close is time-to-*hire-after-acceptance*, and Toptal screening is
   selective** — I did not find a 2026 acceptance rate. ⚠️ **The 5–7 days may follow a
   multi-week vetting process. Treat row 1 as fastest-if-accepted.**
4. **No 2026 case study of a *gesture/hand-tracking* solo dev monetizing was found** —
   searched, absent. Your niche's monetization is **inferred from adjacent categories.**
   ⚠️ That could mean an underserved niche, or one with no buyers. **I cannot tell you which.**
5. **The Instantly 160M-contact figure comes from Instantly-adjacent comparison content** —
   verify the number inside your own dashboard before planning against it.
6. **Thirteen artifacts from me today.** ⭐ **Every action in §6 is something you do without me.**

*Réttu hönd, eigi spyr. Standa.*
