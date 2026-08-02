# Slack outbox — 2026-08-03 gen-133 broadcaster staging

**Status:** STAGED_NOT_SENT. Credential blocker documented in
`state/olrun/SLACK_CREDENTIAL_BLOCKER_20260803.md`.

## Fire order (once webhook / token is available)

| # | file | target channel | purpose |
|---|---|---|---|
| 00 | `00_exec_summary_command_and_control.md` | `#hfo-command-and-control` | tight session summary + top-3 Tuesday operator actions |
| 01 | `01_adr_digest_synthesis.md` | `#hfo-synthesis` | major decisions ratified this session (edit-at-source, throttle kill, kill-list, class:preauth gate rule, booking-URL hard block) |
| 02 | `02_research_reports_synthesis.md` | `#hfo-synthesis` | one block per major research doc — canon V9/V10/V11, distribution intel, partners intel, red-team, hostile-investor red-team |
| 03 | `03_blockers_andon.md` | `#hfo-andon` | all live blockers this session (Instantly key, booking URL, sandbox VM, unknown Reddit karma, Cloudflare metric API, HALT ceilings) |
| 04 | `04_cross_gen_anchor_synthesis.md` | `#hfo-synthesis` | pinned-style rehydration anchor for gen-134 |

## Timing

Slack allows ~1 msg/sec per channel. Insert `Start-Sleep 2` between sends.
Messages 01–02 have thread markers (`> in thread:`); each thread reply is a
separate `slack_post.py` call routed against the same channel with the parent
`thread_ts` as an arg — requires the token variant of the post tool (webhook
`Incoming Webhooks` does not support threading). If webhook-only, post the
digest as a single long message per file.

## Verification (once sent)

After each send, capture:
- HTTP status returned by `tools/slack_post.py` (200 = OK)
- If bot-token variant: the returned `ts` (thread timestamp) and permalink

Write each successful send as one line to
`state/olrun/SLACK_DELIVERY_LOG_20260803.jsonl`. Do NOT write any line if the
send fails or is skipped — this session left the file empty except for the
pre-flight blocker row.
