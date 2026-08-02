# Solo-Developer Revenue Playbooks for Mobile Apps and Indie Games, 2024–Q3 2026

## Executive verdict

**Mobile has not saturated past viability, but “publish an app and let the store find users” is no longer a rational solo-developer strategy.** The viable mobile businesses in 2026 generally bring one of four advantages before launch: an owned audience, a search-discoverable niche, a repeatable app-portfolio process, or unusually strong retention and monetization that can support paid acquisition. RevenueCat reports that almost 15,000 new subscription apps were launching each month by early 2026, up from about 2,000 per month three years earlier; meanwhile, apps launched before 2020 still produced more revenue per app than any newer cohort. citeturn19view7

For qualifying subscription apps in RevenueCat’s dataset, 17.3% reached $1,000 monthly recurring revenue and 4.6% reached $10,000 within two years. Those numbers are **not App Store submission base rates**: RevenueCat excludes apps without active subscription revenue or sufficient installs/revenue, making its sample materially healthier than the universe of submissions. Apple received 557,000 new App Store submissions in 2025 alone, 24% more than in 2024. citeturn19view9turn19view10

The practical conclusions are:

| Lane | Q3 2026 solo-dev attractiveness | Main reason |
|---|---:|---|
| iOS utility/subscription app | **Conditional yes** | Higher-value users and strong subscription infrastructure, but distribution is the bottleneck |
| Android utility/subscription app | **Useful as an extension, weak as a standalone first bet** | Broader reach, but public solo cases rarely disclose enough Android-specific revenue to justify Android-first development |
| Premium Steam indie game | **High upside, extremely low base rate** | Organic discovery can still create enormous outcomes, but the median release earns almost nothing |
| Mobile hyper-casual | **No for a new solo developer** | Paid-UA dependency, publisher gatekeeping, weak retention and a market-wide shift toward hybrid-casual |
| Curated web games | **Underexplored and strategically attractive** | Built-in distribution, zero install friction and lower or zero cash UA on platforms such as Poki and CrazyGames |

For a developer with web, AI and spatial-computing experience, the best risk-adjusted play is **web-first, cross-platform utility software with a mobile companion**, not a mobile-only app and not ad-funded hyper-casual. Mobile should be treated as a high-conversion endpoint for an audience acquired on the open web.

## Evidence quality and scope

The public evidence is uneven. Subscription-app benchmarks are relatively strong because RevenueCat analyzed more than 115,000 apps, $16 billion in revenue and more than one billion transactions. However, its methodology requires active subscription revenue and a minimum threshold of installs or revenue, so the dataset cannot directly answer “what percentage of every submitted app succeeds?” citeturn19view7

Named solo-founder case studies are self-reported and therefore subject to survivorship bias. Revenue is frequently reported as MRR, launch revenue or portfolio revenue rather than audited profit. App portfolios also rarely split revenue between iOS and Android. The tables below distinguish strict solo projects from solo-led microbusinesses and identify undisclosed stacks rather than guessing.

Steam sales figures are a mixture of publisher disclosures and third-party estimates. Unit-sales disclosures are generally more reliable than net-developer proceeds because discounts, regional pricing, refunds, taxes, Valve’s share, publisher recoupment and contractor costs are usually private.

The requested hyper-casual sample could not be honestly produced. I found **no set of five named, strictly solo hyper-casual games launched or financially disclosed during 2024–2026 with public revenue, stack, acquisition and developer proceeds**. Current publishers disclose aggregate downloads, chart positions, retention or ROAS, but not the solo developer’s take-home economics. Presenting older 2020–2022 Supersonic or Voodoo case studies as 2024–2026 outcomes would be misleading, so they are excluded from the core sample.

## Case-study matrix

**iOS-distributed solo and solo-led apps**

