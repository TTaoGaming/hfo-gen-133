# directory_submission_batch

Post a shipped unit to a batch of directories. Auto-submit where an API
exists; stage a copy-paste package for the operator where the directory
requires a web form.

## Pre-flight — the gate

Add a class line to `state/experiments/approvals/latest.txt`:

```
class:directory_submissions:quota=25:seq_range=001-999:expires=2026-08-16T19:00:00Z
```

Quota caps directories/fire. Without a live line, the loop halts.

## Invocation

```powershell
python factory\loops\directory_submission_batch\run.py `
  --unit-id promptbin `
  --url https://promptbin.pages.dev `
  --directories areas\quorum_research\directory_list.csv
```

## Recurring — every 4h after a ship

```powershell
schtasks /Create /TN "hfo-loop-C-promptbin" `
  /TR "python C:\Dev\hfo_gen_133_forge\factory\loops\directory_submission_batch\run.py --unit-id promptbin --url https://promptbin.pages.dev --directories C:\Dev\hfo_gen_133_forge\factory\distribution\promptbin\directory_list.csv" `
  /SC HOURLY /MO 4 /F
```

## Dry-run

```powershell
python factory\loops\directory_submission_batch\run.py `
  --unit-id promptbin --url https://promptbin.pages.dev `
  --directories .\dirs.csv --dry-run
```

## Prereqs

- Python 3.11+
- CSV file with columns `directory,url,submit_kind,notes` (submit_url and
  category optional)
- Live class line in `state/experiments/approvals/latest.txt`
- Optional: SLACK_WEBHOOK_URL for pending-approval pings when >5 stage

## Where things land

- Per-directory package: `factory/distribution/<unit>/directory_submissions/<slug>.md`
- Operator queue: `state/outreach/PENDING_DIRECTORY_APPROVALS.md`
- Submissions log: `state/outreach/directory_submissions.jsonl`
- Receipts: `state/loop_receipts/directory_submission_batch_<YYYYMMDD>.jsonl`
