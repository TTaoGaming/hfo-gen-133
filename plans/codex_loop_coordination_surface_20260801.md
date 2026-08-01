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

## Addendum — 3 goal-pinned loops (Automations D/E/F)

Operator addendum: "you can pin a few goal loops." The first 3 automations
(A/B/C) are infrastructure — they make the coordination surface itself work.
These 3 are pinned directly to top-level HFO gen-133 goals: each one watches
one number that matters and andons when that number stalls.

| automation | goal-pin | reads | writes | andon condition |
|---|---|---|---|---|
| `hfo-codex-goal-income-hunt-4h` | $0 → first paying client | `task_queue.jsonl`, `task_results.jsonl`, own history | `task_queue.jsonl` (append one new action if none pending), `state/ssot/goal_income_hunt.jsonl` | no income-tagged positive signal in 72h |
| `hfo-codex-goal-spatial-factory-shipping-daily` | 1 branded demo shipped/day (LOGO→100APPS) | live curl of `demo01`–`demo25`-handpiano.pages.dev | `state/ssot/goal_spatial_shipping.jsonl` | live-URL set unchanged across 48h of daily fires |
| `hfo-codex-goal-cross-family-quorum-daily` | no single-family decisions on major actions | `quorum_syntheses.jsonl`, `valkyrie_votes_*.jsonl`, `chains/SIGRUN_P4.jsonl` tail | `state/ssot/goal_quorum_health.jsonl` | a keyword-matched "major" SIGRUN_P4 row has no matching quorum vote within ±24h |

Ground-truth check performed this session (not doctrine-assumed): curl'd
`demo01`–`demo12`-handpiano.pages.dev directly. Result: **only `demo01` is
live (HTTP 200); demo02–demo25 all fail DNS resolution** (not yet
provisioned). This is real signal, not a placeholder — 1 of 100 apps
shipped, consistent with the pipeline's early stage. Automation E's first
witness-test row (below) carries this exact result.

None of D/E/F call any MCP tool, plugin connector, or provider API. D uses
two fixed-URL read-only curls; E uses 25 fixed-URL read-only curls; F is
pure local file read. This is a direct application of the permission-stall
finding below, not incidental.

## Pre-authorization gates (per CRITICAL ADDENDUM — L_SCHEDULER_FIRES_PERMISSION_STALLS)

Operator-observed failure class on Antigravity: 12+ Nidhöggr conversation
windows stalled forever on a per-conversation MCP consent dialog ("Allow
using this MCP tool? hfo/board_status") — the scheduler fires correctly,
but the loop never closes because a headless run cannot answer an
interactive prompt. Applied that lens to every automation in this session,
old and new.

**What Codex's own config actually says** (`C:\Users\tommy\.codex\config.toml`,
read this session): `approval_policy = "on-request"`, `sandbox_mode =
"workspace-write"`. `on-request` means: when the agent needs to do something
outside its sandbox (network egress not already permitted, writes outside
the workspace, etc.), it prompts a human for approval. `C:\Dev` (and
therefore `C:\Dev\hfo_gen_133_forge`, `hfo_gen_131_forge`, `hfo_gen_130_forge`)
are all listed as `trust_level = "trusted"` projects, which loosens some of
that prompting for trusted-project shell commands. Several MCP servers ARE
configured (`hfo-sigrun-memory-gen130`, `node_repl`, `hfo-gen132-coordination-facade`,
`openaiDeveloperDocs`) and several plugins are enabled (`chrome`,
`computer-use`, `github`, `gmail`, `stripe`, `cloudflare`, etc.) — any of
these, if an automation's prompt actually invoked them, would be a live
candidate for the same per-conversation-consent stall seen on Antigravity.
There is no `hfo/board_status`-named tool in this Codex config; that is an
Antigravity-side MCP tool, not present here — confirmed by grep across all
config, not assumed absent.

**Does Codex have the same per-conversation gate as Antigravity?
Honest answer: UNKNOWN, not verified either way this session** — this
session cannot make Codex's scheduler fire on demand to observe a live
consent dialog (or its absence) in real time. What IS verified, directly:

1. **Grepped all 6 pre-existing ACTIVE automation.toml prompts verbatim**
   for any MCP/plugin/connector tool reference. Zero matches (the one
   `connector` hit in Garmr's prompt is inside its own FORBIDDEN list —
   `"...connector probe, GitHub/Slack write..."` — not a tool invocation).
   All 6 use only shell commands (git, sqlite reducer calls) and file
   read/write.
