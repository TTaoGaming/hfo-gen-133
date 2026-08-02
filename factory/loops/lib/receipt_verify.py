"""Pre-send verification helpers used by every loop that touches the outside world.

Three checks, one API
---------------------
url_head_ok(url)              -> (bool, status_int_or_None)
required_slots_filled(text, slots) -> (bool, missing[])
not_suppressed(target, suppression_list_path) -> (bool, reason_or_None)

Composite
---------
verify_before_send(payload)   -> VerifyResult
    payload = {
        "targets": [{"kind":"url","value":"..."}, {"kind":"email","value":"..."}],
        "text": "the body",
        "required_slots": ["{intro_reference}", "{unit_link}"],
        "suppression_lists": {"email": "state/outreach/suppression_emails.txt"},
    }

Every helper is stdlib + urllib. HEAD requests have 10s timeout + 1 retry.
"""

from __future__ import annotations

import dataclasses
import re
import time
import urllib.error
import urllib.request
from pathlib import Path
from typing import Iterable

USER_AGENT = "hfo-gen133-factory-loop/0.1 (+ops@olrun.local)"
HEAD_TIMEOUT = 10.0
HEAD_RETRY = 1


@dataclasses.dataclass
class VerifyResult:
    ok: bool
    checks: list[dict]

    def failed(self) -> list[dict]:
        return [c for c in self.checks if not c["ok"]]


def url_head_ok(url: str) -> tuple[bool, int | None]:
    """HEAD (fall back to GET on 405) with 10s timeout + 1 retry."""
    for method in ("HEAD", "GET"):
        for attempt in range(HEAD_RETRY + 1):
            try:
                req = urllib.request.Request(url, method=method, headers={"User-Agent": USER_AGENT})
                with urllib.request.urlopen(req, timeout=HEAD_TIMEOUT) as resp:
                    status = getattr(resp, "status", None) or resp.getcode()
                    if status and 200 <= status < 400:
                        return True, status
                    if status and status == 405 and method == "HEAD":
                        break  # try GET
                    return False, status
            except urllib.error.HTTPError as e:
                if e.code == 405 and method == "HEAD":
                    break
                if attempt < HEAD_RETRY:
                    time.sleep(0.5 * (attempt + 1))
                    continue
                return False, e.code
            except (urllib.error.URLError, TimeoutError, OSError):
                if attempt < HEAD_RETRY:
                    time.sleep(0.5 * (attempt + 1))
                    continue
                return False, None
    return False, None


_SLOT_RE = re.compile(r"\{[a-z0-9_]+\}")


def required_slots_filled(text: str, required_slots: Iterable[str]) -> tuple[bool, list[str]]:
    """Return (ok, missing). Missing = required slot literal not present OR
    any leftover {template_slot} pattern found."""
    missing: list[str] = []
    for slot in required_slots:
        # A "filled" slot means the literal placeholder is GONE and something
        # non-trivial replaced it. Cheapest check: placeholder text should not
        # still be literally in the body.
        if slot in text:
            missing.append(slot)
    leftover = _SLOT_RE.findall(text)
    for l in leftover:
        if l not in missing:
            missing.append(l)
    return (not missing), missing


def not_suppressed(target: str, suppression_list_path: str | Path | None) -> tuple[bool, str | None]:
    if not suppression_list_path:
        return True, None
    p = Path(suppression_list_path)
    if not p.exists():
        return True, None
    t = target.strip().lower()
    for raw in p.read_text(encoding="utf-8").splitlines():
        line = raw.strip().lower()
        if not line or line.startswith("#"):
            continue
        if line == t:
            return False, f"target on suppression list: {suppression_list_path}"
    return True, None


def verify_before_send(payload: dict) -> VerifyResult:
    checks: list[dict] = []

    text = payload.get("text", "")
    required_slots = payload.get("required_slots", []) or []
    if required_slots or "{" in text:
        ok, missing = required_slots_filled(text, required_slots)
        checks.append(
            {
                "kind": "required_slots",
                "ok": ok,
                "detail": "" if ok else f"unfilled: {missing}",
            }
        )

    supp = payload.get("suppression_lists", {}) or {}
    for tgt in payload.get("targets", []) or []:
        kind = tgt.get("kind")
        value = tgt.get("value")
        if not value:
            checks.append({"kind": f"target_{kind}", "ok": False, "detail": "empty target"})
            continue
        if kind == "url":
            ok, status = url_head_ok(value)
            checks.append(
                {
                    "kind": "url_head",
                    "ok": ok,
                    "target": value,
                    "detail": f"status={status}",
                }
            )
        else:
            supp_path = supp.get(kind)
            ok, reason = not_suppressed(value, supp_path)
            checks.append(
                {
                    "kind": f"suppression_{kind}",
                    "ok": ok,
                    "target": value,
                    "detail": reason or "",
                }
            )

    all_ok = all(c["ok"] for c in checks) if checks else True
    return VerifyResult(ok=all_ok, checks=checks)


if __name__ == "__main__":  # pragma: no cover
    import json

    demo = {
        "text": "hi {name}, saw your post about {topic} — love your {intro_reference}.",
        "required_slots": ["{name}", "{topic}", "{intro_reference}"],
    }
    res = required_slots_filled(demo["text"], demo["required_slots"])
    print(json.dumps({"filled": res[0], "missing": res[1]}))
    assert res[0] is False and len(res[1]) >= 3
    demo2 = {"text": "hi Tao, saw your post about foss — love your recent talk."}
    res2 = required_slots_filled(demo2["text"], [])
    print(json.dumps({"filled": res2[0], "missing": res2[1]}))
    assert res2[0] is True
    print("OK")
