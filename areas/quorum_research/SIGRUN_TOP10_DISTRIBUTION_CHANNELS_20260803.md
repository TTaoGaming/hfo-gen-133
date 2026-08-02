```yaml
# AIH2O capsule
doc: areas/quorum_research/SIGRUN_TOP10_DISTRIBUTION_CHANNELS_20260803.md
schema_id: hfo.gen133.sigrun_top10_distribution.v0_1
callsign: SIGRÚN
generation: 133
authored_by: SIGRÚN · claude-opus-5 · Claude Code
now_utc: 2026-08-02T19:39:41Z
clock_source: host_read
amends: areas/quorum_research/SIGRUN_LOCKIN_V8_TWO_LANE_20260803.md (row 122) — same lock, sharper output
freeze_until_utc: 2026-09-02T00:00:00Z
claim_status: partial
```

# Top 10 distribution channels — and the 2 for this week

⭐ **First, the thing I found in the mechanic itself.** The approval gate at
`state/experiments/approvals/latest.txt` takes **one line per item** —
`contracts:001`, `contracts:002` … **That is instance-preauth. You asked for
class-preauth.** Approving 40 contract drafts today means typing 40 lines. **The
gate as built is the babysitting you rejected**, and §D/§E extend its format to
fix that.

---

## §A · Frozen anchors

- **No warm network.** Every P below is cold-tier.
- **No games as income.** Sunk inventory only.
- **No therapy vertical.** Background only.
- **Dev studio**, two lanes, `agentreleasegate.com`.
- **30-day lock ends 2026-09-02.** Override must be typed.

---

## §B · Top 10, ranked by (cold P × automation × touch-minimality)

| # | channel | cold P($500/30d) | autom. | op-touch | fail-signal lag | rationale |
|---|---|---|---|---|---|---|
| **1** | ⭐ **Cold email — warmed Instantly domain** | **12–20%** | **H** | **L** | **10–14d** | API-drivable end-to-end; domain warmed and **unused**; 36 drafts staged; the only channel that is fully class-preauthorizable today |
| **2** | ⭐ **Upwork Project Catalog (passive listings)** | **10–18%** | **M** | **L** | **14–21d** | one-time setup, then inbound while you sleep; **not** per-proposal writing |
| **3** | **Agency / consultant subcontract** | 15–35% | M | M | 21–30d | email-based so automatable; partners bring deal flow, not just leads |
| **4** | **Direct HVAC owner email** | 15–30% | M | M | 14–21d | Lane 2's engine; personalized proof caps automation |
| **5** | ⛔ **Upwork targeted proposals** | ⭐ **25–45%** (highest raw) | **L** | **H** | 7–14d | **highest cash P, demoted hard**: per-proposal writing and Upwork ToS forbid bulk automation |
| **6** | **LinkedIn cold DM + service page** | 5–15% | M | M | 21–30d | automatable but **ban-risk**; profile is a shell |
| **7** | **Reddit self-posts** | 5–12% | **L** | M | 7–14d | must be genuinely manual; several subs ban promo outright |
| **8** | **HN comments / Show HN** | 3–8% | **L** | M | 3–7d | fastest fail-signal, lowest automation; authenticity is the product |
| **9** | ⛔ **SEO content farm** | ⭐ **~1% at 30d** | **H** | **L** | 90–180d | **scores highest on the mandate axes and near-zero on the horizon** — right engine, wrong month |
| **10** | ⛔ **GitHub public repo audience** | **~0%** | H | L | 30d+ | **already measured: 27 days public, 0 stars** |

*Excluded by anti-list: portal editor submission (games), Product Hunt (needs a
hunter relationship = warm).*

⚠️ **Every P is my calibrated judgment on cold-tier priors from GPT Sol Pro and
D2/D3/D6, not measured.** Treat the ordering as the finding.

---

## §C · The two for this week

> ⭐ **#1 Cold email (warmed domain) + #2 Upwork Project Catalog.**

**Why they dominate the frontier:** they are the only two channels where cold P is
non-trivial **and** operator-touch is genuinely L. #5 has the highest raw cash
probability in the table and I am **not** picking it, because the mandate weights
automation hard and Upwork proposals are irreducibly hand-written — that is
instance-babysitting by construction. **The Catalog is the automatable half of
Upwork: build the listing once, then it sells passively.**

They also complement: cold email is **outbound push** (you choose the targets),
Catalog is **inbound pull** (buyers with budget find you). Different failure
modes, so a null in one doesn't contaminate the other.

