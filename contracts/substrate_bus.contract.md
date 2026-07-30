# CONTRACT — the four-substrate bus

```yaml
contract: substrate_bus
schema_id: hfo.gen133.contract.substrate_bus.v0_1
spec: GEN133_ARCHITECTURE_PRINCIPLES.md §2, §3
companions: contracts/pheromone.contract.md · contracts/crypto_anchor.contract.md
            contracts/bitemporal_rollup.contract.md
test: tests/held_out/substrate_bus/red_first.md
authored_by: SIGRÚN P4 · claude-opus-5
valid_time_utc: 2026-07-30T00:00:00Z
status: SPECIFIED — 1 of 4 substrates live (git). Slack ⛔B3 · XTDB not running · SQLite unbuilt
sealed: false
```

## 1 · The four substrates and what each is FOR

| substrate | role | authority | cadence |
|---|---|---|---|
| **git** | identity · chains · specs · code | ⭐ **CANONICAL** | commit-triggered |
| **Slack** | fast pheromone bus · human-legible summaries | projection | real-time |
| **XTDB** | bitemporal graph · as-of queries | projection | batch |
| **SQLite** | per-carrier local checkpoint · working memory · LangGraph state | **local only** | continuous |

### The one rule that makes this a bus and not a swamp

> **SB-1 — git is authoritative; everything else is a re-derivable projection.**
>
> If a projection disagrees with git, **the projection is wrong and gets
> rebuilt**. Never repair git from a projection. A projection that cannot be
> dropped and rebuilt from the log has silently become a second source of truth,
> and two sources of truth is zero sources of truth.

This is ADR g130-0144 carried forward: all projection returns are **evidence, not
truth**. The append-only chains are authority.

---

## 2 · git — canonical

**Holds:** `state/identity/soul/**` · `chains/*.jsonl` · `state/ssot/*.jsonl` ·
contracts · specs · code · `state/roster/ROSTER.json`.

| aspect | rule |
|---|---|
| auth | **push is operator-controlled** (world-effect gate). Reads are open — the repo is public |
| write path | carrier appends a chain row → commits → push is gated |
| cadence | commit-triggered. Another carrier learns of it on its next pull |
| ordering | per-carrier total order via `prev_hash`. **No global order** (PH-4) |
| conflict | two rows referencing one ancestor is a **legal DAG, not a fork** (M-3). A *disputed head* is a fork and is `andon` |

**SB-2 — a pheromone reaches git before it reaches anywhere else.** git-first,
then best-effort fan-out. A pheromone that made it to Slack but not to git did
not happen.

**SB-3 — pull latency is a real cost and must be budgeted.** Commit-triggered
coordination means a valkyrie emitting hourly is visible to peers only after
their next pull. For an hourly tier that is fine. **For sub-hourly coordination
it is not**, which is precisely what Slack is for (§3).

> ⚠️ **UNDER_SPECIFIED — push is operator-gated, and 72 carriers cannot each wait
> for a human.** This is the single largest unsolved problem in the bus: the
> canonical substrate has a human in its write path. Options, none chosen:
> (a) a narrow append-only bot credential scoped to `state/ssot/` and `chains/`
> only; (b) carriers write locally and one scheduled pusher batches; (c) chain
> rows go to a separate repo with looser gating than specs and code.
> `TODO: operator picks. Until then, multi-carrier coordination through git is`
> `throttled to the rate a human presses a button, and no cadence claim in this`
> `architecture is achievable.` **This blocks the whole fleet, not just the mesh.**

---

## 3 · Slack — the fast pheromone bus

**Holds:** every pheromone, in human-legible form. Summaries. `andon`.

| aspect | rule |
|---|---|
| auth | `@ChatGPT` bot posts from Codex · operator posts as human · apex/valkyrie post via webhook |
| channels | `#hfo-synthesis` (pheromones) · `#hfo-andon` (andon only) · others per `areas/institution/slack/channels.md` |
| cadence | real-time |
| authority | **none.** Projection only |

**SB-4 — a Slack outage must never create phantom silence.** A carrier that
reached git is not flagged silent, whatever Slack shows. Silence evaluation reads
**git**, and Slack is where humans watch it happen. Inverting this makes an
outage in a non-authoritative service look like a fleet-wide death.

**SB-5 — Slack posting is a SEND** and stays operator-gated until an authorized
bot identity exists. ⛔ **B3.** Claude lanes additionally have no Slack connector
and cannot post at all in non-interactive sessions — **half the fleet is
write-blind on the human surface**, and that asymmetry is a fact about the
current wiring, not a design choice.

**SB-6 — consumers are idempotent on `hash`.** Delivery is at-least-once.

---

## 4 · XTDB — the bitemporal graph

**Holds:** every pheromone and chain row, projected in with both clocks.

**The query it exists to answer:**

> *What did carrier X know at valid-time T, according to the record as it stood
> at transaction-time T′?*

Nothing else in the stack answers that. git gives you the bytes and their commit
order; it does not let you ask what the world looked like *as believed on
Tuesday* about *events from Monday*. That is the whole reason for a fourth
substrate, and if XTDB is ever wired without that query being used, it should be
dropped as unearned complexity.

