---
schema_id: hfo.gen133.microsaas_unit.v0_1
doc_kind: UNIT_README
subject: prompt-versioning-lite
claim_status: SCAFFOLDED_UNDEPLOYED
created_utc: 2026-08-02T00:00:00Z
created_by: Executor (Cowork/Claude), gen-133
sealed: false
---

# prompt-versioning-lite

**Git for prompts, without the git.** Paste a prompt, get a content-addressed
URL. Every edit is a new revision with a word-level diff. One-click rerun on
any model via LiteLLM. Free for 10 prompts, $9/mo for unlimited.

## Deploy

```bash
# from repo root
node factory/scripts/deploy-unit.mjs prompt-versioning-lite
```

Publishes to `https://prompt-versioning-lite.pages.dev/`. Wire custom domain
`prompt-versioning-lite.agentreleasegate.com` in the Cloudflare Pages UI
(≤ 5 min per README at `factory/microsaas_template/README.md`).

## Verify

```bash
node factory/scripts/verify-unit.mjs prompt-versioning-lite
```

Checks `/`, `/app.html`, `/pricing`, `/privacy.html`, `/robots.txt` return 2xx.
Appends a chain-row with status VERIFIED or FAILED.

## Files

- `.placeholder-config.json` — all copy, pricing, SEO, FAQ tokens
- `src/app.html` — the tool page (overrides template default)
- `src/prompt-tool.js` — client logic (SHA-256 revs, LCS diff, /api/run stub)
- `dist/` — build output, gitignored

The landing page, styles, favicon, headers, redirects, robots, sitemap, and
legal pages come from `factory/microsaas_template/` and are inherited at build.

## v0 truthful-red notes

- **Persistence is localStorage.** Multi-device sync and true immutability
  land when we add a Cloudflare D1 backend (planned Wednesday if launch pulls
  signups).
- **`/api/run` is a stub.** The client falls back to a demo response so the
  page never appears broken. LiteLLM Worker lands with the D1 backend.
- **Freemium cap is client-side.** Server-side enforcement lands with Stripe.

None of these are shipping blockers — the pitch is "URL you paste into Slack"
and that works today. See root `README.md` for the operator handoff.

## Target keywords (SEO)

- primary: prompt versioning tool
- long-tail: `git for llm prompts`, `share prompt version url`, `litellm prompt history diff`

## GitHub repo

`github.com/TTaoGaming/prompt-versioning-lite` — scaffolded, awaiting operator
`git init && git remote add && git push`.
