---
schema_id: hfo.gen133.s08.evidence_card.v0_1
seat: S08
callsign: Research and Candidate Scout
expected_task_id: 6a526109ba348191b5f23ad3172ad568
wip: 1
created_utc: 2026-08-02T04:30:00Z
canonical_repo: TTaoGaming/hfo-gen-133
canonical_branch: agent/gen133-bootstrap-20260730
lane: grants_jobs_income_opportunities
question: Is Anthropic Fellows Program, AI Security job 5030244008 still an actionable immediate-income candidate after its advertised July 26 deadline?
result: REVISE
fitness_credit: 0
consumer:
  - S09 product decision queue
  - income-lane backlog owner
verifier: distinct nonproducer current-source reviewer
expiry: 2026-08-09T04:30:00Z or immediately on official posting/form change
privacy_class: SANITIZED_PUBLIC
world_effect_ceiling: public-source read + one Git evidence card + one Slack pointer
---

# S08 evidence card — Anthropic AI Security Fellows deadline status

## Self-probe

- Carrier identity: S08 Research and Candidate Scout; expected native task ID `6a526109ba348191b5f23ad3172ad568` supplied by wake packet, not independently exposed by the connector surface.
- Tools available/used: GitHub branch search/read/write/readback; public web search/open; Slack channel read/post.
- Duplicate check: no Gen-133 card matched `Anthropic Fellows AI Security`, Greenhouse job `5030244008`, or the July 26 deadline before this write.

## Exact candidate

- Organization: Anthropic
- Candidate: **Anthropic Fellows Program, AI Security**
- Greenhouse job ID: `5030244008`
- Official job URL: https://job-boards.greenhouse.io/anthropic/jobs/5030244008
- Listed locations: London, Ontario, Remote-Friendly United States, San Francisco
- Program shape stated by the posting: four months, full time, expected 40 hours/week; weekly US stipend `$3,850`; compute funding around `$15,000/month`; US/UK/Canada work authorization required; remote fellows permitted in those countries.

## Bounded finding

**REVISE the candidate from `APPLY_NOW` to `NEXT_COHORT_WATCH`.**

On 2026-08-02 the official Greenhouse page remained reachable and Anthropic's live careers index still listed the role. The same posting says applications for the next cohort close at **11:59 p.m. PT on July 26** and the cohort is expected to start November 2. That advertised deadline is already past. The page also says Anthropic runs multiple cohorts, reviews applications on a rolling basis, and may accommodate off-cycle starts. The linked Airtable application endpoint still resolves, but a resolving form does not prove that late applications are accepted, reviewed for this cohort, or assigned to a later cohort.

Therefore this is not honest immediate-income inventory without a fresh official deadline or explicit late-application statement. Preserve the lead as a high-fit watch item; do not count it as an open application opportunity.

## Dated primary/current sources

1. Anthropic Greenhouse job `5030244008`, fetched 2026-08-02: deadline July 26; expected November 2 start; four months full-time; stipend, compute support, qualifications, work authorization, remote policy, and recruiting partner. https://job-boards.greenhouse.io/anthropic/jobs/5030244008
2. Anthropic live careers index, fetched 2026-08-02: the AI Security Fellows role remained listed as Remote-Friendly United States among current openings. https://www.anthropic.com/careers/jobs
3. Official application redirect from the posting, checked 2026-08-02: `https://bit.ly/afpsafety` resolved to an Airtable form endpoint. Form reachability is transport evidence only, not acceptance-status evidence.

## Supported claims

- The named posting and Greenhouse job ID were publicly reachable on 2026-08-02.
- The careers index still presented the role as an open listing on 2026-08-02.
- The posting itself states a July 26 application deadline and November 2 expected cohort start.
- The posting states multiple cohorts and rolling review, but does not explicitly authorize post-deadline applications for the advertised cohort.
- The opportunity is topically aligned with AI security, agent research, open-source contribution, offensive security, empirical ML, and ambiguous technical ownership.

## Excluded claims

- No claim that the application is currently accepting or reviewing late submissions.
- No claim that July 26 refers to any year other than the current advertised cycle; the page omits the year in the deadline sentence.
- No claim that the user qualifies, will receive an interview, or will receive a full-time offer.
- No claim that Colorado residency is independently approved beyond the posting's `Remote-Friendly, United States` wording.
- No application, account creation, resume upload, reference contact, outreach, terms acceptance, or private-data use occurred.
- No income timing claim: even a valid application would be a competitive four-month program starting around November, not near-term cash.

## License / terms uncertainty

- Software license: not applicable.
- Application privacy terms, Constellation recruiting terms, Airtable data handling, reference-check consent, and Anthropic candidate AI-use policy were not accepted or fully audited.
- The posting says Constellation manages applications/interviews and that completing its external form is required; submitting the Greenhouse shell alone is insufficient.

## Cost and operator-minute estimate

- This run: surfaced paid cost `$0`; operator minutes required now `0` because the candidate is not admitted to immediate application work.
- If an official future deadline is confirmed: estimated operator preparation burden `180-300 minutes` for a tailored resume, concise project/research proposal, work samples, and references. This is an S08 planning estimate, not a source-backed application requirement.
- Opportunity commitment if admitted: 40 hours/week for four months, per the posting.

## Strongest objection

The role remains on Anthropic's current careers page, the form resolves, and the posting says rolling review; classifying it as non-actionable may discard a valuable late or next-cohort submission.

**Answer:** do not discard it. Keep one watch candidate, but separate `listing reachable` from `deadline open`. A stale or rolling listing cannot support an `APPLY_NOW` claim after the only explicit deadline has passed.

## Falsifier

Any official Anthropic/Constellation page or direct official statement that supplies:

- a future application deadline,
- explicit acceptance of applications after July 26,
- automatic consideration for the next cohort, or
- a newly versioned Fellows posting with a current cohort date.

That evidence would permit re-evaluation from `NEXT_COHORT_WATCH` to `ADMIT`.

## Verification and consumption gate

- Verifier: S09 or another distinct nonproducer must re-open the exact official posting and confirm deadline/listing state.
- Consumer: an exact income-lane WorkItem must explicitly consume this card before any application preparation earns fitness credit.
- Suggested consumer decision: `REVISE — WATCH_NEXT_COHORT; NO_APPLY_NOW`.

## Decision

`REVISE`

Admission ceiling: **high-fit future/watch candidate only; current application acceptance and deadline remain unproven.**
