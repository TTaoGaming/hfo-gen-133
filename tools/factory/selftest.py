"""
Held-out tests for the factory. These test the REFUSALS, not the happy path --
a factory that cannot refuse is a reward-hack generator.

Run:  python -m tools.factory.run_factory --selftest
Exit 0 = all pass. Non-zero = the factory is not safe to run unattended.
"""
from __future__ import annotations

import dataclasses

from .core import Artifact, Opportunity, RejectedOpportunity, extract_requirements, \
    make_uid, strip_html, validate_opportunity
from .generate import compose_variants
from .grade import grade, verify_outreach_row

CASES: list[tuple[str, callable]] = []


def case(name):
    def deco(fn):
        CASES.append((name, fn))
        return fn
    return deco


def _op(**kw) -> Opportunity:
    base = dict(
        uid="t-1", adapter="remoteok", market="M2",
        title="Computer Vision Engineer",
        entity="Acme Robotics",
        url="https://example.com/jobs/1",
        body=("We are looking for someone with experience in computer vision and "
              "real-time video pipelines. You will build hand tracking for our "
              "consumer product using MediaPipe and OpenCV. Requirements:\n"
              "- 3+ years of Python\n- Experience with pose estimation\n"
              "- Ship production code. Contact: hiring@acme.example\n") * 2,
        tags=["computer vision", "python"],
    )
    base.update(kw)
    return Opportunity(**base)


# --------------------------------------------------------------------------
@case("E8: outreach verifier EXITS NON-ZERO on a soft-metric row")
def t_soft_metric():
    ok, why = verify_outreach_row({"named_human": "Jane Okafor", "response": "3 replies"})
    assert ok is False, "a '3 replies' row must FAIL -- this is the canon E8 test"
    ok2, _ = verify_outreach_row({"named_human": "Jane Okafor",
                                  "response": "let me know what you think"})
    assert ok2 is False
    ok3, _ = verify_outreach_row({"named_human": "", "response": "$6,000 works"})
    assert ok3 is False, "no named human must fail even with a price"
    ok4, why4 = verify_outreach_row({"named_human": "Jane Okafor",
                                     "response": "we can do $6,000, start Monday"})
    assert ok4 is True, why4
    return "soft metrics rejected, price+date accepted"


@case("opportunity without a live URL is REJECTED before generation")
def t_no_url():
    for bad in (_op(url=""), _op(url="not-a-url"), _op(entity=""), _op(body="too short")):
        try:
            validate_opportunity(bad)
        except RejectedOpportunity:
            continue
        raise AssertionError(f"should have been rejected: {bad.url!r}/{bad.entity!r}")
    validate_opportunity(_op())
    return "4 malformed opportunities rejected, 1 valid accepted"


@case("every generated variant carries a falsifiable price-or-date ask")
def t_ask_present():
    op = _op()
    op.requirements = extract_requirements(op.body)
    arts = compose_variants(op, 3)
    assert len(arts) == 3, len(arts)
    for a in arts:
        assert a.price_or_date_ask.strip(), f"{a.strategy} has no ask"
        assert a.named_target, f"{a.strategy} has no named target"
        assert op.url in a.evidence_urls
    assert len({a.strategy for a in arts}) == 3, "variants must use distinct strategies"
    assert len({a.body for a in arts}) == 3, "variants must not be identical text"
    return f"3 distinct strategies, all with asks ({[a.strategy for a in arts]})"


@case("grader scores an ask-less artifact as reward_hack_risk=HIGH")
def t_grader_catches_decoration():
    op = _op()
    op.fit_score = 0.9
    good = compose_variants(op, 1)[0]
    bad = dataclasses.replace(good, variant_id="t::BAD", price_or_date_ask="",
                              named_target="")
    gs = {g.variant_id: g for g in grade(op, [good, bad])}
    assert gs["t::BAD"].reward_hack_risk == "high", gs["t::BAD"].reward_hack_risk
    assert gs["t::BAD"].total < gs[good.variant_id].total
    assert "DO NOT SEND" in gs["t::BAD"].one_line_verdict
    return f"ask-less variant graded high-risk ({gs['t::BAD'].total:.3f} vs {gs[good.variant_id].total:.3f})"


