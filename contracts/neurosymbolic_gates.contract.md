# CONTRACT — neurosymbolic gates

```yaml
contract: neurosymbolic_gates
schema_id: hfo.gen133.contract.neurosymbolic_gates.v0_1
spec: GEN133_FORMAL_SPEC.md §3
test: tests/held_out/test_neurosymbolic_gates.py
status: SPECIFIED — 6 of 12 gates have NO implementation anywhere
sealed: false
```

## The principle

**Neural proposes. Symbolic disposes.** No neural component both decides and
effects.

Root cause (RBR doctrine): the reflex fires before the deliberate pass can gate
it, and because generation is autoregressive the reflexive token then corrupts
the reasoning that would have caught it. You cannot delete the reflex — it *is*
the substrate. You **neutralize its authority and catch its errors
architecturally**: reason-first ordering, propose/dispose split, an external
symbolic gate at irreversibility, reversibility by default, and separate
adversarial verification.

**L8: a gate implemented by the substrate it gates shares the blind spot.** Every
gate below must be deterministic, non-neural, and external to the carrier.

## The twelve gates

| # | gate | fires at | verdict on failure | implementation |
|---|---|---|---|---|
| G1 | no-fake-green write seam | chain-row write | `exit 2` | gen-130 `bb_append.py` — **not ported** |
| G2 | prev-link contiguity | chain append | reject + `andon` | gen-130 `append_chain_note.py` — **not ported** |
| G3 | single-writer lock | chain open | reject second writer | **ABSENT everywhere** ⛔ |
| G4 | effect-ceiling allowlist | every tool call | deny | gen-130 `pretooluse_gate.py` — ⛔ **B2** |
| G5 | roster membership | spawn / first emit | `exit 1` | **none** |
| G6 | pheromone schema | emit | reject | **none** |
| G7 | cadence / silence | hourly world tick | flag per SLO | **none** |
| G8 | capsule integrity | rehydration inject | fail-closed | partial: `verify_capsules.py` |
| G9 | canon-hash | soul / capsule read | reject | **none** (manual only) |
| G10 | budget ($0 mesh) | mesh dispatch | deny | gen-130 cost-tier router — **not ported** |
| G11 | reason-first presence | before irreversible call | deny | gen-130 `pretooluse_gate.py` — ⛔ **B2** |
| G12 | cross-provider verify | identity / canon claims | deny same-family attestation | **none** |

## Preconditions — for every gate

| # | precondition |
|---|---|
| P1 | the gate is **deterministic** — same input, same verdict, always |
| P2 | the gate is **non-neural** — no model call in the decision path |
| P3 | the gate is **external** to the carrier it gates |
| P4 | the gate **fails closed** — an error in the gate denies, never allows |
| P5 | the gate's own artifact is **git-tracked** — runtime green with untracked enforcement is ANDON |

P5 is inherited from gen-130 ADR g130-0110 and is not pedantry: an untracked gate
is a gate that vanishes on the next clone, which means the enforcement claim was
true only on one machine.

## Postconditions

| # | postcondition |
|---|---|
| Q1 | a verdict is recorded with the input that produced it |
| Q2 | a deny is observable — it emits, it does not merely return |
| Q3 | no partial effect occurred before the deny |

## Invariants

| # | invariant |
|---|---|
| NS-1 | **static PASS ≠ runtime PASS.** Run the thing, record the actual exit code. |
| NS-2 | **red-first.** A gate is proven by demonstrating it **denies** a known-bad input before it is trusted to allow a good one. A gate only ever observed allowing has not been tested. |
| NS-3 | **delta gate, not absolute.** A known-red tree must not block all work: compare the FAIL set to the recorded baseline. Same FAILs ⇒ PROCEED. A **new** FAIL ⇒ halt + ANDON. |
| NS-4 | **a false positive is a real defect.** A gate that denies honest work trains carriers to route around it, which destroys every gate's authority — not just that one. See B2. |
| NS-5 | **no vesting.** The irreversible set never shrinks. Autonomy grows inside the reversible envelope, never by expanding it. |

## ⛔ B2 — a live NS-4 violation, reproduced this session

`pretooluse_gate.py:390` `DELETE_MARKERS` contains the bare string `"rm "`,
matching any text containing r-m-space — "confirm exit", "perform", "warm",
"inform". On match the gate demands a `reason_first_scratchpad` inside a
`tool_input` field the Bash tool has no slot for ⇒ **unsatisfiable**.

**Controlled A/B run in this spec session (2026-07-30):**

| run | command | message text | result |
|---|---|---|---|
| 1 | `git commit -q -m "<msg>"` | contained the literal token `rm ` (in the phrase "pretooluse rm marker") | **DENIED** — "delete: reflex-before-reason: missing reason-first scratchpad" |
| 2 | `git commit -q -F <file>` | identical content, token removed, message moved out of the command string | **ALLOWED** — commit `fed444c` |

`verifier_result`: two runs, same repository, same operation, differing only in
whether the command string contained `rm `. This **confirms the false positive**
and confirms it is triggered by the command string, not by the operation.

`remaining_risk`: the second half of the original hypothesis — whether a genuine
`rm -rf` phrased another way still passes — remains **UNVERIFIED**. I did not
test it and will not: probing a delete gate by attempting a delete is exactly the
wrong experiment to run unsupervised.

**Status: `BLOCKED`. Not fixed by this lane** — editing an enforcement gate is
code authorship on the safety path and needs `EMERGENCY_FORGE`.

## Honest flaw

**Six of twelve gates have no implementation anywhere**, four more exist only at
gen-130 and are unported, and one of the two most important (G3, single-writer)
is *known absent* — which is why a sibling lane wrote to this repository
mid-session on 2026-07-30 with nothing stopping it. This table is a design. A
design is not protection, and I will not describe it as protection.
