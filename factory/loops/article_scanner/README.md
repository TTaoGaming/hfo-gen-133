# article_scanner

Daily scan of named-author blogs, AI newsletters, and community
aggregators. Scores each item against six factory axes, writes a
daily digest, and posts the headline to Slack. Companion to LOOP-D
(`demand_signal_mine`).

See `SPEC.md` for the full contract and `sources.yaml` for the feed
list.

## Manual invocation

```powershell
# Windows (operator's home rig)
python C:\Dev\hfo_gen_133_forge\factory\loops\article_scanner\run.py `
  --sources C:\Dev\hfo_gen_133_forge\factory\loops\article_scanner\sources.yaml `
  --seed    C:\Dev\hfo_gen_133_forge\factory\loops\article_scanner\seed_urls.json
```

```bash
# POSIX / GitHub Actions
python factory/loops/article_scanner/run.py \
  --sources factory/loops/article_scanner/sources.yaml \
  --seed    factory/loops/article_scanner/seed_urls.json
```

Useful flags:

- `--dry-run` — skip the LLM call; regex-only scoring
- `--window-hours 168` — one-week backfill
- `--threshold 0.20` — widen the funnel
- `--sources-only ghuntley,humanlayer` — run against a subset

## Weekly review

Every Sunday, run:

```powershell
python C:\Dev\hfo_gen_133_forge\factory\loops\article_scanner\weekly_review.py
```

Writes `state/factory_targets/ARTICLE_WEEK_<yyyymmdd>.md` — top-20 of
the past 7 days with `pick`/`skip`/`note` columns. Operator edits the
file in place; downstream MAP-Elites scoring picks it up.

## Cron install

- **Windows Task Scheduler** — `.\install_windows_task.ps1`
- **GitHub Actions** — `.github/workflows/article-scanner.yml`
  (already committed; enable by merging to `main`)

## Environment

- `LITELLM_PROXY_URL` — required for LLM scoring; falls back to
  regex-only stub if missing.
- `LITELLM_API_KEY` — optional bearer token for the proxy.
- `SLACK_WEBHOOK_URL` — required for headline posts to
  `#hfo-synthesis`; skipped silently if unset.

All secrets read from process env or repo-root `.env` (autoloaded).

## Outputs

| Path | What |
|---|---|
| `state/factory_targets/article_signals.jsonl` | every scored signal, all time |
| `state/factory_targets/ARTICLE_DIGEST_<yyyymmdd>.md` | daily top-10 |
| `state/factory_targets/ARTICLE_WEEK_<yyyymmdd>.md` | Sunday top-20 for operator pick/skip |
| `state/factory_targets/article_scanner_source_health.json` | consecutive-failure counter per source |
| `state/loop_receipts/article_scanner_<yyyymmdd>.jsonl` | chain-row receipts |

## Coordination with LOOP-D

LOOP-D (`demand_signal_mine`) covers Reddit + HN pain patterns. LOOP-A
(this loop) covers named-author industry-evolution signal. They share
the `slack_escalate` and `litellm_client` libs. They do **not** share a
digest — different audiences.
