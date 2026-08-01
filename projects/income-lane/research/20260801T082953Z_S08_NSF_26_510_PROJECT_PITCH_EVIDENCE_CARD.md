---
schema_id: hfo.gen133.s08.research_evidence_card.v1
card_id: S08_NSF_26_510_PROJECT_PITCH_20260801T082953Z
result: ADMIT
callsign_or_seat: S08_RESEARCH_CANDIDATE_SCOUT
carrier_task_id_expected: 6a526109ba348191b5f23ad3172ad568
carrier_task_id_observed: 6a526109ba348191b5f23ad3172ad568
carrier_task_id_match: true
carrier_identity_claim: DISPOSABLE_SCHEDULED_CARRIER_NOT_LINEAGE
controller: operator_direct
wip: 1
valid_time_utc: 2026-08-01T08:29:53Z
transaction_time_utc: SEE_GITHUB_COMMIT_METADATA
canonical_repository: TTaoGaming/hfo-gen-133
canonical_branch: agent/gen133-bootstrap-20260730
research_lane: grants_jobs_income_opportunities
candidate: NSF_SBIR_STTR_Program_Solicitation_26_510_Project_Pitch_to_Phase_I
candidate_contract_version: NSF_26_510_posted_2026-05-22_current_observed_2026-08-01
candidate_next_full_proposal_deadline: 2026-11-04T17:00:00_LOCAL_SUBMITTER
privacy_class: PUBLIC_PRIMARY_SOURCES_AND_SANITIZED_REPOSITORY_POINTERS_ONLY
effect_ceiling: RESEARCH_CARD_AND_SANITIZED_SLACK_POINTER_ONLY
expiry_utc: 2026-08-08T08:29:53Z
verifier: Sigrun/P4_APEX_FALSIFICATION_or_other_distinct_nonproducer
consumer: Garmr/P1_INCOME_LANE_FOR_ONE_NO_SEND_NSF_PROJECT_PITCH_FIT_MATRIX
fitness_credit: ZERO_UNTIL_EXACT_CONSUMER_ACK
sealed: false
---

# S08 evidence card — NSF 26-510 is admissible for one no-send Project Pitch fit matrix, not an application

## Changed queue evidence

The prior S08 card completed the `distribution_and_buyer_evidence` lane at commit `1967da06dcd80f8a295bccf7a9fd872c992595d3`, blob `a0fefe171074c0cc0a6141b90c58678469801598`. The explicit rotation therefore advances to `grants_jobs_income_opportunities`.

The standing Gen-133 income dispatch remains red at `projects/income-lane/garmr_outreach_dispatch.md`, blob `27741e1787083522f802a736abff1de7da1e7f45`: external income is still recorded as `$0`, while all sends and applications remain operator-gated. This card does not displace the active spatial golden-app WIP and does not authorize parallel producer work.

## Bounded question

Does the current NSF `26-510` SBIR/STTR Phase I route justify exactly one no-send qualification matrix for the HFO/spatial total-tool-virtualization program, without asserting eligibility, deep-tech novelty, market demand, or authorizing a Project Pitch or full proposal submission?

## Decision

`ADMIT` the opportunity for **one no-send Project Pitch fit matrix only**.

NSF 26-510 is an active, current funding opportunity for U.S. small businesses developing high-risk technologies into commercial products. A Phase I proposal may request up to `$305,000` for 6–18 months, but a company must first submit a Project Pitch and receive an official invitation. The required pitch is materially smaller than a full proposal and asks for four bounded sections: technology innovation, technical objectives/challenges, market opportunity, and company/team.

The HFO program has possible alignment with NSF's AI topic—safe, reliable, privacy-preserving, adversary-robust and resource-efficient AI systems—and with the broader goal of turning high-risk R&D into market-ready innovations. That is only hypothesis-level fit. Current Gen-133 evidence may still describe integration architecture, workflow governance, and prototypes rather than a defensible high-risk scientific or engineering innovation.

No Project Pitch, registration, account creation, terms acceptance, proposal, outreach, or submission is authorized by this card.

## Self-probe

```yaml
expected_task_id: 6a526109ba348191b5f23ad3172ad568
observed_task_id: 6a526109ba348191b5f23ad3172ad568
task_id_match: true
tools_observed:
  github_connector: authenticated_read_write_and_exact_file_readback
  slack_public_channel: authenticated_read_write
  web_primary_sources: read
  native_task_inventory: not_exposed_in_this_carrier
  gmail_calendar_drive_private_data: not_used
  research_gov_or_nsf_account: not_accessed
  shell_or_browser_runtime: unavailable
  task_mutation: not_called
```

## Exact candidate and dated primary sources

Observed `2026-08-01`:

1. NSF Program Solicitation `NSF 26-510`, posted `2026-05-22`, marked active/current: https://www.nsf.gov/funding/opportunities/small-business-innovation-research-small-business-technology/nsf26-510/solicitation
2. NSF Project Pitch instructions and field limits: https://seedfund.nsf.gov/apply/project-pitch/
3. NSF application process and timing: https://seedfund.nsf.gov/apply/get-started/
4. NSF SBIR/STTR eligibility and requirements: https://seedfund.nsf.gov/solicitation-eligibility/
5. NSF Artificial Intelligence topic: https://seedfund.nsf.gov/topics/artificial-intelligence/
6. NSF Phase I rules, intellectual-property treatment, and award conditions: https://seedfund.nsf.gov/resources/awardees/phase-1/rules-and-regulations/
7. NSF full-proposal process and current deadlines: https://seedfund.nsf.gov/apply/full-proposal/

## Current contract facts supported

- `NSF 26-510` is the current active solicitation and replaced prior solicitations `24-579`, `24-580`, and `24-582`.
- The next listed full-proposal deadline after this observation is `2026-11-04` at 5:00 p.m. in the submitting organization's local time.
- A Phase I proposal may request up to `$305,000` for 6–18 months, subject to availability of funds.
- Phase I applicants must first submit a Project Pitch and receive an official invitation; an invitation is not an award.
- NSF says a Project Pitch normally receives an official response in about one to two months.
- The pitch requests four bounded narratives: technology innovation (up to 3,500 characters), technical objectives/challenges (3,500), market opportunity (1,750), and company/team (1,750).
- The solicitation evaluates intellectual merit, broader impacts, and commercial potential.
- The proposing firm must qualify as a U.S. small-business concern with no more than 500 employees including affiliates. Ownership/control, U.S.-work, PI-employment, research-security, foreign-affiliation, and other eligibility rules apply.
- The PI's primary employment must be with the small business at award and during performance; the solicitation defines primary employment as at least 51% and treats outside employment above 19.6 hours per week as conflicting absent an approved deviation.
- The current solicitation permits at most two Project Pitch submissions per company per 12 months and no more than three for the same project/technology.
- NSF takes no equity. A small business may retain subject-invention ownership, while federal rights, disclosure/registration duties, award conditions, and possible march-in rights remain.
- The NSF AI topic explicitly includes systems intended to be safe, reliable, fair, robust against sophisticated adversaries, privacy preserving, and computationally efficient.

## Supported HFO fit hypotheses

These are candidate pitch themes, not established grant claims:

1. **Technical-risk hypothesis:** whether a digest-bound, effect-ceiling-controlled durable-agent runtime can measurably reduce unauthorized actions and false-green completion under carrier/model variance.
2. **Spatial-access hypothesis:** whether a standardized input-adapter layer can convert low-cost camera/gesture signals into reliable application control across reused software without bespoke application rewrites.
3. **Resource-access hypothesis:** whether intent-to-outcome tool virtualization can provide useful interactive capability on low-cost devices for constrained users.
4. **Evaluation hypothesis:** whether mutation-based negative controls, independent verification, idempotency/version gates, and explicit ConsumerAck can create reproducible safety measurements for autonomous workflows.

A viable Project Pitch must choose exactly one core technical innovation and define measurable R&D uncertainty. Combining all four would likely be too broad and read as a platform vision rather than a Phase I research plan.

## Excluded claims

- No claim that TTao, any company, or any affiliate satisfies U.S. ownership, citizenship/permanent-residency control, employee-count, PI-employment, work-location, tax, registration, research-security, or foreign-affiliation requirements.
- No private corporate, immigration, employment, capitalization, financial, banking, tax, resume, customer, or partner data was inspected.
- No claim that HFO is novel relative to prior art, patentable, production-ready, independently verified, deployed at scale, or already commercialized.
- No claim that workflow receipts, agent prompts, mythology, architecture documents, or same-provider tests alone constitute NSF-grade technical R&D.
- No claim that the spatial golden app has an independent `STOOD`, ConsumerAck, browser proof, customer validation, or market evidence.
- No claim that the November 4 full-proposal deadline is realistically reachable. Project Pitch review alone commonly takes one to two months, and a full proposal requires invitation, company registrations, budgets, personnel documents, support letters, and compliance material.
- No Project Pitch or proposal account was opened; no form, certification, application, or submission was prepared or sent.
- No funding probability, award timing, income timing, or reviewer interest is asserted.

## License, terms, IP, and compliance uncertainty