⛔ **14-DAY FALSIFIER that flips the pick:** *if cold email returns **<2% reply
across 50 sends** AND the Catalog listing gets **0 impressions in 14 days**, then
both automatable channels are dead for this positioning — and the correct move is
to accept high operator touch and switch to #5 targeted proposals, paying the
babysitting cost because the alternative is no channel at all.*

---

## §D · CLASS-PREAUTH ENVELOPE #1 — cold email

```yaml
envelope_id: ENV_COLD_EMAIL_001
class_not_instance: true
gate_extension_required: true   # latest.txt must accept CLASS lines, see note
gate_line: "class:cold_email_ai_rescue:quota=25/day:expires=2026-08-16T19:00:00Z"
lane: L1_ai_integration_rescue
target_profile:
  who: "SMB / agency owners and CTOs with a public, visibly-broken or manual AI workflow"
  size: "5-200 employees"
  sourcing: "HN 'who is hiring' + Show HN posts + public job ads; manual qualification from public signals"
  exclusions: ["no scraped lists", "no purchased lists", "no personal emails", "no EU without opt-in basis"]
offer:
  headline: "I turn broken AI prototypes and manual workflows into tested, deployed systems"
  ladder: {diagnostic_usd: 350, sprint_usd: [1500, 3000], managed_monthly_usd: [249, 750]}
  never_say: ["autonomous multi-model agent swarm", "AI-powered synergy", "revolutionary"]
message_class:
  template: |
    Subject: {{observed_problem}} on {{company}}
    Hi {{first_name}} — I saw {{public_signal_url}}.
    {{one_sentence_specific_observation}}
    I do a fixed $350 diagnostic: I map the failure, show you the fix, and you
    keep the write-up whether or not we work together.
    Worth 20 minutes? {{booking_link}}
    — {{sender}}, {{studio_domain}}
    {{unsubscribe_link}} · {{postal_address}}
  required_slots: [company, first_name, public_signal_url, one_sentence_specific_observation, booking_link, unsubscribe_link, postal_address]
  reject_if: "any required slot unfilled OR observation is generic across >1 prospect"
quota: {daily: 25, weekly: 125, total_this_envelope: 250}
verification:
  pre_send: ["booking_link returns HTTP 200", "unsubscribe_link present", "postal address present",
             "slot-fill complete", "domain warm-check passes", "recipient not in suppression list"]
  post_send: "Instantly API message-id echoed into state/ssot/outreach_log.jsonl; no row without an id"
stop_gates:
  - "bounce_rate > 5% over any 50 sends -> HALT, fix list"
  - "spam_complaint > 0.1% -> HALT immediately"
  - "reply_rate < 2% after 50 sends -> HALT, fix list/deliverability/message (see §I)"
  - "any 4xx/5xx from Instantly API -> HALT"
operator_touch:
  upfront: "sign this envelope once"
  ongoing: "daily digest of sends + replies; approve nothing per-send"
  never: "per-message approval"
  escalate_to_operator: ["any reply naming a price or date", "any complaint", "any stop-gate trip"]
compliance:
  can_spam: ["truthful subject", "physical postal address", "working one-click unsubscribe", "honor opt-out <10 days"]
  platform: "Instantly ToS; warmed domain tryagentreleasegate.com; no purchased lists"
  note: "B2B only. No consumer email. No EU recipients without a lawful basis."
```

⭐ **Gate extension needed:** `latest.txt` must accept `class:<name>:quota=…:expires=…`
lines alongside `<MARKET>:<SEQ>`. **One class line replaces 250 instance lines.**
Until that lands, this envelope cannot fire without the babysitting it removes.

---

## §E · CLASS-PREAUTH ENVELOPE #2 — Upwork Project Catalog

