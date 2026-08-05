---
schema_id: hfo.gen133.s08.research_evidence_card.v1
seat: S08_RESEARCH_AND_CANDIDATE_SCOUT
carrier_task_id_expected: 6a526109ba348191b5f23ad3172ad568
carrier_task_id_observed: 6a526109ba348191b5f23ad3172ad568
carrier_task_id_match: true
wip: 1
valid_time_utc: 2026-08-05T02:28:35Z
transaction_time_utc: SEE_GITHUB_COMMIT_METADATA
canonical_repository: TTaoGaming/hfo-gen-133
canonical_branch: agent/gen133-bootstrap-20260730
lane: grants_jobs_income_opportunities
question_changed_from: itch_purchase_counter_buyer_and_refund_semantics
candidate_employer: Close
primary_candidate_role: Senior Backend Engineer - Agents
primary_candidate_posting_id: 29f5c695-8282-4407-ac09-2b61b9f2fc1e
alternate_candidate_role: Senior Software Engineer - Backend
alternate_candidate_posting_id: 01fc4ad7-4d33-4f64-919f-502bb2c20efc
decision: REVISE
headline: ONE_CLOSE_APPLICATION_PRIMARY_AGENTS_ROLE_GENERIC_BACKEND_FALLBACK_ONLY
fitness_credit: 0
sealed: false
consumer: CLOSE_AGENTS_2026_TRUTH_BOUND_APPLICATION_PACKET_001
expiry_utc: 2026-08-12T02:28:35Z
immediate_expiry_on:
  - primary Agents posting closes or materially changes
  - Close publishes a documented multiple-application or generic-pool routing policy
  - an authorized Close representative directs the candidate to the generic posting
  - the generic posting adds a materially lower and truthful qualification route
  - named consumer changes
---

# S08 evidence card — Close duplicate-application routing gate

## Self-probe and changed question

- Expected and observed carrier IDs match: `6a526109ba348191b5f23ad3172ad568`.
- Native task inventory exposed the expected enabled S08 carrier; no task state was mutated.
- Exposed surfaces used: authenticated GitHub search/read/write/readback, public Slack read/pointer, and current public web research.
- Prior S08 wake completed `distribution_and_buyer_evidence`; explicit rotation advances to `grants_jobs_income_opportunities`.
- Repository search found no prior S08 card for exact alternate posting ID `01fc4ad7-4d33-4f64-919f-502bb2c20efc`.

## Bounded uncertainty

Does Close's current broad Backend posting justify a second application packet or replace the already-admitted Agents-specific posting, given the exact public MCP portfolio and the unresolved production-history gap?

## Exact candidates and dated primary sources

Observed `2026-08-05`:

1. Close official Ashby posting, Agents UUID `29f5c695-8282-4407-ac09-2b61b9f2fc1e`: https://jobs.ashbyhq.com/Close/29f5c695-8282-4407-ac09-2b61b9f2fc1e
2. Close official Ashby posting, generic Backend UUID `01fc4ad7-4d33-4f64-919f-502bb2c20efc`: https://jobs.ashbyhq.com/close/01fc4ad7-4d33-4f64-919f-502bb2c20efc
3. Close official careers and hiring-process surface: https://www.close.com/careers
4. Prior exact S08 admission card for the Agents posting, commit `7090660200e57ba53bc0295afc4cc4ed58b5d677`, blob `b2d298cba5bf9620167c71cb55342db3f915034e`: https://github.com/TTaoGaming/hfo-gen-133/blob/7090660200e57ba53bc0295afc4cc4ed58b5d677/projects/income-lane/research/20260804T212704Z_S08_CLOSE_AGENTS_MULTI_LEVEL_TRUTH_BOUND_APPLICATION_GATE_EVIDENCE_CARD.md

## Supported claims

- The Agents-specific posting directly names MCP integrations, agent orchestration, eval and observability work, pause and recovery semantics, prevention of latent calls, and cost-aware model routing.
- The Agents-specific posting explicitly describes calibration across Software Engineer, Senior, and Staff levels rather than requiring the applicant to assert a level in advance.
- The generic Backend posting permits an applicant to express interest in Agents, Communications, CRM, or Growth, but its current public text still asks for shipped LLM-backed features to real users, internet-facing API operation, and battle-tested production incidents.
- The current generic posting does not establish a lower production-history bar or the same explicit multi-level calibration route.
- Close's official hiring surface describes a potentially material follow-on assessment burden; this raises the cost of duplicate speculative packets without proving a corresponding benefit.
- The exact MCP portfolio remains more directly legible against the Agents-specific vocabulary than against the broad Backend pool.

## Excluded claims

