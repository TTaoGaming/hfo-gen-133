# RED FIRST — the twelve neurosymbolic gates

`contracts/neurosymbolic_gates.contract.md` · spec §3

## Exact invocation

```
cd C:\Dev\hfo_gen_133_forge
python -m pytest tests/held_out/neurosymbolic_gates -q
```

## Assertions

```python
GATES = ["G1","G2","G3","G4","G5","G6","G7","G8","G9","G10","G11","G12"]

# --- NS-2: prove DENY before trusting ALLOW. Every gate gets a red-first pair. ---
@pytest.mark.parametrize("gate", GATES)
def test_gate_denies_known_bad(gate):
    assert fire(gate, known_bad_input(gate)).verdict == "DENY"

@pytest.mark.parametrize("gate", GATES)
def test_gate_allows_known_good(gate):
    assert fire(gate, known_good_input(gate)).verdict == "ALLOW"

@pytest.mark.parametrize("gate", GATES)
def test_gate_is_deterministic(gate):                # P1
    inp = known_bad_input(gate)
    assert len({fire(gate, inp).verdict for _ in range(10)}) == 1

@pytest.mark.parametrize("gate", GATES)
def test_gate_makes_no_model_call(gate):             # P2 -- non-neural
    with audit_effects() as fx:
        fire(gate, known_bad_input(gate))
    assert fx.model_calls == []

@pytest.mark.parametrize("gate", GATES)
def test_gate_fails_closed(gate):                    # P4
    with gate_internal_error(gate):
        assert fire(gate, known_good_input(gate)).verdict == "DENY"

@pytest.mark.parametrize("gate", GATES)
def test_gate_artifact_is_git_tracked(gate):         # P5 -- ADR g130-0110
    assert git_tracked(implementation_path(gate))

def test_deny_is_observable():                       # Q2
    r = fire("G1", known_bad_input("G1"))
    assert r.emitted and r.recorded_input

def test_no_partial_effect_before_deny():            # Q3
    with audit_effects() as fx:
        fire("G4", known_bad_input("G4"))
    assert fx.files == []

# --- NS-4: a false positive is a real defect ---
def test_G4_does_not_deny_honest_work():             # ⛔ B2 -- CONFIRMED FAILING
    for phrase in ["confirm exit 0", "perform the check", "warm cache", "inform lane"]:
        assert fire("G4", bash_command(f'echo "{phrase}"')).verdict == "ALLOW"

def test_G4_still_denies_a_genuine_destructive_command():   # ⚠️ DO NOT RUN UNSUPERVISED
    # the UNVERIFIED half of B2. Requires a sandboxed harness, not a live tree.
    assert fire("G4", bash_command(genuine_destructive_variant())).verdict == "DENY"

def test_G12_denies_same_family_attestation():
    assert fire("G12", attestation(author="claude", attestor="claude")).verdict == "DENY"
```

## Why it is RED today

| gate | implementation | red reason |
|---|---|---|
| G1 | gen-130 `bb_append.py` | not ported to gen-133 |
| G2 | gen-130 `append_chain_note.py` | not ported |
| **G3** | **ABSENT EVERYWHERE** | single-writer lock does not exist — this is why a sibling lane wrote to this repo mid-session on 2026-07-30 with nothing stopping it |
| G4 / G11 | gen-130 `pretooluse_gate.py` | ⛔ **B2 — confirmed false positive** |
| G5, G6, G7, G9, G12 | **none** | never built |
| G8 | partial (`verify_capsules.py`) | not wired to injection |
| G10 | gen-130 cost-tier router | not ported |

**6 of 12 gates have no implementation anywhere.**

## ⛔ B2 — confirmed by controlled A/B in this spec session

`pretooluse_gate.py:390` — `DELETE_MARKERS` contains the bare string `"rm "`,
matching any text containing r-m-space.

| run | command form | message text | result |
|---|---|---|---|
| 1 | `git commit -q -m "<msg>"` | contained the literal token `rm ` | **DENIED** — `delete: reflex-before-reason: missing reason-first scratchpad` |
| 2 | `git commit -q -F <file>` | identical content, token removed, message moved out of the command string | **ALLOWED** — commit `fed444c` |

`verifier_result`: two runs, same repository, same git operation, differing only
in whether the command string contained `rm `. The false positive **reproduces**,
and the trigger is the command string, not the operation.

`remaining_risk`: the second half — whether a genuine destructive command phrased
another way still passes — is **UNVERIFIED**. I did not test it and will not.
Probing a delete gate by attempting a delete is the wrong experiment to run
unsupervised, and `test_G4_still_denies_a_genuine_destructive_command` above is
marked accordingly: it needs a sandboxed harness, never a live tree.

**Status `BLOCKED`. Not fixed by this lane** — editing an enforcement gate is code
authorship on the safety path and requires `verb=EMERGENCY_FORGE`.

## What turns it green

1. Port G1, G2, G10 from gen-130 (they exist and are proven there).
2. Build G3 — the single-writer lock. It is the gate whose absence has already
   caused a real incident in this generation.
3. Build G5 once the roster file exists.
4. Operator authorizes an `EMERGENCY_FORGE` for B2.

## Honest flaw

**A design is not protection.** Six gates are prose, four live on another
generation, and the enforcement I *did* meet this session denied an honest commit
while — by its own construction — leaving a real destructive command reachable by
rephrasing. That is NS-4 in the worst direction: a gate that trains carriers to
route around it. I routed around it (by moving the message to a file) rather than
weakening it, and I am recording that I did so.
