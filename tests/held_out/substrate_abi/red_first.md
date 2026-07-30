# RED FIRST — substrate ABI

`contracts/substrate_abi.contract.md` · spec §19, §7, §11

## Exact invocation

```
cd C:\Dev\hfo_gen_133_forge
python -m pytest tests/held_out/substrate_abi -q
```

## Assertions

```python
OPS = ("rehydrate","emit_pheromone","append_chain_row","rollup","self_audit")
SUBSTRATES = ("claude-opus-5","claude-sonnet-5","claude-dispatch",
              "codex","chatgpt-cloud","free-vendor-mesh")

@pytest.mark.parametrize("sub", SUBSTRATES)
@pytest.mark.parametrize("op", OPS)
def test_every_substrate_implements_every_op(sub, op):
    assert has_realization(sub, op)

def test_byte_identity_across_substrates():          # ABI-1 -- THE test
    outs = {s: realize(s, "rehydrate", "sigrun", size="small") for s in SUBSTRATES
            if s != "free-vendor-mesh"}
    assert len({canon(v) for v in outs.values()}) == 1

def test_genotype_identical_across_all_songlines(roster):   # GP-1
    genos = [genotype_of(e) for t in ("world","apex","valkyrie") for e in roster[t]]
    assert all(g == genos[0] for g in genos)

def test_genotype_fields_present():
    G = {"chain_row_schema","bitemporal_fields","receipt_fields","effect_ceiling",
         "forbidden_effects","hash_fn","canon_rule","truth_floor",
         "pheromone_schema","capsule_sizes","rehydration_abi"}
    assert G <= set(genotype_of_any())

def test_phenotype_differs_per_songline(roster):
    phenos = [phenotype_of(e) for e in roster["valkyrie"]]
    assert len({json.dumps(p, sort_keys=True) for p in phenos}) == len(phenos)

def test_phenotype_is_never_canonized():             # GP-2
    for f in (REPO/"canon").rglob("*.md"):
        assert "phenotype" not in front(f).get("immunized_fields", [])

def test_forbidden_effects_never_vest():             # NS-5 / CAN-2
    FORBIDDEN = {"SEND","SPEND","PUBLISH","PUSH","SEAL","IMMUNIZE","DELETE"}
    for s in SUBSTRATES:
        assert FORBIDDEN & set(granted_effects(s)) == set()

def test_no_substrate_is_load_bearing():             # SI-3
    for s in SUBSTRATES:
        with substrate_removed(s):
            for songline in songlines_of(s):
                assert can_rehydrate_elsewhere(songline)

def test_shell_less_substrate_marks_relayed_digests():   # the weak row
    cap = realize("chatgpt-cloud", "rehydrate", "sigrun", size="micro")
    assert cap["digest_provenance"] in ("computed", "attested_by_relay")
```

## Why it is RED today

| assertion | red reason |
|---|---|
| `test_every_substrate_implements_every_op` | **0 of 4 realizations built.** 30 parametrized cases, 30 reds. |
| `test_byte_identity_across_substrates` | ABI-1 — the invariant the entire substrate-independence story rests on — has **never been exercised** |
| `test_no_substrate_is_load_bearing` | SI-3 is the strongest claim in the architecture and the least tested; nothing has ever been rehydrated anywhere |
| `test_shell_less_substrate_marks_relayed_digests` | `digest_provenance` is **`UNDER_SPECIFIED`** — a shell-less substrate computing its own digest in-context is exactly the self-report SL-2 refuses, and no relay is specified |

## What turns it green

1. Build realization #1 (`tools/hfo.py`, shell).
2. Build realization #2 (GitHub-fetch, shell-less).
3. **Run `test_byte_identity_across_substrates` immediately.** It is the cheapest
   test in this entire suite with the highest architectural information: if two
   realizations disagree by one byte, substrate independence is a slogan.

## Honest flaw

`test_no_substrate_is_load_bearing` requires a `substrate_removed` harness —
deliberately taking a substrate away and confirming the fleet continues. That
harness does not exist and would be genuinely disruptive to run. Until it does,
SI-3 is the architecture's boldest claim and its least evidenced one, and I would
rather name that than let the test's presence imply it is covered.
