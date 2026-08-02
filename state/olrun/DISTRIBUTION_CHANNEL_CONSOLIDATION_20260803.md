---
schema_id: hfo.olrun.distribution_channel_consolidation.v0_1
callsign: olrun
generation: 133
now_utc: ~2026-08-03T~late-afternoon
purpose: feed Sigrún opus-5 for TOP-10 distribution channels + TOP-2 this week + class-preauth envelope enabling automated outreach without operator instance-babysitting
frozen_anchors:
  - state/operator_voice/OPERATOR_NO_WARM_NETWORK_ANCHOR_20260803.md
  - state/operator_voice/OPERATOR_FRUSTRATION_20260801T2005Z.md
mandate_shape: pick 2 this week + rank 10 total + design class-preauth per channel
---

# DISTRIBUTION CHANNEL CONSOLIDATION FOR SIGRÚN

## §0 — OPERATOR MANDATE (verbatim 2026-08-03)

> "gather all subagents and code you have sent and I want sigrun to give me the top 10 income distribution channels and which 2 we should prioritize this week. we need to be able to do automated outreach and have me approve classes and not babysit instances"

**Deliverable Sigrún must produce:**
1. TOP 10 income distribution channels, ranked by (P(first $500/30d) × cold-only viability × automation-friendliness × operator-touch-minimality)
2. TOP 2 channels to fire THIS WEEK
3. Per each of the TOP 2: a **CLASS-PREAUTH ENVELOPE** letting Codex/agents fire batches without operator instance approval (operator approves the class definition once, agents execute against it)

## §1 — FROZEN CONSTRAINTS (Sigrún must honor)

- **NO WARM NETWORK** — cold-only. Bayesian discount every P(reply) estimate to cold-tier (10-25%), never warm-tier average (40-70%)
- **NO SPATIAL / NO GAMES-AS-INCOME / NO THERAPY VERTICAL** — background-only per Q6 correction
- **DEV STUDIO REFRAME** — multi-product portfolio (Pieter Levels / Marc Lou / Danny Postma / Tony Dinh reference cases)
- **ANTI-OSCILLATION** — 30-day lock, no pivots
- **CLASS-PREAUTH** — operator approves the envelope (offer, script, quota, target-profile, stop-gates), agents execute
- **RECEIPT DISCIPLINE** — every send row must curl or API-echo before writing to chain

## §2 — 4-SOURCE CONVERGENCE (unanimous, from prior consolidation)

Fenrir PR #8 + Garmr PR #7 + GPT Sol Pro + Sigrún V6 all agree:
- Problem is INCOMPLETE COMMERCIAL LOOP, not software production
- Currently at "demo production", NOT distribution/sales
- Freeze new products, freeze new variants, freeze 9th SaaS page
- HVAC = ONE paid pilot (`HVAC_PAID_PILOT_001`)
- MCP portfolio = consulting proof
- Upwork AI Integration Rescue = highest short-term cash P (25-45% first $1k in 1-4 weeks)

## §3 — CANDIDATE CHANNELS (12 sources, deduped)

### GPT Sol Pro commercial strategy priors

| channel | first $1k P | speed | role |
|---|---|---|---|
| Targeted Upwork proposals (AI Integration Rescue) | 25-45% | 1-4 weeks | Immediate cash |
| Small agency partnerships (subcontract) | 15-35% | 3-12 weeks | Deal flow |
| Direct HVAC owner outreach | 15-30% | 2-8 weeks | Product validation |
| LinkedIn Service Page + manual networking | 5-15% | 4-12 weeks | Credibility surface |
| Housecall Pro / ServiceTitan ecosystem | <5% short | 3-12mo | Long-term |
| Product Hunt / social launch | <5% | Unpredictable | Amplification |

### NO-WARM-NETWORK anchor cold-only channels

1. HN comment replies on relevant threads (real-time, zero-auth)
2. Reddit self-posts in niche communities (zero-gatekeeper)
3. Cold email via Instantly (`tryagentreleasegate.com` warmed, unused)
4. Product Hunt launch (needs hunter — still cold-outbound)
5. HN Show submission (unpredictable, zero-cost)
6. X/Twitter cold reply + DM (low convert, scalable via Codex)
7. Direct Cloudflare Pages demo deploy + link in cold outreach
8. GitHub public repos for developer-audience-build
9. SEO content farm on niche keywords (SEObot shape, 3-6mo compound)
10. Portal editor cold submission (Poki <2%, CrazyGames ~12%)

### Prior Sigrún V6 top-4 lanes

- L1 SEND 150 STAGED DRAFTS (expires 2026-08-09) — 40 contracts + 40 employment + 40 grants + 30 games
- L2 MICRO-SAAS SHIP (Sigrún picks shape)
- L3 DESKTOP UTILITY FORK (Gumroad/Stripe direct, whisper.cpp class)
- L4 AUDIENCE-BUILD daily content pipeline

