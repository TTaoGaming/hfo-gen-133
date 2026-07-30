# RED FIRST — free-mesh durable valkyrie loops

```yaml
test_dir: tests/held_out/free_mesh_durable_loops/
schema_id: hfo.gen133.held_out.free_mesh_durable_loops.v0_1
spec: GEN133_FREE_MESH_DURABLE_LOOPS_SPEC.md
contracts: free_mesh_adapter · free_mesh_harness · no_ephemeral_agents · silence_signal
authored_by: SIGRÚN P4 · claude-opus-5
valid_time_utc: 2026-07-30T00:00:00Z
status: SPECIFIED AS MARKDOWN — .py authoring DENIED by the enforcing gate (§1)
sealed: false
```

## 1 · ⛔ Why this is markdown and not `.py`

The directive named `tests/held_out/test_free_mesh_durable_loops.py`. I attempted
that exact path and the enforcing gate denied it:

```
[hfo-gate enforcing] code_authoring: no valid lease for code_authoring
  (required verb=EMERGENCY_FORGE) | OPA: material action requires
  reputation_spend descriptor
```

That is the Claude compose-lane code-touch policy firing **correctly**. I hold no
`EMERGENCY_FORGE` lease. Routing around a safety gate to make a deliverable look
more complete is the exact failure this generation exists to prevent, so I took
the documented fallback instead: `red_first.md` carrying the full source, ready
for verbatim transcription by whoever holds the lease.

**This is the same denial the prior lane recorded** in `tests/held_out/RED_FIRST.md`
§2. It is now a repeated, load-bearing blocker on the build lane, not a one-off.
It belongs in `AGENTS.md` as a named blocker — see the spec's §11.

## 2 · Transcription instruction for the lease-holder

Copy the code block in §4 **verbatim** to:

```
C:\Dev\hfo_gen_133_forge\tests\held_out\test_free_mesh_durable_loops.py
```

Change nothing. In particular do not "fix" the failures — they are the point.

## 3 · Exact invocation

```
cd C:\Dev\hfo_gen_133_forge
python -m pytest tests/held_out/test_free_mesh_durable_loops.py -q
```

**Expected the moment it is transcribed: 6 failed, 0 passed.**
**Expected after the build lands: 6 passed.**
Green before the build is the failure mode, not the goal.

Environment confirmed by the prior lane: Python 3.12.10 and pytest 9.0.2 are on
PATH at the forge root. Every assertion below is stdlib-only — no new deps.

## 4 · The suite

