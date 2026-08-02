# LOOP-C · DIRECTORY_SUBMISSION_BATCH — SPEC

```yaml
AIH2O:
  version: gen-133
  loop: directory_submission_batch
  role: executor
  actor: factory_loop
  verifier: gate_reader.gate_active('directory_submissions') + per-directory HEAD 200
  clock_source: host_read
  chain: state/loop_receipts/directory_submission_batch_<UTCDATE>.jsonl
  ship_log: state/outreach/directory_submissions.jsonl
  operator_queue: state/outreach/PENDING_DIRECTORY_APPROVALS.md
```

## Inputs

- `--unit-id` — slug of shipped unit (matches `state/factory_ships/MICROSAAS_SHIPS.jsonl:slug`)
- `--url` — deployed unit URL
- `--directories path/to/directory_list.csv`

CSV schema (headers required):

```csv
directory,url,submit_kind,notes,submit_url,category
Product Hunt,https://producthunt.com,web_form,ship Tuesday,https://www.producthunt.com/posts/new,productivity
BetaList,https://betalist.com,web_form,,https://betalist.com/submit,
AlternativeTo,https://alternativeto.net,api,requires 3 alternatives,,
SaaSHub,https://saashub.com,web_form,,https://www.saashub.com/submit,
```

`submit_kind ∈ {api, web_form, manual_only}` — api tries auto, web_form
stages a copy-paste package, manual_only always stages.

Base list ships in
`areas/quorum_research/DISTRIBUTION_CHANNELS_INTEL_20260803.md §2.13`.

## Class pre-authorization

**REQUIRED** unless `--skip-gate` is passed (single-shot only). Add to
`state/experiments/approvals/latest.txt`:

```
class:directory_submissions:quota=25:seq_range=001-999:expires=2026-08-16T19:00:00Z
```

Quota caps how many directories the loop touches per fire.

## Outputs

Per directory, one row in `state/outreach/directory_submissions.jsonl`:

```json
{
  "ts_utc": "2026-08-02T12:34:56Z",
  "unit_id": "promptbin",
  "directory": "Product Hunt",
  "url": "https://producthunt.com",
  "status": "staged_for_operator",
  "package_path": "factory/distribution/promptbin/directory_submissions/product_hunt.md"
}
```

Web-form directories also get a markdown package under
`factory/distribution/<unit_id>/directory_submissions/<slug>.md` with
copy-paste fields + a checkbox appended to
`state/outreach/PENDING_DIRECTORY_APPROVALS.md`.

## Kill conditions

- Gate line missing / expired → HALT (`gate_missing`)
- Directory URL HEAD not 200 → `skipped_site_down`, continue to next
- CAPTCHA required (implicit via web_form path) → `staged_for_operator`

## Cadence

Fire every 4h after each unit ships. Recurring task suggestion:

```powershell
schtasks /Create /TN "hfo-loop-C-directory-<unit>" `
  /TR "python C:\Dev\hfo_gen_133_forge\factory\loops\directory_submission_batch\run.py --unit-id <unit> --url https://<unit>.pages.dev --directories C:\...\directory_list.csv" `
  /SC HOURLY /MO 4 /F
```

## Chain-row axes

| action | claim_status | notes |
|---|---|---|
| `gate_missing` | failed | no live class line |
| `start_batch:<unit>` | proposed | shows quota |
| `stage_operator:<dir>` | proposed | staged, awaits human |
| `api_submit:<dir>` | wired_with_receipts | api integration succeeded |
| `skip_site_down:<dir>` | partial | HEAD failed |
| `finish_batch:<unit>` | wired_with_receipts | summary row |
