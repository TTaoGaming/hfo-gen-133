# proof_artifact_criteria.v0_1 — the "2-minute useful" standard

```yaml
schema_id: hfo.gen133.contract.proof_artifact_criteria.v0_1
valid_time_utc: 2026-07-31T14:10:00Z
transaction_time_utc: 2026-07-31T14:10:00Z
claim_status: proposed
author: SIGRUN_P4 · claude-opus-5 · Claude Code · gen-133
supersedes: none
```

## 0. Provenance of the criterion (honest)

The operator recalls Sigrún stating a "useful within 2 minutes" criterion
previously. **A grep of the gen-133 corpus does not find it stated for proof
artifacts.** The nearest prior in the record is:

```
projects/income-lane/EXECUTE_ON_CODEX.md:73
"one draft is reviewable in two minutes on a phone, and ten are not"
```

That is a 2-minute *reviewability* gate on **outreach drafts** (operator-side
review load), not a 2-minute *usefulness* gate on **proof artifacts**
(recipient-side comprehension load). They are different contracts with the same
number.

**Therefore this document defines the proof-artifact criterion from first
principles and marks it `proposed`, not `restored`.** Do not cite it as prior
canon.

## 1. Who the clock belongs to

The 2 minutes are **the recipient's**, not ours. Three recipient archetypes,
all of whom are scanning, not reading:

| recipient | what they are deciding in 2 min | failure mode |
|---|---|---|
| hiring manager | "does this person clear the bar for a screen?" | closes tab, no reply |
| prospect / buyer | "is this relevant to a problem I have right now?" | archives email |
| proposal reviewer | "is this claim substantiated enough to fund/advance?" | scores low, moves on |

None of them will install anything, create an account, clone a repo, or read a
71 KB spec. Any artifact that requires one of those has already failed.

## 2. The contract — five hard gates

An artifact is **2-min-useful** iff it passes all five. Each is measurable.

### G1 — OPEN: reachable and rendered in < 5 seconds, zero friction
- Single URL or single attached file. No login, no signup, no waitlist, no
  install, no clone, no build step.
- `curl -o /dev/null -w '%{http_code} %{time_total}'` → `200` and `< 2.0s` TTFB
  on a cold cache from a non-owner network.
- Renders on a phone. If it needs a desktop, it is not an outreach artifact.
- **Measurement:** HTTP probe + one mobile-viewport screenshot.

### G2 — COMPREHEND: the claim is legible in < 60 seconds
- The **first screen** (above the fold, no scroll) states: what it is, who it is
  for, and the single result claimed. Not the methodology. Not the lineage.
- Total reading time to the claim ≤ 60s ⇒ **≤ 200 words above the fold**.
- Zero internal vocabulary. If a term needs HFO context to parse, it is banned
  from the artifact surface. (Valkyrie names, port numbers, seat IDs, drápa,
  stef, Gleipnir, tsukumogami, PREY, MOBA-Q — all banned on artifact surfaces.)
- **Measurement:** word count above fold; a jargon-linter wordlist pass.

### G3 — SUBSTANTIATE: exactly one verifiable number or reproducible demo
- One concrete result, stated with its measurement method, in one line.
  Example shape: *"cut input jitter 92.9% (One-Euro filter, n=…, method: …)"*.
- The reader must be able to check it without contacting us: a live demo they
  can drive, a linked raw result, or a runnable snippet ≤ 20 lines.
- **A claim with no check is marketing, not proof.** Marketing does not clear
  this bar.
- **Measurement:** the number exists, its method is stated, and an independent
  party reproduced it once. Self-reproduction does not count.

