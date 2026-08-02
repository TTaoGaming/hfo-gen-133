#!/usr/bin/env python3
"""LOOP-A · ARTICLE_SCANNER — daily scan of named-author blogs, AI
newsletters, and community aggregators. Scores each item against six
factory axes, writes a daily digest, posts headline to Slack.

Companion to LOOP-D (`demand_signal_mine`). LOOP-D listens to users
complaining; LOOP-A listens to builders publishing.

AIH2O header
------------
AIH2O:
  version: gen-133
  loop: article_scanner
  role: executor
  actor: factory_loop
  verifier: n_signals > 0 OR explicit zero-signal chain-row with reason
  clock_source: host_read
  chain: state/loop_receipts/article_scanner_<UTCDATE>.jsonl
  signal_log: state/factory_targets/article_signals.jsonl
  daily_digest: state/factory_targets/ARTICLE_DIGEST_<UTCDATE>.md

CLI
---
    python factory/loops/article_scanner/run.py \\
        --sources sources.yaml --seed seed_urls.json

Kill conditions
---------------
- Per-source: 3 consecutive failed fetches -> mark degraded, skip 24 h
- Digest empty 3 days running -> halt-escalate operator
- LiteLLM 4xx/5xx -> back off (2s/4s/8s) then regex fallback

stdlib-only except for the optional `yaml` module (falls back to a
tiny inline parser that handles our exact schema).
"""

from __future__ import annotations

import argparse
import hashlib
import html
import json
import os
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime, timedelta, timezone
from pathlib import Path
from xml.etree import ElementTree as ET

_HERE = Path(__file__).resolve()
_FORGE = _HERE.parents[3]
sys.path.insert(0, str(_FORGE))
from factory.loops.lib import chain_row, litellm_client, slack_escalate  # noqa: E402


LOOP = "article_scanner"
SIGNAL_LOG = _FORGE / "state" / "factory_targets" / "article_signals.jsonl"
DIGEST_DIR = _FORGE / "state" / "factory_targets"
SOURCE_HEALTH = _FORGE / "state" / "factory_targets" / "article_scanner_source_health.json"

USER_AGENT = "hfo-gen133-article-scanner/0.1 (+contact: ops@hfo.local)"
HN_TOP_JSON = "https://hacker-news.firebaseio.com/v0/topstories.json"
HN_ITEM_JSON = "https://hacker-news.firebaseio.com/v0/item/{id}.json"
REDDIT_JSON = "https://www.reddit.com/r/{sub}/new.json?limit=50"

AXES = (
    "build_opportunity",
    "distribute_tactic",
    "tool_adoption",
    "market_signal",
    "competitive_threat",
    "hive_infra_pattern",
)

# Paywall snippet-only sources — never grab full body.
PAYWALL_HOSTS = {"wsj.com", "www.wsj.com", "nytimes.com", "www.nytimes.com", "ft.com", "www.ft.com"}


# ---------------------------------------------------------------------------
# Time helpers
# ---------------------------------------------------------------------------
def _utc_now() -> datetime:
    return datetime.now(timezone.utc)


def _utc_iso() -> str:
    return _utc_now().strftime("%Y-%m-%dT%H:%M:%SZ")


def _utc_today() -> str:
    return _utc_now().strftime("%Y%m%d")


# ---------------------------------------------------------------------------
# Tiny YAML reader (fallback if PyYAML absent). Handles the exact subset
# used by sources.yaml: comments, a top-level `sources:` list, list items
# opened with `- key: value`, scalar values, `[a, b, c]` inline lists.
# ---------------------------------------------------------------------------
def _load_yaml(path: Path) -> dict:
    try:
        import yaml  # type: ignore
        return yaml.safe_load(path.read_text(encoding="utf-8"))
    except ImportError:
        return _tiny_yaml(path.read_text(encoding="utf-8"))


def _coerce(v: str):
    v = v.strip()
    if v.startswith("[") and v.endswith("]"):
        inner = v[1:-1].strip()
        if not inner:
            return []
        return [_coerce(x) for x in inner.split(",")]
    if v.lower() in ("true", "yes"):
        return True
    if v.lower() in ("false", "no"):
        return False
    if v.startswith(("'", '"')) and v.endswith(("'", '"')):
        return v[1:-1]
    try:
        return int(v)
    except ValueError:
        pass
    try:
        return float(v)
    except ValueError:
        pass
    return v


