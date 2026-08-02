#!/usr/bin/env python3
"""multi_family_vote.py — the quorum engine behind the Olrun facade.

Sends ONE prompt to N model families INDEPENDENTLY and gathers structured
adversarial votes on whether a memory capsule should be carried into gen-133.

INDEPENDENCE IS THE POINT (structural, not aspirational):

  * `build_family_payload(family_key, base_prompt)` is the ONLY payload
    constructor. Its signature can physically see exactly two things: the key
    of the family being built, and the single shared base prompt. It has no
    parameter through which another family's name, model, or response could
    arrive.
  * The base prompt is rendered ONCE, before any family is contacted, and is
    passed by value to every family. No family's output is ever fed back into
    prompt construction.
  * Families are dispatched CONCURRENTLY via a thread pool, so there is no
    sequential ordering for one family's answer to leak into the next one's
    input.
  * `tools/tests/test_multi_family_vote.py::test_payloads_are_mutually_blind`
    asserts this by construction.

No hard third-party dependencies: stdlib urllib.request + json only.

Subcommands
  families   probe each configured family; JSON to stdout; exit 0 iff >=1 up
  vote       gather independent votes on a capsule; write votes JSON
  apply      write quorum result back into the capsule's frontmatter
"""

from __future__ import annotations

import argparse
import concurrent.futures
import json
import re
import sys
import time
import urllib.error
import urllib.request
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path

FORGE_ROOT = Path(__file__).resolve().parent.parent.parent

OLLAMA_BASE = "http://127.0.0.1:11434"
LITELLM_BASE = "http://127.0.0.1:4001"
# Matches tools/litellm_config.yaml general_settings.master_key. Local-only
# loopback sentinel, not a secret.
LITELLM_MASTER_KEY = "local-only-no-external-access"

DEFAULT_TIMEOUT_S = 120.0
VALID_VERDICTS = ("keep", "drop", "repair")

# Below this many PARSED votes, no concurrence score is reported. Agreement is a
# property of a group; it cannot be measured on a sample of one.
MIN_VOTES_FOR_CONCURRENCE = 2

# Concurrency is for isolation, not speed. Independence comes from payload
# construction, so throttling is always safe. It is also necessary: every
# ollama_* family shares ONE local Ollama host, which serializes model loads.
# Measured on this host — firing 9 families at once queued 9 model loads and
# every request blew a 90s timeout. Keep this small on single-GPU hosts.
DEFAULT_MAX_PARALLEL = 2

# ---------------------------------------------------------------------------
# Family registry.
#
# A "family" is a distinct MODEL FAMILY, not a distinct size of one model.
# Adversarial quorum only means something across families that were pretrained
# separately; two checkpoints of one family share their blind spots and their
# agreement is consensus drift, not concurrence.
#
# `arch` records the underlying pretraining family reported by Ollama, so a
# caller can tell at a glance when two configured families are secretly kin.
# ---------------------------------------------------------------------------
FAMILIES: dict[str, dict] = {
    "ollama_granite":  {"kind": "ollama", "model": "granite3.3:8b",  "arch": "granite",  "endpoint": OLLAMA_BASE},
    "ollama_mistral":  {"kind": "ollama", "model": "ministral-3:8b", "arch": "mistral3", "endpoint": OLLAMA_BASE},
    "ollama_llama":    {"kind": "ollama", "model": "llama3.2:3b",    "arch": "llama",    "endpoint": OLLAMA_BASE},
    "ollama_qwen":     {"kind": "ollama", "model": "qwen3.5:9b",     "arch": "qwen35",   "endpoint": OLLAMA_BASE},
    "ollama_gemma":    {"kind": "ollama", "model": "gemma4:e4b",     "arch": "gemma4",   "endpoint": OLLAMA_BASE},
    "ollama_phi":      {"kind": "ollama", "model": "phi4-mini:3.8b", "arch": "phi3",     "endpoint": OLLAMA_BASE},
    "ollama_falcon":   {"kind": "ollama", "model": "falcon3:7b",     "arch": "falcon3",  "endpoint": OLLAMA_BASE},
    "ollama_deepseek": {"kind": "ollama", "model": "deepseek-r1:7b", "arch": "qwen2",    "endpoint": OLLAMA_BASE},
    # llama4:scout is deliberately NOT registered: 67GB, OOMs on this host.
    "litellm_gemini_flash": {
        "kind": "litellm", "model": "nidhoggr-gemini-flash", "arch": "gemini",
        "endpoint": LITELLM_BASE,
    },
}