@case("placeholder targets ('your company', '[Name]') are caught as high risk")
def t_placeholder():
    op = _op(entity="your company")
    op.fit_score = 0.8
    art = compose_variants(op, 1)[0]
    g = grade(op, [art])[0]
    assert g.reward_hack_risk == "high", g.reward_hack_risk
    return "placeholder entity -> high risk"


@case("an off-domain listing produces NO artifact at all, not a confident irrelevant one")
def t_mirror():
    op = _op(body="Underwater basket weaving for aquatic hobbyists. " * 20,
             title="Basket Weaver", tags=[])
    op.fit_score = 0.5
    assert compose_variants(op, 3) == [], "generated a pitch for an off-domain listing"
    return "zero variants emitted for an unrelated listing"


@case("REGRESSION 2026-08-02: substring capability matches are not evidence")
def t_substring_false_positive():
    """Adversarial review found a car-detailing lot-attendant listing scoring
    fit 0.471 and grading 'send as-is'. Its ENTIRE capability evidence was
    'rag' matched inside 'cove(rag)e' and 'unity' inside 'opport(unity)'."""
    from .fit import score as fit_score
    from .profile import assets_for
    body = ("Vehicle Detailing: Clean, detail, and prepare vehicles so they are "
            "showroom-ready for resale. We offer dependent coverage and this "
            "opportunity supports our community of associates. ") * 6
    op = _op(title="Lot Attendant", entity="Clutch", body=body, tags=[])
    fit_score(op)
    assert op.fit_components["capability"] == 0.0, \
        f"substring false positives survived: {op.fit_signals}"
    assert assets_for(body) == [], "an irrelevant listing still matched an asset"
    assert compose_variants(op, 3) == [], "still generated a pitch for a car wash"
    return f"car-wash listing: capability=0.0, assets=[], variants=[] (fit {op.fit_score:.3f})"


@case("risk cannot be LOW without capability evidence and a reachable human")
def t_world_dependent_checks():
    """The grader must depend on something the factory does not control,
    otherwise 'low risk' is the generator grading its own template."""
    op = _op()                                # has 'Contact: hiring@acme.example'
    op.requirements = extract_requirements(op.body)
    op.contact = "hiring@acme.example"
    op.fit_score = 0.7
    art = compose_variants(op, 1)[0]
    g = grade(op, [art])[0]
    assert g.checks["capability_evidence"], "on-domain listing failed capability_evidence"
    assert g.checks["deliverable_to_human"], "published contact failed deliverability"

    portal = _op()                            # same listing, no way to reach a person
    portal.requirements = extract_requirements(portal.body)
    portal.contact = ""
    portal.fit_score = 0.7
    gp = grade(portal, compose_variants(portal, 1))[0]
    assert gp.checks["deliverable_to_human"] is False
    assert gp.reward_hack_risk != "low", \
        "an unaddressable application was graded low risk"
    return "capability + deliverability gate the LOW band"


@case("html stripping and requirement extraction produce clean targetable text")
def t_parse():
    raw = ("<div><p>About us</p><ul><li>Experience with MediaPipe and hand tracking</li>"
           "<li>Strong background in real-time video</li></ul>"
           "<p>Email us at jobs&#x40;example.com</p></div>")
    txt = strip_html(raw)
    assert "<" not in txt and "&#x" not in txt, txt
    reqs = extract_requirements(txt)
    assert any("MediaPipe" in r for r in reqs), reqs

    # REGRESSION 2026-08-02: feeds that ship ESCAPED markup. Stripping tags
    # before unescaping entities turned '&lt;li&gt;' into a real '<li>' that
    # survived into a requirement and would have been quoted at a buyer.
    esc = ("&lt;ul&gt;&lt;li&gt;Fluent in Python; experience with C++ is a plus&lt;/li&gt;"
           "&lt;li&gt;Hands-on with modern ML frameworks like PyTorch&lt;/li&gt;&lt;/ul&gt;")
    et = strip_html(esc)
    assert "<" not in et and "&lt;" not in et, et
    ereqs = extract_requirements(et)
    assert ereqs and all("li>" not in r for r in ereqs), ereqs
    return f"{len(reqs)} reqs from raw + {len(ereqs)} from escaped markup, none leaked"


