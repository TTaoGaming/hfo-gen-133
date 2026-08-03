"""
Variant generation.

Three strategies, deliberately different *approaches* rather than reworded
copies -- otherwise the overnight A/B tests nothing:

  PROOF_FIRST     lead with a live artifact + the one seam that matches their
                  stated requirement. Ask = a specific date.
  PILOT_OFFER     lead with a fixed scope, a price band and a refund condition.
                  Ask = a price confirmation.
  PROBLEM_MIRROR  quote their own requirement back and ask the one disqualifying
                  question a real buyer can answer in a sentence. Ask = answer + date.

TWO RULES LEARNED FROM THE FIRST LIVE RUN (2026-08-02T04:10Z), both structural:

 1. **A template never hardcodes a claim.** Every claim sentence is interpolated
    from the chosen asset's own `pitch` / `proof_sentence` / `scale_fact`. The
    first run produced "I build webcam input layers ... https://github.com/..."
    because the prose was hardcoded while the URL came from asset selection.
    Claim and link can no longer disagree, because they now come from one object.

 2. **Strategies are scored for SUITABILITY, not just emitted.** Offering a
    $4-8k fixed-price pilot to a company hiring a salaried employee is not a
    variant, it is a discard. PROOF_FIRST without a live demo asset is a link to
    a repo dressed as a demo. Unsuitable strategies are dropped, not ranked low.

Generation is deterministic and costs $0. `llm_variants()` is the optional hook
for a model-written variant; it is off by default because
`L_UNBOUNDED_AGENT_SPEND` is an open failure class and no cost ceiling is wired.
"""
from __future__ import annotations

import re
import textwrap

from .core import Artifact, Opportunity, truncate_words
from .profile import CAPABILITIES, DISCLOSURE, OFFER, OPERATOR, assets_for

STRATEGIES = ("PROOF_FIRST", "PILOT_OFFER", "PROBLEM_MIRROR",
              "PORTAL_PITCH", "JAM_ENTRY", "GRANT_FIT")
_NEXT_DAYS = "Tuesday or Thursday"

_CONTRACT_SHAPE = re.compile(
    r"(?i)\b(contract|freelance|freelancer|consultant|consulting|part[- ]time|"
    r"project[- ]based|fixed[- ]price|statement of work|\bsow\b|hourly|day rate|"
    r"agency|studio|short[- ]term|temporary|1099|b2b)\b")
_FULLTIME_SHAPE = re.compile(
    r"(?i)\b(full[- ]time|salary|salaried|benefits package|401\(?k\)?|equity|"
    r"health insurance|pto|paid time off|permanent)\b")


def _channel(op: Opportunity) -> str:
    if op.adapter == "hn_contracts":
        return "email reply to the HN thread contact" if op.contact else "HN thread reply"
    if op.adapter == "linkedin_cached":
        return "LinkedIn DM / InMail"
    if op.adapter == "game_portals":
        return f"{op.entity} developer-portal submission form / published intake"
    if op.adapter == "itch_jams":
        return "itch.io jam community post or a message to the jam host"
    if op.market == "M6":
        return "INTERNAL MEMO — not sendable; a solicitation has no recipient"
    return "job application note (cover-letter field)"


def _addressee(op: Opportunity) -> str:
    person = (op.source_payload or {}).get("person")
    if person:
        return f"Hi {str(person).split()[0]}"
    return "Hi"


def _cap_hits(text: str) -> int:
    from .fit import _matcher            # word-boundary; see the bug note in fit.py
    low = text.lower()
    return sum(1 for t in CAPABILITIES if _matcher(t).search(low))


def _top_requirement(op: Opportunity) -> str:
    """The single requirement line the outreach will mirror.

    Returns "" when no requirement line actually names something the operator
    does. Previously this accepted the best of a bad set (`best_hits >= 0`),
    which is how culture copy got quoted back as a technical requirement. A
    quote that misses is worse than no quote: it proves nobody read the listing.
    """
    if not op.requirements:
        return ""
    best, best_hits = "", 0
    for r in op.requirements[:10]:
        hits = _cap_hits(r)
        if hits > best_hits:
            best, best_hits = r, hits
    return truncate_words(best.rstrip(". "), 26) if best_hits > 0 else ""