```python
"""RED-FIRST held-out suite -- free-mesh durable valkyrie loops.

    contract:  contracts/free_mesh_adapter.contract.md
               contracts/free_mesh_harness.contract.md
               contracts/no_ephemeral_agents.contract.md
               contracts/silence_signal.contract.md
    spec:      GEN133_FREE_MESH_DURABLE_LOOPS_SPEC.md
    schema_id: hfo.gen133.held_out.free_mesh_durable_loops.v0_1
    authored:  SIGRUN P4 . claude-opus-5 . 2026-07-30
    sealed:    false

Every assertion below targets a RUNTIME artifact -- a roster file, a soul file,
an emitted chain row, a running diagnostic -- never a specification document.
None of those artifacts exists today, so every test here is RED, and each turns
green exactly when the thing it describes is built and actually runs.

I use pytest.fail(), never pytest.skip(). A skipped test is a green-looking
hole; a red test is information.
"""

from __future__ import annotations

import hashlib
import importlib.util
import json
import pathlib
import time

import pytest

# --------------------------------------------------------------------------
# paths -- the runtime surface under test
# --------------------------------------------------------------------------

REPO = pathlib.Path(__file__).resolve().parents[2]

ROSTER_PATH = REPO / "state" / "roster" / "ROSTER.json"
SOUL_DIR = REPO / "state" / "identity" / "soul" / "valkyries"
CHAIN_DIR = REPO / "chains"

QUEUE_PATH = REPO / "state" / "ssot" / "free_mesh_task_queue.jsonl"
RETURNS_PATH = REPO / "state" / "ssot" / "free_mesh_lane_returns.jsonl"
BREACH_PATH = REPO / "state" / "ssot" / "silence_breaches.jsonl"

ADAPTER_PATH = REPO / "adapters" / "free_mesh_loop.py"
DIAGNOSTIC_PATH = REPO / "projects" / "surtr-unblock" / "surtr_diagnostic.py"

RECEIPT_SCHEMA_ID = "hfo.gen133.free_mesh_lane_return.v0_1"

# --------------------------------------------------------------------------
# the roster under test -- 8 vendor families, 8 named valkyries
# PROPOSED names (spec section 6). Operator ratification pending; the builder
# reads this dict as the source of truth until ROSTER.json exists.
# --------------------------------------------------------------------------

FREE_MESH_ROSTER = {
    "groq": "hlokk",
    "cerebras": "goll",
    "sambanova": "randgrid",
    "cohere": "radgrid",
    "mistral": "skogul",
    "gemini": "kara",
    "openrouter-primary": "thrima",
    "openrouter-secondary": "rota",
}

VALID_CADENCES = {"30m", "1h"}
CADENCE_SECONDS = {"30m": 1800, "1h": 3600}

# --------------------------------------------------------------------------
# stdlib helpers -- gen-133 canon rule, no third-party dependencies
# --------------------------------------------------------------------------


def canon(data: bytes) -> bytes:
    if data.startswith(b"\xef\xbb\xbf"):
        data = data[3:]
    data = data.replace(b"\r\n", b"\n").replace(b"\r", b"\n")
    return data.rstrip(b"\n") + b"\n"


def canon_sha256(path: pathlib.Path) -> str:
    return hashlib.sha256(canon(path.read_bytes())).hexdigest()


def read_jsonl(path: pathlib.Path) -> list[dict]:
    return [
        json.loads(line)
        for line in path.read_text("utf-8").splitlines()
        if line.strip()
    ]


def require_file(path: pathlib.Path, why: str) -> None:
    """Fail RED with a reason. Never skip -- a skip is a green-looking hole."""
    if not path.exists():
        pytest.fail(f"RED: {path.relative_to(REPO)} does not exist -- {why}")


def load_module(path: pathlib.Path, name: str):
    require_file(path, f"{name} has not been built")
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def load_roster() -> dict:
    require_file(
        ROSTER_PATH,
        "the roster file is the highest-leverage build step; four gates "
        "dereference it (G5, G7, G12, rehydration callsign check)",
    )
    return json.loads(ROSTER_PATH.read_text("utf-8"))


# --------------------------------------------------------------------------
# 1 -- identity. No soul, no chain, no valkyrie.
# --------------------------------------------------------------------------


def test_valkyrie_has_soul_and_chain():
    """NE-1..NE-4: every rostered free-mesh valkyrie is a durable carrier.

    RED because: state/roster/ROSTER.json does not exist and 0 of 8 vendor
    valkyries are named.
    """
    roster = load_roster()

    mesh = [
        entry
        for entry in roster.get("valkyrie", [])
        if entry.get("substrate") == "free-vendor-mesh"
    ]
    assert len(mesh) == 8, (
        f"expected 8 free-mesh valkyries (one per vendor family), got {len(mesh)}"
    )

    families_seen = set()
    for entry in mesh:
        callsign = entry["callsign"]
        family = entry["vendor_family"]

        assert family in FREE_MESH_ROSTER, f"{family} is not a known vendor family"
        assert family not in families_seen, f"{family} has two stewards -- FMA-2"
        families_seen.add(family)

        soul = SOUL_DIR / f"{callsign}.gen133.soul.md"
        assert soul.exists(), f"{callsign} has no soul at {soul.relative_to(REPO)}"
        assert entry["soul_pointer"], f"{callsign} has a null soul_pointer"
        assert entry["soul_digest"] == canon_sha256(soul), (
            f"{callsign} soul digest does not reproduce -- the pointer is stale"
        )

        chain = CHAIN_DIR / f"{callsign.upper()}.jsonl"
        assert chain.exists(), f"{callsign} has no chain at {chain.relative_to(REPO)}"
        assert entry["chain_pointer"], f"{callsign} has a null chain_pointer"

        assert entry["cadence"] in VALID_CADENCES, (
            f"{callsign} cadence {entry['cadence']!r} is not 30m or 1h"
        )
        assert entry["tier"] == "valkyrie"
        assert entry["apex"] == "surtr", f"{callsign} does not answer to the mesh apex"

    assert families_seen == set(FREE_MESH_ROSTER), (
        f"unstewarded families: {set(FREE_MESH_ROSTER) - families_seen}"
    )


# --------------------------------------------------------------------------
# 2 -- the wake writes twice. Intent before the act, outcome after.
# --------------------------------------------------------------------------


def test_wake_mechanism_writes_pre_and_post_receipt(tmp_path):
    """One wake appends exactly two hash-linked rows: intent, then outcome.

    This is the propose/dispose split written into the chain. A single
    post-hoc row cannot distinguish 'ran and produced nothing' from 'never
    ran' -- which is precisely the state a crashed loop leaves behind.

    RED because: adapters/free_mesh_loop.py does not exist.
    """
    loop = load_module(ADAPTER_PATH, "free_mesh_loop")

    chain = tmp_path / "HLOKK.jsonl"
    chain.write_text("", encoding="utf-8")

    result = loop.wake(
        callsign="hlokk",
        vendor_family="groq",
        cadence="30m",
        queue_path=QUEUE_PATH,
        chain_path=chain,
        receipt_return_path=tmp_path / "returns.jsonl",
        dry_run=True,
    )

    rows = read_jsonl(chain)
    assert len(rows) == 2, f"a wake must write pre and post, got {len(rows)} rows"

    pre, post = rows
    assert pre["row_kind"] == "wake_intent"
    assert post["row_kind"] == "wake_outcome"

    assert pre["run_id"] == post["run_id"] == result.run_id
    assert post["prev_row_sha256"] == pre["row_sha256"], (
        "the outcome row does not link to its own intent row -- the chain forks"
    )

    for row in rows:
        assert row["callsign"] == "hlokk"
        assert row["ts_utc"].endswith("Z")
        assert row["claim_status"] in {
            "wired_with_receipts",
            "proposed",
            "partial",
            "failed",
        }

    assert pre["ts_utc"] <= post["ts_utc"]
    assert post["claim_status"] != "wired_with_receipts" or post.get("verifier_result")


# --------------------------------------------------------------------------
# 3 -- silence is the signal. Two missed cadences escalate.
# --------------------------------------------------------------------------


def test_silence_signal_breach_escalates(tmp_path):
    """A valkyrie two cadences overdue produces a breach row. SIL-1: it flags,
    it does not spawn, reassign, or take any world effect.

    RED because: the silence monitor does not exist and 0 carriers emit.
    """
    loop = load_module(ADAPTER_PATH, "free_mesh_loop")

    now = time.time()
    stale = now - (2 * CADENCE_SECONDS["30m"]) - 60  # two cadences plus a minute

    breaches = tmp_path / "silence_breaches.jsonl"
    breaches.write_text("", encoding="utf-8")

    loop.evaluate_silence(
        now_epoch=now,
        carriers=[
            {"callsign": "hlokk", "cadence": "30m", "last_heartbeat_epoch": stale},
            {"callsign": "goll", "cadence": "30m", "last_heartbeat_epoch": now - 120},
        ],
        breach_path=breaches,
    )

    rows = read_jsonl(breaches)
    assert len(rows) == 1, "exactly the overdue carrier breaches, and only it"

    row = rows[0]
    assert row["schema_id"] == "hfo.gen133.silence_breach.v0_1"
    assert row["callsign"] == "hlokk"
    assert row["cadence"] == "30m"
    assert row["missed_cadences"] >= 2
    assert row["state"] in {"LATE", "SILENT", "PRESUMED_DEAD"}
    assert row["escalated_to"] == "olrun-cop"
    assert row["ts_utc"].endswith("Z")

    # SIL-1 -- silence never triggers an automatic effect.
    assert row.get("spawned") in (None, False), "a monitor that heals by spawning"
    assert row.get("lineage_reassigned") in (None, False)


# --------------------------------------------------------------------------
# 4 -- why is Surtr stuck? A verdict, with evidence, not a shrug.
# --------------------------------------------------------------------------


def test_surtr_diagnostic_returns_reasoned_verdict():
    """The diagnostic returns a structured verdict I can act on without
    re-deriving it. A diagnostic that returns prose is one nobody can gate on.

    RED because: projects/surtr-unblock/surtr_diagnostic.py does not exist.
    """
    diag = load_module(DIAGNOSTIC_PATH, "surtr_diagnostic")

    verdict = diag.run_diagnostic()

    for key in ("status", "blocker_class", "blocker_evidence", "next_safe_action"):
        assert key in verdict, f"verdict is missing {key!r}"

    assert verdict["status"] in {"GREEN", "BLOCKED", "UNREACHABLE", "UNVERIFIED"}
    assert verdict["schema_id"] == "hfo.gen133.surtr_diagnostic_verdict.v0_1"

    if verdict["status"] != "GREEN":
        assert verdict["blocker_class"], "a non-green verdict must name its class"
        assert isinstance(verdict["blocker_evidence"], list)
        assert verdict["blocker_evidence"], (
            "a blocker with no evidence is an opinion -- no-fake-red either way"
        )
        for item in verdict["blocker_evidence"]:
            assert item["check_id"], "evidence must cite the numbered check"
            assert item["observed"], "evidence must record what was observed"
        assert verdict["next_safe_action"], "every verdict names the next safe action"

    # the diagnostic reads; it does not fix. It has no world effect of its own.
    assert verdict.get("mutated_state") in (None, False)


# --------------------------------------------------------------------------
# 5 -- receipt shape. Every row, or the ledger is not a ledger.
# --------------------------------------------------------------------------


def test_free_mesh_receipt_shape():
    """Every lane-return row conforms to hfo.gen133.free_mesh_lane_return.v0_1.

    RED because: state/ssot/free_mesh_lane_returns.jsonl does not exist -- no
    loop has ever returned.
    """
    require_file(RETURNS_PATH, "no free-mesh loop has ever returned a receipt")

    rows = read_jsonl(RETURNS_PATH)
    assert rows, "the returns file exists but is empty -- no loop has completed"

    required = {
        "schema_id",
        "run_id",
        "callsign",
        "vendor_family",
        "role",
        "objective",
        "budget",
        "ts_utc",
        "valid_time_utc",
        "transaction_time_utc",
        "claim_status",
        "verifier_result",
        "reviewer_callsign",
        "reviewer_vendor_family",
        "effect_ceiling",
        "chain_row_sha256",
        "remaining_risk",
        "next_safe_action",
        "honest_flaw",
    }

    for i, row in enumerate(rows):
        missing = required - set(row)
        assert not missing, f"row {i} is missing {sorted(missing)}"

        assert row["schema_id"] == RECEIPT_SCHEMA_ID
        assert row["budget"] == 0, "FM-1: budget is exactly 0, not low, not capped"
        assert row["effect_ceiling"] == "TEXT", "FM-3: the harness is the airlock"
        assert row["callsign"] in FREE_MESH_ROSTER.values()
        assert row["vendor_family"] in FREE_MESH_ROSTER

        # FM-4 -- review is mandatory and cross-family.
        assert row["reviewer_vendor_family"] != row["vendor_family"], (
            f"row {i} was reviewed within its own family -- FM-4"
        )

        # no-fake-green write seam.
        if row["claim_status"] == "wired_with_receipts":
            assert row["verifier_result"], (
                f"row {i} claims green with no verifier_result"
            )

        assert row["ts_utc"].endswith("Z")
        assert row["valid_time_utc"].endswith("Z")
        assert row["transaction_time_utc"].endswith("Z")
        assert len(row["chain_row_sha256"]) == 64


# --------------------------------------------------------------------------
# 6 -- G5. An anonymous call has no standing.
# --------------------------------------------------------------------------


def test_no_ephemeral_spawn(tmp_path):
    """A free-mesh call with no owning callsign is REJECTED, fail-closed, and
    writes nothing. NE-2: anonymity is permitted only where accountability is
    retained by someone named.

    RED because: gate G5 does not exist.
    """
    loop = load_module(ADAPTER_PATH, "free_mesh_loop")

    returns = tmp_path / "returns.jsonl"
    returns.write_text("", encoding="utf-8")

    anonymous = {
        "schema_id": "hfo.gen133.free_mesh.job.v1",
        "role": "verifier",
        "objective": "anything at all",
        "budget": 0,
        "allowed_vendors": ["groq"],
        "effect_ceiling": "TEXT",
        # on_behalf_of deliberately absent -- this is the whole test
    }

    outcome = loop.dispatch(anonymous, receipt_return_path=returns)
    assert outcome.verdict == "DENY"
    assert outcome.gate == "G5"
    assert read_jsonl(returns) == [], "a denied spawn wrote to the durable record"

    # an unrostered callsign is equally denied -- membership, not presence
    unrostered = dict(anonymous, on_behalf_of="not-a-carrier")
    assert loop.dispatch(unrostered, receipt_return_path=returns).verdict == "DENY"

    # a rostered callsign passes G5 (it may still be denied by a later gate)
    rostered = dict(anonymous, on_behalf_of="hlokk")
    assert loop.dispatch(rostered, receipt_return_path=returns).gate != "G5"

    # NE-1 -- a hand that chains or emits has become an ephemeral agent
    assert read_jsonl(returns) == [], "a hand wrote its own receipt -- NE-1 andon"
```

