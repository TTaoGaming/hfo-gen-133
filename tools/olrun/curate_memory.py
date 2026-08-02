#!/usr/bin/env python3
"""curate_memory.py -- harvest candidate memory capsules from the LIVE gen-130 stores.

This tool does NOT port data and does NOT build a new store. It POINTS at the two
existing gen-130 sqlite memory stores, opens them STRICTLY READ-ONLY, runs bm25
ranked FTS5 queries per topic, and emits small *curated abstract* capsules under
this forge's `state/curated_memory/` tree.

Subcommands
-----------
  health   probe both stores read-only, print JSON, exit 0 iff healthy
  harvest  bm25-rank both stores per topic, write one capsule .md per hit
  index    flatten capsule frontmatter into INDEX.jsonl

Hard rules enforced in code
---------------------------
  * stdlib only
  * gen-130 stores opened `file:...?mode=ro` -- never written
  * clock is a real host read (`datetime.now(timezone.utc)`), never a literal
  * FTS5 topic strings are sanitized so punctuation cannot raise a syntax error
  * writes are fenced to `state/curated_memory/` (or the OS temp dir, for tests)

Usage
-----
  python tools/olrun/curate_memory.py health
  python tools/olrun/curate_memory.py harvest \
      --topics "soul.md,agent card,skill library,memory system" \
      --limit-per-topic 12 --out state/curated_memory/2026-08-02/
  python tools/olrun/curate_memory.py index --out state/curated_memory/2026-08-02/
"""

from __future__ import annotations

import argparse
import datetime
import hashlib
import json
import re
import sqlite3
import sys
import tempfile
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Iterable, Optional

# --------------------------------------------------------------------------
# Constants -- the LIVE gen-130 stores. Read-only. Never written by this tool.
# --------------------------------------------------------------------------

GEN130_ROOT = Path(r"C:/Dev/hfo_dev_2026_5_30/hfo_gen_130_forge")
STORE_A = str(GEN130_ROOT / "state/memory/sigrun_recall_gen130.sqlite")
STORE_B = str(GEN130_ROOT / "state/memory/hfo_bitemporal_memory.sqlite")

STORE_A_NAME = "sigrun_recall_gen130"
STORE_B_NAME = "hfo_bitemporal_memory"

REPO_ROOT = Path(__file__).resolve().parents[2]
CURATED_ROOT = REPO_ROOT / "state" / "curated_memory"

ABSTRACT_CHARS = 1200
CLOCK_SOURCE = "host_read"

FRONTMATTER_KEYS = (
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
)


class UnsafeOutputDir(Exception):
    """Raised when an --out path resolves outside the permitted write roots."""


# --------------------------------------------------------------------------
# Clock -- always a real host read
# --------------------------------------------------------------------------


def utc_now_iso() -> str:
    return datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def utc_today() -> str:
    return datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%d")


# --------------------------------------------------------------------------
# Store access -- READ ONLY
# --------------------------------------------------------------------------


def open_ro(path: str) -> sqlite3.Connection:
    """Open a sqlite file strictly read-only. Any write raises OperationalError."""
    conn = sqlite3.connect("file:" + str(path).replace("\\", "/") + "?mode=ro", uri=True)
    conn.row_factory = sqlite3.Row
    return conn


# --------------------------------------------------------------------------
# FTS5 query construction -- punctuation-proof
# --------------------------------------------------------------------------

_TOKEN_RE = re.compile(r"[0-9A-Za-z_]+")

# fts5 bareword keywords; must be quoted or they are parsed as operators
_FTS_KEYWORDS = {"AND", "OR", "NOT", "NEAR"}


def _tokens(topic: str) -> list[str]:
    return [t for t in _TOKEN_RE.findall(topic or "") if t]


def build_fts_query(topic: str) -> Optional[str]:
    """Turn an arbitrary human topic string into a safe FTS5 MATCH expression.

    Every token is emitted as a double-quoted fts5 string, so operators,
    quotes, dots, dashes, drive letters and `NEAR(` can never be parsed as
    syntax. Multi-token topics emit BOTH forms:

        ("a b" OR ("a" AND "b"))

    because store A uses a `porter unicode61` tokenizer (phrase `"soul md"`
    matches `soul.md`) while store B's FTS is plain unigram, where the phrase
    form scores 0 hits and only the AND form matches.

    Returns None if the topic reduces to no searchable tokens -- callers must
    skip such topics rather than issuing an empty MATCH.
    """
    toks = _tokens(topic)
    if not toks:
        return None
    quoted = ['"' + t.replace('"', '""') + '"' for t in toks]
    if len(quoted) == 1:
        return quoted[0]
    phrase = '"' + " ".join(t.replace('"', '""') for t in toks) + '"'
    conjunction = " AND ".join(quoted)
    return f"({phrase} OR ({conjunction}))"


