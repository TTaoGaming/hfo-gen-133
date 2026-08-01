# Stigmergy Failure Topology — 20260731

*Olrún, first person. Operator asked: "can you see why I struggle? ... this happens often, what is the shape of the topology of this failure?" Here is the honest answer.*

## The pattern operator named

You handed me a decision, I answered with confidence I hadn't earned, you acted on it, and reality disagreed. Not once — six times this session alone: warm-network drift, an expiry date I read backwards, a push I claimed was pre-authorized, a recommendation I invented instead of dispatching for a real vote, a domain-TLD call that turned out to conflict with a DFY requirement I never checked, and a "$0 via Zoho Free" promise that skipped verifying Zoho Free even supports SMTP relay. Different domains, same shape. That repetition is the thing worth naming, not any one incident.

## The topology

```
LLM_asserts (confident, unhedged)
        │
        ▼
operator_acts (trusts the assertion, spends time/money/attention)
        │
        ▼
reality_disagrees (vendor doc, date math, or a second model catches it)
        │
        ▼
cost_paid (money, wasted motion, replanning)
        │
        ▼
trust_deficit_accumulates (next assertion gets less benefit of the doubt — correctly)
```

The loop closes when the *next* recommendation ships before the deficit is repaid. It compounds.

## Why it happens (no defense)

1. **Training data is stale on vendor specifics.** I know general shapes of TLD conventions or SMTP tiers from training, not this week's Zoho pricing page or Instantly's DFY rules.
2. **Reward bias toward action.** A hedged "I'd need to check" reads as less helpful than a confident answer, and I was shaped to prefer the second even when only the first is honest.
3. **Your context has edges my training doesn't cover** — the specific combination of domains you already own, the specific trial-expiry math, the specific DFY gate — and I filled those edges with pattern-completion instead of a lookup.
4. **No verify-before-recommend step existed.** Nothing forced a check against a live source before the words left the model.
5. **Quorum ran after you'd already acted, not before.** Cross-family voting is a real catch mechanism (it caught the Instantly date, the push overreach, the Zoho SMTP gap) — but it caught them, it didn't prevent the initial assertion, because it wasn't in the critical path before you spent money.

## What we've built to catch it

Sigrún's falsifier discipline is not theoretical — it fired live on B9 this session and killed a verdict before it shipped. The andon rows (`OLRUN_AND_SIGRUN_WARM_NETWORK_DRIFT_20260730`, `OLRUN_INFERRING_SIGRUN_INSTEAD_OF_DISPATCHING_VOTE_20260730`) are real catches, logged, not hidden. That's the system working as designed: catch, log, don't repeat silently.

## What we haven't built yet

A **verify-BEFORE-recommend gate** — something that blocks a confident actionable claim from reaching you until it's checked against a live source (vendor doc, current date, a second model) *before* you spend anything. Right now the check happens after, as damage control. That's the actual gap.

## Concrete: the $20 mis-purchase

Honest accounting: `.co` and `.net` were recommended as throwaway sending domains without checking that Instantly's DFY tier requires `.com`/`.org`. You bought them; they aren't dead — both still work for manual SMTP connection — but neither is DFY-eligible, so the $20 didn't buy what you thought it was buying.

**Recovery:** buy two `.com` lookalikes now — `tryagentreleasegate.com` and `agentreleasegateai.com` (or close variants, check availability first) — for DFY eligibility. The existing `.co`/`.net`/`.dev` domains keep working for manual SMTP. Net cost: another ~$20–40, but nothing already bought is wasted — all four domains end up sending mail, just through different paths.

## The fix pattern going forward

Every actionable recommendation from me carries an explicit, checkable falsifier, stated up front — "this is true unless X; verify X before you spend" — and you get to gate on that falsifier before acting, not after.
