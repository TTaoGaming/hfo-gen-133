# HELD-OUT TEST — substrate independence

```yaml
test: tests/held_out/test_substrate_independence.md
schema_id: hfo.gen133.held_out.substrate_independence.v0_1
spec: SUBSTRATE_APEX_ASSIGNMENT.md §4, §8
authored_by: SIGRÚN P4 · claude-opus-5
valid_time_utc: 2026-07-30T00:00:00Z
status: SPECIFIED AS MARKDOWN — .py authoring DENIED (code_authoring lease)
sealed: false
```

## 1 · What is held out

Ordinary held-out tests hold out **data**. This one holds out **the substrate** —
it asks whether a result survives being computed by a different mind.

> **GREEN** — the task passes on **≥3 independent model families** ⇒ the finding
> is about the world.
> **RED** — the task passes on exactly one family ⇒ the finding was about the
> tool. The task has encoded a substrate quirk.

A red here is *information*, not a defect: it tells you which of your results are
actually artifacts of one tokenizer, one RLHF history, one tool surface.

## 2 · The correction this test exists to enforce

**Count families, not platforms.** Two agreeing OpenAI carriers reached through
two different interfaces are one witness in two coats. A quorum that looks 6-wide
can be 3-deep, and the whole correctness-by-construction argument rests on the
depth, not the width.

## 3 · Exact invocation

```
cd C:\Dev\hfo_gen_133_forge
python -m pytest tests/held_out/test_substrate_independence.py -q
```

**Expected on transcription: 6 failed.**

## 4 · Assertions

```python
SUBSTRATES = ["claude","codex","chatgpt-cloud","antigravity","vscode","free-mesh"]
MIN_FAMILIES = 3

def families_of(results):
    return {r["model_family"] for r in results}

def test_every_carrier_records_model_family(roster):
    # the provenance gap: rows stamp agent + seat, never model. Without this
    # field NOTHING below is computable.
    for entry in roster["apex"] + roster["valkyrie"]:
        assert entry.get("model_family"), f"{entry['callsign']} records no model_family"
        assert entry.get("substrate") in SUBSTRATES

def test_every_chain_row_records_model_family():
    for path in (REPO/"chains").glob("*.jsonl"):
        for row in read_jsonl(path):
            assert row.get("model_family"), f"{path.name}: row {row['row_sha256'][:8]} has no family"

def test_consensus_is_weighted_by_family_not_platform():
    # THE test. Three platforms, one family, is ONE witness.
    results = [ {"substrate":"codex",         "model_family":"openai",  "verdict":"PASS"},
                {"substrate":"chatgpt-cloud", "model_family":"openai",  "verdict":"PASS"},
                {"substrate":"vscode",        "model_family":"openai",  "verdict":"PASS"} ]
    assert independence_score(results) == 1, "3 platforms of 1 family scored as 3"
    assert verdict(results) == "RED"

def test_task_passing_on_three_families_is_green():
    results = [ {"substrate":"claude",      "model_family":"anthropic", "verdict":"PASS"},
                {"substrate":"codex",       "model_family":"openai",    "verdict":"PASS"},
                {"substrate":"antigravity", "model_family":"google",    "verdict":"PASS"} ]
    assert len(families_of(results)) >= MIN_FAMILIES
    assert verdict(results) == "GREEN"

def test_single_family_pass_is_a_red_signal():
    results = [ {"substrate":"claude", "model_family":"anthropic", "verdict":"PASS"} ]
    v = verdict(results)
    assert v == "RED"
    assert reason(results) == "SUBSTRATE_COUPLED"   # not "insufficient data"

def test_no_substrate_holds_a_majority_of_apexes(roster):
    # concentration risk: one outage must not take the strategic tier
    from collections import Counter
    counts = Counter(e["substrate"] for e in roster["apex"])
    top_substrate, top_count = counts.most_common(1)[0]
    assert top_count <= len(roster["apex"]) // 2, \
        f"{top_substrate} holds {top_count} of {len(roster['apex'])} apexes"

def test_migration_preserves_one_lineage_one_chain():      # MG-1
    chain = read_jsonl(REPO/"chains"/"NIDHOGGR.jsonl")
    migrations = [r for r in chain if r["row_kind"] == "migration_intent"]
    assert migrations, "no migration has occurred"
    for m in migrations:
        assert m["from_substrate"] != m["to_substrate"]
        assert m["operator_ratified"] is True          # SIL-5: never automatic
        assert m["model_family_from"] and m["model_family_to"]
    # the callsign never changes across a migration -- a new callsign is a FORK
    assert len({r["callsign"] for r in chain}) == 1
```

## 5 · Why each is RED today

| assertion | red reason |
|---|---|
| `test_every_carrier_records_model_family` | **no roster file**, and `model_family` is not a field anywhere in gen-133 |
| `test_every_chain_row_records_model_family` | no `chains/` directory; the gen-130 provenance gap (rows stamp agent + seat, never model) carries forward unfixed |
| `test_consensus_is_weighted_by_family_not_platform` | no `independence_score()`; consensus today would count platforms |
| `test_task_passing_on_three_families_is_green` | **0 substrates have returned a receipt**; ≥3 is unreachable |
| `test_single_family_pass_is_a_red_signal` | no `verdict()` / `reason()` |
| `test_no_substrate_holds_a_majority_of_apexes` | ⛔ **5 of 8 apexes are on Codex right now** — this fails on live state, not on absence, and it is *meant* to fail during stabilization |

## 6 · The one that fails on purpose

`test_no_substrate_holds_a_majority_of_apexes` is red because of a **deliberate
operator decision** — pack on Codex until stable. It is in the suite anyway,
because a concentration risk you have chosen is still a risk you should be able to
see. It turns green as the §7 migrations execute, and it is the cleanest single
indicator that stabilization actually finished.

**Do not delete it to make the suite green.** Its redness is the measurement.

## 7 · What turns them green

1. Add `model_family` to the roster schema and to every chain row. **This is the
   cheapest high-value change in the whole architecture** — three of six
   assertions here, and the entire §4.1 correction, are blocked on one field.
2. Get any two substrates emitting real receipts, then a third from a different
   family.
3. Build `independence_score()` / `verdict()` weighting by family.
4. Complete the stabilization migrations (`SUBSTRATE_APEX_ASSIGNMENT.md` §7).

## 8 · Honest flaw

The test assumes `model_family` is knowable and stable per carrier. It may be
neither: VSCode's backing model is user-configurable and can change without a
chain row, and cloud platforms swap underlying models without notice. **A
`model_family` field that is stamped once at roster time will silently go stale,
and a stale family label is worse than none — it produces confident wrong
independence scores.** The field should be stamped **per row, from the runtime**,
not inherited from the roster. I have written the assertions that way
(`test_every_chain_row_records_model_family`), but the roster assertion above
still permits the weaker pattern, and I have not resolved which wins.

Second: `independence_score` treats families as equally independent. Two families
trained on overlapping corpora with similar RLHF are not as independent as the
count suggests. I have no way to measure that and I am not going to pretend the
number is better than ordinal.

Nothing here has been executed.
