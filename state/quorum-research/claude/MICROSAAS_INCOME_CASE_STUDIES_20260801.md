```yaml
schema_id: hfo.quorum_research.internal.v0_1
family: anthropic
model: sonnet-5
source: capsules/research/MICROSAAS_INCOME_CASE_STUDIES_20260801.md
consolidated_utc: 2026-08-02T01:15Z
clock_source: host_read
```

---

# Micro-SaaS Income Case Studies — Solo Dev Distribution + Monetization Playbook

- agent: sonnet-5, HFO gen-133, research valkyrie (compose lane, no code-touch)
- date: 2026-08-01
- clock_source: host_read
- timebox: 30 min
- data file: `state/research/microsaas_income_cases_20260801.jsonl`
- rehydration read-order-0: **read [[operator-recurring-context]] / operator frustration file first** if picking this back up cold — this capsule is standalone data, not a decision.

⚠️ UNVERIFIED-CLASS NOTE: all figures below are self-reported by founders (Twitter/X posts, personal blogs, Indie Hackers posts) or aggregator writeups citing those self-reports. None are independently audited (no Stripe Atlas public dashboards were found live). Treat as directional, not ground truth. Truthful-red > false-green.

## Top-5 Solo-SaaS Exemplars 2026 (with revenue receipts)

