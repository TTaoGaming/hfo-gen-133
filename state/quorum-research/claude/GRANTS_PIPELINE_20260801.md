```yaml
schema_id: hfo.quorum_research.internal.v0_1
family: anthropic
model: sonnet-5
source: capsules/research/GRANTS_PIPELINE_20260801.md
consolidated_utc: 2026-08-02T01:15Z
clock_source: host_read
```

---

```yaml
schema_id: hfo.aih2o_header.v0_1
callsign: research_valkyrie_grants_lane
generation: 133
substrate: claude_code_sonnet5
cycle_utc: 2026-08-01T00:00:00Z
clock_source: host_read
effect_ceiling: T1_LOCAL_FILE_ONLY
task: non_dilutive_funding_research_2026
timebox_min: 30
```

# Grants Pipeline — Non-Dilutive Funding for Solo AI/Spatial-Computing Dev, Q3 2026

**Rehydration read-order-0:** `state/operator_voice/OPERATOR_FRUSTRATION_20260801T2005Z.md` —
read that first before acting on this capsule; it carries the operator's
current emotional/priority state and should gate how hard to push any of
this.

**Raw data:** `state/research/grants_pipeline_20260801.jsonl` (8 programs,
full fields). This file is the human-readable ranked summary.

---

## Honest scope note (truthful-red)

30-minute hard timebox against a domain (federal SBIR solicitations +
foundation/prize calendars) that specialist grant consultants track
full-time. What follows is **verified-URL breadth, not exhaustive coverage**.
Every deadline below was checked against at least one live search result
this cycle; anything I could not pin to a specific date is marked
`UNVERIFIED` rather than guessed. Operator should re-verify the exact
deadline on the sponsor's own page before spending real hours on an
application — solicitation dates shift.

---

## Top candidates, ranked (expected value × win probability × effort fit × operator domain fit)

