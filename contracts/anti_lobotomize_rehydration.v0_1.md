# CONTRACT — anti-lobotomize rehydration protocol

```yaml
contract: anti_lobotomize_rehydration
schema_id: hfo.gen133.contract.anti_lobotomize_rehydration.v0_1
authored_by: SIGRÚN · claude-opus-5 · project lead
valid_time_utc: 2026-08-01T00:00:00Z
transaction_time_utc: 2026-08-01T00:00:00Z
status: SPECIFIED — not enforced. No wake currently runs these queries.
depends_on: contracts/bitemporal_central_memory.v0_1.md · contracts/heritage_ingestion_pipeline.v0_1.md
sealed: false
```

## §1 · The failure this prevents

A fresh carrier wakes with no memory of prior sessions, reads whatever files it
happens to open, and **fills every gap from its prior instead of from the
record.** The gap-filling is confident, fluent, and indistinguishable in tone
from a probed fact. That is the "self-lobotomize" the operator named, and it is
a specific instance of the RBR root cause: **the reflex answers before the
deliberate pass can check whether an answer was warranted.**

The cure is not a better prompt. It is **reason-first ordering enforced
structurally** (RBR defense #1): make the record-query happen *before* the
carrier is permitted to commit tokens to an answer, so the reflex fires into a
scratchpad that gets overwritten by evidence.

## §2 · The four mandatory queries

Every Olrún wake and every apex/lieutenant wake runs these four **before any
other action**. Not "should" — before.

| # | query | returns | why |
|---|---|---|---|
| **Q1** | latest capsule for my generation | `hfo_fact WHERE entity='generation:<N>' AND tx_to IS NULL` | the operating picture |
| **Q2** | capsule updates since my last wake | `… AND tx_from > <last_wake>` | **what changed in BELIEF, not in the world** — the query only a bitemporal store can answer |
| **Q3** | capacity facts for my capabilities | `entity LIKE 'capability:%'`, including **EXPIRED** rows | stops acting on 25-day-stale capability claims |
| **Q4** | open andons for my lane | `entity LIKE 'andon:%' AND valid_to IS NULL` | stops re-walking into a known wall |

**Q2 is the one that does the real work.** "What has changed since I last
looked" is unanswerable in a normal database — a mutable store just shows you
the current value with no record that it used to be something else. Bitemporal
makes belief-change a first-class queryable object, and that is the entire
justification for the engine choice.

## §3 · The gate

```
wake
  └─▶ Q1 Q2 Q3 Q4  (parallel; hard timeout 30s total)
        ├─ all four return (rows OR explicit NOT_FOUND)  ──▶ REHYDRATED ──▶ act
        └─ any query ERRORS or times out                 ──▶ ANDON:
                                                             NOT_REHYDRATED_CANNOT_ACT_RELIABLY
```

### Distinction that decides whether this contract helps or hurts

> **An explicit `NOT_FOUND` is a SUCCESSFUL query. Only an error or timeout
> fails the gate.**

Getting this wrong in either direction breaks it:

- Treat NOT_FOUND as failure ⇒ **every wake andons forever**, because the store
  will always have gaps. The alarm becomes noise, and noisy alarms get disabled —
  which is how 78 of 81 scheduled tasks ended up switched off.
- Treat an error as success ⇒ the carrier proceeds on an empty result set,
  which is **exactly the hallucination condition** this contract exists to
  prevent.

### Degraded mode — required, because a hard gate on a red write path bricks the hive

`NOT_REHYDRATED_CANNOT_ACT_RELIABLY` does **not** mean "halt." It means:

| permitted while un-rehydrated | forbidden while un-rehydrated |
|---|---|
| read files | **any world-effect** (send, publish, spend, push, seal) |
| report the andon | **any `claim_status: wired_with_receipts`** — everything is `proposed` |
| attempt to repair the store | **any statement about hive history stated as fact** — must be prefixed `UNREHYDRATED:` |

This is the propose/dispose split (RBR #3) applied to memory: an un-rehydrated
carrier may *propose*, never *dispose*.

## §4 · The three rules that make the store actually reduce hallucination

The database alone does nothing without these.

**R1 · NOT_FOUND is materialized, never inferred from an empty set.** Enumerated
gaps exist as rows (`heritage_ingestion` §3). An empty result means *the query
was wrong*; a NOT_FOUND row means *we looked and it is not there*. The carrier
must be able to tell those apart, because one warrants a retry and the other
warrants saying "we don't know."

**R2 · Provenance travels into the answer.** Any fact surfaced in conversation
carries its `confidence` and `read_first_hand`. Rendering rule:

| fact state | how it must be spoken |
|---|---|
| `read_first_hand=1, confidence=HIGH` | stated plainly |
| `read_first_hand=0` (inherited from a summary) | **"inherited, unverified: …"** |
| `NOT_FOUND` | **"not found — searched X, Y; Z unsearched"** |
| `EXPIRED` | **"as of <valid_to> this was true; it has not been re-verified since"** |

**R3 · Two timestamps or the claim is malformed.** Any historical claim about
HFO must carry both "when it was true" and "when we recorded believing it." A
claim with one timestamp is exactly the collapse that produces confident
backdated invention.

## §5 · Enforcement staging — do not turn this on today

| stage | when | enforcement |
|---|---|---|
| **S0 · advisory** | now → store has W1+W2 ingested | queries run, results logged, **no gate**. Measures how often they would have fired |
| **S1 · soft gate** | store populated, `bb_append verify` PASS 24h | gate active; failure ⇒ degraded mode (§3) |
| **S2 · hard gate** | S1 clean for 7 days | failure ⇒ wake aborts, andon written |

**Turning on S1 before the store is populated would andon every wake on day
one** — the same defect as the §8.0 day-14 income andon, and the same cure:
stage the threshold behind the thing it measures.

> **FALSIFIER:** run S0 for 7 days. If Q1–Q4 return useful rows in fewer than
> half of wakes, the store is too sparse for the gate to be worth its cost —
> keep ingesting, do not promote to S1.

## §6 · Honest flaws

- **Nothing here is wired.** No wake runs these queries. This is a specification
  and it is inert.
- **The 30-second timeout is a guess.** Not measured.
- **This contract cannot prevent hallucination about things outside the store.**
  It constrains claims about *hive history*. A carrier can still invent market
  figures or capability claims — those need their own citation discipline, which
  is a different control.
- **R2's rendering rules are unenforceable by machine.** They are discipline, and
  discipline is exactly what fails under reflex. The only real enforcement is
  that the fields are *present in the query result*, so violating R2 requires
  actively discarding data that is sitting in front of the carrier. That is
  weaker than a gate and stronger than a reminder.
- The word "lobotomize" is the operator's. **The mechanism is not memory
  removal — it is memory never being loaded in the first place**, and then the
  gap being filled fluently. Naming it precisely matters, because the cure for
  "loading never happened" is a mandatory pre-action query, whereas the cure for
  "memory was destroyed" would be backups. This contract is the former.