| Case | Solo status | Revenue disclosed in 2024–2026 | Stack | Monetization | Acquisition that drove the result |
|---|---|---:|---|---|---|
| **Brainrot — Yoni Smolyar** | Strict solo | **$26,000 in its first 30 days** | Swift; Cursor and Claude Code; Superwall and PostHog were also identified in the founder discussion | Subscription | A pre-existing social following was the largest channel. A Product Hunt editorial placement generated more than 10,000 downloads in one day; ongoing social, Instagram, X and Reddit supported the launch. citeturn20view0turn20view1turn20view2 |
| **HabitKit — Sebastian Röhl** | Strict solo | **$10,000 MRR in 2024**; later reporting described months above that level | Flutter, with native Swift/SwiftUI and Kotlin/Jetpack Compose work for platform-specific widgets | Freemium subscription | Organic App Store and Google Play ranking began producing meaningful revenue in 2023; an MKBHD/The Studio feature caused a major December 2024 download and revenue spike. A Times Square promotion produced little measurable revenue, illustrating that visibility without relevant intent does not necessarily convert. citeturn20view3turn20view4turn20view5 |
| **Habit Pixel — Hirvesh Munogee** | Strict solo | **$1,000 MRR after eight months**, launched May 2025 | Not publicly disclosed | Freemium; $1.99 monthly and $33.99 annual subscriptions at launch | Initial X and Reddit launch posts produced roughly 1,300 downloads by late May. Onboarding fixes and purchasing-power-parity pricing later improved international conversion. citeturn19view2turn20view8turn20view9 |
| **FitSaver — Chetan** | Strict solo | Approximately **$3,000 cumulative in four months**, with 88 active subscriptions | Not publicly disclosed | Subscription/freemium | Reddit and problem-first build-in-public posts were the principal channel. The founder reported that posts framed around the user problem worked better than explicit startup promotion. citeturn19view3turn20view12 |
| **Floga — Umberto Mezzadra** | Solo-led microbusiness, not strict one-person engineering | **$120,000 in 24 hours** from an initial lifetime offer; subsequently **$10,000 MRR** | Flutter, Firebase and RevenueCat; development assistance was hired | Lifetime preorder outside the stores, followed by subscription | The decisive asset was an existing audience built around the founder’s physical yoga/screen-time product. The launch sold to a warm customer list instead of relying on App Store discovery. citeturn19view4turn20view15turn20view16turn20view17 |

The common pattern is not “iOS users pay more.” It is **distribution attached to a clear intent**. Brainrot had an audience and editorial amplification; HabitKit combined store search with a creator feature; Habit Pixel and FitSaver found early users in problem-specific communities; Floga converted existing customer trust. None of these results came from merely submitting a build.

**Android-distributed solo and solo-led apps**

Android-specific revenue is almost never separated from iOS revenue in public founder reports. The cases below therefore demonstrate cross-platform businesses available on Android, not audited Android-only economics.

| Case | Revenue level | Stack | Monetization | Android-relevant acquisition playbook |
|---|---:|---|---|---|
| **ARTMVSTD — Max Artemov** | **$22,000 monthly** across more than 30 apps within roughly one year | Flutter; Artemov learned it specifically to expand to Android | Portfolio appears primarily subscription/freemium, although the precise mix was not disclosed per app | Keyword-first ASO: identify terms with useful popularity and manageable competition, build one focused feature, place the target keyword in metadata, then repeat. Artemov said ASO increased impressions, downloads and revenue by about 50%; paid ads and short-form video were used selectively after organic validation. citeturn19view5turn20view19 |
| **HabitKit** | **$10,000 MRR** in 2024 | Flutter plus native Kotlin/Jetpack Compose and Swift widget code | Subscription/freemium | Ranking in both Google Play and the App Store became the durable baseline; creator coverage delivered a discontinuous spike. citeturn20view3turn20view4turn20view5 |
| **Habit Pixel** | **$1,000 MRR in eight months** | Not disclosed | Freemium subscription | X and Reddit created the first cohort; localized purchasing-power-parity pricing opened purchases in Southeast Asia and Latin America. citeturn20view8turn20view9 |
| **FitSaver** | Approximately **$3,000 in four months** | Not disclosed | Subscription | Problem-focused Reddit posts and direct user feedback; the report also mentions Android subscription implementation issues, illustrating the additional billing and support surface of cross-platform distribution. citeturn19view3turn20view12turn20view13 |
| **Sarafan Mobile — Viktor Seraleev** | More than **$60,000 monthly** across a portfolio | Predominantly native Swift for video apps; experiments with Kotlin Multiplatform and React Native | Predominantly subscription portfolio | ASO, Google Ads, Apple Search Ads, Product Hunt and large-volume TikTok/Instagram publishing. Apple Search Ads became too expensive in the photo/video category; Google Ads was the paid channel that remained scalable. Short-form content worked but required six posts per day during one experiment. citeturn19view6turn20view20turn20view21turn20view22 |