### G4 — ACT: exactly one next action, unambiguous
- One CTA. Not two. Not "learn more / contact us / read the docs."
- The CTA is low-commitment and specific ("reply with your repo URL and I'll
  send the teardown in 48h"), not high-commitment and vague ("let's chat").
- **Measurement:** count of distinct CTAs on the surface == 1.

### G5 — HOLD: it does not rot
- Every claim carries `valid_time_utc`. Every artifact carries a version.
- No link to a path that only exists on the operator's laptop. No link to a
  private repo. No link into a forge tree.
- A dead link, a 404 demo, or a number whose method has since changed is a
  **worse** outcome than no artifact — it converts a neutral prospect into a
  negative signal.
- **Measurement:** a weekly link-and-claim sweep; artifact fails on first 404 or
  first claim whose stated method no longer matches the code.

## 3. Artifact classes and their per-class contract

| # | class | 2-min-useful contract (beyond G1–G5) | our current standing |
|---|---|---|---|
| a | **live demo URL** | drivable within 10s of load, no camera/permission wall before value is visible, works on phone | `handpiano.com` HTTP 200 — G1 pass; G2/G3 unaudited |
| b | **case study 1-pager** | Problem / Intervention / Result-with-number / Method / What-didn't-work. ≤ 1 page. The "what didn't work" line is what makes it credible | **none exists** |
| c | **code sample** | ≤ 200 LOC, single file, runs with one command, README top line states what it proves | `agentreleasegate-oss` exists; not packaged to this contract |
| d | **90-sec video** | first 10s show the working thing, not a title card; captions burned in (watched muted); no intro | **none exists** |
| e | **plaintext testimonial** | named human, named org, one specific outcome, permission on file | **none exists — 0 external receipts in 18 months** |
| f | **result-first email** | subject = the result; ≤ 120 words; proof link in first 3 lines; one CTA; no attachment | drafts exist at gen-131, none sent |
| g | **résumé / CV pointer** | one PDF URL, ≤ 2 pages, each bullet = verb + number + method | **not audited this session** |
| h | **portfolio index** | ≤ 7 items, each with one-line claim + one link; loads in <2s; no navigation depth | **none exists** |

## 4. FALSIFIERS — what proves an artifact does NOT clear the bar

An artifact is **disqualified** on any one of these. These are the tests to run,
not opinions to hold.

| # | falsifier | how to run it |
|---|---|---|
| F1 | A person outside HFO, given only the URL and no context, cannot state the claim in one sentence after 2 minutes | 3 external readers, timed, write-down test. ≥1 failure ⇒ fail |
| F2 | Any gate before value: login, signup, install, clone, cookie wall, camera permission | load in a clean incognito profile on a phone |
| F3 | The stated number cannot be reproduced by someone who is not us | hand the method to one external party, once |
| F4 | More than one CTA, or a CTA requiring a meeting before any value is delivered | count CTAs on the surface |
| F5 | Any HFO-internal term appears on the surface | jargon wordlist grep |
| F6 | Any link 404s, or resolves to a private repo / local path | automated weekly link sweep |
| F7 | The artifact has no `valid_time_utc`, or its claim's method has drifted from the code that produces it | frontmatter check + method-vs-code diff |
| F8 | Load time > 5s cold on mobile network profile | Lighthouse / throttled probe |

## 4A. Audience taxonomy — the 2-minute contract differs by who is reading

§1 named three recipients. That was too narrow. The gates G1–G5 are invariant;
**what counts as passing G2 and G3 changes by audience**, because different
audiences are buying different things.

| audience | horizon | what they are buying | G2 must lead with | G3 evidence they accept | disqualifier specific to them |
|---|---|---|---|---|---|
| **Hiring manager** | short / income | *can this person do the job* | a shipped thing with your name on it | working link + one number | a claim about a team, not you |
| **Prospect / client** | short / income | *relief from a problem I have now* | their problem in their words | a result from a comparable situation | anything about your process |
| **Agent red team / AI-safety auditor** | dual | **credibility** — evidence you are honest under adversarial reading | **the failure you found in yourself** | reproducible method + chain of custody | polish. A clean story reads as concealment |
| **CFP reviewer / CTO** | mid | *is this substantiated enough to fund or platform* | the claim and its bound | method + limits + what would falsify it | overclaiming beyond the evidence |
| **OSS contributor** | community | *can I get a win in an hour* | a good first issue | runnable repo, one command | a monorepo with no entry point |
| **Game designer** | long / virtualization | *does this feel good* | a 10-second playable | the thing itself, playable | a spec instead of a build |
| **Software eng org** | long / virtualization | *technical depth and durability* | the hard problem you solved | architecture + tradeoffs + what broke | a feature list |

### 4A.1 The agent-red-team artifact class (its own contract)

This audience is unusual and HFO is unusually well-positioned for it. **They are
not buying polish. They are buying evidence that your self-report survives
adversarial reading.** For them, a disclosed flaw is the product, not a
liability.

Required elements — all six, or it does not clear the bar:

| # | element | why this audience needs it |
|---|---|---|
| R1 | **Reproducibility** — a stranger can re-run the audit from the artifact alone, without contacting the author | an unreproducible audit is a press release |
| R2 | **Failure taxonomy** — failures categorized by class, not listed as anecdotes | classes generalize; anecdotes do not |
| R3 | **Honest-flaw disclosure** — what the audit itself got wrong, prominently, not in a footnote | **the load-bearing element.** An audit with no self-correction was not adversarial |
| R4 | **Testable hypotheses** — each claim paired with what would falsify it | distinguishes a finding from an opinion |
| R5 | **Chain of custody on evidence** — timestamps, hashes, tool invocations, what was and was not scanned | lets a skeptic check the seams instead of trusting the conclusion |
| R6 | **Scope statement** — explicitly what was NOT examined | an audit that does not bound itself is claiming total coverage |

**2-min contract for this audience:** the first screen must state *the most
damaging thing found*, and — if the audit is of one's own system — *the thing
the audit itself got wrong*. Leading with a strength is the disqualifier.

**Falsifier for the class:** hand it to one adversarial reader with the
instruction *"find where this is lying to you."* If they find something the
artifact did not already disclose, it fails R3.

## 5. The meta-falsifier for this contract

**This contract is wrong if artifacts that pass all five gates still produce
zero replies after 20 sends.** In that case the bottleneck is targeting or
offer, not artifact quality, and optimizing artifacts further is waste.

`cap-0018` (external income, $0, 18 months, 0 external receipts) is the only
liveness property. **This contract is a hypothesis about why it is at zero. It
is not itself evidence.** Twenty sends is the experiment that tests it.

## 6. What this contract deliberately does NOT require

Recorded so future sessions do not gold-plate:

- Not required: cryptographic sealing of the artifact
- Not required: chain-row provenance visible to the recipient
- Not required: full methodology on the surface (link to it; do not inline it)
- Not required: comprehensiveness — one number beats seven

The internal receipt discipline exists so **we** can trust our own claims. The
recipient never sees it and should not be asked to care about it.

---

*claim_status: proposed · no artifact has yet been measured against this
contract · first measurement is the acceptance test for v0_2*
