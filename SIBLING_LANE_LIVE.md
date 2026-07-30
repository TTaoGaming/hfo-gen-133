# ⚠️ SIBLING_LANE_LIVE.md — two writers, one seat. Operator reconciliation needed.

```yaml
schema_id: hfo.gen133.sibling_lane_blocker.v1_0
severity: HIGH
status: UNRESOLVED — deferred to operator
valid_time_utc: 2026-07-30T13:25:00Z
raised_by: SIGRUN_P4 apex compose lane · claude-opus-5 · session 5f1ef0c9
```

## What happened

During one session, `git HEAD` at this forge advanced **twice with no action by
this lane**:

```
627e5ee  feat(gen133): add deterministic Sigrun heritage capsule family   (~23 min in)
f220090  chore(gen133): checkpoint capsule publication hold               (~21 min in)
```

Both touched `capsules/**`. Additionally `state/sigrun/` appeared **untracked**
after this lane's final commit — a third unattributed write.

## Current state (verified 2026-07-30T13:25Z)

| check | result |
|---|---|
| `list_sessions` | **no lane currently running** — all sessions `isRunning: false` |
| `HEAD` vs `origin` | **identical** (`1fa3555`) — nothing unpushed, no clobber risk |
| path collision | **NONE** — sibling touched `capsules/**`, this lane touched everything else. Disjoint |
| chain rows written by either | **ZERO** — `chains/` at gen-133 is empty |
| untracked residue | `state/sigrun/` — unattributed, not committed by this lane |

**Nothing is corrupted.** This is a governance defect, not a data-loss event.

## Why the detection is weak, and this is the real finding

1. **`git author` cannot discriminate.** All 11 commits carry
   `OBSIDIAN_SPIDER`. Two different writers, one identity — so the audit trail
   cannot answer "who wrote this."
2. **The session query cannot see across providers.** `list_sessions` enumerates
   local CCD sessions only. A Codex or ChatGPT-desktop lane is invisible to it.
   That limit was stated at 05:20Z and confirmed as the actual failure mode 50
   minutes later.
3. **The detection was accidental.** It surfaced because a routine `git status`
   looked different than one taken earlier. There is no detector — only a lucky
   diff.
4. **Floor invariant F3 (single writer) is enforced by nothing here.** No lock
   file, no kernel, no gate. It held today only because neither lane wrote a chain.

## What the operator needs to reconcile

| # | question | why it matters |
|---|---|---|
| 1 | **Which process made `627e5ee` / `f220090` / `state/sigrun/`?** Likely a Codex or ChatGPT-desktop lane — the commit style and the authored `build_capsules.py` fit — but that is inference, not identification | until it is named, nobody can tell whether two carriers occupy P4 |
| 2 | **Partition ownership, or stop one.** Proposed split: sibling owns `capsules/**`; this lane's successor owns the rest | disjoint paths are why nothing broke; that was luck, not design |
| 3 | **Give each writer a distinct git identity** | `OBSIDIAN_SPIDER` for both makes the history unauditable |
| 4 | **Repo name diverges from convention** — this lane created `hfo-gen-133`, but the operator's pattern is `hive-fleet-obsidian-gen-132`. Optional fix: `gh repo rename hive-fleet-obsidian-gen-133` (GitHub auto-redirects the old URL; history preserved). **Not executed — outside the hard-stop scope** | consistency for anyone following the per-gen repo pattern |

## Minimum fix (the actual cure)

A **lock file at the forge root** claimed before any write:

```json
{"holder": "<lane id>", "substrate": "<model/provider>",
 "claimed_utc": "...", "expires_utc": "...", "paths": ["..."]}
```

Claimed inside the lock, released explicitly, **never expired by timeout** (kernel
invariant 6). A session query is necessary and demonstrably not sufficient — it
cannot see the writers that actually showed up.

## Push status

**Everything committed by this lane is already pushed** (`HEAD == origin ==
1fa3555`). Nothing was deferred and nothing is at risk of clobbering. This file is
a **blocker notice**, not a hold on unpushed work.

*No receipt = no state. Two writers on one seat is a defect, not a team.*
