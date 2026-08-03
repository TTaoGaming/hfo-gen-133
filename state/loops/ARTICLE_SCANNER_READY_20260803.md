# ARTICLE_SCANNER — READY handoff · 2026-08-03 (Tuesday)

Loop is coded, seeded, and tested locally. This file is the operator's
Tuesday-morning enable checklist. Nothing external has been triggered
yet — Windows Task Scheduler is not installed, GitHub Actions workflow
is committed but has not run.

```yaml
AIH2O:
  version: gen-133
  loop: article_scanner
  role: handoff
  actor: automation_executor
  verifier: operator ran install_windows_task.ps1 OR merged workflow to main
  clock_source: host_read
  chain: state/loop_receipts/article_scanner_<UTCDATE>.jsonl
  deliverables:
    - factory/loops/article_scanner/SPEC.md
    - factory/loops/article_scanner/README.md
    - factory/loops/article_scanner/sources.yaml
    - factory/loops/article_scanner/seed_urls.json
    - factory/loops/article_scanner/run.py
    - factory/loops/article_scanner/weekly_review.py
    - factory/loops/article_scanner/install_windows_task.ps1
    - .github/workflows/article-scanner.yml
```

## What operator does Tuesday

### 1. Smoke-test locally (2 min)

```powershell
cd C:\Dev\hfo_gen_133_forge
python factory\loops\article_scanner\run.py --dry-run --no-slack
```

Expected: exits 0, prints JSON with `n_signals >= 11` (the 11 seed URLs
are guaranteed to land in the very first run), writes:

- `state\factory_targets\article_signals.jsonl` (11+ rows)
- `state\factory_targets\ARTICLE_DIGEST_YYYYMMDD.md`
- `state\loop_receipts\article_scanner_YYYYMMDD.jsonl`

### 2. Install Windows scheduled tasks (30 s)

```powershell
cd C:\Dev\hfo_gen_133_forge\factory\loops\article_scanner
.\install_windows_task.ps1
```

Installs:

- `hfo-article-scanner-daily`  — daily 06:00 local, runs `run.py`
- `hfo-article-scanner-weekly` — Sunday 06:15 local, runs `weekly_review.py`

Verify:

```powershell
schtasks /Query /TN hfo-article-scanner-daily /V /FO LIST
schtasks /Run /TN hfo-article-scanner-daily
```

Uninstall path:

```powershell
.\install_windows_task.ps1 -Uninstall
```

### 3. Enable GitHub Actions fallback (1 min)

The workflow file is already at `.github/workflows/article-scanner.yml`.
It runs on `main` once merged. Merge or push, then:

```bash
gh workflow list
gh workflow run article-scanner
gh run watch
```

Add repo secrets (optional but recommended):

- `LITELLM_PROXY_URL` — else CI runs in --dry-run (regex-only scoring)
- `LITELLM_API_KEY`   — optional bearer for the proxy
- `SLACK_WEBHOOK_URL` — else Slack post is silently skipped

### 4. Confirm the Sunday review lands

Next Sunday (2026-08-09), operator should see
`state/factory_targets/ARTICLE_WEEK_20260809.md` with pick/skip columns.
Flip `[ ]` to `[x]` on rows worth building around. Commit the file — the
git diff **is** the pick receipt; downstream MAP-Elites cell scoring
reads it.

## Blockers (fallbacks documented in-code)

| Env var missing | Runner behavior |
|---|---|
| `LITELLM_PROXY_URL` | falls back to regex-only scoring; every row tagged `remaining_risk=["stub_llm_label"]` |
| `SLACK_WEBHOOK_URL` | scanner still writes digest; Slack post logged as `skipped`; no crash |
| both | still produces a usable digest; operator gets same data via file only |

Runner never crashes on missing secrets. All misses go to chain-row.

## Kill conditions (baked in, no action needed)

- Any source with **3 consecutive failed fetches** → marked degraded,
  skipped for 24 h. State in
  `state/factory_targets/article_scanner_source_health.json`.
- **3 consecutive days with zero signals** → chain-row `failed`, Slack
  `halt` escalation, exit code 2. State in
  `state/factory_targets/article_scanner_empty_streak.json`.
- LiteLLM 4xx/5xx → back off 2s/4s/8s, then regex fallback. Never halts.

## Coordination with parallel LOOP-D work

If the parallel agent lands a shared Slack push helper (per operator's
mandate note), swap the `slack_escalate.post()` call in `run.py` (search
for `slack_status`) to the new helper. Behavior is otherwise identical.
Both loops write to `#hfo-synthesis` and use the same `.env` webhook.

## What is NOT wired here (out of scope, tracked)

- Harvester that reads the operator's `[x]` picks and injects them into
  MAP-Elites cell scoring — noted in `weekly_review.py` header as
  `factory/loops/article_scanner/harvest_picks.py` (planned).
- Full-text article body fetching. Only feed-provided summary +
  first-500-char snippet are stored. Paywalled hosts (WSJ, NYT, FT) get
  the shorter snippet only.
- OAuth-gated sources (Twitter/X, LinkedIn). The single X seed URL
  (`ttunguz`) is present as an operator-seeded URL only; the runner does
  not scan X directly.

## Verification receipts

Chain-row events emitted per run:

- `start_scan` (proposed)
- `fetch_source` per source (wired_with_receipts | partial)
- `finish_scan` (wired_with_receipts | partial | failed)
- `weekly_review` (wired_with_receipts | partial) — Sunday only

All rows include `clock_source: host_read` and the standard AIH2O
verifier fields.