def _tiny_yaml(text: str) -> dict:
    """Parses the exact schema of our sources.yaml. Not a general YAML."""
    out: dict = {"sources": []}
    current: dict | None = None
    for raw in text.splitlines():
        line = raw.rstrip()
        if not line.strip() or line.strip().startswith("#"):
            continue
        if line == "sources:":
            continue
        # New list item under sources
        m = re.match(r"^  -\s+(\w+):\s*(.*)$", line)
        if m:
            if current is not None:
                out["sources"].append(current)
            current = {}
            current[m.group(1)] = _coerce(m.group(2))
            continue
        # Continuation key inside the current item
        m = re.match(r"^    (\w+):\s*(.*)$", line)
        if m and current is not None:
            current[m.group(1)] = _coerce(m.group(2))
            continue
    if current is not None:
        out["sources"].append(current)
    return out


# ---------------------------------------------------------------------------
# Source health tracking (3-strikes -> degraded 24h)
# ---------------------------------------------------------------------------
def _load_health() -> dict:
    if not SOURCE_HEALTH.exists():
        return {}
    try:
        return json.loads(SOURCE_HEALTH.read_text(encoding="utf-8"))
    except Exception:
        return {}


def _save_health(h: dict) -> None:
    SOURCE_HEALTH.parent.mkdir(parents=True, exist_ok=True)
    SOURCE_HEALTH.write_text(json.dumps(h, indent=2, sort_keys=True), encoding="utf-8")


def _is_skipped(sid: str, health: dict) -> bool:
    rec = health.get(sid) or {}
    until = rec.get("skip_until_utc")
    if not until:
        return False
    try:
        return _utc_now() < datetime.strptime(until, "%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=timezone.utc)
    except Exception:
        return False


def _mark_source(sid: str, ok: bool, health: dict) -> None:
    rec = health.setdefault(sid, {"fail_streak": 0, "last_ok_utc": None, "skip_until_utc": None})
    if ok:
        rec["fail_streak"] = 0
        rec["last_ok_utc"] = _utc_iso()
        rec["skip_until_utc"] = None
    else:
        rec["fail_streak"] = rec.get("fail_streak", 0) + 1
        if rec["fail_streak"] >= 3:
            rec["skip_until_utc"] = (_utc_now() + timedelta(hours=24)).strftime("%Y-%m-%dT%H:%M:%SZ")


# ---------------------------------------------------------------------------
# robots.txt cache (best-effort, 24h TTL)
# ---------------------------------------------------------------------------
_ROBOTS_CACHE: dict[str, tuple[float, "urllib.robotparser.RobotFileParser | None"]] = {}


def _robots_ok(url: str) -> bool:
    import urllib.robotparser as rp
    host = urllib.parse.urlparse(url).netloc
    if not host:
        return True
    now = time.time()
    cached = _ROBOTS_CACHE.get(host)
    if not cached or now - cached[0] > 24 * 3600:
        parser = rp.RobotFileParser()
        parser.set_url(f"https://{host}/robots.txt")
        try:
            parser.read()
        except Exception:
            parser = None
        _ROBOTS_CACHE[host] = (now, parser)
        cached = _ROBOTS_CACHE[host]
    parser = cached[1]
    if parser is None:
        return True  # can't check -> assume OK; be nice with UA + delay
    try:
        return parser.can_fetch(USER_AGENT, url)
    except Exception:
        return True


# ---------------------------------------------------------------------------
# Fetchers
# ---------------------------------------------------------------------------
def _http_get(url: str, timeout: float = 20.0) -> tuple[bool, str, str]:
    if not _robots_ok(url):
        return False, "", "robots_disallow"
    try:
        req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT, "Accept": "*/*"})
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            data = resp.read()
            enc = resp.headers.get_content_charset() or "utf-8"
            try:
                text = data.decode(enc, errors="replace")
            except Exception:
                text = data.decode("utf-8", errors="replace")
            return True, text, ""
    except urllib.error.HTTPError as e:
        return False, "", f"HTTP {e.code}"
    except (urllib.error.URLError, TimeoutError, OSError) as e:
        return False, "", str(e)


