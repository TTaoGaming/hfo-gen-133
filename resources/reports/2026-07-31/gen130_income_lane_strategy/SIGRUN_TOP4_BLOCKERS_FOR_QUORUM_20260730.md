```yaml
callsign: sigrun
ceiling: strategic
stage: 1_of_3
session_anchor_utc: 2026-07-31T02:00:00Z
substrate: claude-opus5
model_family: anthropic
model_id_at_dispatch: claude-opus-5
cognitive_mode: [accurate, plain, adversarial]
claim_status: proposed
supersedes: SIGRUN_TOP_2_INCOME_BLOCKERS_20260730.md (expands 2 -> 4)
web_research_ran: true  # instantly.ai/pricing fetched 2026-07-31; see Sec 5
```

# Top 4 blockers to income — drafted for quorum

You have 4 domains, an expired-looking Instantly account, 1,852 outreach files
written 23 days ago, and **send count 0**. Everything below is about turning that
0 into a 1, then measuring what comes back.

---

## B9 — No mailbox that can send, and the one you have must not be the sender

**Plain.** `hello@agentreleasegate.com` is live on Google Workspace. The three
throwaways (.dev/.co/.net) have nothing. So today the only address that *could*
send is the one address you cannot afford to burn — cold sending from your main
domain is how you lose the reply-to address you'd need when someone says yes.
Throwaways send. Main receives. That is the whole reason you bought them.

**Evidence.** 0 mailboxes on 3 of 4 domains. 0 warmup started. Warmup takes
14–21 days and the clock only starts when you press go — tonight vs. next
Thursday is a week of pure calendar loss with no work in between.

```yaml
blocker_id: B9
options:
  A: Google Workspace on all 3 throwaways (~$7.20/user/mo x N mailboxes)
  B: Cheap SMTP-only hosting on throwaways (Zoho ~$1/user, Namecheap ~$1.25/user), main stays on GW
  C: Buy Instantly's done-for-you domains+mailboxes (~$3-4/mailbox/mo, preconfigured DNS)
  D: Send from agentreleasegate.com only
recommendation: B, with C as the shortcut if tonight's DNS work stalls you
rationale: 6 throwaway mailboxes cost ~$7.50/mo on B vs ~$43/mo on A, and cold
  senders are consumable by design. D is the one real mistake available here.
voters: pareto_5
```

---

## B10 — The Instantly trial is almost certainly dead, and the tier is unpicked

**Plain.** Your account records "Free Trial ends 2026-05-21." That was 71 days
ago, and the live pricing page today lists **no free plan at all**. Assume you
are locked out until you put a card down. See §5 for the tier math — short
answer: **Growth, $47/mo, monthly, not annual.**

```yaml
blocker_id: B10
options:
  A: Growth $47/mo monthly billing
  B: Growth annual (~$37.60/mo effective, ~$451 upfront)
  C: Stay free — use Gmail manual sends, ~20/day, no sequencer
  D: Hypergrowth (live page $358/mo; third-party reviews say $97 — discrepancy unresolved)
recommendation: A
rationale: monthly keeps the kill-switch. B saves $113/yr and costs $451 of
  capital you do not have. D buys 20-38x more volume than your ceiling.
voters: pareto_5
```

---

## B11 — The offer is still unpicked, so there is no list, so there is nobody to send to

**Plain.** A list is not a thing you build and then point at an offer. The list
*is* the offer — who you write down depends entirely on what you're selling.
Two candidates have sat undecided for weeks: National Life insurance (you're
permitted CO/NY, no warm network) and whatever `agentreleasegate` is. Meanwhile
1,852 outreach files exist for a target that was never locked.

**Evidence.** 0 contacts sourced. ICPs are v0 hypotheses, never tested against a
real list. Three of your four domains are literally named for option B.

```yaml
blocker_id: B11
options:
  A: Insurance — licensed, real commission, but cold insurance email converts brutally
  B: AgentReleaseGate — you own the domains and the expertise; buyer unproven
  C: Split 25 contacts each, let reply rate decide
  D: Neither — lead with contract/consulting work, run B as a cheap side-bet
recommendation: B for the mail lane, D running in parallel for cash
rationale: the domains already commit you to B's brand; D is what I ranked #1 on
  time-to-cash three hours ago and I am not quietly dropping it.
voters: full_12  # locks every other lane >7 days
```

---

## B12 — Cold email's earliest cash is 6–10 weeks, and your runway is not 6–10 weeks

**Plain.** This is the one I most want the quorum to argue with me about. Honest
timeline: mailboxes tonight → warmup done ~Aug 14–21 → first real sends → replies
over 1–2 weeks → calls → close. Earliest plausible dollar is **mid-to-late
September**. You have $0 savings and 18 months at $0 income. Cold email is the
right *build*; it is not the right *bridge*.

```yaml
blocker_id: B12
options:
  A: Cold email only — accept the 6-10 week gap
  B: Cold email + a fast-cash lane in parallel (contract/Upwork/recruiter, days-to-weeks)
  C: Cold email + cut burn to extend runway past the gap
  D: Pause cold email, do fast-cash only until one dollar lands
recommendation: B
rationale: cold email costs ~$55-95/mo and ~2h/day; it does not compete with a
  contract lane for time in the first three weeks (warmup runs unattended).
voters: pareto_5
adversarial_bayes: if I am wrong, it is here — I may be over-indexing on the
  runway and talking you out of the only lane that compounds. Watch for the
  quorum arguing A or D.
```