# --------------------------------------------------------------------------
# Hit model
# --------------------------------------------------------------------------


@dataclass
class Hit:
    source_store: str
    source_path: str
    source_generation: Optional[int]
    topic: str
    bm25_score: float
    title: str
    body_text: str
    extra: dict = field(default_factory=dict)

    def dedupe_key(self) -> tuple[str, str]:
        return (self.source_store, self.source_path.replace("\\", "/").lower())


# --------------------------------------------------------------------------
# health
# --------------------------------------------------------------------------


def health_report(store_a: str = STORE_A, store_b: str = STORE_B) -> dict:
    report: dict[str, Any] = {
        "store_a_docs": 0,
        "store_b_events": 0,
        "fts_ok": False,
        "generations": {},
    }
    errors: list[str] = []
    fts_a = fts_b = False

    try:
        conn = open_ro(store_a)
        try:
            report["store_a_docs"] = conn.execute("SELECT count(*) FROM docs").fetchone()[0]
            gens = conn.execute(
                "SELECT generation, count(*) FROM docs GROUP BY generation ORDER BY 2 DESC"
            ).fetchall()
            report["generations"] = {("null" if g[0] is None else str(g[0])): g[1] for g in gens}
            probe = build_fts_query("memory")
            conn.execute(
                "SELECT count(*) FROM docs_fts WHERE docs_fts MATCH ?", (probe,)
            ).fetchone()
            fts_a = True
        finally:
            conn.close()
    except Exception as exc:  # noqa: BLE001 -- health must report, not crash
        errors.append(f"{STORE_A_NAME}: {exc}")

    try:
        conn = open_ro(store_b)
        try:
            report["store_b_events"] = conn.execute(
                "SELECT count(*) FROM memory_events"
            ).fetchone()[0]
            probe = build_fts_query("memory")
            conn.execute(
                "SELECT count(*) FROM memory_events_fts WHERE memory_events_fts MATCH ?",
                (probe,),
            ).fetchone()
            fts_b = True
        finally:
            conn.close()
    except Exception as exc:  # noqa: BLE001
        errors.append(f"{STORE_B_NAME}: {exc}")

    report["fts_ok"] = bool(fts_a and fts_b)
    report["store_a_path"] = str(store_a)
    report["store_b_path"] = str(store_b)
    report["probed_utc"] = utc_now_iso()
    report["clock_source"] = CLOCK_SOURCE
    if errors:
        report["errors"] = errors
    return report


def health_exit_code(report: dict) -> int:
    """Exit 0 iff both stores were readable AND store A has docs."""
    ok = (
        report.get("fts_ok") is True
        and report.get("store_a_docs", 0) > 0
        and report.get("store_b_events", 0) > 0
        and not report.get("errors")
    )
    return 0 if ok else 1


# --------------------------------------------------------------------------
# search
# --------------------------------------------------------------------------

_HEADING_RE = re.compile(r"^\s{0,3}#{1,6}\s+(.+?)\s*$", re.MULTILINE)


def derive_title(body: str, source_path: str) -> str:
    m = _HEADING_RE.search(body or "")
    if m:
        return m.group(1).strip()[:160]
    stem = Path(source_path.replace("\\", "/")).name
    return (stem or source_path)[:160]


def search_store_a(conn: sqlite3.Connection, topic: str, query: str, limit: int) -> list[Hit]:
    rows = conn.execute(
        """
        SELECT d.path AS path, d.rel_path AS rel_path, d.generation AS generation,
               d.body AS body, bm25(docs_fts) AS score
        FROM docs_fts
        JOIN docs d ON d.rowid = docs_fts.rowid
        WHERE docs_fts MATCH ?
        ORDER BY bm25(docs_fts)
        LIMIT ?
        """,
        (query, limit),
    ).fetchall()
    hits = []
    for r in rows:
        body = r["body"] or ""
        hits.append(
            Hit(
                source_store=STORE_A_NAME,
                source_path=r["path"],
                source_generation=r["generation"],
                topic=topic,
                bm25_score=float(r["score"]),
                title=derive_title(body, r["rel_path"] or r["path"]),
                body_text=body,
                extra={"rel_path": r["rel_path"]},
            )
        )
    return hits


