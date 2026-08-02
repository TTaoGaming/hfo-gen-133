# factory/loops — the 6 reusable Codex loop runners

Six self-contained loops the operator can fire from a normal PowerShell.
Each loop lives in its own folder with `run.py`, `SPEC.md`,
`test_vectors.md`, `README.md`. Shared primitives live in `lib/`.

## The 6 loops

| ID | Folder | Fires | Ships to |
|---|---|---|---|
| A | `microsaas_unit_ship/` | per unit spec OR daily 08:00 queue | `state/factory_ships/MICROSAAS_SHIPS.jsonl` |
| B | `foss_fork_variant/` | 3-5/day per operator-approved candidate | `state/factory_ships/FOSS_FORKS.jsonl` |
| C | `directory_submission_batch/` | every 4h after each ship | `state/outreach/directory_submissions.jsonl` |
| D | `demand_signal_mine/` | cron daily 06:00 UTC | `state/factory_targets/DEMAND_SIGNAL_LOG.jsonl` + daily digest |
| E | `partner_pitch_batch/` | weekly Monday 09:00 | `state/outreach/partner_pitches/*` + weekly index |
| F | `seo_content_draft/` | Mon/Wed/Fri 04:00 | `content/blog/<unit>/*.md` + `content/PUBLISH_QUEUE.md` |

Every loop:
- Reads config from files, not CLI (no secrets in shell history)
- Writes chain rows to `state/loop_receipts/<loop>_<UTCDATE>.jsonl` with AIH2O schema
- Halts on kill conditions and Slack-escalates when a halt is material
- Runs standalone under Python 3.11+; no sandbox VM required

## Shared library (`lib/`)

| Module | Purpose |
|---|---|
| `chain_row.py` | AIH2O chain-row append helper (JSONL, atomic write, `row_id` monotone) |
| `gate_reader.py` | Wraps `tools/olrun/approvals_parser.py` — reads class-preauth lines |
| `kill_gates.py` | Reusable halt-condition evaluator (bounce/spam/reply/error/license/build/URL) |
| `receipt_verify.py` | Pre-send verification (URL 200 check, required-slot check, suppression) |
| `slack_escalate.py` | Reads SLACK_WEBHOOK_URL from `.env`, posts hot-reply + halt pings |
| `litellm_client.py` | Thin LiteLLM proxy client — never direct-calls OpenAI/Anthropic keys |

## Operator invocation cheatsheet

### One-shot a single microSaaS unit

```powershell
python factory\loops\microsaas_unit_ship\run.py --spec factory\targets\pending\promptbin.json
```

### Fork a FOSS project

```powershell
python factory\loops\foss_fork_variant\run.py --config factory\targets\forks\hvac-jobsheets.json
```

### Submit a shipped unit to directories

```powershell
# 1. Add gate line ONCE:
echo "class:directory_submissions:quota=25:seq_range=001-999:expires=2026-08-16T19:00:00Z" `
  >> state\experiments\approvals\latest.txt

# 2. Fire:
python factory\loops\directory_submission_batch\run.py `
  --unit-id promptbin --url https://promptbin.pages.dev `
  --directories factory\distribution\promptbin\directory_list.csv
```

### Register recurring Windows scheduled tasks

```powershell
schtasks /Create /TN "hfo-loop-A-microsaas-daily" `
  /TR "python C:\Dev\hfo_gen_133_forge\factory\loops\microsaas_unit_ship\run.py --queue --max 3" `
  /SC DAILY /ST 08:00 /F

schtasks /Create /TN "hfo-loop-D-demand-mine" `
  /TR "python C:\Dev\hfo_gen_133_forge\factory\loops\demand_signal_mine\run.py --subreddits C:\...\subs.txt --patterns C:\...\patterns.json --cells C:\...\cells.json" `
  /SC DAILY /ST 06:00 /F

schtasks /Create /TN "hfo-loop-E-partner-monday" `
  /TR "python C:\Dev\hfo_gen_133_forge\factory\loops\partner_pitch_batch\run.py --partners C:\...\partners.csv --template C:\...\template.md --intro C:\...\intro.txt" `
  /SC WEEKLY /D MON /ST 09:00 /F

# LOOP-F fires Mon/Wed/Fri — three separate schtasks entries (see seo_content_draft/README.md)
```

### Class-preauth grammar

Copied verbatim from `tools/olrun/approvals_parser.py`:

```
class:<name>:quota=<N>:seq_range=<a-b>:expires=<UTC ISO-8601>
```

Instance override (skip a specific item inside a class):

```
!<market>:<seq>
```

Live class names this repo already supports:
`contracts_hn`, `contracts_github`, `employment_hn`, `grants_gov`,
`games_crazygames`, `games_kongregate`, `games_poki`, `cold_email_ai_rescue`,
plus loops-C and loops-E registered dynamically:
`directory_submissions`, `partner_pitch`.

### Common env vars

Read from `.env` at repo root (autoloaded by `lib/slack_escalate.py` and
`lib/litellm_client.py`):

```
SLACK_WEBHOOK_URL=https://hooks.slack.com/services/T.../B.../...   # optional
LITELLM_PROXY_URL=http://localhost:4000                             # optional
LITELLM_API_KEY=sk-...                                              # optional bearer for proxy
LITELLM_DEFAULT_MODEL=gpt-4o-mini                                   # optional fallback
```

Without any of these, loops still run and mark the LLM step as `dry_run`.

## Fitness check

- `python factory\loops\lib\chain_row.py --selftest` → writes 2 rows to a temp jsonl
- `python factory\loops\lib\kill_gates.py` → runs 3 asserts
- `python factory\loops\lib\receipt_verify.py` → runs 2 asserts
- `python factory\loops\lib\slack_escalate.py "test"` → prints `{"posted": false/true, ...}`
- Each `run.py --help` should show usage without crashing
