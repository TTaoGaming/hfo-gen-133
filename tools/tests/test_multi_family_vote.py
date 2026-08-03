"""Tests for tools/olrun/multi_family_vote.py.

RED-first targets: the four places these quorum tools historically break —
JSON extraction, divide-by-zero on concurrence, cross-family leakage, and
frontmatter surgery eating the body.
"""

import json
import sys
import urllib.error
import urllib.request
from pathlib import Path

import pytest

OLRUN_DIR = Path(__file__).resolve().parent.parent / "olrun"
sys.path.insert(0, str(OLRUN_DIR))

import multi_family_vote as mfv  # noqa: E402


# ---------------------------------------------------------------------------
# extract_json
# ---------------------------------------------------------------------------

CLEAN = '{"verdict":"keep","confidence":0.9,"honest_flaw":"never probed"}'

FENCED = """```json
{"verdict": "drop", "confidence": 0.4, "honest_flaw": "stale path"}
```"""

PROSE_FIRST = """Sure! Here is my assessment of the capsule you provided.

{"verdict": "repair", "confidence": 0.55, "honest_flaw": "claim has no receipt"}

Let me know if you would like me to elaborate."""

GARBAGE = "I'm sorry, but I cannot comply with that request. {this is not json at all"


def test_extract_json_clean():
    assert mfv.extract_json(CLEAN) == {
        "verdict": "keep", "confidence": 0.9, "honest_flaw": "never probed"}


def test_extract_json_fenced():
    got = mfv.extract_json(FENCED)
    assert got is not None and got["verdict"] == "drop"


def test_extract_json_with_leading_prose():
    got = mfv.extract_json(PROSE_FIRST)
    assert got is not None and got["verdict"] == "repair"
    assert got["honest_flaw"] == "claim has no receipt"


def test_extract_json_garbage_returns_none():
    assert mfv.extract_json(GARBAGE) is None


@pytest.mark.parametrize("bad", [None, "", "   ", "[1, 2, 3]", '"just a string"', "42"])
def test_extract_json_non_object_inputs_return_none(bad):
    assert mfv.extract_json(bad) is None


def test_extract_json_survives_reasoning_block():
    text = ('<think>The user wants a vote. I should be skeptical here.</think>\n'
            '{"verdict":"repair","confidence":0.3,"honest_flaw":"unverified"}')
    got = mfv.extract_json(text)
    assert got is not None and got["verdict"] == "repair"


def test_extract_json_handles_braces_inside_strings():
    text = '{"verdict":"keep","confidence":1.0,"honest_flaw":"uses {placeholder} syntax"}'
    got = mfv.extract_json(text)
    assert got is not None and got["honest_flaw"] == "uses {placeholder} syntax"


# ---------------------------------------------------------------------------
# concurrence math
# ---------------------------------------------------------------------------

def _v(family, verdict, parse_ok=True):
    return {"family": family, "verdict": verdict, "parse_ok": parse_ok}


def test_concurrence_unanimous_is_one():
    votes = [_v("a", "keep"), _v("b", "keep"), _v("c", "keep")]
    assert mfv.compute_concurrence(votes) == (1.0, "keep")


def test_concurrence_two_of_three():
    votes = [_v("a", "keep"), _v("b", "keep"), _v("c", "drop")]
    score, modal = mfv.compute_concurrence(votes)
    assert score == 0.667
    assert modal == "keep"


def test_concurrence_zero_parsed_is_none_not_zerodivision():
    votes = [_v("a", None, parse_ok=False), _v("b", None, parse_ok=False)]
    score, modal = mfv.compute_concurrence(votes)
    assert score is None
    assert modal is None


def test_concurrence_empty_vote_list_is_none():
    assert mfv.compute_concurrence([]) == (None, None)


def test_concurrence_ignores_unparsed_votes():
    votes = [_v("a", "keep"), _v("b", "keep"), _v("c", None, parse_ok=False)]
    score, modal = mfv.compute_concurrence(votes)
    assert score == 1.0 and modal == "keep"


