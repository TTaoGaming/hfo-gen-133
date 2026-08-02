#!/usr/bin/env python
"""Olrun facade RELAY -- N result files in, ONE compressed synthesis out.

The operator should read one thing, not N. This polls result files (JSON,
JSONL, or markdown), extracts only the headline facts that change a decision
(exit codes, claim_status, counts, HONEST_FLAW lines), and writes a single
markdown synthesis under a hard word budget.

  poll --sources <glob-or-comma-paths> --out state/olrun/relay/{date}_relay.md

Never crashes on a missing or malformed source -- those land under
'## Unreadable sources' and the synthesis still ships. stdlib only.
"""

from __future__ import annotations

import argparse
import glob as globmod
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import _chain  # noqa: E402

WORD_BUDGET = 400

_HONEST_FLAW_RE = re.compile(r"^[\s>*\-#]*HONEST[_ ]FLAW\s*[:\-]\s*(.+)$", re.IGNORECASE | re.MULTILINE)
_CLAIM_RE = re.compile(r"claim[_ ]status\s*[\"']?\s*[:=]\s*[\"']?([a-z_]+)", re.IGNORECASE)
_EXIT_RE = re.compile(r"exit[_ ]?code\s*[\"']?\s*[:=]\s*[\"']?(-?\d+)", re.IGNORECASE)
_COUNT_RE = re.compile(r"\b(\d+)\s+(passed|failed|errors?|rows?|skills?|leads?|files?)\b", re.IGNORECASE)


def expand_sources(spec: str):
    """Comma-separated list; each item may be a literal path or a glob."""
    out = []
    for raw in str(spec).split(","):
        item = raw.strip()
        if not item:
            continue
        matches = sorted(globmod.glob(item, recursive=True))
        if matches:
            out.extend(m for m in matches if os.path.isfile(m))
        else:
            out.append(item)  # keep it, so it reports as unreadable
    seen, uniq = set(), []
    for p in out:
        ap = os.path.abspath(p)
        if ap not in seen:
            seen.add(ap)
            uniq.append(p)
    return uniq


def _walk_json(obj, facts, depth=0):
    if depth > 6:
        return
    if isinstance(obj, dict):
        for key in ("exit_code", "claim_status", "valid", "status", "count",
                    "row_id", "skill", "honest_flaw", "verifier_result"):
            if key in obj and not isinstance(obj[key], (dict, list)):
                val = obj[key]
                if key == "verifier_result":
                    val = str(val)[:120]
                facts.append((key, val))
        for val in obj.values():
            _walk_json(val, facts, depth + 1)
    elif isinstance(obj, list):
        for item in obj[:50]:
            _walk_json(item, facts, depth + 1)


def extract_facts(path: str):
    """-> (facts:[(k,v)], flaws:[str], error:str|None)"""
    try:
        with open(path, "r", encoding="utf-8", errors="replace") as fh:
            text = fh.read()
    except OSError as exc:
        return [], [], "unreadable (%s)" % exc.__class__.__name__
    if not text.strip():
        return [], [], "empty file"

    facts, flaws = [], []
    parsed = False
    stripped = text.lstrip()
    looked_structured = stripped[:1] in "{["
    if looked_structured:
        try:
            _walk_json(json.loads(text), facts)
            parsed = True
        except ValueError:
            pass
    if not parsed and stripped[:1] == "{":  # try JSONL
        rows, bad = [], 0
        for line in text.splitlines():
            if not line.strip():
                continue
            try:
                rows.append(json.loads(line))
            except ValueError:
                bad += 1
        if rows:
            facts.append(("jsonl_rows", len(rows)))
            if bad:
                facts.append(("jsonl_malformed_lines", bad))
            # Detail sampling is tail-biased (recent rows are the interesting
            # ones), but adverse statuses are swept from EVERY row. A chain is
            # append-only: reading only the tail makes any failure older than
            # the window invisible to the operator, which is precisely the
            # "relay silently drops a red" failure this tool must not have.
            _walk_json(rows[-3:], facts)
            for row in rows:
                if not isinstance(row, dict):
                    continue
                cs = row.get("claim_status")
                if isinstance(cs, str) and cs in ADVERSE_CLAIM_STATUS:
                    facts.append(("claim_status", cs))
                ec = row.get("exit_code")
                if isinstance(ec, int) and ec != 0:
                    facts.append(("exit_code", ec))
                hf = row.get("honest_flaw")
                if isinstance(hf, str) and hf.strip():
                    flaws.append(hf.strip())
            parsed = True

    if not parsed:
        for m in _CLAIM_RE.finditer(text):
            facts.append(("claim_status", m.group(1)))
        for m in _EXIT_RE.finditer(text):
            facts.append(("exit_code", int(m.group(1))))
        for m in _COUNT_RE.finditer(text):
            facts.append(("count", "%s %s" % (m.group(1), m.group(2).lower())))

    for m in _HONEST_FLAW_RE.finditer(text):
        flaws.append(m.group(1).strip())
    for key, val in list(facts):
        if key == "honest_flaw" and isinstance(val, str) and val.strip():
            flaws.append(val.strip())

    # 'unreadable' is reserved for files we genuinely could not parse. A file we
    # read fine that simply carries no exit code / claim_status is READ, and is
    # reported as 'no numeric receipts' -- conflating the two would overstate
    # how much of the input actually failed.
    err = None
    if looked_structured and not parsed:
        err = "malformed JSON/JSONL (parsed as neither)"
    return facts, flaws, err


