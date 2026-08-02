# Evolutionary Improvement of FOSS Exemplars: A 2026 Evidence Audit

## Executive judgment

The central thesis is viable, but the evidence supports a narrower version than the proposed framing.

The proven model is **not** “run MAP-Elites or NSGA-II over product ideas and expect market evolution.” The proven model is:

1. Start from a validated interaction pattern or workflow.
2. Add one immediately legible structural difference.
3. Build an automated evaluator for properties that can actually be measured.
4. Use AI-generated variants and optimization algorithms only inside that bounded evaluation loop.
5. Expose a small number of finalists to real users as early as possible.
6. Let distribution, retention, and willingness-to-pay—not synthetic LLM judgments—determine survival.

Across the requested algorithms, I found only one strong 2024–2026 production deployment with hard operational outcomes: **AlphaEvolve**. Google reports that evolved code recovered an average 0.7% of worldwide compute capacity, reduced Spanner write amplification by 20%, reduced software storage footprints by nearly 9%, and contributed to TPU circuit design. A 2026 external example from WPP reported a 5–10% improvement in prediction accuracy and recommendation scores. These are real deployments, but they are large-enterprise optimization cases, not solo-product or small-team go-to-market cases. citeturn15view0turn15view1

For MAP-Elites, Novelty Search, POET, NSGA-II/III, and CMA-ES, I found **no publicly verifiable 2024–2026 solo or small-team production product case** meeting all of the requested conditions: real customers or players, a deployed product, and a measurable external business outcome. Public examples remain concentrated in robotics, industrial simulation, engineering optimization, game-agent research, and benchmarks. That does not prove no private cases exist; it means there is no defensible public base rate on which to underwrite a solo-product strategy.

The product-assimilation evidence is much stronger. Balatro, Brotato, Halls of Torment, Slither.io, Quordle, AudioPen, Photo AI, Lancer, and SEObot all support the principle that a solo or small team can capture value by combining an already-legible base loop with a strong new mechanic, workflow, user segment, or packaging layer. The successful products were not mere reskins. They changed the decision structure, reduced workflow friction, served a newly reachable platform, or used a new model capability to productize work that previously required an operator.

For the immediate four-day decision, the highest-probability move is:

> **Publish the existing portfolio, but do not indiscriminately submit all twenty games to curated portals. Release the viable set on itch.io, then submit only the top three to five differentiated titles to CrazyGames and Kongregate. Do not spend this week making a Suika reskin for Poki.**

This has the highest probability of producing a genuine external product signal in seven days. It does not have the highest probability of producing $500 cash; warm-network contract work does. A new micro-SaaS built from zero in four days is less likely to produce either signal than shipping already-staged inventory.

## Formal evolutionary algorithms in production

### Evidence standard

A qualifying case required all of the following:

- Deployment during 2024–2026.
- Use outside a purely academic benchmark.
- A live product, operational system, or paying-user workflow.
- A measurable external or operational outcome.
- Enough public detail to connect the algorithm to the outcome.
- Preferably a solo or small-team operator.

Under that standard, most claimed examples do not qualify. A paper that optimizes robot gait, game-agent behavior, test generation, or a simulated industrial workstation is evidence that the algorithm works on its objective—not that it improves a software product in market.

### Production-evidence matrix

| Method | Best 2024–2026 public evidence found | Measured outcome | Does it satisfy the requested solo/small-team production standard? |
|---|---|---:|---|
| **MAP-Elites** | Parametric-Task MAP-Elites and related work includes industrial-workstation and robotics scenarios; the public examples are research or simulation deployments. citeturn15view7 | Better coverage or performance in task spaces; no public customer, revenue, retention, or shipping outcome. | **No qualifying case found.** |
| **Novelty Search / POET** | Public work remains centered on open-ended environment generation, agents, and research domains. Voyager shares the open-ended skill-growth idea but is a Minecraft research agent, not a product deployment. citeturn15view5 | Voyager obtained 3.3× more unique items and unlocked milestones up to 15.3× faster than research baselines. | **No. Academic environment outcome.** |
| **NSGA-II / NSGA-III** | Numerous engineering and scheduling applications exist, but no well-documented 2024–2026 solo-product case with revenue, retention, or external users was located. | Usually Pareto improvements on modeled objectives. | **No qualifying case found.** |
| **CMA-ES** | Continued use in engineering, medicine, robotics, and parameter optimization; publicly documented examples are generally institutional optimization or benchmarks rather than small-team software products. citeturn5search7 | Better objective values or fitted parameters. | **No qualifying case found.** |
| **AlphaEvolve** | Google production infrastructure, WPP marketing-model optimization, TPU and storage/compiler work. citeturn15view0turn15view1 | 0.7% average worldwide compute recovery; 20% lower Spanner write amplification; nearly 9% lower software storage; WPP reports 5–10% lifts. | **Yes for industrial production; no for solo/small-team product deployment.** |
| **OpenEvolve** | Community open-source implementation of the AlphaEvolve pattern, released in 2025. It includes function minimization, kernel and algorithm examples and a MAP-Elites archive. citeturn15view2 | Repository examples and benchmark improvements; no verified revenue or live-product outcome found. | **No. Framework is real; production case is absent.** |
| **DSPy optimization** | DSPy reports production use at Databricks, Shopify, and Dropbox. AWS demonstrates MIPROv2 optimization for Amazon Nova migration prompts. citeturn15view3turn15view4 | Improved task-quality metrics in documented optimization workflows; no public small-team revenue or customer-retention result attributable to DSPy. | **Partial production evidence, but not a qualifying small-team commercial case.** |
| **Voyager-style skill growth** | Voyager’s automatic curriculum and executable skill library compound agent capabilities in Minecraft. citeturn15view5 | Research-environment task and exploration gains. | **No production-product case found.** |

