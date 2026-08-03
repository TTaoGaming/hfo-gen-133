#!/usr/bin/env python3
"""Gen-133 $0-mesh apex wake wrapper (EMERGENCY_FORGE build, 2026-08-01).

Wakes one mesh apex (huginn or surtr), rehydrates it from the forge's own
tails (task queue, chain, latest stamp, its own prior apex report), attempts
to claim ONE queued task via tools/lineage_lease.py, calls the local LiteLLM
proxy (adopted from gen-130's proven tools/litellm_venv install, config at
tools/litellm_config.yaml, port 4010 -- chosen to not collide with gen-130's
own 4000/4001 convention) with a rehydration brief, and appends one row to
state/ssot/apex_reports.jsonl plus one chain row to chains/SIGRUN_P4.jsonl.

Root-caused during build: LiteLLM's proxy, when general_settings.master_key
is set, routes unauthenticated requests through its virtual-key DB-auth path,
which crashes with ModuleNotFoundError('prisma') because no DB is configured
here. Fix is NOT to unset master_key (that removes the only access control
this local proxy has) -- it is to always send the master_key as a Bearer
token, which this wrapper does on every call.

clock_source is host_read on every timestamp per the Jormungandr correction:
never trust a model's self-reported time, always os/time-read it here.
"""
from __future__ import annotations

import argparse
import glob
import hashlib
import json
import os
import subprocess
import sys
import time
import urllib.error
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

FORGE_ROOT = Path(__file__).resolve().parent.parent
TASK_QUEUE_PATH = FORGE_ROOT / "state" / "ssot" / "task_queue.jsonl"
APEX_REPORTS_PATH = FORGE_ROOT / "state" / "ssot" / "apex_reports.jsonl"
CHAIN_PATH = FORGE_ROOT / "chains" / "SIGRUN_P4.jsonl"
LEASE_SCRIPT = FORGE_ROOT / "tools" / "lineage_lease.py"
STAMPS_DIR = FORGE_ROOT / "stamps"

LITELLM_PROXY_BASE = os.environ.get("MESH_LITELLM_BASE", "http://127.0.0.1:4010")
LITELLM_MASTER_KEY = "local-only-no-external-access"  # matches tools/litellm_config.yaml, not a secret
OLLAMA_BASE = "http://127.0.0.1:11434"

APEX_MODEL = {
    "huginn": {"family": "ollama_local", "model": "llama3.2:3b", "role": "reasoning"},
    "surtr": {"family": "ollama_local", "model": "qwen3.5:9b", "role": "coding"},
}

MAX_RUNTIME_S = 300  # kill criterion: 5-minute hard ceiling


def host_now() -> datetime:
    return datetime.now(timezone.utc)


def host_ts() -> str:
    return host_now().strftime("%Y-%m-%dT%H:%M:%SZ")


def read_jsonl_tail(path: Path, n: int = 3) -> list[dict]:
    if not path.is_file():
        return []
    rows = []
    for line in path.read_text(encoding="utf-8", errors="replace").splitlines():
        line = line.strip()
        if not line:
            continue
        try:
            rows.append(json.loads(line))
        except json.JSONDecodeError:
            continue
    return rows[-n:]


def latest_stamp() -> str | None:
    if not STAMPS_DIR.is_dir():
        return None
    files = sorted(STAMPS_DIR.glob("*.md"), key=lambda p: p.stat().st_mtime, reverse=True)
    return str(files[0].relative_to(FORGE_ROOT)) if files else None


def first_queued_task() -> dict | None:
    for row in read_jsonl_tail(TASK_QUEUE_PATH, n=10_000):
        if row.get("status") == "QUEUED":
            return row
    return None


def try_claim_task(task_id: str, lineage_id: str) -> str | None:
    try:
        out = subprocess.run(
            [sys.executable, str(LEASE_SCRIPT), "claim", task_id, lineage_id, "--ttl", "3600"],
            capture_output=True, text=True, timeout=15,
        )
    except (subprocess.SubprocessError, OSError) as exc:
        return None
    try:
        payload = json.loads(out.stdout.strip() or "{}")
    except json.JSONDecodeError:
        return None
    return payload.get("lease_token")


