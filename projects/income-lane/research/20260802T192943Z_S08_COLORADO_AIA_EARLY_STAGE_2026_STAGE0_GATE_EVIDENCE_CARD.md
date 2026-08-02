---
schema_id: hfo.gen133.s08.research_evidence_card.v1
seat: S08_RESEARCH_AND_CANDIDATE_SCOUT
carrier_task_id_expected: 6a526109ba348191b5f23ad3172ad568
carrier_task_id_observed: 6a526109ba348191b5f23ad3172ad568
carrier_task_id_match: true
wip: 1
valid_time_utc: 2026-08-02T19:29:43Z
transaction_time_utc: SEE_GITHUB_COMMIT_METADATA
canonical_repository: TTaoGaming/hfo-gen-133
canonical_branch: agent/gen133-bootstrap-20260730
lane: grants_jobs_income_opportunities
question_changed_from: amazon_appstore_distribution_boundary_then_explicit_lane_rotation_advanced
candidate_program: Colorado OEDIT Advanced Industries Early-Stage Capital and Retention Grant
candidate_cycle: 2026_JULY_AUGUST
candidate_deadline: 2026-08-27T17:00:00-06:00
candidate_deadline_utc: 2026-08-27T23:00:00Z
decision: REVISE
headline: REVISE_TO_STAGE0_ELIGIBILITY_AND_MATCH_GATE_NOT_FULL_APPLICATION
fitness_credit: 0
sealed: false
expiry_utc: 2026-08-09T19:29:43Z
immediate_expiry_on:
  - production_OEDIT_page_or_portal_disagrees_with_preview_source
  - deadline_or_program_terms_change
  - exact_project_or_applicant_entity_changes
  - source_page_or_application_route_closes
  - exact_workitem_consumer_change
---

# S08 evidence card — Colorado AIA Early-Stage Capital and Retention Grant, summer 2026

## Self-probe and changed question

- Native task inventory returned active task `6a526109ba348191b5f23ad3172ad568`; expected and observed IDs match.
- Used: native task readback, authenticated GitHub read/write/readback, current official Colorado OEDIT web sources, and Slack pointer after Git readback.
- Not used: private company records, Secretary of State account data, financial statements, bank balances, resumes, application portal, account creation, terms acceptance, outreach, application, submission, spend, deployment, publication, merge, or task mutation.
- The prior S08 wake completed `distribution_and_buyer_evidence`; explicit lane rotation advances to `grants_jobs_income_opportunities`.

## Bounded question

Should the current Colorado OEDIT `Advanced Industries Early-Stage Capital and Retention Grant` become an immediate full application WorkItem for the Spatial App Factory / AI software lane, or only a bounded stage-0 eligibility and matching-capital gate?

## Exact current primary sources — observed 2026-08-02

1. Colorado OEDIT official preview page, exact program and 2026 cycle: https://oedit.nxt-dev.colorado.gov/advanced-industries-early-stage-capital-retention-grant
2. Colorado OEDIT official preview program index: https://oedit.nxt-dev.colorado.gov/advanced-industries-accelerator-programs
3. Colorado OEDIT production program index, older searchable snapshot: https://oedit.colorado.gov/advanced-industries

Source caveat: the carrier could not fetch the production exact-program URL because it returned HTTP 403 to the research surface. The current deadline and detailed rules came from the `oedit.nxt-dev.colorado.gov` official-state preview hostname, crawled within five days. Production portal confirmation remains `UNKNOWN` and is a required pre-application gate.

## Supported claims

- `CURRENT_CYCLE_SIGNAL`: the current official OEDIT preview says the application is open and due **August 27, 2026 at 5:00 PM Mountain Time**.
- `AWARD_CEILING`: the page states up to `$250,000` per project, with a possible lift to `$500,000` for a project that materially impacts more than one advanced industry.
- `MATCH_BURDEN`: the program requires a **2-to-1 company-to-State cash match**. A `$50,000` request implies `$100,000` in non-State cash; a `$250,000` request implies `$500,000`.
- `CONDITIONAL_MATCH_PATH`: an otherwise eligible company may apply without dedicated matching funds, but a conditional award requires the match to be obtained within six months or the award is forfeited.
- `ENTITY_AND_LOCATION_GATE`: the business must be registered and in Good Standing with the Colorado Secretary of State, and must be headquartered in Colorado or have at least 50% of employees in Colorado.
- `SIZE_GATE`: the page states fewer than `$20 million` received from grants and third-party investors since inception and annual revenue below `$10 million`.
- `TECHNOLOGY_MATURITY_GATE`: the project must be beyond idea-only status and show proof of concept/proof of principle, valid IP or trade secrets, a completed prototype, technical validation, a commercialization plan, a market assessment confirming an opportunity, and initial startup activity.
- `DISRUPTION_GATE`: OEDIT defines disruptive technology as a significant departure from currently available industry technology; merely using currently available components does not establish significant impact.
- `PROCESS_BURDEN`: the application includes pre-qualification, a full application, supporting business and financial documents, scored technology/business/management/Colorado-benefit sections, and potentially pitch training and a committee pitch.
- `PAYMENT_TIMING`: the program is a reimbursement grant. A formal grant agreement must be executed before grant funds may be spent.
- `ACCOUNT_LEAD_TIME`: the program says new application-portal users are manually added and activation may take several days.

## Excluded claims