### What AlphaEvolve actually proves

AlphaEvolve proves that LLM-driven mutation can produce valuable code when four conditions hold:

- The mutable surface is bounded.
- The evaluator is deterministic or highly reliable.
- Candidate execution is sandboxed.
- Many cheap evaluations can be run without human review.

Google’s 2026 interface reflects exactly that architecture: the user provides a seed program and a client-side evaluator; AlphaEvolve generates candidate programs, while the client executes and scores them. citeturn15view0

It does **not** prove that an LLM can reliably evolve “a better game,” “a better SaaS,” or “a more marketable product” from abstract judgments. Compute utilization, write amplification, storage consumption, circuit correctness, and prediction accuracy are crisp objectives. Product desirability is sparse, delayed, contextual, and vulnerable to proxy gaming.

For a solo operator, the implication is that AlphaEvolve-style code evolution is appropriate for:

| Good target | Evaluator |
|---|---|
| Bundle-size reduction | Compressed bytes and cold-load time |
| Physics or pathfinding performance | Frame time, correctness suite, memory |
| Procedural-level generation | Solvability, completion distribution, novelty descriptors |
| Pricing-page copy | Real conversion experiment, not an LLM score |
| Agent prompt or tool policy | Held-out task completion, cost, latency, error rate |
| SQL/query optimization | Test equivalence and runtime |
| Ad-placement timing | Real retention and revenue experiments with guardrails |
| Difficulty tuning | Player deaths, completion, replay and session continuation |

It is inappropriate to ask an optimizer to maximize “fun,” “originality,” or “commercial potential” using only an LLM judge. Those scores can be used as cheap filters, but not as fitness ground truth.

### Where each algorithm fits a product pipeline

**MAP-Elites** is the best conceptual fit for maintaining a portfolio of differentiated variants. Rather than producing one “best” game, it can preserve elites across behavioral niches such as short versus long sessions, low versus high control complexity, relaxing versus high-pressure play, portrait versus landscape, and deterministic versus chaotic mechanics. Its value is diversity preservation, not market validation.

**NSGA-II or NSGA-III** is appropriate once objectives are measurable and in tension. A browser game might optimize session duration, load time, crash rate, replay probability, mobile usability, ad opportunities, and content-production cost. The failure mode is straightforward: optimizing synthetic metrics before meaningful traffic produces a beautifully organized Pareto frontier of guesses.

**CMA-ES** is the most immediately practical technique for continuous tuning: spawn rates, acceleration, cooldowns, enemy health curves, drop probabilities, animation timings, pricing thresholds, retrieval weights, or prompt-router thresholds. It is usually a better first optimizer than an LLM code mutator because its search surface is controlled and rollback is trivial.

**Novelty Search and POET** are more useful for generating tests and environments than for choosing products. A POET-like loop could generate increasingly difficult player profiles, browser constraints, agent tasks, or adversarial input sets. That may improve robustness, but no public evidence shows that it predicts commercial success.

**DSPy** is useful when a product already has a labeled development set and a task metric. AWS’s example uses user-supplied data, user-defined metrics, and MIPROv2’s Bayesian search to optimize prompts and examples. citeturn15view4 It is much less useful before the developer knows what correct output looks like.

**OpenEvolve** is usable now and is not a Google DeepMind release. It is a community implementation maintained by Asankhaya Sharma and the OpenEvolve community. The repository exposes MAP-Elites coverage, iteration costs, evaluators, containers, and provider-specific cost estimates. citeturn15view2 The repository is credible as software, but its public success stories do not yet establish a business outcome.

### The adversarial conclusion on formal evolution

The formal-EA portion of the strategy should be treated as an **engineering leverage layer**, not a business thesis.

A defensible sequence is:

> market exemplar → licensed implementation → explicit mutation surface → deterministic evaluator → candidate archive → human review → real-user test → retention or revenue decision.

The unsupported sequence is:

> FOSS repository → LLM mutations → synthetic “fun” score → assume product-market improvement.

No requested algorithm currently has a credible public base rate for repeatedly turning undifferentiated FOSS products into profitable solo products.

## Exemplar assimilation cases

### What successful assimilation actually looks like

The strongest cases assimilate at one of three levels:

**Interaction assimilation:** preserve a familiar core loop but add a new decision system. Balatro and survivors-likes fit here.

**Workflow assimilation:** reproduce a valuable professional workflow, then compress it into software. SEObot, Lancer, Adspirer, and transcription tools fit here.

**Infrastructure assimilation:** place open-model capability behind a simpler interface, personalization layer, or distribution channel. Photo AI and Whisper-derived tools fit here.

Conceptual assimilation is much more common than code forking. The commercial value usually lies in the new mechanic, distribution, UX, data, workflow integration, or audience—not in the inherited code.

