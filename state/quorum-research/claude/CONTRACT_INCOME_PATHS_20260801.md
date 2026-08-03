```yaml
schema_id: hfo.quorum_research.internal.v0_1
family: anthropic
model: sonnet-5
source: capsules/research/CONTRACT_INCOME_PATHS_20260801.md
consolidated_utc: 2026-08-02T01:15Z
clock_source: host_read
```

---

```yaml
# AIH2O capsule
doc: capsules/research/CONTRACT_INCOME_PATHS_20260801.md
schema_id: hfo.gen133.capsule.research.contract_income.v0_1
generation: 133
authored_by: research-valkyrie · claude-sonnet-5 · Claude Code
valid_time_utc:       2026-08-01T00:00:00Z
transaction_time_utc: 2026-08-01T00:00:00Z
claim_status: partial   # real market data via WebSearch; NOT operator-verified by application
timebox: 30min hard cap
data: state/research/contract_income_platforms_20260801.jsonl
```

# Contract Income Paths — 2026 fast-path research

**Rehydration read-order-0:** `memory/operator-recurring-context.md` — operator is at
capacity limit, overwhelmed, "only a few demos," has sent no emails/offers. He wants
faster income than app-building, and his recurring job should be limited to *taste*
(pick a thing, react to a result) — not more architecture. This deliverable is written
to be actionable in under 30 minutes of his attention, not a menu to research further.

---

## The ONE fastest path

**Reactivate the existing Upwork account today, this week.** Not a new platform.

Reasoning: every gated marketplace (Toptal, Arc, Turing) charges *unpaid vetting time*
— weeks before first dollar, 2-5% acceptance. Every open marketplace with real client
volume (Upwork) charges *zero* entry cost beyond writing a proposal. The operator
already cleared Upwork's trust bar once ($2k, 1 client) — reactivation is a support
flow (log in with prior credentials/SSO, follow the reactivation email), not a
re-vetting. This is the only lane in the dataset where "days" is a realistic
time-to-first-dollar for a solo operator starting *this week*, not "weeks to months."

Everything else researched here (Toptal, Braintrust, Arc, Turing, Bugcrowd, Prolific,
GLG/AlphaSights) is real, but every one of them trades speed for something else —
higher rate ceiling, lower fee, or a differentiated niche — at the cost of a slower or
less certain first payout. Given the operator's stated capacity limit, speed dominates.

---

## Top 5 platforms to apply to THIS WEEK, ranked

Ranked by (time-to-first-dollar × probability × operator fit):

1. **Upwork (reactivate)** — days, existing trust, zero new vetting. Portfolio need:
   2-3 line profile update pointing at `demo01-handpiano.pages.dev` (already live,
   HTTP 200) as proof-of-work; no new build required.
2. **Contra** — 0% commission, open signup, days-to-weeks. Portfolio need: same
   demo01 link + a one-paragraph "what I build" blurb. Weaker on inbound discovery,
   strong as a zero-cost second listing running in parallel with Upwork.
3. **Braintrust** — 1-3 weeks, engineer keeps ~90-95% of billed rate (best take-home
   split of any marketplace researched). Portfolio need: application + short interview;
   demo01 + a one-line description of the agent-release-gate work as differentiation.
4. **Arc.dev** — 2-4 weeks, mid-tier rates, real screening. Apply in parallel with #1-3
   since it costs only time, not money, and does not block other applications.
5. **GLG / AlphaSights (expert network)** — UNVERIFIED this pass (see gotcha in the
   JSONL row) but flagged because the operator's actual specialty — agent release
   gates, policy-as-code, held-out/mutation testing for AI agent safety — is a genuine
   2026 expert-call topic these networks pay for. **Do not apply blind**: needs one
   direct 10-minute look at glginsights.com / alphasights.com's own expert-application
   pages before treating this as actionable. Flagged, not confirmed.

