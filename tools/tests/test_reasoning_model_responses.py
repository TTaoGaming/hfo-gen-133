"""Reasoning models answer in `thinking`, not `content`.

Field evidence 2026-08-02: qwen3.5:9b scored 8/8 parse failures with `raw: ''`
while Ollama reported done_reason=stop and eval_count=34 -- the model answered
correctly every time and the tool discarded the answer, because it read only
`message.content` and qwen puts its JSON in `thinking`.

This is not a cosmetic parsing bug. Reasoning models are the ones most likely to
give a non-constant verdict, so dropping them biased the quorum toward exactly
the degenerate rubber-stamp voters that `quorum_diagnose.py` then flagged. A
silent read failure is indistinguishable downstream from a model that refused to
answer.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "olrun"))
from multi_family_vote import _extract_text  # noqa: E402

JSON = '{"verdict":"keep","confidence":0.5,"honest_flaw":"none"}'


def test_ollama_plain_content():
    assert _extract_text("ollama", {"message": {"content": JSON}}) == JSON


def test_ollama_reasoning_model_puts_answer_in_thinking():
    payload = {"message": {"content": "", "thinking": JSON}}
    assert _extract_text("ollama", payload) == JSON, (
        "qwen3.5-shaped reply read as empty -- the exact 8/8 field failure"
    )


def test_content_wins_when_both_present():
    payload = {"message": {"content": JSON, "thinking": "internal musing"}}
    assert _extract_text("ollama", payload) == JSON


def test_ollama_generate_endpoint_shape():
    assert _extract_text("ollama", {"response": "", "thinking": JSON}) == JSON
    assert _extract_text("ollama", {"response": JSON}) == JSON


def test_openai_reasoning_content_fallback():
    payload = {"choices": [{"message": {"content": "", "reasoning_content": JSON}}]}
    assert _extract_text("openai", payload) == JSON


def test_genuinely_empty_returns_empty_not_crash():
    assert _extract_text("ollama", {"message": {"content": ""}}) == ""
    assert _extract_text("ollama", {}) == ""


def test_whitespace_only_is_treated_as_empty():
    payload = {"message": {"content": "   \n ", "thinking": JSON}}
    assert _extract_text("ollama", payload) == JSON