### Games

| Product or family | Base exemplar | Added mechanic or differentiation | Publicly documented tools | Outcome | Time to first revenue |
|---|---|---|---|---:|---|
| **Balatro** | Poker-hand scoring combined with the roguelike deckbuilder pattern | Jokers, multiplicative scoring interactions, deck modification, blinds, run progression and highly combinatorial builds | Precise production toolchain was not established by the reviewed commercial sources | More than $1 million gross in eight hours; profitability reportedly within one hour; 250,000 copies in 72 hours, 500,000 in ten days, and one million in under a month. citeturn19view0turn19view1turn19view2 | **About one hour to profitability; revenue immediately at launch.** |
| **Brotato** | Vampire Survivors-style automatic combat and escalating waves | Six-weapon builds, short waves, a between-wave shop, distinct characters and stat-driven build construction | Godot is publicly associated with the title; exact production workflow is not fully documented in the reviewed sources. citeturn19view3 | Public reporting credits it with more than one million copies during its early-access period; later third-party estimates are substantially higher but should not be treated as audited revenue. | First-revenue timestamp not disclosed; monetization began with paid early access. |
| **Halls of Torment** | Vampire Survivors progression plus early Diablo aesthetics and itemization | ARPG-style equipment, quests, class progression, directional/manual attacks and persistent unlocks | Godot | One million Steam sales by October 2024. It was explicitly described as a Vampire Survivors–Diablo combination. citeturn19view4 | Exact first-sale timing not disclosed. |
| **Boneraiser Minions** | Survivors-like arena loop | Necromancy/minion composition, auto-battler decisions, relics and spells instead of direct weapon replication | GameMaker; developed and published by caiys/caiysware. citeturn19view5 | Third-party estimate of approximately 133,600 copies and $566,600 gross as of August 2026. This is **not evidence of $1 million-plus revenue**. citeturn19view6 | Not disclosed. |
| **Slither.io** | Classic Snake plus Agar.io’s shared multiplayer arena and mass accumulation | Body-collision combat, trapping, boost-for-mass tradeoff, persistent leaderboard and low-friction browser/mobile play | Browser networking and mobile clients; detailed stack not necessary to the commercial conclusion | The solo-created game reportedly exceeded $100,000 in daily revenue roughly three months after release. citeturn19view12 | Exact first-revenue day unavailable; ad monetization began near launch. |
| **Suika-family browser clones** | Physics dropping plus 2048-like merge progression | Themes, altered object ladders, multiplayer, power-ups or different physics | The moonfloof repository uses plain JavaScript and Matter.js; other clones use Phaser, TypeScript, Vite, Godot or Defold. citeturn14search1turn14search13turn14search25 | No defensible revenue outcome was found for the cited FOSS repositories. GitHub popularity is modest and is not a proxy for product revenue. | **Unverifiable.** |
| **Wordle variants** | Wordle’s daily shared-result word puzzle | Absurdle adversarially changes the answer space; Quordle applies each guess to four simultaneous boards; Octordle expands to eight | Primarily lightweight browser applications; exact stacks vary | Quordle was acquired by Merriam-Webster, but transaction terms were not disclosed. citeturn19view13turn14search0 | First-revenue timing and revenue are not public. |

Several requested premises require correction.

First, **“all Vampire Survivors clones made $1 million-plus” is unsupported**. Halls of Torment and Brotato clearly reached large unit volumes. Boneraiser Minions has strong user reviews, but the available 2026 estimate is closer to $567,000 gross than $1 million. citeturn19view6

Second, Balatro was not a fast AI-generated remix. It was a deeply integrated design in which the borrowed vocabulary—poker hands and roguelike deckbuilding—made the game immediately understandable, while the scoring combinatorics created a distinct system. Its launch outcome was extraordinarily fast, but the product-development process was not.

Third, Slither.io is a useful exemplar because its added mechanic was both simple to explain and strategically deep. “Agar.io plus Snake” describes the product, but body collision, coiling, boosting and death-to-resource conversion changed how players interacted. That is different from changing art and retaining the same decision graph. The game’s rapid viral distribution also depended on YouTube and social play, not merely portal acceptance. citeturn14search19turn19view12

Fourth, Wordle variants demonstrate that a single-dimensional mechanic change can be enough when the original loop already has cultural distribution. Quordle’s four-board change was legible in one sentence and led to an acquisition, but the undisclosed price means it cannot be used as a quantitative revenue case. citeturn19view13

### Micro-SaaS and AI products