def _article(phrase: str) -> str:
    """'held-out test runner ...' -> 'the held-out test runner ...'"""
    if not phrase:
        return phrase
    first = phrase.split()[0].lower().strip("(),")
    if first in ("the", "a", "an", "my", "its", "every", "all") or phrase[0].isupper():
        return phrase
    return "the " + phrase


#: The PROBLEM_MIRROR question must be about THEIR failure domain, not ours.
_DOMAIN_FAILURES = (
    (re.compile(r"(?i)\b(camera|webcam|video|frame|vision|tracking|pose|gesture|ar/vr|webxr)\b"),
     "bad lighting, dropped frames, a user turning away from the camera"),
    (re.compile(r"(?i)\b(llm|prompt|rag|chatbot|agent|gpt|claude|gemini|embedding)\b"),
     "malformed documents, inputs that look nothing like your eval set, users pasting "
     "things the pipeline has never seen"),
    (re.compile(r"(?i)\b(etl|pipeline|warehouse|analytics|data engineer|spark|airflow)\b"),
     "late-arriving rows, a schema that drifted upstream, nulls where the contract "
     "promised values"),
)
_DEFAULT_FAILURE = ("malformed or unexpected input, upstream changes nobody announced, "
                    "users doing something the happy path never anticipated")


def _failure_modes(op: Opportunity) -> str:
    blob = f"{op.title} {' '.join(op.tags)} {op.body[:2500]}"
    for pat, text in _DOMAIN_FAILURES:
        if pat.search(blob):
            return text
    return _DEFAULT_FAILURE


def _seam_for(op: Opportunity, asset: dict) -> str:
    seams = asset.get("technical_seams") or []
    if not seams:
        return ""
    low = f"{op.title} {op.body}".lower()
    if any(t in low for t in ("test", "ci", "qa", "reliability", "robust", "eval")):
        for s in seams:
            if any(k in s.lower() for k in ("test", "noisy", "ci", "held-out")):
                return s
    if any(t in low for t in ("camera", "video", "stream", "webcam")):
        for s in seams:
            if "video" in s.lower() or "setVideoSource" in s:
                return s
    return seams[0]


def _wrap(text: str) -> str:
    out = []
    for para in text.strip().split("\n\n"):
        para = re.sub(r"\s+", " ", para).strip()
        if para:
            out.append(textwrap.fill(para, width=88))
    return "\n\n".join(out)


# ---------------------------------------------------------------------------
# strategy suitability
# ---------------------------------------------------------------------------
def _asset(aid: str) -> dict:
    from .profile import ASSETS
    return next(a for a in ASSETS if a["id"] == aid)