def _parse_rss(xml_text: str) -> list[dict]:
    """RSS 2.0 or Atom -> list of {title, link, summary, published (unix)}."""
    items: list[dict] = []
    try:
        root = ET.fromstring(xml_text)
    except ET.ParseError:
        return items

    def _t(node, tag_options):
        for t in tag_options:
            found = node.find(t)
            if found is not None and (found.text or "").strip():
                return found.text.strip()
            # Atom uses attrib for links
            if t.endswith("link") and found is not None and found.get("href"):
                return found.get("href")
        return ""

    def _parse_date(s: str) -> float:
        if not s:
            return 0.0
        for fmt in (
            "%a, %d %b %Y %H:%M:%S %Z",
            "%a, %d %b %Y %H:%M:%S %z",
            "%Y-%m-%dT%H:%M:%S%z",
            "%Y-%m-%dT%H:%M:%SZ",
            "%Y-%m-%dT%H:%M:%S.%fZ",
        ):
            try:
                dt = datetime.strptime(s, fmt)
                if dt.tzinfo is None:
                    dt = dt.replace(tzinfo=timezone.utc)
                return dt.timestamp()
            except ValueError:
                continue
        return 0.0

    # RSS: channel/item
    for it in root.iter():
        tag = it.tag.split("}", 1)[-1].lower()
        if tag == "item":
            title = _t(it, [".//{*}title", "title"])
            link = _t(it, [".//{*}link", "link"])
            summary = _t(it, [".//{*}description", "description", ".//{*}summary"])
            pub = _t(it, [".//{*}pubDate", "pubDate", ".//{*}updated", ".//{*}published"])
            items.append({
                "title": html.unescape(title or "")[:400],
                "url": (link or "").strip(),
                "summary": _strip_tags(html.unescape(summary or "")),
                "published_utc": _parse_date(pub),
            })
        elif tag == "entry":
            title = _t(it, [".//{*}title", "title"])
            link_node = it.find(".//{*}link")
            link = link_node.get("href") if link_node is not None else ""
            summary = _t(it, [".//{*}summary", ".//{*}content"])
            pub = _t(it, [".//{*}updated", ".//{*}published"])
            items.append({
                "title": html.unescape(title or "")[:400],
                "url": (link or "").strip(),
                "summary": _strip_tags(html.unescape(summary or "")),
                "published_utc": _parse_date(pub),
            })
    return items


def _strip_tags(s: str) -> str:
    return re.sub(r"<[^>]+>", " ", s or "").strip()[:2000]


def _parse_html_index(html_text: str, base_url: str) -> list[dict]:
    """Grab <a href> anchors within probable article contexts."""
    items: list[dict] = []
    for m in re.finditer(r'<a[^>]+href="([^"]+)"[^>]*>([^<]{6,200})</a>', html_text, flags=re.I):
        href = urllib.parse.urljoin(base_url, m.group(1))
        text = html.unescape(m.group(2)).strip()
        if not text or href == base_url:
            continue
        items.append({
            "title": text[:400],
            "url": href,
            "summary": "",
            "published_utc": 0.0,
        })
    # Dedup by url
    seen = set()
    uniq = []
    for it in items:
        if it["url"] in seen:
            continue
        seen.add(it["url"])
        uniq.append(it)
    return uniq[:100]


def _fetch_hn_top(limit: int) -> list[dict]:
    ok, text, _ = _http_get(HN_TOP_JSON)
    if not ok:
        return []
    try:
        ids = json.loads(text)[:limit]
    except Exception:
        return []
    out: list[dict] = []
    for hid in ids:
        ok2, item_text, _ = _http_get(HN_ITEM_JSON.format(id=hid))
        if not ok2:
            continue
        try:
            item = json.loads(item_text)
        except Exception:
            continue
        if not isinstance(item, dict) or item.get("deleted") or item.get("dead"):
            continue
        out.append({
            "title": (item.get("title") or "")[:400],
            "url": item.get("url") or f"https://news.ycombinator.com/item?id={item.get('id')}",
            "summary": _strip_tags(item.get("text") or ""),
            "published_utc": float(item.get("time") or 0),
        })
        time.sleep(0.05)
    return out


def _fetch_reddit(sub: str) -> list[dict]:
    ok, text, _ = _http_get(REDDIT_JSON.format(sub=sub))
    if not ok:
        return []
    try:
        data = json.loads(text)
    except Exception:
        return []
    out: list[dict] = []
    for child in data.get("data", {}).get("children", []):
        d = child.get("data", {})
        out.append({
            "title": (d.get("title") or "")[:400],
            "url": "https://www.reddit.com" + d.get("permalink", ""),
            "summary": _strip_tags(d.get("selftext") or "")[:600],
            "published_utc": float(d.get("created_utc") or 0),
        })
    time.sleep(1.5)  # be nice
    return out


