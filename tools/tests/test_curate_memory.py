"""RED-first tests for tools/olrun/curate_memory.py.

Run:
    PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 python -m pytest tools/tests/test_curate_memory.py -q
"""

from __future__ import annotations

import importlib.util
import sqlite3
import sys
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parents[2]
MODULE_PATH = REPO_ROOT / "tools" / "olrun" / "curate_memory.py"


def _load_module():
    spec = importlib.util.spec_from_file_location("curate_memory", MODULE_PATH)
    if spec is None or spec.loader is None:  # pragma: no cover
        pytest.fail(f"cannot load {MODULE_PATH}")
    mod = importlib.util.module_from_spec(spec)
    sys.modules["curate_memory"] = mod
    spec.loader.exec_module(mod)
    return mod


cm = _load_module()


# ---------------------------------------------------------------- health ----


def test_health_reports_real_store_doc_counts():
    """Integration probe against the LIVE gen-130 stores. Skips if absent."""
    if not Path(cm.STORE_A).exists():
        pytest.skip(f"store A missing: {cm.STORE_A}")
    if not Path(cm.STORE_B).exists():
        pytest.skip(f"store B missing: {cm.STORE_B}")

    report = cm.health_report()

    assert report["store_a_docs"] > 8000, report
    assert report["store_b_events"] > 4000, report
    assert report["fts_ok"] is True, report
    assert isinstance(report["generations"], dict)
    assert report["generations"], "expected at least one generation bucket"


def test_health_marks_missing_store_unhealthy(tmp_path):
    report = cm.health_report(
        store_a=str(tmp_path / "nope_a.sqlite"),
        store_b=str(tmp_path / "nope_b.sqlite"),
    )
    assert report["store_a_docs"] == 0
    assert report["fts_ok"] is False
    assert cm.health_exit_code(report) != 0


# ------------------------------------------------------------- sanitizer ----


@pytest.fixture()
def fts_probe_db():
    """Tiny in-memory fts5 table so the sanitizer test never depends on gen-130."""
    conn = sqlite3.connect(":memory:")
    conn.execute("CREATE VIRTUAL TABLE t USING fts5(body, tokenize='porter unicode61')")
    conn.execute("INSERT INTO t(body) VALUES ('the soul.md file defines the agent card')")
    conn.execute("INSERT INTO t(body) VALUES ('a memory system for spatial gesture work')")
    conn.commit()
    yield conn
    conn.close()


NASTY_TOPICS = [
    'soul.md',
    'agent card',
    '.md',
    '-dashed-topic-',
    'he said "hi" loudly',
    'quote" unbalanced',
    'NEAR(a b)',
    'foo OR bar AND NOT baz',
    'C:\\Dev\\path\\file.md',
    'failure pattern',
    'a*b^c(d)',
    "it's a 100% match",
]


@pytest.mark.parametrize("topic", NASTY_TOPICS)
def test_fts_query_never_raises_syntax_error(fts_probe_db, topic):
    q = cm.build_fts_query(topic)
    if q is None:
        return  # topic reduced to nothing -- caller must skip it
    # Must not raise sqlite3.OperationalError: fts5: syntax error
    fts_probe_db.execute("SELECT count(*) FROM t WHERE t MATCH ?", (q,)).fetchone()


def test_fts_query_matches_dotted_and_phrase_topics(fts_probe_db):
    q = cm.build_fts_query("soul.md")
    n = fts_probe_db.execute("SELECT count(*) FROM t WHERE t MATCH ?", (q,)).fetchone()[0]
    assert n == 1

    q2 = cm.build_fts_query("memory system")
    n2 = fts_probe_db.execute("SELECT count(*) FROM t WHERE t MATCH ?", (q2,)).fetchone()[0]
    assert n2 == 1


def test_fts_query_returns_none_for_punctuation_only():
    assert cm.build_fts_query("!!! ???") is None
    assert cm.build_fts_query("   ") is None


# ------------------------------------------------------------- frontmatter --


REQUIRED_KEYS = [
    "capsule_id",
    "title",
    "source_store",
    "source_path",
    "source_generation",
    "topic",
    "bm25_score",
    "harvested_utc",
    "clock_source",
    "sigrun_approved",
    "quorum_votes",
    "concurrence_score",
    "rehydration_probe",
]


def _sample_hit():
    return cm.Hit(
        source_store="sigrun_recall_gen130",
        source_path=r"C:\Dev\some\path with spaces\SOUL.md",
        source_generation=130,
        topic='soul.md "quoted" -- tricky: value',
        bm25_score=-10.403247669831517,
        title='A Title: with "quotes" and --- dashes',
        body_text="# A Title\n\n---\n\nbody text with a --- separator line\n",
    )


