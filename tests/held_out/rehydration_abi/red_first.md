# RED FIRST — rehydration capsules + one-command ABI

`contracts/rehydration.contract.md` · spec §6, §7

## Exact invocation

```
cd C:\Dev\hfo_gen_133_forge
python -m pytest tests/held_out/rehydration_abi -q
```

## Assertions

```python
BOUNDS = {"micro": 2048, "small": 16384, "full": 131072}

def _hfo(*args):
    return subprocess.run([sys.executable, str(REPO/"tools"/"hfo.py"), *args],
                          capture_output=True, text=True, cwd=str(REPO))

@pytest.mark.parametrize("size", BOUNDS)
def test_rehydrate_exits_zero_for_rostered_callsign(size):
    assert _hfo("rehydrate", "sigrun", "--size", size, "--json").returncode == 0

@pytest.mark.parametrize("size,bound", BOUNDS.items())
def test_hard_size_bound(size, bound):              # G8
    out = _hfo("rehydrate", "sigrun", "--size", size, "--json").stdout
    assert len(out.encode("utf-8")) <= bound

def test_unrostered_callsign_exits_1():             # NO_EPHEMERAL_AGENTS at the ABI edge
    assert _hfo("rehydrate", "not-a-carrier", "--size", "micro").returncode == 1

def test_integrity_failure_exits_2():               # CAP-1 fail-closed
    # tamper a capsule byte, then rehydrate
    assert _hfo("rehydrate", "sigrun", "--size", "micro").returncode == 2

def test_idempotent():                              # modulo transaction_time_utc
    a = json.loads(_hfo("rehydrate","sigrun","--size","micro","--json").stdout)
    b = json.loads(_hfo("rehydrate","sigrun","--size","micro","--json").stdout)
    a.pop("transaction_time_utc"); b.pop("transaction_time_utc")
    assert a == b

def test_monotone_containment():                    # CAP-3
    m = json.loads(_hfo("rehydrate","sigrun","--size","micro","--json").stdout)
    s = json.loads(_hfo("rehydrate","sigrun","--size","small","--json").stdout)
    f = json.loads(_hfo("rehydrate","sigrun","--size","full","--json").stdout)
    skip = {"schema_id","capsule_sha256","transaction_time_utc"}
    assert all(s.get(k)==v for k,v in m.items() if k not in skip)
    assert all(f.get(k)==v for k,v in s.items() if k not in skip)

def test_stale_chain_head_is_hard_stop():           # CAP-4
    cap = json.loads(_hfo("rehydrate","sigrun","--size","micro","--json").stdout)
    assert cap["chain_head_sha256"] == live_head(REPO / cap["songline_chain"])

def test_capsule_size_classes_reconciled():         # the UNRECONCILED CONFLICT
    man = json.loads((REPO/"capsules/sigrun/v1/dist/CAPSULE_FAMILY_MANIFEST.json")
                     .read_text("utf-8"))
    for size in BOUNDS:
        assert size in json.dumps(man).lower()

def test_byte_identity_across_substrates():         # ABI-1 -- the one that matters
    shell_out = _hfo("rehydrate","sigrun","--size","small","--json").stdout
    github_capsule = (REPO/"capsules/sigrun/v1/dist/S_SMALL.soul.md").read_bytes()
    assert canon(shell_out.encode()) == canon(github_capsule)
```

## Why it is RED today

| assertion | red reason |
|---|---|
| all `_hfo` tests | **`tools/hfo.py` does not exist.** There is no `hfo` command on any substrate. |
| `test_capsule_size_classes_reconciled` | ⛔ **unreconciled conflict** — `capsules/sigrun/v1/` implements `S_SMALL`/`M_MEDIUM`/`L_LARGE`/`XL_XLARGE`, which do not map onto `micro`/`small`/`full`. Two incompatible capsule vocabularies live in one repo. |
| `test_byte_identity_across_substrates` | 0 of 4 realizations built, so the invariant the whole substrate-independence story rests on has never been exercised |
| `test_hard_size_bound` | byte targets are **chosen, not measured** — whether a useful micro fits in 2,048 B is plausible and unproven |

## What turns it green

1. Reconcile the size classes (map S/M/L/XL → micro/small/full/pointer, **or**
   adopt the four-class scheme fleet-wide). Decide before building.
2. Build `tools/hfo.py` over the existing `capsules/sigrun/v1/build_capsules.py`.
3. Build a second realization (GitHub-fetch for shell-less substrates) and run
   `test_byte_identity_across_substrates` — **run this one first**; it is the
   cheapest test with the highest architectural information.

## Honest flaw

`test_integrity_failure_exits_2` as written above is not a real test — it
rehydrates an untampered capsule and asserts exit 2. The transcriber must
actually corrupt a byte first. I am flagging it rather than leaving a plausible-
looking assertion that would pass for the wrong reason, which is the exact defect
class this suite exists to catch.