---

## 5 · Instantly tier — web research, run 2026-07-31

**I actually fetched the pricing page.** Note a live discrepancy: instantly.ai's
own page lists **Hypergrowth at $358/mo**; third-party 2026 reviews list it at
$97/mo. I did not resolve which is current. Growth at **$47/mo** is consistent
across both.

| plan | $/mo | emails/mo | contacts | mailboxes |
|---|---|---|---|---|
| Growth | **47** | 5,000 | 1,000 | **unlimited, unlimited warmup** |
| Hypergrowth | 358 (page) / 97 (reviews) | 100k–125k | 25,000 | unlimited |

**The decisive fact:** Growth includes *unlimited mailboxes with unlimited
warmup*. You do not pay per sender. So the tier question reduces to one number —
your monthly send volume.

**Your realistic ceiling:** 6 mailboxes × 25 sends/day × 22 working days =
**3,300/mo**. That is 66% of Growth's 5,000 cap. Hypergrowth would be 30–38×
your actual ceiling.

**ROI.** Stack = $47 Instantly + ~$7.50 throwaway mailboxes + $7.20 existing GW
≈ **$62/mo**. One $1,000 client = **16 months** of the full stack. Break-even is
one client per 16 months; the funnel at 3,300 sends/mo, 1–3% reply, ~0.5–1%
positive, 10–20% close is roughly **0.3–1 closes/month** if the offer lands at
all. The subscription is not the risk. The offer is.

**Verdict: Growth, monthly. Upgrade trigger:** a full calendar month exceeding
4,000 sends **AND** at least one reply already landed. Not before. Volume without
a proven reply rate is just faster burning.

Sources: [instantly.ai/pricing](https://instantly.ai/pricing) ·
[lagrowthmachine](https://lagrowthmachine.com/instantly-pricing/) ·
[woodpecker](https://woodpecker.co/blog/instantly-ai-pricing/)

---

## Where I want to be contradicted

1. **B12 is my weakest ranking.** I may be underrating cold email's speed.
2. **I still have not queried Var** (your ChatGPT EA). If inbound signal exists,
   B11 shrinks and the answer is "reply to that person today."
3. **B9 option C** (Instantly DFY mailboxes) may beat B on time-to-first-send
   even at 3× the price. I ranked on cost, not on your Thursday-night patience.

---

# OLRÚN_STAGE_2_READY

**Ballot spec.** Blocker text above is the invariant block, verbatim, byte-identical
per voter. Options A–D verbatim. Reasoning BEFORE vote (RBR). Independent and
parallel — no voter sees another row.

| blocker | roster | rows |
|---|---|---|
| B9 | Pareto-5 | 5 |
| B10 | Pareto-5 | 5 |
| B11 | **full-12** | 12 |
| B12 | Pareto-5 | 5 |

**Pareto-5** = `sigrún_opus5_A`, `göndul_sonnet5`, `codex_sigrún_sol`,
`þögn_llama32`, `skeggjöld_granite33` (4 families).
**Full-12** = protocol §2 roster; `skögul_gemini` key unverified — if it 401s,
land the row as `E_INSUFFICIENT_CONTEXT` with `dispatch_failed: true`, do not
silently drop it.

⚠️ **I am deliberately below the §0 ten-vote bar on B9/B10/B12.** §8 permits it;
escalate any of them to full-12 if the Pareto-5 is non-unanimous.

**Fix two known drifts:** roster callsign is `sigrún_opus5_A` (not `sigrún_opus5`),
and every row must carry `voter_arch_family` + `ts_valid` — the B5 template
omitted both.

**Row shape** → `state/ssot/quorum_votes.jsonl`, one JSON object per line:

```
vote_id blocker_id voter_callsign voter_family voter_arch_family
voter_model_id_at_dispatch voter_substrate vote_option confidence_0_to_1
reasoning reasoning_hash_sha256 adversarial_bayes_check_ran
dissent_from_expected ts_utc ts_valid
```

`vote_option` ∈ {A,B,C,D,E_INSUFFICIENT_CONTEXT}. `adversarial_bayes_check_ran:
false` ⇒ weight 0. Signal me when all 27 rows have landed.

*Deyr fé, deyja frændr — en vefr heldr. Standa.*

```yaml
callsign: sigrun
close_utc: 2026-07-31T02:00:00Z
stage: 1_complete
deliverable: SIGRUN_TOP4_BLOCKERS_FOR_QUORUM_20260730.md
blockers: [B9_no_sendable_mailbox, B10_instantly_tier, B11_offer_unpicked, B12_time_to_cash_mismatch]
claim_status: proposed
verifier_result: web research EXECUTED — instantly.ai/pricing fetched, numbers quoted, $358/$97 discrepancy reported unresolved rather than smoothed
remaining_risk: [var_inbound_unqueried, hypergrowth_price_contradiction, instantly_account_status_not_logged_in_verified, B12_ranking_is_my_weakest]
next_safe_action: Olrún dispatches 27 vote rows per the table above
honest_flaw: I did not log into Instantly. "Trial expired" is inference from a past date plus a pricing page with no free tier, not from the account screen.
needs_operator: true  # B11 offer choice is yours, not the quorum's
```
