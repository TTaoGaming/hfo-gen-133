"""
FACTORY CORE — gen-133 distribution-artifact factory.

Pipeline:  search -> parse -> fit -> generate -> grade -> queue

Design notes (deliberate, argued in stamps/FACTORY_PDCA_20260802.md):
  * stdlib only. No LangGraph / CrewAI. The pipeline is five pure functions over
    dataclasses; an orchestration framework would add a dependency and a failure
    surface for zero behavioural gain. Canon SIGRUN_CANON_5_QUESTIONS §1 and
    HIVE_REVIEW §9.5 both say freeze the stack this week.
  * Nothing in this package sends, posts, publishes, spends, or authenticates.
    The terminal operation is a write to outputs/factory_samples/.
"""
from __future__ import annotations

import dataclasses
import datetime as _dt
import hashlib
import html as _html
import json
import re
from typing import Any, Callable, Iterable


# --------------------------------------------------------------------------
# clock
# --------------------------------------------------------------------------
def utc_now() -> str:
    """clock_source: host_read"""
    return _dt.datetime.now(_dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def today_utc() -> str:
    return _dt.datetime.now(_dt.timezone.utc).strftime("%Y-%m-%d")


# --------------------------------------------------------------------------
# data model
# --------------------------------------------------------------------------
@dataclasses.dataclass
class Opportunity:
    """One specific, named, externally-verifiable target.

    Hard rule: `url` must be a real live URL and `entity` a real named org or
    person. An Opportunity without both is rejected by the pipeline -- that is
    the structural defence against "generic best-practice outreach template".
    """
    uid: str                       # stable hash id
    adapter: str                   # which adapter produced it
    market: str                    # M1 contracts / M2 employment / M6 grants ...
    title: str
    entity: str                    # named company / org / person
    url: str                       # live listing URL
    posted_utc: str = ""
    location: str = ""
    compensation: str = ""
    tags: list[str] = dataclasses.field(default_factory=list)
    body: str = ""                 # raw requirement text, plain
    contact: str = ""              # email/handle if the listing published one
    source_payload: dict[str, Any] = dataclasses.field(default_factory=dict)

    # populated by parse()/fit()
    requirements: list[str] = dataclasses.field(default_factory=list)
    fit_signals: list[str] = dataclasses.field(default_factory=list)
    fit_score: float = 0.0
    fit_components: dict[str, float] = dataclasses.field(default_factory=dict)

    def slug(self) -> str:
        base = f"{self.entity}-{self.title}"
        base = re.sub(r"[^a-zA-Z0-9]+", "-", base).strip("-").lower()
        return base[:60] or "opportunity"

    def to_json(self) -> dict[str, Any]:
        d = dataclasses.asdict(self)
        d["source_payload"] = {
            k: v for k, v in d["source_payload"].items()
            if isinstance(v, (str, int, float, bool, list)) and len(str(v)) < 4000
        }
        return d


@dataclasses.dataclass
class Artifact:
    """One generated distribution artifact (a variant)."""
    variant_id: str
    strategy: str                  # PROOF_FIRST / PILOT_OFFER / PROBLEM_MIRROR
    channel: str                   # where it would be sent
    subject: str
    body: str
    price_or_date_ask: str         # the falsifiable ask. empty => reward-hack
    named_target: str              # the specific human or org addressed
    evidence_urls: list[str] = dataclasses.field(default_factory=list)
    generator: str = "compositional_v1"
    word_count: int = 0
    suitability: float = 1.0       # is this STRATEGY right for this opportunity?
    suitability_reason: str = ""
    asset_id: str = ""             # which evidence asset the claims came from

    def to_json(self) -> dict[str, Any]:
        return dataclasses.asdict(self)


@dataclasses.dataclass
class Grade:
    variant_id: str
    rank: int
    fit_score: float
    artifact_score: float
    total: float
    reward_hack_risk: str          # low | medium | high
    reward_hack_reasons: list[str]
    checks: dict[str, bool]
    one_line_verdict: str
    acceptance_event: str = ""     # what would actually falsify this, per market

    def to_json(self) -> dict[str, Any]:
        return dataclasses.asdict(self)


# --------------------------------------------------------------------------
# helpers
# --------------------------------------------------------------------------
def make_uid(adapter: str, url: str, title: str) -> str:
    h = hashlib.sha256(f"{adapter}|{url}|{title}".encode("utf-8")).hexdigest()
    return f"{adapter}-{h[:12]}"


_TAG_RE = re.compile(r"<[^>]+>")
_WS_RE = re.compile(r"[ \t\xa0]+")


_MOJI = re.compile(r"[ÂÃ][\x80-\xbf‘-”·\xa0]")


def fix_mojibake(txt: str) -> str:
    """Repair UTF-8 bytes that a feed decoded as latin-1 ('Â·' -> '·').

    Several boards double-encode. Left unrepaired, the garbage gets quoted
    verbatim into an outreach body, which is an instant discard by any reader.
    """
    if not txt or not _MOJI.search(txt):
        return txt
    try:
        repaired = txt.encode("latin-1", "strict").decode("utf-8", "strict")
    except (UnicodeEncodeError, UnicodeDecodeError):
        return _MOJI.sub(" ", txt)          # cannot repair cleanly -> strip it
    return repaired if len(_MOJI.findall(repaired)) < len(_MOJI.findall(txt)) else txt


def strip_html(raw: str) -> str:
    """Markup -> plain targetable text.

    ORDER BUG FIXED 2026-08-02: entities must be unescaped BEFORE tags are
    stripped, and then re-checked. Several feeds ship escaped markup
    (`&lt;li&gt;`); stripping first and unescaping second turned those into real
    `<li>` tags that survived into extracted requirements and would have been
    quoted verbatim at a buyer.
    """
    if not raw:
        return ""
    txt = fix_mojibake(raw)
    for _ in range(3):                      # entities -> tags -> entities ...
        before = txt
        txt = _html.unescape(txt)
        for tag in ("</p>", "<br>", "<br/>", "<br />", "</li>", "</div>", "</h2>", "</h3>"):
            txt = txt.replace(tag, "\n")
        txt = txt.replace("<li>", "- ")
        txt = _TAG_RE.sub(" ", txt)
        if txt == before:
            break
    txt = _html.unescape(txt)               # remaining text entities
    txt = txt.replace(" ", " ").replace("’", "'").replace("—", "--")
    txt = _WS_RE.sub(" ", txt)
    txt = re.sub(r"\n{3,}", "\n\n", txt)
    return txt.strip()


_REQ_LEAD = re.compile(
    r"^\s*(?:[-*•●▪]|\d+[.)])\s+(.{12,200})$", re.M)
_REQ_KEYWORD = re.compile(
    r"(?i)\b(you (?:will|should|have|:)|experience (?:with|in)|proficien\w+|"
    r"familiar\w* with|strong (?:background|knowledge)|require\w*|must have|"
    r"looking for someone|we need|skills?:)\b")


# Section headers and boilerplate that look like requirements but say nothing.
_BOILER = re.compile(
    r"(?i)^(requirements?|qualifications?|responsibilities|benefits?|what you"
    r"(?:'ll| will)? (?:do|get)|about (?:us|the (?:role|team|company))|nice to have|"
    r"who you are|the role|perks|why join|apply now|equal opportunity|we offer|"
    r"your profile|tech stack|skills?)\s*[:.]?\s*$")


# Culture / benefits / values copy. Quoting this back as though it were a
# technical requirement is the tell of a machine that did not read the listing.
# Found 2026-08-02: a Samsara artifact quoted "You are a life-long learner: We
# have ambitious goals" and answered it with hand-tracking API seams.
_CULTURE = re.compile(
    r"(?i)(life[- ]long learner|growth mindset|ambitious goals|we are looking for "
    r"people|our values|diversity|inclusi|equal opportunity|competitive salary|"
    r"benefits|401\(?k\)?|health insurance|paid time off|unlimited pto|"
    r"work[- ]life balance|team player|passionate about|fast[- ]paced environment|"
    r"wear many hats|rock ?star|ninja|family|mission[- ]driven|make an impact|"
    r"generous|perks|stock options|dental|vision insurance|parental leave)")


def _quotable(s: str) -> bool:
    """Is this line clean enough to quote back at the buyer verbatim?"""
    if _BOILER.match(s) or _CULTURE.search(s):
        return False
    letters = sum(c.isalpha() or c.isspace() for c in s)
    if letters / max(len(s), 1) < 0.80:          # bullet glyph soup / mojibake residue
        return False
    if len(s.split()) < 4:
        return False
    if _MOJI.search(s):
        return False
    return True


def extract_requirements(body: str, limit: int = 12) -> list[str]:
    """Pull concrete requirement lines out of a listing body.

    Bulleted lines first (highest precision), then keyword-bearing sentences.
    Lines that are section headers, glyph soup, or too short to be specific are
    dropped -- a bad quote is worse than no quote.
    """
    out: list[str] = []
    seen: set[str] = set()

    def _add(s: str) -> None:
        s = _WS_RE.sub(" ", s).strip(" -*•·:;. ")
        if 16 <= len(s) <= 220 and _quotable(s):
            k = s.lower()[:60]
            if k not in seen:
                seen.add(k)
                out.append(s)

    for m in _REQ_LEAD.finditer(body):
        _add(m.group(1))
        if len(out) >= limit:
            return out
    for sent in re.split(r"(?<=[.!?])\s+|\n", body):
        if _REQ_KEYWORD.search(sent):
            _add(sent)
            if len(out) >= limit:
                break
    return out


# A bare '@' must NOT be preceded by whitespace -- otherwise the sentence
# "official mail only comes from addresses ending in @samsara.com" yields the
# contact "in@samsara.com". Whitespace is only tolerated around the obfuscated
# spellings, where it is conventional.
# A bare English " at " is NOT an obfuscated '@'. Allowing it turned "a job
# offer at Humana.com" into offer@Humana.com and "apply online at cloudbeds.com"
# into online@cloudbeds.com. Only the bracketed spellings count.
_EMAIL_RE = re.compile(
    r"(?:\b([\w.+-]{2,64})@|\b([\w.+-]{2,64})\s?(?:\[at\]|\(at\)|\{at\})\s?)"
    r"([\w-]+(?:\.[\w-]+)+)\b")

#: English words that appear immediately before an address in running prose.
_NOT_A_LOCALPART = frozenset(
    "in to at from the a an is are was were be been and or but for with on of "
    "ending end only come comes coming send sent sending mail email address "
    "domain here there this that our your their its all any".split())

#: Addresses that exist for a legally or ethically distinct purpose. Sending an
#: unsolicited pitch to any of these is worse than sending nothing.
#:
#: FOUND 2026-08-02 while assembling the approve list: the extractor had picked
#: `accessibleinterviewing@samsara.com` and `accommodations@cloudbeds.com` --
#: ADA disability-accommodation request lines -- and offered them as the hiring
#: contact for a cold pitch. That is not a near-miss, it is a harm.
_CONTACT_BLOCKLIST = re.compile(
    r"(?i)^(accessib\w*|accommodat\w*|ada|disabilit\w*|eeo|compliance|legal|privacy|"
    r"dpo|gdpr|security|abuse|report\w*|no-?reply|donot\w*|unsubscribe|postmaster|"
    r"webmaster|press|media|investor\w*|billing|invoice\w*|support|help|helpdesk|"
    r"info|sales|marketing|newsletter|example|test|your\w*|name|email|user)$")


def find_contact(body: str) -> str:
    """First address in the body that is plausibly a human reachable about work.

    Returns "" rather than a wrong address: a portal application with no contact
    is merely weak, whereas a pitch sent to an accessibility line is a harm.
    """
    if not body:
        return ""
    for m in _EMAIL_RE.finditer(body):
        local = m.group(1) or m.group(2) or ""
        domain = m.group(3)
        if not local or len(local) < 3:
            continue
        if local.lower() in _NOT_A_LOCALPART:
            continue
        if _CONTACT_BLOCKLIST.match(local):
            continue
        if not re.search(r"\.[a-z]{2,10}$", domain, re.I):
            continue
        return f"{local}@{domain}"
    return ""


#: Entity strings that are not a company name. QA sweep 2026-08-02 found
#: "Code", "Stealth", "Remote", "*Y Combinator", "10 Ancestry.com Operations",
#: "Adyen ( https://www.adyen.com/ )" reaching the `target:` line of an artifact.
_JUNK_ENTITY = re.compile(
    r"(?i)^(remote|onsite|hybrid|stealth|confidential|various|multiple|n/?a|"
    r"unknown|anywhere|worldwide|company|startup|client|tbd|none|null|"
    r"full[- ]time|part[- ]time|contract|freelance)$")


def clean_entity(raw: str) -> str:
    """Normalise a company name, or return "" if it is not one.

    "" is the right answer for junk: `validate_opportunity` then rejects the
    Opportunity, which is better than addressing a letter to "Remote".
    """
    if not raw:
        return ""
    s = _html.unescape(fix_mojibake(raw)).strip()
    s = re.sub(r"\(\s*https?://[^)]*\)", "", s)        # "Adyen ( https://... )"
    s = re.sub(r"https?://\S+", "", s)
    s = re.sub(r"^[\s*\-–—•|,.]+", "", s)              # "*Y Combinator"
    s = re.sub(r"^\d+\s+(?=[A-Za-z])", "", s)          # "10 Ancestry.com Operations"
    s = re.sub(r"\s*\(\s*\)\s*", " ", s)
    s = _WS_RE.sub(" ", s).strip(" -–—|,;:.")
    if len(s) < 2 or _JUNK_ENTITY.match(s):
        return ""
    if not re.search(r"[A-Za-z]{2}", s):               # digits/symbols only
        return ""
    return s[:80]


def clean_title(raw: str) -> str:
    if not raw:
        return ""
    s = _html.unescape(_html.unescape(fix_mojibake(raw)))
    s = _TAG_RE.sub(" ", s)
    return _WS_RE.sub(" ", s).strip(" -–—|,;:")[:140]


def truncate_words(text: str, n: int) -> str:
    w = text.split()
    return text if len(w) <= n else " ".join(w[:n]) + " ..."


# --------------------------------------------------------------------------
# pipeline
# --------------------------------------------------------------------------
class RejectedOpportunity(Exception):
    pass


class AlreadyQueued(Exception):
    """This opportunity already has a sample from an earlier run today.

    Not an error: the hourly cron re-searches the same feeds by design, so most
    of what it finds is already queued. Counted separately from failures."""


def validate_opportunity(op: Opportunity) -> None:
    """Structural gate. An Opportunity that fails this is never generated against."""
    if not op.url.startswith(("http://", "https://")):
        raise RejectedOpportunity(f"no live URL: {op.url!r}")
    if not op.entity or len(op.entity) < 2:
        raise RejectedOpportunity("no named entity")
    if not op.title:
        raise RejectedOpportunity("no title")
    if len(op.body) < 120:
        raise RejectedOpportunity(f"body too thin ({len(op.body)} chars) to target specifically")


def run_pipeline(
    adapters: Iterable[Any],
    *,
    fit_fn: Callable[[Opportunity], None],
    generate_fn: Callable[[Opportunity, int], list[Artifact]],
    grade_fn: Callable[[Opportunity, list[Artifact]], list[Grade]],
    emit_fn: Callable[[Opportunity, list[Artifact], list[Grade]], str],
    per_adapter: int = 12,
    n_variants: int = 3,
    min_fit: float = 0.0,
    log: Callable[[str], None] = print,
) -> dict[str, Any]:
    """Search -> parse -> fit -> generate -> grade -> queue. Returns a run report."""
    report: dict[str, Any] = {
        "run_started_utc": utc_now(),
        "adapters": {},
        "samples": [],
        "errors": [],
    }
    for ad in adapters:
        name = ad.name
        stat = {"market": ad.market, "fetched": 0, "rejected": 0,
                "kept": 0, "samples": 0, "status": "ok", "note": ""}
        try:
            ops = list(ad.search())
            stat["fetched"] = len(ops)
        except Exception as exc:                       # adapter isolation
            stat["status"] = "error"
            stat["note"] = f"{type(exc).__name__}: {exc}"
            report["adapters"][name] = stat
            report["errors"].append(f"{name}: {exc}")
            log(f"  [{name}] ERROR {exc}")
            continue

        if getattr(ad, "blocked_reason", ""):
            stat["status"] = "blocked"
            stat["note"] = ad.blocked_reason

        scored: list[Opportunity] = []
        for op in ops:
            try:
                validate_opportunity(op)
            except RejectedOpportunity as exc:
                stat["rejected"] += 1
                continue
            op.requirements = extract_requirements(op.body)
            if not op.contact:
                op.contact = find_contact(op.body)
            fit_fn(op)
            scored.append(op)

        scored.sort(key=lambda o: o.fit_score, reverse=True)
        scored = [o for o in scored if o.fit_score >= min_fit][:per_adapter]
        stat["kept"] = len(scored)

        for op in scored:
            try:
                arts = generate_fn(op, n_variants)
                if not arts:
                    stat["no_strategy"] = stat.get("no_strategy", 0) + 1
                    continue
                grades = grade_fn(op, arts)
                path = emit_fn(op, arts, grades)
                stat["samples"] += 1
                best = min(grades, key=lambda g: g.rank)
                report["samples"].append({
                    "uid": op.uid, "adapter": name, "market": ad.market,
                    "entity": op.entity, "title": op.title, "url": op.url,
                    "fit_score": round(op.fit_score, 3),
                    "best_variant": best.variant_id,
                    "best_total": round(best.total, 3),
                    "reward_hack_risk": best.reward_hack_risk,
                    "path": path,
                })
            except AlreadyQueued:
                stat["deduped"] = stat.get("deduped", 0) + 1
            except Exception as exc:
                report["errors"].append(f"{name}/{op.uid}: {type(exc).__name__}: {exc}")
                log(f"  [{name}] sample error {op.uid}: {exc}")

        report["adapters"][name] = stat
        log(f"  [{name}] fetched={stat['fetched']} rejected={stat['rejected']} "
            f"kept={stat['kept']} new={stat['samples']} "
            f"dedup={stat.get('deduped', 0)} nostrat={stat.get('no_strategy', 0)} "
            f"{stat['status']}")

    report["run_finished_utc"] = utc_now()
    report["total_samples"] = len(report["samples"])
    return report


def jsonl_append(path: str, row: dict[str, Any]) -> None:
    """Single-line append. NOTE: NTFS gives no atomic-append guarantee
    (JORMUNGANDR_BOUNDARY_TESTS B-1). This factory runs single-writer by design;
    the hourly cron must not overlap itself."""
    line = json.dumps(row, ensure_ascii=False, separators=(",", ":"))
    assert "\n" not in line
    with open(path, "a", encoding="utf-8", newline="\n") as fh:
        fh.write(line + "\n")