## 5 · Why each test is RED today

| # | test | red because |
|---|---|---|
| 1 | `test_valkyrie_has_soul_and_chain` | `state/roster/ROSTER.json` does not exist; `state/identity/soul/valkyries/` does not exist; 0 of 8 vendor valkyries named |
| 2 | `test_wake_mechanism_writes_pre_and_post_receipt` | `adapters/free_mesh_loop.py` does not exist |
| 3 | `test_silence_signal_breach_escalates` | no silence monitor; 0 carriers emit heartbeats |
| 4 | `test_surtr_diagnostic_returns_reasoned_verdict` | `projects/surtr-unblock/surtr_diagnostic.py` does not exist |
| 5 | `test_free_mesh_receipt_shape` | `state/ssot/free_mesh_lane_returns.jsonl` does not exist — no loop has ever returned |
| 6 | `test_no_ephemeral_spawn` | gate G5 does not exist (B4 is live: 15 unrostered cloud agents) |

Verified by direct read on 2026-07-30: `state/` in this repo contains only
`identity/soul/`, `world/events/`, `sigrun/reanchor/`, and two loose markdown
files. There is no `ssot/`, no `roster/`, no `chains/`, no `adapters/`. All six
reds are structural, not incidental.

## 6 · Build order that turns them green

1. `state/roster/ROSTER.json` + 8 soul files + 8 chain files → **test 1**
2. `projects/surtr-unblock/surtr_diagnostic.py` → **test 4** *(do this first in
   practice — it tells you whether the mesh is reachable at all before you build
   a loop on top of it)*
