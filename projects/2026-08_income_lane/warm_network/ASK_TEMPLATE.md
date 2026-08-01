# WARM-NETWORK AVAILABILITY ASK — templates

```yaml
schema_id: hfo.gen133.income.warm_network_ask.v0_1
valid_time_utc: 2026-07-31T19:30:00Z
author: SIGRUN_P4 · drafted for OPERATOR to send
DRI: OPERATOR — every message here is operator-sent. The hive drafts; it does not send.
why_operator_only: warm relationships are the highest-value and least-replaceable asset
                   in the system. See delegation spec section 1.3.
effect_ceiling: DRAFT ONLY. Nothing here is sent by any agent.
```

## Rules that make this work — read before sending

1. **One ask. No pitch deck, no link dump, no case study attached.** The ask is for an intro or a lead. Anything else lowers the reply rate.
2. **Under 120 words.** Someone who knows you does not need context.
3. **Give something regardless of the answer.** The free 2-minute teardown costs nothing and makes a "no" comfortable, which is what keeps the relationship intact.
4. **Send individually. Never BCC, never a group.** A visible group ask reads as broadcast and converts near zero.
5. **Do not follow up more than once.** These are relationships, not a sequence.
6. **Send in the operator's own voice.** Edit these until they sound like you. A template that sounds like a template defeats the entire advantage this channel has.

---

## A — Former colleague / someone who has seen you work

> Hey [NAME] —
>
> Quick one. I'm taking on contract AI-engineering work starting now — agent
> reliability and eval, 20–25 hrs/week.
>
> The specific thing I've gotten good at: catching agents that report "done"
> without a checkable receipt. I've been building gates that refuse a green
> status unless it carries independent proof.
>
> If you know a team fighting that — agents passing tests that didn't run,
> evals that look clean and aren't — I'd appreciate an intro.
>
> Either way, happy to send you a 2-minute teardown of any agent surface you
> care about. No strings.
>
> [YOUR NAME]

## B — Someone in a hiring position

> Hi [NAME] —
>
> I'm available for contract or fractional AI-engineering work, 20–25 hrs/week,
> starting immediately.
>
> Background: 18 months building agent-reliability infrastructure — policy
> gates, held-out verification, append-only audit trails. Concretely: a gate
> that refuses to record a task as complete unless a verifier artifact exists.
>
> Are you or anyone on your team dealing with agents that self-report success?
> If it's not a fit, no problem at all — but if you know someone hiring for
> this, an intro would mean a lot.
>
> [YOUR NAME]

## C — Peer / practitioner (no hiring authority, but knows people)

> [NAME] —
>
> Reaching out because you know this space better than most.
>
> I'm opening up 20–25 hrs/week for contract agent-reliability work. The niche
> is narrow on purpose: agents that claim done without proof, and the
> deterministic gates that catch it.
>
> Not asking you to hire me — asking if two or three names come to mind who'd
> find that useful right now.
>
> And if you want one, I'll do a free 2-minute teardown of any public agent
> surface, whether or not anything comes of this.
>
> [YOUR NAME]

## D — Recruiter you have worked with before

> Hi [NAME] —
>
> Circling back. I'm open to contract or full-time AI-engineering roles again,
> available immediately.
>
> Focus: agent reliability, evaluation, and security — the "did it actually do
> what it claims" layer. 20–25 hrs/week for contract, or full-time for the
> right role.
>
> If anything crosses your desk, I'd appreciate the ping. Happy to send a short
> written summary of recent work if that's useful for a submission.
>
> [YOUR NAME]

---

## What you say when someone replies "what exactly do you do?"

Keep it to three sentences. Do not escalate into the full architecture.

> AI agents routinely report that they finished a task when they didn't — they
> pass a test that never ran, or mark a fix complete with no evidence behind it.
> I build the gate that refuses to accept "done" unless it carries a checkable
> artifact, so the failure surfaces at the moment it happens instead of in
> production. Usually a 1–2 week engagement to install it, then ongoing if it's
> earning its keep.

## What you say when someone asks your rate

> Contract work is $[RATE]/hr, 20–25 hrs/week. For a scoped audit instead of an
> ongoing engagement, it's a fixed $[AUDIT_PRICE] for a one-week deliverable.

**Fill both numbers in BEFORE sending message #1.** Being asked your rate and not
having one ready is the most common way a warm lead cools, and it will be asked.

---

## FALSIFIERS

| # | falsifier | what it means |
|---|---|---|
| F1 | 10 asks → 0 replies in 7 days | the network is colder than assumed. Upwork becomes the real #1 and this lane closes. **Worth $0 and 45 minutes to learn** |
| F2 | Replies come but all say "not right now" | timing, not fit. Re-ask in 60 days; do not follow up sooner |
| F3 | Replies ask what you do and the 3-sentence answer doesn't land | the positioning is wrong, not the channel. **Fix the sentence before sending ask #6** |
| F4 | The operator will not send these because they feel like asking for a favor | **the most likely failure and it is not a technical one.** Then the constraint on 18 months of $0 was never tooling |
