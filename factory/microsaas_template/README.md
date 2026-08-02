---
schema_id: hfo.gen133.factory_template.v0_1
doc_kind: TEMPLATE_README
subject: HFO gen-133 micro-SaaS factory template
claim_status: SCAFFOLD_READY
created_utc: 2026-08-02T00:00:00Z
created_by: Executor (Cowork/Claude), gen-133
sealed: false
---

# HFO gen-133 micro-SaaS factory template

Static landing page + Cloudflare Pages one-command deploy + Stripe / Cal.com
placeholders. Built to let one operator ship a unit in ≤ 4 hours end-to-end.

## Ship in 3 commands

```bash
# 1. Copy the template into a new unit directory
cp -r factory/microsaas_template factory/units/my-tool
cd factory/units/my-tool

# 2. Edit .placeholder-config.json — every {{TOKEN}} in src/ + public/ is
#    replaced by the matching key. Missing keys make `pnpm run build` fail.
$EDITOR .placeholder-config.json

# 3. Deploy — creates a Cloudflare Pages project named after TOOL_SLUG and
#    publishes to https://<slug>.pages.dev/. Also chain-rows the ship.
pnpm install
pnpm run deploy my-tool my-tool
```

## Placeholder tokens

Every literal `{{TOKEN}}` in any `.html/.css/.js/.txt/.xml/.json/.md/.svg`
under `src/` or `public/` is substituted. If a token is missing at build time
the build **fails loud** — the site never ships with `[[MISSING:X]]` visible.

Core tokens: `TOOL_SLUG`, `SUBDOMAIN`, `ROOT_DOMAIN`, `TOOL_NAME`,
`SEO_TITLE`, `SEO_DESCRIPTION`, `SEO_KEYWORDS`,
`HERO_HEADLINE`, `HERO_SUBHEAD`, `HERO_CTA_PRIMARY`, `HERO_MICRO_PROOF`,
`PROBLEM_STATEMENT`, `DEMO_SLOT`,
`FEATURE_{1,2,3}_{TITLE,BODY}`,
`PRICING_FREE_BULLETS`, `PRICING_PRO_PRICE`, `PRICING_PRO_BULLETS`,
`FAQ_{1..4}_{Q,A}`,
`STRIPE_LINK`, `CAL_LINK`, `GITHUB_URL`.

`DEMO_SLOT` accepts raw HTML — units drop an `<iframe src="/app.html">` or
inline widget markup here.

## What ships

```
dist/
├── index.html          ← landing page (hero → pricing → faq → footer)
├── app.html            ← the actual tool (each unit provides its own)
├── privacy.html
├── terms.html
├── styles.css
├── app.js              ← waitlist stub + stripe-link guard
├── favicon.svg
├── _headers            ← CSP, cache, security headers
├── _redirects          ← short URLs, alias routes
├── robots.txt
└── sitemap.xml
```

## Cloudflare custom-domain wiring (operator, ≤ 5 min per unit)

1. Cloudflare dashboard → Pages → `<slug>` project → **Custom domains** → *Set up a custom domain* → enter `<slug>.agentreleasegate.com`.
2. Cloudflare auto-creates the CNAME if `agentreleasegate.com` is on the same account. If it's on a different registrar, add `<slug> CNAME <slug>.pages.dev` manually.
3. HTTPS provisions in ~60s.
4. Verify: `curl -I https://<slug>.agentreleasegate.com/` returns `HTTP/2 200`.

## Chain-row provenance

Every `pnpm run deploy` appends a JSONL row to
`state/factory_ships/MICROSAAS_SHIPS.jsonl`. The row starts as
`CLAIMED_UNVERIFIED` and is upgraded to `VERIFIED` via
`pnpm run log-ship <slug> VERIFIED "5/5 curl 200"` once the 5 canonical URLs
return 200 (`/`, `/app.html`, `/pricing`, `/privacy.html`, `/robots.txt`).

Truthful-red discipline: an unverified ship stays `CLAIMED_UNVERIFIED` — no
retro-active upgrade without a curl receipt.

## Stripe and Cal.com placeholders

- `STRIPE_LINK`: set to a Stripe Payment Link URL (or leave `#` — the client
  script hides the "buy now" fragment until it's set). Landing page falls back
  to a waitlist email capture in the interim.
- `CAL_LINK`: your Cal.com booking URL. Footer + `/book` redirect both use it.

Operator swaps both live Tuesday 2026-08-04 morning.
