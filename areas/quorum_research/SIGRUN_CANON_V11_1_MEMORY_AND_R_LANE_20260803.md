```yaml
# AIH2O capsule
doc: areas/quorum_research/SIGRUN_CANON_V11_1_MEMORY_AND_R_LANE_20260803.md
schema_id: hfo.gen133.sigrun_canon_v11_1_memory_r_lane.v0_1
callsign: SIGRÚN
generation: 133
authored_by: SIGRÚN · claude-opus-5 · Claude Code
now_utc: 2026-08-02T22:05:19Z
clock_source: host_read
amends: V11 (row 128) — adds durable-memory layer + R-lane scanner spec
claim_status: partial
```

# V11.1 — durable memory and the R lane

## §0 · Two of your three asks already shipped

⭐ **Item 1 (six lanes) landed in V11, chain row 128** — R/P/D/S/C/H with agent
pools, weekly $ targets, kill criteria, and an operator-hours budget (S 3.0 ·
D 1.0 · C 0.5 · P 0.5 · R 0 · H 0). ⭐ **Item 3's Framework correction was me,
this turn** — I patched `FRAMEWORK` in place and a probe now greps it, so a revert
fails the capability. **I won't re-ship either.**

**What's genuinely new here: the memory layer, and the R-lane spec.**

---

## §1 · Slack — the honest gate

⛔ ⭐ **I probed before speccing, and Slack cannot send.**

```
.env  →  SLACK_WEBHOOK_URL={{FROM_SIGRUN_SECRETS}}
```

**That is a literal placeholder template string, not a webhook.** It does not match
`hooks.slack.com/services/T…/B…/…`. `tools/slack_post.py` exists and is
functional stdlib code — **it just has no credential to use.**
`state/ssot/slack_bridge.jsonl` is **0 bytes**.

> ⭐ **If I specced "Slack broadcast per lane" without leading with this, I would
> be building the exact Potemkin loop this session has spent twelve canons
> diagnosing.** The routing design below is real and ready. **It broadcasts
> nothing until one line in `.env` is replaced.**

**Routing, once unblocked:**

| lane | channel | what goes | cadence |
|---|---|---|---|
| **S** services | `#hfo-cash` | every reply, every booking, every dollar | ⭐ immediate |
| **D** distribution | `#hfo-distribution` | send batches, stop-gate trips | daily digest |
| **P** product | `#hfo-ships` | one line per shipped unit + its live URL | on ship |
| **R** research | `#hfo-research` | ⭐ **prior updates only**, never raw articles | daily digest |
| **C** content | `#hfo-content` | drafts awaiting your voice | on draft |
| **H** hive | `#hfo-synthesis` | ADRs, census leaks, andons | on event |

⭐ **Anchor message pinned in `#hfo-synthesis`:** studio identity, the three bright
lines, the 1-unit/week cap, the 2026-08-16 falsifier, and a pointer to the session
index. **One message, pinned, so a cold rehydrate reads the floor before it reads
opinions.**

⛔ **Sending remains ENV-C.** Even once credentialed, I stage; you sign the class
once and then the digests flow.

---

## §2 · ADR discipline — backfilled, not just specced

`canon/adr/` existed with **exactly one ADR**. ⭐ **I backfilled this session's
material decisions as ADR rows rather than leaving them buried in twelve canons** —
because "logged to Slack" is worthless if the decisions themselves live only in
prose nobody re-reads.

**The rule, going forward:** *a decision is material if reversing it would change
what the operator does next week.* Material decision → ADR row, same turn, with
`status`, `authority` (chain row), and `supersedes`. ⛔ **No ADR = the decision
does not exist** — the same rule the capability registry applies to claims.

**Backfilled:** studio identity · two-lane cut · 1-unit/week throttle ·
talent-networks-first · MIT-only forks · HVAC demotion · booking-door bright line.

---

## §3 · Session index for rehydration

⭐ **The real problem this solves:** a fresh Sigrún reading 12 canons in sequence
will re-derive a stale position, because **V9 contradicts V11 and V8 contradicts
V10.** The index states the *current* floor and marks everything else historical.

`state/olrun/SESSION_INDEX_20260803.md` — read-order for the next wake:
**(1)** operator anchors, **(2)** the lock-in contract + six-lane JSON,
**(3)** the ADR index, **(4)** the latest canon only. ⛔ **Older canons are
history, not instruction.**

---

## §4 · R lane, assuming the scanner runs

**Sources** (daily 06:00 cron): TLDR · Ben's Bites · Import AI · The Rundown ·
AlphaSignal · Latent Space · ByteByteGo · Martin Fowler · Simon Willison ·
ghuntley · humanlayer · moekhalil · calv.info · spronta.com · HN front+new ·
r/LocalLLaMA · r/mcp · r/AIAgents · r/vibecoding.

⭐ **The one rule that keeps R from becoming a fifth production loop:**

> **R emits `prior_delta` records, never build orders.** Each item must name the
> cell, probability, or lane assumption it moves — and by how much. **An item that
> cannot name what it changes is dropped, not filed.**

**Kill criteria (from V11):** `target_queue_empty` twice → pause.
⭐ **Plus a ratio gate: if fewer than 5% of scanned items produce a non-null
`prior_delta` over 7 days, the scanner halts itself.** Sources that produce
nothing get dropped individually after 14 days.

⭐ **R consumes zero operator hours. If it ever asks for your time, it has
failed.** Its entire output surface is a daily digest line in `#hfo-research`
and updated numbers in the lane JSON.

---

## §5 · Honest flaws

1. ⭐ **The Slack push you asked for is blocked on one line of `.env`, and I found
   that only because I probed before writing.** Had I trusted the earlier
   "webhook confirmed present" note, I would have specced a broadcast layer that
   silently sends nothing — **which is precisely how the 12 phantom Suika receipts
   happened.**
2. **I backfilled ADRs from my own canons.** ⚠️ **That means the ADR record
   inherits my errors** — including positions I later retracted. Each backfilled
   row carries its superseding row where one exists, but **I am the only auditor
   of my own history here.**
3. **The session index is a document, and documents are what this session has
   been over-producing.** ⭐ **Its only defence is that it is *subtractive*** — it
   tells the next wake what to *ignore*. If it grows past one screen it has failed.
4. **The article scanner is specced, not built**, and I did not verify a cron
   exists. ⚠️ **Treat R as inactive until a `prior_delta` record appears.**
5. ⛔ **None of this moves a dollar.** Memory, ADRs and R are all H-lane and
   R-lane work — **zero operator hours by design, and zero revenue by
   construction.** ⭐ **The booking door is still dead, and it remains the only
   twenty-minute task on this board that unblocks money.**

*Réttu hönd, eigi spyr. Standa.*