# Claim statuses that must NEVER be compressed out of a relay. Compression may
# lose precision; it may never lose bad news.
ADVERSE_CLAIM_STATUS = frozenset({"failed", "partial", "proposed"})


def summarize_facts(facts):
    """Collapse to the decision-changing minimum."""
    exits = [v for k, v in facts if k == "exit_code" and isinstance(v, int)]
    claims = [str(v) for k, v in facts if k == "claim_status"]
    counts = [str(v) for k, v in facts if k in ("count", "jsonl_rows", "jsonl_malformed_lines")]
    valids = [v for k, v in facts if k == "valid" and isinstance(v, bool)]
    bits = []
    if exits:
        bad = [e for e in exits if e != 0]
        bits.append("exit %s" % (",".join(str(e) for e in sorted(set(exits))))
                    + (" (NONZERO)" if bad else ""))
    if valids:
        bits.append("valid %d/%d" % (sum(1 for v in valids if v), len(valids)))
    if claims:
        # Adverse statuses are surfaced FIRST and are never truncated away.
        # A relay that drops a 'failed' because it sorted third has reward-hacked
        # its own compression objective -- the one failure mode this tool exists
        # to avoid, and the one the operator cannot detect from the relay alone.
        adverse, benign = [], []
        for c in claims:
            bucket = adverse if c in ADVERSE_CLAIM_STATUS else benign
            if c not in bucket:
                bucket.append(c)
        counted = {c: claims.count(c) for c in adverse}
        rendered = ["%s x%d" % (c, counted[c]) for c in adverse] + benign[:2]
        bits.append("claim_status " + "/".join(rendered))
    if counts:
        seen = []
        for c in counts:
            if c not in seen:
                seen.append(c)
        bits.append("counts " + ", ".join(seen[:3]))
    return "; ".join(bits) if bits else "no numeric receipts"


def word_count(text: str) -> int:
    return len(text.split())