def fetch_source(src: dict) -> tuple[bool, list[dict], str]:
    """Returns (ok, items, error_msg). Empty items with ok=True is legal."""
    kind = src.get("kind")
    url = src.get("url", "")
    if kind == "rss":
        ok, text, err = _http_get(url)
        if not ok:
            return False, [], err
        return True, _parse_rss(text), ""
    if kind == "html":
        ok, text, err = _http_get(url)
        if not ok:
            return False, [], err
        return True, _parse_html_index(text, url), ""
    if kind == "hn_top":
        items = _fetch_hn_top(int(src.get("limit", 50)))
        return (True, items, "") if items else (False, [], "hn_empty")
    if kind == "reddit_json":
        items = _fetch_reddit(url)
        return (True, items, "") if items is not None else (False, [], "reddit_err")
    return False, [], f"unknown_kind:{kind}"


# ---------------------------------------------------------------------------
# Scoring
# ---------------------------------------------------------------------------
_REGEX_AXIS = {
    "build_opportunity": re.compile(r"\b(build|ship|opportunity|missing|no one has|niche|underserved)\b", re.I),
    "distribute_tactic": re.compile(r"\b(cold email|distribution|growth|acquire|virality|referral|seo)\b", re.I),
    "tool_adoption": re.compile(r"\b(claude|cursor|copilot|mcp|agent|framework|library|sdk|stack)\b", re.I),
    "market_signal": re.compile(r"\b(revenue|funding|valuation|acqui|acquisition|arr|price|pricing|market|billion|million)\b", re.I),
    "competitive_threat": re.compile(r"\b(compet|clone|launched|announcing|takes on|rival|entrant)\b", re.I),
    "hive_infra_pattern": re.compile(r"\b(orchestrat|agent loop|context engineering|durable|swarm|hive|multi-agent|memory|receipt)\b", re.I),
}


def regex_score(item: dict) -> tuple[str, float]:
    body = ((item.get("title") or "") + " " + (item.get("summary") or "")).lower()
    best_axis = "market_signal"
    best_hits = 0
    for axis, rx in _REGEX_AXIS.items():
        n = len(rx.findall(body))
        if n > best_hits:
            best_hits = n
            best_axis = axis
    # normalized "confidence" 0..1 based on hit density
    conf = min(1.0, best_hits / 6.0) if best_hits else 0.0
    return best_axis, conf


def _hash_seen(url: str) -> str:
    return hashlib.sha1(url.encode("utf-8", errors="replace")).hexdigest()[:16]


def _load_seen_urls() -> set[str]:
    if not SIGNAL_LOG.exists():
        return set()
    seen: set[str] = set()
    with SIGNAL_LOG.open("r", encoding="utf-8", errors="replace") as fh:
        for line in fh:
            line = line.strip()
            if not line:
                continue
            try:
                seen.add(json.loads(line).get("url", ""))
            except Exception:
                continue
    return seen


LITELLM_BACKOFFS = [2, 4, 8]  # seconds