| Product | Base workflow or model | Added product layer | Public tools | Outcome | Time to first revenue |
|---|---|---|---|---:|---|
| **Lancer** | Upwork agency prospecting, account management and proposal workflow | AI agent that operationalizes the founder’s prior agency process and helps scale Upwork activity | Detailed complete stack not disclosed in the reviewed case | $10,000 MRR within two months and approximately $20,000 MRR by the July 2026 interview. The founder also reported losing four months and thousands of dollars on an unsafe account-connection approach before rebuilding it. citeturn19view7 | Exact first customer not stated; $10,000 MRR by month two. |
| **SEObot** | SEO agency/content-operations workflow | Automated keyword research, content creation, optimization, internal linking and backlink work for busy founders | Stripe is identified by the revenue-profile source; fuller stack not reliably disclosed | TrustMRR listed roughly $47,300 over the prior 30 days and claims more than 200,000 articles, 1.2 billion impressions and 30 million clicks. These are platform/founder-supplied figures rather than audited financial statements. citeturn19view8 | Not publicly established. |
| **Adspirer** | Paid-media manager and advertising-operations workflow | Conversational AI connected to ad accounts, automated monitoring and campaign-management assistance | Next.js, Google Cloud, Stripe, Clerk, Datadog, Anthropic, Docker, FastAPI, GitHub Actions, GraphQL, OpenAI, Redis and Twilio are listed. citeturn19view9 | Revenue presentation is internally inconsistent and its Stripe key had expired by June 2026. Treat any exact MRR claim as **low confidence**. citeturn19view9 | Unverifiable. |
| **AudioPen** | Speech transcription followed by manual cleanup and organization | Converts unstructured spoken thoughts into concise, organized written notes | Public coverage identifies OpenAI APIs; strict dependence on Whisper is not conclusively documented in the sources reviewed. citeturn20search29 | Reported 100 paying customers in two days and roughly $12,000–$15,000 monthly revenue by 2024. The creator had an existing audience, which materially weakens its value as a cold-start base rate. citeturn20search25 | **Within two days.** |
| **MacWhisper and similar local transcription apps** | OpenAI Whisper speech recognition | Native Mac UX, local/private transcription, file management, export and model selection | Whisper plus native desktop packaging | Commercial products clearly exist, but no sufficiently reliable public revenue and first-revenue figures were located for MacWhisper. | **Unverifiable.** |
| **Photo AI** | Stable Diffusion 1.5 image generation and fine-tuning | Personalized photo models, browser onboarding, payment, preset scenarios and a nontechnical consumer workflow | Stable Diffusion 1.5, PHP, jQuery and SQLite are publicly reported. citeturn19view10 | Reportedly near profitable within days and at approximately $100,000 monthly revenue by September 2024, about 18 months after launch. Figures are based on founder interviews and industry reporting, not audited statements. citeturn19view10 | **Within days.** |

Lancer is the strongest 2026 micro-SaaS case in the requested set because it shows more than “wrap a model.” The founder had direct domain experience, validated the pain, inherited distribution and credibility from agency work, and automated a workflow with an existing willingness to pay. citeturn19view7

SEObot and Adspirer are better described as **workflow productizations** than remixes of one named software exemplar. They assimilate work historically performed by agencies or platform specialists. SEObot’s published numbers are significant, but they come through a revenue-transparency platform and product-supplied operational claims. Adspirer’s profile explicitly says its Stripe connection expired, and the displayed financial figures are not internally clean enough to use as a valuation-quality source. citeturn19view8turn19view9

Whisper-derived products prove that open model capability can support many products, but public attribution is messy. Some voice products use Whisper, some use OpenAI APIs without naming the underlying speech model, and some have migrated to proprietary or alternative transcription providers. AudioPen has a stronger commercial story than MacWhisper in the public record, but the source material does not establish that Whisper alone created the outcome.

Photo AI is the cleanest Stable Diffusion assimilation case. The model supplied commodity generation capability; the product supplied personalization, onboarding, scenario presets, payment, and an approachable interface. The founder reportedly retained Stable Diffusion 1.5 because it continued to work better for the specific product despite newer model releases. citeturn19view10

### The pattern that survives scrutiny

The successful cases generally include at least three of the following:

| Component | Why it matters |
|---|---|
| Familiar base loop or workflow | Reduces explanation and user-acquisition friction |
| One-sentence differentiation | Makes the product easy to position |
| Structural—not cosmetic—change | Creates different decisions or outcomes |
| Existing distribution | Publisher, audience, platform, community or professional network |
| Immediate first-use payoff | Users understand value before long onboarding |
| Persistent progression or saved work | Creates return behavior |
| User-specific data or personalization | Makes the wrapper harder to replace |
| Real-world workflow integration | Connects model output to an economically valuable action |
| Fast payment path | Converts demand before a large platform is built |

“Reskin and ship” appears in the visible surface of many markets, but it is not the robust success pattern. The defensible pattern is **recognizable core plus meaningful delta plus distribution**.

## Curated platforms and monetization

### Probability methodology

No major platform publishes a reliable acceptance rate or a probability that a newly accepted solo title earns $500. Any precise percentage claiming to be a platform statistic should be treated skeptically.

The ranges below are **analyst estimates**, not disclosed platform metrics. They are based on:

- Whether listing is automatic, manual or performance-gated.
- Whether accepted content receives real distribution.
- Whether monetization is available immediately.
- Whether the platform discloses a revenue formula.
- The amount of existing audience normally required.
- The strength of the platform’s current consumer distribution.
- Whether the developer has no prior track record.

For game portals, “accepted” means reaching a monetizable release, not merely passing an upload form. The probability of first $500 is conditional on acceptance and assumes up to six months unless otherwise noted.

### Game platforms