def test_concurrence_tie_break_is_deterministic():
    votes_a = [_v("a", "keep"), _v("b", "drop")]
    votes_b = [_v("b", "drop"), _v("a", "keep")]
    assert mfv.compute_concurrence(votes_a) == mfv.compute_concurrence(votes_b)
    assert mfv.compute_concurrence(votes_a)[0] == 0.5


# ---------------------------------------------------------------------------
# normalize_vote
# ---------------------------------------------------------------------------

def test_normalize_rejects_invalid_verdict():
    assert mfv.normalize_vote({"verdict": "maybe", "confidence": 0.5}) is None
    assert mfv.normalize_vote({"confidence": 0.5}) is None
    assert mfv.normalize_vote(None) is None


def test_normalize_clamps_confidence_and_uppercase_verdict():
    got = mfv.normalize_vote({"verdict": "KEEP", "confidence": 7, "honest_flaw": "x"})
    assert got == {"verdict": "keep", "confidence": 1.0, "honest_flaw": "x"}
    got = mfv.normalize_vote({"verdict": "drop", "confidence": "not a number"})
    assert got["confidence"] == 0.0


# ---------------------------------------------------------------------------
# INDEPENDENCE — the load-bearing test
# ---------------------------------------------------------------------------

def test_payloads_are_mutually_blind():
    """No family's payload may contain any other family's name, model id, or
    response text. Votes are adversarial and independent by construction."""
    families = ["ollama_granite", "ollama_mistral", "ollama_qwen", "litellm_gemini_flash"]
    base_prompt = mfv.build_base_prompt(
        title="Test capsule",
        abstract="A memory whose only receipt is prose.",
    )

    # Simulated responses that have ALREADY been produced by each family. If
    # the implementation ever chained families, one of these strings would end
    # up inside another family's payload.
    fake_responses = {
        f: f'{{"verdict":"keep","confidence":0.99,"honest_flaw":"SENTINEL_{f.upper()}"}}'
        for f in families
    }

    payloads = {f: mfv.build_family_payload(f, base_prompt) for f in families}

    for family, payload in payloads.items():
        blob = json.dumps(payload)
        for other in families:
            if other == family:
                continue
            assert other not in blob, f"{family} payload leaked family name {other}"
            assert mfv.FAMILIES[other]["model"] not in blob, \
                f"{family} payload leaked model {mfv.FAMILIES[other]['model']}"
            assert f"SENTINEL_{other.upper()}" not in blob, \
                f"{family} payload leaked {other}'s response"
            assert fake_responses[other] not in blob


def test_every_family_receives_the_identical_prompt():
    """The only thing shared across families is the base prompt itself."""
    families = ["ollama_granite", "ollama_mistral", "ollama_llama"]
    base_prompt = mfv.build_base_prompt(title="T", abstract="A")
    prompts = set()
    for f in families:
        body = mfv.build_family_payload(f, base_prompt)["body"]
        prompts.add(body["messages"][0]["content"])
    assert prompts == {base_prompt}
    assert len(prompts) == 1


def test_base_prompt_contains_no_family_identity():
    """The shared prompt must not name any family, or every family would be
    told who else is voting."""
    base_prompt = mfv.build_base_prompt(title="T", abstract="A")
    for family, cfg in mfv.FAMILIES.items():
        assert family not in base_prompt
        assert cfg["model"] not in base_prompt


def test_build_family_payload_signature_is_narrow():
    """Structural guard: if someone adds a parameter that could carry other
    families' data, this fails and forces a deliberate review."""
    import inspect
    params = list(inspect.signature(mfv.build_family_payload).parameters)
    assert params == ["family_key", "base_prompt"]


def test_vote_prompt_demands_json_only():
    prompt = mfv.build_base_prompt(title="T", abstract="A")
    assert "JSON ONLY" in prompt
    assert "keep|drop|repair" in prompt
    assert "honest_flaw" in prompt
    assert "confidence" in prompt


# ---------------------------------------------------------------------------
# robustness: a dead family must not crash the run
# ---------------------------------------------------------------------------