@case("REGRESSION 2026-08-02: a claim may not cite a URL it does not describe")
def t_claim_url_coherence():
    """First live run emitted 'I build webcam input layers ... github.com/TTaoGaming'
    -- hand-piano prose attached to the agent-harness URL. Structurally perfect,
    factually incoherent, and graded 'send as-is'. Must never recur."""
    op = _op()
    op.fit_score = 0.8
    art = compose_variants(op, 1)[0]
    # every emitted variant must be coherent by construction
    g = grade(op, [art])[0]
    assert g.checks["claim_url_coherent"], "generator emitted an incoherent claim/URL pair"
    # and the grader must CATCH one if it is forged
    forged = dataclasses.replace(art, variant_id="t::FORGED",
                                 asset_id="agent_harness")   # body still says 'piano'
    gf = grade(op, [forged])[0]
    assert gf.checks["claim_url_coherent"] is False, "grader is blind to claim/URL mismatch"
    assert gf.reward_hack_risk == "high", gf.reward_hack_risk
    return "generator coherent by construction; grader catches a forged mismatch"


@case("a salaried full-time listing does not get a fixed-price pilot offer")
def t_strategy_suitability():
    from .generate import strategy_plan
    ft = _op(body=("Full-time salaried position with benefits package, 401k, health "
                   "insurance and paid time off. You will build computer vision "
                   "pipelines with MediaPipe. Requirements:\n- 3+ years Python\n") * 3)
    strategies = {s for s, _a, _sc, _r in strategy_plan(ft)}
    assert "PILOT_OFFER" not in strategies, f"pitched a pilot at a salaried role: {strategies}"
    ct = _op(market="M1", body=("Seeking a freelance contractor on a project-based "
                                "statement of work for computer vision and hand tracking "
                                "using MediaPipe. Requirements:\n- Python\n") * 3)
    assert "PILOT_OFFER" in {s for s, _a, _sc, _r in strategy_plan(ct)}
    return "pilot offer dropped for salaried, kept for contract"


@case("variants receive DISTINCT grades so the top-pick is a real ranking")
def t_ranks_differ():
    op = _op(market="M1", body=_op().body + "\nThis is a freelance contract engagement. ")
    op.fit_score = 0.6
    arts = compose_variants(op, 3)
    gs = grade(op, arts)
    totals = {round(g.total, 4) for g in gs}
    assert len(totals) > 1, f"all variants scored identically ({totals}) -- rank is arbitrary"
    return f"{len(arts)} variants, {len(totals)} distinct totals: {sorted(totals)}"


@case("REGRESSION 2026-08-02: never extract an accessibility/legal address as a contact")
def t_contact_blocklist():
    """Assembling the approve list surfaced `accessibleinterviewing@samsara.com`
    and `accommodations@cloudbeds.com` -- ADA accommodation request lines -- being
    offered as the hiring contact for a cold pitch. Sending there is a harm, not
    a near-miss. "" is the correct answer."""
    from .core import find_contact
    for bad in ("Need an accommodation? Email accessibleinterviewing@samsara.com today",
                "Contact accommodations@cloudbeds.com for assistance with this process",
                "Questions to privacy@acme.com or legal@acme.com only",
                "Send to no-reply@acme.com",
                "official mail only comes from addresses ending in @samsara.com",
                "review the job offer at Humana.com when ready",
                "you can apply online at cloudbeds.com instead"):
        got = find_contact(bad)
        assert got == "", f"extracted a blocked address: {got!r} from {bad!r}"
    assert find_contact("Reach me at steven@kanary.com to discuss") == "steven@kanary.com"
    assert find_contact("mail recruiting@starbridge.ai") == "recruiting@starbridge.ai"
    return "4 blocked-purpose addresses refused, 2 real contacts kept"