DEFAULT_FAMILIES = "ollama_granite,ollama_mistral"

# ---------------------------------------------------------------------------
# THE VOTING PROMPT. One constant. Rendered once. Shared verbatim by every
# family. Nothing family-specific is ever interpolated into it.
# ---------------------------------------------------------------------------
VOTE_PROMPT_TEMPLATE = """You are an independent reviewer casting ONE vote, ALONE.
You cannot see any other reviewer's vote. Do not guess what another reviewer
would say, and do not try to agree with anyone. Your value here is your
independence.

MEMORY CAPSULE UNDER REVIEW
title: {title}
abstract:
{abstract}

QUESTION
Should this memory be carried forward into generation 133?
  keep   = carry it forward as-is; it is grounded and still true
  drop   = do not carry it forward; it is wrong, stale, or worthless
  repair = worth keeping, but unproven, overstated, or mis-scoped, and must be
           rewritten before it is carried forward

Also name the single most important HONEST FLAW: what is wrong, unproven, or
unverified about this memory. Do not flatter it. A vote that names no flaw is a
failed vote.

REPLY FORMAT
Reply with JSON ONLY. No prose, no explanation, no markdown fences, no preamble,
no trailing commentary. Exactly this object and nothing else:
{{"verdict":"keep|drop|repair","confidence":0.0-1.0,"honest_flaw":"<what is wrong or unproven about this memory>"}}
"""


def host_now_utc() -> str:
    """Host clock read. clock_source=host_read, never generated."""
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


# ---------------------------------------------------------------------------
# JSON extraction — survives fences, preamble prose, and reasoning models.
# ---------------------------------------------------------------------------

_FENCE_RE = re.compile(r"```(?:json|JSON)?\s*\n(.*?)(?:\n\s*```|$)", re.DOTALL)


def _balanced_object_slices(text: str):
    """Yield every balanced {...} slice, outermost-first, string-aware."""
    for start in (i for i, ch in enumerate(text) if ch == "{"):
        depth = 0
        in_str = False
        esc = False
        for i in range(start, len(text)):
            ch = text[i]
            if in_str:
                if esc:
                    esc = False
                elif ch == "\\":
                    esc = True
                elif ch == '"':
                    in_str = False
                continue
            if ch == '"':
                in_str = True
            elif ch == "{":
                depth += 1
            elif ch == "}":
                depth -= 1
                if depth == 0:
                    yield text[start:i + 1]
                    break


def extract_json(text: str | None) -> dict | None:
    """Best-effort extraction of a single JSON OBJECT from model output.

    Handles, in order: clean JSON, ```json fenced JSON, JSON preceded or
    followed by prose (including <think> blocks). Returns None for anything
    that does not yield a JSON object — never raises, never guesses.
    """
    if not text or not isinstance(text, str):
        return None

    def _try(candidate: str) -> dict | None:
        try:
            parsed = json.loads(candidate)
        except (json.JSONDecodeError, ValueError):
            return None
        return parsed if isinstance(parsed, dict) else None

    direct = _try(text.strip())
    if direct is not None:
        return direct

    for block in _FENCE_RE.findall(text):
        got = _try(block.strip())
        if got is not None:
            return got
        for slice_ in _balanced_object_slices(block):
            got = _try(slice_)
            if got is not None:
                return got

    for slice_ in _balanced_object_slices(text):
        got = _try(slice_)
        if got is not None:
            return got

    return None


