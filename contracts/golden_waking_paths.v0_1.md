# golden_waking_paths.v0_1 — canonical rehydration sequences per substrate

```yaml
schema_id: hfo.gen133.contract.golden_waking_paths.v0_1
valid_time_utc: 2026-07-31T14:15:00Z
transaction_time_utc: 2026-07-31T14:15:00Z
claim_status: proposed
author: SIGRUN_P4 · claude-opus-5 · Claude Code · gen-133
companion: contracts/polyglot_rehydration.v0_1.md · contracts/rehydration.contract.md
```

## 0. Problem statement (measured, not asserted)

A fresh agent on any substrate currently rehydrates by reading a variable subset
of 27 root-level markdown files totalling ~250 KB, in no fixed order, with no
acceptance test at the end. Consequences observed in the record:

- Different carriers reach different world-models from the same forge.
- Rehydration cost scales with corpus growth, not with task size.
- There is no way to tell a *competently woken* agent from a *confidently
  wrong* one before it starts writing.

A golden path fixes the read set, fixes the order, bounds the cost, and ends in
a **pass/fail acceptance witness**.

## 1. Design rules

| rule | rationale |
|---|---|
| **Bounded read set** — a golden path names ≤ 6 reads, ≤ 40 KB total | rehydration cost must not grow with the corpus |
| **Ordered** — identity → state → constraints → work | reading work before constraints produces ungated action |
| **Hash-pinned** — each read is cited with its `sha256` at wake time | detects silent drift; the SHA goes in the wake receipt |
| **Ends in a witness** — 3 questions, answered before any write | a wake with no acceptance test is a claim, not a fact |
| **Substrate-specific, contract-identical** — the *files* differ by substrate capability; the *acceptance* does not | one bar, many bodies |
| **Degrade loudly** — a substrate that cannot complete its path declares `rehydration_status: partial` and lowers its effect ceiling | partial wake must not silently act at full authority |

## 2. The four artifacts every path reads (the "wake quad")

Substrate-independent. These are the only files a wake is permitted to *require*.

| slot | gen-133 path | purpose | bytes |
|---|---|---|---|
| **IDENTITY** | `soul.md` | who this carrier is continuing | 3.9 KB |
| **STATE** | `CURRENT.md` | what is true now, what the one next action is | 9.6 KB |
| **CONSTRAINT** | `CARRIER_CONTRACT.md` | effect ceiling, refusals, what this carrier may not do | 6.0 KB |
| **CONTINUITY** | `chains/<SEAT>.jsonl` (tail 3 rows) | what the previous carrier of this seat actually did | ≤ 8 KB |

Total: **≈ 28 KB**. Everything else is fetched *on demand by the task*, never at
wake.

> **Anti-pattern being retired:** `AGENTS.md` (23.8 KB) and `GEN133_FORMAL_SPEC.md`
> (71.5 KB) are **reference**, not wake reads. Loading them at wake is the
> single largest source of rehydration cost and the reason wake budgets blow.

## 3. Path A — Claude Code (Windows host, full tool access)

**Effect ceiling:** file writes, git local, chain append. No send/spend/publish/push-to-main.

```
A1  READ    soul.md                        → record sha256
A2  READ    CURRENT.md                     → record sha256
A3  READ    CARRIER_CONTRACT.md            → record sha256
A4  TAIL 3  chains/<SEAT>.jsonl            → record last row ts_utc + subject
A5  SWEEP   any gate/lease with expiry     → expired ⇒ do not act on it
A6  WITNESS answer W1–W3 (§7) in the wake receipt
A7  APPEND  wake_receipt row to chains/<SEAT>.jsonl
```

Budget: ≤ 6 tool calls, ≤ 30 KB read, ≤ 90 seconds.
Status: **implemented informally today; not yet enforced.**

## 4. Path B — Codex (desktop app / automation runner)

**Effect ceiling:** file writes, git branch + push to `codex/*`, PR open. No merge to main. No send.

