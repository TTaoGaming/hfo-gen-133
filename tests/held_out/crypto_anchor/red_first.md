# RED FIRST — crypto anchor

`contracts/crypto_anchor.contract.md` · spec §8

## Exact invocation

```
cd C:\Dev\hfo_gen_133_forge
python -m pytest tests/held_out/crypto_anchor -q
```

## Assertions

```python
SOUL = REPO / "state" / "identity" / "soul" / "sigrun.gen133.soul.md"

def test_soul_canon_hash_reproduces():               # GREEN-CAPABLE TODAY
    assert canon_sha256_with_placeholder(SOUL) == \
        "83b09f1e1009135e5e1ac4d112c63d3c28738c821fb4c3ac24ac3aa7e4f1adb0"

def test_canonicalization_rule_is_stated_in_artifact():   # CR-1
    assert "self_hash_convention" in SOUL.read_text("utf-8")

def test_every_durable_artifact_stamps_sealed():     # CR-5
    for f in REPO.rglob("*.md"):
        if has_frontmatter(f) and "sealed:" in front(f):
            if front(f)["sealed"] is False:
                assert front(f).get("seal_note")

def test_no_agent_generated_private_key_exists():    # CR-4
    for pat in ("*.pem", "*.key", "id_ed25519", "*.pk8"):
        assert not list(REPO.rglob(pat))

def test_ed25519_slot_is_null_not_fabricated():      # CR-4 / R10
    assert front(SOUL)["ed25519_pubkey"] is None
    assert front(SOUL)["ed25519_fingerprint"] is None

def test_chain_row_schema_required_fields():         # §8.2
    REQUIRED = {"schema_id","callsign","songline","tier","carrier",
                "valid_time_utc","transaction_time_utc","verifier_result",
                "claim_status","remaining_risk","next_safe_action","honest_flaw",
                "prev_sha256","row_sha256","sealed","seal_note"}
    for f in (REPO/"chains").glob("*.jsonl"):
        for row in read_jsonl(f):
            assert REQUIRED <= set(row)

def test_row_hash_reproduces():
    for f in (REPO/"chains").glob("*.jsonl"):
        for row in read_jsonl(f):
            b = dict(row); b["row_sha256"] = "SELF_HASH_PLACEHOLDER"
            assert row["row_sha256"] == sha256(canon(json.dumps(b, sort_keys=True).encode()))

def test_legacy_unreproducible_anchor_is_retained_not_deleted():   # CR-7
    assert grep(REPO, "fb07f523") and grep(REPO, "LEGACY_UNREPRODUCIBLE")

def test_fb07f523_is_not_asserted_as_current():
    for f in REPO.rglob("*.md"):
        assert "stef_parity: fb07f523" not in f.read_text("utf-8")

def test_permaweb_anchor_refetches():                # NETWORK -- operator-gated
    r = fetch("https://arweave.net/w1rsVQkkejXv7tVj_pMhcAz7HMFpY_dgwxGhoytBc9M")
    assert sha256(r) == "d32b6e4418537be4f5992c44d96e4c35f7aa4fab18762828cc703c385bf84ec0"
```

## Why it is RED today

| assertion | red reason |
|---|---|
| `test_chain_row_schema_required_fields`, `test_row_hash_reproduces` | **`chains/` at gen-133 is empty.** No row exists to check. |
| `test_permaweb_anchor_refetches` | no network egress authorized to this lane; the anchor is an **inherited, unverified** claim |
| `test_every_durable_artifact_stamps_sealed` | plausible today, **never run** |
| `test_soul_canon_hash_reproduces` | this one is **green-capable right now** — and that is exactly why it belongs here: it is the single assertion in the suite with a concrete expected digest |

## What turns it green

1. Any gen-133 chain row at all (blocked on choosing a writer — see `AGENTS.md`).
2. Operator generates the Ed25519 keypair, private half never on the agent path.
   Until then `test_ed25519_slot_is_null_not_fabricated` is the *correct* state
   and passing it is a feature, not a gap.
3. Network authorization for the permaweb re-fetch.

## Honest flaw

`test_soul_canon_hash_reproduces` is the only assertion here with a hard expected
value, and that value was computed by a single Claude lane. Under G12 a digest
confirmed only by one model family is not independently verified — so even the
green-capable test in this file needs a cross-family run before it means what it
appears to mean.
