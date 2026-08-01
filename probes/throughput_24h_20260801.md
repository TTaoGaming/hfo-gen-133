---
probe: throughput_24h
window: 2026-07-31T13:31Z to 2026-08-01T13:31Z
run_by: THRUD sonnet5
requested_for: local_b4579cd1
---

# Throughput probe — last 24h — 2026-08-01

Numbers only. UNKNOWN where not derivable from this session's tool access. Adjectives rejected.

## External effect

| Metric | Value | Source |
|---|---|---|
| handpiano.com HTTP status | 200, 0.34s | `curl -s -o /dev/null -w "%{http_code}" https://handpiano.com` |
| agentreleasegate.com HTTP status | 200, 0.28s | same, target agentreleasegate.com |
| tryagentreleasegate.com HTTP status | 000 (TIMEOUT, curl errcode 28, TLS handshake completed then 0 bytes in 15s) | same, target tryagentreleasegate.com, retried with `-v`, DNS resolved to Cloudflare IP 2606:4700:3037::6815:4006, request sent, no response |
| demo01-handpiano.pages.dev HTTP status | 200, 0.23s | same, target demo01-handpiano.pages.dev |
| GitHub commits pushed, all TTaoGaming repos, 24h | 1 repo touched: `hfo-gen-133`, `pushed_at: 2026-08-01T13:25:05Z` | `curl -s https://api.github.com/users/TTaoGaming/repos?sort=pushed` — next most recent repo push was `sigrun_lineage_lifeboat` at 2026-07-25 (6 days stale) |
| GitHub commits, this local repo, all branches, 24h | 276 total; 270 on `origin/agent/gen133-bootstrap-20260730` (the pushed/active branch); 0 on current checked-out branch `agent/sigrun-gen133-spec-20260730` | `git log --all --since="24 hours ago" --oneline`, per-branch breakdown via loop over `git branch -a` |
| Commits on THIS session's checked-out branch, 24h | 0 (HEAD commit `60893a4` is dated 2026-07-30 08:46:59 -0600, ~29h old) | `git log --since="24 hours ago" --oneline` on HEAD |
| Current branch pushed to origin? | NO — `git rev-parse origin/agent/sigrun-gen133-spec-20260730` returns "unknown revision", branch not on remote at all | `git branch -r` listing does not contain it |
| Emails sent (Instantly.ai) | UNKNOWN — no tool access to Instantly.ai from this session | not probed |
| Content published (Substack/LinkedIn/Twitter/blog) | UNKNOWN — no tool access, not probed | not probed |

## Internal work-product

| Metric | Value | Source |
|---|---|---|
| Files modified/created under `hfo_gen_133_forge/` (excl. `.git/`), 24h | 1243 files | `find "C:/Dev/hfo_gen_133_forge" -type f -newermt "24 hours ago" \| grep -v '\.git/' \| wc -l` |
| Total bytes of those files | 75M | `du -ch <filelist>` |
| Breakdown by top-level dir (file count) | `projects` 1097, `resources` 63, `contracts` 33, `state` 16, `tools` 6, `inbox` 5, `archives` 5, `plans` 2, `chains` 2, `capsules` 2, `canon` 2, repo-root loose `.md` 9 | same filelist, `sed` on path + `sort \| uniq -c` |
| `chains/SIGRUN_P4.jsonl` total rows | 37 | `wc -l` |
| `chains/SIGRUN_P4.jsonl` rows dated 20260801 | 10 | `grep -c 20260801` |
| `chains/SIGRUN_P4.jsonl` last-modified | 2026-07-31 23:20:53 -0600 (~14h ago) | `stat` |
| `state/ssot/*.jsonl` files touched in 24h | 14 of 15 files in that dir | per-file `find -newermt` check |
| Largest `state/ssot` row count touched in 24h | `heritage_inventory_20260801.jsonl` 300 rows | `wc -l` |
| Files repo-wide (of the 1243 touched-in-24h set) containing string `sigrun_apex` | 2 | `grep -l sigrun_apex <filelist> \| wc -l` |
| Uncommitted working-tree changes on current branch | 100 total: 71 untracked (`??`), 28 deleted (`D`), 1 modified (`M`) | `git status --porcelain \| awk '{print $1}' \| sort \| uniq -c` |

## Claimed vs delivered (drift signal)

| Metric | Value | Source |
|---|---|---|
| Sessions with `lastActivityAt` in last 24h | ≥40 (of 50 rows returned; `list_sessions` has no explicit 24h filter and the call caps at 50 rows total across ALL history, so 40 is a floor, not a ceiling — true count could be higher) | `mcp__ccd_session_mgmt__list_sessions(limit=50)`, manual timestamp cutoff at 2026-07-31T13:32Z |
| Sessions currently `isRunning: true` at probe time | 6 (`local_603f3b01`, `local_8a34fce6`, `local_a411a1f2`, `local_e2c62a57`, `local_b4579cd1`, `local_85d61bcf`) | same listing, `isRunning` field |
| Sessions that produced a verifiable chain row / bytes-on-disk / external URL, per-session attribution | UNKNOWN — `list_sessions` returns title/cwd/timestamps only, no per-session diff or output attribution; would require opening each session transcript individually (out of 30-min timebox) | not measured |
| productive_fraction (sessions → verified artifact) | UNKNOWN — cannot compute without per-session attribution above. Aggregate proxy only: 1243 files touched / 276 repo commits / 1 external repo pushed / 1 of 4 checked URLs down, in a 24h window with ≥40 sessions active | derived, not measured directly |

## One-line conclusion

**2 URLs up (handpiano.com, agentreleasegate.com), 1 URL up on Pages (demo01-handpiano.pages.dev), 1 URL DOWN (tryagentreleasegate.com — TLS connects, 0 bytes, 15s timeout) / 276 commits pushed across all branches in 24h (270 on the active bootstrap branch, 0 on this session's own branch, which also isn't pushed to origin) / 75M across 1243 files shipped internally / productive_fraction UNKNOWN (session-level attribution not available from `list_sessions`, only aggregate repo/URL evidence above).**
