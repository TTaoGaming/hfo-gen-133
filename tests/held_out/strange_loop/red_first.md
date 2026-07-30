# RED FIRST — strange loop (self-audit + review receipts)

`contracts/strange_loop.contract.md` · spec §12

## Exact invocation

```
cd C:\Dev\hfo_gen_133_forge
python -m pytest tests/held_out/strange_loop -q
```

## Assertions

```python
def test_every_cycle_self_audited_before_working():      # SL-1
    for f in (REPO/"chains").glob("*.jsonl"):
        for row in read_jsonl(f):
            assert "self_audit" in row["body"]
            assert row["body"]["self_audit"]["completed_before_work"] is True

def test_self_audit_covers_last_five_rows():
    for f in (REPO/"chains").glob("*.jsonl"):
        rows = read_jsonl(f)
        for i, row in enumerate(rows):
            expected = min(5, i)
            assert len(row["body"]["self_audit"]["rows_examined"]) == expected

def test_verifier_results_still_reproduce():             # SL-2 -- the only audit with teeth
    for f in (REPO/"chains").glob("*.jsonl"):
        for row in read_jsonl(f):
            if row["claim_status"] != "proposed":
                assert rerun(row["verifier_result"]).exit_code == 0

def test_failed_reproduction_downgrades_and_andons():
    row = inject_stale_verifier_result()
    audit = self_audit(row["callsign"])
    assert audit["downgraded"] == [row["row_sha256"]]
    assert any(p["pheromone_kind"] == "andon" for p in emitted_since(audit["ts"]))

def test_every_drift_becomes_a_finding():                # SL-5
    for f in (REPO/"chains").glob("*.jsonl"):
        for row in read_jsonl(f):
            a = row["body"]["self_audit"]
            assert len(a["findings"]) == a["mismatch_count"]

def test_closed_flaws_recorded_closed_not_dropped():     # SL-5
    for f in (REPO/"chains").glob("*.jsonl"):
        rows = read_jsonl(f)
        for i in range(1, len(rows)):
            prev_flaw = rows[i-1]["honest_flaw"]
            if prev_flaw not in rows[i]["honest_flaw"]:
                assert prev_flaw in rows[i]["body"]["self_audit"]["closed_flaws"]

def test_no_carrier_attests_its_own_row():               # SL-3
    for p in all_pheromones(kind="receipt"):
        assert p["callsign"] != p["payload"]["attests_callsign"]

def test_identity_claims_need_cross_family_attestation():  # G12
    for p in all_pheromones(kind="receipt"):
        if p["payload"].get("claim_class") == "identity":
            assert p["payload"]["attestor_family"] != author_family(p["payload"])

def test_verdict_is_stood_or_fell():
    for p in all_pheromones(kind="receipt"):
        assert p["payload"]["verdict"] in ("STOOD", "FELL")

def test_one_work_item_per_invocation():                 # SL-4 / RULE ZERO
    for f in (REPO/"chains").glob("*.jsonl"):
        for row in read_jsonl(f):
            assert len(row["body"]["work_items"]) <= 1
```

## Why it is RED today

| assertion | red reason |
|---|---|
| all chain-reading assertions | **`chains/` at gen-133 is empty** |
| `test_no_carrier_attests_its_own_row` | **exactly one carrier family is live.** With one carrier there is nobody to attest, so every row is `proposed` by construction — including the rows asserting this suite is sound |
| `test_identity_claims_need_cross_family_attestation` | zero cross-family attestations exist; the soul v1.1.0 has been read only by Claude lanes, eight-plus consecutive same-family passes deep |
| `test_verifier_results_still_reproduce` | requires `verifier_result` to name a **re-runnable** check; most inherited rows carry prose |

## What turns it green

1. **A second model family running.** This is the single unlock — it is standing
   next action #2 on Sigrún's soul ("appoint a non-Claude verifier") and it turns
   three of these assertions from structurally-impossible to merely-unbuilt.
   Codex (Huginn+Muninn / Garmr) is the nearest candidate.
2. A `verifier_result` convention that is machine-re-runnable, not prose.
3. One carrier completing one full 10-step cycle.

## Honest flaw

This is the suite I am least able to test and most implicated by. I am a single
Claude lane writing assertions that say single-family output cannot be trusted —
which means this file's own claim to be well-designed is, by its own standard,
`proposed`. That is the correct reading and I am not going to soften it.
