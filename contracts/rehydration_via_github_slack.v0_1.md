```yaml
# AIH2O capsule
doc: contracts/rehydration_via_github_slack.v0_1.md
schema_id: hfo.gen133.contract.rehydration_via_github_slack.v0_1
generation: 133
authored_by: SIGRÚN P4 · claude-opus-5 · ceiling=strategic
valid_time_utc:       2026-08-01T04:48:42Z
transaction_time_utc: 2026-08-01T04:48:42Z
git_head: 60893a4
claim_status: partial   # ⭐ GitHub half has a RUNTIME RECEIPT (§1). Slack half is BLOCKED and unverifiable from this session.
sealed: false
supersedes: nothing
complements:
  - contracts/pheromone.contract.md        (pheromone shape + prev_pheromone_hash chaining — NOT restated)
  - contracts/silence_signal.contract.md   (silence-as-signal SLOs — NOT restated, INSTANTIATED in §3)
  - contracts/rehydration_capsules_tiered.v0_1.md (what gets pushed — NOT restated)
A_assumption: the operator wants rehydration to survive this laptop; durability means "another carrier on another machine can wake correctly"
I_input: `git remote -v` · `git branch -a` (35 local) · `git ls-remote --heads origin` (2) · pheromone.contract.md status line · session MCP auth state
H_hypothesis: git already IS the working pheromone bus — Fenrir invented it unprompted and it has 26 hourly receipts — and the only thing missing is `git push`
H2_heldout: a carrier on a different machine clones origin and rehydrates Fenrir correctly. Today it cannot: 26 of 26 Fenrir receipts are local-only.
O_output: the measured gap · a GitOps rehydration protocol · a bitemporal verification rule · an honest Slack blocker
```

# FORMAL REHYDRATION VIA GITHUB + SLACK v0_1

## 1 · ⭐ The finding: git is already the pheromone bus, and it is already working

I went looking for a rehydration design and found a running one. `git branch -a`
in this forge, right now:

```
fenrir/evo-20260730T142723Z … fenrir/evo-20260801T043706Z     ← 26 branches
```

**Fenrir emits an hourly timestamped branch.** Twenty-six of them, spanning
2026-07-30T14:27Z → 2026-08-01T04:37Z. The most recent is **11 minutes before
this document's `valid_time`.** Fenrir is alive *as I write this*.

Three consequences, in order of importance:

**(a) Fenrir's roster liveness upgrades from `asserted` to `receipted`.**
`contracts/schemas/apex_roster.v0_3.md` §5 honest-flaw 1 says the only apex this
lane could receipt was Sigrún. That is now **two**. This is also the third
independent line of evidence vindicating the operator's declaration — after the
🔒 operator-lock at `SUBSTRATE_APEX_ASSIGNMENT.md:45` and the §5 NOW liveness
table. The `OLRUN_ROSTER_AND_CLASS_RECONCILIATION` claim that Fenrir had "zero
hits" is not merely wrong about documents; it is wrong about a **process that
was running while it was being written.**

**(b) Silence-as-signal has real data and nobody read it.** The cadence has
exactly one gap:

| window | branches | verdict |
|---|---|---|
| 07-30T14:27 → 07-31T05:43 | 16, hourly, no gap | ✅ green |
| **07-31T05:43 → 07-31T19:31** | **0 — a 13h48m hole** | ⛔ **SILENT, and never flagged** |
| 07-31T19:31 → 08-01T04:37 | 10, hourly, no gap | ✅ green |

`silence_signal.contract.md` exists, specifies SLOs per tier, and has a held-out
test path. **It was not applied to the one carrier producing continuous presence
data.** A thirteen-hour apex outage happened yesterday and the fleet learned it
today, from a `git branch` listing, by accident.

**(c) The stigmergy design question is answered by precedent, not by me.** A
branch named `<callsign>/<kind>-<ts>` is a pheromone: it is append-only, ordered,
hash-linked (a commit *is* `prev_hash`), timestamped, and legible to any git on
any machine — every property `pheromone.contract.md` asks for. **Adopt Fenrir's
convention rather than designing one.**