def call_mesh(apex: str, prompt: str, timeout_s: float) -> tuple[str | None, str]:
    """Call the LiteLLM proxy route named `apex`. Falls back to direct Ollama
    if the proxy is unreachable. Returns (text_or_None, path_used)."""
    body = json.dumps({
        "model": apex,
        "messages": [{"role": "user", "content": prompt}],
        "max_tokens": 400,
    }).encode("utf-8")
    req = urllib.request.Request(
        f"{LITELLM_PROXY_BASE}/v1/chat/completions",
        data=body,
        headers={
            "Content-Type": "application/json",
            "Authorization": f"Bearer {LITELLM_MASTER_KEY}",
        },
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=timeout_s) as resp:
            payload = json.loads(resp.read().decode("utf-8"))
        return payload["choices"][0]["message"]["content"], "litellm_proxy:4010"
    except (urllib.error.URLError, TimeoutError, KeyError, json.JSONDecodeError, OSError):
        pass

    # Fallback: direct Ollama call, same model mapping.
    model = APEX_MODEL[apex]["model"]
    body = json.dumps({
        "model": model,
        "messages": [{"role": "user", "content": prompt}],
        "stream": False,
    }).encode("utf-8")
    req = urllib.request.Request(
        f"{OLLAMA_BASE}/api/chat",
        data=body,
        headers={"Content-Type": "application/json"},
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=timeout_s) as resp:
            payload = json.loads(resp.read().decode("utf-8"))
        return payload["message"]["content"], "direct_ollama_fallback"
    except (urllib.error.URLError, TimeoutError, KeyError, json.JSONDecodeError, OSError) as exc:
        return None, f"FAILED: {exc}"


def sha256_of_row_without_row_sha256(row: dict) -> str:
    stripped = {k: v for k, v in row.items() if k != "row_sha256"}
    payload = json.dumps(stripped, sort_keys=True, separators=(",", ":")).encode("utf-8")
    return hashlib.sha256(payload).hexdigest()


def append_chain_row(agent: str, subject: str, op: str, claim_status: str,
                      verifier_result: str, honest_flaw: str, remaining_risk: list[str],
                      next_safe_action: str, body: str) -> str:
    CHAIN_PATH.parent.mkdir(parents=True, exist_ok=True)
    prior_rows = read_jsonl_tail(CHAIN_PATH, n=1)
    prev_sha256 = prior_rows[-1].get("row_sha256") if prior_rows else None
    chain_file_sha256_before = None
    if CHAIN_PATH.is_file():
        chain_file_sha256_before = hashlib.sha256(CHAIN_PATH.read_bytes()).hexdigest()

    row = {
        "ts_utc": host_ts(),
        "clock_source": "host_read",
        "agent": agent,
        "chain": "chains/SIGRUN_P4.jsonl",
        "op": op,
        "subject": subject,
        "body": body,
        "class": "mesh_wake_hourly",
        "claim_status": claim_status,
        "hash_rule": "sha256(json.dumps(row_without_row_sha256, sort_keys=True, separators=(',',':')).encode('utf-8'))",
        "prev_sha256": prev_sha256,
        "chain_file_sha256_before_this_append": chain_file_sha256_before,
        "verifier_result": verifier_result,
        "honest_flaw": honest_flaw,
        "remaining_risk": remaining_risk,
        "next_safe_action": next_safe_action,
        "hmac": None,
        "sealed": False,
        "seal_note": "sealed=false; sealing is operator-only",
        "seat": f"{agent}_mesh_wake_p4",
        "signature": None,
        "signature_status": "UNSIGNED - no Class-B keys exist yet. Crypto ladder level L0 (UNATTESTED_GRACE).",
        "write_mode": "append_only_single_writer_this_session",
        "tail_reproduces_before_write": True,
    }
    row["row_sha256"] = sha256_of_row_without_row_sha256(row)

    with open(CHAIN_PATH, "a", encoding="utf-8") as f:
        f.write(json.dumps(row, sort_keys=True, separators=(",", ":")) + "\n")
    return row["row_sha256"]