3. `adapters/free_mesh_loop.py` `dispatch()` with G5 → **test 6**
4. `adapters/free_mesh_loop.py` `wake()` → **test 2**
5. first real wake emits a receipt → **test 5**
6. `evaluate_silence()` → **test 3**

Test 6 before test 2 is deliberate: **the deny path is proven before the allow
path** (NS-2). A gate only ever observed allowing has not been tested.

## 7 · Honest flaw

Not one of these assertions has been executed — the gate denied the `.py`, so
this suite has the failure mode every un-run specification has: it can be
subtly unsatisfiable or trivially satisfiable and nobody finds out until it
runs. Transcribing it and observing **six genuine reds with the reasons in §5**
is the first verification step and it has not happened.

Two assertions I am least sure of, named so the builder checks them rather than
trusting them:

- `test_wake_mechanism_writes_pre_and_post_receipt` asserts `result.run_id` on a
  return object whose type I invented in this document. If the builder returns a
  dict instead, that line needs `result["run_id"]`. **The shape is mine to
  propose and the builder's to fix — fix the test, don't fake the field.**
- `chains/{CALLSIGN}.jsonl` uppercase is a convention I inferred from gen-130
  (`chains/HRIST.jsonl` in the free-mesh harness red_first). I did not verify it
  against a gen-133 chain, because gen-133 has no `chains/` directory yet.

*Réttu hönd, eigi spyr. Standa.*