| Platform | Current gate and economics | Estimated acceptance for a cold solo submission | Estimated P(first $500 \| accepted) | Typical time |
|---|---|---:|---:|---|
| **Poki** | Multi-stage testing followed by final human review of test results, quality and uniqueness. Final review alone takes one to two weeks. citeturn17view0 | **5–15%** | **30–55%** | One to four months; longer if iteration is requested |
| **CrazyGames** | Manual QA, then a two-week Basic Launch to a limited audience; Basic Launch has no monetization. Full Launch depends on engagement metrics and requires SDK integration. citeturn17view2turn17view3 | **10–25% for Full Launch** | **25–50%** | One to four months |
| **Kongregate** | Reopened to new games in 2026. Approved eligible games are automatically enrolled in a temporary 70% of net-revenue program. citeturn17view5turn17view6 | **40–70%** | **5–20%** | Two to nine months |
| **Game Jolt** | Relatively open publishing and community discovery; monetization and visibility depend heavily on creator audience and community engagement | **85–98% for listing** | **2–8%** | Three to twelve months or never |
| **Miniclip** | No longer functions as an open general-purpose browser-game portal. Its public publishing proposition is a selective mobile-publishing relationship with user acquisition, cross-promotion and monetization support. citeturn16view10turn14search33 | **Below 1–5% for a cold publishing pitch** | Not meaningfully comparable; a signed publishing deal would already imply material investment | Three to twelve months |
| **itch.io** | Self-service listing with little curation; discovery is primarily developer-driven | **Approximately 100% if policy-compliant** | **1–5% without an audience** | Same-day listing; revenue may take weeks, years or never |

These ranges should not be interpreted as statistically observed frequencies. They are deliberately conservative decision ranges.

### Poki

Poki is not a place to send a four-day reskin and expect a quick feature. A game must pass testing stages before final review. At final review, Poki explicitly examines the game’s measured results, its adherence to quality guidelines and whether it is unique enough within its category. The final decision itself takes one to two weeks. citeturn17view0

Poki’s 2026 editor and operator priorities are consistent with fast browser comprehension: a rapid hook, clear player fit, quality, mobile/browser compatibility, uniqueness and evidence that users continue playing. Poki reports substantial scale—roughly 100 million monthly active users, more than 600 developer partners and about one billion monthly gameplays—but this makes the gate more valuable and therefore more selective, not less. citeturn2search16

No public source establishes an average time from cold submission to “first featured,” and the concept is not uniform: a launch placement, category exposure, homepage testing and sustained recommendation are different events. A cold developer should plan in months rather than days.

### CrazyGames

CrazyGames’ process is partly automated in instrumentation but **manually reviewed** at the submission and QA stage. Passing QA leads to a Basic Launch with real players. During Basic Launch, the SDK is optional and monetization is disabled. A Full Launch requires SDK integration and depends on metrics such as average playtime, retention, conversion, play count and player feedback. citeturn17view2turn17view3

The platform says new games can receive initial visibility, including a homepage new-games carousel, but continued distribution is performance-driven. It also requires monetizable games to be original and clearly distinguishable, use the CrazyGames SDK, exclude other portal branding and exclude external ads. citeturn17view3

The claimed fixed **60% ad revenue and 70% IAP formula is not supported by the current public developer terms**. The terms say compensation is calculated monthly using game popularity, advertising performance and advertiser interest. They do not disclose a universal fixed percentage. They do disclose a 50% compensation increase during an optional two-month period of browser exclusivity. citeturn18view0

Therefore, revenue at 100,000 plays cannot be calculated from public documents. A transparent working model is:

\[
\text{gross ad value}
=
100{,}000 \times
(0.8\text{–}2.0\ \text{impressions/play})
\times
(\$2\text{–}\$8\ \text{eCPM})/1000
\]

That produces approximately **$160–$1,600 of platform-side advertising value** before an undisclosed developer/platform allocation, invalid-traffic adjustments and geographic mix. A cautious developer-payout planning range is **roughly $100–$1,000 per 100,000 plays**, with $300–$600 a more useful central planning interval than the upper bound. This is a model, not a reported CrazyGames payout.

Payments are monthly after reaching a €100 threshold. citeturn17view3

### Kongregate, Game Jolt and Miniclip

Kongregate is more relevant in August 2026 than stale advice suggests. It reopened submissions and launched a temporary “Welcome Back” program paying approved games 70% of net revenue. Eligible revenue includes banner, interstitial and pre-roll advertising, plus virtual goods when the API is integrated. “Net” is after items such as ad-network shares, mediation fees, fraud adjustments and advertiser nonpayment. The program was explicitly described as temporary and targeted to end later in 2026. citeturn17view5turn17view6

The opportunity is therefore real but time-sensitive. Its weakness is distribution. Kongregate’s historical brand does not establish that a new 2026 upload will receive enough traffic to reach $500.

Game Jolt is useful for community presence, devlogs, feedback and direct supporter activity. Its low listing friction should not be confused with high commercial discovery. It is more likely to produce comments and relationships than significant passive browser-game ad revenue.

Miniclip should be removed from the open-browser-portal comparison. The company pivoted away from its large web portal in 2022 and now presents itself primarily as a selective mobile publisher offering user acquisition, cross-promotion, product expertise and monetization support across a large game network. citeturn16view10turn14search33 A cold HTML5 upload is not the relevant route.

### Non-game curated channels