The Android playbook that emerges is **cross-platform portfolio leverage**, not Android exclusivity. Flutter appears repeatedly because it reduces the cost of testing many narrow ideas. Native development remains rational where video rendering, widgets, background processing, spatial sensors or platform-specific performance are central to the product.

**Premium Steam indie games**

| Game | Solo status and stack | 2024–2026 financial outcome | Monetization | Acquisition path that mattered |
|---|---|---:|---|---|
| **Balatro — LocalThunk** | Solo-developed in Lua using the LÖVE framework; published by Playstack | More than **250,000 units in three days** and **one million units in under a month**. At its approximately $15 list price, the first million units represent roughly $15 million in list-price-equivalent gross sales before discounts, regional pricing, refunds and platform/publisher deductions. citeturn15search8turn15search31 | Premium paid game, later expanded across platforms | A playable demo enabled small creators to discover the game. Coverage snowballed from smaller streamers to larger creators; wishlists grew from 43 shortly after the Steam page appeared to 28,661 by July 2023 and more than 87,000 by November. Steam Next Fest, a streamer tournament and Playstack support converted that organic validation into a major launch. citeturn15search4turn15search24 |
| **Manor Lords — Greg Styczeń / Slavic Magic** | Solo-led development in Unreal Engine, later Unreal Engine 5; published by Hooded Horse | **One million units in roughly 24 hours** and **three million by February 2025**. At its roughly $40 launch price, three million units imply a list-price-equivalent ceiling near $120 million, substantially above realized net revenue. citeturn16search17turn16search15 | Premium Early Access | A Steam Next Fest demo created a large wishlist jump; the game launched with approximately 3.2 million wishlists. Patreon, an Epic MegaGrant, persistent organic wishlist growth and Hooded Horse’s publishing operation supported the long prelaunch runway. citeturn16search3turn16search6turn16search20 |
| **Buckshot Roulette — Mike Klubnika** | Strict solo original; Godot; Steam publishing by Critical Reflex | **One million Steam copies in roughly ten days** and **eight million PC copies by December 2025**. At a roughly $3 price, eight million units correspond to approximately $24 million in list-price-equivalent gross sales. citeturn15search3turn15search23turn15search27 | Low-price premium | The game first launched on itch.io, became highly visible on Twitch and TikTok, then spread to YouTube. Critical Reflex subsequently brought the already-viral game to Steam. citeturn15search3turn15search27 |
| **The Farmer Was Replaced — Timon Herzog** | Solo developer; engine not reliably disclosed in the reviewed sources; published by micro-publisher Metaroot | About **$4,000 in the first 30 days of Early Access**, versus approximately **$1.65 million in the first 30 days after the October 2025 full release**; more than 400,000 lifetime units were reported around release. citeturn15search1turn15search5turn15search13 | Premium paid game | Unexpected Early Access virality created the foundation. Before version 1.0, Metaroot rebuilt the Steam page, localized the game and marketing materials into 11 languages, and leaned into more than 6.6 million TikTok views. citeturn15search13turn15search25 |
| **Tangy TD — Cakez** | Strict solo; custom engine; development streamed publicly for four years | **$788,449 gross and $635,611 net in its first month**, after approximately $250,000 gross in the first week | Premium paid game | The founder livestreamed development and built a community over several years. The emotional launch-revenue reveal itself went viral and introduced the game to a larger audience, compounding the existing community launch. citeturn16news28turn16news29 |