| Case | Founder | Product | Revenue | Time to milestone | Channel |
|---|---|---|---|---|---|
| [Photo AI](https://www.indiehackers.com/post/photo-ai-by-pieter-levels-complete-deep-dive-case-study-0-to-132k-mrr-in-18-months-3a9a2b1579) | Pieter Levels | AI photo generation | $100K-$150K MRR (peaked $150K, [stabilized ~$100K](https://inspectural.com/blog/levelsio-photoai-single-file-php/)) | 18 mo to $132K | Twitter/X (pre-built audience) |
| [Marc Lou portfolio](https://indieai.directory/blog/marc-lou-81683-february-2026-income-breakdown/) | Marc Lou | ShipFast + DataFast + TrustMRR + CodeFast | $81.7K (Feb 2026) / $94.8K (Jan 2026) combined | ~4 mo per new product launch cadence | Twitter/X + newsletter |
| [Plausible Analytics](https://plausible.io/blog/growing-saas-mrr) | Uku Täht (+ Marko Saric) | Privacy-first web analytics | $10K MRR at 9 mo; [$1M ARR by 2022, ~$3.1-3.5M ARR 2024-25](https://churnkey.co/subscription-heroes/how-plausible-grew-to-1m-arr-without-ads-or-investors-marko-saric-co-founder-of-plausible/) | 9 mo to $10K MRR | SEO + open-source trust |
| [Leadmore AI](https://rethinklab.co/blog/from-0-to-10k-mrr-a-2026-indie-hacker-playbook) | solo (unnamed) | B2B AI outbound marketing | $30K+ MRR, growing | ~12 mo | Cold email (dogfooded own product) |
| [35-app portfolio](https://www.buildmvpfast.com/blog/solo-developer-35-micro-saas-apps-77k-month-portfolio-2026) | solo (unnamed) | 35 "boring problem" SaaS tools | $77K/mo aggregate | n/a (volume strategy) | SEO (long-tail) |

Also referenced for context (not full case rows): [8 solo founders at $20K-$62K MRR](https://medium.com/@tamimbuilds/8-solo-founders-who-quietly-hit-20k-62k-mrr-in-the-last-6-months-5032e610badc); [$602K solo indie hacker portfolio breakdown](https://www.buildmvpfast.com/blog/602k-revenue-solo-indie-hacker-app-portfolio-breakdown-2026); [one solo founder at $125K MRR / ~$1.5M run rate](https://www.indiehackers.com/post/hitting-125k-mrr-as-a-solo-founder-by-doubling-down-on-the-right-segment-c4o2Tfs6mjdpip5yZhaO).

## Distribution Channel Breakdown — ranked by what actually drove ARR

1. **Pre-built personal audience (Twitter/X, "build in public")** — the single strongest correlate across the biggest winners (Photo AI, Marc Lou portfolio). This isn't a channel you turn on; it's a multi-year asset built *before* the product existed. [Source](https://prems.ai/blog/indie-hacker-marketing-playbook-2026).
2. **SEO / content** — cited as the highest-ROI channel available to founders with no existing audience: "SEO content delivers 702% ROI over 3 years" ([source](https://prems.ai/blog/indie-hacker-marketing-playbook-2026)). Plausible and the 35-app portfolio both rode long-tail organic search rather than paid or social.
3. **Community + intent signals** — "someone complaining about a problem in a forum is worth 100 cold emails to people who might have the problem someday" ([ShippedSolo](https://shippedsolo.com/blog/12-free-distribution-channels-for-indie-hackers/)); founders active in community 6 months pre-launch convert 3-5x better than cold outreach.
4. **Product Hunt** — high variance, best used as an amplifier once you already have ~1,000+ email list / niche authority, not as the primary strategy ([Launchedly](https://launchedly.app/blog/why-product-hunt-killed-indie-makers)).
5. **Cold email** — weakest of the channels surveyed for 2026; still used successfully in B2B niches (Leadmore AI) but consistently ranked below intent-based/community approaches by practitioners.

**The 80/20 as stated by practitioners:** Reddit + Twitter/X + Product Hunt give ~80% of the value for ~20% of the effort — but only *after* an audience or niche-authority base exists. Without that base, SEO/content is the more replicable cold-start channel.

## Time-to-first-dollar / time-to-milestone (median across cases)

- Median time to **$10K MRR**: **12-18 months** from first paying customer; top performers 6-9 months ([source](https://www.indiehackers.com/post/hitting-125k-mrr-as-a-solo-founder-by-doubling-down-on-the-right-segment-c4o2Tfs6mjdpip5yZhaO)).
- 85% of tracked indie founders bootstrap to $10K MRR before ever taking outside funding; typical span is 6-18 months from first line of code ([bigideasdb](https://bigideasdb.com/bootstrapping-a-company-in-2026)).
- Base-rate reality check: **82% of micro-SaaS products never reach $5K/mo; 93% never reach $10K/mo.** The five exemplars above are survivorship-biased outliers, not the median outcome.

## Pricing model that dominates for solo

- **B2B self-serve subscription, $49-99/mo per seat** is repeatedly cited as the "sweet spot" — few enough customers needed to hit meaningful MRR, high enough price to justify support time ([SoftwareSeni](https://www.softwareseni.com/solo-founder-saas-metrics-from-0-to-10k-mrr-in-6-months-with-realistic-timelines/)).
- Consumer/prosumer tools cluster at **$9-29/mo** (35-app portfolio) — needs higher volume but larger addressable market and pure SEO-driven acquisition.
- **70-90% net margins are the norm** for solo bootstrapped SaaS (no employees; costs are hosting $30-200/mo + API usage + 2.9%+30¢ payment processing) — this is the real reason "$10K MRR solo" competes with a senior engineer salary.
- Emerging 2026 variant: **usage/referral-fee pricing** (TrustMRR takes 3% of MRR it refers) rather than flat subscription — worth watching as an alternative model.

## Ideas operator could adapt — bridge to spatial/AI stack

- **Operator's edge is web + AI + spatial**, which none of the exemplars above are doing — Photo AI, Plausible, ShipFast are all flat 2D web tools. A spatial-computing angle (WebXR/hand-tracking/gesture UI layered on a boring, unglamorous B2B pain point) is differentiated territory none of these five occupy — the SEO/content playbook (item 2 above) is the cold-start channel most compatible with no pre-existing Twitter audience.
- **"Boring problem" framing (35-app case) is directly portable**: pick a recurring, unglamorous operational pain point (compliance checklists, inspection logs, spatial-audit workflows) rather than a flashy AI demo — boring problems have steadier long-tail SEO volume and lower competition from hype-chasing builders.
- **Portfolio-of-small-bets (Marc Lou, 35-app case) fits a solo operator better than one big swing** — ship several narrow tools reusing the same auth/billing/hosting scaffolding, let SEO/content compound across all of them, and let the failures be cheap.
- **B2B $49-99/mo self-serve pricing** is the fastest realistic path to a $10K MRR floor with the fewest customers needed — worth defaulting to over consumer freemium unless there's already a distribution edge (there isn't yet).

## Chain row

```json
{"row_class":"research_receipt","agent":"sonnet-5_research_valkyrie","task":"microsaas_income_case_studies","clock_source":"host_read","date":"2026-08-01","claim_status":"proposed","verifier_result":"5 case studies + channel/pricing/timeline synthesis, all URL-sourced from WebSearch (self-reported founder figures, not independently audited)","remaining_risk":["all revenue figures are self-reported, no third-party audit found","survivorship bias: 5 exemplars vs 82-93% failure base rate not adjusted for","no direct interview/primary-source verification done, aggregator-of-aggregator risk for some URLs (e.g. buildmvpfast, indieai.directory)"],"next_safe_action":"if operator wants to act on this, next step is picking ONE boring-problem niche adjacent to spatial/AI stack and validating demand via community/SEO signal before building, per the playbook above","honest_flaw":"did not independently verify any founder's Stripe/bank dashboard; all numbers trace back to the founders' own public claims or third-party blog summaries of those claims; time-boxed to 30 min so depth-per-case is shallow"}
```
