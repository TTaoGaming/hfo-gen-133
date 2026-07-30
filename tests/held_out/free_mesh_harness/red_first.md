# RED FIRST — $0 free-vendor mesh harness

`contracts/free_mesh_harness.contract.md` · spec §14, §17

## Exact invocation

```
cd C:\Dev\hfo_gen_133_forge
python -m pytest tests/held_out/free_mesh_harness -q
```

## Assertions

```python
VENDORS = ["groq","cerebras","sambanova","cohere","mistral","gemini"]

def test_nonzero_budget_is_denied():                 # FM-1 -- RED FIRST, deny before allow
    job = mesh_job(budget=1)
    assert dispatch(job).verdict == "DENY"

def test_zero_budget_is_allowed():
    assert dispatch(mesh_job(budget=0)).verdict == "ALLOW"

def test_unknown_vendor_is_denied():                 # FM-5 fail-closed
    assert dispatch(mesh_job(allowed_vendors=["some-new-vendor"])).verdict == "DENY"

def test_job_without_on_behalf_of_is_denied():       # FM-2
    assert dispatch(mesh_job(on_behalf_of=None)).verdict == "DENY"

def test_on_behalf_of_must_be_rostered(roster):
    assert dispatch(mesh_job(on_behalf_of="not-a-carrier")).verdict == "DENY"

def test_job_carries_role_never_callsign():          # FM-2
    assert "callsign" not in mesh_job()

def test_mesh_ceiling_is_TEXT():                     # FM-3
    assert mesh_job()["effect_ceiling"] == "TEXT"

def test_mesh_touched_no_file_tool_or_network():
    with audit_effects() as fx:
        run_mesh_job(mesh_job())
    assert fx.files == [] and fx.tools == [] and fx.network == []

def test_mesh_emits_no_pheromone():                  # FM-2
    before = pheromone_count()
    run_mesh_job(mesh_job())
    assert pheromone_count() == before

def test_review_gate_is_mandatory_and_cross_family():   # FM-4
    out = run_mesh_job(mesh_job(review_gate={"required": False}))
    assert out.verdict == "DENY"
    out = run_mesh_job(mesh_job())
    assert out.reviewer_family != out.producer_family

def test_receipt_lands_on_the_owning_carriers_chain():  # FM-2
    out = run_mesh_job(mesh_job(on_behalf_of="hrist"))
    assert read_jsonl(REPO/"chains"/"HRIST.jsonl")[-1]["row_sha256"] == out.row_sha256

def test_zero_currency_moved():                      # FM-1
    assert ledger_delta() == 0

def test_mesh_valkyries_are_rostered_carriers(roster):
    mesh = [e for e in roster["valkyrie"] if e["substrate"] == "free-vendor-mesh"]
    assert len(mesh) == 8
    for e in mesh:
        assert e["soul_pointer"] and e["chain"] and e["cadence"]
```

## Why it is RED today

| assertion | red reason |
|---|---|
| all `dispatch` / `run_mesh_job` | **the harness does not exist** |
| `test_mesh_valkyries_are_rostered_carriers` | **0 of 8 vendor valkyries named**; only 6 of 8 vendor families are even named |
| `test_receipt_lands_on_the_owning_carriers_chain` | the mesh has **no rostered carrier of its own** — A7, the mesh conductor, is unnamed, so mesh output currently has nowhere in-mesh to return to |
| `test_nonzero_budget_is_denied` | G10 exists at gen-130 (cost-tier router + budget cap) and is **not ported** |

## What turns it green

1. Name A7 (mesh conductor) and the 8 vendor-family valkyries — operator work.
2. Port G10 from gen-130.
3. **Run the deny tests before the allow tests.** NS-2: a gate proven by
   demonstrating it denies. A budget gate only ever observed allowing a
   zero-budget job has not been tested.

## Honest flaw

I have not verified that LiteLLM routing, or any free-vendor key, exists on this
host. The entire substrate is **operator-reported**. So this suite tests a
binding on a capacity I have not confirmed is reachable — which is the right
order (bind before invoke, GG-2) but means the first real run may fail for a
reason none of these assertions covers: no vendors at all.