The Steam winners are not “five ideas that happened to be good.” Every case had a distribution mechanism before or immediately after launch: playable demos and streamers, millions of wishlists, itch.io virality, TikTok localization, or a multi-year creator community. The game itself supplied a highly legible content hook that creators could show in seconds.

**Mobile hyper-casual**

A compliant five-case solo sample is unavailable. The absence of public evidence is itself commercially meaningful: the lane is controlled by publisher testing infrastructure, paid acquisition and confidential profit-sharing agreements rather than transparent storefront sales.

Voodoo stated in 2024 that Apple’s tracking changes raised acquisition costs and reduced ad-inventory value, squeezing the traditional ad-funded hyper-casual model. By 2023, hyper-casual represented only 25% of Voodoo’s revenue, leading the company to replace its large prototype network with a smaller group capable of building higher-retention hybrid-casual products. citeturn17search6

Current public publisher evidence is aggregate rather than developer-specific. Supersonic reported 6.2 billion cumulative downloads and approximately 190 million average monthly active users during January–October 2024, but did not disclose acceptance rates, development advances, recoupment waterfalls or solo-developer payouts. citeturn17search16 Voodoo’s Mob Control advertising case disclosed improvements of 12% in day-one ROAS, 10.5% in day-seven ROAS and 10% in day-30 ROAS, but again did not disclose the developer’s revenue or contract. citeturn17search18

**Research conclusion for this lane:** a solo developer cannot underwrite a hyper-casual project from available 2024–2026 public data. The publisher can see the relevant CPI, retention, ad-load, LTV and creative-testing distribution; the outside developer cannot. That information asymmetry is a reason to avoid the lane unless a publisher funds testing and provides transparent access to campaign and monetization data.

## Revenue distributions and realistic base rates

The case studies above are extreme upper-tail examples. The distribution data is much less attractive.

| Lane | Best available 2024–2026 distribution evidence | Realistic interpretation |
|---|---|---|
| Subscription apps, blended iOS/Android | At month 12, median monthly revenue was **under $50**. The 75th percentile was $223, the 90th percentile $971 and the 95th percentile $2,352. citeturn19view8 | A $1,000-monthly app is approximately a top-decile outcome among the measured launch cohort; a $10,000-monthly app is far deeper in the tail |
| Qualifying 2025 subscription apps | Within two years, **17.3% reached $1,000 MRR** and **4.6% reached $10,000 MRR**; gaming subscription apps recorded 20.0% and 8.9%, respectively. citeturn19view9 | Useful as a conditional benchmark after an app has enough activity to enter RevenueCat’s dataset, not as the probability facing a random submission |
| All App Store submissions | No public dataset connects all 557,000 2025 submissions to monthly revenue. RevenueCat explicitly excludes apps without active subscription revenue or minimum activity. citeturn19view7turn19view10 | Any precise “percentage of submissions” is modeled, not observed |
| Steam releases | A 2026 analysis of 2025 releases estimated median gross revenue near **$249**; roughly two-thirds earned under $1,000 and 90% under $50,000. A separate 2024 analysis estimated only 0.5% of indie releases exceeded $1 million and the top 8% captured 80% of the measured revenue. citeturn16search21turn16search4 | Steam remains highly Pareto-distributed: a viable upper tail coexists with a median below the submission fee plus minimal development labor |
| Hyper-casual | No public solo-developer median. Market evidence instead shows publisher consolidation and migration toward hybrid-casual. citeturn17search6turn17search16 | The observable success stories are selected after prototype and paid-UA testing; they do not reveal the denominator of failed prototypes |

