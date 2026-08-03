"""
Apex grading — deterministic, structural, no model call.

The design rule: grade properties that are MECHANICALLY CHECKABLE, because
"claims move through your system as prose, and prose cannot fail"
(WHY_BLOCKED_AND_WHOM_TO_ADOPT). A rubric a model scores by vibe would be one
more prose layer. Every check below is a regex or a set operation.

`reward_hack_risk` answers exactly one question:
    could this artifact be marked a success WITHOUT a real buyer moving?
An artifact with no named target, or no price-or-date ask, can only ever produce
soft signals (a like, a "cool!", a reply saying "interesting"). Those are the
metrics the operator's own falsifier scores as ZERO. So: high risk.
"""
from __future__ import annotations

import re
from typing import Iterable

from .core import Artifact, Grade, Opportunity
from .profile import ACCEPTANCE_EVENT, verified_assets

# --- soft-metric detector (canon §6 E8) ------------------------------------
SOFT_ASK = re.compile(
    r"(?i)\b(let me know what you think|thoughts\?|any feedback|would love to connect|"
    r"happy to chat sometime|reach out if|if you(?:'re| are) interested|keep me in mind|"
    r"looking forward to hearing|feel free to|excited to learn more|"
    r"open to opportunities|please consider my)\b")

# --- falsifiable ask detector ---------------------------------------------
PRICE_TOK = re.compile(r"(?i)(\$\s?\d|\bUSD\b|\bday rate\b|\bhourly\b|\bfixed\b|\bbudget\b|\brange\b|\bapprove\b)")
DATE_TOK = re.compile(
    r"(?i)\b(monday|tuesday|wednesday|thursday|friday|next week|this week|the week of|"
    r"\d{1,2}(?:st|nd|rd|th)?\s+(?:jan|feb|mar|apr|may|jun|jul|aug|sep|oct|nov|dec)|"
    r"\d{4}-\d{2}-\d{2}|\d{1,2}/\d{1,2}/\d{4}|"
    r"15 minutes|20 minutes|30 minutes|start date|kick ?off|"
    # M5/M6 asks resolve on a different vocabulary of dates than a sales call:
    r"deadline|close date|closing date|review date|turnaround|"
    r"review time|slot|submission window|by when|how long)\b")

PLACEHOLDER = re.compile(r"(?i)(your company|the company|hiring manager|to whom it may|"
                         r"\[.*?\]|\{\{.*?\}\}|EXAMPLE_DO_NOT_SEND|company named in listing)")

STOP = set("the a an and or but for with from that this your our you we they it is are was "
           "will can has have had to of in on at as by be been not if then than into out up "
           "about their there here more most all any some other such who what when which".split())

WEIGHTS = {
    "named_target": 0.12,
    "live_listing_url": 0.06,
    "verified_evidence_url": 0.06,
    "has_ask": 0.09,
    "ask_is_falsifiable": 0.13,
    "mirrors_their_language": 0.09,
    "claim_url_coherent": 0.09,
    "no_soft_metric": 0.04,
    "length_sane": 0.03,
    # the two world-dependent checks carry the most weight, deliberately
    "capability_evidence": 0.18,
    "deliverable_to_human": 0.11,
}
CORE = ("named_target", "has_ask", "ask_is_falsifiable", "claim_url_coherent",
        "capability_evidence")

# Assets, keyed by id -> the terms whose presence in the body means the body is
# actually TALKING ABOUT that asset. Used by the coherence check below.
from .profile import ASSETS as _ASSETS                                # noqa: E402

_ASSET_TERMS = {
    a["id"]: set(re.findall(r"[a-z]{4,}", (a.get("proof_sentence", "") + " " +
                                           a.get("pitch", "")).lower()))
    for a in _ASSETS
}
_ASSET_URL = {a["id"]: a.get("url", "") for a in _ASSETS}


def _shingles(text: str, n: int = 4) -> set[tuple[str, ...]]:
    words = [w for w in re.findall(r"[a-z]{3,}", text.lower()) if w not in STOP]
    return {tuple(words[i:i + n]) for i in range(max(0, len(words) - n + 1))}


def check(op: Opportunity, art: Artifact) -> dict[str, bool]:
    blob = f"{art.subject}\n{art.body}"
    verified_urls = {a["url"] for a in verified_assets() if a.get("url")}
    ask = art.price_or_date_ask or ""

    return {
        "named_target": bool(art.named_target.strip())
                        and not PLACEHOLDER.search(art.named_target),
        "live_listing_url": op.url in art.evidence_urls,
        "verified_evidence_url": bool(verified_urls & set(art.evidence_urls)),
        "has_ask": bool(ask.strip()),
        "ask_is_falsifiable": bool(PRICE_TOK.search(ask) or DATE_TOK.search(ask))
                              and bool(PRICE_TOK.search(blob) or DATE_TOK.search(blob)),
        "mirrors_their_language": len(_shingles(blob) & _shingles(op.body)) >= 1,
        "claim_url_coherent": _claim_url_coherent(art),
        "no_soft_metric": not SOFT_ASK.search(blob),
        # a repackaging plan and a bid/no-bid memo are longer than a cover
        # letter by design; judging them on one band would punish the format
        "length_sane": _length_ok(art),
        # --- the two checks the factory does NOT control ---------------------
        "capability_evidence": _capability_evidence(op),
        "deliverable_to_human": _deliverable_to_human(op),
    }