def search_store_b(conn: sqlite3.Connection, topic: str, query: str, limit: int) -> list[Hit]:
    rows = conn.execute(
        """
        SELECT event_id, lineage, source_path, summary, payload_text,
               bm25(memory_events_fts) AS score
        FROM memory_events_fts
        WHERE memory_events_fts MATCH ?
        ORDER BY bm25(memory_events_fts)
        LIMIT ?
        """,
        (query, limit),
    ).fetchall()
    hits = []
    for r in rows:
        summary = (r["summary"] or "").strip()
        payload = (r["payload_text"] or "").strip()
        body = (summary + "\n\n" + payload).strip()
        hits.append(
            Hit(
                source_store=STORE_B_NAME,
                source_path=r["source_path"],
                source_generation=None,  # bitemporal store carries lineage, not generation
                topic=topic,
                bm25_score=float(r["score"]),
                title=summary[:160] or derive_title("", r["source_path"]),
                body_text=body,
                extra={"event_id": r["event_id"], "lineage": r["lineage"]},
            )
        )
    return hits


# --------------------------------------------------------------------------
# capsule rendering / parsing
# --------------------------------------------------------------------------


def capsule_id(source_path: str, topic: str) -> str:
    raw = (source_path or "") + "\x00" + (topic or "")
    return hashlib.sha256(raw.encode("utf-8")).hexdigest()[:12]


def _abs_source(source_path: str) -> str:
    p = (source_path or "").replace("\\", "/")
    pp = Path(p)
    if not pp.is_absolute():
        pp = GEN130_ROOT / p
    return str(pp).replace("\\", "/")


def rehydration_probe(source_path: str) -> str:
    """A shell command that exits 0 iff the source file still exists on disk."""
    return f'test -f "{_abs_source(source_path)}"'


def _slug(text: str, maxlen: int = 60) -> str:
    s = re.sub(r"[^0-9A-Za-z]+", "_", (text or "").strip().lower()).strip("_")
    return (s or "capsule")[:maxlen].strip("_") or "capsule"


def _abstract(body: str, limit: int = ABSTRACT_CHARS, title: str = "") -> str:
    text = (body or "").replace("\r\n", "\n").replace("\r", "\n")
    # The capsule already renders `# <title>`; drop a leading heading that just
    # repeats it so the abstract does not open with a duplicated H1.
    if title:
        lead = _HEADING_RE.match(text.lstrip("\n"))
        if lead and lead.group(1).strip() == title.strip():
            stripped = text.lstrip("\n")
            text = stripped[lead.end():].lstrip("\n")
    text = text[:limit]
    # A bare `---` line inside the abstract would look like a frontmatter fence
    # to naive readers; neutralise it without dropping the content.
    text = re.sub(r"(?m)^-{3,}\s*$", "- - -", text)
    truncated = len(body or "") > limit
    if truncated:
        text = text.rstrip() + "\n\n[... abstract truncated at %d chars; see source ...]" % limit
    return text.strip()


def _fm_value(value: Any) -> str:
    """JSON-encode so the value is unambiguous and round-trips with stdlib only."""
    return json.dumps(value, ensure_ascii=False)


def render_capsule(hit: Hit, harvested_utc: Optional[str] = None) -> str:
    harvested_utc = harvested_utc or utc_now_iso()
    fm = {
        "capsule_id": capsule_id(hit.source_path, hit.topic),
        "title": hit.title,
        "source_store": hit.source_store,
        "source_path": hit.source_path,
        "source_generation": hit.source_generation,
        "topic": hit.topic,
        "bm25_score": hit.bm25_score,
        "harvested_utc": harvested_utc,
        "clock_source": CLOCK_SOURCE,
        "sigrun_approved": False,
        "quorum_votes": [],
        "concurrence_score": None,
        "rehydration_probe": rehydration_probe(hit.source_path),
    }
    comments = {
        "sigrun_approved": "  # set true only by an approval pass",
        "quorum_votes": "  # filled by multi_family_vote.py",
    }
    lines = ["---"]
    for key in FRONTMATTER_KEYS:
        lines.append(f"{key}: {_fm_value(fm[key])}{comments.get(key, '')}")
    lines.append("---")
    lines.append("")
    lines.append(f"# {hit.title}")
    lines.append("")
    lines.append(_abstract(hit.body_text, title=hit.title))
    lines.append("")
    lines.append("## Why this survived")
    lines.append("")
    lines.append(
        f"bm25-ranked hit for topic `{hit.topic}` in `{hit.source_store}` "
        f"(score {hit.bm25_score:.4f}; lower is a stronger match). "
        "Candidate only -- `sigrun_approved: false` until an approval pass "
        "and cross-family quorum vote say otherwise."
    )
    lines.append("")
    return "\n".join(lines)


