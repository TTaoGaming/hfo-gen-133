"""Deterministic fit scoring. No model call, no randomness, fully explainable.

fit_score is a 0..1 number built from four transparent components so that a
human reading apex_grade.json can see exactly why a listing ranked where it did.
"""
from __future__ import annotations

import datetime as _dt
import re

from .core import Opportunity
from .profile import CAPABILITIES, DISQUALIFIERS

_MONEY = re.compile(r"(?i)(\$\s?\d[\d,]*(?:\s?[-–]\s?\$?\d[\d,]*)?(?:\s?k)?|\d+\s?k\s?[-–]\s?\d+\s?k)")
_RECENCY_BONUS = 0.15


_DATE_FORMATS = ("%Y-%m-%dT%H:%M:%SZ", "%Y-%m-%dT%H:%M:%S", "%Y-%m-%d %H:%M:%S",
                 "%Y-%m-%d", "%a, %d %b %Y %H:%M:%S %z", "%a, %d %b %Y %H:%M:%S %Z")


def _freshness(posted: str) -> tuple[float, int | None]:
    """-> (0..1 score, age_days or None when the listing states no date)."""
    if not posted:
        return 0.5, None                    # unknown: neither rewarded nor punished
    txt = posted.strip()
    for fmt in _DATE_FORMATS:
        try:
            dt = _dt.datetime.strptime(txt, fmt)
            break
        except ValueError:
            continue
    else:
        try:
            dt = _dt.datetime.fromisoformat(txt.replace("Z", "+00:00"))
        except ValueError:
            return 0.5, None
    if dt.tzinfo is None:
        dt = dt.replace(tzinfo=_dt.timezone.utc)
    age = (_dt.datetime.now(_dt.timezone.utc) - dt).days
    if age < 0:
        return 0.5, age
    if age <= 7:
        return 1.0, age
    if age <= 21:
        return 0.8, age
    if age <= 45:
        return 0.5, age
    if age <= 90:
        return 0.2, age
    return 0.0, age


#: Word-boundary matcher, built once per term.
#
#: BUG FOUND 2026-08-02 by adversarial review: naive `term in text` matched
#: "rag" inside "cove(rag)e" and "unity" inside "opport(unity)"/"comm(unity)".
#: A car-detailing lot-attendant listing scored fit 0.471 on those two false
#: positives alone and the grader passed it as "send as-is". Substring matching
#: on short capability tokens is not a near-miss, it is noise wearing evidence's
#: clothes -- it silently converts unrelated listings into qualified targets.
_TERM_RE: dict[str, "re.Pattern[str]"] = {}


def _matcher(term: str) -> "re.Pattern[str]":
    p = _TERM_RE.get(term)
    if p is None:
        p = re.compile(r"(?<![a-z0-9])" + re.escape(term) + r"(?![a-z0-9])")
        _TERM_RE[term] = p
    return p


def _weighted_hits(text: str, table: dict[str, float]) -> tuple[float, list[str]]:
    low = text.lower()
    total, hits = 0.0, []
    for term, w in table.items():
        if _matcher(term).search(low):
            total += w
            hits.append(term)
    return total, hits


def _cap_score(text: str) -> tuple[float, list[str]]:
    return _weighted_hits(text, CAPABILITIES)


def _disq_score(text: str) -> tuple[float, list[str]]:
    return _weighted_hits(text, DISQUALIFIERS)


def score(op: Opportunity) -> None:
    """Mutates op: sets fit_score, fit_components, fit_signals."""
    haystack = f"{op.title}\n{' '.join(op.tags)}\n{op.body}"

    cap_raw, cap_hits = _cap_score(haystack)
    disq_raw, disq_hits = _disq_score(haystack)

    # 1. capability match, saturating -- 12 raw points is a strong match
    capability = min(cap_raw / 12.0, 1.0)

    # 2. title match counts double; a term in the title is what the buyer named
    title_raw, title_hits = _cap_score(op.title)
    title = min(title_raw / 5.0, 1.0)

    # 3. reachability -- a listing that names money or a contract shape is
    #    closer to a price-or-date reply than one that does not
    reach = 0.0
    if op.compensation or _MONEY.search(op.body):
        reach += 0.5
    if re.search(r"(?i)\b(contract|freelance|consultant|part[- ]time|project[- ]based|"
                 r"fixed[- ]price|sow|statement of work)\b", haystack):
        reach += 0.3
    if op.contact:
        reach += 0.2
    reach = min(reach, 1.0)

    # 4. specificity -- can we actually target this, or is it boilerplate?
    spec = min(len(op.requirements) / 8.0, 1.0)

    # 5. freshness -- a 3-month-old post is very likely filled. Outreach into a
    #    closed role produces silence, which is indistinguishable from rejection
    #    and therefore poisons the PDCA read.
    fresh, age_days = _freshness(op.posted_utc)

    penalty = max(disq_raw / 6.0, -1.0)   # negative

    raw = (0.34 * capability + 0.22 * title + 0.18 * reach
           + 0.13 * spec + 0.13 * fresh) + penalty
    op.fit_score = round(max(0.0, min(1.0, raw)), 4)
    op.fit_components = {
        "capability": round(capability, 3),
        "title_match": round(title, 3),
        "reachability": round(reach, 3),
        "specificity": round(spec, 3),
        "freshness": round(fresh, 3),
        "age_days": age_days,
        "disqualifier_penalty": round(penalty, 3),
    }
    op.fit_signals = sorted(set(title_hits)) + [f"-{d}" for d in disq_hits]
    if not op.fit_signals:
        op.fit_signals = sorted(set(cap_hits))[:6]