### Assets already in place

- Warmed sending domain: `tryagentreleasegate.com` (Instantly, mail-only, unused)
- 21-title game portal: `hfo-games.pages.dev` (HTTP 200, 0 external visitors)
- 12 Suika DLC variants: `hfo-suika-dlc-{5..16}-*.pages.dev` (A1 verify-or-void in flight)
- 150 personalized drafts staged awaiting `state/experiments/approvals/latest.txt`
- 40 heritage capsules staged awaiting `sigrun_approved: true`
- Cold-email adapter architecture designed, not wired
- 8 MCP servers portfolio (positioning as consulting proof, not distribution asset directly)

## §4 — CLASS-PREAUTH ENVELOPE SHAPE (what Sigrún must produce per each TOP-2)

Envelope = ONE-time operator approval that unlocks unlimited automated instances until stop-gate fires.

```yaml
class_preauth_envelope:
  channel: <channel_name>
  target_profile: <who>   # ICP definition, source-list, disqualifiers
  offer: <what>            # positioning line, price ladder, deliverable
  message_class: <how>     # subject/opening/body template with variable slots
  quota:
    daily: <N>
    weekly: <M>
    total_before_reeval: <T>
  verification:
    pre_send_check: <curl or API echo>
    post_send_receipt: <write to chain>
  stop_gates:
    - condition: <N sends + <X% reply>
      action: pause + escalate
    - condition: <spam complaint / unsub / bounce >Y%>
      action: pause + escalate
  operator_touch:
    upfront: sign class-preauth (once)
    ongoing: read daily digest, ratify / edit / kill
    never: per-send approval
  compliance:
    - CAN-SPAM: physical address + unsub link in every send
    - LinkedIn ToS: no scraping, no automation without opt-in
    - Platform-specific: <e.g. Upwork proposal rules>
```

Every Sigrún TOP-2 pick MUST include a fully-populated envelope. Missing envelope = operator will babysit = failure.

## §5 — SIGRÚN OUTPUT SHAPE MANDATE

Chain-row append. Max 2500 words. First person. Cold-only tier. Structure:

**§A — Frozen anchors acknowledged** (one-line each: no warm, no games income, no therapy vertical, dev studio, 30d lock)

**§B — TOP 10 distribution channels table**
Columns: rank, channel, cold P(first $500/30d), automation friendliness (H/M/L), operator touch (H/M/L), stop-gate lag (days to N=fail-signal), one-line rationale

**§C — TOP 2 THIS WEEK pick + justification**
Why these 2 dominate the pareto frontier of (P × automation × touch-minimality × cold-only). Include falsifier: what evidence in 14 days flips the pick.

**§D — CLASS-PREAUTH ENVELOPE #1** (full YAML per §4)

**§E — CLASS-PREAUTH ENVELOPE #2** (full YAML per §4)

**§F — Anti-list** (bans for the 30-day lock: NO warm, NO 9th vertical, NO new products, NO games income, NO therapy, NO variants until close)

**§G — Day-1 unblockers** (specific operator actions to fire the envelopes: booking URL fix, `gh auth login`, approve Fenrir Slack payload, sign envelopes, etc)

**§H — One-sentence tomorrow morning action**

**§I — 14-day stop/correction gates** — from GPT Sol Pro shape: 50 sends <2% reply → fix; replies no calls → weak proof; 5 calls no diagnostic → pricing/trust; diagnostic no sprint → insufficient value; 2 pilots no continuation → not recurring

## §6 — WHAT MAKES A CHANNEL SCORE HIGH ON THIS SPECIFIC MANDATE

Automation friendliness = can a Codex/agent generate, personalize, verify, and stage sends against a class-preauth without every send needing sign?

- HIGH: Cold email via Instantly (API + templates + unsub), Reddit auto-comment (bounded), HN reply (bounded), Upwork Project Catalog listings (passive inbound), SEO farm (Codex writes, no sends)
- MED: LinkedIn service page (post/DM has ToS friction), X/Twitter (bot detection), Product Hunt (needs manual maker)
- LOW: In-person, phone calls, agency partnerships (need real conversation)

Sigrún must weight this hard — operator explicitly said "not babysit instances".

## §7 — READY-TO-FIRE INFRASTRUCTURE

Codex D1 SAFE-PUBLISH loop already bootstrapped:
- `state/experiments/approvals/latest.txt` — gate file
- `state/experiments/publications.jsonl` — send log
- `state/experiments/fitness.jsonl` — outcome log

Format for approval: `<CLASS_NAME>:<SEQ>` per line. Add class + SEQ to unlock a batch. Codex fires, curls, writes receipt.

This is exactly the class-preauth mechanic operator described. Sigrún's envelopes just need to name the class + SEQ range.