def test_capsule_frontmatter_roundtrips_with_all_required_keys(tmp_path):
    hit = _sample_hit()
    text = cm.render_capsule(hit, harvested_utc="2026-08-02T00:00:00Z")
    path = tmp_path / "000_sample.md"
    path.write_text(text, encoding="utf-8")

    fm, body = cm.parse_capsule(path.read_text(encoding="utf-8"))

    for key in REQUIRED_KEYS:
        assert key in fm, f"missing frontmatter key {key}"

    assert fm["source_store"] == "sigrun_recall_gen130"
    assert fm["source_path"] == hit.source_path
    assert fm["source_generation"] == 130
    assert fm["topic"] == hit.topic
    assert fm["bm25_score"] == pytest.approx(hit.bm25_score)
    assert fm["harvested_utc"] == "2026-08-02T00:00:00Z"
    assert fm["clock_source"] == "host_read"
    assert fm["sigrun_approved"] is False
    assert fm["quorum_votes"] == []
    assert fm["concurrence_score"] is None
    assert isinstance(fm["capsule_id"], str) and len(fm["capsule_id"]) == 12
    assert isinstance(fm["rehydration_probe"], str) and fm["rehydration_probe"]
    assert "## Why this survived" in body


def test_capsule_body_is_abstract_not_archive():
    hit = _sample_hit()
    hit.body_text = "x" * 100_000
    text = cm.render_capsule(hit, harvested_utc="2026-08-02T00:00:00Z")
    assert len(text) < 4000, "capsule must be a curated abstract, not a whole document"


def test_null_generation_roundtrips(tmp_path):
    hit = _sample_hit()
    hit.source_store = "hfo_bitemporal_memory"
    hit.source_generation = None
    fm, _ = cm.parse_capsule(cm.render_capsule(hit, harvested_utc="2026-08-02T00:00:00Z"))
    assert fm["source_generation"] is None


# ----------------------------------------------------------- write fencing --


def test_out_dir_outside_allowed_roots_is_rejected():
    with pytest.raises(cm.UnsafeOutputDir):
        cm.assert_out_allowed(REPO_ROOT / "chains")
    with pytest.raises(cm.UnsafeOutputDir):
        cm.assert_out_allowed(REPO_ROOT.parent / "escape_me")


def test_curated_memory_root_is_allowed():
    cm.assert_out_allowed(cm.CURATED_ROOT / "2026-08-02")


def test_harvest_writes_only_under_out_dir(tmp_path):
    if not Path(cm.STORE_A).exists():
        pytest.skip(f"store A missing: {cm.STORE_A}")

    out = tmp_path / "harvest_out"
    forge_state = cm.CURATED_ROOT
    before = sorted(p.as_posix() for p in forge_state.rglob("*")) if forge_state.exists() else []

    written = cm.harvest(
        topics=["soul.md", "memory system"],
        limit_per_topic=2,
        out_dir=out,
    )

    assert written, "expected at least one capsule"
    for p in written:
        rp = Path(p).resolve()
        assert out.resolve() in rp.parents, f"{rp} escaped {out}"

    # nothing new landed in the forge's curated_memory root
    after = sorted(p.as_posix() for p in forge_state.rglob("*")) if forge_state.exists() else []
    assert before == after, "harvest touched the forge curated_memory root"

    # every file under out is a capsule we reported
    on_disk = sorted(p.resolve() for p in out.rglob("*") if p.is_file())
    assert on_disk == sorted(Path(p).resolve() for p in written)


def test_index_writes_jsonl_next_to_capsules(tmp_path):
    if not Path(cm.STORE_A).exists():
        pytest.skip(f"store A missing: {cm.STORE_A}")

    out = tmp_path / "idx_out"
    cm.harvest(topics=["soul.md"], limit_per_topic=2, out_dir=out)
    index_path = cm.build_index(out)

    assert index_path.exists()
    import json

    rows = [json.loads(line) for line in index_path.read_text(encoding="utf-8").splitlines() if line.strip()]
    assert rows
    for row in rows:
        for key in REQUIRED_KEYS:
            assert key in row, f"index row missing {key}"
        assert "capsule_file" in row


# ------------------------------------------------------------- store reads --


def test_stores_are_opened_read_only():
    if not Path(cm.STORE_A).exists():
        pytest.skip(f"store A missing: {cm.STORE_A}")
    conn = cm.open_ro(cm.STORE_A)
    try:
        with pytest.raises(sqlite3.OperationalError):
            conn.execute("CREATE TABLE should_not_exist (x INTEGER)")
    finally:
        conn.close()