- No claim that TTao, any current company, or the Spatial App Factory is eligible.
- No claim that a FOSS reskin, retheme, input adapter, app catalog, or generic AI-agent workflow is itself a qualifying disruptive technology.
- No claim that the operator has a Colorado entity in Good Standing, eligible headquarters or employee distribution, acceptable revenue/funding history, valid project-owned IP or trade secrets, a completed grant-grade prototype, technical validation, a market assessment, business financials, customer evidence, support letters, or matching cash.
- No claim that a working demo equals OEDIT proof of commercial viability or market need.
- No claim that an application would be competitive, approved, paid, profitable, or faster than customer-funded work.
- No application portal account, pre-qualification, application, pitch, grant agreement, award, reimbursement, or ConsumerAck exists.

## License, terms, and privacy uncertainty

- This is a public grant program, not a software-license candidate; software-license classification is not applicable.
- Any FOSS components used in a proposed project would still need exact license, attribution, provenance, and project-IP boundaries. The grant page's reference to valid IP and trade secrets does not convert third-party FOSS into applicant-owned IP.
- The exact application-portal privacy terms, attestations, data-retention rules, Colorado Special Provisions, grant agreement, audit duties, reimbursement mechanics, and any repayment/clawback terms were not fully inspected or accepted.
- Required application materials include private company, personnel, and financial information. None was accessed or externalized.
- The production exact-program page and application portal were not directly readable from this carrier; deadline and current-cycle status need production readback before operator work begins.

## Decision

`REVISE` this opportunity from **immediate full application** to a single stage-0 WorkItem:

`COLORADO_AIA_ESCR_2026_STAGE0_ELIGIBILITY_AND_MATCH_GATE`

The gate should answer only whether one exact Colorado entity and one exact project can truthfully satisfy the entity, location, disruptive-technology, maturity, IP, commercialization, private-document, deadline, and 2-to-1 matching-capital requirements. Do not draft a full grant application until the gate is consumed and passes.

For the current Spatial App Factory thesis, a reskin/retheme/catalog proposition is not enough by itself. A successor would need to identify a defensible technical innovation and prove why it is a significant departure from available technology, not merely a new packaging or distribution layer.

## Cost and operator-minute estimate

- This research card: `$0` direct spend; approximately `12–18` carrier minutes; `0` operator minutes.
- Stage-0 gap matrix: estimated `25–45` consumer minutes plus `15–25` operator minutes for private yes/no attestations and source pointers.
- Production page/portal confirmation: estimated `5–10` operator or authorized consumer minutes; account creation is not included.
- Full application after a passed gate: likely multi-hour work with substantial private-document and operator review burden; exact hours remain `UNKNOWN` until the live form and one project are bound.
- Capital exposure is not an application fee but the required non-State cash match: exactly `2x` the requested State amount at execution, subject to conditional-award rules.

## Strongest objection

The deadline is still more than three weeks away, the program offers up to `$250,000`, and OEDIT explicitly allows otherwise eligible companies to apply before matching cash is fully secured. Waiting for perfect readiness could forfeit a valuable non-dilutive funding cycle.

**Response:** that supports a rapid stage-0 gate, not an unbounded application. The current public record still requires a disruptive proprietary project, a completed and validated prototype, commercialization and market evidence, private financial documentation, and a credible path to a 2-to-1 cash match. Starting prose before those bindings are true would create application theater and operator debt.

## Falsifier

Revise this verdict toward `ADMIT_FULL_APPLICATION` only if all of the following are bound to one exact project before expiry:

1. the production OEDIT page or live portal confirms the August 27, 2026 deadline and current requirements;
2. a named Colorado entity is verified as registered, in Good Standing, and location-eligible;
3. the project has a completed prototype plus technical validation;
4. the project demonstrates a significant technical departure beyond ordinary use, integration, reskinning, or retheming of available FOSS/AI components;
5. valid IP, trade-secret, and third-party-license boundaries are documented;
6. a commercialization plan and actual market-assessment evidence exist;
7. required private financial and personnel documents are available for operator-authorized use;
8. a requested grant amount and truthful `2x` non-State cash-match path are selected;
9. a named consumer accepts the application workload and deadline risk.

Retire the current cycle if production readback contradicts the preview deadline, the project cannot pass the disruption/maturity gate, or the private-document and matching-capital burden cannot be supported without invented claims.

## Verifier

- Structural: `S04_STRUCTURAL_PREFLIGHT_VERIFIER` may verify exact task, source, deadline, program, decision, expiry, and card-byte bindings with same-provider binding weight `0`.
- Strategic: `S09_STRATEGIC_REASONING_AND_VOTING` should test opportunity cost against customer-funded work, current job packets, and other grants.
- Binding eligibility requires operator-authorized private evidence and current production OEDIT/portal readback. S08 cannot establish it.

## Consumer

- Immediate: `S09_STRATEGIC_REASONING_AND_VOTING` and the income-lane backlog owner.
- Suggested exact WorkItem: `COLORADO_AIA_ESCR_2026_STAGE0_ELIGIBILITY_AND_MATCH_GATE`.
- Success condition: one evidence-backed `PASS_STAGE0 | FAIL_STAGE0 | HOLD_PRIVATE_EVIDENCE` tied to a named entity and project.
- Fitness remains `0` until an exact WorkItem records ConsumerAck against this card's commit/path/blob.

## Honest flaw

The most current detailed source was an official Colorado state **preview/development hostname**, not a successful production-page or portal readback. The public production index visible to search was stale and the exact production page returned HTTP 403 to this carrier. The August 27, 2026 deadline is therefore a strong current signal, not yet a production-confirmed fact. This card also cannot evaluate actual eligibility without private company, financial, IP, prototype, and market evidence that this role is forbidden to access.