| Platform | Current status | Estimated public-listing acceptance | Estimated P(first $500 \| listed) | Typical time |
|---|---|---:|---:|---|
| **Official MCP Registry** | Open, vendor-neutral catalog and API for public MCP servers; entries are self-reported and subject to community moderation. No native monetization. citeturn16view5turn16view6 | **70–95%** for valid, nonmalicious submissions | **0–5% from registry discovery alone** | One to six months if the server has its own billing and distribution |
| **OpenAI GPT Store** | Automated and human policy review. OpenAI announced an engagement-based US builder program in 2024, but I could not verify a broadly available, transparent 2026 payout formula from current official materials. citeturn16view7 | **60–90%** if compliant | **Unverifiable; model below 5%** | Indeterminate |
| **Poe** | Active creator monetization. Developers can set a per-message price and earn when users message their bots, subject to region and program terms. citeturn16view8 | **70–95%** | **5–20%** | One to six months |
| **Character.AI** | Large consumer bot platform, but no official broadly available creator-revenue program was located in this review | **80–98% for public characters** | **Approximately zero in direct platform payout absent a verified program** | Not applicable |
| **Product Hunt** | Open launch surface with competitive daily ranking; revenue depends primarily on product fit and the audience brought to the launch | **80–95% for listing; 3–10% for top-five placement** | **5–15% with no audience; 15–35% with a relevant existing audience** | Launch day through thirty days |

The official MCP Registry is not an Anthropic-owned app store in the ordinary sense. It launched as an open catalog, accepts maintainer-supplied information, uses community moderation and is intended as an upstream source for more opinionated subregistries. MCP was subsequently donated to Linux Foundation stewardship. Anthropic reported more than 75 connectors in Claude and 97 million monthly SDK downloads across Python and TypeScript, but that ecosystem scale does not imply server revenue. citeturn16view5turn16view6

The registry is therefore a distribution and credibility surface, not a business model. A paid MCP product still needs authentication, billing, quotas, support, a useful proprietary service, and external acquisition.

For the GPT Store, the 2024 official announcement said US builders would be paid based on engagement and promised more details. citeturn16view7 I found no official evidence sufficient to treat GPT Store payouts as a predictable 2026 solo-developer channel. The correct planning assumption is zero until the builder’s account is actually enrolled and displays binding payout terms.

Poe has a more concrete creator economy. Its June 2026 documentation says creators can set a price per message, earn that price on answered messages and participate from the United States and numerous other eligible regions. Poe also tells creators to bring their own marketing, which is an important acknowledgment that listing is not distribution. citeturn16view8

I could not verify a comparable broad Character.AI creator-payout system through an official current program page. That makes Character.AI a potential audience or experimentation channel, but not a dependable path to the first $500.

### Product Hunt in the post-hype market

Product Hunt remains useful as a coordinated launch event, credibility artifact and feedback mechanism. It should not be treated as an audience generator.

A small 2026 study of five founders found that four launches with complete data all ranked in the top six, yet seven-day signups ranged from 71 to about 450 and paid conversion ranged from zero to roughly 20%. Excluding a launch that combined Product Hunt and LinkedIn traffic, the others clustered between 71 and 150 signups. The highest-ranked launch had the lowest paid conversion. The study is tiny and self-reported, but its conclusion is consistent: Product Hunt amplified an existing audience more than it created one. citeturn16view9

For a solo founder without an audience, Product Hunt is still worth using after there is a clear paid proposition, good onboarding and an outreach list. It is not worth spending most of a four-day window manufacturing launch theater for an unvalidated product.

## Highest-probability move this week

### Decision matrix

The following are subjective Bayesian ranges informed by the platform mechanics above. They are not platform statistics.

“External signal” means at least one of:

- Fifty non-bot player sessions.
- Ten substantive pieces of user feedback.
- A portal advancing the title into testing or Basic Launch.
- A measurable repeat-play or return cohort.
- A paying customer or credible sales conversation.

| Move | P(genuine external signal in seven days) | P(first $500 within ninety days) | Main constraint | Judgment |
|---|---:|---:|---|---|
| **Publish the existing portfolio to itch.io and submit a curated subset to CrazyGames/Kongregate** | **65–85%** | **5–15%** | Portfolio quality and lack of owned distribution | **Best product-signal move** |
| **Fork one Suika FOSS exemplar, AI-reskin it and submit to Poki** | **10–25%** | **2–8%** | Poki testing timeline, uniqueness requirement and clone saturation | **Reject for this week** |
| **Build a new micro-SaaS from zero** | **20–40%** | **3–10%** | No validated pain, no distribution and four-day window | **Inferior to shipping staged inventory** |
| **Pursue contracts using warm relationships** | **40–70% for $500 if genuine warm leads exist** | **40–70%** | Existing trust and buyer access | **Best cash move, but not a product experiment** |
| **Cold-start contract outreach with no network** | **10–25%** | **10–25%** | Sales cycle and trust | Useful hedge, not a certain result |

The recommended action is therefore a barbell:

> **Spend roughly three and a half days shipping and instrumenting the best existing games, and the remaining half-day contacting warm contract leads.**

This preserves the product experiment while recognizing that contract work has a materially higher probability of generating $500 quickly when trust already exists.

### Why the Suika-to-Poki option loses

