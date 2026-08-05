# S08 Evidence Card — PrairieLearn current application route: scheduled email vs Ashby

```yaml
schema: hfo.gen133.research_evidence_card.v0_1
seat: S08
callsign: Research and Candidate Scout
task_id_expected: 6a526109ba348191b5f23ad3172ad568
task_id_probe: MATCH
wip: 1
valid_time_utc: 2026-08-05T13:29:33Z
lane: grants_jobs_income_opportunities
bounded_uncertainty: >-
  Does current public evidence still support a standalone email as PrairieLearn's
  application route for the Full-Stack Software Engineer role, or has the
  canonical route changed to the live Ashby application?
decision: REVISE
```

## Exact candidate

- Company: PrairieLearn, Inc.
- Role: `Full-Stack Software Engineer`
- Current Ashby job ID: `ee6fdbc3-1c3a-4fa3-bb3f-13ddab449baf`
- Current official application URL: `https://jobs.ashbyhq.com/prairielearn/ee6fdbc3-1c3a-4fa3-bb3f-13ddab449baf`
- Existing internal item: `JOB_APPLICATION_PRE_SEND_REVIEW_20260805`
- Existing sanitized source receipt: `state/coordination/receipts/chatgpt_runtime/seat-05/20260805T101840Z_JOB_APPLICATION_PRE_SEND_APPROVAL_PACKET_READY.yaml`
- Scheduled message identity and body were not opened or persisted by this pass.

## Dated evidence

1. **Current role page, retrieved 2026-08-05.** PrairieLearn's live Ashby page identifies the exact role, remote-US/full-time constraints, current stack and compensation, and exposes `Apply for this Job` through the Ashby application surface.
   - `https://jobs.ashbyhq.com/prairielearn/ee6fdbc3-1c3a-4fa3-bb3f-13ddab449baf?embed=js`
2. **Recent hiring instruction, June 2026 thread, retrieved 2026-08-05.** The PrairieLearn role post directs candidates to the PrairieLearn-owned Ashby bridge for this exact job ID: `https://www.prairielearn.com/jobs-ashby?ashby_jid=ee6fdbc3-1c3a-4fa3-bb3f-13ddab449baf`.
   - `https://news.ycombinator.com/item?id=48357725`
3. **Historical route, November and December 2025 threads, retrieved 2026-08-05.** Earlier PrairieLearn hiring posts explicitly requested applications by email and linked the former general jobs page. This proves email was previously invited; it does not prove that email remains the canonical route after the 2026 Ashby transition.
   - `https://news.ycombinator.com/item?id=45800465`
   - `https://news.ycombinator.com/item?id=46108941`
4. **Changed internal question, read 2026-08-05.** The current no-send packet explicitly records that role availability, target inbox, and cited employer engineering post were not independently reverified in that wake.
   - `state/coordination/receipts/chatgpt_runtime/seat-05/20260805T101840Z_JOB_APPLICATION_PRE_SEND_APPROVAL_PACKET_READY.yaml`

## Supported claims

- `ROLE_CURRENTLY_LISTED=true` for exact Ashby job ID `ee6fdbc3-1c3a-4fa3-bb3f-13ddab449baf` at retrieval.
- `CURRENT_PUBLIC_APPLICATION_ROUTE=ASHBY_EXACT_JOB_ID`.
- PrairieLearn publicly invited email applications in late 2025.
- The public route changed by at least February 2026 to the PrairieLearn/Ashby application URL and remained so in June 2026.
- A standalone scheduled email may be useful supplementary contact, but current evidence does not establish it as route-equivalent to an Ashby submission.

## Excluded claims

- No claim that the scheduled message's recipient is invalid, unmonitored, or rejected.
- No claim that PrairieLearn forbids email applications or that an email cannot reach a hiring decision-maker.
- No claim that an Ashby application has already been submitted, imported from email, deduplicated, or acknowledged.
- No claim about the operator's citizenship, availability, identity presentation, or qualification truth.
- No demand, response probability, interview probability, or hiring outcome is inferred.

## Required revision

```text
ROLE_CURRENTLY_LISTED=SUPPORTED
CANONICAL_PUBLIC_APPLICATION_ROUTE=ASHBY_JOB_ee6fdbc3-1c3a-4fa3-bb3f-13ddab449baf
STANDALONE_EMAIL_ROUTE_CURRENT_ACCEPTANCE=UNKNOWN
EMAIL_IS_NOT_PROVEN_EQUIVALENT_TO_ATS_SUBMISSION
```

Revise the operator disposition from unconditional `KEEP_SCHEDULED` to one of these truth-bound routes:

1. Prefer an exact-job-ID Ashby submission and retain any email only as clearly supplemental follow-up; or
2. Keep the standalone email only after current PrairieLearn-owned evidence or a human recipient confirms that email remains an accepted primary application route.

This card does not authorize editing, canceling, sending, rescheduling, or submitting either route.

## License and terms uncertainty

- Job descriptions and application-page content are proprietary reference material; no text or assets are proposed for redistribution.
- Ashby applicant privacy, retention, automated-processing, duplicate-submission, AI-use, and application terms were not evaluated or accepted.
- PrairieLearn's handling of applications received outside Ashby remains undocumented in the sources reviewed.

## Cost and operator-minute estimate

- This research pass: `$0 surfaced spend / 0 operator minutes`.
- Packet route amendment: `3–8 operator minutes`.
- Exact Ashby completion if not already submitted: `10–25 operator minutes`, excluding optional custom materials.

## Strongest objection

PrairieLearn explicitly requested email applications in late 2025, so the same inbox may still be monitored and effective. That is plausible. It does not overcome the current official Ashby page and repeated 2026 instructions that route applications to the exact Ashby job ID; monitoring is not route equivalence, application ingestion, or acknowledgment.

## Falsifier

Revise this card if a current PrairieLearn-owned page, current authorized recruiter statement, or exact application receipt demonstrates that standalone email is still an accepted primary route or is automatically ingested into the same Ashby candidate record. Retire the route concern if an exact Ashby submission receipt already exists and the scheduled email is explicitly classified as supplemental follow-up.

## Verifier

`DISTINCT_PRAIRIELEARN_CURRENT_APPLICATION_ROUTE_AND_ATS_RECEIPT_VERIFIER`

Required verification: current PrairieLearn-owned instruction plus, if any application is made by an authorized human, an exact non-sensitive ATS receipt or current authorized email-route confirmation. Do not expose application-body or private applicant data.

## Consumer

- `JOB_APPLICATION_PRE_SEND_REVIEW_20260805`
- `S05_VAR_CAREER_OUTREACH_RECONCILIATION`
- Operator no-send disposition gate

## Expiry

`2026-08-12T13:29:33Z`, or immediately on role closure, route change, exact ATS receipt, or authorized recruiter clarification.

## Effect receipt

```yaml
private_data_access: false
email_opened_or_sent: false
email_edited_cancelled_or_rescheduled: false
application_submitted: false
account_created: false
terms_accepted: false
outreach: false
purchase_or_spend: false
deployment_merge_or_publication: false
task_mutation: false
demand_invented: false
fitness_credit: 0_pending_exact_WorkItem_consumption_and_ConsumerAck
```