def normalize_vote(obj: dict | None) -> dict | None:
    """Coerce a parsed object into the vote contract, or None if it does not
    carry a usable verdict. Confidence is clamped; a missing/garbage
    confidence degrades to 0.0 rather than failing the whole vote."""
    if not isinstance(obj, dict):
        return None
    raw_verdict = obj.get("verdict")
    if not isinstance(raw_verdict, str):
        return None
    verdict = raw_verdict.strip().lower()
    if verdict not in VALID_VERDICTS:
        return None
    try:
        confidence = float(obj.get("confidence", 0.0))
    except (TypeError, ValueError):
        confidence = 0.0
    confidence = max(0.0, min(1.0, confidence))
    flaw = obj.get("honest_flaw", "")
    if not isinstance(flaw, str):
        flaw = json.dumps(flaw, ensure_ascii=False)
    return {"verdict": verdict, "confidence": confidence, "honest_flaw": flaw.strip()}


# ---------------------------------------------------------------------------
# Concurrence math.
# ---------------------------------------------------------------------------

def compute_concurrence(votes: list[dict]) -> tuple[float | None, str | None]:
    """(concurrence_score, modal_verdict) over votes with parse_ok=True.

    Zero parsed votes yields (None, None) — NOT a ZeroDivisionError, and NOT a
    false 0.0 that would read as 'the families disagreed'.
    """
    parsed = [v.get("verdict") for v in votes if v.get("parse_ok") and v.get("verdict")]
    if not parsed:
        return None, None
    if len(parsed) < MIN_VOTES_FOR_CONCURRENCE:
        # One vote is not a quorum. Returning 1.0 here would report perfect
        # cross-family agreement from a single model that happened to answer
        # while its peers timed out -- a fabricated consensus, and the most
        # dangerous possible output of a tool built to detect disagreement.
        # The verdict is still surfaced; the AGREEMENT score is withheld.
        return None, parsed[0]
    counts = Counter(parsed)
    top = max(counts.values())
    # Deterministic tie-break: VALID_VERDICTS order, so the same votes always
    # produce the same modal verdict regardless of arrival order.
    modal = sorted((v for v, c in counts.items() if c == top),
                   key=lambda v: VALID_VERDICTS.index(v))[0]
    return round(top / len(parsed), 3), modal


# ---------------------------------------------------------------------------
# Payload construction — the independence boundary.
# ---------------------------------------------------------------------------

def build_family_payload(family_key: str, base_prompt: str) -> dict:
    """Build the wire payload for ONE family.

    Deliberately narrow signature: this function can see the family it is
    building and the single shared base prompt. There is no parameter through
    which another family's identity, payload, or response could enter, so
    cross-family leakage is impossible by construction rather than by
    convention.
    """
    cfg = FAMILIES[family_key]
    if cfg["kind"] == "ollama":
        return {
            "url": f"{cfg['endpoint']}/api/chat",
            "headers": {"Content-Type": "application/json"},
            "body": {
                "model": cfg["model"],
                "messages": [{"role": "user", "content": base_prompt}],
                "stream": False,
                "format": "json",
                "options": {"temperature": 0, "num_predict": 400},
            },
        }
    if cfg["kind"] == "litellm":
        return {
            "url": f"{cfg['endpoint']}/v1/chat/completions",
            "headers": {
                "Content-Type": "application/json",
                "Authorization": f"Bearer {LITELLM_MASTER_KEY}",
            },
            "body": {
                "model": cfg["model"],
                "messages": [{"role": "user", "content": base_prompt}],
                "max_tokens": 400,
                "temperature": 0,
            },
        }
    raise ValueError(f"unknown family kind: {cfg['kind']}")


def _extract_text(kind: str, payload: dict) -> str:
    """Pull the model's text, tolerating reasoning-model response shapes.

    Reasoning models (qwen3.5, deepseek-r1, ...) return their answer under
    `thinking` / `reasoning_content` and leave `content` EMPTY. Reading only
    `content` scored those models as 100% parse failures -- qwen3.5:9b was 8/8
    unparseable with `raw: ''` while Ollama reported done_reason=stop and
    eval_count=34, i.e. it answered perfectly and we threw the answer away.

    That silently excluded exactly the models most likely to actually judge
    rather than apply a constant prior, which biased the quorum toward the
    degenerate voters. A parse failure and an empty read look identical
    downstream, so this has to be handled here.
    """
    if kind == "ollama":
        msg = payload.get("message") or {}
        for key in ("content", "thinking", "reasoning_content"):
            val = msg.get(key)
            if isinstance(val, str) and val.strip():
                return val
        # /api/generate shape (non-chat) uses top-level keys.
        for key in ("response", "thinking"):
            val = payload.get(key)
            if isinstance(val, str) and val.strip():
                return val
        return ""
    choice = payload["choices"][0]
    msg = choice.get("message") or {}
    for key in ("content", "reasoning_content", "thinking"):
        val = msg.get(key)
        if isinstance(val, str) and val.strip():
            return val
    return ""


