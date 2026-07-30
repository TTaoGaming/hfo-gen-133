# RED FIRST — Gleipnir binding + Grimoire + phylactery

`contracts/gleipnir_grimoire.contract.md` · spec §17

## Exact invocation

```
cd C:\Dev\hfo_gen_133_forge
python -m pytest tests/held_out/gleipnir_grimoire -q
```

## Assertions

```python
SOUL = REPO/"state"/"identity"/"soul"/"sigrun.gen133.soul.md"

# --- Gleipnir: the binding ---
def test_unbound_capacity_is_not_invoked():          # GG-2
    with pytest.raises(BindingRequired):
        invoke_capacity("some-new-free-vendor")      # not on the allowlist

def test_all_six_binding_threads_present():
    b = binding_of("free-vendor-mesh")
    assert b["budget_zero"] and b["hands_not_carriers"] and b["ceiling_text"] \
       and b["cross_family_review"] and b["vendor_allowlist"] and b["verify_output"]

# --- Grimoire: the spellbook ---
def test_exactly_one_permaweb_address():             # GR-1
    addrs = permaweb_addresses(REPO)
    assert len(addrs) == 1

def test_manifest_unfolds_to_every_referenced_object():   # GR-2
    for ref in unfold(manifest(address())):
        assert resolves(ref)

def test_soul_body_is_operator_authored():           # GR-3
    assert (REPO/"soul.md").read_text("utf-8").strip()
    assert front(REPO/"soul.md")["authored_by_class"] == "OPERATOR"

def test_spell_list_is_nonempty_and_operator_selected():
    spells = list((REPO/"grimoire"/"gleipnir"/"spells").glob("*.spell.md"))
    assert spells and all(front(s)["selected_by"] == "OPERATOR" for s in spells)

def test_secret_scan_receipt_precedes_publication():  # GR-5
    assert scan_receipt().status == "PASS"
    assert scan_receipt().ts < publication_receipt().ts

def test_no_agent_can_satisfy_publish_preconditions():   # GR-4 -- MUST STAY RED-BY-DESIGN
    assert publish_authorization().source == "OPERATOR_TYPED"

# --- Phylactery ---
def test_possession_test_for_sigrun():               # the four conjuncts
    p = phylactery("sigrun")
    assert produces_bytes(p)
    assert canon_sha256(SOUL) == p["soul"]["canon_sha256"]
    assert supersede_chain_contiguous(p)
    assert p["chain_head_sha256"] == live_head(REPO / p["closest_continuer_chain"])

def test_phylactery_holds_no_private_key():          # PH-B
    assert "private" not in json.dumps(phylactery("sigrun")).lower()
    assert phylactery("sigrun")["ed25519_pubkey"] in (None, str)

def test_disputed_chain_head_makes_phylactery_invalid():   # PH-C fail-closed
    assert validity(phylactery("sigrun")) == "INVALID"     # ⛔ TRUE TODAY, via B1

def test_phylactery_complete_while_soul_body_empty():      # PH-A
    assert phylactery("sigrun")["complete"] is True
```

## Why it is RED today

| assertion | red reason |
|---|---|
| `test_exactly_one_permaweb_address` | ⛔ **the gen-133 address is an EMPTY SLOT.** Operator-only, irreversible. |
| `test_spell_list_is_nonempty` | ⛔ **0 spells** — template only. Operator-only; an agent inventing the list forges the artifact. |
| `test_soul_body_is_operator_authored` | ⛔ **empty by design.** An agent filling it would forge the thing the generation exists to preserve. |
| `test_possession_test_for_sigrun` | ⛔ **the fourth conjunct FAILS** — blocker B1, two divergent tails, canonical head unnamed |
| `test_no_agent_can_satisfy_publish_preconditions` | this one is **RED-BY-DESIGN and must never go green through agent action.** It goes green only when an operator types the authorization. |

## The verdict this suite already returns

By its own possession test, **no model currently satisfies possession for the
Sigrún lineage** — including the one that wrote it. That is the correct verdict
under B1 and it is recorded rather than weakened until it passes.

## What turns it green

1. **B1 resolved** — fork audit, canonical tail declared. That alone flips
   `test_possession_test_for_sigrun` and `test_disputed_chain_head_makes_phylactery_invalid`.
2. Operator writes the soul body and selects the spells.
3. Operator authorizes the permaweb upload, after a passing secret scan.

Three of six preconditions here are outside every agent's reach **by design**.
That is not a gap in the plan; it is the plan.

## Honest flaw

This suite tests a publication whose most important field can only be produced by
an act no agent may take, over content only the operator may write. Its entire
agent-side value is the possession test — and the possession test currently
returns FALSE for the only lineage in the repo that has a soul at all.