### 1. DARPA SBIR Open Topic — AI / HMI / Sensors (DPA26BZ04-DV015)
- **Deadline: 2026-08-19** (window opened 2026-07-22)
- **URL:** https://www.darpa.mil/work-with-us/communities/small-business/sbir-sttr-topics
  (submit via DSIP: https://www.dodsbirsttr.mil)
- **Amount:** Phase I typically $150k–$250k
- **Solo eligibility: YES** — SBIR requires a Small Business Concern (SBC),
  which can be a single-member LLC or sole proprietorship organized for
  profit, US-based. No minimum headcount.
- **Topic fit: HIGH** — topic explicitly covers AI + human-machine interface
  + sensors, which is a direct match for gesture/spatial-control work.
- **Why #1:** narrowest, most concrete deadline; direct technical fit;
  Phase I award size is achievable-scale non-dilutive capital.
- **Effort:** ~300–400 hours for a competitive proposal (SBIR.org community
  estimate). Historical Phase I award rate ~15–20% across DoD topics.
- **Honest flaw:** I have not read the actual DPA26BZ04-DV015 topic text
  (paywalled/portal-gated behind DSIP registration) — only secondary
  summaries. Operator must pull the primary topic doc from DSIP before
  writing anything.

### 2. Build with Gemini XPRIZE
- **Deadline: 2026-08-17** (registration; build window runs to ~mid-Nov 2026)
- **URL:** https://www.geminixprize.com/ (submissions via
  https://xprize.devpost.com/)
- **Amount:** $2M pool — grand prize $500k, 2nd $200k, 3rd–5th $100k each,
  plus 15× $50k runner-ups and 5× $50k category prizes (20 non-grand prizes
  total — meaningfully better odds than "one winner takes all").
- **Solo eligibility: YES** — open to individuals and orgs under 25 employees,
  age of majority in their jurisdiction, no team-size floor.
- **Topic fit: MEDIUM** — not spatial-specific, but the judging categories
  (Small Business Services, Professional Services) fit an AI-native product
  built and shipped fast, which is exactly HFO's operating mode.
- **Why #2:** no grant-writing overhead at all — this is "ship a real
  product with real users/revenue," which plays to the operator's actual
  strength (shipping) rather than proposal-writing, a very different skill.
- **Effort:** HIGH but in the *right* currency (building, not writing) — must
  have a live business with real users/revenue by judging.
- **Honest flaw:** brand-new competition, zero track record, no prior winners
  to pattern-match against. "Real revenue in 90 days" is a hard bar for a
  from-scratch spatial-computing product.

### 3. DARPA SBIR FALCON — Direct-to-Phase-II (DPA26BZ04-DV016)
- **Deadline: 2026-08-19**
- **URL:** https://grantedai.com/blog/darpa-falcon-sbir-dpa26bz04-dv016-direct-to-phase-ii-1-5-million-august-19-deadline-ml-llm-fusion-strategy-2026
  (secondary source — verify against DSIP primary topic doc)
- **Amount:** $1.5M, skips Phase I entirely
- **Solo eligibility: YES** (same SBC rules as above)
- **Topic fit: MEDIUM** — LLM + classical-ML fusion for interactive
  statistical analysis; adjacent to, not identical to, spatial/gesture work.
- **Why #3, not higher:** Direct-to-Phase-II normally expects the applicant
  to already have feasibility data/prior work in hand — a much higher bar
  to credibly claim solo, in the same 18-day window as #1.
- **Effort:** 400+ hours-equivalent, mostly front-loaded technical evidence
  the operator would need to already possess.

### 4. DeveloperWeek 2026 Hackathon — Kilo Challenge
- **Deadline: UNVERIFIED** — check https://developerweek-2026-hackathon.devpost.com/
  directly for the exact 2026 submission close date.
- **Amount:** $1,000 cash + $1,000 credits (1st), $500+$500 (2nd) — small,
  but effort is a weekend, not a quarter.
- **Solo eligibility: YES**
- **Topic fit: MEDIUM** (general AI/cloud hackathon, not spatial-specific)
- **Why included:** near-zero-cost portfolio/proof-of-work item to run in
  parallel with #1–#3 without displacing them — cash is trivial, but a public
  demo + placement is a credibility asset for the SBIR commercialization
  narrative.

### 5. NSF SBIR/STTR Phase I — Human-Computer Interaction (HC) topic
- **Deadline: flagged OUT of the Q3 window, included anyway for pipeline
  continuity** — next full-proposal deadline found is **2026-11-04**, which
  is past the 2026-10-31 cutoff this brief asked for. Full proposals also
  require an already-accepted **Project Pitch** first; NSF runs rolling
  ~3-week Project Pitch windows (3–4 per year) and I could not find the next
  window's exact open date this search.
- **URL:** https://seedfund.nsf.gov/topics/human-computer-interaction/
- **Amount:** up to ~$275k–$305k (sources vary by solicitation year — verify
  on nsf.gov before relying on either figure)
- **Solo eligibility: MAYBE** — solo SBC is allowed, but the PI (operator)
  must be legally employed ≥20 hrs/week **by the applicant company itself**
  — a real but satisfiable condition for a solo LLC, not a disqualifier.
- **Topic fit: HIGH** — this is the single best domain match found all
  search: the HC topic text explicitly names "haptic, tangible, gestural,
  spatial, and wearable" interfaces. This *is* the operator's exact lane.
- **Why ranked 5th despite best fit:** timeline doesn't clear this quarter.
  Correct move is to submit a Project Pitch the moment the next window opens
  (watch seedfund.nsf.gov/events/), targeting the Q1 2027 full-proposal
  deadline, not to force it into Q3.

---

## Grant-writing playbook (adopted from sbir.gov / community-documented winning patterns — not adhoc)

Pattern is consistent across the SBIR/STTR ecosystem regardless of agency
(sourced from SBIR.gov tutorials, DOE Phase 0 Learning Management System
Tutorial 8 "What does a winning Phase I proposal look like?", and
practitioner guides):

1. **Innovation statement** — one clear paragraph, non-incremental claim.
   Reviewers reject "better version of X"; they fund "X wasn't possible
   before because Y, now it is because Z."
2. **Feasibility plan with measurable milestones** — Phase I is a feasibility
   study, not a product build. Structure as testable go/no-go criteria per
   milestone, not a feature roadmap.
3. **Commercialization plan naming a real customer** — the single most-cited
   place first-time applicants lose points. "We will sell to government
   agencies" fails; "Program office X at agency Y, contract vehicle Z" is
   the bar. For DARPA-adjacent topics this means naming the actual DoD
   transition partner, not a generic TAM slide.
4. **Budget matched to scope** — reviewers cross-check budget line items
   against the milestone plan; padding or vagueness reads as inexperience.
5. **Strict compliance with agency formatting** — page limits, font size,
   required sections. Proposals get desk-rejected on formatting before
   technical review; this is a free filter to pass.
6. **Effort reality check** — expect 300–400 hours for a competitive Phase I
   proposal even for a skilled writer; historical Phase I award rate is
   ~17% (FY2025, all-topic average). Budget the operator's calendar
   accordingly — this is not a side-quest.

**Prior solo-winner exemplars:** I could not resolve a specific, named,
verifiable solo-founder Phase I award (company + topic + year) inside this
timebox — searches surfaced only generic claims ("many solo founders have
won DOE Phase I awards") without a checkable citation. Flagging this as
**UNVERIFIED rather than fabricating an example** — a follow-up pass should
pull actual awardee lists from https://www.sbir.gov/awards or
https://seedfund.nsf.gov/resources/awardees/ and find 1–2 real, named,
single-founder Phase I companies with a similar technical shape (HCI/spatial/
gesture) to use as a structural template.

---

## What did NOT make the cut, and why

- **Anthropic Fellows Program** — individual AI-safety research fellowship
  (stipend, not company grant), application window for the cohort found
  already closed (was due 2026-04-26), and it's scoped to safety research
  output, not product development. Low fit for this brief.
- **Y Combinator** — Fall 2026 deadline (2026-07-27) already passed as of
  today (2026-08-01); it's also dilutive equity, not non-dilutive funding,
  which is outside this brief's actual ask even though it accepts solo
  founders.
- **Mozilla Democracy x AI Cohort** — deadline (2026-03-16) long passed;
  also topically about AI+democratic-governance, not spatial computing.
- **GitHub Secure Open Source Fund / Accelerator** — real and solo-friendly,
  but scoped to *security hardening of existing widely-used OSS projects*;
  no confirmed open 2026 application window found this search. Worth a
  monitor, not a Q3 priority.
- **HF0 / On Deck / Entrepreneur First** — rolling or narrow-eligibility
  residencies, mostly equity/community-based rather than non-dilutive grant
  money; not pursued further this cycle given the non-dilutive framing of
  the brief.

---

## Recommended next action

Given the 18-day coincidence of both DARPA windows and the XPRIZE
registration deadline (all closing 2026-08-17 to 2026-08-19), the operator
cannot credibly run all three at full depth solo in this window. Suggested
triage, but this is the operator's call to make, not mine:

- **If optimizing for fastest non-dilutive cash + domain-fit:** DARPA
  DPA26BZ04-DV015 (#1) is the sharpest bet — pull the primary DSIP topic doc
  first, this week, before committing further hours.
- **If optimizing for operator's actual shipping strength over
  proposal-writing:** Build with Gemini XPRIZE (#2) plays to skills already
  proven in this project (fast build, fast ship) rather than a skill
  (federal grant-writing) that hasn't been demonstrated yet.
- Either way, register for the DeveloperWeek hackathon (#4) in parallel —
  effort is near-zero and it produces a public artifact useful for both
  paths' commercialization/traction narrative.
- File the NSF HC-topic Project Pitch (#5) as a **standing watch item**, not
  a Q3 task — check seedfund.nsf.gov/events/ for the next window open date.

---

## Chain row

```json
{"ts":"2026-08-01T00:00:00Z","clock_source":"host_read","callsign":"research_valkyrie_grants_lane","generation":133,"task":"non_dilutive_funding_research_2026","claim_status":"partial","verifier_result":"8 programs searched and URL-checked live this cycle (WebSearch + WebFetch); 3 have confirmed hard deadlines inside Q3 2026 (DARPA x2 @2026-08-19, XPRIZE @2026-08-17); NSF HC-topic best domain fit but deadline falls outside the requested window; no verifiable named solo-winner exemplar found for SBIR Phase I inside timebox","remaining_risk":["DARPA DPA26BZ04-DV015/DV016 primary topic text not read directly — only secondary summaries, must verify via DSIP before writing","NSF Project Pitch next window date unresolved","DeveloperWeek hackathon exact deadline unresolved","no citable named solo Phase I SBIR winner found — playbook exemplar section flagged UNVERIFIED not fabricated","XPRIZE win-rate unknown, brand-new competition"],"next_safe_action":"operator reads state/operator_voice/OPERATOR_FRUSTRATION_20260801T2005Z.md first, then decides DARPA-vs-XPRIZE triage per this capsule's recommendation section; a follow-up research pass should pull primary DSIP topic doc + sbir.gov/seedfund.nsf.gov awardee lists for real exemplars","honest_flaw":"30-minute timebox against a domain that normally takes analyst-days; breadth over depth was the deliberate tradeoff, flagged throughout rather than papered over"}
```