def build_synthesis(entries, unreadable, out_path):
    """entries: [(path, summary, flaws)]"""
    ts = _chain.utc_now_iso()
    head = [
        "# Olrun relay synthesis",
        "",
        "- generated_utc: %s (clock_source: host_read)" % ts,
        "- sources_read: %d | unreadable: %d" % (len(entries), len(unreadable)),
        "",
        "## Headline",
        "",
    ]
    nonzero = sum(1 for _p, s, _f in entries if "NONZERO" in s)
    failed = sum(1 for _p, s, _f in entries
                 if any(a in s for a in ADVERSE_CLAIM_STATUS))
    if not entries:
        head.append("No readable sources. Nothing is proven this cycle.")
    elif nonzero or failed:
        head.append("%d of %d sources carry a nonzero exit or an adverse claim_status "
                    "(%s). Read those first." % (max(nonzero, failed), len(entries),
                                                 ", ".join(sorted(ADVERSE_CLAIM_STATUS))))
    else:
        head.append("All %d readable sources report zero exits and no failed claim_status. "
                    "Exit 0 proves the process ran, not that the claim is true." % len(entries))

    body = ["", "## Per-source receipts", ""]
    for path, summary, _flaws in entries:
        body.append("- `%s` -- %s" % (path.replace("\\", "/"), summary))

    flaws = []
    for _p, _s, fl in entries:
        for f in fl:
            if f not in flaws:
                flaws.append(f)
    flaw_sec = []
    if flaws:
        flaw_sec = ["", "## Honest flaws carried forward", ""]
        flaw_sec += ["- %s" % f for f in flaws]

    unread_sec = []
    if unreadable:
        unread_sec = ["", "## Unreadable sources", ""]
        unread_sec += ["- `%s` -- %s" % (p.replace("\\", "/"), why) for p, why in unreadable]

    tail = ["", "## Next safe action", "",
            "Open only the sources flagged above. Everything else is accounted for.", ""]

    def render(source_lines):
        return "\n".join(head + body[:3] + source_lines + flaw_sec + unread_sec + tail) + "\n"

    # Hard word budget: trim per-source detail first, then flaws, never the headline.
    source_lines = body[3:]
    shown = len(source_lines)
    while shown > 1:
        kept = source_lines[:shown]
        if shown < len(source_lines):
            kept = kept + ["- ... (%d more source line(s) trimmed for the word budget)"
                           % (len(source_lines) - shown)]
        if word_count(render(kept)) <= WORD_BUDGET:
            break
        shown -= 1
    kept = source_lines[:shown]
    if shown < len(source_lines):
        kept = kept + ["- ... (%d more source line(s) trimmed for the word budget)"
                       % (len(source_lines) - shown)]
    while word_count(render(kept)) > WORD_BUDGET and len(flaw_sec) > 3:
        flaw_sec = flaw_sec[:-1]

    text = render(kept)
    os.makedirs(os.path.dirname(os.path.abspath(out_path)) or ".", exist_ok=True)
    with open(out_path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(text)
    return text


def cmd_poll(args):
    out_path = args.out.replace("{date}", _chain.utc_today())
    sources = expand_sources(args.sources)
    entries, unreadable = [], []
    for path in sources:
        if not os.path.isfile(path):
            unreadable.append((path, "not found"))
            continue
        try:
            facts, flaws, err = extract_facts(path)
        except Exception as exc:  # noqa: BLE001 - a bad source must never kill the relay
            unreadable.append((path, "extract failed: %s" % exc.__class__.__name__))
            continue
        if err:
            unreadable.append((path, err))
            continue
        entries.append((path, summarize_facts(facts), flaws))

    text = build_synthesis(entries, unreadable, out_path)
    words = word_count(text)

    _chain.append_row(
        action="poll_and_relay",
        skill=None,
        verifier_result="sources_read=%d unreadable=%d out=%s words=%d"
                        % (len(entries), len(unreadable), out_path, words),
        claim_status="wired_with_receipts" if entries else "partial",
        remaining_risk=[
            "fact extraction is regex/shape heuristic; a novel result format degrades to "
            "'no headline facts' rather than a wrong fact",
            "compression is lossy by design -- the synthesis is a pointer, not a replacement",
        ],
        next_safe_action="operator reads %s and opens only the flagged sources" % out_path,
        honest_flaw="a source that lies in its own exit_code/claim_status field is relayed "
                    "faithfully; the relay does not re-verify upstream claims",
        chain_path=args.chain,
        extra={"out_path": out_path, "word_count": words},
    )

    print(out_path)
    print("word_count=%d (budget=%d) sources_read=%d unreadable=%d"
          % (words, WORD_BUDGET, len(entries), len(unreadable)))
    return 0


def build_parser():
    p = argparse.ArgumentParser(
        prog="poll_and_relay.py",
        description="Poll N result files, emit ONE compressed synthesis.",
    )
    p.add_argument("--chain", default=None)
    sub = p.add_subparsers(dest="cmd", required=True)
    poll = sub.add_parser("poll", help="read sources and write the synthesis")
    poll.add_argument("--sources", required=True,
                      help="comma-separated paths and/or globs")
    poll.add_argument("--out", default="state/olrun/relay/{date}_relay.md")
    return p


def main(argv=None):
    args = build_parser().parse_args(argv)
    return {"poll": cmd_poll}[args.cmd](args)


if __name__ == "__main__":
    sys.exit(main())
