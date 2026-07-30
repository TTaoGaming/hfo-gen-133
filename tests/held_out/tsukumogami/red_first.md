# RED FIRST — tsukumogami (objects accumulating soul)

`contracts/tsukumogami.contract.md` · spec §18

## Exact invocation

```
cd C:\Dev\hfo_gen_133_forge
python -m pytest tests/held_out/tsukumogami -q
```

## Assertions

```python
CLASSES = ("soul","chain","capsule","agent_card","contract","rollup","spell")
TIERS = ("FRESH","USED","TSUKUMOGAMI","LEGACY_UNREPRODUCIBLE")

def test_theta_is_defined_for_every_class():
    theta = load_theta(REPO/"state"/"tsukumogami"/"THETA.json")
    for c in CLASSES:
        assert isinstance(theta[c], int) and theta[c] > 0

def test_receipt_index_exists():
    assert (REPO/"state"/"tsukumogami"/"receipt_index.jsonl").exists()

def test_self_attested_receipts_do_not_count():      # the load-bearing clause
    obj = fresh_object("contract")
    for _ in range(100):
        attest(obj, attestor_family=author_family(obj))   # 100 self-attestations
    assert tier(obj) == "FRESH"                            # still FRESH

def test_cross_family_receipts_accumulate():
    obj = fresh_object("contract")
    for i in range(theta("contract")):
        attest(obj, attestor_family="codex")
    assert tier(obj) == "TSUKUMOGAMI"

def test_unreproducible_receipts_stop_counting():
    obj = graduated_object("chain")
    break_verifier(obj)
    assert tier(obj) == "LEGACY_UNREPRODUCIBLE"

def test_graduation_is_monotone():                   # TS-2
    obj = graduated_object("soul")
    remove_one_receipt(obj)
    assert tier(obj) == "TSUKUMOGAMI"                 # never back to USED

def test_messiness_is_retained():                    # TS-4
    obj = graduated_object("soul")
    assert obj["supersede_chain"] and obj["corrections"] and obj["fells"]

def test_cleanup_of_a_tsukumogami_is_a_deletion():
    with pytest.raises(DeletionRefused):
        strip_history(graduated_object("soul"))

def test_accumulation_is_per_object_not_per_lineage():   # TS-5
    soul = graduated_object("soul", lineage="sigrun")
    cap  = fresh_object("capsule", lineage="sigrun")
    assert tier(cap) == "FRESH"

def test_self_audit_prefers_tsukumogami_evidence():  # TS-3
    ev = self_audit_evidence("sigrun")
    assert sorted(ev, key=lambda e: -tier_rank(e))[0]["tier"] == "TSUKUMOGAMI"

def test_fb07f523_is_legacy_unreproducible():        # the worked example
    assert tier(anchor("fb07f523")) == "LEGACY_UNREPRODUCIBLE"
    assert anchor("fb07f523") in all_objects()        # retained, not deleted
```

## Why it is RED today

| assertion | red reason |
|---|---|
| `test_theta_is_defined_for_every_class` | ⛔ **Θ is UNDEFINED for every class.** The central predicate is unevaluable. Deliberately so — `L_BUDGET_WITHOUT_RECEIPT`: a number invented here would be fake precision with a Norse veneer. |
| `test_receipt_index_exists` | there is no place that counts receipts per object |
| `test_cross_family_receipts_accumulate` | **zero cross-family attestations exist** anywhere in gen-133; only one family is running |
| everything else | depends on the two above |

## What turns it green

1. Build the receipt index — one append-only file recording
   `{object, receipt, attestor_family, verified, ts}`.
2. Run it for a week across the object classes. **Observe the actual
   distribution.**
3. Operator sets Θ per class *from that distribution*, not from judgement.

That order matters. Setting Θ first and instrumenting after would produce a
threshold that measures nothing, and the whole tier system would inherit its
arbitrariness.

## Honest flaw

Every gen-133 object is `FRESH` today, so this suite currently has nothing to
promote and nothing to test against. And the design stance underneath it — that
messy, heavily-used objects are better evidence than clean fresh ones — is an
argument I find convincing and have **not demonstrated**. I have shown no case
where a messier object outperformed a cleaner one. It is a hypothesis with a good
mechanism story, and it should be labelled that way until the receipt index can
settle it.