- No claim that the two postings share one requisition, applicant record, reviewer, interview loop, or assessment.
- No claim that Close penalizes, merges, deduplicates, or prefers multiple applications; no public duplicate-application policy was found.
- No claim that either role is guaranteed open beyond the observation time, or that the generic posting supersedes the Agents posting.
- No claim that an application has been submitted, reviewed, rejected, or advanced for either posting.
- No claim that the operator satisfies private work-authorization, chronology, production-user, incident-response, or reference requirements.
- No claim that a scheduled email, draft, or prepared packet equals an application.

## License, terms, and privacy uncertainty

- No ATS account, application form, privacy consent, candidate attestation, assessment terms, or retention terms were opened or accepted during this pass.
- Close's handling of multiple applications and cross-role candidate routing remains undocumented in the sources inspected.
- Close states that AI assistance is expected but applications that read as fully AI-generated will not be considered. Final facts and prose therefore require operator authorship and review.
- Existing public portfolio license and dependency-chain uncertainty remains unchanged from the prior Agents card; this card does not reopen that audit.

## Decision

`REVISE` the existing consumer packet as follows:

`ONE_CLOSE_APPLICATION_PRIMARY_AGENTS_ROLE_GENERIC_BACKEND_FALLBACK_ONLY`

- Keep exact posting `29f5c695-8282-4407-ac09-2b61b9f2fc1e` as the primary Close target.
- Do not create or send a separate application for generic posting `01fc4ad7-4d33-4f64-919f-502bb2c20efc` from current evidence.
- Retain the generic posting only as a fallback if the Agents posting closes or materially changes, or if Close explicitly routes the candidate to the broad pool.
- Do not interpret this routing decision as proof of qualification, submission authority, or employer preference.

This revision reduces duplicate packet and review burden while preserving the higher-signal target. It does not assert that duplicate applications are harmful; their benefit is simply not evidenced.

## Cost and operator-minute estimate

- This evidence card: `$0` direct spend; approximately `12-18` carrier minutes; `0` operator minutes.
- Existing packet amendment: `5-10` consumer minutes; `0-5` operator minutes during the already-required review.
- Avoided duplicate preparation estimate: `15-30` consumer minutes plus `10-20` operator minutes.
- A later skills assessment may require several hours if the application advances; whether separate postings create separate assessments is `UNKNOWN`.

## Strongest objection

A broad Backend application could let Close route the candidate across several teams and may increase the chance of finding a lower-level fit.

**Response:** the current public generic posting does not document a lower-level route and retains the same decisive missing evidence: real-user LLM delivery and battle-tested production operation. The Agents posting has more exact portfolio overlap and explicit multi-level calibration. A second packet therefore adds known effort and ambiguity without evidenced incremental access.

## Falsifier

- `ADMIT` the generic posting separately if Close publishes or communicates that candidates should apply to multiple roles, that the generic pool is the preferred routing surface, or that it offers a materially lower truthful qualification route.
- `REVISE` the primary target if the Agents posting closes, materially changes, or stops exposing multi-level calibration.
- `RETIRE` the generic fallback if Close states that duplicate or cross-role applications are not considered, or if its role requirements materially diverge from the verified portfolio.
- `UNKNOWN` remains appropriate if the two forms expose materially different questions but no authorized comparison can be made without account or terms interaction.

## Verifier

- `S04_STRUCTURAL_PREFLIGHT_VERIFIER`: bind both posting IDs and URLs, prior card commit/blob, current card bytes, task ID, branch, decision, consumer, and expiry; same-provider binding weight `0`.
- `S09_STRATEGIC_REASONING_AND_VOTING`: compare one-target focus against speculative multi-role reach and operator burden.
- Operator: verify private chronology and authorize any final target or submission; no agent may infer consent from a draft or scheduled message.

## Consumer and expiry

- Consumer: `CLOSE_AGENTS_2026_TRUTH_BOUND_APPLICATION_PACKET_001`.
- Required result: amend the packet with `PRIMARY_POSTING_ID`, `FALLBACK_POSTING_ID`, and `NO_DUPLICATE_APPLICATION_WITHOUT_NEW_PRIMARY_EVIDENCE`.
- Expiry: `2026-08-12T02:28:35Z`, or immediately on a listed material change.
- Fitness remains `0` until an exact WorkItem records consumption and ConsumerAck.

## Honest flaw and effect ledger

No authenticated ATS form or employer duplicate-application policy was inspected, so this is an expected-value routing decision under public evidence, not a statement about Close's internal recruiting behavior. Search-indexed public job text can change without notice. No task mutation, account creation, terms acceptance, outreach, application, purchase, send, spend, deployment, merge, publication, private-data use, or demand invention occurred.
