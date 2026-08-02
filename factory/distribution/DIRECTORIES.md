---
schema_id: hfo.gen133.distribution_directories.v0_1
doc_kind: SUBMISSION_LIST
subject: 20 launch directories for the first-3 units
claim_status: STAGED_UNAPPROVED
created_utc: 2026-08-02T00:00:00Z
sealed: false
---

# Launch directories — submission list

**Rule:** operator submits nothing until each unit's URL returns `HTTP 200` and
the pricing / FAQ / Cal.com link are all live. All 20 accept a bare public URL,
so submit in order of "lowest activation energy first."

Legend: `moderation` = manual review lag before listing goes live · `paid?` =
whether basic listing costs money · `fields` = what the form needs beyond the URL.

## Tier 1 — free, fast, high-signal (day of launch)

| # | Directory | URL | Moderation | Paid? | Fields required |
|---|---|---|---|---|---|
| 1 | **IndieHackers Products** | https://www.indiehackers.com/products | none | free | tagline (60 chars), description (300), pricing, screenshot |
| 2 | **BetaList** | https://betalist.com/submit | 2-14 days | free (skip-line $129) | tagline, description, founder story, launch date, screenshot |
| 3 | **SaaSHub** | https://www.saashub.com/submit-alternative | ~48h | free | name, tagline, categories (up to 5), description, pricing, competitors |
| 4 | **AlternativeTo** | https://alternativeto.net/software/new/ | 2-5 days | free | name, description, platforms, license, categories, alternatives-to |
| 5 | **StackShare** | https://stackshare.io/services/new | ~24h | free | name, description, category (tools/services), homepage, GitHub |
| 6 | **TinyLaunch** | https://tinylaunch.com/submit | ~24h | free | one-line pitch, category, launch date |
| 7 | **Uneed** | https://www.uneed.best/submit-a-tool | 1-3 days | free (featured €49) | name, tagline, description, category, screenshot, pricing |
| 8 | **Startupbase** | https://startupbase.io/submit | ~24h | free (badge $19) | name, tagline, description, launch date, categories |
| 9 | **ToolFinder** | https://toolfinder.co/submit | 1-5 days | free (featured $49) | name, tagline, description, category, pricing model |
| 10 | **Peerlist Launchpad** | https://peerlist.io/launchpad/submit | none (weekly cycle) | free | project card, description, tags, founder bio, launch week |
| 11 | **MicroLaunch** | https://microlaunch.net/submit | ~24h | free (featured $9) | name, tagline, categories, pricing |
| 12 | **LaunchPedia** | https://launchpedia.com/submit | 3-7 days | free (paid tier $29) | name, description, category, launch date, contact email |
| 13 | **Fazier** | https://fazier.com/submit | ~24h | free (upvote-boost $19) | name, tagline, description, launch date, categories |

## Tier 2 — AI-native / niche (day of launch to +2 days)

| # | Directory | URL | Notes |
|---|---|---|---|
| 14 | **There's An AI For That (TAAFT)** | https://theresanaiforthat.com/submit-ai/ | The 800-lb gorilla of AI directories. Review lag ~3-14 days. Free listing, paid featured. |
| 15 | **Futurepedia** | https://www.futurepedia.io/submit-tool | Ranks well on Google for AI-tool queries. Free, ~5-day review. |
| 16 | **AI Tool Report** | https://aitoolreport.com/submit | Free listing, newsletter-driven. |
| 17 | **Insidr AI** | https://www.insidr.ai/submit-tool/ | Curated. Slower review (~1 week) but higher trust. |
| 18 | **aitools.fyi** | https://aitools.fyi/submit | Community-driven. Fast approval. |
| 19 | **G2 (Sellers)** | https://sell.g2.com/#claim | Longest tail — takes weeks but SEO gold. Requires business email. |
| 20 | **Product Hunt Ships** | https://www.producthunt.com/ships | Waitlist / launch teaser page (not a launch itself — that's Tier 3). |

## Tier 3 — launch platforms (schedule for +1 week after directory soak)

Launch here **after** you have ≥ 5 pieces of validation from the directories
above (e.g. IH upvotes, a BetaList feature). Launching on PH cold is a coin
flip; launching with soaked-in signal is much better.

- **Product Hunt** — https://www.producthunt.com/posts/new (12:01 AM PT launch, hunter optional)
- **Hacker News "Show HN"** — https://news.ycombinator.com/submit (see `HN_SHOW_DRAFTS.md`)
- **Reddit** — see `REDDIT_DRAFTS.md`

## Submission field cheat sheet (copy-paste ready)

- **Tagline (60 chars):** see each unit's SEO_TITLE in `.placeholder-config.json`
- **Description (300 chars):** see SEO_DESCRIPTION
- **Categories:** `Developer Tools`, `AI`, `Productivity`, `SaaS`, `Open Source`
- **Pricing model:** `Freemium`
- **Launch date:** 2026-08-04
- **Founder:** Tao / TTaoGaming
- **Contact email:** ttaogaming@gmail.com

## Operator's submission-day playbook (≤ 3 hrs)

1. **Warm start.** Submit to Tiers 1 & 2 (numbered 1-19) in one sitting.
   Copy-paste from the fields cheat sheet.
2. **Peerlist Launchpad.** Post the project card the moment doors open for the
   week — the launchpad cycles Monday morning.
3. **HN Show + Reddit** go live at the same time as the directories.
4. **DO NOT do Product Hunt** until you have IH upvotes and at least one
   BetaList feature soaked in. PH from cold = wasted shot.
5. **Track:** paste every listing URL back into `state/factory_ships/DIRECTORY_SUBMISSIONS.jsonl`
   with `{ unit_slug, directory, url, status, submitted_at }`.