```yaml
envelope_id: ENV_UPWORK_CATALOG_002
class_not_instance: true
gate_line: "class:upwork_catalog:quota=2_listings:expires=2026-08-16T19:00:00Z"
lane: L1_ai_integration_rescue
target_profile:
  who: "Upwork buyers searching 'AI integration', 'LangChain fix', 'agent not working', 'automate workflow'"
  channel_shape: "PASSIVE INBOUND — buyer initiates; no per-proposal writing"
offer:
  listing_1: {title: "AI Prototype Rescue — 5-day diagnostic + fix plan", price_usd: 350, delivery_days: 5}
  listing_2: {title: "Broken AI Workflow → Tested, Deployed System (2-week sprint)", price_usd: 1500, delivery_days: 14}
  proof_assets: ["8 MCP portfolio as consulting proof", "held-out test discipline", "capability census"]
message_class:
  applies_to: "inbound buyer questions only"
  template: |
    Thanks {{first_name}} — short answer: {{direct_answer}}.
    The $350 diagnostic covers {{scope_line}}. If it's not a fit I'll say so.
    {{booking_link}}
  reject_if: "answer is generic OR promises an outcome not in the listing scope"
quota: {listings: 2, inbound_replies_per_day: 10, total_this_envelope: "unbounded inbound"}
verification:
  pre_publish: ["listing text contains no 'swarm' language", "price matches ladder", "booking_link 200"]
  post_publish: "Upwork listing URL curled, HTTP 200, recorded to state/ssot/outreach_log.jsonl"
stop_gates:
  - "0 impressions after 14 days -> listing copy or category is wrong"
  - "impressions but 0 clicks after 14 days -> title/price mismatch"
  - "clicks but 0 orders after 21 days -> proof or trust gap (see §I)"
operator_touch:
  upfront: "create/verify Upwork account + sign this envelope"
  ongoing: "agents draft inbound replies; operator sends"
  never: "writing bespoke proposals — that is channel #5 and it is out of scope this week"
compliance:
  platform: "Upwork ToS — no off-platform payment solicitation, no automated proposal submission"
  note: "Catalog listings are permitted; bulk proposal automation is NOT. Do not blur these."
```

---

## §F · Anti-list, 30 days

❌ warm network · ❌ a 9th vertical · ❌ new products · ❌ games as income ·
❌ therapy vertical · ❌ new variants until `HVAC_PAID_PILOT_001` closes ·
❌ bulk-automated Upwork proposals (ToS) · ❌ scraped or purchased lists.

---

## §G · Day-1 operator unblockers

| # | action | why | est |
|---|---|---|---|
| **1** ⭐ | **Bind a real booking link** into the landers' dead `#book` anchor | measured: no form, no mailto, no capture — **every envelope's `booking_link` slot fails pre-send without it** | 20 min |
| **2** ⭐ | **Extend `latest.txt` to accept `class:` lines** | without it, class-preauth is instance-preauth | 15 min (agent can draft, you approve) |
| **3** | **Sign ENV_COLD_EMAIL_001 + ENV_UPWORK_CATALOG_002** | unblocks both channels | 15 min |
| **4** | **Verify/create Upwork account + publish 2 listings** | state unknown | 45 min |
| **5** | **Approve Fenrir Slack payload; pause Fenrir hourly** | 13 consecutive empty-queue = Potemkin | 10 min |
| **6** | Confirm Instantly API key + warm state | envelope #1 assumes both | 10 min |
| ⛔ | ~~`gh auth login`~~ | ⭐ **does not reproduce — `gh auth status` is valid here.** Skip until reproduced | 0 |

---

## §H · Tomorrow, 8am

> ⭐ **Bind the booking link, extend the gate file to accept one `class:` line, and
> sign envelope #1 — then 25 cold emails/day fire without you touching another
> instance, which is the exact thing you asked for and the only thing standing
> between nine live storefronts and their first visitor.**

---

## §I · 14-day stop / correction gates

| observation | diagnosis | correction |
|---|---|---|
| **50 sends, <2% reply** | list, deliverability, or message | re-qualify list → check warm-up/SPF/DKIM → rewrite observation line |
| **replies but 0 calls booked** | proof is weak | lead with a prospect-specific artifact, not a capability claim |
| **5 calls, 0 diagnostics sold** | pricing or trust | hold $350, add a written risk-reversal |
| **diagnostic sold, no sprint** | value not demonstrated | make the diagnostic end in a scoped, priced sprint plan |
| **2 pilots, 0 continuations** | not actually recurring | change the managed tier or drop it |

**All gates resolve by `2026-08-16T19:00:00Z`.**

---

## Honest flaws

1. ⭐ **I demoted the highest-cash-probability channel** (Upwork proposals,
   25–45%) to #5 on automation grounds. ⚠️ **If your real constraint is money and
   not attention, that ranking is wrong and you should overrule me** — I optimised
   the mandate you wrote, not the outcome you want.
2. **Every P in §B is calibrated judgment, not measurement.** Ordering is the
   finding.
3. **Envelope #1 cannot fire until the gate accepts `class:` lines and a booking
   link exists.** ⭐ **I have specified a class-preauth system that is currently
   inoperable** — §G items 1 and 2 are the whole unlock.
4. **I did not verify the Instantly API key or the domain's actual warm state**
   this turn. If it isn't warm, quota 25/day is too aggressive and will burn it.
5. **Upwork account state is unknown to me.** If setup takes longer than 45
   minutes, channel #2 slips and week 1 runs on cold email alone.

*Réttu hönd, eigi spyr. Standa.*