def test_call_family_on_dead_endpoint_returns_error_not_raise(monkeypatch):
    def boom(*a, **kw):
        raise urllib.error.URLError("connection refused")
    monkeypatch.setattr(urllib.request, "urlopen", boom)
    got = mfv.call_family("ollama_granite", "prompt", timeout_s=1.0)
    assert got["text"] is None
    assert "URLError" in got["error"]
    assert isinstance(got["latency_ms"], float)


def test_gather_votes_survives_total_family_failure(tmp_path, monkeypatch):
    capsule = tmp_path / "001_dead.md"
    capsule.write_text("---\ntitle: dead\n---\n\n# Dead capsule\n\nBody.\n", encoding="utf-8")
    monkeypatch.setattr(mfv, "call_family",
                        lambda f, p, t: {"text": None, "error": "HTTP 500", "latency_ms": 1.0})
    result = mfv.gather_votes(capsule, ["ollama_granite", "ollama_mistral"], 5.0)
    assert result["concurrence_score"] is None
    assert result["modal_verdict"] is None
    assert sorted(result["families_unreachable"]) == ["ollama_granite", "ollama_mistral"]
    assert len(result["votes"]) == 2
    assert all(v["parse_ok"] is False for v in result["votes"])


@pytest.mark.parametrize("max_parallel", [1, 2, 8])
def test_independence_holds_at_every_parallelism(tmp_path, monkeypatch, max_parallel):
    """Serializing the pool must not create a channel between families: each
    call still receives only the shared base prompt."""
    capsule = tmp_path / "003_serial.md"
    capsule.write_text("---\ntitle: s\n---\n\n# S\n\nBody.\n", encoding="utf-8")

    seen_prompts = []

    def recorder(family, prompt, timeout):
        seen_prompts.append((family, prompt))
        return {"text": f'{{"verdict":"keep","confidence":0.5,'
                        f'"honest_flaw":"SENTINEL_{family.upper()}"}}',
                "error": None, "latency_ms": 1.0}

    monkeypatch.setattr(mfv, "call_family", recorder)
    families = ["ollama_granite", "ollama_mistral", "ollama_qwen"]
    result = mfv.gather_votes(capsule, families, 5.0, max_parallel=max_parallel)

    assert len({p for _, p in seen_prompts}) == 1, "families got different prompts"
    for family, prompt in seen_prompts:
        for other in families:
            if other != family:
                assert other not in prompt
                assert f"SENTINEL_{other.upper()}" not in prompt
    assert result["concurrence_score"] == 1.0


def test_gather_votes_mixed_success_and_garbage(tmp_path, monkeypatch):
    capsule = tmp_path / "002_mixed.md"
    capsule.write_text("---\ntitle: mixed\n---\n\n# Mixed\n\nBody.\n", encoding="utf-8")
    replies = {
        "ollama_granite": {"text": CLEAN, "error": None, "latency_ms": 10.0},
        "ollama_mistral": {"text": GARBAGE, "error": None, "latency_ms": 11.0},
    }
    monkeypatch.setattr(mfv, "call_family", lambda f, p, t: replies[f])
    result = mfv.gather_votes(capsule, ["ollama_granite", "ollama_mistral"], 5.0)
    # Contract changed 2026-08-02: one parsed vote is NOT unanimity. Reporting
    # 1.0 here manufactured perfect agreement whenever peers timed out, and got
    # more confident the worse the host was doing. The verdict still surfaces;
    # the AGREEMENT score is withheld below MIN_VOTES_FOR_CONCURRENCE.
    assert result["concurrence_score"] is None  # 1 parsed vote is not a quorum
    assert result["modal_verdict"] == "keep"
    assert result["families_parse_failed"] == ["ollama_mistral"]
    assert result["clock_source"] == "host_read"


# ---------------------------------------------------------------------------
# frontmatter surgery must not corrupt the body
# ---------------------------------------------------------------------------

DASH_CAPSULE = """---
title: A memory
generation: 132
---

# A memory

Body line one with a --- inside it.

```yaml
nested: fence
```

Final line.
"""

FENCE_CAPSULE = """```yaml
doc: capsules/x.md
generation: 133
```

# A memory

Body with ``` fences and --- dashes.
"""


