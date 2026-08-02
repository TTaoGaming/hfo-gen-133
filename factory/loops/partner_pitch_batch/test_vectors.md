# LOOP-E test vectors

## Vector 1 — gate missing

`state/experiments/approvals/latest.txt` has no `class:partner_pitch` line.

Expected: exit 2, chain row `gate_missing` claim_status=failed.

## Vector 2 — happy path (dry-run)

partners.csv:
```
name,first_name,company,blog_url,site_url,twitter_url,youtube_url,offer
Ada Lovelace,Ada,Analytical Engines,https://example.com/ada-blog,https://example.com/ada,,,25% revshare
```
template.md:
```
Hi {first_name},

Loved this from your writing: "{intro_reference}"

Quick pitch: {operator_intro}

Would {partner_company} want in on {our_offer}?

— {sender}
```

Wait — template contains `{sender}` which our loop does NOT provide.

Expected: chain row `rejected_missing_slots:ada-lovelace` failed with
`missing=["{sender}"]`.

Fix by removing `{sender}` from template and rerunning.

## Vector 3 — happy path corrected

Same as V2 but template without `{sender}`. Add
`class:partner_pitch:quota=5:seq_range=001-999:expires=2026-12-31T00:00:00Z`
to latest.txt.

Expected in dry-run:
- chain row `staged:ada-lovelace` wired_with_receipts
- File at `state/outreach/partner_pitches/ada-lovelace_YYYYMMDD.md`
  with frontmatter `awaiting_operator_sign: true` and body rendered
- Weekly index at `state/outreach/PARTNER_PITCH_INDEX_YYYY-Www.md`

## Vector 4 — partner with no scrape-able content

Partner CSV has all URL fields empty.

Expected: `unverified_skip:<slug>` failed with "content fetch returned empty".

## Vector 5 — LLM extracts nothing genuine (real fetch, thin content)

Partner site is a one-page landing with 20 words of boilerplate.

Expected: LLM returns "NONE" → chain row `rejected_generic:<slug>` failed.
Better than sending generic; operator can pick a different partner.
