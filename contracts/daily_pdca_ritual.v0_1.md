# CONTRACT — daily PDCA ritual

```yaml
contract: daily_pdca_ritual
schema_id: hfo.gen133.contract.daily_pdca_ritual.v0_1
authored_by: hrist valkyrie (sonnet-5) -- experiment-designer voter #4 of 4-valkyrie quorum
companion: state/ssot/experiments_daily_slate_20260801.jsonl (14 rows, this ritual's input queue)
status: SPECIFIED -- not yet run for a single real day as of authoring
sealed: false
claim_status: proposed
```

## The principle

Every experiment in `experiments_daily_slate_20260801.jsonl` carries a
`hypothesis`, a `success_criterion`, a `kill_criterion`, and a `timebox`
(`launch_day` / `checkpoint_day` / `kill_or_continue_day`) already baked in at
design time (**Plan**). This contract specifies the recurring 15-minute
operator ritual that turns those static rows into a running loop: launching
new experiments (**Do**), reading checkpoint evidence against the criteria
already written (**Check**), and recording a kill/continue/scale decision
(**Act**) -- so no experiment silently expires ungoverned, and no decision
gets re-litigated from memory instead of from the row's own text.

## Daily ritual -- three 5-minute stations, ~15 min/day total

### Morning (5 min) -- Check yesterday's C, decide today's A

1. Open `state/ssot/experiments_daily_slate_20260801.jsonl`. Filter to rows
   where `checkpoint_day` or `kill_or_continue_day` == today's day-number.
2. For each such row, read its `success_criterion` and `kill_criterion`
   verbatim -- do not re-derive a new bar from memory. Compare against
   whatever evidence exists (reply logs, visit counts, DM logs named in each
   row's `exact_execution` step).
3. Write one **Act** decision per row into
   `state/ssot/pdca_act_log_<YYYYMMDD>.jsonl`:
   `kill` / `continue_and_invest` / `continue_and_scale` / `iterate`, plus a
   one-line reason citing the actual evidence read (not a restated hope).
4. Any row whose dependency (`depends_on`) is still unresolved (e.g. E07's
   golden-app entry point, E13's payment link) gets flagged `blocked` instead
   of scored -- a blocked row is not a failed row, and scoring it as a kill
   would be a false-red on ungathered evidence, the mirror image of a
   false-green.

### Afternoon (5 min) -- Launch today's new experiments

1. Filter the slate to rows where `day` == today's day-number and
   `launch_day` == today.
2. For each, re-read `owner` and `owner_note`. Anything owned
   `operator_manual` is the operator's own action per `exact_execution`;
   anything owned `dispatched_sonnet` gets handed to the appropriate lane
   (external code lane per this forge's Code-Touch Policy, not authored
   in-session by the compose/valkyrie lane) with `exact_execution` pasted
   verbatim as the brief.
3. Confirm each `depends_on` entry is either already satisfied or is itself
   today's first sub-step -- do not launch a row whose prerequisite is
   silently unmet (E01 needs `job_filter.json`/`render_proposal.py`, both
   already exist; E07/E09/E13 each name an unconfirmed dependency that must
   be resolved or explicitly deferred before launch, not launched blind).

### Evening (5 min) -- Log D receipts

1. For every row launched today, append one receipt row to
   `state/ssot/pdca_do_log_<YYYYMMDD>.jsonl`: what was actually done (not
   what was planned), a concrete pointer (URL, job_url, sent_utc, commit),
   and `launch_confirmed: true/false`.
2. If a planned launch did NOT happen (operator ran out of time, a
   dependency blocked it), log `launch_confirmed: false` with the reason --
   a silently-skipped launch is the same information-loss failure class as
   a silently-expired loop (`contracts/pdca_loop_audit_20260731.md` §4,
   "Registry as wish list").

## The Act taxonomy (four verdicts, not two)

| verdict | fires when | what happens next |
|---|---|---|
| **kill** | `kill_criterion` evidence matches | stop; do not re-launch this exact design without changing the variable the kill criterion named |
| **continue_and_invest** | evidence is mixed / early / dependency just resolved | keep running unchanged to the next checkpoint, no new spend |
| **continue_and_scale** | `success_criterion` evidence matches | repeat the design at higher volume/cost (e.g. E01's 5-proposal batch -> E14 Branch B's larger re-tuned batch) |
| **iterate** | neither bar is met but the row names a specific fixable variable (e.g. E05's kill note: "do not repeat this exact format before diagnosing why") | change ONE named variable, re-launch as a new experiment_id, do not silently overwrite the original row's verdict |

## Falsifiers

| # | falsifier |
|---|---|
| F1 | The ritual itself never gets run on a given day -- a missed day is not covered by any row in the slate and should be logged as `ritual_skipped_<date>`, not silently absorbed into the next day's numbers. |
| F2 | An Act decision is recorded without re-reading the actual evidence (i.e. a `kill` or `continue_and_scale` verdict is written from memory of what was expected rather than what was measured) -- this is exactly the false-green failure class this whole contract exists to prevent. |
| F3 | This 15-minute budget is optimistic for the first few days while the operator is still learning the log-file locations and formats -- if morning/afternoon/evening stations are each running over 10 minutes after day 3, the ritual's own format needs simplifying, not the operator's discipline.