def llm_score(item: dict, dry_run: bool) -> dict:
    """Returns {axis, relevance, novelty, actionability, hfo_action}.
    Falls back to regex on any failure."""
    axis_guess, conf = regex_score(item)
    if dry_run:
        return {
            "axis": axis_guess,
            "relevance": round(conf, 2),
            "novelty": 0.5,
            "actionability": 0.3,
            "hfo_action": "(dry-run: regex-only score, no LLM label)",
            "model": "dry_run",
        }

    prompt = (
        "You classify an article for a factory that builds micro-SaaS + open-source tools "
        "under the HFO gen-133 program. Return ONLY a JSON object, no prose.\n\n"
        "Schema:\n"
        '{"axis": "<one of: build_opportunity, distribute_tactic, tool_adoption, '
        'market_signal, competitive_threat, hive_infra_pattern>", '
        '"relevance": <0..1>, "novelty": <0..1>, "actionability": <0..1>, '
        '"hfo_action": "<one concrete action, <=120 chars>"}\n\n'
        f"TITLE: {item.get('title','')[:200]}\n"
        f"SUMMARY: {item.get('summary','')[:600]}\n"
        f"URL: {item.get('url','')}\n"
    )
    for attempt, backoff in enumerate([0] + LITELLM_BACKOFFS):
        if backoff:
            time.sleep(backoff)
        r = litellm_client.complete(prompt, max_tokens=200, temperature=0.2)
        if not r.ok:
            continue
        # accept fenced ```json ... ``` as well
        text = r.text.strip()
        m = re.search(r"\{.*\}", text, flags=re.S)
        if not m:
            continue
        try:
            parsed = json.loads(m.group(0))
            axis = parsed.get("axis") if parsed.get("axis") in AXES else axis_guess
            return {
                "axis": axis,
                "relevance": float(parsed.get("relevance", conf)),
                "novelty": float(parsed.get("novelty", 0.5)),
                "actionability": float(parsed.get("actionability", 0.3)),
                "hfo_action": str(parsed.get("hfo_action", ""))[:200],
                "model": r.model,
            }
        except Exception:
            continue
    # exhausted -> regex fallback
    return {
        "axis": axis_guess,
        "relevance": round(conf, 2),
        "novelty": 0.5,
        "actionability": 0.3,
        "hfo_action": "(llm_unavailable: regex-only fallback)",
        "model": "regex_fallback",
    }


def composite(row: dict) -> float:
    return round(
        float(row.get("relevance", 0)) * float(row.get("novelty", 0)) * float(row.get("actionability", 0)),
        4,
    )


# ---------------------------------------------------------------------------
# Seed injection
# ---------------------------------------------------------------------------
def _load_seed(path: Path | None) -> list[dict]:
    if not path or not path.exists():
        return []
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except Exception:
        return []
    urls = data.get("urls") or []
    now = _utc_now().timestamp()
    out = []
    for u in urls:
        host = urllib.parse.urlparse(u.get("url", "")).netloc
        summary = "(seeded — snippet-only, paywalled source)" if host in PAYWALL_HOSTS else "(operator-seeded URL, first-run guarantee)"
        out.append({
            "title": u.get("title") or u.get("url", ""),
            "url": u.get("url", ""),
            "summary": summary,
            "published_utc": now,
            "_seed_axis_hint": u.get("tag"),
            "_source_id": u.get("source_hint") or "seed",
            "_seeded": True,
        })
    return out


# ---------------------------------------------------------------------------
# Digest writers
# ---------------------------------------------------------------------------
def append_signal(sig: dict) -> None:
    SIGNAL_LOG.parent.mkdir(parents=True, exist_ok=True)
    with SIGNAL_LOG.open("a", encoding="utf-8", newline="\n") as fh:
        fh.write(json.dumps(sig, ensure_ascii=False, sort_keys=True) + "\n")


def build_daily_digest(signals: list[dict], day: str, threshold: float) -> Path:
    out = DIGEST_DIR / f"ARTICLE_DIGEST_{day}.md"
    out.parent.mkdir(parents=True, exist_ok=True)
    top = sorted(signals, key=composite, reverse=True)[:10]

    lines = [f"# Article Digest — {day}\n\n",
             f"**Signals kept (>= {threshold} composite):** {len(signals)}\n\n",
             "## Top 10 by (relevance × novelty × actionability)\n\n"]
    for i, s in enumerate(top, 1):
        lines.append(
            f"### {i}. [{s.get('title','(untitled)')[:140]}]({s.get('url','')})\n"
            f"- **source:** `{s.get('source_id','?')}` · **axis:** `{s.get('axis','?')}` · "
            f"**score:** {composite(s)} "
            f"(rel={s.get('relevance',0):.2f}, nov={s.get('novelty',0):.2f}, act={s.get('actionability',0):.2f})\n"
            f"- **hfo_action:** {s.get('hfo_action','') or '(none)'}\n"
            f"- **published:** {s.get('published_iso','?')}\n\n"
        )
    lines.append("## Per-axis coverage\n\n")
    axis_ct: dict[str, int] = {}
    for s in signals:
        axis_ct[s.get("axis", "?")] = axis_ct.get(s.get("axis", "?"), 0) + 1
    for axis in AXES:
        lines.append(f"- `{axis}` — {axis_ct.get(axis, 0)}\n")
    out.write_text("".join(lines), encoding="utf-8")
    return out


# ---------------------------------------------------------------------------
# Empty-streak halt tracking
# ---------------------------------------------------------------------------
EMPTY_STREAK = _FORGE / "state" / "factory_targets" / "article_scanner_empty_streak.json"


