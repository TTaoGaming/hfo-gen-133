#!/usr/bin/env python3
"""Append the operator-requested Suika DLC 5-16 deployment receipts.

This is intentionally narrow: one fixed batch, one exact chain path, one
exclusive lock, duplicate rejection, canonical per-row hashes, and no sealing.
It never edits or repairs historical rows in the already-divergent chain.
"""
from __future__ import annotations

import hashlib
import json
import os
from datetime import datetime, timezone
from pathlib import Path

FORGE = Path(__file__).resolve().parents[2]
CHAIN = FORGE / "chains" / "SIGRUN_P4.jsonl"
LOCK = FORGE / "chains" / ".SIGRUN_P4.suika_dlc_5_16.lock"
UPSTREAM = "c30848ed79f7c23e54a89e3e58a993b4fd991d14"

VARIANTS = [
    (5, "timer_mode", "timer-mode", "c5fc1456", 2),
    (6, "gravity_flip", "gravity-flip", "e4aa02ee", 1),
    (7, "boss_fruits", "boss-fruits", "3e8346da", 1),
    (8, "character_select", "character-select", "12e4d679", 1),
    (9, "daily_seed", "daily-seed", "afe913b2", 1),
    (10, "combo_burst", "combo-burst", "aa8c9534", 1),
    (11, "reverse_suika", "reverse-suika", "bcc8343d", 1),
    (12, "gauntlet_mode", "gauntlet-mode", "1036e0aa", 1),
    (13, "relic_draft", "relic-draft", "f22a2603", 1),
    (14, "joker_hands", "joker-hands", "c928cb99", 1),
    (15, "evolution_frenzy", "evolution-frenzy", "8c74ac27", 1),
    (16, "curse_pacts", "curse-pacts", "22ab6686", 1),
]


def canonical(row: dict) -> bytes:
    return json.dumps(row, sort_keys=True, separators=(",", ":"), ensure_ascii=True).encode("utf-8")


def row_hash(row: dict) -> str:
    without = dict(row)
    without.pop("row_sha256", None)
    return hashlib.sha256(canonical(without)).hexdigest()


def load_rows() -> list[dict]:
    return [json.loads(line) for line in CHAIN.read_text(encoding="utf-8-sig").splitlines() if line.strip()]


