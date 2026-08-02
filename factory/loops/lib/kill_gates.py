"""Reusable halt-condition evaluator for factory loops.

A loop calls `check(metrics, thresholds)` before each material action.
If any threshold trips, the loop MUST halt, chain-row the reason, and
optionally slack_escalate.

Standard axes
-------------
bounce_pct       : email bounces / attempted sends
spam_pct         : spam complaints / delivered
reply_pct        : replies / delivered            (used as LOW-side gate: kill on <threshold)
error_rate       : HTTP 4xx+5xx / attempted network calls
license_reject   : boolean — LOOP-B kill on GPL/AGPL when whitelist not present
build_failed     : boolean — LOOP-A/B kill on non-zero build exit
url_verify_0     : boolean — LOOP-A kill on 0/5 canonical URLs 200

Thresholds are all in [0, 1] except *_max which are absolute counts. A
threshold of None disables that axis.

Design notes
------------
- Kill on any tripped axis (OR, not AND).
- Return a KillDecision so the caller can chain-row the raw judgment.
- No I/O — pure function so unit tests are trivial.
"""

from __future__ import annotations

import dataclasses
from typing import Any


@dataclasses.dataclass(frozen=True)
class KillDecision:
    kill: bool
    tripped: list[str]                       # axis names that fired
    reasons: dict[str, str]                  # axis -> human readable reason
    metrics: dict[str, Any]                  # snapshot passed in
    thresholds: dict[str, Any]

    def to_row_extra(self) -> dict:
        return {
            "kill": self.kill,
            "tripped": self.tripped,
            "reasons": self.reasons,
            "metrics_snapshot": self.metrics,
            "thresholds_snapshot": self.thresholds,
        }


DEFAULT_THRESHOLDS = {
    "bounce_pct_max": 0.05,        # 5% bounce → halt
    "spam_pct_max": 0.001,         # 0.1% spam → halt (postmaster tolerance)
    "reply_pct_min": None,         # unset by default; set for cold-email loops
    "error_rate_max": 0.20,        # 20% network errors → halt
    "url_verify_min": 1,           # LOOP-A: at least 1/5 URLs must 200
}


def check(metrics: dict[str, Any], thresholds: dict[str, Any] | None = None) -> KillDecision:
    t = {**DEFAULT_THRESHOLDS, **(thresholds or {})}
    tripped: list[str] = []
    reasons: dict[str, str] = {}

    def _trip(axis: str, reason: str) -> None:
        tripped.append(axis)
        reasons[axis] = reason

    if t.get("bounce_pct_max") is not None:
        val = metrics.get("bounce_pct")
        if val is not None and val > t["bounce_pct_max"]:
            _trip("bounce_pct", f"{val:.3f} > {t['bounce_pct_max']}")
    if t.get("spam_pct_max") is not None:
        val = metrics.get("spam_pct")
        if val is not None and val > t["spam_pct_max"]:
            _trip("spam_pct", f"{val:.4f} > {t['spam_pct_max']}")
    if t.get("reply_pct_min") is not None:
        val = metrics.get("reply_pct")
        if val is not None and val < t["reply_pct_min"]:
            _trip("reply_pct", f"{val:.3f} < {t['reply_pct_min']}")
    if t.get("error_rate_max") is not None:
        val = metrics.get("error_rate")
        if val is not None and val > t["error_rate_max"]:
            _trip("error_rate", f"{val:.3f} > {t['error_rate_max']}")
    if metrics.get("license_reject"):
        _trip("license_reject", str(metrics.get("license_reject_reason", "incompatible license")))
    if metrics.get("build_failed"):
        _trip("build_failed", str(metrics.get("build_failed_reason", "non-zero exit")))
    if t.get("url_verify_min") is not None:
        val = metrics.get("url_verify_ok")
        if val is not None and val < t["url_verify_min"]:
            _trip("url_verify", f"only {val}/{metrics.get('url_verify_total', '?')} URLs verified")

    return KillDecision(
        kill=bool(tripped),
        tripped=tripped,
        reasons=reasons,
        metrics=dict(metrics),
        thresholds=t,
    )


if __name__ == "__main__":  # pragma: no cover
    d = check({"bounce_pct": 0.08, "spam_pct": 0.0005})
    print(d)
    assert d.kill and "bounce_pct" in d.tripped
    d2 = check({"url_verify_ok": 0, "url_verify_total": 5})
    print(d2)
    assert d2.kill and "url_verify" in d2.tripped
    d3 = check({"bounce_pct": 0.01})
    print(d3)
    assert not d3.kill
    print("OK")
