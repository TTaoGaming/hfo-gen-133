---
schema_id: hfo.gen133.s08.evidence_card.v0_1
seat: S08
callsign: Research and Candidate Scout
expected_task_id: 6a526109ba348191b5f23ad3172ad568
wip: 1
created_utc: 2026-08-02T09:32:00Z
canonical_repo: TTaoGaming/hfo-gen-133
canonical_branch: agent/gen133-bootstrap-20260730
lane: grants_jobs_income_opportunities
question: Is Anthropic Research Operations, External Artifacts job 5208278008 an honest fully remote United States candidate for a Colorado-based operator?
result: REVISE
fitness_credit: 0
consumer:
  - S09 income-candidate triage
  - income-lane backlog owner
verifier: distinct nonproducer current-source reviewer
expiry: 2026-08-09T09:32:00Z or immediately on official posting or application-form change
privacy_class: SANITIZED_PUBLIC
world_effect_ceiling: public-source read + one Git evidence card + one Slack pointer
---

# S08 evidence card — Anthropic Research Operations external-artifacts hybrid boundary

## Self-probe

- Carrier identity: S08 Research and Candidate Scout; expected task ID `6a526109ba348191b5f23ad3172ad568` came from the wake packet and was not independently exposed by the connector surface.
- Tools used: GitHub exact-branch search/read/write/readback, public web read of official Anthropic/Greenhouse pages, and one bounded Slack pointer.
- Duplicate check: no exact Gen-133 card matched Greenhouse job `5208278008`; broad phrase matches were unrelated to this named job.

## Exact candidate

- Organization: Anthropic
- Role: **Research Operations, External Artifacts**
- Greenhouse job ID: `5208278008`
- Official posting: https://job-boards.greenhouse.io/anthropic/jobs/5208278008
- Public location label: `Remote-Friendly, United States`
- Posted annual salary range: `$260,000-$310,000 USD`

## Bounded finding

**REVISE the candidate from `FULLY_REMOTE_US_APPLY_NOW` to `HYBRID_25_PERCENT_FIT_TRIAGE`.**

The exact posting was live with an application form on 2026-08-02 and labels the role `Remote-Friendly, United States`. However, its logistics section says Anthropic currently expects all staff to be in an office at least **25% of the time**, with some roles requiring more. The application separately requires an answer about willingness to work in person 25% of the time, asks whether the candidate is open to relocation, and asks for the address from which the candidate plans to work.

Therefore the public `Remote-Friendly` label does not support a fully remote Colorado-work claim. The posting does not state which office would bind this role, how the 25% is scheduled, whether travel is acceptable instead of relocation, or whether travel/relocation costs are covered. Keep the job as a high-value fit-triage candidate only if the operator is willing to resolve that location burden before spending substantial application time.

## Dated primary/current sources

1. Anthropic Greenhouse job `5208278008`, read 2026-08-02: role status, location label, responsibilities, qualifications, compensation, hybrid policy, education, visa statement, and application questions. https://job-boards.greenhouse.io/anthropic/jobs/5208278008
2. Anthropic candidate AI-use guidance, last updated 2025-07-10 and read 2026-08-02: candidates should create first drafts themselves, may use AI to refine authentic material, must not invent experience, and should not use AI during assessments or live interviews unless explicitly permitted. https://www.anthropic.com/candidate-ai-guidance

## Supported claims

- The exact job page and application form were publicly reachable on 2026-08-02.
- The role is publicly labeled `Remote-Friendly, United States`, but the same posting states a company expectation of at least 25% office time.
- The application form explicitly asks about 25% in-person work, relocation openness, and planned work address.
- The stated minimum education is a bachelor's degree or equivalent education, training, and/or experience; no fixed numeric minimum years is published on the page.
- The role requires demonstrated technical writing, baseline LLM fluency, ability to inspect evaluation evidence and technical arguments, and a record of completing complex multi-contributor work against hard deadlines.
- Preferred evidence includes AI-safety or threat-modeling familiarity, safety/compliance documentation, long-form technical publications, and polished document production.
- The listed annual salary range is `$260,000-$310,000 USD`.

## Excluded claims

- No claim that this is a fully remote role from Colorado.
- No claim that quarterly travel, temporary visits, or another arrangement satisfies the 25% office expectation.
- No claim about the assigned office, cadence, travel reimbursement, relocation package, or exception policy; the posting does not resolve them.
- No claim that the operator meets the education, experience, writing, coordination, or portfolio bar.
- No claim that internal HFO receipts are suitable public writing samples or that confidential/private material may be submitted.
- No claim of interview probability, offer probability, start date, or near-term income.
- No application, account creation, résumé upload, outreach, terms acceptance, reference contact, relocation commitment, or private-data use occurred.

## License / terms uncertainty

- Software license: not applicable.
- Greenhouse applicant privacy terms, data-retention rules, background/reference checks, relocation terms, and any employment agreement were not accepted or fully audited.
- Anthropic's published AI guidance permits refinement of a candidate-authored first draft, but rejects invented experience and generally bars AI during take-home or live assessment stages unless Anthropic explicitly allows it. Any future application WorkItem must preserve that authorship boundary.

## Cost and operator-minute estimate

- This research run: surfaced paid cost `$0`; operator minutes required now `0`.
- Honest first gate: `10-15 operator minutes` to decide whether 25% office presence/possible relocation is acceptable. This is an S08 planning estimate, not an employer-stated requirement.
- If accepted for preparation: estimated `150-240 operator minutes` to select non-private writing evidence, map experience to the minimum qualifications, produce an authentic first draft of the required 200-400 word `Why Anthropic?` response, and review the application. This is a planning estimate, not a success forecast.
- Office/travel cost remains `UNKNOWN`; the posting does not provide enough information to estimate it honestly.

## Strongest objection

The salary and topical fit are unusually strong, Anthropic explicitly encourages interested candidates not to self-reject, and waiting to resolve every logistics detail before applying may lose a live opportunity.

**Answer:** preserve the candidate, but do not launder `Remote-Friendly` into `fully remote`. A bounded fit-triage WorkItem can first decide the 25% office constraint and identify one authentic, non-private long-form artifact. Without both, application work risks becoming high-effort speculation.

## Falsifier

Any official Anthropic source or recruiter-authored clarification bound to this exact job that confirms one of the following would change the classification:

- Colorado-based fully remote work with no regular office requirement;
- a named office/cadence and acceptable travel arrangement the operator accepts;
- an exception that removes the 25% requirement for this role; or
- closure/removal of job `5208278008`, which would retire the candidate.

## Verification and consumption gate

- Verifier: S09 or another distinct nonproducer reopens the exact posting and confirms the location label, 25% policy, required application questions, and live status.
- Consumer: an exact income-lane WorkItem must explicitly consume this card before preparation earns fitness credit.
- Suggested first WorkItem: `ANTHROPIC_5208278008_HYBRID_AND_PUBLIC_WRITING_SAMPLE_FIT_TRIAGE` with no application submission authority.
- Admission gate: operator accepts the unresolved office/relocation burden **and** identifies at least one authentic, non-private artifact demonstrating technical writing or multi-contributor delivery.

## Decision

`REVISE`

Admission ceiling: **live, high-compensation candidate for hybrid/logistics and evidence-fit triage only; not verified fully remote, not application-ready, and not income evidence.**