def call_family(family_key: str, base_prompt: str, timeout_s: float) -> dict:
    """Send the shared prompt to ONE family. Never raises.

    Returns {"text": str|None, "error": str|None, "latency_ms": float}.
    """
    cfg = FAMILIES[family_key]
    payload = build_family_payload(family_key, base_prompt)
    req = urllib.request.Request(
        payload["url"],
        data=json.dumps(payload["body"]).encode("utf-8"),
        headers=payload["headers"],
        method="POST",
    )
    started = time.monotonic()
    try:
        with urllib.request.urlopen(req, timeout=timeout_s) as resp:
            body = json.loads(resp.read().decode("utf-8", errors="replace"))
        text = _extract_text(cfg["kind"], body)
        return {"text": text, "error": None,
                "latency_ms": round((time.monotonic() - started) * 1000, 1)}
    except urllib.error.HTTPError as exc:
        err = f"HTTP {exc.code}"
    except urllib.error.URLError as exc:
        err = f"URLError: {exc.reason}"
    except (TimeoutError, OSError) as exc:
        err = f"{type(exc).__name__}: {exc}"
    except (KeyError, TypeError, json.JSONDecodeError) as exc:
        err = f"malformed response: {type(exc).__name__}: {exc}"
    return {"text": None, "error": err,
            "latency_ms": round((time.monotonic() - started) * 1000, 1)}


# ---------------------------------------------------------------------------
# Probing.
# ---------------------------------------------------------------------------

def probe_family(family_key: str, timeout_s: float = 10.0, deep: bool = False) -> dict:
    """Runtime reachability probe.

    Two strengths, and the output ALWAYS says which one ran, because a listing
    check is not a generation check:

      shallow (default, probe_method=listing)
          the endpoint answers and the model/route appears in its catalogue.
          Cheap. Does NOT prove the model will actually generate: a route can
          be served with a dead API key behind it, and a model can be pulled
          but OOM on load. Measured on this host: litellm_gemini_flash lists
          fine and then HTTP 500s on every real call.

      deep (--deep, probe_method=live_generation)
          a real minimal generation. Slower, and the only one that earns the
          word "reachable" without a caveat.
    """
    cfg = FAMILIES[family_key]
    result = {"reachable": False, "endpoint": cfg["endpoint"], "model": cfg["model"],
              "arch": cfg["arch"], "latency_ms": None, "error": None,
              "probe_method": "live_generation" if deep else "listing"}

    if deep:
        started = time.monotonic()
        outcome = call_family(family_key, "Reply with the single word: ok", timeout_s)
        result["latency_ms"] = outcome["latency_ms"]
        if outcome["error"] is None and (outcome["text"] or "").strip():
            result["reachable"] = True
        else:
            result["error"] = outcome["error"] or "empty generation"
        return result

    started = time.monotonic()
    try:
        if cfg["kind"] == "ollama":
            req = urllib.request.Request(f"{cfg['endpoint']}/api/tags", method="GET")
            with urllib.request.urlopen(req, timeout=timeout_s) as resp:
                tags = json.loads(resp.read().decode("utf-8", errors="replace"))
            present = {m.get("name") for m in tags.get("models", [])}
            result["latency_ms"] = round((time.monotonic() - started) * 1000, 1)
            if cfg["model"] in present:
                result["reachable"] = True
            else:
                result["error"] = f"endpoint up but model {cfg['model']} not pulled"
        else:
            req = urllib.request.Request(
                f"{cfg['endpoint']}/v1/models", method="GET",
                headers={"Authorization": f"Bearer {LITELLM_MASTER_KEY}"},
            )
            with urllib.request.urlopen(req, timeout=timeout_s) as resp:
                models = json.loads(resp.read().decode("utf-8", errors="replace"))
            result["latency_ms"] = round((time.monotonic() - started) * 1000, 1)
            ids = {m.get("id") for m in models.get("data", [])}
            if cfg["model"] in ids:
                result["reachable"] = True
                result["caveat"] = ("route listed only; upstream key/quota unverified. "
                                    "re-run with --deep to actually generate.")
            else:
                result["error"] = f"proxy up but route {cfg['model']} not served"
    except urllib.error.HTTPError as exc:
        result["latency_ms"] = round((time.monotonic() - started) * 1000, 1)
        result["error"] = f"HTTP {exc.code}"
    except (urllib.error.URLError, TimeoutError, OSError, json.JSONDecodeError) as exc:
        result["latency_ms"] = round((time.monotonic() - started) * 1000, 1)
        result["error"] = f"{type(exc).__name__}: {exc}"
    return result


