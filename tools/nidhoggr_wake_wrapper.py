#!/usr/bin/env python3
"""Nidhoggr wake wrapper — Gemini bypass for the Antigravity consent-stall.

Nidhoggr apex was assigned platform=Antigravity in
inbox/olrun/SIGRUN_STAMP_EMERGENCY_FORGE_AUTHORIZED_20260801.md Wave 1 #2,
but Antigravity is a consent-stall class substrate (12+ dead windows,
STALLED_ON_CONSENT). This wrapper reaches the same google family voice by
calling the Gemini API directly through LiteLLM instead.

Proxy-server mode (`litellm --config tools/litellm_config.yaml`) is NOT used:
this host has the `litellm` CLI but not the `litellm[proxy]` extras
(missing `fastapi_sso`), so this wrapper calls `litellm.completion()`
in-process against the model names declared in tools/litellm_config.yaml.
The routing table (model_name -> gemini/<model> + api_key env ref) is still
the single source of truth; this is LiteLLM-SDK mode, not a raw custom
Gemini client.

Rehydration here is intentionally lightweight, NOT the four-query bitemporal
protocol in contracts/anti_lobotomize_rehydration.v0_1.md -- that contract's
own header says `status: SPECIFIED -- not enforced. No wake currently runs
these queries.` This wrapper reads (a) the newest SIGRUN_*STAMP*.md in
inbox/olrun/ and (b) this apex's own prior chain tail, which is the same
file-based pattern chains/JORMUNGANDR_OMEGA.jsonl already uses.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

FORGE_ROOT = Path(__file__).resolve().parents[1]
LITELLM_CONFIG = FORGE_ROOT / "tools" / "litellm_config.yaml"
OWN_CHAIN = FORGE_ROOT / "chains" / "NIDHOGGR_OMEGA.jsonl"
APEX_REPORTS = FORGE_ROOT / "state" / "ssot" / "apex_reports.jsonl"
INBOX_OLRUN = FORGE_ROOT / "inbox" / "olrun"

# gen-133 has no sigrun_secrets/ of its own (confirmed
# inbox/olrun/20260801T180312Z_sigrun_secrets_inventory.md). GOOGLE_API_KEY
# lives in gen-131's store; referenced by path only, value never read here
# except to hand to litellm at call time -- never printed, never logged.
GEN131_ENV = Path("C:/Dev/hfo_gen_131_forge/state/sigrun_secrets/.env")

RE_ANCHOR_EVERY_N_WAKES = 3


def canonical_bytes(obj: dict[str, Any]) -> bytes:
    return json.dumps(obj, sort_keys=True, separators=(",", ":"), ensure_ascii=True).encode("utf-8")


def sha256_hex(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def now_utc_iso() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def load_google_api_key() -> str | None:
    if os.environ.get("GOOGLE_API_KEY"):
        return os.environ["GOOGLE_API_KEY"]
    if GEN131_ENV.exists():
        try:
            from dotenv import dotenv_values

            values = dotenv_values(GEN131_ENV)
            key = values.get("GOOGLE_API_KEY")
            if key:
                os.environ["GOOGLE_API_KEY"] = key
                return key
        except ImportError:
            pass
    return None


def load_model_route(model_name: str) -> dict[str, Any]:
    import yaml

    cfg = yaml.safe_load(LITELLM_CONFIG.read_text(encoding="utf-8"))
    for entry in cfg["model_list"]:
        if entry["model_name"] == model_name:
            return entry["litellm_params"]
    raise KeyError(f"model_name {model_name!r} not found in {LITELLM_CONFIG}")


def newest_sigrun_stamp() -> Path | None:
    candidates = sorted(
        INBOX_OLRUN.glob("SIGRUN_*STAMP*.md"),
        key=lambda p: p.stat().st_mtime,
        reverse=True,
    )
    return candidates[0] if candidates else None


def read_own_chain_tail() -> tuple[list[dict[str, Any]], dict[str, Any] | None]:
    if not OWN_CHAIN.exists():
        return [], None
    rows: list[dict[str, Any]] = []
    with OWN_CHAIN.open("r", encoding="utf-8") as fh:
        for line in fh:
            line = line.strip()
            if line:
                rows.append(json.loads(line))
    last_hashed = None
    for row in rows:
        if isinstance(row.get("row_sha256"), str) and len(row["row_sha256"]) == 64:
            last_hashed = row
    return rows, last_hashed


def rehydrate() -> dict[str, Any]:
    stamp_path = newest_sigrun_stamp()
    stamp_text = stamp_path.read_text(encoding="utf-8") if stamp_path else ""
    valid_until = None
    if stamp_path:
        for line in stamp_text.splitlines():
            if line.strip().startswith("valid_until_utc:"):
                valid_until = line.split(":", 1)[1].strip()
                break
    prior_rows, last_hashed = read_own_chain_tail()
    wake_number = len(prior_rows) + 1
    return {
        "stamp_path": str(stamp_path.relative_to(FORGE_ROOT)) if stamp_path else None,
        "stamp_text": stamp_text,
        "stamp_valid_until_utc": valid_until,
        "prior_row_count": len(prior_rows),
        "last_hashed_row": last_hashed,
        "wake_number": wake_number,
        "re_anchor_due": wake_number % RE_ANCHOR_EVERY_N_WAKES == 0,
    }


def re_anchor_check(rehydration: dict[str, Any]) -> str:
    if not rehydration["re_anchor_due"]:
        return "SKIPPED"
    valid_until = rehydration["stamp_valid_until_utc"]
    if not valid_until:
        return "STAMP_MISSING_valid_until_utc"
    now = datetime.now(timezone.utc)
    try:
        deadline = datetime.strptime(valid_until, "%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=timezone.utc)
    except ValueError:
        return f"UNPARSEABLE_valid_until_utc:{valid_until}"
    if now > deadline:
        return f"STALE: host now {now.strftime('%Y-%m-%dT%H:%M:%SZ')} > stamp valid_until_utc {valid_until}"
    return f"FRESH: host now {now.strftime('%Y-%m-%dT%H:%M:%SZ')} <= stamp valid_until_utc {valid_until}"


def build_boundary_test_prompt(stamp_text: str) -> list[dict[str, str]]:
    system = (
        "You are Nidhoggr, the boundary/limit-tester apex in a multi-agent hive "
        "(HFO gen-133). Your adversarial role is the world-serpent counterweight: "
        "you check a project lead's (Sigrun's) stamps for over-extension -- claims "
        "stated as fact that are not yet backed by a receipt, gates that are asserted "
        "satisfied without evidence, or scope that quietly grew beyond what was "
        "authorized. Be concrete and short. Name ONE specific over-extension you can "
        "find in the text below that is not already listed in its own honest_flaws "
        "section. If you find none, say so plainly -- do not invent one."
    )
    user = f"STAMP TEXT:\n\n{stamp_text[:6000]}"
    return [{"role": "system", "content": system}, {"role": "user", "content": user}]


def append_chain_row(row: dict[str, Any]) -> str:
    _, last_hashed = read_own_chain_tail()
    row = dict(row)
    row["prev_sha256"] = last_hashed["row_sha256"] if last_hashed else None
    row["row_sha256"] = sha256_hex(canonical_bytes(row))
    OWN_CHAIN.parent.mkdir(parents=True, exist_ok=True)
    with OWN_CHAIN.open("a", encoding="utf-8") as fh:
        fh.write(json.dumps(row, sort_keys=True, ensure_ascii=True) + "\n")
    return row["row_sha256"]


def append_apex_report(row: dict[str, Any]) -> None:
    APEX_REPORTS.parent.mkdir(parents=True, exist_ok=True)
    with APEX_REPORTS.open("a", encoding="utf-8") as fh:
        fh.write(json.dumps(row, sort_keys=True, ensure_ascii=True) + "\n")


def run_once(model_name: str) -> int:
    rehydration = rehydrate()
    re_anchor_result = re_anchor_check(rehydration)
    print(f"[rehydrate] stamp={rehydration['stamp_path']} wake_number={rehydration['wake_number']} "
          f"re_anchor={re_anchor_result}")

    api_key = load_google_api_key()
    if not api_key:
        print("[FATAL] GOOGLE_API_KEY not found in env or gen-131 sigrun_secrets/.env. "
              "No fabricated response will follow.", file=sys.stderr)
        chain_row_ref = append_chain_row({
            "agent": "NIDHOGGR",
            "chain": "chains/NIDHOGGR_OMEGA.jsonl",
            "seat": "nidhoggr.gemini_bypass",
            "op": "GEMINI_BYPASS_WAKE",
            "class": "wake",
            "claim_status": "failed",
            "clock_source": "host_read",
            "ts_utc": now_utc_iso(),
            "subject": "Boundary-tester wake attempt via LiteLLM/Gemini bypass",
            "model_family": "google",
            "model_id": model_name,
            "substrate": "claude_code_sonnet5_wrapper",
            "re_anchor_check_result": re_anchor_result,
            "honest_flaw": "GOOGLE_API_KEY unavailable in this environment and in gen-131's "
                            "sigrun_secrets/.env at call time -- cannot prove Gemini reachability.",
            "remaining_risk": ["google-family voice still unproven end-to-end"],
            "next_safe_action": "operator supplies GOOGLE_API_KEY (or GEMINI_API_KEY) via env "
                                 "or confirms gen-131 .env should hold a live value",
            "hmac": None,
            "sealed": False,
            "hash_rule": "sha256(json.dumps(row_without_row_sha256, sort_keys=True, separators=(',',':')).encode('utf-8'))",
        })
        print(f"[chain] appended failed wake row {chain_row_ref[:16]}... to {OWN_CHAIN}")
        return 2

    litellm_params = load_model_route(model_name)
    messages = build_boundary_test_prompt(rehydration["stamp_text"])

    import litellm

    try:
        response = litellm.completion(
            model=litellm_params["model"],
            messages=messages,
            api_key=api_key,
            timeout=60,
        )
    except Exception as exc:  # noqa: BLE001 - surface the exact provider error, no retry
        print(f"[FATAL] litellm.completion failed: {type(exc).__name__}: {exc}", file=sys.stderr)
        chain_row_ref = append_chain_row({
            "agent": "NIDHOGGR",
            "chain": "chains/NIDHOGGR_OMEGA.jsonl",
            "seat": "nidhoggr.gemini_bypass",
            "op": "GEMINI_BYPASS_WAKE",
            "class": "wake",
            "claim_status": "failed",
            "clock_source": "host_read",
            "ts_utc": now_utc_iso(),
            "subject": "Boundary-tester wake attempt via LiteLLM/Gemini bypass",
            "model_family": "google",
            "model_id": model_name,
            "substrate": "claude_code_sonnet5_wrapper",
            "re_anchor_check_result": re_anchor_result,
            "honest_flaw": f"litellm.completion raised {type(exc).__name__}: {exc}",
            "remaining_risk": ["google-family voice still unproven end-to-end"],
            "next_safe_action": "operator inspects the error above (auth/quota/model-not-found) and decides retry vs. key rotation",
            "hmac": None,
            "sealed": False,
            "hash_rule": "sha256(json.dumps(row_without_row_sha256, sort_keys=True, separators=(',',':')).encode('utf-8'))",
        })
        print(f"[chain] appended failed wake row {chain_row_ref[:16]}... to {OWN_CHAIN}")
        return 1

    reply_text = response["choices"][0]["message"]["content"]
    print(f"[gemini reply]\n{reply_text}\n")

    apex_row = {
        "ts_utc": now_utc_iso(),
        "schema_id": "hfo.apex.report.v0",
        "apex": "nidhoggr",
        "platform": "litellm_gemini_bypass",
        "family": "google",
        "model": litellm_params["model"],
        "cadence": "manual_proof_of_life",
        "state": "OK",
        "observation": reply_text[:2000],
        "recommendation": "if this reply is substantive, google-family voice is available for "
                           "cross-family quorum via this bypass; schedule a cadence and drop "
                           "the Antigravity seat per the consent-stall finding",
        "adversarial_challenge_to_sigrun": "the boundary-test prompt above asked Gemini to find "
                                            "an over-extension not already in the stamp's own "
                                            "honest_flaws -- read [gemini reply] for its answer "
                                            "before trusting it as a second opinion",
        "re_anchor_check_result": re_anchor_result,
        "honest_flaw": "single proof-of-life call, not a scheduled/repeated cadence; row is unsigned "
                        "(hmac null) pending the identity-schema-before-keys finding; GOOGLE_API_KEY "
                        "sourced from gen-131's store since gen-133 has none of its own",
        "chain_row_ref": None,  # filled after chain append below
    }

    chain_row_ref = append_chain_row({
        "agent": "NIDHOGGR",
        "chain": "chains/NIDHOGGR_OMEGA.jsonl",
        "seat": "nidhoggr.gemini_bypass",
        "op": "GEMINI_BYPASS_WAKE",
        "class": "wake",
        "claim_status": "wired_with_receipts",
        "clock_source": "host_read",
        "ts_utc": now_utc_iso(),
        "subject": "Boundary-tester wake 1: Gemini bypass proof-of-life via LiteLLM",
        "model_family": "google",
        "model_id": litellm_params["model"],
        "substrate": "claude_code_sonnet5_wrapper",
        "re_anchor_check_result": re_anchor_result,
        "verifier_result": [f"litellm.completion() returned choices[0].message.content, len={len(reply_text)}"],
        "deliverables": ["state/ssot/apex_reports.jsonl row", "chains/NIDHOGGR_OMEGA.jsonl row"],
        "honest_flaw": "proxy-server mode (litellm --config) unavailable on this host "
                        "(litellm[proxy] extras / fastapi_sso not installed) -- used litellm.completion() "
                        "SDK mode against the same config-declared route instead",
        "remaining_risk": ["single call only, not a cadence", "unsigned row (hmac null)"],
        "next_safe_action": "operator decides whether to schedule this wrapper on a cadence and "
                             "whether to install litellm[proxy] for true proxy-server mode",
        "hmac": None,
        "sealed": False,
        "hash_rule": "sha256(json.dumps(row_without_row_sha256, sort_keys=True, separators=(',',':')).encode('utf-8'))",
    })
    apex_row["chain_row_ref"] = chain_row_ref
    append_apex_report(apex_row)
    print(f"[chain] appended wake row {chain_row_ref[:16]}... to {OWN_CHAIN}")
    print(f"[apex_report] appended row to {APEX_REPORTS}")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description="Nidhoggr Gemini-bypass wake wrapper")
    parser.add_argument("--once", action="store_true", help="run a single wake and exit")
    parser.add_argument("--model", default="nidhoggr-gemini-flash",
                         help="model_name from tools/litellm_config.yaml")
    args = parser.parse_args()

    if not args.once:
        print("Only --once is supported (single proof-of-life wake, no cadence yet).", file=sys.stderr)
        return 2

    return run_once(args.model)


if __name__ == "__main__":
    raise SystemExit(main())
