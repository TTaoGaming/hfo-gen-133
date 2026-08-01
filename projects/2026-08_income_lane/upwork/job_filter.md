# UPWORK JOB FILTER — what to bid on, what to skip

```yaml
schema_id: hfo.gen133.income.upwork_job_filter_rationale.v0_1
valid_time_utc: 2026-07-31T00:00:00Z
author: sonnet-5 code lane, dispatched by SIGRUN_P4 gen-133
machine_readable_rules: job_filter.json (this file is the prose companion)
```

## Read this first: what is measured vs. guessed

Every numeric threshold in `job_filter.json` carries a `confidence` field:
`MEASURED` or `UNVERIFIED_HEURISTIC`. **Only two thresholds in this filter
are `MEASURED`** — both taken verbatim from the task brief, not derived:

- **Skip if `proposals_count >= 50`** — the brief's own disqualifying
  threshold.
- **Skip if `post_age_days > 7`** — matches `render_proposal.py`'s
  `--max-age-days` default, chosen so the filter and the render gate never
  silently disagree about what counts as stale.

Every other number (client spend floor, hire-rate floor, hourly-rate
floor, the "preferred" proposal-count band) is `UNVERIFIED_HEURISTIC` —
common Upwork-practitioner wisdom or an outright guess, not a number this
operator has measured. **Do not present any of them as a validated
threshold.** They exist so bidding has a starting rule instead of no rule;
the first 20 real proposals should correct them.

## Bid if all of

1. Title or description matches at least one keyword in the operator's
   actual niche language (agent reliability, agent eval, hallucination,
   guardrail, policy-as-code, audit trail, etc. — see `job_filter.json`
   for the full list). **Do not bid on generic "AI" or "machine learning"
   postings that don't touch reliability/verification** — that is a
   different, much more crowded market this operator does not have
   differentiated proof for yet.
2. Client payment method is verified.
3. Client total platform spend >= $1,000 (⚠️ UNVERIFIED_HEURISTIC).
4. Client hire rate >= 40% (⚠️ UNVERIFIED_HEURISTIC).

## Skip if any of

1. Title or description signals a full application/platform build, an
   MVP build, or "full stack developer" generalist scope — different
   skill and scope from a reliability audit or gate installation.
2. Unpaid trial, equity-only, or revenue-share-only compensation.
3. Stated hourly ceiling clearly below a sustainable floor (placeholder:
   under $35/hr — ⚠️ UNVERIFIED_HEURISTIC, should track 15-20% below the
   operator's real `[RATE]` in `PROFILE.md`, not be set independently of
   it).
4. **`proposals_count >= 50`** — MEASURED, from the task brief.
5. **`post_age_days > 7`** — MEASURED, matches the render gate's default.

## Preferred, not a hard filter

- `proposals_count <= 10` is where realistic odds of being read actually
  live, per general practitioner wisdom (⚠️ UNVERIFIED_HEURISTIC — this
  operator has no data of their own yet on this).
- Client geography in a payment-friction-free set (US/EU/CA/UK/AU) is a
  soft preference, not a disqualifier.

## What this filter does NOT do

- It does not score or rank jobs — it is bid/skip, not a ranked list.
- It does not read the live Upwork job feed. Someone (operator or a
  future scraper) has to produce the job data this filter is applied to;
  no scraping or API call is part of this build.
- It does not replace judgment on an edge case. A job that fails one soft
  `UNVERIFIED_HEURISTIC` rule but is otherwise an unusually strong fit is
  a human call, not an automatic skip.

## Review

Re-score every threshold in `job_filter.json` after the first 20
submitted proposals: if the `UNVERIFIED_HEURISTIC` rules are excluding
jobs that would have converted, loosen them; if bid-on jobs are
converting at 0%, tighten them. Until that first batch of real outcomes
exists, treat every `UNVERIFIED_HEURISTIC` number here as a placeholder,
not a validated filter.