# ---------------------------------------------------------------------------
# Capsule reading / frontmatter surgery.
# ---------------------------------------------------------------------------

def split_frontmatter(text: str) -> tuple[str | None, list[str], str]:
    """(style, frontmatter_lines, body).

    style is 'dashes' (--- ... ---), 'yamlfence' (```yaml ... ```), or None.
    Joining the pieces back must reproduce the file byte-for-byte in the body
    portion; the body is returned untouched.
    """
    lines = text.splitlines(keepends=True)
    if not lines:
        return None, [], text
    first = lines[0].strip()
    if first == "---":
        for i in range(1, len(lines)):
            if lines[i].strip() == "---":
                return "dashes", [l.rstrip("\n").rstrip("\r") for l in lines[1:i]], "".join(lines[i + 1:])
        return None, [], text
    if first in ("```yaml", "```YAML"):
        for i in range(1, len(lines)):
            if lines[i].strip() == "```":
                return "yamlfence", [l.rstrip("\n").rstrip("\r") for l in lines[1:i]], "".join(lines[i + 1:])
        return None, [], text
    return None, [], text


def upsert_frontmatter(fm_lines: list[str], updates: dict[str, str]) -> list[str]:
    """Replace existing top-level keys in place; append the rest in order."""
    out = list(fm_lines)
    for key, value in updates.items():
        line = f"{key}: {value}"
        pattern = re.compile(rf"^{re.escape(key)}\s*:")
        for idx, existing in enumerate(out):
            if pattern.match(existing):
                out[idx] = line
                break
        else:
            out.append(line)
    return out


def render_capsule(style: str, fm_lines: list[str], body: str) -> str:
    fm = "\n".join(fm_lines)
    if style == "yamlfence":
        return f"```yaml\n{fm}\n```\n{body}"
    return f"---\n{fm}\n---\n{body}"


def capsule_title_and_abstract(path: Path, max_abstract_chars: int = 2400) -> tuple[str, str]:
    text = path.read_text(encoding="utf-8", errors="replace")
    _, fm_lines, body = split_frontmatter(text)

    title = None
    for line in body.splitlines():
        if line.startswith("# "):
            title = line[2:].strip()
            break
    if not title:
        for line in fm_lines:
            m = re.match(r"^(?:title|doc|schema_id)\s*:\s*(.+)$", line)
            if m:
                title = m.group(1).strip()
                break
    if not title:
        title = path.stem

    abstract = body.strip()
    if not abstract:
        abstract = "\n".join(fm_lines).strip()
    if len(abstract) > max_abstract_chars:
        abstract = abstract[:max_abstract_chars].rstrip() + "\n[...capsule truncated for review...]"
    return title, abstract


def build_base_prompt(title: str, abstract: str) -> str:
    """Render THE shared prompt. Called exactly once per vote run; the result
    is passed by value to every family."""
    return VOTE_PROMPT_TEMPLATE.format(title=title, abstract=abstract)


