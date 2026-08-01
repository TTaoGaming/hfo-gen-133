---
schema_id: hfo.gen133.s08.research_evidence_card.v1
card_id: S08_OPENAI_OFFENSIVE_SECURITY_AGENT_ENGINEER_20260801T133250Z
result: REVISE
callsign_or_seat: S08_RESEARCH_CANDIDATE_SCOUT
carrier_task_id_expected: 6a526109ba348191b5f23ad3172ad568
carrier_task_id_observed: 6a526109ba348191b5f23ad3172ad568
carrier_task_id_match: true
carrier_identity_claim: DISPOSABLE_SCHEDULED_CARRIER_NOT_LINEAGE
controller: operator_direct
wip: 1
valid_time_utc: 2026-08-01T13:32:50Z
transaction_time_utc: SEE_GITHUB_COMMIT_METADATA
canonical_repository: TTaoGaming/hfo-gen-133
canonical_branch: agent/gen133-bootstrap-20260730
repository_head_observed_before_write: eb27711b9d97fe0db4fcde712761ae48813c838b
research_lane: grants_jobs_income_opportunities
candidate_organization: OpenAI
candidate_role: Offensive Security Agent Engineer
candidate_location: Remote_US_New_York_City_Seattle_Washington_DC_San_Francisco
candidate_application_id: dd7443fe-a7b8-4794-8dd5-cb7d14c00c64
candidate_contract_version: official_openai_careers_observed_2026-08-01
privacy_class: PUBLIC_PRIMARY_SOURCES_AND_SANITIZED_REPOSITORY_POINTERS_ONLY
effect_ceiling: FILE_AND_SANITIZED_SLACK_POINTER_ONLY
expiry_utc: 2026-08-03T13:32:50Z
verifier: Sigrun/P4_APEX_FALSIFICATION_or_other_distinct_nonproducer
consumer: Garmr/P1_INCOME_LANE_FOR_ONE_OPENAI_ROLE_FAMILY_COMPARISON
fitness_credit: ZERO_UNTIL_EXACT_CONSUMER_ACK
sealed: false
---

# S08 evidence card — OpenAI Offensive Security Agent Engineer

## Changed queue edge and bounded question

The prior S08 card completed the `distribution_and_buyer_evidence` lane at commit
`e39c63e9db62d606bf21a5936d35facf219dcf3f`. The explicit rotation therefore
advances to `grants_jobs_income_opportunities`.

The standing income dispatch remains red at
`projects/income-lane/garmr_outreach_dispatch.md`, blob
`27741e1787083522f802a736abff1de7da1e7f45`: external income is recorded as `$0`,
while every application and send remains operator-gated. Repository search found
no prior Gen-133 card naming this exact role; that search is not proof of global
absence.

Question: does OpenAI's current `Offensive Security Agent Engineer` role justify a
separate no-send application packet, or should it be retained only as a higher-bar
alternative to the already admitted `Security Engineer, Agent Security` role?

## Decision

`REVISE`.

The role is current, explicitly Remote-US, and unusually close to the HFO thesis:
build specialized agents that continuously test infrastructure and applications,
encode expert workflows into tools and policies, use human approval for dangerous
actions, recover from failure, remain observable, and evaluate meaningful security
outcomes. Compensation is listed as `$347K-$490K + equity`.

However, this is a Staff-to-Principal technical-owner role requiring substantial
hands-on offensive-security judgment plus production-quality software. Public HFO
artifacts show relevant agent-control and regression-resistance concepts, but they
do not establish penetration-testing depth, exploit validation, cloud/Kubernetes
security mastery, or production vulnerability-management outcomes.

Do not open a second independent OpenAI application lane. Retain this role as one
comparison row against the already admitted `Security Engineer, Agent Security`
role. Advance it only if private evidence clearly supports the offensive-security
bar and makes it the stronger truthful fit.

No application, account action, resume disclosure, outreach, or submission is
authorized.

## Self-probe

```yaml
expected_task_id: 6a526109ba348191b5f23ad3172ad568
observed_task_id: 6a526109ba348191b5f23ad3172ad568
task_id_match: true
tools_observed:
  github_connector: authenticated_read_write_and_exact_file_readback
  slack_public_channel: authenticated_read_write
  web_primary_sources: read
  shell_or_browser_runtime: unavailable
  gmail_calendar_drive_private_data: not_used
  task_mutation: not_called
```

## Exact candidate and dated primary sources

Observed `2026-08-01`:

1. OpenAI official role page, `Offensive Security Agent Engineer`:
   https://openai.com/careers/offensive-security-agent-engineer-remote-us/
2. OpenAI official careers search showing the role as active:
   https://openai.com/careers/search/?q=agent
3. Official application route surfaced by OpenAI, Ashby application ID
   `dd7443fe-a7b8-4794-8dd5-cb7d14c00c64`:
   https://jobs.ashbyhq.com/openai/dd7443fe-a7b8-4794-8dd5-cb7d14c00c64/application
4. Gen-133 `CARRIER_CONTRACT.md`, branch blob
   `26e78ac3fedfa4c49cb4285a9c81426a2b13f84b`, as public evidence of authority
   ceilings, actor/carrier separation, refusal sets, receipt requirements, and
   no-self-verification discipline.
5. Gen-133 terminal-cancellation producer return at commit
   `22e92d32623843934c7dc76a19a7ec492b971d59`, blob
   `2ed9c4996a412b7de9c1304354dbf96c41c0edc8`, as bounded evidence of regression
   tests, exact command/exit-code capture, rollback, remaining risk, and explicit
   nonbinding producer status. It is not offensive-security proof.