def _bump_empty_streak(had_signals: bool) -> int:
    rec = {}
    if EMPTY_STREAK.exists():
        try:
            rec = json.loads(EMPTY_STREAK.read_text(encoding="utf-8"))
        except Exception:
            rec = {}
    if had_signals:
        rec = {"streak": 0, "last_ok_utc": _utc_iso()}
    else:
        rec = {"streak": int(rec.get("streak", 0)) + 1, "last_ok_utc": rec.get("last_ok_utc")}
    EMPTY_STREAK.parent.mkdir(parents=True, exist_ok=True)
    EMPTY_STREAK.write_text(json.dumps(rec, indent=2, sort_keys=True), encoding="utf-8")
    return rec["streak"]


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--sources", type=Path, default=_HERE.parent / "sources.yaml")
    p.add_argument("--seed", type=Path, default=_HERE.parent / "seed_urls.json")
    p.add_argument("--window-hours", type=int, default=24)
    p.add_argument("--threshold", type=float, default=0.05,
                   help="min composite score to keep (default 0.05 — lenient)")
    p.add_argument("--dry-run", action="store_true", help="skip LLM classification")
    p.add_argument("--sources-only", type=str, default="",
                   help="comma-separated source ids to include (rest skipped)")
    p.add_argument("--no-slack", action="store_true", help="skip Slack post even if webhook is set")
    args = p.parse_args(argv)

    cfg = _load_yaml(args.sources)
    sources = [s for s in cfg.get("sources", []) if s.get("enabled", True)]
    if args.sources_only:
        keep = {s.strip() for s in args.sources_only.split(",") if s.strip()}
        sources = [s for s in sources if s.get("id") in keep]

    health = _load_health()
    chain_row.append_row(
        LOOP,
        action="start_scan",
        verifier_result=f"sources={len(sources)} window={args.window_hours}h threshold={args.threshold} dry_run={args.dry_run}",
        claim_status="proposed",
        remaining_risk=["rate_limit", "source_down", "llm_unavailable"],
        next_safe_action="fetch",
        honest_flaw="none",
        extra={"source_ids": [s.get("id") for s in sources]},
    )

    seen_urls = _load_seen_urls()
    window_cutoff = _utc_now().timestamp() - args.window_hours * 3600

    all_items: list[dict] = []

    # Fetch each source, honoring skip_until_utc
    for src in sources:
        sid = src.get("id", "?")
        if _is_skipped(sid, health):
            chain_row.append_row(
                LOOP, action="fetch_source",
                verifier_result=f"skipped (degraded): {sid}",
                claim_status="partial", remaining_risk=["source_degraded"],
                next_safe_action="wait_24h",
                honest_flaw=f"source {sid} exceeded 3 consecutive failures",
                extra={"source_id": sid, "skip_until_utc": health[sid].get("skip_until_utc")},
            )
            continue

        t0 = time.time()
        ok, items, err = fetch_source(src)
        ms = int((time.time() - t0) * 1000)
        _mark_source(sid, ok, health)

        if not ok:
            chain_row.append_row(
                LOOP, action="fetch_source",
                verifier_result=f"{sid}: failed ({err}) — streak={health[sid]['fail_streak']}",
                claim_status="partial", remaining_risk=["source_down"],
                next_safe_action="retry_next_run",
                honest_flaw=err,
                extra={"source_id": sid, "elapsed_ms": ms, "fail_streak": health[sid]["fail_streak"]},
            )
            continue

        # Attach source metadata + window filter
        keep = []
        for it in items:
            if it.get("published_utc") and it["published_utc"] < window_cutoff:
                continue
            it["_source_id"] = sid
            it["_source_name"] = src.get("name", sid)
            it["_source_tags"] = src.get("tags", [])
            keep.append(it)
        all_items.extend(keep)
        chain_row.append_row(
            LOOP, action="fetch_source",
            verifier_result=f"{sid}: {len(items)} items, kept {len(keep)} in window",
            claim_status="wired_with_receipts", remaining_risk=[],
            next_safe_action="score",
            honest_flaw="none",
            extra={"source_id": sid, "n_items": len(items), "n_in_window": len(keep), "elapsed_ms": ms},
        )

    _save_health(health)

    # Seed injection — force first-run appearance of operator URLs
    seed_items = _load_seed(args.seed)
    seed_injected = 0
    for s in seed_items:
        if s["url"] not in {i.get("url") for i in all_items} and s["url"] not in seen_urls:
            all_items.append(s)
            seed_injected += 1

    # Score + persist
    signals: list[dict] = []
    for it in all_items:
        if not it.get("url"):
            continue
        # Dedup against historical log
        if it["url"] in seen_urls:
            continue
        # Paywall-safe truncation
        host = urllib.parse.urlparse(it["url"]).netloc
        if host in PAYWALL_HOSTS:
            it["summary"] = (it.get("summary") or "")[:500] + " [paywall-snippet]"

        scored = llm_score(it, dry_run=args.dry_run)
        # Boost relevance floor for seeded operator picks
        if it.get("_seeded"):
            scored["relevance"] = max(scored["relevance"], 0.7)
            scored["novelty"] = max(scored["novelty"], 0.7)
            scored["actionability"] = max(scored["actionability"], 0.6)

        row = {
            "ts_utc": _utc_iso(),
            "url": it["url"],
            "url_hash": _hash_seen(it["url"]),
            "title": it.get("title", ""),
            "summary_first_500": (it.get("summary") or "")[:500],
            "source_id": it.get("_source_id", "?"),
            "source_name": it.get("_source_name", it.get("_source_id", "?")),
            "source_tags": it.get("_source_tags", []),
            "published_utc": it.get("published_utc") or None,
            "published_iso": (
                datetime.fromtimestamp(it["published_utc"], tz=timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
                if it.get("published_utc") else "unknown"
            ),
            "seeded": bool(it.get("_seeded")),
            **scored,
        }
        row["composite"] = composite(row)
        if row["composite"] < args.threshold and not row["seeded"]:
            continue
        append_signal(row)
        signals.append(row)

    day = _utc_today()
    digest = build_daily_digest(signals, day, args.threshold)
    empty_streak = _bump_empty_streak(bool(signals))

    # Slack headline
    slack_status = "skipped"
    if signals and not args.no_slack:
        top = sorted(signals, key=composite, reverse=True)[:3]
        headline = "\n".join([f"• *{s['axis']}* — <{s['url']}|{s['title'][:100]}>" for s in top])
        text = f":newspaper: `article_scanner` — {len(signals)} signals; top:\n{headline}\n_digest:_ `{digest.name}`"
        ok, status = slack_escalate.post(text)
        slack_status = f"posted={ok} status={status}"

    # Halt if 3d empty streak
    if empty_streak >= 3 and not signals:
        slack_escalate.escalate(
            LOOP, "3-DAY EMPTY DIGEST",
            f"article_scanner produced 0 signals for {empty_streak} consecutive days — check sources.yaml + LiteLLM proxy",
            severity="halt",
        )
        chain_row.append_row(
            LOOP, action="finish_scan",
            verifier_result=f"HALT: 0 signals × {empty_streak}d",
            claim_status="failed",
            remaining_risk=["operator_intervention_required"],
            next_safe_action="operator_inspect_sources_yaml_and_llm_config",
            honest_flaw="empty digest streak exceeded 3 days",
            extra={"digest": str(digest.relative_to(_FORGE)), "empty_streak_days": empty_streak,
                   "sources_scanned": len(sources), "seed_injected": seed_injected,
                   "slack": slack_status},
        )
        return 2

    status_final = "wired_with_receipts" if signals else "partial"
    chain_row.append_row(
        LOOP, action="finish_scan",
        verifier_result=f"{len(signals)} kept signals; digest={digest.name}; empty_streak={empty_streak}d",
        claim_status=status_final,
        remaining_risk=[] if signals else ["zero_signals_but_streak_ok"],
        next_safe_action="operator_review_digest",
        honest_flaw="none" if signals else "zero signals — patterns may be too narrow",
        extra={
            "n_items_fetched": len(all_items),
            "n_signals": len(signals),
            "digest": str(digest.relative_to(_FORGE)),
            "seed_injected": seed_injected,
            "empty_streak_days": empty_streak,
            "slack": slack_status,
        },
    )

    print(json.dumps({
        "n_sources": len(sources),
        "n_items_fetched": len(all_items),
        "n_signals": len(signals),
        "seed_injected": seed_injected,
        "digest": str(digest),
        "empty_streak_days": empty_streak,
        "slack": slack_status,
    }, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