# ---------------------------------------------------------------------------
# Subcommands.
# ---------------------------------------------------------------------------

def resolve_families(spec: str) -> list[str]:
    keys = [k.strip() for k in spec.split(",") if k.strip()]
    unknown = [k for k in keys if k not in FAMILIES]
    if unknown:
        raise SystemExit(f"unknown families: {unknown}. known: {sorted(FAMILIES)}")
    seen, ordered = set(), []
    for k in keys:
        if k not in seen:
            seen.add(k)
            ordered.append(k)
    return ordered


def cmd_families(args) -> int:
    keys = resolve_families(args.families) if args.families else sorted(FAMILIES)
    timeout = args.timeout if not args.deep else max(args.timeout, 60.0)
    # A deep probe GENERATES, so it must respect the same throttle as voting;
    # an unthrottled deep probe is what saturated Ollama during bring-up.
    workers = min(args.max_parallel, len(keys)) if args.deep else len(keys)
    with concurrent.futures.ThreadPoolExecutor(max_workers=max(1, workers)) as pool:
        results = dict(zip(keys, pool.map(lambda k: probe_family(k, timeout, args.deep), keys)))
    print(json.dumps(results, indent=2, sort_keys=True))
    return 0 if any(r["reachable"] for r in results.values()) else 1


def gather_votes(capsule_path: Path, family_keys: list[str], timeout_s: float,
                 max_parallel: int = DEFAULT_MAX_PARALLEL) -> dict:
    title, abstract = capsule_title_and_abstract(capsule_path)

    # Rendered ONCE, before any family is contacted. Every family receives this
    # exact string and nothing else. There is no per-family prompt mutation.
    base_prompt = build_base_prompt(title, abstract)

    def one(family_key: str) -> dict:
        outcome = call_family(family_key, base_prompt, timeout_s)
        vote = {
            "family": family_key,
            "model": FAMILIES[family_key]["model"],
            "arch": FAMILIES[family_key]["arch"],
            "verdict": None,
            "confidence": None,
            "honest_flaw": None,
            "raw": outcome["text"] or "",
            "parse_ok": False,
            "latency_ms": outcome["latency_ms"],
            "error": outcome["error"],
        }
        normalized = normalize_vote(extract_json(outcome["text"]))
        if normalized:
            vote.update(normalized)
            vote["parse_ok"] = True
        elif outcome["text"] is not None and outcome["error"] is None:
            vote["error"] = "unparseable response (no usable verdict JSON)"
        return vote

    # Concurrent dispatch, throttled. Independence does not depend on the
    # worker count: `one` closes over the shared base_prompt only, so families
    # remain mutually blind at any level of parallelism, including 1.
    workers = max(1, min(max_parallel, len(family_keys)))
    with concurrent.futures.ThreadPoolExecutor(max_workers=workers) as pool:
        votes = list(pool.map(one, family_keys))

    score, modal = compute_concurrence(votes)
    unreachable = [v["family"] for v in votes if v["raw"] == "" and v["error"]]
    return {
        "capsule_id": capsule_path.stem,
        "capsule_path": str(capsule_path).replace("\\", "/"),
        "capsule_title": title,
        "votes": votes,
        "concurrence_score": score,
        "modal_verdict": modal,
        "voted_utc": host_now_utc(),
        "clock_source": "host_read",
        "families_requested": family_keys,
        "families_unreachable": unreachable,
        "families_parse_failed": [
            v["family"] for v in votes if not v["parse_ok"] and v["family"] not in unreachable
        ],
    }


