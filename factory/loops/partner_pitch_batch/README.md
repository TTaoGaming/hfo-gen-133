# partner_pitch_batch

Fetch each partner's public content, extract ONE genuine reference, render
a personalized template, stage for operator sign. Never sends.

## Pre-flight — the gate

```
class:partner_pitch:quota=25:seq_range=001-1000:expires=<UTC>
```

Add to `state/experiments/approvals/latest.txt`.

## Invocation

```powershell
python factory\loops\partner_pitch_batch\run.py `
  --partners C:\...\partners.csv `
  --template C:\...\template.md `
  --intro C:\...\intro.txt
```

## Weekly Monday 09:00

```powershell
schtasks /Create /TN "hfo-loop-E-partner-pitch" `
  /TR "python C:\Dev\hfo_gen_133_forge\factory\loops\partner_pitch_batch\run.py --partners C:\...\partners.csv --template C:\...\template.md --intro C:\...\intro.txt" `
  /SC WEEKLY /D MON /ST 09:00 /F
```

## Dry-run

```powershell
python factory\loops\partner_pitch_batch\run.py `
  --partners .\partners.csv --template .\template.md --intro .\intro.txt `
  --dry-run --skip-gate
```

Skips the LLM (uses `[DRY_RUN reference]`) and gate check. Useful for
smoking out template placeholder bugs.

## Template placeholders

Only these six are auto-filled:

- `{first_name}`
- `{partner_name}`
- `{partner_company}`
- `{intro_reference}`  ← the genuine one-liner
- `{operator_intro}`   ← your `--intro` file
- `{our_offer}`        ← from partner CSV, falls back to "revshare on any unit we co-launch"

Any other `{...}` placeholder → REJECT with `rejected_missing_slots`.

## Where things land

- Staged pitch: `state/outreach/partner_pitches/<slug>_<YYYYMMDD>.md`
- Weekly index: `state/outreach/PARTNER_PITCH_INDEX_<YYYY-Www>.md`
- Receipts: `state/loop_receipts/partner_pitch_batch_<YYYYMMDD>.jsonl`