def strategy_plan(op: Opportunity) -> list[tuple[str, dict, float, str]]:
    """-> [(strategy, asset, suitability 0..1, rationale)], best first.

    A strategy scoring 0 is DROPPED, not emitted with a low rank.
    """
    # --- M5 games and M6 grants have their own artifact shapes. A portal
    # --- submission is a repackaging plan, not a cover letter; a grant is a
    # --- bid/no-bid call against a hard close date. Sharing the job-application
    # --- templates with them would be the same claim/context mismatch that
    # --- produced hand-tracking pitches at car washes.
    if op.market == "M5":
        games = _asset("omega_games")
        if op.adapter == "game_portals":
            return [("PORTAL_PITCH", games, 0.9,
                     "standing submission channel with a published intake")]
        return [("JAM_ENTRY", games, 0.7,
                 "dated event with a named host and published rules")]
    if op.market == "M6":
        return [("GRANT_FIT", _asset("demo01_handpiano"), 0.5,
                 "federal solicitation -- bid/no-bid against a published close date")]

    ranked = assets_for(f"{op.title} {' '.join(op.tags)} {op.body}")
    if not ranked:
        return []          # nothing in the portfolio speaks to this listing
    live = [a for a in ranked if a.get("is_live_demo")]
    blob = f"{op.title} {op.body}"
    contract = bool(_CONTRACT_SHAPE.search(blob)) or op.market in ("M1", "M5")
    fulltime = bool(_FULLTIME_SHAPE.search(blob))
    req = _top_requirement(op)
    plan: list[tuple[str, dict, float, str]] = []

    # --- PROOF_FIRST: needs a genuinely live, relevant demo -----------------
    if live:
        asset = live[0]
        rel = min(sum(1 for t in asset["relevant_to"] if t in blob.lower()) / 4.0, 1.0)
        if rel > 0:
            plan.append((
                "PROOF_FIRST", asset, round(0.55 + 0.45 * rel, 3),
                f"live demo {asset['id']} matches {rel:.0%} of its relevance terms"))
    # else: no live demo relevant to this listing -> the strategy is dropped.

    # --- PILOT_OFFER: needs contract shape AND the asset the OFFER describes -
    #
    # BUG FOUND 2026-08-02 by QA sweep: 58 of 66 PILOT_OFFER variants pitched
    # "a camera-control layer: a working webcam/gesture input layer" and then
    # cited the agent-harness repo as proof. OFFER is fixed prose about the
    # camera layer, so it is only truthful next to the camera-layer asset.
    # Binding them here means the pair cannot drift.
    offer_asset = live[0] if live else None
    if offer_asset is not None:
        if contract:
            s = 0.9 if op.market in ("M1", "M5") else 0.7
            if fulltime:
                s -= 0.35                  # listing mixes both; hedge down
            plan.append(("PILOT_OFFER", offer_asset, round(max(s, 0.0), 3),
                         "listing carries contract/freelance language"))
        elif not fulltime:
            plan.append(("PILOT_OFFER", offer_asset, 0.35,
                         "engagement shape unstated -- pilot offer is a guess"))
    # no live camera-layer asset relevant here, or a clearly salaried listing
    # -> PILOT_OFFER is dropped rather than pitched against the wrong proof.

    # --- PROBLEM_MIRROR: needs a quotable, on-domain requirement -----------
    if req:
        hits = _cap_hits(req)
        s = min(0.45 + 0.18 * hits, 1.0)
        plan.append(("PROBLEM_MIRROR", ranked[0], round(s, 3),
                     f"quotable requirement with {hits} capability overlap(s)"))

    plan.sort(key=lambda x: -x[2])
    return plan


# ---------------------------------------------------------------------------
def compose_variants(op: Opportunity, n: int = 3) -> list[Artifact]:
    plan = strategy_plan(op)
    if not plan:
        return []
    channel = _channel(op)
    hi = _addressee(op)
    who = op.entity or "your team"
    req = _top_requirement(op)

    out: list[Artifact] = []
    for strategy, asset, suit, rationale in plan[:max(1, n)]:
        seam = _seam_for(op, asset)
        builder = {"PROOF_FIRST": _proof_first, "PILOT_OFFER": _pilot_offer,
                   "PROBLEM_MIRROR": _problem_mirror, "PORTAL_PITCH": _portal_pitch,
                   "JAM_ENTRY": _jam_entry, "GRANT_FIT": _grant_fit}[strategy]
        subject, body, ask = builder(op, who, hi, req, asset, seam)
        body = (_wrap(body) + f"\n\n-- \n{OPERATOR['handle']} · {OPERATOR['email']}\n"
                f"{OPERATOR['github']}\n({DISCLOSURE})")
        out.append(Artifact(
            variant_id=f"{op.uid}::{strategy}",
            strategy=strategy, channel=channel,
            subject=subject, body=body, price_or_date_ask=ask,
            named_target=op.entity or (op.source_payload or {}).get("person", ""),
            evidence_urls=([asset["url"]] if asset.get("url") else [])
                          + ([_asset("demo01_handpiano")["url"]]
                             if strategy in ("PORTAL_PITCH", "JAM_ENTRY") else [])
                          + [op.url],
            generator="compositional_v1",
            word_count=len(body.split()),
            suitability=suit, suitability_reason=rationale, asset_id=asset["id"],
        ))
    return out


# --- strategy builders (all claims interpolated from `asset`) --------------
def _proof_first(op, who, hi, req, asset, seam):
    subject = f"{asset['one_line'].split(':')[0].strip().capitalize()} — re: {truncate_words(op.title, 8)}"
    mirror = f'Your listing asks for "{req}". ' if req else ""
    seam_line = (f"The part that is usually missing is {_article(seam)}: "
                 f"{asset['why_it_matters']}. " if seam else "")
    body = f"""
{hi} — {asset['pitch']}. Rather than describe it: {asset['url']} — {asset['proof_sentence']}.

{mirror}{seam_line}It is {asset['scale_fact']}.

I would rather show than pitch. Do you have 15 minutes {_NEXT_DAYS}? I will walk through it
against {who}'s actual use case and you can tell me on that call whether it is useful.
"""
    return subject, body, f"a 15-minute call on {_NEXT_DAYS}"


