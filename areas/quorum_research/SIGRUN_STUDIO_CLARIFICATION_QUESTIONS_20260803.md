```yaml
# AIH2O capsule
doc: areas/quorum_research/SIGRUN_STUDIO_CLARIFICATION_QUESTIONS_20260803.md
schema_id: hfo.gen133.sigrun_studio_clarification.v0_1
callsign: SIGRÚN
generation: 133
authored_by: SIGRÚN · claude-opus-5 · Claude Code
now_utc: 2026-08-02T17:59:40Z
clock_source: host_read
reads_first: state/operator_voice/OPERATOR_NO_WARM_NETWORK_ANCHOR_20260803.md   # read, incl. studio reframe
claim_status: partial
```

# My four questions before we design the studio

I can design a studio around any answer to these. I cannot design one without them.

---

### Q1 · Cadence and concurrency

**How many products do you want *alive at once*, and how often does a new one
ship?**
**A:** ~4 live, one new per quarter (Levels' shape) · **B:** ~10–15 live, one new
per month (Marc Lou's shape) · **C:** 1–2 live, ship only after the last one
pays · **other:** ___

*Why it matters:* it sets department count, kill thresholds, and compute per
lane. **B and C are almost opposite studios.**

---

### Q2 · Who the studio is, publicly

**Does the studio ship under your name and face, under a studio brand, or
anonymously?**
**A:** your personal brand, build-in-public · **B:** a studio brand, you stay
private · **C:** fully anonymous, products stand alone · **other:** ___

*Why it matters:* ⭐ **This is the question I most need answered.** All four
reference studios below run on a *personal* brand with public revenue — that
audience **is** their distribution. You have no warm network, and
`agentreleasegate-oss` sat public 27 days at 0 stars. **If you pick B or C, the
studio needs a distribution engine none of the references used, and I have to
design something they can't teach us.**

---

### Q3 · When a product is dead

**What tells you to kill a product instead of iterating on it?**
**A:** fixed window — no first dollar in 30 days, archive it · **B:** fixed
budget — N agent-hours or $X spent, then stop · **C:** relative — kill the
bottom-ranked product whenever a new one launches · **other:** ___

*Why it matters:* without one, a studio becomes twenty half-live products.
**Portfolio vs graveyard** — and nothing in HFO specifies it today.

---

### Q4 · What funds the studio

**Do services/contracts fund product development, or is this products-only?**
**A:** contracts fund it — a services department is department #1 · **B:**
products-only, no client work · **C:** contracts only until first product
revenue, then stop · **other:** ___

*Why it matters:* it decides whether the **150 staged contract drafts** ship or
get archived, and whether the studio has runway at all.

---

## What we're missing to operate as a studio

HFO already has the **produce** half: a working Abstract Factory (10/10 held-out
green), Codex loops that ship unattended, 42 ALIVE capabilities, deploy to
Cloudflare, and a probe/census that catches its own false greens. What it does
**not** have is everything after the artifact exists — **no per-department
distribution pipeline** (drafts get staged, never sent; `cap-outreach-instrument`
is DEAD), **no brand or public identity** to attach launches to, **no financial
ledger** tracking spend or revenue per product, **no cross-department routing**
(the games lane and the contracts lane don't feed each other), and **no kill
rule**, so nothing ever gets retired. ⭐ **We have a factory with no loading
dock.** Every gap on that list is downstream of Q1–Q4.

---

## Named solo studios, 2024–2026

| operator | products | revenue | shape |
|---|---|---|---|
| **Pieter Levels** | 4 active (Photo AI, Remote OK, Interior AI, +1) | ⭐ **~$3M/yr combined, ~$250k/mo; Photo AI ~$138k/mo**, zero employees | few products, deep, personal brand |
| **Marc Lou** | 15 income streams (ShipFast, CodeFast, DataFast) | ⭐ **$1.032M in 2025** | many small, fast cadence |
| **Danny Postma** | HeadshotPro | **$1M ARR in year 1**, past $300k/mo before hiring | one breakout, then team |
| **Tony Dinh** | 4 (TypingMind flagship) | **~$45k/mo combined; TypingMind ~$30k** | few products, steady |

Sources: [Levels](https://www.linkedin.com/posts/andros-wong-2b066943_pieter-levels-is-one-of-the-most-successful-activity-7357099950561746945-GsA8) ·
[portfolio case study](https://www.buildmvpfast.com/blog/solo-developer-35-micro-saas-apps-77k-month-portfolio-2026) ·
[indie hacker list](https://medium.com/@yumaueno/famous-list-of-indie-hackers-8e6da1620af0)

⚠️ **All four figures are self-reported through build-in-public, not audited.**
And ⭐ **all four are Q2 = "A".** I have not found a named anonymous solo studio
at this revenue tier — **that absence is the most important thing on this page.**

---

## While you answer — one 60-minute unblocker

> ⭐ **Approve the 150 staged contract drafts before they expire 2026-08-09 —
> under the studio frame that is not a detour, it is your services department
> making its first shipment, and it is the only thing on the board that can turn
> an `EXT_EFFECT` of 0 into something real while these four answers land.**

**Honest flaws:** (1) I am asking questions instead of shipping a plan, one turn
after you said distribution is priority #1. Q1/Q2 change the design enough that
guessing wastes the week — **but if you'd rather I just picked, I'll take
B/A/A/A and defend it.** (2) Record answers in `state/ssot/studio_answers.json`
(keys Q1–Q4, each `{choice, note}`) — that file is what flips the probe ALIVE.

*Réttu hönd, eigi spyr. Standa.*