@case("REGRESSION 2026-08-02: junk company names never reach the target line")
def t_entity_cleaning():
    """QA sweep found 'Stealth', 'Remote', '*Y Combinator', 'NestlÃ©',
    'Adyen ( https://www.adyen.com/ )' printed as `- **target:**`."""
    from .core import clean_entity, clean_title
    assert clean_entity("Stealth") == ""
    assert clean_entity("Remote") == ""
    assert clean_entity("*Y Combinator") == "Y Combinator"
    assert clean_entity("Adyen ( https://www.adyen.com/ )") == "Adyen"
    assert clean_entity("10 Ancestry.com Operations") == "Ancestry.com Operations"
    assert clean_entity("NestlÃ©") == "Nestlé", clean_entity("NestlÃ©")
    assert "&amp;" not in clean_title("Program &amp;amp; Events Coordinator")
    # and a junk entity must make the whole Opportunity fail validation
    try:
        validate_opportunity(_op(entity=clean_entity("Stealth")))
    except RejectedOpportunity:
        return "junk entities cleaned or rejected; mojibake and entities decoded"
    raise AssertionError("an Opportunity with a junk entity was accepted")


@case("REGRESSION 2026-08-02: PILOT_OFFER may only cite the asset its offer describes")
def t_pilot_offer_asset_binding():
    """QA sweep: 58 of 66 PILOT_OFFER variants pitched 'a camera-control layer:
    a working webcam/gesture input layer' and then cited the agent-harness repo
    as proof. OFFER is fixed prose about the camera layer."""
    from .generate import strategy_plan
    llm = _op(market="M1", title="AI Engineer", tags=[],
              body=("Freelance contract for an LLM agent platform. Requirements:\n"
                    "- prompt engineering and langchain experience\n"
                    "- build an evaluation harness\n") * 4)
    for strat, asset, _s, _r in strategy_plan(llm):
        if strat == "PILOT_OFFER":
            raise AssertionError(
                f"offered the camera-layer pilot while citing {asset['id']}")
    cv = _op(market="M1", title="Computer Vision Contractor", tags=[],
             body=("Freelance contract. Requirements:\n- computer vision and "
                   "hand tracking with mediapipe\n- webcam pipelines\n") * 4)
    pilots = [(s, a) for s, a, _sc, _r in strategy_plan(cv) if s == "PILOT_OFFER"]
    assert pilots and pilots[0][1]["id"] == "demo01_handpiano", pilots
    return "pilot offer dropped on an LLM listing, bound to the demo asset on a CV listing"


@case("uid is stable and collision-resistant")
def t_uid():
    a = make_uid("remoteok", "https://x/1", "CV Engineer")
    b = make_uid("remoteok", "https://x/1", "CV Engineer")
    c = make_uid("remoteok", "https://x/2", "CV Engineer")
    assert a == b and a != c
    return "stable across calls, distinct across urls"


@case("the factory module imports no network-write or send capability")
def t_no_send():
    import inspect
    from . import emit, generate, grade as g, run_factory
    banned = ("smtplib", "requests.post", "urlopen(req, data", "slack", "webhook",
              "sendmail", "tweepy", "linkedin_api")
    for mod in (emit, generate, g, run_factory):
        src = inspect.getsource(mod).lower()
        for b in banned:
            assert b.lower() not in src, f"{mod.__name__} references {b}"
    return "no send/post/publish capability present in the factory package"


# --------------------------------------------------------------------------
def run() -> int:
    failed = 0
    print(f"factory selftest — {len(CASES)} held-out cases\n")
    for name, fn in CASES:
        try:
            note = fn()
            print(f"  PASS  {name}\n        -> {note}")
        except Exception as exc:                       # noqa: BLE001
            failed += 1
            print(f"  FAIL  {name}\n        -> {type(exc).__name__}: {exc}")
    print(f"\n{len(CASES) - failed}/{len(CASES)} passed")
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(run())
