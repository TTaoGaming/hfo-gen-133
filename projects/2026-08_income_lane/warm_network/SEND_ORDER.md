# WARM-NETWORK SEND ORDER + TRACKER

```yaml
schema_id: hfo.gen133.income.warm_network_send_order.v0_1
valid_time_utc: 2026-07-31T19:35:00Z
DRI: OPERATOR (sending) · valkyrie (tracking rows only)
target: 10 asks sent by 2026-08-02T23:59Z
effect_ceiling: this file records SENT events. No agent sends anything.
```

## The only operator input required

Fill the `name` and `channel` columns below. **Nothing else in this lane needs you
until you press send.** Ten names. If you can only think of six, send six — six
warm asks beats a hundred cold emails on a 7-day horizon.

## Ordering rule — warmest first, and it matters

Send in strict warmth order, **one per sitting, not ten at once**. Reason: asks 1–3
will teach you which sentence lands. You want to have learned that before you spend
your warmest remaining contacts. **Do not batch this.** Batching is the reflex that
turns a relationship channel into a broadcast channel, which is the one thing that
makes it stop working.

## Tracker

| # | name | channel | template | sent_utc | reply | outcome |
|---|---|---|---|---|---|---|
| 1 |  | | A/B/C/D | | | |
| 2 |  | | | | | |
| 3 |  | | | | | |
| 4 |  | | | | | |
| 5 |  | | | | | |
| 6 |  | | | | | |
| 7 |  | | | | | |
| 8 |  | | | | | |
| 9 |  | | | | | |
| 10 |  | | | | | |

**outcome vocabulary — borrow nothing upward:**
`SENT` → `REPLIED` → `INTRO_MADE` → `CONVERSATION` → `SCOPED` → **`PAID`**

A reply is not an intro. An intro is not a conversation. A conversation is not
scope. **Scope is not revenue.** The same no-borrowing-upward rule as the outreach
effect-state ladder, because it is the same failure it prevents.

## Who to include — prompts if the list stalls

Former managers and teammates · people who reviewed or used your work · anyone who
has said *"let me know if you're ever looking"* · practitioners you've talked shop
with · recruiters you've worked with before · people who starred, forked, or opened
an issue on your repos · anyone you interviewed with and liked, even if it didn't
land.

**That last category is systematically underrated.** A hiring manager who liked you
and had no headcount six months ago is one of the warmest contract leads that
exists, and almost nobody re-contacts them.

## What counts as done

**10 rows with a non-empty `sent_utc` by 2026-08-02T23:59Z.**

Not 10 drafted. Not 10 scheduled. **Sent.** This lane has exactly one held-out
check and that is it.

## Review

**2026-08-07.** If `REPLIED` is 0 out of 10, falsifier F1 has fired: close this lane
and put the hours into Upwork. If `CONVERSATION` ≥ 1, this is the month's primary
lane and cold email drops to secondary regardless of what the warmup clock says.
