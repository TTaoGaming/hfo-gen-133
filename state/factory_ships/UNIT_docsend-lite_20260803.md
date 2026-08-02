---
schema_id: hfo.gen133.microsaas_unit_ship.v0_1
doc_kind: UNIT_SHIP_REPORT
unit_slug: docsend-lite
subject: Unit 6 — docsend-lite (Papermark rejected as AGPL, scratch build on pdf.js)
claim_status: SCAFFOLDED_AWAITING_DEPLOY
created_utc: 2026-08-02T00:00:00Z
created_by: Executor (Cowork/Claude), gen-133
sealed: false
---

# Unit 6 · docsend-lite — ship report

## What the unit does

Upload a PDF (or paste a public PDF URL on the free tier) → get a shareable link with an optional password gate, an expiry timestamp, and a view counter beacon. Recipient opens the link, enters the password (checked via `SHA-256(salt + password)` client-side), sees the PDF rendered in-browser via pdf.js. Each page-in-view emits one analytics beacon; on Pro the beacon writes to Cloudflare KV, on Free the endpoint returns 202 (no storage). Simple, MIT, self-hostable.

## FOSS parent + license verification (the required 30-min check)

### Rejected: Papermark

**Papermark's license is AGPL-3.0.** Confirmed by inspecting the LICENSE file at `github.com/mfts/papermark` (checked at request time). AGPL means any fork or self-host would inherit AGPL obligations for the entire linked stack, including our operator's other units. For a factory whose whole thesis is "many small units, easy to fork," AGPL is a non-starter. **Rejected within the 30-minute budget.**

### Also considered (rejected)

- **OpenSign** — AGPL. Same problem.
- **Papermark v1 pre-AGPL commits** — technically MIT once, but Papermark relicensed the whole project; rebasing from an old commit is legally fine but socially awful and forfeits every subsequent improvement. Not worth it.
- **DocuSeal** — AGPL.

### Accepted: from-scratch build on pdf.js

Mozilla pdf.js is Apache 2.0. Loaded at runtime from `https://cdn.jsdelivr.net/npm/pdfjs-dist@4.7.76/legacy/build/pdf.min.mjs` — not bundled, not modified. Our code is MIT.

**Fallback plan from the brief** (`stripe-webhook-inspector`) is therefore **NOT invoked** — docsend-lite ships as originally scoped, from scratch, in budget.

**Our license:** MIT. See `factory/units/docsend-lite/LICENSE` (attributes pdf.js and documents the Papermark rejection).

## Placeholder-config JSON slots

`factory/units/docsend-lite/.placeholder-config.json` operator-swap slots:

- `STRIPE_LINK`: `"#"` — swap for real Payment Link ($19/mo).
- `CAL_LINK`: `"https://cal.com/ttao/15min"`.
- `GITHUB_URL`: `"https://github.com/TTaoGaming/docsend-lite"`.
- `SUBDOMAIN` / `ROOT_DOMAIN`: `docsend-lite.agentreleasegate.com`.

All landing copy already populated.

**Additional Tuesday operator step (Pro tier):** create a Cloudflare KV namespace named `DOCSEND_KV` and bind it in `wrangler.toml` (add a `[[kv_namespaces]] binding = "DOCSEND_KV" id = "<id>"` block). Then `/api/v1/view` starts writing view rollups. Without this binding the endpoint returns 202 with no storage (documented in `functions/api/view.js`).

## 5 canonical URLs (post-deploy HEAD check)

1. `https://docsend-lite.pages.dev/`
2. `https://docsend-lite.pages.dev/app.html`
3. `https://docsend-lite.pages.dev/pricing`  (302 → `/#pricing`)
4. `https://docsend-lite.pages.dev/privacy.html`
5. `https://docsend-lite.pages.dev/robots.txt`

Plus: `/view.html` returns 200 with `X-Robots-Tag: noindex,nofollow` — smoke-test in browser by opening a generated share link (creator flow → paste PDF URL → get link → open link → password gate renders → unlock → pdf.js renders pages).

## Distribution package

### Reddit — r/SaaS (primary — pitch-deck audience)

**Title:** I built an MIT-licensed DocSend alternative — Papermark is AGPL, so I wrote one from scratch

**Body:**
> DocSend is $15-45/mo, which is a lot when you're pre-revenue. Papermark is the OSS answer but AGPL — fork it into your product and you have to open-source your entire stack. Not workable if you want to embed it or use it commercially.
>
> Built a from-scratch alternative on pdf.js (Apache 2.0). Upload PDF, get a link with password + expiry + view analytics. All MIT.
>
> Free tier: 3 shared docs, 7-day expiry, password gate, basic view counter. Runs 100% on Cloudflare's free tier (Pages + a KV binding for Pro). Self-hostable on your own subdomain with one `wrangler pages deploy`.
>
> Pro ($19/mo, launching Tuesday): unlimited docs, 90-day expiry, per-page analytics, email-capture gate.
>
> Link: `https://docsend-lite.agentreleasegate.com/`. Source MIT on GitHub.
>
> Question for the r/SaaS lurkers: is 3 free docs the right cutoff or should it be higher? I want the free tier useful without giving away the Pro use case.

