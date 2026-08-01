---
callsign: codex_loop_builder
generation: 133
domain: cross-substrate coordination surface (local FS + GitHub + Slack-deferred)
plan_utc: 2026-08-01T13:45:00Z
---

# Codex Loop Coordination Surface — gen-133

Operator directive: "launch codex gpt agents on loops as well and coordinate
with local or GitHub and slack." This plan is the wiring diagram for the 3
new Codex automations built this session (all shipped `status = "PAUSED"` —
operator arms them manually in the Codex UI; see Discipline section).

## Diagram — who writes what, who reads what

```
                         C:\Dev\hfo_gen_133_forge  (shared mirror, local FS)
                         ================================================
  state/ssot/task_queue.jsonl  <-- producer(s): Sigrun / any Claude session
        |
        | reads (claim-by-file-order, never rewrites queue)
        v
  hfo-codex-pullwork-hourly (NEW, Codex, hourly)
        |
        | appends
        v
  state/ssot/task_results.jsonl  ---------------------\
                                                         |
  state/ssot/andon_pulls.jsonl  <--- appended on blocker by ANY of the 3 new  |
        ^                            automations (pullwork, github-push,      |
        |                            chain-watch is read-only and never       |
        |                            writes here itself, see below)           |
        |                                                                     |
  chains/SIGRUN_P4.jsonl  <--- Claude/Sigrun sessions (existing)              |
  state/ssot/lane_returns.jsonl  <--- Fenrir (existing Codex automation)      |
  state/ssot/wake_receipts.jsonl <--- new: any actor's wake capsule           |
        |                                                                     |
        | all 5 tailed hourly                                                |
        v                                                                     |
  hfo-codex-chain-tail-poll-hourly (NEW, Codex, hourly, READ-ONLY)            |
        |                                                                     |
        | appends                                                            |
        v                                                                     |
  state/ssot/codex_chain_watcher.jsonl  <-- cross-substrate awareness record  |
        (any Claude session, Sigrun, or operator can tail this to see        |
         "what did Codex loops notice since I was last here")                |
                                                                               |
  <all of the above, plus whatever else changed in the working tree>  <------/
        |
        | git add -A && commit && push (own branch only, never force)
        v
  hfo-codex-github-push-4h (NEW, Codex, every 4h)
        |
        | appends
        v
  state/ssot/github_pushes.jsonl  --> GitHub remote (origin/<current branch>)
        |
        v
  ============================================================
  GitHub: https://github.com/TTaoGaming/hfo-gen-133
  ============================================================
        |
        | any agent with `git fetch`/`git pull` access sees fresh state
        v
  Claude Code sessions (this one) / Antigravity / ChatGPT-cloud / future
  Codex sessions on other machines -- all converge on the same repo state
  within one push cycle (<=4h latency)
```

## Surfaces work meets on

1. **Local FS (`state/ssot/*.jsonl`, `chains/*.jsonl`)** — the fast surface,
   sub-hour latency, but only visible to processes with filesystem access to
   this exact machine's `C:\Dev\hfo_gen_133_forge` checkout. This is where
   the 3 new automations do their actual read/write work.
2. **GitHub (`origin/<branch>`)** — the slow surface (4h cadence via
   Automation B), but the ONLY one visible cross-machine. This is what makes
   the local JSONL rows readable by a Claude session running on a different
   host, or by Antigravity, or by a future ChatGPT-cloud agent that can only
   read GitHub, not this laptop's disk.
3. **Slack (#hfo-synthesis)** — already used by the existing Fenrir and
   Jörmungandr automations for one-pheromone-per-cycle broadcasts. Not wired
   for the 3 new automations this session (see Deferred below).

## Verified this session

- `git remote -v` in `C:\Dev\hfo_gen_133_forge` confirms `origin` =
  `https://github.com/TTaoGaming/hfo-gen-133.git` (fetch+push). Remote
  exists; no remote-creation needed.
- `state/ssot/` directory exists with 19 pre-existing JSONL files including
  `task_queue.jsonl` (schema `hfo.gen133.schema.task_queue.v0_1`, 1 QUEUED
  row) and `task_results.jsonl` (0 rows — genuinely empty, not missing).
- 5 files the new automations need did not exist and were created empty this
  session (append-only JSONL, safe to start at 0 rows):
  `andon_pulls.jsonl`, `wake_receipts.jsonl`, `github_pushes.jsonl`,
  `codex_chain_watcher.jsonl`, `slack_bridge.jsonl`.
- Manual test push proof: see `state/ssot/github_pushes.jsonl` first row
  (this session, hand-run, not via the automation) plus the commit SHA
  reported in the return row to `inbox/olrun/`.

## Deferred — Slack

Per the operator's directive text ("Slack coordination = deferred"), no
Slack API call was attempted from this session. `state/ssot/slack_bridge.jsonl`
was created empty as the landing spot: the intended shape is that a future
Slack-authorized session (interactive Claude with the Slack MCP connected,
or a Codex automation with resolved channel IDs like Fenrir/Jörmungandr
already have) posts a pheromone per notable row in `codex_chain_watcher.jsonl`
or `github_pushes.jsonl`, and any local reader can also just tail
`slack_bridge.jsonl` to see what would have been said without needing Slack
access itself. Wiring the actual Slack post is out of scope for this session.

## Honest flaws / open risks

- **Automation B (`github-push-4h`) does `git add -A` on a shared mirror
  that other lanes actively edit.** This session's own `git status` showed
  ~10 deleted files and ~15 untracked files already in flight before this
  work started (unrelated restructuring, not touched here). Once armed,
  every 4h fire will sweep up whatever is dirty at that moment under a
  `chore(codex-sync)` commit authored by Codex, not by whichever lane
  actually made the change. This is exactly what the operator's spec asked
  for, but it does blur attribution. Mitigated only by: (a) it never force-
  pushes, (b) it aborts on conflict/detached-HEAD, (c) every push lands a
  receipt row naming the exact file count and commit SHA so the blur is at
  least auditable after the fact. Not fixed further — operator's call on
  whether that trade-off is acceptable before arming.
- **Fenrir's 34 orphaned `fenrir/evo-*` branches** (found during the audit,
  see `probes/codex_automation_audit_20260801.md`) are a pre-existing
  condition, not caused by anything in this session. `hfo-codex-github-push-4h`
  only pushes the currently checked-out branch, so it will not accidentally
  merge or clean up Fenrir's orphans — flagged here only so the operator
  doesn't conflate the two loops' branch hygiene.
- **`hfo-codex-pullwork-hourly`'s claim mechanism is optimistic, not
  locked.** Because it never rewrites `task_queue.jsonl` in place (to avoid
  concurrent-writer corruption), two different pullwork-style consumers
  racing on the same hour could both pick the same QUEUED row. This is
  acceptable at WIP=1 with a single armed consumer; if the operator arms a
  second pull-style loop against the same queue later, add a real claim
  marker (e.g. a `claimed_by`/`claimed_at` row appended to a separate
  claims file) before that point.

## Discipline confirmation

All 3 new `automation.toml` files ship with `status = "PAUSED"`. Nothing
fires until the operator opens the Codex desktop UI and flips each one to
ACTIVE by hand. This plan and the audit are the artifacts for this session;
arming is an explicit separate operator action.