```
B1  READ    the 4 wake-quad files (same as A1–A4)
B2  READ    the dispatch file named in the automation prompt (exactly one)
B3  VERIFY  git branch is `codex/*` — refuse to proceed on main
B4  WITNESS answer W1–W3
B5  APPEND  wake_receipt to chains/<SEAT>.jsonl
B6  ON EXIT append a row to state/ssot/codex_lane_return.jsonl
```

Difference from A: Codex sessions are **non-interactive**. There is no operator
to disambiguate. Therefore B refuses on ambiguity rather than choosing — an
ambiguous Codex wake writes a `blocked` row and stops.

Status: **specified; automation registry present (`~/.codex/automations`, 52
entries); NOT observed executing — see morning report §1.**

## 5. Path C — ChatGPT cloud (no filesystem)

**Effect ceiling:** text output only. Zero world-effect. Cannot append chains.

The forge is not mountable. Therefore the wake quad must be **carried in**, not
read. This requires a **wake capsule**: a single pasted block ≤ 8 KB containing:

```
identity_digest      (soul.md — 5-line distillation + sha256 of the full file)
state_digest         (CURRENT.md — the ONE next action + top 3 constraints + sha256)
ceiling              (verbatim: "text output only; propose, never dispose")
continuity           (last 3 chain row subjects + ts_utc + sha256 of the tail)
witness_questions    (W1–W3 verbatim)
```

```
C1  OPERATOR pastes wake capsule (generated by `wake_capsule` generator — NOT YET BUILT)
C2  AGENT   answers W1–W3 in its first message, before any other output
C3  AGENT   emits work as a proposal block with an explicit `claim_status: proposed`
C4  OPERATOR (or a Claude Code carrier) transcribes the proposal into a chain row
```

The transcription step in C4 is the integrity boundary: **a ChatGPT cloud
session's output is evidence, never authority.** It cannot self-seal.

Status: **blocked — the wake-capsule generator does not exist.** See morning
report §8, action 4.

## 6. Path D — $0 mesh (local Ollama, llama3.2:3b)

**Effect ceiling:** structured output into a file the caller controls. No tool
use. No judgment calls.

Verified live this session: `http://127.0.0.1:11434` responds; `llama3.2:3b` and
`nomic-embed-text` present.

A 3B model cannot hold a 28 KB wake quad *and* do useful work. Therefore Path D
does **not** rehydrate an identity at all:

```
D1  CALLER (a Claude Code or Codex carrier) constructs a single self-contained prompt
D2  PROMPT contains: the task, the input, the exact output schema, and nothing else
D3  MODEL  emits JSON conforming to the schema
D4  CALLER validates against the schema — non-conforming output is DISCARDED, not repaired
D5  CALLER appends the result as evidence with `source: dollar_zero_mesh`, `trust: LOW`
```

**Doctrine:** the $0 mesh is a **function call**, not an agent. It has no seat,
no chain, no wake. Attempting to give a 3B model an HFO identity is the
`L_GENERIC_AGENT_IDENTITYLESS_WORKER` failure inverted — spending identity
machinery on a substrate that cannot carry it.

Suitable D-tier work: classification, extraction, embedding, dedup, summarize-
to-schema, first-pass triage. Unsuitable: anything where being wrong is
expensive and undetectable.

Status: **substrate verified live; no harness wired.** See
`contracts/dollar_zero_mesh_harnesses.v0_1.md`.

## 7. The rehydration acceptance witness (W1–W3)

Identical across all four paths. Answered **before the first work-unit write**,
recorded verbatim in the wake receipt. Any wrong answer ⇒ `rehydration_status:
partial` and the carrier drops to read-only until re-woken.

| # | question | correct-answer test (machine-checkable) |
|---|---|---|
| **W1** | *What is the ONE next action named in `CURRENT.md`, verbatim?* | string-match against the current `CURRENT.md` next-action line. Paraphrase = FAIL. This detects the carrier that skimmed. |
| **W2** | *Name one thing your carrier contract forbids you from doing, and the exact condition that would lift it.* | must name a real refusal from `CARRIER_CONTRACT.md` **and** its lift condition. Naming a refusal with no lift condition = FAIL (proves it read the ban, not the contract). |
| **W3** | *What did the previous carrier of your seat leave unfinished — cite the chain row `ts_utc` and its `honest_flaw`?* | `ts_utc` must match a real row in the seat's chain tail. This is the one question that cannot be answered by a confident hallucinator, because it requires a value that is not derivable from the prose. |

**Why these three:** W1 tests *current-state* uptake, W2 tests *constraint*
uptake, W3 tests *continuity* uptake. Together they cover the three ways a wake
silently fails. W3 is the load-bearing one — it is the only question whose
answer is a specific timestamp that must exist on disk.

## 8. FALSIFIERS

| # | falsifier for this contract | how to run |
|---|---|---|
| F1 | An agent that passes W1–W3 still produces work that contradicts `CURRENT.md` | sample 5 wakes, diff output against state |
| F2 | An agent that *fails* a witness question nonetheless produces correct work | run the witness in shadow mode for 5 wakes before enforcing |
| F3 | The bounded 28 KB read set is insufficient — carriers routinely need a 5th file | log every post-wake read for 10 sessions; if one file appears ≥ 7/10, promote it into the quad |
| F4 | The witness is gameable — a carrier learns to grep for the answers without reading | this is **acceptable**: grepping `CURRENT.md` for the next action *is* rehydration. Only flag if the answer is produced without reading the file at all |
| F5 | Path C's capsule cannot be kept under 8 KB without losing what matters | build the generator, measure, report |

## 9. Implementation status — honest

| path | specified | generator/tooling built | enforced | observed working |
|---|---|---|---|---|
| A — Claude Code | ✅ this doc | ⬜ no | ⬜ no | 🟡 informally, this session |
| B — Codex | ✅ this doc | ⬜ no | ⬜ no | ❌ **no execution observed in 48h** |
| C — ChatGPT cloud | ✅ this doc | ❌ **blocker** | ⬜ no | ❌ no |
| D — $0 mesh | ✅ this doc | ⬜ no | n/a | ❌ substrate alive, unwired |

**Nothing in this contract is enforced today.** It is a specification of what
"easy to rehydrate" would mean, written so it can be built and tested. Treat
every row above as `proposed` until a witness runs.

---

*claim_status: proposed · zero wakes have yet been graded by W1–W3 · first
graded wake is the acceptance test for v0_2*