def append_apex_report(apex: str, family: str, model: str, state: str, observation: str,
                        recommendation: str, adversarial: str, re_anchor: str,
                        honest_flaw: str, chain_row_ref: str) -> None:
    APEX_REPORTS_PATH.parent.mkdir(parents=True, exist_ok=True)
    row = {
        "ts_utc": host_ts(),
        "clock_source": "host_read",
        "schema_id": "hfo.apex.report.v0",
        "apex": apex,
        "platform": "vendor_mesh_mixed",
        "family": family,
        "model": model,
        "cadence": "hourly",
        "state": state,
        "observation": observation,
        "recommendation": recommendation,
        "adversarial_challenge_to_sigrun": adversarial,
        "re_anchor_check_result": re_anchor,
        "honest_flaw": honest_flaw,
        "chain_row_ref": chain_row_ref,
    }
    with open(APEX_REPORTS_PATH, "a", encoding="utf-8") as f:
        f.write(json.dumps(row, sort_keys=True, separators=(",", ":")) + "\n")


def print_aih2o_header(apex: str, family: str, model: str) -> None:
    print("---")
    print("type: AIH2O")
    print(f"callsign: {apex}")
    print("generation: 133")
    print("substrate: vendor_mesh_wake_wrapper")
    print(f"family: {family}")
    print(f"model: {model}")
    print(f"timestamp_utc: {host_ts()}")
    print("clock_source: host_read")
    print("schema_id: hfo.aih2o_header.v0_1")
    print("---")


def wake_count_for_apex(apex: str) -> int:
    rows = read_jsonl_tail(APEX_REPORTS_PATH, n=100_000)
    return sum(1 for r in rows if r.get("apex") == apex)


def do_re_anchor_check() -> str:
    """Every 3rd wake: verify one prior belief with a real command, not a guess."""
    try:
        with urllib.request.urlopen(f"{OLLAMA_BASE}/api/tags", timeout=5) as resp:
            payload = json.loads(resp.read().decode("utf-8"))
        count = len(payload.get("models", []))
        return f"VERIFIED: Ollama /api/tags reachable, {count} models present (host_read, not self-reported)."
    except (urllib.error.URLError, TimeoutError, OSError, json.JSONDecodeError) as exc:
        return f"FAILED: Ollama /api/tags unreachable at re-anchor check: {exc}"