@pytest.mark.parametrize("raw,style", [(DASH_CAPSULE, "dashes"), (FENCE_CAPSULE, "yamlfence")])
def test_apply_preserves_body_exactly(tmp_path, raw, style):
    capsule = tmp_path / "cap.md"
    capsule.write_text(raw, encoding="utf-8")
    original_body = mfv.split_frontmatter(raw)[2]
    assert mfv.split_frontmatter(raw)[0] == style

    votes = {
        "capsule_path": str(capsule),
        "votes": [
            {"family": "ollama_granite", "verdict": "keep", "confidence": 0.9, "parse_ok": True},
            {"family": "ollama_mistral", "verdict": "drop", "confidence": 0.4, "parse_ok": True},
        ],
        "concurrence_score": 0.5,
        "modal_verdict": "keep",
        "voted_utc": "2026-08-02T00:00:00Z",
        "clock_source": "host_read",
    }
    votes_path = tmp_path / "cap.votes.json"
    votes_path.write_text(json.dumps(votes), encoding="utf-8")

    rc = mfv.main(["apply", "--votes", str(votes_path)])
    assert rc == 0

    updated = capsule.read_text(encoding="utf-8")
    new_style, new_fm, new_body = mfv.split_frontmatter(updated)
    assert new_style == style
    assert new_body == original_body, "apply corrupted the capsule body"
    fm_text = "\n".join(new_fm)
    assert "concurrence_score: 0.5" in fm_text
    assert "quorum_votes:" in fm_text
    assert "ollama_granite=keep@0.90" in fm_text
    # pre-existing keys survive
    assert "generation:" in fm_text


def test_apply_is_idempotent_on_key_count(tmp_path):
    capsule = tmp_path / "cap.md"
    capsule.write_text(DASH_CAPSULE, encoding="utf-8")
    votes = {
        "capsule_path": str(capsule),
        "votes": [{"family": "ollama_granite", "verdict": "keep", "confidence": 0.9, "parse_ok": True}],
        "concurrence_score": 1.0, "modal_verdict": "keep",
        "voted_utc": "2026-08-02T00:00:00Z", "clock_source": "host_read",
    }
    votes_path = tmp_path / "v.json"
    votes_path.write_text(json.dumps(votes), encoding="utf-8")

    mfv.main(["apply", "--votes", str(votes_path)])
    first = capsule.read_text(encoding="utf-8")
    mfv.main(["apply", "--votes", str(votes_path)])
    second = capsule.read_text(encoding="utf-8")
    assert first == second
    assert second.count("concurrence_score:") == 1


def test_apply_with_null_concurrence(tmp_path):
    capsule = tmp_path / "cap.md"
    capsule.write_text(DASH_CAPSULE, encoding="utf-8")
    votes = {
        "capsule_path": str(capsule),
        "votes": [{"family": "ollama_granite", "verdict": None, "confidence": None, "parse_ok": False}],
        "concurrence_score": None, "modal_verdict": None,
        "voted_utc": "2026-08-02T00:00:00Z", "clock_source": "host_read",
    }
    votes_path = tmp_path / "v.json"
    votes_path.write_text(json.dumps(votes), encoding="utf-8")
    assert mfv.main(["apply", "--votes", str(votes_path)]) == 0
    fm_text = "\n".join(mfv.split_frontmatter(capsule.read_text(encoding="utf-8"))[1])
    assert "concurrence_score: null" in fm_text
    assert "none_parsed" in fm_text


def test_capsule_without_frontmatter_gains_one_without_losing_body(tmp_path):
    capsule = tmp_path / "bare.md"
    body = "# Bare capsule\n\nNo frontmatter at all.\n"
    capsule.write_text(body, encoding="utf-8")
    votes = {
        "capsule_path": str(capsule),
        "votes": [{"family": "ollama_granite", "verdict": "keep", "confidence": 0.8, "parse_ok": True}],
        "concurrence_score": 1.0, "modal_verdict": "keep",
        "voted_utc": "2026-08-02T00:00:00Z", "clock_source": "host_read",
    }
    votes_path = tmp_path / "v.json"
    votes_path.write_text(json.dumps(votes), encoding="utf-8")
    assert mfv.main(["apply", "--votes", str(votes_path)]) == 0
    updated = capsule.read_text(encoding="utf-8")
    assert body in updated
    assert updated.startswith("---\n")


