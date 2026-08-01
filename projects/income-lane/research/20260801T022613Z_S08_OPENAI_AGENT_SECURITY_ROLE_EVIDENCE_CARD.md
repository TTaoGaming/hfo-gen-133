---
schema_id: hfo.gen133.s08.research_evidence_card.v1
card_id: S08_OPENAI_AGENT_SECURITY_ROLE_20260801T022613Z
result: ADMIT
callsign_or_seat: S08_RESEARCH_CANDIDATE_SCOUT
carrier_task_id_expected: 6a526109ba348191b5f23ad3172ad568
carrier_task_id_observed: 6a526109ba348191b5f23ad3172ad568
carrier_task_id_match: true
carrier_identity_claim: DISPOSABLE_SCHEDULED_CARRIER_NOT_LINEAGE
controller: operator_direct
wip: 1
valid_time_utc: 2026-08-01T02:26:13Z
transaction_time_utc: SEE_GITHUB_COMMIT_METADATA
canonical_repository: TTaoGaming/hfo-gen-133
canonical_branch: agent/gen133-bootstrap-20260730
research_lane: grants_jobs_income_opportunities
candidate_organization: OpenAI
candidate_role: Security Engineer, Agent Security
candidate_location: San Francisco and Remote - US
candidate_application_id: e9bea775-7eb6-438a-ab96-27d5f941e69d
candidate_contract_version: official_openai_careers_observed_2026-08-01
privacy_class: PUBLIC_PRIMARY_SOURCES_AND_SANITIZED_REPOSITORY_POINTERS_ONLY
effect_ceiling: FILE_AND_SANITIZED_SLACK_POINTER_ONLY
expiry_utc: 2026-08-03T02:26:13Z
verifier: Sigrun/P4_APEX_FALSIFICATION_or_other_distinct_nonproducer
consumer: Garmr/P1_INCOME_LANE_FOR_ONE_NO_SEND_QUALIFICATION_PACKET
sealed: false
---

# S08 evidence card — OpenAI Security Engineer, Agent Security

## Changed queue evidence

The prior S08 card completed the `distribution_and_buyer_evidence` lane at commit `dd1cff05440d2d60956c996161bd64e093e8cbad`. The explicit lane rotation now advances to `grants_jobs_income_opportunities`.

The standing Gen-133 income dispatch remains materially red:

- `projects/income-lane/garmr_outreach_dispatch.md`
- branch blob: `27741e1787083522f802a736abff1de7da1e7f45`
- declared liveness metric: external income remains `$0` with zero external receipts
- effect ceiling: file plus draft; every send or application submission remains operator-gated

A current official OpenAI listing now supplies one concrete, non-invented opportunity to evaluate. This does not displace `SPATIAL_FACTORY_GOLDEN_APP_001`; it is research-only until a consumer explicitly admits a later no-send packet.

## Bounded question

Is OpenAI's current `Security Engineer, Agent Security` role sufficiently aligned with the public HFO work to justify exactly one no-send qualification and proof-artifact packet, without claiming that TTao satisfies the production-security bar or authorizing an application?

## Decision

`ADMIT` the role as one **candidate opportunity for a no-send qualification packet only**.

The official role is current, accepts Remote-US candidates, and explicitly seeks security controls for agentic systems, sandboxing, policy enforcement, agent-infrastructure hardening, monitoring pipelines, and AI/ML security. Those problem statements overlap materially with HFO's public work on effect ceilings, carrier/actor separation, policy-like refusal contracts, bounded execution, false-green mutation testing, digest-bound receipts, and independent-verification gates.

The overlap is conceptual and artifact-level, not proof that the applicant meets the role. Garmr must not draft or submit an application until private resume evidence is checked against the load-bearing production requirements.

## Self-probe

```yaml
expected_task_id: 6a526109ba348191b5f23ad3172ad568
observed_task_id: 6a526109ba348191b5f23ad3172ad568
task_id_match: true
tools_observed:
  github: read_write
  slack: read_write
  web_primary_sources: read
  gmail_calendar_drive_private_data: not_used
  shell_or_browser_runtime: unavailable
  native_task_mutation: not_called
```

## Exact candidate and dated primary sources

Observed on `2026-08-01`:

1. OpenAI official role page, `Security Engineer, Agent Security`: https://openai.com/careers/security-engineer-agent-security-san-francisco/
2. OpenAI official careers search, where the role appears as an active listing with an `Apply now` route: https://openai.com/careers/search/?q=agent
3. Official application route surfaced by OpenAI, Ashby application ID `e9bea775-7eb6-438a-ab96-27d5f941e69d`: https://jobs.ashbyhq.com/openai/e9bea775-7eb6-438a-ab96-27d5f941e69d/application
4. Gen-133 `CARRIER_CONTRACT.md`, exact branch blob `26e78ac3fedfa4c49cb4285a9c81426a2b13f84b`, as a public example of authority ceilings, actor/carrier separation, refusal sets, receipt requirements, and no-self-verification discipline.
5. Gen-133 quarantined false-green negative control at commit `81d9af9c67eeb2152e99ba0e51476f0db05f9ad1`, blob `9f111f4f4abef8f75803d9bafb9e513d125cde4f`, as an example of mutation-based testing for fabricated ConsumerAck and digest-bound provenance.

## Official role facts supported by the current source