def _pilot_offer(op, who, hi, req, asset, seam):
    subject = f"{OFFER['duration']}, {OFFER['price_band']} — {OFFER['name']} for {who}"
    mirror = f'You wrote that you need "{req}". ' if req else ""
    proof = (f"Working proof this is not vapour — {asset['url']} — {asset['proof_sentence']}."
             if asset.get("url") else
             f"Proof of throughput: {asset['proof_sentence']}.")
    body = f"""
{hi} — a concrete offer rather than a resume.

{mirror}I ship a {OFFER['name']}: {OFFER['scope']}. Fixed scope, {OFFER['duration']},
{OFFER['price_band']}. The deliverable is {OFFER['deliverable']}.

The condition that makes it safe for you: {OFFER['guarantee']}.

{proof}{(' It exposes ' + _article(seam) + '.') if seam else ''}

Two questions and I will stop taking your time: is {OFFER['price_band']} inside the range
you can approve without a procurement cycle, and if it is, can we start the week after next?
"""
    return subject, body, f"confirm {OFFER['price_band']} is in range, and a start week"


def _problem_mirror(op, who, hi, req, asset, seam):
    quoted = req or truncate_words(op.title, 10)
    subject = f'"{truncate_words(quoted, 9)}" — one question first'
    proof = (f"I ask because of what I run at {asset['url']}: {asset['proof_sentence']}"
             if asset.get("url") else
             f"I ask because {asset['proof_sentence']}")
    body = f"""
{hi} — I read the {who} listing properly, so one question first, because the answer decides
whether I am worth your time.

You listed: "{quoted}"

The question: when that breaks in production, is it breaking because the logic is wrong, or
because the input is wrong — {_failure_modes(op)}? Those need opposite fixes, and most
applicants will not ask you which one you actually have.

{proof}. The part I got right there was not the clever layer, it was
{_article(seam) or 'the layer underneath it'}: {asset['why_it_matters']}.

Tell me which of the two it is, and whether {_NEXT_DAYS} works for 15 minutes, and I will
come with something specific to your stack.
"""
    return subject, body, f"answer the input-vs-model question + 15 minutes {_NEXT_DAYS}"


# --- M5 / M6 builders ------------------------------------------------------
def _shortlist(k: int = 3) -> list[str]:
    from .profile import GAME_CATALOGUE
    return GAME_CATALOGUE["portal_candidates"][:k]


def _portal_pitch(op, who, hi, req, asset, seam):
    """A repackaging PLAN, not a cover letter. The operator asked for the
    distribution artifact, not the game."""
    from .profile import GAME_CATALOGUE as G
    picks = _shortlist(3)
    sp = op.source_payload or {}
    verified = sp.get("requirements_verified", False)
    reqs = sp.get("known_requirements") or []
    # quote one of THEIR published requirements, so the pitch demonstrably
    # answers their spec rather than describing our catalogue at them
    their_req = next((r for r in reqs if "iframe" in r.lower() or "mobile" in r.lower()),
                     reqs[0] if reqs else "")
    mirror = (f'\nYou require: "{their_req}". Both points are addressed below.\n'
              if their_req else "")
    caveat = ("" if verified else
              "\nI have not been able to read your submission spec directly -- your "
              "developer site renders client-side and returns no text to a plain fetch -- "
              "so tell me where the current spec lives and I will conform to it exactly "
              "rather than guess.\n")
    live = _asset("demo01_handpiano")
    subject = f"{len(G['portal_candidates'])} self-contained HTML5 titles — submission fit for {who}"
    body = f"""
{hi} — I have a catalogue of {G['total_titles']} finished HTML5 games and I want to put the
right ones on {who}. This is the honest version, including what is not ready.
{mirror}
NOTHING OF MINE IS PUBLISHED YET, so there is no store page to judge me by. The closest live
build is {live['url']} — {live['proof_sentence']}. It is the same construction as the
catalogue: one page, no install, runs on a phone.

WHAT EXISTS: {G['total_titles']} titles, every one a single self-contained index.html with no
external network calls. Median {G['median_bytes']:,} bytes; the largest is {G['max_bytes']:,}.
{G['touch_ready']} of {G['total_titles']} already handle touch and pointer input.

WHAT IS NOT READY, stated up front: {G['xframe_blocked']} of {G['total_titles']} ship an
X-Frame-Options SAMEORIGIN header that blocks iframe embedding. That is one line per file and
I will have it removed before I submit anything. I am also excluding
{len(G['ip_encumbered'])} titles whose names are trademark-encumbered rather than send you
something you would have to take down.

That leaves {len(G['portal_candidates'])} submittable titles. My first three for you:
{picks[0]}, {picks[1]}, {picks[2]}.

REPACKAGING PLAN, per title: strip the frame header, wire your SDK for ads and analytics,
verify touch on a real handset at portrait and landscape, hold the payload under 100 KB, and
hand you a build plus a 30-second capture.
{caveat}
Two questions: is a batch of three the right first submission for {who}, or do you prefer one
title through review before more? And what is your current review turnaround, so I can plan
the work against a real date?
"""
    return subject, body, (f"{who}'s review turnaround (a date or a number of days) "
                           f"and whether to submit 1 title or a batch of 3")


