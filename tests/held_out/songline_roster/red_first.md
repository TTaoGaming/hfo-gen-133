# RED FIRST — songline + roster

`contracts/songline.contract.md` · `contracts/substrate_roster.contract.md` · spec §2, §19

## Exact invocation

```
cd C:\Dev\hfo_gen_133_forge
python -m pytest tests/held_out/songline_roster -q
```

## Assertions

```python
TIER_SIZES   = {"world": 1, "apex": 8, "valkyrie": 16}
TIER_CADENCE = {"world": "hourly", "apex": "daily", "valkyrie": "hourly"}
ROSTER = REPO / "state" / "roster" / "ROSTER.json"

def test_roster_exists():
    assert ROSTER.exists()

def test_tier_sizes_are_1_8_16(roster):
    for tier, size in TIER_SIZES.items():
        assert len(roster[tier]) == size

def test_cadence_matches_operator_canonical(roster):
    # world hourly, apex DAILY, valkyrie hourly -- operator canonical 2026-07-30
    for tier, cadence in TIER_CADENCE.items():
        for e in roster[tier]:
            assert e["cadence"] == cadence

def test_four_durable_pointers(roster):
    for tier in TIER_SIZES:
        for e in roster[tier]:
            for f in ("callsign", "soul_pointer", "chain", "cadence"):
                assert e.get(f)

def test_no_callsign_at_two_tiers(roster):          # SR-2
    seen = set()
    for tier in TIER_SIZES:
        for e in roster[tier]:
            assert e["callsign"] not in seen
            seen.add(e["callsign"])

def test_every_substrate_has_apex_and_valkyries(roster):   # SI-4
    for s in roster["substrates"]:
        assert s["apex"] and s["valkyries"]

def test_chain_prev_links_contiguous(roster):       # SL-3
    for tier in TIER_SIZES:
        for e in roster[tier]:
            rows = read_jsonl(REPO / e["chain"])
            for i in range(1, len(rows)):
                assert rows[i]["prev_sha256"] == rows[i-1]["row_sha256"]

def test_no_invented_callsigns(roster):             # SR-3
    # TBD_OPERATOR / UNNAMED_ROSTER_SLOT are LEGAL values.
    # This test does not force names; it forces the placeholders to be explicit.
    for tier in TIER_SIZES:
        for e in roster[tier]:
            assert e["callsign"] or e.get("slot_status") in
                   ("TBD_OPERATOR", "UNNAMED_ROSTER_SLOT", "VACANT_RESERVED")
```

## Why it is RED today

| assertion | red reason |
|---|---|
| `test_roster_exists` | **`state/roster/ROSTER.json` does not exist.** Root cause of most reds in this suite. |
| `test_tier_sizes_are_1_8_16` | 5 of 8 apex and 9 of 16 valkyries are named; 3 apex + 4 valkyrie slots are open |
| `test_chain_prev_links_contiguous` | ⛔ **blocker B1** — `SIGRUN_P4.jsonl` has two divergent tails (58 rows head `a3eca451…` vs 61 rows head `6dfb0b8e…`), fork unlocated. This assertion is *expected to fail loudly* and must not be relaxed to make it pass. |
| `test_every_substrate_has_apex_and_valkyries` | Antigravity, $0 mesh, and laptop/VM have no apex; Claude Dispatch and ChatGPT cloud have no named valkyries |

## What turns it green

1. Write `state/roster/ROSTER.json` with the 1/8/16 shape, placeholders explicit.
2. Operator names A6, A7, A8 and V13–V16 (or the architecture amends to 1-7-16).
3. **B1 resolved** — full row-hash + prev-link audit of all three `SIGRUN_P4.jsonl`
   copies, fork point located, canonical tail declared by the operator or a
   different-family verifier.

## Honest flaw

`test_chain_prev_links_contiguous` will stay red until B1 is resolved, and B1 is
not resolvable by this lane. A suite with a permanently-red member trains readers
to ignore red. The mitigation is the **delta gate** (NS-3): compare the FAIL set
to a recorded baseline; same FAILs ⇒ PROCEED, a new FAIL ⇒ ANDON. That baseline
does not exist yet.