- Location is listed as `San Francisco and Remote - US`.
- Compensation is listed as `$234.4K–$385K + equity`.
- The team secures agentic AI systems and user/customer data against agent-specific risks.
- Responsibilities include identity-, network-, and runtime-level defenses, including sandboxing and policy enforcement.
- The role requires production-grade security tooling and safety-monitoring pipelines across agent executions.
- Stated qualifications include strong Python or systems-language engineering, secure high-reliability service experience, isolation/container/kernel security, network security, identity-based controls, large-scale telemetry, cloud security, and familiarity with AI/ML security.
- The application route was present when observed; the official page did not expose a closing deadline in the readable content, so availability must be revalidated immediately before any packet is prepared.

## Public HFO alignment that may be useful in a qualification packet

The following are possible proof-artifact themes, not verified applicant qualifications:

1. **Agent authority and confused-deputy controls** — effect ceilings, operator-only actions, no authority from repository text, and explicit refusal sets in `CARRIER_CONTRACT.md`.
2. **Identity and provenance** — actor/carrier separation, exact task binding, source-digest binding, idempotency, and ConsumerAck provenance.
3. **False-green resistance** — quarantined negative controls for task-ID mismatch, actor/carrier conflation, stale source digests, duplicate versions, and fabricated acknowledgements.
4. **Human-in-the-loop safety** — no-send/no-spend/no-deploy boundaries, named consumers, explicit approvals, rollback, expiry, and honest-flaw fields.
5. **Agent observability concepts** — Git-first immutable receipts, Slack pointers, exact commands/exit-code requirements, and same-provider verification weight zero.

These artifacts could support a concise technical case study only after they are packaged as ordinary engineering language with runnable evidence and without private or mythic identity material.

## Excluded claims

- No claim that TTao meets the role's production-security, container/kernel, network, cloud, telemetry, or high-reliability-service requirements.
- No claim of staff level, years of experience, work authorization, location eligibility, compensation fit, interview readiness, or cultural fit.
- No resume, LinkedIn profile, private portfolio, employment history, references, or application answers were inspected.
- No claim that Gen-133 is production software, independently verified, deployed at scale, or accepted by an external customer.
- No claim that HFO's public repository is currently suitable to send to a recruiter without cleanup and packaging.
- No application account was created, no form fields or applicant privacy terms were completed, and no application was submitted.
- No buyer response, recruiter interest, interview, offer, income, or ConsumerAck exists.

## License, terms, and privacy uncertainty

- The OpenAI role page links an applicant privacy policy, but the full ATS form and all application-specific terms were not inspected because the application UI requires JavaScript.
- The role can close or change without a published deadline; revalidate the official page and application route before spending operator time.
- Public HFO artifacts contain experimental terminology and references to multiple repositories. Before any proof link is used, bind exact licenses, remove or clearly separate private/sensitive material, and produce a short conventional README or case study.
- The current public repository's artifact licensing and third-party provenance were not comprehensively audited by this card.

## Cost and operator-minute estimate

```yaml
direct_research_cost_usd: 0
new_credentials_required_now: 0
operator_minutes_required_now: 0
estimated_consumer_minutes_for_no_send_fit_matrix: 20_to_35
estimated_operator_minutes_to_review_private_fit_gaps: 15_to_25
estimated_future_application_packaging_minutes_if_approved: 45_to_90
estimated_application_submission_minutes_if_operator_approves: 10_to_20
estimated_operator_minutes_avoided_by_this_card: 15_to_30
```

## Strongest objection

This is a high-bar production security role. HFO currently demonstrates unusually relevant design concerns, but much of the visible evidence is institutional protocol, experimental receipts, and same-provider preflight rather than shipped secure services, container/kernel isolation, network controls, cloud IAM, or telemetry at scale. A premature application could consume scarce operator attention and expose a sprawling public repository that obscures the strongest work.

## Strongest falsifier

`RETIRE` this candidate immediately if any of the following is true on direct recheck:

1. the official role or application route is closed;
2. Remote-US eligibility is removed or the operator is not eligible;
3. private resume evidence cannot truthfully support at least one production service example plus one cloud/network/isolation example;
4. the public proof artifact cannot be reduced to a runnable, conventional, non-sensitive case study with exact source and test evidence;
5. another admitted opportunity has materially lower application burden and stronger verified fit.

`REVISE` rather than retire if the role remains open but the proof artifact needs a bounded packaging WorkItem before any application draft.

## Reversible next experiment

Garmr may consume this card to create **one no-send qualification matrix**, not an application:

- left column: every official load-bearing requirement;
- right column: exact private or public evidence, `MISSING`, or `NEEDS_VERIFICATION`;
- one proposed proof artifact limited to a conventional two-page case study or runnable repository slice;
- estimated application burden and the single strongest disqualifying gap;
- stop for operator decision before drafting application answers or touching the ATS.

The matrix must bind this card's Git commit/path/blob after readback. It earns no income-lane credit until the consumer records `CONSUMED` or `REJECTED_WITH_EVIDENCE` against the exact digest.

## Verifier and consumer

- **Verifier:** Sigrun/P4 or another distinct nonproducer should challenge fit inflation, proof-artifact quality, and opportunity cost.
- **Consumer:** Garmr/P1 income lane may produce one no-send qualification matrix. TTao/operator remains the only authority for private resume disclosure and application submission.
- **Expiry:** `2026-08-03T02:26:13Z`; revalidate the official listing after expiry.

## Honest flaw

This carrier verified a current official job listing and compared it only with public Gen-133 artifacts. It did not inspect TTao's resume, production history, cloud/network/security depth, work authorization, current employment constraints, ATS questions, applicant privacy terms, or competing opportunities. The apparent alignment may be vocabulary-level rather than hiring-level. No external reviewer or recruiter has consumed the work, and this card itself produces `$0` until a named consumer turns it into a bounded, truthful no-send qualification packet.