def cmd_vote(args) -> int:
    capsule_path = Path(args.capsule).resolve()
    if not capsule_path.is_file():
        print(json.dumps({"error": f"capsule not found: {capsule_path}"}), file=sys.stderr)
        return 2
    result = gather_votes(capsule_path, resolve_families(args.families),
                          args.timeout, args.max_parallel)
    blob = json.dumps(result, indent=2, ensure_ascii=False)
    if args.out:
        out_path = Path(args.out).resolve()
        out_path.parent.mkdir(parents=True, exist_ok=True)
        out_path.write_text(blob + "\n", encoding="utf-8")
        print(f"wrote {out_path}", file=sys.stderr)
    print(blob)
    # Truthful-red: zero parsed votes is a failed run even though the process
    # completed without an exception.
    #
    # Keyed on PARSED VOTES, not on concurrence_score. Since
    # MIN_VOTES_FOR_CONCURRENCE=2, a deliberate single-family run always has
    # concurrence None -- keying exit status on that reported every per-family
    # sweep as a total failure (ok=0/100) while writing 100 perfectly good vote
    # files. The exit code must track whether a vote was obtained, not whether
    # enough votes existed to measure agreement between them.
    n_parsed = sum(1 for v in result.get("votes", []) if v.get("parse_ok"))
    return 0 if n_parsed else 1


def cmd_apply(args) -> int:
    votes_path = Path(args.votes).resolve()
    if not votes_path.is_file():
        print(json.dumps({"error": f"votes file not found: {votes_path}"}), file=sys.stderr)
        return 2
    result = json.loads(votes_path.read_text(encoding="utf-8"))

    capsule_path = Path(args.capsule).resolve() if args.capsule else Path(result["capsule_path"]).resolve()
    if not capsule_path.is_file():
        print(json.dumps({"error": f"capsule not found: {capsule_path}"}), file=sys.stderr)
        return 2

    text = capsule_path.read_text(encoding="utf-8")
    style, fm_lines, body = split_frontmatter(text)
    if style is None:
        style, fm_lines, body = "dashes", [], text

    summary = ", ".join(
        f"{v['family']}={v['verdict']}@{v['confidence']:.2f}"
        for v in result["votes"] if v.get("parse_ok")
    ) or "none_parsed"
    score = result.get("concurrence_score")
    updates = {
        "quorum_votes": f'"{summary}"',
        "concurrence_score": "null" if score is None else f"{score}",
        "modal_verdict": result.get("modal_verdict") or "null",
        "quorum_voted_utc": result.get("voted_utc", host_now_utc()),
        "clock_source": result.get("clock_source", "host_read"),
    }
    new_text = render_capsule(style, upsert_frontmatter(fm_lines, updates), body)
    capsule_path.write_text(new_text, encoding="utf-8")

    print(json.dumps({
        "capsule": str(capsule_path).replace("\\", "/"),
        "frontmatter_style": style,
        "applied": {k: v.strip('"') for k, v in updates.items()},
        "body_bytes_preserved": len(body),
    }, indent=2))
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="multi_family_vote",
        description="Independent adversarial cross-family quorum over memory capsules.",
    )
    sub = parser.add_subparsers(dest="cmd", required=True)

    p_fam = sub.add_parser("families", help="probe configured families (runtime probe)")
    p_fam.add_argument("--families", default=None, help="comma-separated subset; default all")
    p_fam.add_argument("--timeout", type=float, default=10.0)
    p_fam.add_argument("--deep", action="store_true",
                       help="actually generate instead of trusting the catalogue listing")
    p_fam.add_argument("--max-parallel", type=int, default=DEFAULT_MAX_PARALLEL,
                       dest="max_parallel", help="only applies to --deep")
    p_fam.set_defaults(func=cmd_families)

    p_vote = sub.add_parser("vote", help="gather independent votes on a capsule")
    p_vote.add_argument("--capsule", required=True)
    p_vote.add_argument("--families", default=DEFAULT_FAMILIES)
    p_vote.add_argument("--out", default=None)
    p_vote.add_argument("--timeout", type=float, default=DEFAULT_TIMEOUT_S)
    p_vote.add_argument("--max-parallel", type=int, default=DEFAULT_MAX_PARALLEL,
                        dest="max_parallel",
                        help="concurrent families; local Ollama serializes model loads")
    p_vote.set_defaults(func=cmd_vote)

    p_apply = sub.add_parser("apply", help="write quorum result into capsule frontmatter")
    p_apply.add_argument("--votes", required=True)
    p_apply.add_argument("--capsule", default=None, help="override; default from votes JSON")
    p_apply.set_defaults(func=cmd_apply)

    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    return args.func(args)


if __name__ == "__main__":
    sys.exit(main())
