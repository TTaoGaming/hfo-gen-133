# LOOP-E · PARTNER_PITCH_BATCH — SPEC

```yaml
AIH2O:
  version: gen-133
  loop: partner_pitch_batch
  role: executor
  actor: factory_loop
  verifier: receipt_verify.verify_before_send required_slots + gate_reader.gate_active('partner_pitch')
  clock_source: host_read
  chain: state/loop_receipts/partner_pitch_batch_<UTCDATE>.jsonl
  staged_out: state/outreach/partner_pitches/<partner_slug>_<UTCDATE>.md
  index: state/outreach/PARTNER_PITCH_INDEX_<isoweek>.md
```

## Inputs

- `--partners partners.csv` — one partner per row. Base list ships in
  `areas/quorum_research/PARTNERS_REVSHARE_AGENCY_INTEL_20260803.md §A`.
  Columns:
  ```
  name, first_name, company, blog_url, site_url, twitter_url, youtube_url, offer
  ```
  All URL columns optional — loop tries whichever are present.
- `--template template.md` — with placeholder tokens. Base templates ship
  in `§D` of the same file. Loop supports these placeholders:
  ```
  {first_name} {partner_name} {partner_company}
  {intro_reference} {operator_intro} {our_offer}
  ```
- `--intro intro.txt` — one paragraph the operator writes about themselves

## Class pre-authorization

REQUIRED unless `--skip-gate`. Add to `state/experiments/approvals/latest.txt`:

```
class:partner_pitch:quota=25:seq_range=001-1000:expires=<UTC>
```

Weekly rhythm targets ~25/wk × 12-16 weeks = 300-400 pitches. Per base
rate 0.3-0.8% → 1-3 deals. Quota is the cap per fire.

## Personalization discipline

For each partner:
1. Fetch first 4 available URLs (site/blog/twitter/youtube profile)
2. Extract raw text (HTML parsed, script/style stripped, first ~6KB)
3. LLM extracts ONE quotable sentence that could ONLY be about them
4. If LLM returns "NONE" or too-short output → REJECT (chain_row `rejected_generic`)
5. Render template with values dict
6. Re-verify no `{slot}` placeholder remains → else REJECT (`rejected_missing_slots`)
7. Write to `state/outreach/partner_pitches/<slug>_<UTCDATE>.md` with
   frontmatter `awaiting_operator_sign: true`

## Outputs

- `state/outreach/partner_pitches/<partner_slug>_<UTCDATE>.md` per partner
- `state/outreach/PARTNER_PITCH_INDEX_<isoweek>.md` — weekly index
- Chain rows in `state/loop_receipts/partner_pitch_batch_<UTCDATE>.jsonl`

## Kill conditions

- Gate missing → HALT (`gate_missing`, exit 2)
- Content fetch empty → `unverified_skip:<slug>` claim_status=failed
- LLM finds no genuine reference → `rejected_generic:<slug>` failed
- Rendered body still has `{slot}` → `rejected_missing_slots:<slug>` failed

## Cadence

Weekly Monday 09:00:

```powershell
schtasks /Create /TN "hfo-loop-E-partner-pitch" `
  /TR "python C:\Dev\hfo_gen_133_forge\factory\loops\partner_pitch_batch\run.py --partners C:\...\partners.csv --template C:\...\template.md --intro C:\...\intro.txt" `
  /SC WEEKLY /D MON /ST 09:00 /F
```

## Chain-row axes

| action | claim_status | notes |
|---|---|---|
| `gate_missing` | failed | halt |
| `unverified_skip:<slug>` | failed | no fetchable content |
| `rejected_generic:<slug>` | failed | LLM found no genuine hook |
| `rejected_missing_slots:<slug>` | failed | template bug or missing csv field |
| `staged:<slug>` | wired_with_receipts | file written, awaits operator sign |
| `finish_batch:<week>` | wired_with_receipts | weekly summary |