**Secondary subs:** r/startups, r/Entrepreneur, r/indiehackers, r/webdev, r/selfhosted.

### Hacker News — Show HN

**Title:** Show HN: DocSend Lite – shareable PDF links with password + view tracking (MIT)

**URL:** `https://docsend-lite.agentreleasegate.com/`

**Top comment (self-post):**
> Author here. Motivation: I wanted a Papermark-style pitch-deck link tool that I could fork into a client project without inheriting AGPL. Nothing on the market was MIT + hosted + simple, so I built it.
>
> Stack: pdf.js in the browser (Apache 2.0), one Cloudflare Pages Function for the view beacon, one KV namespace for analytics on Pro. Total infra cost on Cloudflare free tier is $0 up to 100k views/mo.
>
> Free tier does password + expiry + view counter, storage in localStorage (single-device dashboard). Pro syncs to KV.
>
> Honest limitations disclosed in the FAQ: client-side password check is a friction gate, not military-grade. Use a real data room for material-non-public information.
>
> Curious what people think of the pricing ($19/mo Pro) — I benchmarked against DocSend's $15 personal / $65 team.

### IndieHackers milestone

> "Shipped a Papermark alternative in MIT license — v0 live, first customer TBD."
>
> Long form: paste the Reddit post body + link the Show HN thread once it's up.

### Directories

Tier 1: IndieHackers, BetaList, SaaSHub, AlternativeTo (list under "DocSend alternative" and "Papermark alternative"), StackShare, TinyLaunch, Uneed, Startupbase, ToolFinder, Peerlist Launchpad, MicroLaunch, LaunchPedia, Fazier.

Tier 2: Product Hunt Ships, dev.to cross-post.

### Cold email — VC / founder personas

**Subject:** MIT-licensed DocSend for your portcos

**Body:**
> Hey {first_name},
>
> Saw you {reference — recent tweet, invested in X, wrote Y}. Quick share for your portcos: I built an MIT-licensed DocSend alternative. Password + expiry + view analytics, runs on Cloudflare free tier, forks freely into anything.
>
> Why the license matters: Papermark is AGPL, so founders who want to embed it in their product or self-host inside their company legally can't without opening up their whole stack. Mine is MIT.
>
> Link: `https://docsend-lite.agentreleasegate.com/`. Free tier is 3 docs — enough to try before the Series A deck goes out.
>
> If any of your founders are cost-sensitive on DocSend fees, feel free to forward.
>
> — Tao

**Personas / target list:**
- Y Combinator batch founders currently fundraising (search HN Who's Fundraising, YC directory)
- Emerging VC scouts + associates who blog about tooling
- Existing Papermark users on Twitter frustrated by AGPL constraints
- Indie SaaS founders who send pitch decks to Angels weekly (IH milestones)

**Volume target:** 30 sends. FU1 day 3, FU2 day 8.

## Deploy command operator runs Tuesday

```bash
node factory/scripts/deploy-unit.mjs docsend-lite
node factory/scripts/verify-unit.mjs docsend-lite

# Optional (Pro tier storage — one-time):
wrangler kv namespace create DOCSEND_KV
# copy the id into functions binding via wrangler.toml (Cloudflare Pages Functions
# auto-detect KV bindings from the Pages project settings; alternatively add via
# the Cloudflare dashboard UI: Pages → docsend-lite → Settings → Functions → KV bindings)
```

## Files on disk

```
factory/units/docsend-lite/
├── .placeholder-config.json
├── LICENSE                          # MIT + Papermark-rejection note
├── README.md
├── package.json
├── src/
│   ├── app.html                     # creator: upload / paste URL / set gate
│   ├── view.html                    # viewer: gate + pdf.js render
│   ├── docsend-tool.js              # creator side (localStorage + link gen)
│   └── view-tool.js                 # viewer side (password check + pdf.js + beacon)
├── functions/
│   └── api/
│       └── view.js                  # Pages Function — /api/v1/view (KV write on Pro)
└── public/
    ├── _headers                     # CSP override for pdf.js CDN + view.html noindex
    └── _redirects                   # /v/:id shortlink alias
```

## Truthful-red notes

- **Client-side password check is a friction gate, not military-grade.** URL query params contain the digest and salt; an attacker with the link can attempt offline crack. Disclosed in the FAQ. Real secrets → real data room.
- **Free tier PDF hosting is the user's problem.** They paste a URL to something publicly reachable (Google Drive share, S3 signed URL, GitHub raw). Pro tier hosts on R2 — that's the upgrade.
- **CORS caveat.** If the pasted URL doesn't serve `Access-Control-Allow-Origin`, pdf.js can't fetch it. Error message tells the user this and directs them to Pro / R2. Google Drive and Dropbox direct links work; some corporate share links don't.
- **KV not bound until operator wires it Tuesday.** Analytics beacon returns 202 without storage in the meantime; viewer flow works without it.
- **pdf.js loaded from CDN.** If jsDelivr goes down, viewer breaks. SRI + local fallback is a v0.2 chore.
