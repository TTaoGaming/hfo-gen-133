# DocSend Lite

**One-liner:** Upload PDF → get a shareable link with password + expiry + view analytics. MIT license.

## Why this exists

DocSend is $15-45/mo. Papermark is the OSS answer but **AGPL** — forking it exposes your whole stack. Cloud drive links have no expiry, no password, no analytics. DocSend Lite is the MIT-licensed alternative you can fork into anything.

## Wedge

- **MIT license** — fork freely, self-host, use inside commercial products.
- **Simple gate:** password + expiry + view counter. Nothing more, nothing less.
- **Cloudflare-native:** one Pages project + one KV namespace + one Pages Function. Free tier hosts 100k views/mo at $0.
- **pdf.js in the browser** — no server-side PDF processing, no leaks.

## Pricing

- **Free** — 3 docs (localStorage), password gate, 7-day expiry, basic view counter (single-device).
- **Pro $19/mo** — unlimited docs, per-page analytics, custom expiry, email-capture gate, custom subdomain, team sharing.

## FOSS parent + license

**Rejected: Papermark (AGPL-3.0).** Fork would infect the whole stack. Written from scratch instead.

**Accepted at runtime: Mozilla pdf.js (Apache 2.0).** Loaded from jsDelivr at runtime — not bundled, not modified. Our code is MIT (see `LICENSE`).

## Architecture (v0 MVP)

**Free tier (this ship):**
1. User uploads a PDF locally OR pastes a public URL to a PDF.
2. Tool generates: `docId` (random), `passwordSalt` (random), `passwordDigest` (`SHA-256(salt + password)` if password set), `expiryTs`.
3. Metadata stored in `localStorage` (creator side) + share link contains `docId + src-url + expiry` (viewer side).
4. Viewer opens `/view.html?src=<url>&d=<digest>&s=<salt>&e=<expiry>`, enters password, gets pdf.js render.
5. Viewer beacons `/api/v1/view` with `{docId, page, elapsed_ms}` — currently a stub that returns 202.

**Pro tier (post-Tuesday operator wire-up):**
- Cloudflare R2 bucket for PDF hosting.
- Cloudflare KV for metadata + view rollup.
- `functions/api/view.js` writes to KV; `functions/api/analytics.js` reads.
- Custom subdomain per workspace.

Both tiers use the same viewer code — Pro just backs it with real storage.

## Deploy

```bash
node ../../scripts/deploy-unit.mjs docsend-lite
node ../../scripts/verify-unit.mjs docsend-lite
```

Operator Tuesday work: create KV namespace `DOCSEND_KV`, bind in `wrangler.toml`. See `functions/api/view.js` for env expectations.

## Distribution

See `state/factory_ships/UNIT_docsend-lite_20260803.md`. Targets: r/SaaS, r/startups, IndieHackers milestone, cold email to Y Combinator batch founders + Papermark users who need MIT.

## Truthful-red notes

- **Client-side password check** on Free tier — anyone who reads the URL params can extract the digest and attempt offline crack. This is a friction gate, not military-grade. FAQ discloses this.
- **No R2/KV wire yet.** Free tier is fully local; Pro tier requires operator to bind KV Tuesday.
- **`src=<url>` on Free tier assumes PDF is publicly reachable** (Google Drive share link, S3 signed URL, GitHub raw, etc.). Pro tier hosts on R2.
- **pdf.js is loaded from jsDelivr at runtime.** If the CDN is down, viewer breaks. Acceptable for MVP — subresource integrity + self-hosted fallback is a v0.2 chore.