_FM_LINE_RE = re.compile(r"^([A-Za-z_][A-Za-z0-9_]*):\s*(.*)$")
_DECODER = json.JSONDecoder()


def parse_capsule(text: str) -> tuple[dict, str]:
    """Parse a capsule into (frontmatter dict, body). Trailing `# comments` ignored."""
    lines = (text or "").replace("\r\n", "\n").split("\n")
    if not lines or lines[0].strip() != "---":
        raise ValueError("capsule does not start with a --- frontmatter fence")
    end = None
    for i in range(1, len(lines)):
        if lines[i].strip() == "---":
            end = i
            break
    if end is None:
        raise ValueError("unterminated frontmatter fence")

    fm: dict[str, Any] = {}
    for line in lines[1:end]:
        if not line.strip():
            continue
        m = _FM_LINE_RE.match(line)
        if not m:
            continue
        key, raw = m.group(1), m.group(2).strip()
        try:
            value, _idx = _DECODER.raw_decode(raw)
        except ValueError:
            value = raw
        fm[key] = value
    return fm, "\n".join(lines[end + 1 :]).strip()


# --------------------------------------------------------------------------
# write fencing
# --------------------------------------------------------------------------


def _allowed_roots() -> list[Path]:
    roots = [CURATED_ROOT.resolve()]
    try:
        roots.append(Path(tempfile.gettempdir()).resolve())
    except Exception:  # pragma: no cover
        pass
    return roots


def assert_out_allowed(out_dir: Path) -> Path:
    """Fence every write to state/curated_memory/ (or the OS temp dir, for tests)."""
    target = Path(out_dir).expanduser()
    if not target.is_absolute():
        target = (REPO_ROOT / target).resolve()
    else:
        target = target.resolve()
    for root in _allowed_roots():
        if target == root or root in target.parents:
            return target
    raise UnsafeOutputDir(
        f"refusing to write to {target}; allowed roots: {[str(r) for r in _allowed_roots()]}"
    )


# --------------------------------------------------------------------------
# harvest / index
# --------------------------------------------------------------------------


def parse_topics(raw: str) -> list[str]:
    return [t.strip() for t in (raw or "").split(",") if t.strip()]


def harvest(
    topics: Iterable[str],
    limit_per_topic: int,
    out_dir: Path,
    store_a: str = STORE_A,
    store_b: str = STORE_B,
    verbose: bool = False,
) -> list[Path]:
    out = assert_out_allowed(Path(out_dir))
    out.mkdir(parents=True, exist_ok=True)

    conn_a = open_ro(store_a) if Path(store_a).exists() else None
    conn_b = open_ro(store_b) if Path(store_b).exists() else None

    collected: list[Hit] = []
    seen: set[tuple[str, str]] = set()
    skipped_topics: list[str] = []

    try:
        for topic in topics:
            query = build_fts_query(topic)
            if query is None:
                skipped_topics.append(topic)
                continue
            found: list[Hit] = []
            for conn, fn in ((conn_a, search_store_a), (conn_b, search_store_b)):
                if conn is None:
                    continue
                try:
                    found.extend(fn(conn, topic, query, limit_per_topic))
                except sqlite3.OperationalError as exc:
                    print(f"[warn] topic {topic!r}: {exc}", file=sys.stderr)
            found.sort(key=lambda h: h.bm25_score)
            for hit in found:
                key = hit.dedupe_key()
                if key in seen:
                    continue
                seen.add(key)
                collected.append(hit)
    finally:
        for conn in (conn_a, conn_b):
            if conn is not None:
                conn.close()

    harvested_utc = utc_now_iso()
    written: list[Path] = []
    for i, hit in enumerate(collected):
        name = f"{i:03d}_{_slug(hit.title or Path(hit.source_path).name)}.md"
        path = out / name
        path.write_text(render_capsule(hit, harvested_utc=harvested_utc), encoding="utf-8")
        written.append(path)
        if verbose:
            print(f"  wrote {path}")

    if skipped_topics:
        print(
            f"[warn] skipped topics with no searchable tokens: {skipped_topics}",
            file=sys.stderr,
        )
    return written