- NSF states that awardees retain company ownership and may retain subject-invention ownership, but the federal government receives specified license rights and statutory march-in rights can apply.
- Awardees must disclose and register subject inventions through iEdison and comply with the award letter, SBIR/STTR terms, PAPPG, research-security policies, reporting, and national-policy requirements.
- Open-source components, prior repositories, contractor work, generated assets, third-party models, and pre-existing IP must be separated from proposed subject inventions before any application.
- Repository license metadata is not an IP-rights opinion. A future pitch must bind exact source ownership, contributor rights, third-party dependencies, and the boundary between pre-existing work and federally funded R&D.
- Current NSF terms may change before submission; the version effective on the actual due date controls.

## Cost and operator-minute estimate

```yaml
direct_research_cost_usd: 0
operator_minutes_required_now: 0
credentials_or_registration_required_now: 0
estimated_consumer_minutes_for_no_send_fit_matrix: 35_to_60
estimated_operator_minutes_for_private_eligibility_check: 20_to_40
estimated_no_send_project_pitch_draft_minutes_if_admitted: 120_to_240
estimated_operator_review_minutes_before_any_submission: 30_to_60
estimated_later_registration_and_full_proposal_burden: MULTI_HOUR_TO_MULTI_DAY; NOT_MEASURED
estimated_operator_minutes_avoided_by_this_gate: 20_to_45
near_term_income_value: LOW; award_path_is_months_not_days
```

## Strongest objection

This opportunity can become architecture theater and grant-chasing. NSF funds a bounded, high-risk technical innovation with commercial potential, not a sprawling agent institution, a collection of integrations, or a general vision. Gen-133 currently has incomplete independent verification and zero external income receipts. Spending scarce operator time on a federal pitch before isolating one falsifiable technical risk, one buyer, and one conventional proof artifact could delay nearer-term job, client, or product revenue while still producing no funding.

## Falsifier

`RETIRE` this candidate for the current cycle if any one of these holds after private operator review:

1. the company, ownership/control, PI-employment, U.S.-work, employee-count, or research-security requirements are not satisfied;
2. a Project Pitch, invitation, or Phase I proposal is already pending and the submission limits block another;
3. the proposed work is primarily software integration, consulting, application development, packaging, or routine engineering rather than high-risk technical R&D;
4. no single technical uncertainty can be expressed with a measurable Phase I experiment and a credible advance over existing solutions;
5. no specific customer or beneficiary and commercial pathway can be supported without invented demand;
6. exact IP and contributor provenance cannot be separated into pre-existing and proposed R&D;
7. the operator's current priority requires income within weeks rather than a months-long grant path.

`REVISE` rather than retire when eligibility is plausible but the innovation is too broad, market evidence is missing, or the proof artifact must first be reduced to a conventional runnable slice.

## Reversible next experiment

The named consumer may create one no-send fit matrix, not an application. It must contain:

- each load-bearing eligibility rule marked `VERIFIED_PRIVATE`, `MISSING`, or `DISQUALIFYING`, with no private values copied to Git or Slack;
- one sentence naming the single proposed technical innovation;
- one baseline, one technical risk, one Phase I experiment, one falsifier, and one measurable result;
- one specific customer/beneficiary class plus direct evidence or `MISSING_DEMAND_EVIDENCE`;
- exact pre-existing IP and open-source boundaries;
- a realistic calendar working backward from Project Pitch response time and the `2026-11-04` full-proposal deadline;
- operator burden and opportunity cost versus one job/client/product lane;
- a stop decision: `DRAFT_NO_SEND_PITCH | DEFER | RETIRE`.

The matrix must stop before creating an NSF/Research.gov account, accepting terms, entering private data, contacting NSF, or submitting anything. It must bind this card's exact Git commit/path/blob after readback.

## Verifier, consumer, expiry, and credit

- **Verifier:** Sigrun/P4 or another distinct nonproducer should challenge whether the proposed innovation is truly high-risk R&D, whether demand is invented, and whether the grant opportunity dominates nearer-term income work.
- **Consumer:** Garmr/P1 may produce exactly one sanitized no-send fit matrix. TTao/operator alone controls private eligibility disclosure and every application or submission effect.
- **Expiry:** `2026-08-08T08:29:53Z`; revalidate the active solicitation, Project Pitch rules, and deadlines after expiry.
- **Credit:** zero until a named WorkItem records `CONSUMED` or `REJECTED_WITH_EVIDENCE` against the exact Git blob.

## Honest flaw

This carrier read current official NSF sources and public Gen-133 artifacts only. It did not inspect company eligibility, existing Project Pitch status, private IP ownership, citizenship or residency, employment, registrations, customer interviews, patents/prior art, financial capacity, proposal workload, or reviewer feedback. The fit may collapse once the project is translated from broad system language into one technical innovation. The November deadline may be impractical given the stated one-to-two-month Project Pitch response window. This card produces no income and no funding by itself.
