"""Held-out regression: a relay may lose precision, never bad news.

Caught live 2026-08-02: poll_and_relay read only `rows[-3:]` of a JSONL, so a
`claim_status: failed` older than the last 3 rows was invisible to the operator
and the headline read "no failed claim_status" over a chain holding four of them.

A chain is append-only. Tail-only reading means the relay gets *greener* as more
work is appended -- the failure mode is silent, monotonic, and undetectable from
the relay alone, which is exactly why it needs a test rather than a code comment.
"""
import json
import subprocess
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
TOOL = REPO / "tools" / "olrun" / "poll_and_relay.py"


def _chain(tmp_path, n_benign_tail=8):
    """A chain whose ONLY failure sits far outside any tail window."""
    rows = [{
        "row_id": 1, "ts_utc": "2026-08-02T00:00:00Z", "actor": "test",
        "action": "the_buried_failure", "claim_status": "failed",
        "honest_flaw": "BURIED_RED_MARKER",
        "verifier_result": "deliberately placed at the head of the chain",
    }]
    for i in range(n_benign_tail):
        rows.append({
            "row_id": i + 2, "ts_utc": "2026-08-02T00:00:00Z", "actor": "test",
            "action": "benign_%d" % i, "claim_status": "wired_with_receipts",
            "verifier_result": "exit 0",
        })
    p = tmp_path / "chain.jsonl"
    p.write_text("".join(json.dumps(r) + "\n" for r in rows), encoding="utf-8")
    return p


def _run(chain, out):
    return subprocess.run(
        [sys.executable, str(TOOL), "poll", "--sources", str(chain), "--out", str(out)],
        capture_output=True, text=True, cwd=str(REPO), timeout=120,
    )


def test_failed_status_survives_even_when_buried_at_head(tmp_path):
    chain = _chain(tmp_path, n_benign_tail=8)
    out = tmp_path / "relay.md"
    r = _run(chain, out)
    assert r.returncode == 0, r.stderr
    text = out.read_text(encoding="utf-8")
    assert "failed" in text, (
        "relay dropped a claim_status:failed buried before the tail window.\n" + text
    )
    assert "no failed claim_status" not in text, (
        "relay AFFIRMED absence of failures over a chain containing one -- "
        "this is the reward-hacked-summarization mode.\n" + text
    )


def test_honest_flaw_survives_compression(tmp_path):
    chain = _chain(tmp_path, n_benign_tail=8)
    out = tmp_path / "relay.md"
    assert _run(chain, out).returncode == 0
    assert "BURIED_RED_MARKER" in out.read_text(encoding="utf-8"), (
        "an honest_flaw present in a source did not survive into the relay"
    )


def test_relay_does_not_get_greener_as_benign_rows_are_appended(tmp_path):
    """The monotonicity property: appending good news must not hide old bad news."""
    verdicts = []
    for tail in (2, 8, 40):
        chain = _chain(tmp_path / ("t%d" % tail), n_benign_tail=tail) \
            if (tmp_path / ("t%d" % tail)).mkdir(parents=True, exist_ok=True) is None else None
        out = tmp_path / ("t%d" % tail) / "relay.md"
        assert _run(chain, out).returncode == 0
        verdicts.append("failed" in out.read_text(encoding="utf-8"))
    assert all(verdicts), (
        "relay lost the failure as benign rows accumulated: %r "
        "(tail sizes 2/8/40) -- bad news must not decay with volume" % (verdicts,)
    )


def test_word_budget_still_respected(tmp_path):
    """Preserving reds must not blow the compression budget the operator relies on."""
    chain = _chain(tmp_path, n_benign_tail=40)
    out = tmp_path / "relay.md"
    assert _run(chain, out).returncode == 0
    assert len(out.read_text(encoding="utf-8").split()) < 400