def _jam_entry(op, who, hi, req, asset, seam):
    from .profile import GAME_CATALOGUE as G
    joined = (op.source_payload or {}).get("joined", 0)
    jam = op.title
    body = f"""
{hi} — about {jam}: I build small self-contained browser games and I would like to enter.

Two things that may be useful to you as the host. First, my builds are single-file HTML5,
median {G['median_bytes']:,} bytes, no external requests -- so they load instantly in a browser
and are trivial to judge on a phone. Second, I have a working webcam hand-tracking layer
({_asset('demo01_handpiano')['url']}) and I would like to build the entry around
gesture input, which is unusual enough that it gives your players something they have not
tried in another jam.

Before I commit the time, two questions: does an entry using camera input fall inside your
rules as published, and is the submission deadline as listed on the jam page the real one?

If both are yes I will have a playable build in by the deadline and will credit the jam.
"""
    return (f"Entering {jam} with a gesture-controlled browser build",
            body,
            "confirm camera input is allowed under the rules + confirm the deadline date")


def _grant_fit(op, who, hi, req, asset, seam):
    """Grants have no human to reply. The artifact is a bid/no-bid memo for the
    operator himself, ending in a hard external date."""
    sp = op.source_payload or {}
    close = sp.get("closeDate") or "not stated"
    number = sp.get("number") or "n/a"
    matched = sp.get("matched_query") or "the search term"
    subject = f"BID/NO-BID — {who} {number}: {truncate_words(op.title, 8)}"
    body = f"""
INTERNAL MEMO -- this is a decision aid for you, not an outreach letter. Grants have no
recipient who can reply, so nothing here is sendable.

OPPORTUNITY: {op.title}
Agency: {who} · Number: {number} · Close date: {close}
Listing: {op.url}

WHY IT SURFACED: the solicitation text matched "{matched}", which is the overlap with
{asset['url']} -- {asset['proof_sentence']}.

THE HONEST ASSESSMENT: canon puts grants LAST on speed -- P(income in 90 days) = 0.25 and
6-12 months to cash, against ~0.45-0.60 for contracts and employment. A federal proposal is
multi-week unpaid work with no interim signal. Against your stated need -- money soon enough
to cover API costs and living expenses -- this is the wrong instrument unless the close date
is far enough out that it costs you nothing you would otherwise spend earning.

THE DECISION, and it is yours: bid only if you can name today what you would build, and only
if the close date above is more than six weeks away. Otherwise mark it no-bid and spend the
hours on the contract lane.

NEXT CHECK: read the full solicitation at the listing URL before any drafting.
"""
    return subject, body, f"bid/no-bid decision against close date {close}"


# ---------------------------------------------------------------------------
def llm_variants(op: Opportunity, n: int = 1, *, model: str = "",
                 max_cost_usd: float = 0.0) -> list[Artifact]:
    """Optional model-written variant. Disabled unless a budget is passed.

    Deliberately unimplemented at v0: `L_UNBOUNDED_AGENT_SPEND` is open and no
    cost ceiling exists in this forge. Wire E2 (MAX_RUN_COST_USD + a ledger that
    exits non-zero when exceeded) before enabling.
    """
    if max_cost_usd <= 0:
        return []
    raise NotImplementedError(
        "llm_variants requires the E2 cost ceiling. See canon §6 E2.")