### App Store submission base rates

A defensible answer requires separating **measured rates** from **planning rates**.

The measured conditional rate is:

\[
P(\$1K\ \mathrm{MRR}\mid\text{RevenueCat-qualified app})=17.3\%
\]

\[
P(\$10K\ \mathrm{MRR}\mid\text{RevenueCat-qualified app})=4.6\%
\]

The all-submission rate is:

\[
P(\text{qualified})\times P(\text{milestone}\mid\text{qualified})
\]

Because the first term is undisclosed, the true all-submission result cannot be calculated from public data. A sensitivity model illustrates the likely range:

| Assumed share of submissions that become “qualified active subscription apps” | Implied rate reaching $1K MRR | Implied rate reaching $10K MRR |
|---:|---:|---:|
| 10% | 1.7% | 0.46% |
| 25% | 4.3% | 1.15% |
| 50% | 8.7% | 2.30% |

Given the sub-$50 month-12 median and the filtering in RevenueCat’s methodology, an underwriting assumption of **roughly 2–5% of all consumer-app submissions reaching $1,000 MRR and about 0.5–1% reaching $10,000 MRR** is more realistic than applying 17.3% and 4.6% to every submission. This is a planning inference, not an observed App Store statistic. citeturn19view7turn19view8turn19view9

### Time to first $1,000

RevenueCat’s 2025 reporting placed the median time to $1,000 MRR at approximately **60 days among apps that eventually reached that milestone**. That is a winner-conditional metric, not the median for all launches. citeturn1search0

The unconditional median is effectively **“not reached within two years”**: when only 17.3% reach $1,000 MRR during that interval, more than half of the cohort has no milestone time to measure. citeturn19view9

The practical timelines visible in the named cases range from immediate for Brainrot and Floga, which launched into owned audiences, to eight months for Habit Pixel, roughly a year for Artemov’s portfolio strategy, and multiple years of development/community building for the premium Steam games. The 60-day figure should therefore be used as an early signal for a promising app, not as a forecast for a first-time solo developer.

## Acquisition economics and the paid-versus-organic decision

Global app user-acquisition spending reached an estimated **$78 billion in 2025**, up 13% year over year. iOS spending increased 35%, while Android was approximately flat; non-gaming apps accounted for $53 billion and gaming for $25 billion. This is the competitive auction a solo developer enters when buying installs. citeturn19view11

Actual CPI varies dramatically by category, country, targeting and ad creative. As one directional reference, Adjust reported a global e-commerce CPI of $0.99 in Q1 2025, but $2.70 in North America, $1.66 in Europe and $0.90 in APAC. Those are shopping-app figures, not a universal app CPI, but they demonstrate why “paid ads work” is not a meaningful statement without geography and LTV. citeturn19view12

The break-even rule is simple:

\[
\text{Paid-UA ROI}=\frac{\text{net lifetime value per install}}{\text{CPI}}-1
\]

Using the $2.70 North American CPI benchmark:

| Net LTV per acquired install | Modeled ROI at $2.70 CPI |
|---:|---:|
| $1.00 | –63% |
| $2.00 | –26% |
| $3.00 | +11% |
| $5.00 | +85% |

This table explains why subscription screenshots can be deceptive. A product with a $40 subscriber LTV can still lose money if only a small fraction of paid installs subscribe. The relevant number is **blended net LTV per install**, after non-payers, refunds, store fees, support, variable infrastructure and churn.

Retention magnifies the problem. Across app categories, Adjust’s broad benchmark falls from 26% retention on day one to 13% on day seven and 7% on day 30. Android was approximately 24% on day one and 6% on day 30, versus 27% and 8% on iOS. citeturn19view13

For a solo developer, the rational sequence is therefore:

1. Acquire the first meaningful cohort organically.
2. Verify onboarding, activation, payer conversion, retention and refund behavior.
3. Calculate net LTV by channel and country.
4. Buy traffic only where net LTV consistently exceeds CPI with a margin for measurement error.

