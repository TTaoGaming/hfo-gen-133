# RED FIRST — bitemporal rollup

`contracts/bitemporal_rollup.contract.md` · spec §5

## Exact invocation

```
cd C:\Dev\hfo_gen_133_forge
python -m pytest tests/held_out/bitemporal_rollup -q
```

## Assertions

```python
ROLLUPS = REPO / "state" / "world" / "rollups"
CADENCE_H = {"world": 1, "valkyrie": 1, "apex": 24}

def test_rollups_exist_for_every_songline(roster):
    for tier in ("world","apex","valkyrie"):
        for e in roster[tier]:
            assert (ROLLUPS / tier / f"{e['callsign']}.jsonl").exists()

def test_both_time_axes_present_and_zulu():
    for f in ROLLUPS.rglob("*.jsonl"):
        for r in read_jsonl(f):
            assert r["window"]["valid_time_start"].endswith("Z")
            assert r["transaction_time_utc"].endswith("Z")

def test_rollup_is_derivable_from_source_rows():     # BT-2 -- the real one
    for f in ROLLUPS.rglob("*.jsonl"):
        for r in read_jsonl(f):
            recomputed = recompute_rollup(REPO / r["source_rows"]["chain"], r["window"])
            assert recomputed["counts"] == r["counts"]      # LOG WINS on disagreement

def test_rollups_are_prev_linked():                  # BT-1
    for f in ROLLUPS.rglob("*.jsonl"):
        rows = read_jsonl(f)
        for i in range(1, len(rows)):
            assert rows[i]["prev_rollup_sha256"] == rows[i-1]["rollup_sha256"]

def test_window_size_matches_tier_cadence():
    for tier, hours in CADENCE_H.items():
        for f in (ROLLUPS/tier).glob("*.jsonl"):
            for r in read_jsonl(f):
                assert window_hours(r["window"]) == hours

def test_apex_rolls_up_daily_not_hourly():           # operator canonical
    for f in (ROLLUPS/"apex").glob("*.jsonl"):
        rows = read_jsonl(f)
        assert all(gap_hours(rows[i-1], rows[i]) >= 20 for i in range(1,len(rows)))

def test_no_cross_tier_fabrication():                # BT-3
    for f in (ROLLUPS/"apex").glob("*.jsonl"):
        for r in read_jsonl(f):
            assert set(r["source_rows"]["children"]) <= set(valkyries_of(r["songline"]))

def test_missing_input_is_recorded_not_interpolated():   # BT-4
    for f in ROLLUPS.rglob("*.jsonl"):
        for r in read_jsonl(f):
            c = r["cadence_compliance"]
            assert c["observed"] + c["missed"] == c["expected"]

def test_world_rollup_carries_apex_staleness():
    for r in read_jsonl(ROLLUPS/"world"/"HFO_WORLD.jsonl"):
        assert len(r["apex_rollup_age_hours"]) == 8

def test_asof_query_time_travels():                  # the whole reason for two axes
    out = run("python", "tools/hfo.py", "asof", "sigrun", "2026-07-30T00:00:00Z")
    assert out.returncode == 0 and json.loads(out.stdout)["as_of_query_key"] == \
        "sigrun@2026-07-30T00:00:00Z"
```

## Why it is RED today

| assertion | red reason |
|---|---|
| all | **no rollup has ever been produced at gen-133, at any tier** |
| `test_asof_query_time_travels` | **no as-of query exists.** gen-130 had a working one (`ssot_history_drain.py asof <doc> <ISO_UTC>`, hash-chained SQLite); gen-133 has nothing |
| `test_rollup_is_derivable_from_source_rows` | BT-2 has never been exercised, so derivability is a design claim |

## What turns it green

1. One valkyrie producing one hourly rollup from its own chain.
2. `recompute_rollup` — the derivability checker — built **first**, because BT-2
   is what stops a rollup drifting into an unfalsifiable summary.
3. Port or re-specify the as-of query from gen-130.

## Honest flaw

Bitemporality currently has **no consumer**. Two time axes cost something to
maintain, and the only thing that redeems the cost is the as-of query, which does
not exist. Until it does, `valid_time` and `transaction_time` are overhead
carried on faith — correct faith, in my judgement, but faith.