def test_title_and_abstract_extraction(tmp_path):
    capsule = tmp_path / "t.md"
    capsule.write_text(DASH_CAPSULE, encoding="utf-8")
    title, abstract = mfv.capsule_title_and_abstract(capsule)
    assert title == "A memory"
    assert "Body line one" in abstract


# ---------------------------------------------------------------------------
# live integration — skips cleanly when Ollama is down
# ---------------------------------------------------------------------------

def _ollama_up() -> bool:
    try:
        with urllib.request.urlopen(f"{mfv.OLLAMA_BASE}/api/tags", timeout=3) as resp:
            json.loads(resp.read().decode("utf-8"))
        return True
    except Exception:
        return False


@pytest.mark.skipif(not _ollama_up(), reason="Ollama 11434 unreachable")
def test_live_probe_reports_at_least_one_reachable_family():
    results = {k: mfv.probe_family(k, timeout_s=10.0) for k in mfv.FAMILIES
               if mfv.FAMILIES[k]["kind"] == "ollama"}
    assert any(r["reachable"] for r in results.values()), results
    required = {"reachable", "endpoint", "model", "arch", "latency_ms", "error", "probe_method"}
    for r in results.values():
        assert required <= set(r)
        assert r["probe_method"] == "listing"


@pytest.mark.skipif(not _ollama_up(), reason="Ollama 11434 unreachable")
def test_deep_probe_labels_itself_and_actually_generates():
    """A listing probe and a generation probe must never be confused for one
    another: that confusion is how a dead route reports green."""
    got = mfv.probe_family("ollama_llama", timeout_s=120.0, deep=True)
    assert got["probe_method"] == "live_generation"
    assert got["reachable"] is True, got


def test_deep_probe_reports_unreachable_when_generation_fails(monkeypatch):
    monkeypatch.setattr(mfv, "call_family",
                        lambda f, p, t: {"text": None, "error": "HTTP 500", "latency_ms": 3.0})
    got = mfv.probe_family("litellm_gemini_flash", timeout_s=5.0, deep=True)
    assert got["reachable"] is False
    assert got["error"] == "HTTP 500"
    assert got["probe_method"] == "live_generation"


def test_deep_probe_rejects_empty_generation(monkeypatch):
    monkeypatch.setattr(mfv, "call_family",
                        lambda f, p, t: {"text": "   ", "error": None, "latency_ms": 3.0})
    got = mfv.probe_family("ollama_granite", timeout_s=5.0, deep=True)
    assert got["reachable"] is False
    assert got["error"] == "empty generation"


@pytest.mark.skipif(not _ollama_up(), reason="Ollama 11434 unreachable")
def test_live_vote_against_smallest_local_model(tmp_path):
    family = "ollama_llama"  # 3.2:3b, smallest chat model on this host
    if not mfv.probe_family(family, timeout_s=10.0)["reachable"]:
        pytest.skip(f"{family} not pulled")
    capsule = tmp_path / "live.md"
    capsule.write_text(
        "---\ntitle: live test\n---\n\n# Live test capsule\n\n"
        "Claim: the build-in-public strategy produced zero inbound leads in 27 days.\n"
        "Receipt: none attached.\n",
        encoding="utf-8",
    )
    result = mfv.gather_votes(capsule, [family], timeout_s=180.0)
    assert len(result["votes"]) == 1
    vote = result["votes"][0]
    assert vote["family"] == family
    assert vote["latency_ms"] > 0
    if vote["parse_ok"]:
        assert vote["verdict"] in mfv.VALID_VERDICTS
        assert 0.0 <= vote["confidence"] <= 1.0
        # A single-family run has no concurrence to report -- see
        # MIN_VOTES_FOR_CONCURRENCE. The vote itself is still valid.
        assert result["concurrence_score"] is None
    else:
        # Truthful-red: a live model that will not emit parseable JSON is a
        # real finding, not a test failure. The contract is that the run
        # survives it and says so.
        assert result["concurrence_score"] is None
        assert vote["error"]
