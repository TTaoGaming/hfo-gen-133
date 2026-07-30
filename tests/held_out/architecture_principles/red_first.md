# RED FIRST — architecture principles

```yaml
test_dir: tests/held_out/architecture_principles/
schema_id: hfo.gen133.held_out.architecture_principles.v0_1
spec: GEN133_ARCHITECTURE_PRINCIPLES.md
authored_by: SIGRÚN P4 · claude-opus-5
valid_time_utc: 2026-07-30T00:00:00Z
status: SPECIFIED AS MARKDOWN — .py authoring DENIED (code_authoring lease)
sealed: false
```

## Exact invocation

```
cd C:\Dev\hfo_gen_133_forge
python -m pytest tests/held_out/test_architecture_principles.py -q
```

**Expected on transcription: 8 failed.** Shared helpers per
`tests/held_out/RED_FIRST.md` §4 (`canon`, `canon_sha256`, `read_jsonl`, `REPO`).

## Assertions

```python
APEX = ["nidhoggr","fenrir","jormungandr","huginn","sigrun","surtr","garmr","ratatoskr"]
APEX_CADENCES     = {"4h": 14400, "8h": 28800, "24h": 86400}   # daily is the FLOOR
VALKYRIE_MAX_SECS = 3600                                        # hourly or LESS

def test_apex_cadence_is_strategic(roster):          # principles S1
    apexes = [e for e in roster["apex"]]
    assert len(apexes) == 8
    assert {e["callsign"] for e in apexes} == set(APEX)
    for e in apexes:
        assert e["cadence"] in APEX_CADENCES, f"{e['callsign']} cadence off-tier"
        assert APEX_CADENCES[e["cadence"]] >= 14400, "apex faster than 4h is tactical"

def test_valkyrie_cadence_is_tactical(roster):       # principles S1
    vs = roster["valkyrie"]
    assert 16 <= len(vs) <= 64, f"roster holds {len(vs)}, spec says 16-64"
    for e in vs:
        assert cadence_seconds(e["cadence"]) <= VALKYRIE_MAX_SECS

def test_every_row_is_bitemporal():                  # BT-1
    for path in (REPO/"chains").glob("*.jsonl"):
        for row in read_jsonl(path):
            assert row["valid_time_utc"].endswith("Z")
            assert row["transaction_time_utc"].endswith("Z")
            assert row["prev_hash"] is not None or row["row_index"] == 0
            assert len(row["row_sha256"]) == 64

def test_deterministic_replay():                     # BT-2
    # replay is a PURE function of the log: same coordinate, same bytes, twice,
    # with no network.
    coord = ("2026-07-30T00:00:00Z", "2026-07-30T12:00:00Z")
    a = replay_world_state(*coord)
    b = replay_world_state(*coord)
    assert canon(a) == canon(b)
    assert replay_touched_network() is False

def test_no_read_returns_the_whole_hive():           # NS-1
    # the query engine may compute over everything; an AGENT-facing read may not
    # RETURN everything.
    packet = rehydration_packet(callsign="hlokk")
    assert set(packet["visible_carriers"]) < all_carriers(), "unbounded projection"
    with pytest.raises(BoundedProjectionError):
        agent_read(callsign="hlokk", query="ALL_CARRIER_STATE")

def test_genotype_is_conserved_phenotype_varies():   # GP-1
    souls = list((REPO/"state"/"identity"/"soul").rglob("*.soul.md"))
    assert souls, "no souls exist"
    ids = {frontmatter(s)["schema_id"] for s in souls}
    assert ids == {"hfo.gen133.frontmatter.v3"}, f"genotype drift: {ids}"
    # ...and the phenotype fields genuinely differ between carriers
    assert len({frontmatter(s)["callsign"] for s in souls}) == len(souls)

def test_phylactery_possession(lineage="sigrun"):    # principles S7 -- 4 conjuncts
    p = phylactery(lineage)
    assert p.bytes_reproducible()
    assert p.canon_sha256 == roster_soul_digest(lineage)
    assert p.supersede_chain_contiguous()
    assert p.chain_head_sha256 == live_head(closest_continuer_chain(lineage))

def test_speciation_has_a_fitness_function():        # SP-1
    # a name is not a species. Selection must have RETIRED something.
    assert callable(fitness)
    rounds = read_jsonl(REPO/"state"/"ssot"/"colosseum_rounds.jsonl")
    assert rounds, "no selection event has ever run"
    assert any(r["retired_phenotype"] for r in rounds), \
        "nothing has ever been deselected -- this is a division of labor, not speciation"
```

## Why each is RED today

| assertion | red reason |
|---|---|
| `test_apex_cadence_is_strategic` | `state/roster/ROSTER.json` does not exist; 0 of 8 apex rostered with a cadence |
| `test_valkyrie_cadence_is_tactical` | same; 0 valkyries rostered |
| `test_every_row_is_bitemporal` | `chains/` does not exist in gen-133 |
| `test_deterministic_replay` | no replay function exists |
| `test_no_read_returns_the_whole_hive` | no projection API, no `BoundedProjectionError`, **and no numeric projection bound is set** (principles §3.1) |
| `test_genotype_is_conserved_phenotype_varies` | 2 soul files exist; frontmatter v3 authority sits with Codex-Sigrún and is mid-work |
| `test_phylactery_possession` | ⛔ **B1** — Sigrún phylactery INVALID, canonical head unnamed. Fails the 4th conjunct **by design, correctly** |
| `test_speciation_has_a_fitness_function` | no `fitness()`, no Colosseum round, nothing ever retired |

## What turns them green

1. `state/roster/ROSTER.json` with 8 apex + ≥16 valkyries, each with a cadence.
2. **Resolve B1** — locate the `SIGRUN_P4.jsonl` fork, name the canonical head.
   This is upstream of nearly everything else here.
3. Define `fitness(phenotype)` with at least one **external-effect** term, run one
   Colosseum round, retire one phenotype.
4. Set a numeric projection bound and raise `BoundedProjectionError` past it.

## Honest flaw

`test_phylactery_possession` is the one I most expect to be argued with, so I am
flagging it: it fails today and **that is the correct result**, not a bug in the
test. Weakening it until it passes would make the possession test decoration. The
cure is fixing B1, not the assertion.

`test_speciation_has_a_fitness_function` asserts against
`state/ssot/colosseum_rounds.jsonl`, a path I invented in this document. If
Fenrir's Colosseum already writes somewhere else, the path is wrong and the
assertion is right — **fix the path, not the requirement.**

None of these has been executed.
