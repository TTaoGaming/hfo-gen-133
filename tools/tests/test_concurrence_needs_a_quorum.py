"""Held-out regression: a single surviving vote is not unanimity.

Caught live 2026-08-02 on a real capsule. Two of three families timed out; the
one that answered said `drop`, and the run reported:

    concurrence_score: 1.0   modal_verdict: drop

Read literally that says "every family agreed." What actually happened is that
one small local model answered while its peers fell over. Under load, the models
most likely to time out are the slow careful ones, so this failure mode
systematically manufactures perfect agreement out of infrastructure flakiness --
and it gets MORE confident the worse the host is doing.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "olrun"))
from multi_family_vote import compute_concurrence, MIN_VOTES_FOR_CONCURRENCE  # noqa: E402


def _v(family, verdict, parse_ok=True):
    return {"family": family, "verdict": verdict, "parse_ok": parse_ok}


def test_single_parsed_vote_yields_no_concurrence_score():
    votes = [
        _v("ollama_granite", None, parse_ok=False),
        _v("ollama_mistral", None, parse_ok=False),
        _v("ollama_llama", "drop"),
    ]
    score, modal = compute_concurrence(votes)
    assert score is None, (
        "one vote reported as concurrence=%r -- fabricated unanimity from a "
        "quorum that did not happen" % (score,)
    )
    assert modal == "drop", "the surviving verdict should still be surfaced"


def test_zero_parsed_votes_is_none_not_zero():
    score, modal = compute_concurrence([_v("a", None, False), _v("b", None, False)])
    assert score is None and modal is None


def test_two_agreeing_votes_do_score():
    score, modal = compute_concurrence([_v("a", "keep"), _v("b", "keep")])
    assert score == 1.0 and modal == "keep"


def test_two_disagreeing_votes_score_half():
    score, modal = compute_concurrence([_v("a", "keep"), _v("b", "drop")])
    assert score == 0.5


def test_three_way_split_is_reported_as_contested():
    score, _ = compute_concurrence([_v("a", "keep"), _v("b", "drop"), _v("c", "repair")])
    assert score is not None and score < 0.5


def test_threshold_is_at_least_two():
    assert MIN_VOTES_FOR_CONCURRENCE >= 2, (
        "a quorum of one is not a quorum"
    )


def test_single_family_sweep_exits_zero(tmp_path):
    """Exit status tracks 'did a vote come back', not 'was there a quorum'.

    Keying exit on concurrence_score reported every deliberate single-family
    sweep as ok=0/100 while writing 100 good vote files -- a green run
    misreported as total failure, which trains an operator to ignore exit codes.
    """
    import subprocess
    capsule = tmp_path / "000_probe.md"
    capsule.write_text("---\ntitle: probe\n---\n\n# Probe\n\nBody.\n", encoding="utf-8")
    out = tmp_path / "v.json"
    r = subprocess.run(
        [sys.executable,
         str(Path(__file__).resolve().parents[1] / "olrun" / "multi_family_vote.py"),
         "vote", "--capsule", str(capsule), "--families", "ollama_llama",
         "--out", str(out), "--max-parallel", "1", "--timeout", "150"],
        capture_output=True, text=True, timeout=300,
        cwd=str(Path(__file__).resolve().parents[2]))
    if not out.exists():
        import pytest
        pytest.skip("local Ollama unavailable")
    import json as _json
    data = _json.loads(out.read_text(encoding="utf-8"))
    if not any(v.get("parse_ok") for v in data["votes"]):
        import pytest
        pytest.skip("model returned no parseable vote")
    assert data["concurrence_score"] is None, "one family cannot have concurrence"
    assert r.returncode == 0, (
        "single-family run with a parsed vote exited %d -- a good run reported "
        "as failure" % r.returncode
    )


def test_timeouts_cannot_manufacture_agreement_as_load_increases():
    """The perverse-incentive property: more failures must not mean more confidence."""
    full = [_v("a", "keep"), _v("b", "drop"), _v("c", "repair")]
    degraded = [_v("a", "keep"), _v("b", None, False), _v("c", None, False)]
    full_score, _ = compute_concurrence(full)
    degraded_score, _ = compute_concurrence(degraded)
    assert not (degraded_score is not None and full_score is not None
                and degraded_score > full_score), (
        "losing votes raised the agreement score from %r to %r"
        % (full_score, degraded_score)
    )