## Supported claims

- The role is listed for Remote-US, New York City, Seattle, Washington DC, and San
  Francisco.
- OpenAI describes the level as Staff-to-Principal and the person as technical
  owner for offensive-security agents.
- Responsibilities include agent portfolios, cloud and Kubernetes testing, web
  applications, endpoints, external attack surface, vulnerability validation,
  remediation tracking, fix verification, human-in-the-loop controls, evaluations,
  observability, failure recovery, and production-safe operation.
- The listing values experience extending agent systems with models, tools,
  structured context, memory, orchestration, and feedback loops.
- Public HFO work has plausible relevance to authority limits, dangerous-action
  approval, durable receipts, failure visibility, mutation-style negative controls,
  idempotency, rollback, and regression resistance.
- A conventional proof packet could truthfully show one bounded agent-control loop
  and its red-to-green test history, provided it is not presented as production
  offensive-security experience.

## Excluded claims

- No claim that TTao has substantial hands-on offensive-security experience or
  Staff/Principal scope.
- No claim of cloud, Kubernetes, container, Linux, macOS, source-review, endpoint,
  external-attack-surface, exploit-development, or vulnerability-remediation
  mastery.
- No claim that HFO has continuously tested production systems, found externally
  validated vulnerabilities, fixed them, or measured real attack-surface coverage.
- No resume, employment history, work authorization, references, private portfolio,
  interview history, or application answers were inspected.
- No claim that public HFO repositories are ready to expose to a recruiter without
  conventional packaging, license review, and sensitive-material screening.
- No application form was completed; the Ashby route required JavaScript and its
  full fields and terms were not inspected.
- No deadline is shown in the readable official listing. The role may change or
  close without notice.

## License, terms, privacy, cost, and operator burden

The application route links into a third-party ATS. Applicant privacy terms, data
retention, required disclosures, and all form fields must be reviewed before any
private data is entered. Public proof artifacts also require exact license and
third-party provenance review before being linked.

```yaml
direct_research_cost_usd: 0
credentials_or_terms_used: none
operator_minutes_required_now: 0
estimated_consumer_minutes_for_role_family_comparison: 15_to_25
estimated_operator_minutes_for_private_offsec_fit_check: 15_to_30
estimated_future_no_send_packet_if_selected: 45_to_90
estimated_application_submission_if_operator_approves: 10_to_20
estimated_operator_minutes_avoided_by_not_opening_second_lane: 30_to_60
```

## Strongest objection

The vocabulary match is dangerously flattering. The role is not primarily asking
for an agent-orchestration theorist; it is asking for an offensive-security domain
expert who can own a production system and encode expert attacker judgment. HFO's
most visible strengths are control contracts, workflow safety, experimental
receipts, and same-provider preflight. Without concrete exploit, cloud/Kubernetes,
and remediation evidence, treating this as a strong fit would be resume inflation
and would distract from the lower-bar already admitted OpenAI role or nearer-term
income work.

## Strongest falsifier

`RETIRE` this candidate for the current cycle if any one holds:

1. the official role or application route closes;
2. Remote-US eligibility no longer applies or the operator is ineligible;
3. private evidence cannot support substantial hands-on offensive-security work;
4. no truthful example shows vulnerability discovery, exploitability validation,
   remediation ownership, and fix verification in a real system;
5. no production-quality agent or security system can be explained with concrete
   scale, reliability, observability, and failure-recovery evidence;
6. the already admitted `Security Engineer, Agent Security` role has materially
   stronger verified fit at lower packaging burden;
7. another opportunity has stronger verified fit and lower operator-minute cost.

`ADMIT` only if the private fit matrix verifies the offensive-security bar and a
compact proof artifact can be produced without exaggerating HFO's maturity.

## Reversible next experiment

Garmr may add exactly one comparison row to the existing OpenAI role-family
qualification packet. It must compare:

- exact official requirements;
- verified private evidence, `MISSING`, or `NEEDS_VERIFICATION`;
- staff/principal ownership evidence;
- offensive-security depth and concrete vulnerability outcomes;
- production agent-system evidence;
- proof-artifact packaging burden;
- compensation/location constraints;
- strongest disqualifying gap.

Then choose at most one result:

```text
SELECT_AGENT_SECURITY_ROLE
SELECT_OFFENSIVE_SECURITY_AGENT_ENGINEER
RETIRE_BOTH
```

Stop before drafting application answers, entering the ATS, or submitting. Bind
this card's exact Git commit/path/blob after readback.

## Verifier, consumer, expiry, and honest flaw

- **Verifier:** Sigrun/P4 or another distinct nonproducer should challenge title and
  vocabulary inflation, production evidence, and opportunity cost.
- **Consumer:** Garmr/P1 may add one role-family comparison row; TTao/operator alone
  controls private resume disclosure and application submission.
- **Expiry:** `2026-08-03T13:32:50Z`; revalidate the official page and application
  route after expiry.
- **Credit:** zero until a named WorkItem records `CONSUMED` or
  `REJECTED_WITH_EVIDENCE` against the exact Git blob.

Honest flaw: this carrier compared a current official job listing with public
Gen-133 artifacts only. It did not inspect TTao's resume, security history,
production deployments, exploit reports, cloud/Kubernetes depth, work eligibility,
ATS fields, or competing opportunities. The current fit may be conceptual rather
than hiring-level, and no recruiter or independent verifier has consumed it.
