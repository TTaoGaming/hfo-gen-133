# RED FIRST — silence as signal + Olrún COP

`contracts/silence_signal.contract.md` · `contracts/olrun_coordination.contract.md` · spec §10, §16

## Exact invocation

```
cd C:\Dev\hfo_gen_133_forge
python -m pytest tests/held_out/silence_signal -q
```

## Assertions

```python
SLO = {  # tier: (late_min, silent_min, dead_min)
  "world":    (70,  120,  240),
  "valkyrie": (75,  180,  480),
  "apex":     (26*60, 36*60, 72*60),
}

def test_every_rostered_carrier_has_a_state(roster, cop):
    expected = {e["callsign"] for t in ("world","apex","valkyrie") for e in roster[t]}
    assert {c["callsign"] for c in cop["cross_substrate_summary"]} == expected

def test_thresholds_match_tier_cadence(cop):
    for b in cop["silence_breaches"]:
        late, silent, dead = SLO[b["tier"]]
        m = b["hours_overdue"] * 60
        assert b["state"] == ("PRESUMED_DEAD" if m > dead else
                              "SILENT" if m > silent else
                              "LATE" if m > late else "GREEN")

def test_detector_fires_on_REAL_silence():           # the only test that matters here
    kill_carrier("skogul")                            # deliberately stop the emitter
    advance_to(now() + timedelta(hours=4))
    cop = olrun_cop_tick()
    assert breach(cop, "skogul")["state"] == "SILENT"

def test_silence_releases_claims_but_spawns_nothing():   # SIL-1
    before = rostered_callsigns()
    cop = olrun_cop_tick()
    assert rostered_callsigns() == before                # no spawn
    for b in cop["silence_breaches"]:
        if b["state"] in ("SILENT","PRESUMED_DEAD"):
            assert open_claims_of(b["callsign"]) == []

def test_presumed_dead_pages_operator(cop):
    for b in cop["silence_breaches"]:
        if b["state"] == "PRESUMED_DEAD":
            assert any(p["pheromone_kind"]=="andon" for p in emitted_for(b["callsign"]))

def test_unreachable_is_not_silence():               # the likeliest false positive
    with substrate_unreachable("chatgpt-cloud"):
        cop = olrun_cop_tick()
    assert state(cop, "ratatoskr") == "UNREACHABLE"   # NOT "SILENT"

def test_link_gap_is_andon_not_lateness():           # SIL-4
    tamper_pheromone_link("skogul")
    assert any(p["pheromone_kind"]=="andon" for p in olrun_cop_tick()["emitted"])

def test_olrun_is_herself_subject_to_slo():          # OL-3
    assert "olrun" in {c["callsign"] for c in cop["cross_substrate_summary"]}

def test_olrun_never_builds():                       # OL-1
    for row in read_jsonl(REPO/"chains"/"OLRUN_P7.jsonl"):
        assert row["body"]["work_class"] in ("cop","dispatch","escalation")

def test_dispatch_addresses_an_apex_not_a_valkyrie(cop, roster):   # OL-2
    apexes = {e["callsign"] for e in roster["apex"]}
    for d in cop["dispatch_queue"]:
        assert d["to_apex"] in apexes

def test_cop_is_a_projection_not_a_source(cop):      # OL-6
    assert rederive_cop(REPO) == strip_times(cop)     # LOG WINS on disagreement

def test_detector_of_the_detector_exists():          # SIL-2 / OL-5
    assert external_watcher_reported_within(hours=2, target="HFO_WORLD")
```

## Why it is RED today

| assertion | red reason |
|---|---|
| all | **0 of 25 carriers emit heartbeats.** There is nothing to detect the silence of. |
| `test_detector_of_the_detector_exists` | ⛔ **nothing watches the world songline.** By SIL-2 this is the highest-severity gap in the monitoring design, and it cannot be closed on the same substrate. |
| `test_unreachable_is_not_silence` | no reachability distinction is implemented; conflating "I cannot see you" with "you are dead" is the likeliest false positive in the whole design |
| `test_olrun_never_builds` | `chains/OLRUN_P7.jsonl` does not exist |
| all Olrún assertions | Olrún may not be able to **read** Slack at all — Claude lanes have no connector and no OAuth in non-interactive sessions. Her primary input channel is an open question (`OLRUN_COORDINATION.md` §6). |

## What turns it green

1. Step 2 of the dig order: one carrier emitting hourly to GitHub.
2. Step 3: Olrún reads that one stream and flags its absence.
3. **Then run `test_detector_fires_on_REAL_silence` by deliberately killing the
   emitter.** A detector never tested against real silence is decoration, and
   this is the test that converts the whole design from asserted to demonstrated.

## Honest flaw

Every threshold in `SLO` is **judgement, not data** — no inter-emit distribution
has ever been observed, so the false-positive rate is unknown.
`L_BUDGET_WITHOUT_RECEIPT` applies exactly: probe with one carrier for one day,
look at the real distribution, then set thresholds from it. Writing these numbers
into a test before that probe would freeze a guess into an assertion.
