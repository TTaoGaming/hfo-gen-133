# LOOP-C test vectors

## Vector 1 — gate missing

Precondition: `state/experiments/approvals/latest.txt` has no
`class:directory_submissions:...` line.

Invocation:
```
python factory/loops/directory_submission_batch/run.py \
  --unit-id promptbin --url https://promptbin.pages.dev \
  --directories /tmp/dirs.csv
```

Expected: exit code 2, chain row `gate_missing` claim_status=failed, no
submissions written.

## Vector 2 — happy path, all web_form (dry-run)

Precondition: add
`class:directory_submissions:quota=5:seq_range=001-999:expires=2026-12-31T00:00:00Z`
to latest.txt.

CSV:
```
directory,url,submit_kind,notes
Product Hunt,https://producthunt.com,web_form,ship Tuesday
BetaList,https://betalist.com,web_form,
SaaSHub,https://saashub.com,web_form,
```

Invocation with `--dry-run`.

Expected:
- 3 chain rows `stage_operator:<dir>` proposed
- 3 rows in `state/outreach/directory_submissions.jsonl` status=staged_for_operator
- 3 files under `factory/distribution/promptbin/directory_submissions/`
- 3 checkbox lines appended to `PENDING_DIRECTORY_APPROVALS.md`
- summary row `finish_batch:promptbin` wired_with_receipts

## Vector 3 — CSV has 20 rows, quota=5

Same setup as V2 with 20 rows in CSV.

Expected: only 5 processed, remaining 15 left for next fire.

## Vector 4 — one directory site is down

CSV includes `Broken,https://this-domain-does-not-exist-12345.test,web_form,`.

Expected: `skip_site_down:Broken` chain row, other dirs processed normally.

## Vector 5 — api submitter fallback to web_form

CSV row `AlternativeTo,https://alternativeto.net,api,requires 3 alternatives`
with dry_run OFF and no API integration wired.

Expected: submit_api returns (False, "not yet implemented"), directory
falls through to web_form path, package staged with note appended.