**Deliberately excluded from the top 5:** Toptal (3% acceptance, weeks of unpaid
vetting — wrong shape for "faster than app-building"); Turing/Andela (rates skew
$30-100/hr, below what a senior US-based AI engineer commands, and Andela in
particular is built for full-time placement, not short contracts); Prolific and
Bugcrowd (real money exists but the income ceiling — $19-20/hr eval piecework, or
winner-take-most bounty payouts — is a bridge-cash lane, not a real income
replacement for someone with the operator's skill level).

---

## Portfolio requirements per platform

- **Every platform above** wants the same core artifact: a **live, working URL** —
  the operator already has this in `demo01-handpiano.pages.dev` (verified HTTP 200,
  315,930 B per [[hfo-what-actually-works]]). Do not build a new portfolio site;
  point profiles at what already ships.
- **Upwork/Contra:** profile blurb + 1 portfolio link is sufficient to start applying.
  No certification, no test project.
- **Braintrust/Arc:** short async interview or screening call in addition to the link.
- **Toptal (if ever revisited):** timed technical test + live problem-solving —
  explicitly out of scope for "this week."
- **GLG/AlphaSights (if the follow-up look confirms viability):** likely a profile +
  short bio emphasizing the agent-release-gate / AI-safety-verification specialty,
  not a code portfolio at all — expert networks sell judgment on calls, not delivered
  code.

---

## Rate benchmarks — solo AI engineer, 2026, spatial/vision/agent work

| Tier | Hourly (USD) | Where seen |
|---|---|---|
| Junior AI/ML (0-2yr) | $50-80 | market-wide 2026 aggregate |
| Mid AI/ML (2-5yr) | $80-130 | market-wide 2026 aggregate |
| Senior AI/ML, general | $100-250 | Toptal/Gun.io premium band (client-billed; freelancer nets ~half on Toptal specifically) |
| Upwork AI/ML median | ~$100 | Upwork's own 2026 resource page |
| AR/VR/spatial, US-based senior | $150-250, up to $275-450 for rare skill combos (Unity/Unreal + ARKit/ARCore + hand-tracking) | multiple 2026 hiring-cost aggregators |
| AR/VR, Eastern Europe | $80-120 | same |

**Read for the operator:** his spatial/hand-tracking demo work (demo01-handpiano)
sits in the *rare-skill* AR/VR band ($150-450/hr territory) if positioned as spatial
computing + gesture/hand-tracking specialization, not generic "AI engineer" ($75-150).
Specificity is worth real money here — lead with hand-tracking/spatial, not "AI."

---

## Chain row

```json
{"schema_id":"hfo.gen133.chain.research.v0_1","doc":"capsules/research/CONTRACT_INCOME_PATHS_20260801.md","authored_by":"research-valkyrie · claude-sonnet-5","valid_time_utc":"2026-08-01T00:00:00Z","claim_status":"partial","verifier_result":"WebSearch queries (8) returned live 2026 rate/platform data cross-checked across 2-3 sources per claim; JSONL row-per-platform written to state/research/contract_income_platforms_20260801.jsonl; operator memory files read for fit-context (demo01-handpiano live URL, agentreleasegate specialty)","remaining_risk":["GLG/AlphaSights onboarding/pay UNVERIFIED — flagged not confirmed","Gun.io process/timeline UNKNOWN — rate band is directional only","no application was actually submitted this session — this is research, not action","rate figures are aggregator-reported, not first-party platform-confirmed"],"next_safe_action":"operator (or a narrow-brief executor) reactivates Upwork account and updates profile to lead with demo01-handpiano + spatial/hand-tracking specialization; separately, a 10-min follow-up pass checks glginsights.com/alphasights.com expert-application pages directly before acting on the GLG/AlphaSights row","honest_flaw":"this is a document, not an effect — per [[hfo-what-actually-works]] measured 2026-08-01, coordination/research documents produce 0 external effects on their own; the only thing that moves the needle is the operator (or an executor) actually submitting the Upwork reactivation and first proposal"}
```
