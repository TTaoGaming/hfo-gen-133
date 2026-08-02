---
schema_id: hfo.gen133.distribution_readme.v0_1
doc_kind: DISTRIBUTION_INDEX
subject: distribution package — 3 units, launch-day assets
claim_status: STAGED_UNAPPROVED
created_utc: 2026-08-02T00:00:00Z
sealed: false
---

# Distribution package — first 3 ships

Everything staged for operator approval. **Nothing has been sent, posted, or
submitted.** All assets follow AppAlchemy pattern (pain → build → single
mention at end), keep-it-honest voice, and comply with each channel's rules.

## Contents

- `DIRECTORIES.md` — 20 launch directories with fields cheat-sheet + tiered
  submission playbook.
- `REDDIT_DRAFTS.md` — 3 posts (r/SideProject, r/AIAgents, r/mcp,
  r/LocalLLaMA), one per unit, ready to paste.
- `HN_SHOW_DRAFTS.md` — 3 Show HN submissions (title + URL + top-comment
  body), one per unit.
- `COLD_EMAIL_TEMPLATES.md` — 3 email + follow-up sequences with recipient
  personas and sourcing playbook.

## Launch-day sequencing (Tuesday 2026-08-04)

**T-24h (Monday evening):**
1. Operator swaps `STRIPE_LINK` (Payment Link URL) in each unit's
   `.placeholder-config.json`.
2. Operator swaps `CAL_LINK` in the same file.
3. Operator runs `node factory/scripts/deploy-unit.mjs <slug>` × 3.
4. Operator wires custom domains in Cloudflare Pages UI (≤ 5 min per unit).
5. Operator runs `node factory/scripts/verify-unit.mjs <slug>` × 3 — must
   see `VERIFIED` in the chain-row log.

**T-0 (Tuesday 8:00am PT):**
6. Submit to Tier 1 directories (numbers 1-13 in `DIRECTORIES.md`), 10 min each.
7. Submit to Tier 2 directories (14-20).
8. Post to Reddit (r/SideProject first — highest signal, lowest downside).
9. Submit Show HN (all 3 units, staggered 20 min apart to avoid single-user
   flag).
10. Start cold-email send (30 recipients per unit, personalized first line).

**T+4h:**
11. Reply to every HN comment. Reply to every Reddit comment. Do not argue.
12. Update `state/factory_ships/DIRECTORY_SUBMISSIONS.jsonl` with every
    listing URL you got back.

**T+24h (Wednesday morning):**
13. Consolidate first-day feedback into `state/factory_ships/LAUNCH_DAY_LEARNINGS.md`.
14. Decide which unit to invest deeper backend into based on signal.

## Explicit non-goals

- No Product Hunt this week. Save it for +7 days once directory signal has
  soaked in.
- No Twitter thread on launch day. Save for +2 days with actual metrics.
- No paid ads.
- No press outreach until we have ≥ 3 paying customers.

## What NOT to do

- Do NOT batch the same post across 5 subs at once. Reddit's spam filter
  is aggressive and cross-posting flags you fast.
- Do NOT send cold emails from ttaogaming@gmail.com — use a dedicated
  sending address (hi@agentreleasegate.com) with SPF/DKIM configured. If
  DNS isn't ready, delay cold-email to Wednesday.
- Do NOT use AI-generated first lines in cold email. The 15% reply-rate
  target assumes the personalization is real.