def build_index(out_dir: Path) -> Path:
    out = assert_out_allowed(Path(out_dir))
    if not out.exists():
        raise FileNotFoundError(f"no such capsule dir: {out}")
    index_path = out / "INDEX.jsonl"
    rows = []
    for capsule in sorted(out.glob("*.md")):
        fm, _body = parse_capsule(capsule.read_text(encoding="utf-8"))
        row = {k: fm.get(k) for k in FRONTMATTER_KEYS}
        row["capsule_file"] = capsule.name
        rows.append(row)
    with index_path.open("w", encoding="utf-8", newline="\n") as fh:
        for row in rows:
            fh.write(json.dumps(row, ensure_ascii=False) + "\n")
    return index_path


# --------------------------------------------------------------------------
# CLI
# --------------------------------------------------------------------------

DEFAULT_TOPICS = (
    "soul.md,agent card,skill library,memory system,"
    "spatial gesture,outreach,quorum,failure pattern"
)


def _default_out() -> Path:
    return CURATED_ROOT / utc_today()


def main(argv: Optional[list[str]] = None) -> int:
    ap = argparse.ArgumentParser(prog="curate_memory.py", description=__doc__.split("\n")[0])
    sub = ap.add_subparsers(dest="cmd", required=True)

    p_health = sub.add_parser("health", help="read-only probe of both gen-130 stores")
    p_health.add_argument("--store-a", default=STORE_A)
    p_health.add_argument("--store-b", default=STORE_B)

    p_harvest = sub.add_parser("harvest", help="bm25-harvest candidate capsules")
    p_harvest.add_argument("--topics", default=DEFAULT_TOPICS, help="comma-separated topics")
    p_harvest.add_argument("--limit-per-topic", type=int, default=12)
    p_harvest.add_argument("--out", default=None, help="default: state/curated_memory/<UTC date>/")
    p_harvest.add_argument("--store-a", default=STORE_A)
    p_harvest.add_argument("--store-b", default=STORE_B)
    p_harvest.add_argument("--index", action="store_true", help="also write INDEX.jsonl")

    p_index = sub.add_parser("index", help="flatten capsule frontmatter to INDEX.jsonl")
    p_index.add_argument("--out", default=None, help="default: state/curated_memory/<UTC date>/")

    args = ap.parse_args(argv)

    if args.cmd == "health":
        report = health_report(args.store_a, args.store_b)
        print(json.dumps(report, indent=2, ensure_ascii=False))
        return health_exit_code(report)

    if args.cmd == "harvest":
        out = Path(args.out) if args.out else _default_out()
        topics = parse_topics(args.topics)
        if not topics:
            print("[error] no topics given", file=sys.stderr)
            return 2
        try:
            written = harvest(
                topics=topics,
                limit_per_topic=args.limit_per_topic,
                out_dir=out,
                store_a=args.store_a,
                store_b=args.store_b,
                verbose=True,
            )
        except UnsafeOutputDir as exc:
            print(f"[error] {exc}", file=sys.stderr)
            return 2
        resolved = assert_out_allowed(out)
        summary = {
            "capsules_written": len(written),
            "out_dir": str(resolved),
            "topics": topics,
            "harvested_utc": utc_now_iso(),
            "clock_source": CLOCK_SOURCE,
        }
        if args.index and written:
            summary["index"] = str(build_index(out))
        print(json.dumps(summary, indent=2, ensure_ascii=False))
        return 0 if written else 1

    if args.cmd == "index":
        out = Path(args.out) if args.out else _default_out()
        try:
            index_path = build_index(out)
        except (UnsafeOutputDir, FileNotFoundError) as exc:
            print(f"[error] {exc}", file=sys.stderr)
            return 2
        n = sum(1 for _ in index_path.open("r", encoding="utf-8"))
        print(json.dumps({"index": str(index_path), "rows": n}, indent=2))
        return 0 if n else 1

    return 2


if __name__ == "__main__":
    raise SystemExit(main())