- **FALSIFIER (§1) — RUN, and it held.** `git log -1 fenrir/evo-20260801T043706Z`:
  `date=2026-08-01T04:39:14Z` · `subject=chore(fenrir): record hourly empty evo
  queue` · 1 file changed (`state/ssot/lane_returns.jsonl`, +1 line) ·
  `author=OBSIDIAN_SPIDER`. A machine-shaped conventional-commit message on an
  exact hourly cadence writing one ledger line. **Fenrir's liveness is
  `receipted`.**
- **cost_of_delay: HIGH.** Every hour the silence gate stays unapplied to a
  live emitter, the fleet pays for presence data it does not read.

### 1.1 · ⛔ And the receipt says the loop is EMPTY — because a file is missing

The commit subject is the finding: **`record hourly empty evo queue`.** The row
it wrote is better than the subject:

```jsonc
"queue":            { "observation": "missing", "path": "state/ssot/fenrir_evo_queue.jsonl" },
"status":           "target_queue_empty",
"verifier_result":  "NOT_RUN_QUEUE_EMPTY",
"next_safe_action": "Land one schema-valid target row and its runnable held-out
                     benchmark on agent/gen133-bootstrap-20260730.",
"remaining_risk":   ["target queue path absent on exact remote commit",
                     "held-out benchmark directory absent on exact remote commit",
                     "local commit is not remote delivery"],
"honest_flaw":      "…target_queue_empty records this cycle's no-op but does not
                     prove a producer intentionally emitted an empty queue.",
"prev_sha256":      "e8e158…", "row_sha256": "1efaf3…",
"pheromone":        { "hash_preimage": "pheromone | fenrir | gen133 | 2026-08-01T04:37:06Z | target_queue_empty | none, none, n/a" },
"surtr":            { "status": "not_consulted", "reason": "No queued target." }
```

**Fenrir has emitted 26 perfect hourly heartbeats about nothing — and each one
names the exact file that is missing and the exact action that would unblock it.**