_LENGTH_BAND = {
    "PORTAL_PITCH": (150, 520),
    "GRANT_FIT": (150, 520),
    "JAM_ENTRY": (90, 400),
}


def _length_ok(art: Artifact) -> bool:
    lo, hi = _LENGTH_BAND.get(art.strategy, (90, 340))
    return lo <= art.word_count <= hi


def _capability_evidence(op: Opportunity) -> bool:
    """Does the LISTING actually ask for something the operator can do?

    Adversarial review 2026-08-02: every other check is satisfied by the
    generator's own template, because generator and grader read the same
    `profile.py`. This one reads the buyer's text instead. A capability hit
    buried once in a 900-word body is not demand; the requirement lines and the
    title are where a buyer states what they are paying for.
    """
    from .fit import _matcher
    from .profile import GAME_CATALOGUE, STRONG_CAPABILITIES

    # M5: the evidence is a finished catalogue, and the demand is structural --
    # accepting third-party browser games is a portal's entire business and a
    # jam's entire premise. No keyword inference needed.
    if op.market == "M5":
        return bool(GAME_CATALOGUE["portal_candidates"])
    # M6: a grant "matches" only via a keyword hit on solicitation text, which is
    # far weaker than a buyer naming a requirement. Never established demand.
    if op.market == "M6":
        return False

    signal = (op.title + "\n" + "\n".join(op.requirements)).lower()
    hits = [t for t in STRONG_CAPABILITIES if _matcher(t).search(signal)]
    # at least one UNAMBIGUOUS term, stated where the buyer states what they pay
    # for. Weak terms (python, agent, accessibility) never establish this alone.
    return bool(hits) and sum(STRONG_CAPABILITIES[t] for t in hits) >= 2.0


def _deliverable_to_human(op: Opportunity) -> bool:
    """Is there a route by which a reply can actually come back?

    M1/M2: a named human. M5: a portal's published intake IS the delivery path --
    submissions are routed through it by design, and addressing a named employee
    instead would be worse. M6: there is no recipient at all; a solicitation
    cannot reply, which is why grant artifacts are internal memos, not outreach.
    """
    if op.market == "M6":
        return False
    if op.market == "M5":
        return op.url.startswith("http")
    if op.contact:
        return True
    return bool((op.source_payload or {}).get("person"))


def _claim_url_coherent(art: Artifact) -> bool:
    """Does the body's claim actually describe the URL it cites?

    The first live run shipped "I build webcam input layers ... github.com/..."
    -- structurally perfect, factually incoherent. Structure alone cannot see
    that, so check it directly: the cited URL must belong to the same asset
    whose vocabulary the body is using.
    """
    if not art.asset_id or art.asset_id not in _ASSET_TERMS:
        return False
    body_words = set(re.findall(r"[a-z]{4,}", art.body.lower()))
    own = _ASSET_TERMS[art.asset_id]
    if own and len(own & body_words) / len(own) < 0.45:
        return False                       # body is not describing its own asset
    url = _ASSET_URL.get(art.asset_id, "")
    if url and url not in art.body:
        return False                       # claims the asset but never links it
    # It must not be borrowing another asset's signature vocabulary WITHOUT
    # citing that asset. Citing two assets is legitimate -- the portal pitch
    # describes the game catalogue and links the live demo as the only public
    # build -- so the rule is "every asset you talk about, you also link".
    for other_id, terms in _ASSET_TERMS.items():
        if other_id == art.asset_id or not terms:
            continue
        other_only = terms - own
        if not other_only:
            continue
        if len(other_only & body_words) / len(other_only) > 0.55:
            other_url = _ASSET_URL.get(other_id, "")
            if not other_url or other_url not in art.body:
                return False       # talks about it, never links it -> incoherent
    return True