The moonfloof Suika repository is a legitimate lightweight starting point: it is a generic clone built with JavaScript and Matter.js. citeturn14search1 That makes it technically convenient, not commercially privileged.

A cosmetic reskin fails the most important platform test. Poki examines uniqueness after player testing, and CrazyGames requires monetized titles to be original and clearly distinguishable from existing games. citeturn17view0turn17view3 Even where a code license permits commercial reuse, the curation gate independently evaluates whether the product is differentiated.

Poki’s final review alone takes one to two weeks after preceding testing stages. citeturn17view0 A four-day sprint therefore cannot produce a meaningful Poki outcome this week unless a prior publisher relationship and testing process are already in place.

A Suika-derived game could still be viable if it adds a structural mechanic: adversarial drafting, multiplayer interference, persistent town-building, asynchronous challenges, deckbuilding, physics-based combat, controllable merge evolution, or a creator economy. A theme swap is insufficient.

### How to use the twenty staged games

Do not “auto-submit twenty” as though portal submissions were free lottery tickets. The likely outcome is diluted QA effort, weak thumbnails, repetitive mechanics and a developer profile associated with low differentiation.

Use a portfolio triage score:

\[
S =
0.25H +
0.20R +
0.15M +
0.15O +
0.10L +
0.10Q +
0.05C
\]

Where:

- \(H\): first-thirty-second hook.
- \(R\): replay or session-continuation potential.
- \(M\): mobile/browser usability.
- \(O\): visible originality.
- \(L\): load performance.
- \(Q\): technical quality and crash resistance.
- \(C\): content and update extensibility.

The weights are decision rules, not industry benchmarks. Score all twenty quickly, then choose the best three to five.

The first submission wave should contain distinct genres or interaction loops rather than five variants of the same template. This gives more information about player-market fit and reduces the risk that one weak underlying mechanic causes the entire batch to fail.

### Four-day execution plan

| Day | Work | Exit condition |
|---|---|---|
| **First day** | Run every title on desktop and mobile; measure cold load; record the first minute; score the portfolio; remove titles with fatal bugs, unclear instructions or obvious clone presentation | Three to five candidates selected |
| **Second day** | Fix onboarding, restart speed, controls, responsive layout, audio defaults, save state and fatal performance issues; instrument starts, core-loop entry, deaths, restarts and completed sessions | Each candidate survives at least twenty-five clean browser/device sessions |
| **Third day** | Produce differentiated thumbnails, short descriptions and gameplay clips; publish viable titles on itch.io as a coherent “lab” collection; submit the best three to CrazyGames | Public URLs and portal submissions live |
| **Fourth day** | Submit suitable titles to Kongregate while its 70%-net program is active; conduct direct outreach to browser-game communities and publishers; contact warm contract leads; log qualitative feedback | Real users or buyers contacted, not merely pages published |

CrazyGames’ Basic Launch takes approximately two weeks and has no monetization, so the seven-day objective should be submission progress, player data from self-publishing and qualitative feedback—not immediate portal revenue. citeturn17view2

### Budget allocation

A rational use of the $500 is:

| Use | Budget |
|---|---:|
| Ten to twenty independent playtest sessions, with screen recording and structured questions | $100–$175 |
| One or two strong thumbnails or key-art treatments for the leading candidates | $75–$150 |
| Cross-device/browser testing, hosting or minor asset replacement | $25–$75 |
| Reserve for fixes after portal or player feedback | $150–$250 |
| Paid traffic before retention evidence | **$0** |

Do not use the budget to buy generic traffic. Without a retention signal, paid acquisition mainly purchases a more expensive confirmation that the game does not retain.

### Precommitted survival criteria

Before launch, define what causes a game to survive, mutate or die. A reasonable first-pass internal gate is:

| Metric | Continue | Modify | Stop |
|---|---:|---:|---:|
| Reaches core loop within thirty seconds | ≥70% | 40–70% | <40% |
| Median active session | ≥4 minutes | 2–4 minutes | <2 minutes |
| Immediate replay or restart | ≥20% | 8–20% | <8% |
| Fatal errors in tested sessions | 0 | 1 | More than 1 |
| Unprompted “what is different?” comprehension | Most testers can state it | Mixed | Few can state it |
| Substantive positive comments per 50 players | ≥5 | 2–4 | 0–1 |

These are operating thresholds, not claimed portal averages. Their purpose is to prevent attachment to inventory.

## Implementation doctrine and risk controls

### Build an evolution system around telemetry, not taste

The proposed stack—Python, TypeScript, pyribs, pymoo, Claude and Aider—is sufficient. The missing component is not another optimizer. It is a trustworthy evaluation substrate.

A practical architecture is:

```text
licensed exemplar or internal seed
        ↓
provenance and dependency scan
        ↓
explicit mutable surfaces
        ↓
LLM proposes patch or parameter set
        ↓
sandboxed build and deterministic tests
        ↓
performance and behavior evaluation
        ↓
MAP-Elites archive / NSGA-II population
        ↓
human security, design and IP review
        ↓
small live-user allocation
        ↓
retention, conversion and revenue metrics
        ↓
archive update or retirement
```

The genotype should be deliberately narrow. Good mutable surfaces include configuration files, feature flags, level-generation rules, enemy compositions, item tables, prompt modules, UI copy variants and isolated algorithms. Letting an LLM freely rewrite the repository creates confounded experiments, review burden and security risk.

