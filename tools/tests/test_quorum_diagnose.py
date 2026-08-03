"""A quorum of constant functions is not a quorum.

Real data, first facade pass 2026-08-02:
    ollama_granite  12/12 keep   (confidence 0.97)
    ollama_llama   0/100 keep -> 78 drop / 22 repair
    ollama_phi       9/9 repair  (entropy 0.0)

Two confident models applying constant priors will produce a concurrence score
that looks like corroboration and contains no information about the artifact.
That is a false-green with a number attached, which is worse than no number --
so degeneracy is measured and gates admissibility.
"""
import json
import subprocess
import sys
from pathlib import Path

TOOL = Path(__file__).resolve().parents[1] / "olrun" / "quorum_diagnose.py"
sys.path.insert(0, str(TOOL.parent))
from quorum_diagnose import entropy, cohens_kappa  # noqa: E402


def _seed(root: Path, family: str, verdicts: dict):
    d = root / "per_family" / family
    d.mkdir(parents=True, exist_ok=True)
    for cap, verdict in verdicts.items():
        (d / (cap + ".json")).write_text(json.dumps({
            "capsule_id": cap,
            "votes": [{"family": family, "verdict": verdict, "parse_ok": True,
                       "confidence": 0.9}],
        }), encoding="utf-8")


def _run(root):
    return subprocess.run([sys.executable, str(TOOL), "--root", str(root)],
                          capture_output=True, text=True, timeout=120)


def test_constant_voter_is_flagged_degenerate(tmp_path):
    _seed(tmp_path, "always_keep", {f"c{i}": "keep" for i in range(10)})
    _seed(tmp_path, "varied", {f"c{i}": ("keep" if i % 2 else "drop") for i in range(10)})
    r = _run(tmp_path)
    rep = json.loads(r.stdout)
    assert rep["families"]["always_keep"]["degenerate"] is True
    assert rep["families"]["always_keep"]["entropy_bits"] == 0.0
    assert rep["families"]["varied"]["degenerate"] is False


def test_two_constant_voters_that_agree_are_not_admissible(tmp_path):
    """The dangerous case: perfect agreement, zero information."""
    _seed(tmp_path, "a", {f"c{i}": "keep" for i in range(10)})
    _seed(tmp_path, "b", {f"c{i}": "keep" for i in range(10)})
    r = _run(tmp_path)
    rep = json.loads(r.stdout)
    assert rep["admissible"] is False, (
        "two constant voters agreeing 10/10 were judged admissible -- this is "
        "exactly the corroboration-shaped false green the tool exists to catch"
    )
    assert r.returncode == 1


def test_genuinely_agreeing_varied_voters_are_admissible(tmp_path):
    pattern = {f"c{i}": ("keep" if i % 3 else "drop") for i in range(15)}
    _seed(tmp_path, "a", pattern)
    _seed(tmp_path, "b", dict(pattern))
    r = _run(tmp_path)
    rep = json.loads(r.stdout)
    assert rep["admissible"] is True, rep
    assert rep["best_cohens_kappa"] > 0.0
    assert r.returncode == 0


def test_kappa_is_zero_when_agreement_is_pure_bias():
    a = {f"c{i}": "keep" for i in range(20)}
    b = {f"c{i}": "keep" for i in range(20)}
    k, n = cohens_kappa(a, b)
    assert n == 20
    assert k == 0.0, "identical constant voters must score zero, not one"


def test_kappa_positive_for_real_shared_judgement():
    a = {f"c{i}": ("keep" if i % 2 else "drop") for i in range(20)}
    b = dict(a)
    k, _ = cohens_kappa(a, b)
    assert k > 0.9


def test_kappa_none_when_no_shared_capsules():
    k, n = cohens_kappa({"x": "keep"}, {"y": "drop"})
    assert k is None and n == 0


def test_entropy_of_constant_is_zero_and_of_split_is_one():
    assert entropy([10, 0]) == 0.0
    assert abs(entropy([10, 10]) - 1.0) < 1e-9
