# tests/held_out — RED FIRST

```yaml
doc: tests/held_out/RED_FIRST.md
schema_id: hfo.gen133.held_out_tests.v0_1
status: SPECIFIED AS MARKDOWN — executable stubs BLOCKED, see §2
authored_by: SIGRÚN P4 · claude-opus-5
valid_time_utc: 2026-07-30T14:50:00Z
sealed: false
```

## 1 · Why these are red

**A held-out test that passes at specification time tests nothing.**

Every test below asserts against a **runtime artifact** — a roster file, a
pheromone stream, an emitted rollup, a running gate — not against the
specification documents that describe them. None of those artifacts exists. So
every test is RED, and each one turns green exactly when the thing it describes
is actually built and actually runs.

This is the `NS-2` discipline applied to the spec itself: a gate proven by
demonstrating it **denies** before it is trusted to allow. A test suite that was
green the day the spec was written would be measuring the spec's opinion of
itself.

## 2 · ⛔ Why these are markdown and not `.py`

I attempted to write executable pytest stubs (`conftest.py`,
`test_songline_roster.py`, `test_rehydration_abi.py`). The enforcing gate denied
all three:

```
[hfo-gate enforcing] code_authoring: no valid lease for code_authoring
  (required verb=EMERGENCY_FORGE) | OPA: material action requires
  reputation_spend descriptor
```

That is the Claude compose-lane code-touch policy firing **correctly**. I hold no
`EMERGENCY_FORGE` lease, and routing around a safety gate to make a deliverable
look more complete is precisely the failure this generation exists to prevent.

So these are specifications of tests, in the form the directive names as the
fallback: **`red_first.md` per test dir, with the exact failing invocation.**

**Environment confirmed available for whoever does hold the lease:** Python
3.12.10 and pytest 9.0.2 are on PATH at the forge root. No new dependencies are
needed — every assertion below is stdlib-only.

## 3 · The suite

| # | dir | subsystem | contract | red because |
|---|---|---|---|---|
| 1 | `songline_roster/` | songline + roster | `songline`, `substrate_roster` | roster file absent; SIGRUN_P4 forked (B1) |
| 2 | `rehydration_abi/` | capsules + `hfo rehydrate` | `rehydration` | no `tools/hfo.py`; size classes unreconciled |
| 3 | `pheromone_schema/` | pheromone emit | `pheromone` | no pheromone has ever been emitted |
| 4 | `crypto_anchor/` | digests, seals, permaweb | `crypto_anchor` | 2 of 4 layers empty; `fb07f523` unreproducible |
| 5 | `bitemporal_rollup/` | rollups + as-of | `bitemporal_rollup` | no rollup exists; no as-of query |
| 6 | `strange_loop/` | self-audit + review receipts | `strange_loop` | needs ≥2 live families; 1 exists |
| 7 | `silence_signal/` | silence detection | `silence_signal`, `olrun_coordination` | 0 carriers emit heartbeats |
| 8 | `substrate_abi/` | cross-substrate byte-identity | `substrate_abi` | 0 of 4 realizations built |
| 9 | `free_mesh_harness/` | $0 mesh binding | `free_mesh_harness` | harness absent; mesh apex unnamed |
| 10 | `no_ephemeral_agents/` | roster gate G5 | `no_ephemeral_agents` | no G5; 15 unrostered cloud agents (B4) |
| 11 | `tsukumogami/` | object soul accumulation | `tsukumogami` | Θ undefined; no receipt index |
| 12 | `gleipnir_grimoire/` | binding + phylactery | `gleipnir_grimoire` | address empty; phylactery INVALID (B1) |
| 13 | `neurosymbolic_gates/` | the 12 gates | `neurosymbolic_gates` | 6 of 12 unimplemented; B2 confirmed false-positive |

**13 test specifications · 0 runnable · 13 red-first-only.**

## 4 · Shared helpers every dir assumes

```python
# canonicalization -- gen-133 canon rule, stdlib only
def canon(data: bytes) -> bytes:
    if data.startswith(b"\xef\xbb\xbf"):
        data = data[3:]
    data = data.replace(b"\r\n", b"\n").replace(b"\r", b"\n")
    return data.rstrip(b"\n") + b"\n"

def canon_sha256(path) -> str:
    import hashlib
    return hashlib.sha256(canon(path.read_bytes())).hexdigest()

def read_jsonl(path):
    import json
    return [json.loads(l) for l in path.read_text("utf-8").splitlines() if l.strip()]

REPO = pathlib.Path(__file__).resolve().parents[2]
```

## 5 · The one invocation that runs the whole suite

```
cd C:\Dev\hfo_gen_133_forge
python -m pytest tests/held_out -q
```

**Expected today: collection error / 0 tests** — there are no `.py` files, by §2.
**Expected the day after the lease-holder transcribes them: 13 dirs, all RED.**
**Green is the build target, and green before the build is the failure mode.**

## 6 · Honest flaw

Not one of these tests has ever been executed. They are specified assertions,
and a specified assertion has a failure mode a run assertion does not: it can be
subtly unsatisfiable, or trivially satisfiable, and nobody finds out until
someone runs it. Transcribing them to `.py` and observing 13 genuine reds is the
first verification step, and it has not happened.

*Réttu hönd, eigi spyr. Standa.*