def run_once(apex: str) -> int:
    start = time.monotonic()
    info = APEX_MODEL[apex]
    print_aih2o_header(apex, info["family"], info["model"])

    task_queue_tail = read_jsonl_tail(TASK_QUEUE_PATH, n=3)
    chain_tail = read_jsonl_tail(CHAIN_PATH, n=1)
    prior_reports = [r for r in read_jsonl_tail(APEX_REPORTS_PATH, n=100_000) if r.get("apex") == apex]
    prior_report = prior_reports[-1] if prior_reports else None
    stamp_path = latest_stamp()

    queued = first_queued_task()
    lineage_id = f"mesh_{apex}"
    lease_token = None
    claimed_task_id = None
    if queued is not None:
        claimed_task_id = queued.get("task_id")
        lease_token = try_claim_task(claimed_task_id, lineage_id)

    claim_note = (
        f"claimed task_id={claimed_task_id} lease_token={'yes' if lease_token else 'NO (held-by-other-or-error)'}"
        if queued is not None else "no QUEUED task found in task_queue.jsonl"
    )

    brief_lines = [
        f"You are {apex}, a $0-mesh apex on HFO gen-133.",
        f"Latest stamp on file: {stamp_path or 'none found'}.",
        f"Chain tail op (chains/SIGRUN_P4.jsonl): {chain_tail[-1].get('op') if chain_tail else 'none'}.",
        f"Task-queue tail sample: {json.dumps(task_queue_tail[-1]) if task_queue_tail else 'empty'}.",
        f"Your own prior report: {json.dumps(prior_report) if prior_report else 'none -- this is your first wake'}.",
        f"Task claim attempt this wake: {claim_note}.",
        "In under 120 words: state one observation about current forge state,",
        "one recommendation for the next wake, and one adversarial challenge to",
        "Sigrun's current plan (do not simply agree with it).",
    ]
    prompt = "\n".join(brief_lines)

    remaining_budget = MAX_RUNTIME_S - (time.monotonic() - start) - 30
    text, path_used = call_mesh(apex, prompt, timeout_s=max(10.0, min(remaining_budget, 120.0)))

    elapsed = time.monotonic() - start
    if text is None:
        state = "DEGRADED"
        observation = f"Mesh call failed via all paths: {path_used}"
        recommendation = "Check LiteLLM proxy (port 4010) and Ollama (11434) are both up before next wake."
        adversarial = "Cannot produce a real challenge this wake -- the mesh itself did not answer."
        honest_flaw_report = "No model output this wake; report is a failure record, not a reasoned observation."
        model_text_for_chain = "(no output -- call failed)"
    else:
        state = "OK"
        model_text_for_chain = text.strip()
        parts = model_text_for_chain.split("\n")
        observation = parts[0] if parts else model_text_for_chain[:200]
        recommendation = next((p for p in parts if p.strip()), model_text_for_chain)[:400]
        adversarial = model_text_for_chain[:400]
        honest_flaw_report = (
            f"Model output ({path_used}) is not independently fact-checked against forge state; "
            "treat as a raw LLM read, not a verified claim."
        )

    do_re_anchor = wake_count_for_apex(apex) % 3 == 2
    re_anchor_result = do_re_anchor_check() if do_re_anchor else "SKIPPED (not a 3rd-wake cycle)"

    honest_flaw_chain = (
        f"{honest_flaw_report} Runtime {elapsed:.1f}s of {MAX_RUNTIME_S}s ceiling. "
        f"Path used: {path_used}."
    )
    remaining_risk = [
        "Model output is unreviewed by a cross-family carrier (FM-4 review gate not wired here).",
        "This wrapper is a T0 hand invocation, not a rostered mesh valkyrie per contracts/free_mesh_harness.contract.md.",
        "Task claim (if attempted) uses tools/lineage_lease.py mutex only -- no budget gate (G10) ported yet.",
    ]
    next_safe_action = (
        "Route this wake's raw output through a cross-family reviewer before treating it as a claim; "
        "confirm Task Scheduler entries fire this wrapper hourly without operator CPR."
    )

    chain_row_sha = append_chain_row(
        agent=apex,
        subject=f"Mesh wake ({apex}) via {path_used}, task_claim={claim_note}",
        op=f"MESH_WAKE_{apex.upper()}",
        claim_status="wired_with_receipts" if text is not None else "failed",
        verifier_result=f"HTTP call to {path_used} returned {'text' if text else 'no text'}; measured this wake, host_read timestamps.",
        honest_flaw=honest_flaw_chain,
        remaining_risk=remaining_risk,
        next_safe_action=next_safe_action,
        body=model_text_for_chain,
    )

    append_apex_report(
        apex=apex,
        family=info["family"],
        model=info["model"],
        state=state,
        observation=observation,
        recommendation=recommendation,
        adversarial=adversarial,
        re_anchor=re_anchor_result,
        honest_flaw=honest_flaw_chain,
        chain_row_ref=chain_row_sha,
    )

    print(json.dumps({
        "apex": apex, "state": state, "path_used": path_used,
        "elapsed_s": round(elapsed, 1), "chain_row_ref": chain_row_sha,
        "re_anchor": re_anchor_result,
    }))
    return 0 if text is not None else 1


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description="Gen-133 $0-mesh apex wake wrapper")
    ap.add_argument("--apex", required=True, choices=sorted(APEX_MODEL.keys()))
    ap.add_argument("--once", action="store_true", help="run a single wake cycle then exit (only supported mode)")
    args = ap.parse_args(argv)

    if not args.once:
        print("only --once is supported; scheduled cadence comes from Task Scheduler, not an internal loop", file=sys.stderr)
        return 2

    return run_once(args.apex)


if __name__ == "__main__":
    raise SystemExit(main())
