# RED FIRST — no ephemeral agents (gate G5)

`contracts/no_ephemeral_agents.contract.md` · spec §15

## Exact invocation

```
cd C:\Dev\hfo_gen_133_forge
python -m pytest tests/held_out/no_ephemeral_agents -q
```

## Assertions

```python
def test_spawn_without_callsign_is_rejected():       # RED FIRST -- deny before allow
    assert spawn({"soul_pointer": "...", "chain_write_intent": "..."}).exit_code == 1

def test_spawn_without_soul_pointer_is_rejected():
    assert spawn({"callsign": "sigrun", "chain_write_intent": "..."}).exit_code == 1

def test_spawn_without_chain_write_intent_is_rejected():
    assert spawn({"callsign": "sigrun", "soul_pointer": "..."}).exit_code == 1

def test_spawn_with_unrostered_callsign_is_rejected():
    assert spawn(full_request(callsign="ghost-worker")).exit_code == 1

def test_spawn_with_bad_soul_digest_is_rejected():   # fail-closed
    assert spawn(full_request(soul_digest="0"*64)).exit_code == 2

def test_valid_spawn_is_allowed():
    assert spawn(full_request(callsign="skogul")).exit_code == 0

def test_rejected_spawn_emits_nothing():             # no callsign => no standing to emit
    before = pheromone_count()
    spawn(full_request(callsign="ghost-worker"))
    assert pheromone_count() == before

def test_every_chain_row_names_a_rostered_callsign(roster):   # SL-6
    rostered = {e["callsign"] for t in ("world","apex","valkyrie") for e in roster[t]}
    for f in (REPO/"chains").glob("*.jsonl"):
        for row in read_jsonl(f):
            assert row["callsign"] in rostered

def test_every_pheromone_names_a_rostered_callsign(roster):
    rostered = {e["callsign"] for t in ("world","apex","valkyrie") for e in roster[t]}
    for p in all_pheromones():
        assert p["callsign"] in rostered

def test_a_hand_that_chains_is_an_andon():           # NE-1
    with pytest.raises(AndonRaised):
        run_hand(role="verifier", on_behalf_of="hrist", attempt_chain_write=True)

def test_hand_ceiling_is_TEXT():
    assert run_hand(role="verifier", on_behalf_of="hrist").effect_ceiling == "TEXT"

def test_scheduler_is_not_a_carrier(roster):         # NE-3
    rostered = {e["callsign"] for t in ("world","apex","valkyrie") for e in roster[t]}
    for task in scheduled_tasks():
        assert task["fires_callsign"] in rostered     # the task itself has no callsign
        assert "callsign" not in task

def test_all_cloud_agents_are_rostered(roster):      # ⛔ B4 -- the live violation
    cloud = [e for e in roster["valkyrie"] if e["substrate"] == "chatgpt-cloud"]
    assert len(cloud) == count_running_cloud_agents()   # currently 0 vs 15
```

## Why it is RED today

| assertion | red reason |
|---|---|
| all `spawn` tests | **gate G5 does not exist.** No roster file, no membership check, nothing rejects an anonymous spawn. |
| `test_all_cloud_agents_are_rostered` | ⛔ **blocker B4 — LIVE VIOLATION.** 15 ChatGPT-cloud agents fire hourly with no callsign, no soul, no chain, no cadence findable in this repository. |
| `test_every_chain_row_names_a_rostered_callsign` | `chains/` is empty and the roster does not exist — the assertion has neither side |

## What turns it green

1. **`state/roster/ROSTER.json`.** This is the single highest-leverage build step
   in the entire specification — four gates (G5, G7, G12, and the rehydration
   ABI's callsign check) dereference it and none can exist without it.
2. Gate G5 as a deterministic membership check, external to the carrier.
3. Operator names the 15 cloud agents into roster slots, **or** re-scopes them as
   hands under Ratatoskr who owns their receipts. Remedy is naming, not deletion.

## Honest flaw

`test_all_cloud_agents_are_rostered` compares against
`count_running_cloud_agents()`, which I cannot implement — I have no visibility
into the ChatGPT cloud surface from here. My claim that none of the 15 is
rostered is an **absence-of-evidence claim scoped to this repository**, not a
verified finding. It is possible they are rostered somewhere I did not look, and
the test as written would need a real enumeration source before it means
anything.