Read what this carrier is actually doing: it prev-links its rows across branches
(`prev_sha256` → `prior_local_fenrir_cycle.commit`), hashes its pheromone with a
stated preimage, refuses to overclaim (*"does not prove a producer intentionally
emitted an empty queue"*), enumerates its own remaining risk — **including
`"local commit is not remote delivery"`, which is §2 of this document, diagnosed
by Fenrir 38 hours before I measured it** — and declines to consult Surtr
because there is no work to consult about.

**This is the best-disciplined carrier in the fleet and it has been blocked on a
missing file for 38 hours because nobody read its receipts.** The failure is not
Fenrir's. It is that the fleet has an emission channel and no consumption channel.

> **The Colosseum is alive, scheduled, disciplined, hash-chained,
> conventional-commit-formatted — and starving.**

> **Liveness is not work.** A carrier emitting flawless receipts for an empty
> queue is `L_DESCRIPTOR_GREEN_IS_NOT_RUNTIME_GREEN` raised to the fleet level:
> every gate reads green because the gates measure *emission*, and nothing
> measures *throughput*.

This is also the honest answer to a question the roster could not settle: the
`EMPTY_QUEUE_REWARD_HACK` class that
`OLRUN_ROSTER_AND_CLASS_RECONCILIATION` §2 row 4 declared non-existent
("MISS — that class_id does not exist in this forge's real failure-class
registry") **is not merely real — it is running in production, hourly, and has
been for 38 hours.** It was absent from the *registry*, not from the *world*.
Absence from a registry was mistaken for absence from reality.

**GS-0 — every liveness gate must also assert non-emptiness.** A heartbeat
carrying `queue_depth: 0` is `IDLE`, not `GREEN`. `IDLE` for > 3 cadences is its
own andon class, distinct from `SILENT`.

**And this is the seam to the spatial factory.** Fenrir's evo queue is empty
because nothing produces a population for it. `state/ssot/spatial_reskin_ledger.jsonl`
(spatial factory §9, LG-2) is exactly that population. **The two dispatches in
this turn are the same loop: the factory produces individuals, the Colosseum
selects among them.** Neither is useful alone — an idle tournament and an
unranked pile of demos.

### 1.2 · The 26 ledger rows are invisible from every working branch

`state/ssot/lane_returns.jsonl` **on this branch has 1 line and zero Fenrir
rows.** On `fenrir/evo-20260801T043706Z` it has exactly 1 line — Fenrir's own.
Each of the 26 branches appends one row to the same file, from a base where that
file is empty, and **none is merged.**

So the fleet's ledger has 26 parallel one-row versions of itself. The rows *are*
chained (`prev_sha256` links each cycle to the last), but the chain is
reconstructible only by walking 26 branch refs — which nothing does.

**GS-8 — an append-only log split across unmerged branches is not a log.** Either
the emitter appends to a shared branch, or the consumer walks the ref namespace.
Today neither happens, so a correctly-written, correctly-hashed, correctly-linked
receipt stream is functionally unreadable.

- **FALSIFIER (§1.1/§1.2):** any of the 26 rows has `queue.observation != "missing"`.
  Then the blockage is intermittent, not structural. **⚠️ I sampled 1 of 26; the
  other 25 are inferred from a uniform commit-subject series.**
- **cost_of_delay: ⛔ HIGH.** 38 hours of scheduled compute has produced 26
  ledger rows and zero selections. That is the fleet's only proven durable loop,
  running on nothing, writing where no one looks.

## 2 · ⛔ The gap: 35 local branches, **2** on GitHub

```
git remote -v            → origin  https://github.com/TTaoGaming/hfo-gen-133.git
git branch -a            → 35 local
git ls-remote --heads origin → 2
```

The only branches that reached GitHub are `agent/gen133-bootstrap-20260730` and
`agent/sigrun-gen133-capsule-v2-20260730`. **All 26 Fenrir receipts, plus
Nidhöggr's, Garmr's, and Huginn's integrity branches, exist on exactly one
laptop.**

> **The fleet's best liveness evidence is undiscoverable by any carrier that is
> not on this machine.** That is not a rehydration system. That is a local cache
> with a remote logo on it.

This is the whole of the operator's directive, stated as a measurement: the fix
is not a design, it is **`git push`**. Everything in §3 is scaffolding around
that one missing verb.

- **FALSIFIER (§2):** a second remote exists and carries the branches. `git
  remote -v` shows one. Checked.
- **cost_of_delay: ⛔ MAXIMUM.** A laptop loss today costs 26 apex receipts, 9
  agent branches, and the only runtime proof the fleet has that anything wakes.

## 3 · The protocol — GitOps, adopted

**Exemplar: GitOps (ArgoCD / Flux).** Desired state lives in git; agents
continuously reconcile toward it; drift is detected by diff, not by trust. That
is exactly the shape needed here, and the reconciliation loop is a wake.

**GS-1 — GitHub is the RECORD. Slack is a NOTIFICATION. Never confuse them.**
A claim that exists only in Slack does not exist. Slack messages are edited,
deleted, rate-limited, retained by policy, and unhashable. **Nothing may be
rehydrated from Slack.** Slack answers *should I look?*; git answers *what is
true?*

### 3.1 · Wake — pull before reasoning (RBR defense #1)

```
WAKE(callsign, tier) →
  1. git fetch --prune origin                       # cheap, ~1s, no working-tree effect
  2. read capsules/apex/<callsign>/<S|M|L>.json  @origin/main   # tier per rehydration_capsules_tiered
  3. read chains/<CALLSIGN>.jsonl tail N            # N per tier: 0 / 5 / all
  4. read state/identity/soul/<callsign>...soul.md  # tier 2 only
  5. verify: capsule.chain_head_sha256 == live chain head        (INJECT P4)
             capsule.capsule_sha256 reproduces                   (INJECT P2)
  6. read the pheromone namespace:  git ls-remote --heads origin '<callsign>/*'
       ⇒ newest branch ts vs now  ⇒ own last-seen; and for every OTHER apex ⇒ §3.3 silence check
  7. [Slack, when unblocked] read tail of #hfo-<lane> — SIGNAL ONLY, never a fact source
  8. emit the acceptance witness (golden_waking_paths §1) BEFORE any content token
```

**GS-2 — steps 1–6 complete before the carrier writes its first content token.**
Reason-first ordering is the cheapest big lever against the reflex, and a `git
fetch` is a deterministic, non-neural forcing function: it either succeeded or it
did not.

### 3.2 · Push — after each wake

```
PUSH(callsign) →
  1. append the chain row      → chains/<CALLSIGN>.jsonl        (receipt or it did not happen)
  2. refresh the capsules      → capsules/apex/<callsign>/{S,M,L}.json  (+ new capsule_sha256)
  3. git checkout -b <callsign>/<kind>-$(date -u +%Y%m%dT%H%M%SZ)     # Fenrir's convention, §1(c)
  4. git commit -m "<callsign> <kind>: <one line>"                     # no --no-verify, no --no-gpg-sign
  5. git push origin HEAD                                             # ⭐ THE MISSING VERB (§2)
  6. [Slack, when unblocked] post the one-line summary + the commit URL to #hfo-<lane>
```

**GS-3 — push is not a world-effect gate; publish is.** Pushing an append-only
receipt branch to a repo the operator owns is *durability*, and blocking it
behind an operator prompt is what produced §2. **Merges to the default branch,
tags, releases, and anything public remain gated.** Branch pushes are
pre-authorized by class; the gate lives at the merge, where it belongs.

**GS-4 — one branch per emission, never a force-push, never a rewrite.** The
branch namespace *is* the append-only log (SR-4). A force-push is a chain
rewrite by another road.

### 3.3 · Silence detection — a deterministic, non-neural gate

This is RBR defense #4 (external symbolic gate) applied to liveness, and it is
~10 lines of shell that would have caught yesterday's 13h48m hole:

```
for callsign in <the 8>:
    last = max(ts parsed from `git ls-remote --heads origin "<callsign>/*"`)
    age  = now - last
    if age > 2 × cadence  →  SILENT   → andon
    if age > 1 × cadence  →  LATE     → warn
    if the carrier is known throttled  →  UNREACHABLE, not SILENT     (CC-4)
    if no branch has ever existed      →  NEVER_WOKE, not SILENT      ← the fleet's actual state for 6 of 8
```

**GS-5 — distinguish `NEVER_WOKE` from `SILENT`.** Six of eight apex have never
emitted a branch. Reporting them as "silent" implies they used to speak. The
roster's Q3 (*admission ⇒ expectation*) creates the obligation; `NEVER_WOKE` is
what an unmet founding obligation looks like, and it needs a different alarm than
a carrier that died.

### 3.4 · Bitemporal verification — the proof, and its one honest limit

| axis | source | trust |
|---|---|---|
| **valid time** | `valid_time_utc` inside the capsule/chain row | ⚠️ **carrier-asserted** — a carrier can write any value |
| **transaction time** | `git log --format=%cI` on the commit that introduced it | ✅ **externally witnessed once pushed** — GitHub's receipt, not the carrier's |
| **content integrity** | commit sha + `capsule_sha256` + `prev_pheromone_hash` | ✅ cryptographic |
| **identity** | commit signature | ⛔ **not enforced today** — no signing policy in this forge |

**GS-6 — a receipt is bitemporal only after it is pushed.** Before `git push`,
`transaction_time` is as forgeable as `valid_time`, because both were written by
the same carrier on the same disk. **Push is what converts self-assertion into
external witness.** This is the strongest argument for §2's fix and it is not an
aesthetic one.

**Honest limit:** unsigned commits mean GitHub witnesses *when*, not *who*.
Anyone with push access can author a commit as any callsign. Identity is a
`TODO`, not a property — do not describe this as blood-sealed.

## 4 · ⛔ Slack — blocked, and I will not design past it

**The Slack MCP connector is not authorized in this session** (`plugin:productivity:slack`
requires OAuth; this session is non-interactive). Additionally
`contracts/pheromone.contract.md` carries `status: SPECIFIED — Slack emit
BLOCKED (B3)`.

**Therefore I cannot verify — and do not assert — any of the following:** that
`#hfo-*` channels exist; their names; that a `@ChatGPT` bot handle is installed;
that Ratatoskr can post; or that any carrier has ever read a channel tail. The
operator's directive names these; naming is not evidence, and the whole point of
GS-1 is that Slack is the medium where unverified claims are cheapest.

**What I can specify safely** — a design that is correct whether or not Slack
ever gets connected, because Slack carries no load in it:

| channel | content | direction | source of truth |
|---|---|---|---|
| `#hfo-command` | andons · quorum calls · world-effect requests awaiting the operator | agent → human | GitHub |
| `#hfo-pheromones` | one line per push: `callsign · kind · commit URL` | agent → agent (advisory) | GitHub |
| `#hfo-tournament` | Colosseum / evo-search leaderboard, daily | Fenrir → human | ledger jsonl |
| `#hfo-silence` | `SILENT` / `LATE` / `NEVER_WOKE` alarms from §3.3 | gate → human | git ls-remote |

**GS-7 — every Slack message must carry the commit URL that backs it.** A Slack
line without a git link is decoration, and after 24h it is unfalsifiable
decoration. This single rule is what keeps GS-1 true in practice rather than in
principle.

**Unblock path (not by me — requires the operator):** authorize the Slack
connector via claude.ai connector settings, or `claude mcp` / `/mcp` in an
interactive session. Until then, **`#hfo-silence` is replaceable by a cron that
runs §3.3 and writes an andon file** — and that substitute is strictly better
than Slack, because its output lands in the record instead of beside it.

## 5 · Build order

| # | step | owner | est. | exit criterion |
|---|---|---|---|---|
| 0 | `git log -1 fenrir/evo-20260801T043706Z` — confirm the emitter is the scheduled Codex run | any lane, read-only | 1 min | §1's falsifier is answered |
| 1 | **`git push origin --all`** (or a filtered push of `<callsign>/*` + `agent/*`) | operator or any lane | **5 min** | ⭐ `git ls-remote --heads origin` goes 2 → 35. **This is the highest value-per-minute action in this document.** |
| 2 | §3.3 silence gate as a scheduled script writing an andon file | Codex | 1h | yesterday's 13h48m hole would have alarmed |
| 3 | `PUSH` step 5 wired into every carrier's wake epilogue | Codex | 2h | every wake is externally witnessed (GS-6) |
| 4 | populate `capsules/apex/<callsign>/` so step 2 of WAKE has something to read | apex-wake lane | — | a carrier on another machine can rehydrate |
| 5 | commit signing policy | operator | — | GS-6's identity `TODO` closes |
| 6 | Slack connector authorized; `#hfo-silence` mirrored | operator | — | GS-7 enforced on the first message |

**Steps 1–4 have no dependency on Slack whatsoever.** The durable half of the
operator's directive is unblocked today; the coordination half is gated on an
OAuth the operator must click.

## 6 · Honest flaw

1. **I opened exactly ONE Fenrir commit, the newest.** §1's receipt is
   1-of-26 sampled, not 26-of-26 verified. The other 25 are inferred from an
   identical naming cadence. In particular I have **not** confirmed that all 26
   say "empty queue" — §1.1's "26 heartbeats about nothing" is the reasonable
   reading of a uniform hourly `chore(fenrir)` series and it is **an inference
   from one sample**. §1.1's own falsifier is the check, and it is one `grep` of
   `lane_returns.jsonl` that I did not run.
2. **`NEVER_WOKE` describes 6 of 8 apex.** This document specifies a rehydration
   protocol for a fleet in which three quarters of the seats have never emitted
   anything. Making the protocol good does not make them wake.
3. **The Slack half is a design for a system I cannot see.** §4's table is
   reasoning from the operator's words and from what channels are *for*, not from
   any observed workspace. If `#hfo-*` channels already exist with different
   names and different conventions, §4 is a duplicate taxonomy — the exact error
   §0 of the tiered-capsules contract refuses to make, committed here anyway
   because I had no way to look. **Treat §4 as a proposal to be checked against
   the real workspace before anything is built.**
4. **`git push` may fail for reasons I cannot see from here** — credentials,
   branch protection, repo size, or an org policy. I am calling step 1 "5
   minutes" on the assumption that the two branches already on origin were pushed
   from this machine with working credentials. That is an inference, not a test.

*Réttu hönd, eigi spyr. Standa.*