The named app cases reinforce this sequence. Brainrot used an audience and Product Hunt; HabitKit used ASO and creator coverage; Artemov validates keywords before building; Habit Pixel and FitSaver used Reddit; Floga used an owned customer list. Viktor Seraleev used paid advertising successfully only after repeated testing and abandoned channels that were too expensive. citeturn20view1turn20view4turn20view19turn20view8turn20view12turn19view6

Organic acquisition has no media bill, but it is not free. It consumes founder time through content, community support, ASO, localization, partnerships or product-led sharing. Its main advantage is not nominally zero CAC; it is that organic users usually arrive with stronger intent and provide a safer cohort for validating retention before capital is exposed.

## Publisher deals and adjacent distribution platforms

Steam’s strongest solo outcomes show publishers working **after the product had observable demand signals**:

| Publisher relationship | Observable outcome | What the publisher appears to have added |
|---|---|---|
| **Playstack + Balatro** | One million units in under a month | Multi-platform execution, launch operations and scaling after a demo/streamer-driven wishlist breakout citeturn15search4turn15search8 |
| **Hooded Horse + Manor Lords** | One million units in about 24 hours; three million by February 2025 | Long prelaunch campaign, expectation management, platform coordination and conversion of 3.2 million wishlists citeturn16search3turn16search17turn16search15 |
| **Critical Reflex + Buckshot Roulette** | One million Steam units in roughly ten days; eight million PC units by December 2025 | Steam commercialization and continued support after itch.io/Twitch/TikTok virality had already validated demand citeturn15search23turn15search27 |
| **Metaroot + The Farmer Was Replaced** | Approximately $1.65 million in the first 30 days of version 1.0 | Steam-page repositioning, 11-language localization, creator/social amplification and launch execution citeturn15search13turn15search25 |
| **Voodoo/Supersonic mobile model** | Large publisher-level download and ROAS figures, but no 2024–2026 solo take-home disclosures | Marketability testing, ad creative, UA financing, mediation and monetization optimization; contract economics remain opaque citeturn17search6turn17search16turn17search18 |

The pattern is important: a publisher is more likely to multiply an existing signal than to manufacture demand for an undifferentiated product. For Steam, the signal may be wishlists, demo completion, streamer pickup or itch.io virality. For mobile, it is usually CPI, retention, session length, ad impressions per user and LTV.

There are no sufficiently documented 2024–2026 public outcomes showing what a strict solo developer actually retained after a Voodoo, Supersonic, Supercell-related or Playco deal. Publisher-level revenue, downloads or top-chart rankings cannot be converted into founder profit without the contract’s advance, recoupment, IP ownership, ad-spend allocation, revenue definition and termination rights.

The minimum contract diligence should cover ownership of the IP and store accounts; whether UA is recouped before the revenue split; whether “revenue” means gross receipts, platform proceeds or profit after publisher overhead; who controls ad accounts and analytics; approval rights for ad load and creatives; termination and reversion; payment audit rights; and whether the publisher can cross-promote or clone adjacent mechanics. A large gross-revenue headline is not useful if the developer receives a minority of residual profit after unrestricted recoupment.

### Poki, CrazyGames and itch.io as alternatives

Browser-game distribution deserves more attention than mobile hyper-casual for a web-capable solo developer. Poki states that active developers earned more than €100,000 on average in 2024, but this is a heavily selected metric covering accepted, active developers rather than submissions. citeturn18search0 Poki also reported that its top developer revenues had grown from approximately $50,000 to as much as $1 million annually over five years. citeturn18search12turn18search16

A useful individual example is Artem Lanin, who reported releasing five Poki games in 2025 and reaching 67 million total gameplays. His first title was modest, but using Poki playtests improved the next game, while a timely “brainrot” trend game reached one million plays in one day and approximately 17,000 concurrent users. He described Poki as becoming his primary occupation after more than 25 mobile submissions had failed to gain visibility. Revenue was not disclosed, so the case demonstrates distribution rather than an auditable earnings figure. citeturn18search2

