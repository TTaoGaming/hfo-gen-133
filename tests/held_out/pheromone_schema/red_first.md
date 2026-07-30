# RED FIRST — pheromone schema + emit

`contracts/pheromone.contract.md` · spec §9

## Exact invocation

```
cd C:\Dev\hfo_gen_133_forge
python -m pytest tests/held_out/pheromone_schema -q
```

## Assertions

```python
KINDS = {"heartbeat","claim","release","receipt","blocker","andon",
         "rehydrated","rehydration_failed","rollup","silence_flag","dispatch"}
STREAMS = REPO / "state" / "world" / "pheromones"

def test_pheromone_streams_exist():
    assert STREAMS.exists() and any(STREAMS.rglob("*.jsonl"))

def test_every_pheromone_has_required_fields():
    for f in STREAMS.rglob("*.jsonl"):
        for p in read_jsonl(f):
            for k in ("schema_id","callsign","songline","tier","ts_utc",
                      "pheromone_kind","payload","hash","prev_pheromone_hash"):
                assert k in p

def test_kind_is_enumerated():                       # G6
    for f in STREAMS.rglob("*.jsonl"):
        for p in read_jsonl(f):
            assert p["pheromone_kind"] in KINDS

def test_payload_bounded_1024_bytes():
    for f in STREAMS.rglob("*.jsonl"):
        for p in read_jsonl(f):
            assert len(json.dumps(p["payload"]).encode()) <= 1024

def test_hash_reproduces():
    for f in STREAMS.rglob("*.jsonl"):
        for p in read_jsonl(f):
            body = dict(p); body["hash"] = "SELF_HASH_PLACEHOLDER"
            assert p["hash"] == sha256(canon(json.dumps(body, sort_keys=True).encode()))

def test_prev_pheromone_chain_contiguous():          # the anti-backfill property
    for f in STREAMS.rglob("*.jsonl"):
        rows = read_jsonl(f)
        assert rows[0]["prev_pheromone_hash"] is None
        for i in range(1, len(rows)):
            assert rows[i]["prev_pheromone_hash"] == rows[i-1]["hash"]

def test_ts_monotone_per_carrier():
    for f in STREAMS.rglob("*.jsonl"):
        rows = read_jsonl(f)
        assert all(rows[i]["ts_utc"] >= rows[i-1]["ts_utc"] for i in range(1,len(rows)))

def test_restricted_kinds_have_restricted_emitters():
    for f in STREAMS.rglob("*.jsonl"):
        for p in read_jsonl(f):
            if p["pheromone_kind"] == "silence_flag":
                assert p["tier"] == "world"
            if p["pheromone_kind"] == "dispatch":
                assert p["tier"] in ("world", "apex")

def test_andon_never_decays():                       # PH-6
    assert TAU["andon"] == math.inf

def test_emit_survives_slack_outage():               # PH-1
    # with Slack unreachable, emit must still land in GitHub and NOT flag silence
    with slack_unreachable():
        h = emit(heartbeat("sigrun"))
    assert h in [p["hash"] for p in read_jsonl(STREAMS/"apex"/"sigrun.jsonl")]
    assert "sigrun" not in silence_flags(now())
```

## Why it is RED today

| assertion | red reason |
|---|---|
| `test_pheromone_streams_exist` | **`state/world/pheromones/` does not exist.** No pheromone has ever been emitted by anyone. |
| `test_emit_survives_slack_outage` | there is no emit implementation, and **Claude lanes cannot post to Slack at all** — no MCP connector, no OAuth in non-interactive sessions |
| `test_prev_pheromone_chain_contiguous` | nothing to chain |

## What turns it green

1. One carrier, GitHub-only, emitting one `heartbeat` per hour. That single
   emitter turns four of these assertions green and is step 2 of the
   `CANALIZATION.md` dig order.
2. `test_emit_survives_slack_outage` needs the Slack half, which is `BLOCKED`
   (B3, bot identity) — and note it must be tested *with Slack down*, which is
   the correct way round: the outage case is the one that creates phantom silence.

## Honest flaw

The channel names these tests would eventually assert against are **three-of-six
truncated guesses** relayed from a screenshot. Any test that hardcodes
`#hfo-command-an…` is asserting against an unverified string, which is the same
defect class as a digest quoted instead of computed. Do not write that assertion
until someone with Slack access confirms the exact names.
