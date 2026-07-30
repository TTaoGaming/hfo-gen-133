# RED FIRST — the four-substrate bus

```yaml
test_dir: tests/held_out/substrate_bus/
schema_id: hfo.gen133.held_out.substrate_bus.v0_1
contract: contracts/substrate_bus.contract.md
authored_by: SIGRÚN P4 · claude-opus-5
valid_time_utc: 2026-07-30T00:00:00Z
status: SPECIFIED AS MARKDOWN — .py authoring DENIED (code_authoring lease)
sealed: false
```

## Exact invocation

```
cd C:\Dev\hfo_gen_133_forge
python -m pytest tests/held_out/test_substrate_bus.py -q
```

**Expected on transcription: 6 failed.**

## Assertions

```python
def test_git_wins_on_disagreement():                    # SB-1
    # a projection that disagrees with git is WRONG and gets rebuilt.
    # Never repair git from a projection.
    seed_disagreement(git_says="GREEN", projection_says="SILENT", callsign="hlokk")
    assert resolve_state("hlokk") == "GREEN"
    assert projection_was_rebuilt() is True
    assert git_was_mutated() is False

def test_projection_is_droppable_and_rebuildable():     # SB-7
    before = xtdb_snapshot()
    xtdb_drop_all()
    reproject_from_git()
    assert xtdb_snapshot() == before, "something existed ONLY in the projection"

def test_xtdb_transaction_time_comes_from_the_row():    # section 4.1 step 2
    # NOT from the projector's clock -- that records when the projector ran and
    # silently destroys the property being bought.
    row = {"valid_time_utc": "2026-07-30T01:00:00Z",
           "transaction_time_utc": "2026-07-30T02:00:00Z"}
    project(row)
    doc = xtdb_get(row_sha256(row))
    assert doc.valid_time == row["valid_time_utc"]
    assert doc.transaction_time == row["transaction_time_utc"]

def test_slack_outage_creates_no_phantom_silence():     # SB-4 / PH-1
    with slack_down():
        emit_pheromone(callsign="hlokk", kind="heartbeat")   # reaches git
        assert evaluate_silence()["hlokk"] == "GREEN"

def test_pheromone_reaches_git_before_slack():          # SB-2
    with record_order() as o:
        emit_pheromone(callsign="hlokk", kind="heartbeat")
    assert o.index("git") < o.index("slack")
    with git_unwritable():
        with pytest.raises(DurableRecordError):
            emit_pheromone(callsign="hlokk", kind="heartbeat")

def test_sqlite_is_not_a_coordination_surface():        # SB-9
    # a local DB read by another agent is a hidden channel outside the audit.
    with audit_reads() as fx:
        run_wake(callsign="goll")
    foreign = [p for p in fx.sqlite_paths if "goll" not in str(p)]
    assert foreign == [], f"goll read another carrier's checkpoint: {foreign}"
```

## Why each is RED today

| assertion | red reason |
|---|---|
| `test_git_wins_on_disagreement` | no projection exists to disagree with git |
| `test_projection_is_droppable_and_rebuildable` | **XTDB is not running**; no projector |
| `test_xtdb_transaction_time_comes_from_the_row` | same |
| `test_slack_outage_creates_no_phantom_silence` | ⛔ **B3** — no authorized bot; Claude lanes have no Slack connector at all |
| `test_pheromone_reaches_git_before_slack` | **zero pheromones have ever been emitted** |
| `test_sqlite_is_not_a_coordination_surface` | no carrier has a SQLite checkpoint |

## What turns them green

1. Emit one real pheromone to git. That alone un-reds two assertions.
2. Resolve B3 (authorized bot identity) → Slack half of the bus.
3. Stand up XTDB + the projector; prove it by diffing a replayed coordinate
   against the same coordinate computed directly from the log.
4. Build per-carrier SQLite checkpoints, then run the read-audit.

**Run `test_pheromone_reaches_git_before_slack`'s failure branch first** — the
`git_unwritable()` case. A carrier that cannot write the durable record must fail
loudly; proving that it does is more important than proving the happy path
(NS-2: deny before allow).

## Honest flaw

Every helper here (`slack_down`, `record_order`, `audit_reads`, `xtdb_snapshot`)
is a fixture I described and did not build. The assertions encode the contract's
invariants correctly as far as I can tell, but a fixture that lies makes a green
test worthless — so **the fixtures need review as carefully as the code under
test**, and I am not in a position to write either.

The deeper flaw is upstream of all six: `contracts/substrate_bus.contract.md` §2
records that **git push is operator-gated**, so a carrier cannot reach the
canonical substrate unattended. Until that is resolved, every one of these tests
is measuring a bus that cannot carry traffic at the cadence the architecture
assumes. Fixing that gate matters more than making any of these green.