2. **Empirical liveness evidence already gathered this session and in
   reginleif's same-day probe** shows Fenrir completing 34 hourly cycles
   (git fetch = network, local commit) and Garmr completing hourly SQLite
   writes, unattended, with no operator present to click through a consent
   dialog. This is strong circumstantial evidence that Codex's headless
   heartbeat/cron runner does NOT block plain shell/git operations on a
   per-fire human approval in this trusted-project configuration — but it
   is evidence from bash/git-only automations, not proof for an automation
   that calls an actual MCP tool, which was never tested because none of
   the 6 do that.
3. **Applying the mitigation instead of waiting to prove the gate exists
   or not**: all 6 new automations (A–F) were designed to use ONLY the
   shell/bash tool and local file read/write — zero MCP tool calls, zero
   plugin connector calls, by construction. Each of the 6 new prompts
   contains an explicit "PERMISSION-STALL AVOIDANCE" paragraph instructing
   the model to treat any drift toward an MCP/plugin tool call as
   `ANDON_SCOPE_CREEP` and stop rather than wait on a prompt that a
   headless run can never answer. This sidesteps the open question rather
   than resolving it — named here as the honest limit of this session's
   verification.

**One-time operator pre-authorization checklist** (do these BEFORE arming
any of the 6 new automations, so they run truly unattended):

| consent surface | which loops touch it | operator action needed |
|---|---|---|
| Shell commands (git, curl) inside `C:\Dev\hfo_gen_133_forge` | A, B, C, D, E | none identified — `C:\Dev` is already `trust_level = "trusted"` in `config.toml`; git push/curl from trusted-project shell commands did not prompt this session |
| Outbound network to `*.pages.dev`, `agentreleasegate.com` | D, E | none identified — plain curl from this session's shell succeeded to `agentreleasegate.com` (HTTP 200) and `demo01-handpiano.pages.dev` (HTTP 200) without any prompt; if Codex's sandbox differs from this session's, the first armed cycle's receipt (or its absence) is the real test |
| `origin` push credential for `hfo-gen-133` GitHub repo | B | none identified this session — push succeeded via the existing git credential helper, no separate auth prompt appeared |
| Any MCP tool (`hfo-sigrun-memory-gen130`, `node_repl`, etc.) | none of A–F | N/A by design — these loops were built to never call one |
| Any plugin connector (`chrome`, `computer-use`, `github`, `gmail`, `stripe`, `cloudflare`) | none of A–F | N/A by design — same |

If, after arming, any of A–F's cycles report `ANDON_SCOPE_CREEP` or simply
stop producing chain rows on schedule, that is the `L_SCHEDULER_FIRES_PERMISSION_STALLS`
class manifesting here too — treat a silent chain (no new row in its target
JSONL at the next expected fire time) as equivalent to Antigravity's stalled
conversation window, and escalate to checking the Codex desktop UI's own
run history for that automation, the same diagnostic step reginleif's probe
already recommended for Jörmungandr.

## Fire-to-receipt witness test (per CRITICAL ADDENDUM, point 4)

This session cannot trigger Codex's scheduler directly — there is no tool
here that invokes a Codex automation on demand, only the filesystem where
its `automation.toml` lives. The closest honest substitute: manually
execute, in this session's own shell, the EXACT cycle logic written into
one automation's prompt, and land the exact receipt row it specifies into
the exact target file it names.

**Chosen: `hfo-codex-goal-spatial-factory-shipping-daily`.** Ran
`curl -s -o /dev/null -w "%{http_code}" --max-time 8 https://demoNN-handpiano.pages.dev`
for NN=01..25 exactly as step 1 of its prompt specifies. Result: `live_count=1`,
`live_urls=["demo01-handpiano.pages.dev"]`. Appended exactly the JSON shape
step 3 of its prompt specifies to `state/ssot/goal_spatial_shipping.jsonl`,
labeled `"executor":"claude_sonnet_manual_witness_test"` (not `codex_gpt`) so
the row is honestly distinguishable from a real automation fire once one
happens. **This proves the mechanism closes end-to-end — real network call,
real file write, real receipt — for the one loop tested.** It does NOT prove
Codex's own scheduler will execute this same prompt without stalling; that
remains the open question named above, resolvable only by the operator
arming it and checking for a second row with `executor=codex_gpt`.

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

All 6 new `automation.toml` files (A/B/C infrastructure + D/E/F goal-pinned)
ship with `status = "PAUSED"`. Nothing fires until the operator opens the
Codex desktop UI and flips each one to ACTIVE by hand. This plan and the
audit are the artifacts for this session; arming is an explicit separate
operator action. One (`hfo-codex-goal-spatial-factory-shipping-daily`) has
a manual witness-test row already in its target file proving the mechanism
works; the other 5 are shipped un-fired, TOML-validated only.