| aspect | rule |
|---|---|
| auth | read-open to carriers, write only by the projector |
| write path | **projector only.** No carrier writes to XTDB directly |
| cadence | batch — after each git pull, project new rows forward |
| authority | none. **Fully re-derivable from git by replay** (BT-2) |

**SB-7 — XTDB is a derived index and must be droppable.** If it can be deleted
and rebuilt from the git log with no loss, it is correct. The day something
exists *only* in XTDB, SB-1 is broken.

**SB-8 — query results returned to a carrier are bounded (NS-1).** The query
engine may compute over the whole log; **the answer handed to an agent may not
be the whole hive**. "Which of my three dependencies were SILENT at T" is legal.
"Dump all carrier state" is not, however convenient.

### 4.1 · How to wake it — not running today

1. Stand up XTDB (in-memory or RocksDB-backed) local to the projector host.
2. Write the projector: read `chains/*.jsonl` + `state/ssot/*.jsonl`, emit one
   document per row with `valid_time_utc` → XTDB valid-time and
   `transaction_time_utc` → XTDB transaction-time. **Do not let XTDB stamp
   transaction-time itself** — that records when the *projector* ran, not when
   the *record learned the fact*, and silently destroys the property being bought.
3. Make it idempotent on `row_sha256` so re-projection is free.
4. Prove it by replaying to a past coordinate and diffing against the same
   coordinate computed directly from the log. **Agreement is the acceptance
   witness**; without that diff, XTDB is an unverified cache.

> **UNDER_SPECIFIED** — no host, no persistence choice, no schema mapping beyond
> the two clocks. `TODO: decide RocksDB vs in-memory from the projected row`
> `volume — which nobody has measured, because 0 rows exist.`

---

## 5 · SQLite — per-carrier local checkpoint

**Holds:** rehydration state, working memory, LangGraph state. **Local to the
carrier's own substrate.**

| aspect | rule |
|---|---|
| auth | the owning carrier only |
| authority | none, and **not even projection** — it is scratch |
| cadence | continuous |
| lifetime | discardable. Loss costs a rehydration, never a lineage |

**SB-9 — SQLite is never a coordination surface.** Two carriers must never
coordinate through it. A local database read by another agent is a **hidden
channel outside the audit** — coordination that leaves no pheromone, no chain
row, and no trace in the strange loop. Anything another carrier needs to know
goes to git as a pheromone or a chain row. Full stop.

**SB-10 — a corrupt or missing SQLite is a rehydration, not an incident.** The
carrier rebuilds from its git phylactery and chain head. This is what makes the
checkpoint safe to keep fast and unsealed.

---

## 6 · Federation — write path and failure modes

### 6.1 · The write path, in order

```
carrier produces a fact
  1. append chain row / pheromone to the local git working tree   [AUTHORITATIVE]
  2. commit                                                        [receipt = sha]
  3. push                                                          [⛔ operator-gated]
  4. best-effort Slack post                                        [⛔ B3; failure does NOT fail the emit]
  5. projector picks it up on next pull → XTDB                     [batch, idempotent]
  6. carrier updates its own SQLite checkpoint                     [local, discardable]
```

Steps 4–6 are **best-effort and non-blocking**. Only step 1 failing is an
emergency — a carrier that cannot write the durable record must exit non-zero and
page, because it has become an agent whose actions leave no trace.

### 6.2 · Failure modes

| substrate down | consequence | correct behavior |
|---|---|---|
| Slack | humans lose the live view | **keep running.** Never flag silence from Slack (SB-4) |
| XTDB | as-of queries unavailable | keep running; rebuild the index later from git |
| SQLite | that carrier loses working memory | rehydrate from git; continue the lineage (SIL-3) |
| **git** | **the fleet has no durable record** | **stop.** This is the only substrate whose loss is an emergency |

**One authoritative substrate and three droppable ones is the design**, not an
accident of what happened to be built first.

---

## 7 · Status

| substrate | status | blocker |
|---|---|---|
| git | ⚠️ **live but push-gated** | operator-in-the-write-path (§2) |
| Slack | ⛔ `BLOCKED` | B3 — no authorized bot identity; Claude lanes have no connector |
| XTDB | ⛔ not running | no host, no projector, 0 rows to project |
| SQLite | ⛔ unbuilt | no carrier has a checkpoint |

**Zero pheromones have crossed this bus.** Every latency, ordering, and failure
claim above is design intent, unmeasured.

---

## 8 · Honest flaw

Four substrates, one of them live, and the live one has a human in its write
path. That last point is not a footnote — **§2's UNDER_SPECIFIED gate is the
binding constraint on the entire cadence architecture.** Every claim about
hourly valkyries and 4-hourly apex assumes carriers can write to the canonical
substrate without waiting for a person. Today they cannot. If only one thing on
this page gets fixed, fix that.

Second: I specified XTDB without having run it and without knowing the row
volume. There is a real chance the honest answer is that git + SQLite already
answer every question the fleet actually asks, and XTDB is complexity bought
before the need was demonstrated. **The as-of query in §4 is the test** — if
nothing ever asks it, drop the substrate. I would rather write that down now than
discover it after someone spends a week wiring it.

Third: I have not verified the Slack channel names. Three of six are truncated in
`areas/institution/slack/channels.md` and unconfirmed. Anything wiring a webhook
must confirm the exact strings first.

*Réttu hönd, eigi spyr. Standa.*