### Use MAP-Elites for a catalog, not one winner

For browser games, useful behavioral descriptors might be:

| Descriptor axis | Example cells |
|---|---|
| Session shape | 1–3 minutes, 3–8 minutes, 8–20 minutes |
| Control complexity | one-button, pointer-only, keyboard, mixed |
| Cognitive mode | reflex, planning, word, physics, idle |
| Failure pressure | relaxed, recoverable, punishing |
| Social structure | solo, leaderboard, asynchronous, live multiplayer |
| Progression | none, run-based, persistent unlocks, collection |
| Device fit | portrait mobile, landscape mobile, desktop-first |
| Content burden | systemic, authored-level, narrative, UGC |

The archive then answers “what are our best candidates in each niche?” rather than collapsing everything toward one synthetic score.

This is particularly valuable for a portal portfolio because portals have multiple audiences and recommendation niches. It is less useful if every candidate is another reskin of the same merge game.

### Use NSGA-II only after metrics stabilize

A reasonable multi-objective vector for games is:

\[
f(x) =
[
\text{retention},
\text{active session},
\text{replay rate},
-\text{load time},
-\text{crashes},
-\text{content cost},
\text{originality score}
]
\]

The originality score should include human review and similarity checks, not merely an LLM’s opinion.

For micro-SaaS or agent skills:

\[
f(x) =
[
\text{task success},
-\text{latency},
-\text{model cost},
-\text{human corrections},
\text{paid conversion},
\text{week-four retention}
]
\]

Until there are enough users, task success, latency and cost can be optimized offline. Conversion and retention cannot.

### Prefer cheaper search before elaborate evolution

With four days and $500, a full MAP-Elites or NSGA-II infrastructure is premature. The first selection problem is only twenty games. Human triage plus a small user test is cheaper and provides stronger information.

Formal evolution becomes justified when:

- A title already has meaningful traffic.
- Parameters or modules can be changed independently.
- Evaluation can run automatically.
- At least dozens or hundreds of candidate evaluations are affordable.
- There is evidence that local improvements affect real-user outcomes.
- The cost of maintaining diversity is lower than manually exploring it.

Before that point, successive halving is sufficient: test all twenty cheaply, retain five, test those more deeply, then invest in one or two.

### Maintain a provenance ledger

For every assimilated exemplar, store:

| Field | Required record |
|---|---|
| Repository and commit | Exact origin and revision |
| License | License text and obligations at acquisition time |
| Assets | Source and license of every image, sound, font and dataset |
| Modifications | Human-readable change log |
| Model inputs | Which files were supplied to each LLM |
| Model outputs | Patch, model and timestamp |
| Tests | Functional, security, similarity and license checks |
| Product delta | Written explanation of how the product differs |
| Platform rights | Distribution, exclusivity and monetization restrictions |

A permissive code license does not solve platform differentiation. Nor does it establish rights to unrelated artwork, names, music, datasets or trademarks that may appear in a repository. Treat code, assets and product identity as separate rights surfaces.

### Prevent optimizer-induced product decay

Evolutionary systems exploit evaluators. Expected failure modes include:

- Longer sessions created by slowing the game rather than increasing engagement.
- Higher ad opportunities created by fragmenting play.
- Higher completion generated by removing challenge.
- Better LLM-judge scores produced by verbose or fashionable wording.
- Lower support tickets achieved by hiding contact routes.
- Higher click-through generated by misleading thumbnails.
- Higher short-term conversion paired with refund and churn increases.
- “Originality” produced through random complexity rather than coherent design.

Every objective therefore needs a counter-metric. Session length should be paired with voluntary replay and feedback. Conversion should be paired with retention, refunds and complaints. Ad impressions should be paired with session continuation. Automation rate should be paired with correction rate and task success.

### Final strategic position

The opportunity is real, but the defensible advantage is unlikely to come from possessing MAP-Elites, NSGA-II or an AI swarm. Those are increasingly accessible.

The advantage can come from:

- Better exemplar selection.
- A cleaner licensing and provenance pipeline.
- Faster conversion of concepts into instrumented variants.
- Better evaluation data.
- A catalog of reusable mechanics and agent skills.
- Stronger distribution relationships.
- The discipline to kill weak variants.
- Proprietary behavioral data accumulated across launches.

The strongest near-term plan is therefore:

> **Ship the existing portfolio now, use real traffic to identify a surviving interaction loop, and apply formal evolution only to that loop’s measurable mechanics. Use contracts as a cash hedge. Do not bet the week on a FOSS reskin clearing a selective portal.**

AlphaEvolve demonstrates that evolutionary code generation can create substantial production value when the evaluator is exact. citeturn15view0turn15view1 The product cases demonstrate that familiar exemplars can become large businesses when the added mechanic or workflow is meaningful. The platform evidence demonstrates that curation increasingly rewards differentiation and measured engagement rather than mere technical completion. citeturn17view0turn17view3

What remains unproven is the combined claim that a solo AI swarm can repeatedly evolve FOSS exemplars into profitable products through formal evolutionary search. The rational next step is not to assume that claim. It is to create the smallest portfolio experiment capable of testing it.