def reward_hack_risk(checks: dict[str, bool], op: Opportunity,
                     art_suitability: float = 1.0) -> tuple[str, list[str]]:
    reasons: list[str] = []
    failed_core = [c for c in CORE if not checks[c]]
    if failed_core:
        reasons += [f"core check failed: {c}" for c in failed_core]
        if "claim_url_coherent" in failed_core:
            reasons.append("the body's claim does not describe the URL it cites -- a reader "
                           "who clicks will see something other than what was promised")
        if op.market == "M6":
            reasons.append("grants have no recipient who can reply -- canon puts this market "
                           "LAST on speed (P=0.25, 6-12 months to cash). Treat as a bid/no-bid "
                           "decision against a close date, not as outreach")
        else:
            reasons.append("this artifact can only generate soft signals (a like, a "
                           "'sounds interesting') which the operator's falsifier scores as ZERO")
        return "high", reasons

    if not checks["mirrors_their_language"]:
        reasons.append("shares no 4-word span with the listing -- reads as a template, "
                       "so a reply would not indicate real fit")
    if not checks["no_soft_metric"]:
        reasons.append("contains a soft-metric ask that invites a non-committal reply")
    if not checks["live_listing_url"]:
        reasons.append("no live listing URL attached -- the target cannot be re-verified later")
    if op.fit_score < 0.35:
        reasons.append(f"fit_score {op.fit_score:.2f} is low; a reply here would more "
                       f"likely reflect politeness than demand")
    if not op.contact and op.adapter == "hn_contracts":
        reasons.append("no published contact in the source post -- delivery path unproven")
    if not checks["deliverable_to_human"]:
        reasons.append("no named human and no published contact -- this can only be dropped "
                       "into an application portal, where silence is indistinguishable from "
                       "rejection and the acceptance test cannot resolve either way")
    if art_suitability < 0.5:
        reasons.append(f"strategy suitability {art_suitability:.2f} -- this approach is a "
                       f"guess about the engagement shape, not a read of it")

    if reasons:
        return "medium", reasons

    reasons.append("named target + live URL + falsifiable ask: a reply to this is a real "
                   "signal. NOTE: passing these checks means the artifact PERMITS the "
                   "acceptance event, it does not cause it.")
    return "low", reasons


def _verdict(checks: dict[str, bool], risk: str, art: Artifact, op: Opportunity) -> str:
    if art.strategy == "GRANT_FIT":
        return ("INTERNAL MEMO -- not outreach. A solicitation has no recipient who can "
                "reply; the only external event available is a submission before the "
                "close date. Read it, then bid or kill.")
    if risk == "high":
        bad = ", ".join(c for c in CORE if not checks[c])
        return f"DO NOT SEND -- fails {bad}; would produce an unfalsifiable outcome."
    if risk == "medium":
        return (f"Sendable after a 60-second human edit; {art.strategy} at "
                f"fit {op.fit_score:.2f}, ask = {art.price_or_date_ask}.")
    return (f"Send as-is. {art.strategy} -> {op.entity}; ask = {art.price_or_date_ask}. "
            f"Reply with a price or a date = acceptance-test hit.")


def grade(op: Opportunity, artifacts: Iterable[Artifact]) -> list[Grade]:
    graded: list[Grade] = []
    for art in artifacts:
        checks = check(op, art)
        art_score = sum(w for k, w in WEIGHTS.items() if checks[k])
        suit = float(getattr(art, "suitability", 1.0))
        risk, reasons = reward_hack_risk(checks, op, suit)
        penalty = {"low": 0.0, "medium": 0.10, "high": 0.45}[risk]
        total = max(0.0, 0.35 * op.fit_score + 0.40 * art_score
                        + 0.25 * suit - penalty)
        graded.append(Grade(
            variant_id=art.variant_id, rank=0,
            fit_score=round(op.fit_score, 4),
            artifact_score=round(art_score, 4),
            total=round(total, 4),
            reward_hack_risk=risk,
            reward_hack_reasons=reasons,
            checks=checks,
            one_line_verdict=_verdict(checks, risk, art, op),
            acceptance_event=ACCEPTANCE_EVENT.get(op.market, ACCEPTANCE_EVENT["M1"]),
        ))
    graded.sort(key=lambda g: -g.total)
    for i, g in enumerate(graded, 1):
        g.rank = i
    return graded


# --------------------------------------------------------------------------
# canon §6 E8 -- the verifier must exit non-zero on a soft-metric row.
# --------------------------------------------------------------------------
def verify_outreach_row(row: dict) -> tuple[bool, str]:
    """Score an outreach_log row. ONLY named-human + price-or-date counts.

    Returns (ok, reason). `ok=False` must make the caller exit non-zero.
    """
    who = str(row.get("named_human") or "").strip()
    resp = str(row.get("response") or "").strip()
    if not who or PLACEHOLDER.search(who):
        return False, f"no named human ({who!r})"
    if not resp:
        return False, "no response recorded"
    if SOFT_ASK.search(resp):
        return False, f"soft-metric response: {resp[:80]!r}"
    if re.search(r"(?i)^\s*(\d+\s+(replies|likes|views|impressions|stars|followers)|"
                 r"positive (feedback|response)|lots of interest|good engagement)", resp):
        return False, f"soft metric masquerading as a result: {resp[:80]!r}"
    if not (PRICE_TOK.search(resp) or DATE_TOK.search(resp)):
        return False, f"response names neither a price nor a date: {resp[:80]!r}"
    return True, "named human named a price or a date"