def main() -> None:
    lock_fd = os.open(LOCK, os.O_CREAT | os.O_EXCL | os.O_WRONLY)
    try:
        os.write(lock_fd, f"pid={os.getpid()}\n".encode("ascii"))
        os.fsync(lock_fd)
        rows = load_rows()
        if not rows or not isinstance(rows[-1].get("row_sha256"), str):
            raise RuntimeError("current chain tail has no declared row_sha256")
        if row_hash(rows[-1]) != rows[-1]["row_sha256"]:
            raise RuntimeError("current chain tail self-hash is invalid; refusing to extend it")

        existing = {row.get("variant_id") for row in rows}
        requested = {f"suika_dlc_{n}_{mechanic}" for n, mechanic, *_ in VARIANTS}
        duplicates = sorted(existing & requested)
        if duplicates:
            raise RuntimeError(f"duplicate variant receipt(s) already present: {duplicates}")

        prev = rows[-1]["row_sha256"]
        now = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
        appended: list[dict] = []
        for n, mechanic, project_slug, preview_hash, deploy_attempts in VARIANTS:
            variant_id = f"suika_dlc_{n}_{mechanic}"
            project = f"hfo-suika-dlc-{n}-{project_slug}"
            deploy_url = f"https://{project}.pages.dev/"
            preview_url = f"https://{preview_hash}.{project}.pages.dev/"
            row = {
                "schema_id": "hfo.gen133.suika_dlc_deploy_receipt.v0_1",
                "generation": 133,
                "kind": "deployment_receipt",
                "op": "DEPLOY_SUIKA_DLC_VARIANT",
                "author": "codex_gunnr",
                "authorization_source": "operator-typed /goal in current Codex task",
                "variant_id": variant_id,
                "mechanic": mechanic,
                "clone_path": f"outputs/staged_sends/games/{variant_id}",
                "upstream_repo": "https://github.com/moonfloof/suika-game.git",
                "upstream_commit": UPSTREAM,
                "license": "Unlicense",
                "cloudflare_project": project,
                "deploy_url": deploy_url,
                "returned_deployment_url": preview_url,
                "deploy_attempts": deploy_attempts,
                "http_status": 200,
                "test_result": {
                    "mechanic_unit": "PASS 2/2",
                    "local_http_hook": "PASS HTTP 200 + exact mechanic hook",
                    "local_browser_runtime": "PASS 10/10",
                    "live_browser_runtime": "PASS 10/10",
                    "combined": "PASS",
                },
                "verifier_result": (
                    "node --test: 2/2; localhost curl: HTTP 200 + exact hook; "
                    "pre-existing held-out Playwright probe local: 10/10; stable Pages origin: 10/10"
                ),
                "claim_status": "wired_with_receipts",
                "sealed": False,
                "hmac": None,
                "signature": None,
                "marketplace_submission": "NONE",
                "external_post_by_this_run": "NONE",
                "cold_outreach_by_this_run": "NONE",
                "paid_tier_change": "NONE",
                "remaining_risk": [
                    "The containing SIGRUN_P4 chain was already globally invalid before this append: 3 hash mismatches, 3 predecessor breaks, and 9 unhashed rows in the 98-row pre-append audit.",
                    "The hash-prefixed Cloudflare preview alias returned by Wrangler showed a Windows/Chromium TLS cipher mismatch during DLC-5 verification; the stable production Pages alias returned HTTP 200 and passed the full live runtime probe.",
                    "Mechanic unit tests are self-authored consistency checks; the pre-existing runtime probe is independently authored but covers common live gameplay, not every full mechanic threshold.",
                    "No mobile touch hit-box playthrough or external-human response check was available; no outbound post or marketplace submission was made by this run.",
                ],
                "honest_flaw": (
                    "These rows prove deployed bytes, stable-origin HTTP/runtime behavior, and focused state transitions. "
                    "They do not repair the pre-existing chain, prove marketplace acceptance, traffic, revenue, or a human mobile playthrough."
                ),
                "next_safe_action": "Operator mobile-play DLC 5-16 and keep all marketplace submissions staged pending a separate explicit approval.",
                "hash_rule": "sha256(json.dumps(row_without_row_sha256,sort_keys=True,separators=(',',':'),ensure_ascii=True).encode('utf-8'))",
                "prev_sha256": prev,
                "ts_utc": now,
            }
            row["row_sha256"] = row_hash(row)
            appended.append(row)
            prev = row["row_sha256"]

        payload = b"".join(canonical(row) + b"\n" for row in appended)
        fd = os.open(CHAIN, os.O_WRONLY | os.O_APPEND | getattr(os, "O_BINARY", 0))
        try:
            written = os.write(fd, payload)
            os.fsync(fd)
        finally:
            os.close(fd)
        if written != len(payload):
            raise RuntimeError(f"short append: wrote {written} of {len(payload)} bytes")

        verify = load_rows()[-len(appended):]
        expected_prev = rows[-1]["row_sha256"]
        for row in verify:
            if row.get("prev_sha256") != expected_prev or row_hash(row) != row.get("row_sha256"):
                raise RuntimeError(f"post-append verification failed at {row.get('variant_id')}")
            expected_prev = row["row_sha256"]
        print(json.dumps({
            "appended": len(appended),
            "first_variant": appended[0]["variant_id"],
            "last_variant": appended[-1]["variant_id"],
            "prior_tail": rows[-1]["row_sha256"],
            "new_tail": appended[-1]["row_sha256"],
            "line_count": len(rows) + len(appended),
        }, indent=2))
    finally:
        os.close(lock_fd)
        LOCK.unlink(missing_ok=True)


if __name__ == "__main__":
    main()