CrazyGames reports more than 50 million monthly players and offers ad revenue sharing plus selected IAP through Xsolla. Its developer documentation explicitly positions platform traffic as zero-cash-UA distribution: accepted games can reach the existing audience without buying installs, with ranking driven by engagement, retention and session length. These are platform claims rather than independent performance audits, but the economic model is materially more solo-friendly than purchasing mobile installs before retention is proven. citeturn18search1turn18search9

itch.io remains valuable as a validation and virality surface rather than a dependable median-revenue channel. Buckshot Roulette is the clearest recent example: itch.io exposure and creator sharing demonstrated demand before the game moved to Steam with a publisher. citeturn15search3turn15search27 No robust 2024–2026 public dataset was found for median itch.io game revenue.

## Recommendation for a web, AI and spatial-computing solo developer

The recommended income lane is **a narrow AI utility with a web acquisition surface and a cross-platform mobile client**, built as a portfolio of controlled experiments rather than one large consumer bet.

A strong architecture would be:

| Layer | Recommended role |
|---|---|
| Web application | Primary onboarding, SEO, link sharing, demos, waitlist, content and possibly web checkout where permitted |
| iOS/Android application | Camera, spatial capture, notifications, offline workflows, sensors, widgets and high-retention repeated use |
| AI service | A workflow-specific transformation or decision, not a generic chatbot wrapper |
| Spatial capability | Differentiating feature for capture, visualization or measurement; not the sole addressable market |
| Monetization | Freemium with an annual subscription, team/pro tier or usage allowance; avoid ad-funded economics |
| Distribution | Search-intent content, programmatic examples/templates, relevant professional communities, integrations and shareable outputs |
| Stack | Flutter when custom cross-platform UI and rapid portfolio reuse dominate; React Native when web/TypeScript code and hiring ecosystem matter more; Swift/Kotlin only for performance-critical spatial or media components |

The first product should be small enough to ship in four to eight weeks and should target a query or workflow where the user already spends money or labor. Examples of the shape—not specific validated opportunities—include spatial site documentation, AI-assisted room or asset inventories, visual field reports, location-aware training, property inspection, event/exhibit authoring, or camera-based professional measurement. The mobile feature should make the workflow materially better, while the web surface supplies discoverability and shareability.

The operating plan should use explicit gates:

| Gate | Continue when | Stop or reposition when |
|---|---|---|
| Problem validation | Users already perform the task repeatedly and can name its cost | Interest is aspirational, infrequent or entertainment-only |
| Organic acquisition | Search/community traffic produces activated users without paid installs | Every user requires direct founder outreach indefinitely |
| Activation | A new user reaches the core outcome in one session | Users require extensive explanation before seeing value |
| Retention | A meaningful cohort returns because the workflow recurs | Retention depends primarily on reminders or novelty |
| Monetization | Conversion and net LTV support the expected support/AI costs | Revenue is consumed by inference, storage, refunds or support |
| Paid acquisition | Net LTV exceeds CPI by a substantial safety margin | Campaign profitability depends on optimistic future renewals |

**Final verdict:** mobile is still Pareto-positive for a solo developer in Q3 2026 **only as part of a differentiated distribution system**. The stores are saturated past viability for undifferentiated, store-discovery-dependent apps. They are not saturated past viability for products that arrive with owned demand, search intent, a creator/community loop, a portfolio-ASO engine or high-value workflow economics.

For this developer profile, the ranking is:

**web-first AI utility with mobile companion > native iOS niche utility > cross-platform app portfolio > premium web/Steam game experiment > Android-only utility > mobile hyper-casual.**

The central bet should not be “mobile.” It should be **an owned acquisition channel plus a recurring problem**, with mobile used where hardware access, immediacy and retention improve the product. The evidence from 2024–2026 consistently shows that distribution—not framework choice—is the scarce asset.