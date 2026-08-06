# S08 Evidence Card — Jump Application & Product Security remote-US and experience gate

```yaml
schema: hfo.gen133.research_evidence_card.v0_1
seat: S08
role: Research and Candidate Scout
task_id_expected: 6a526109ba348191b5f23ad3172ad568
task_id_probe: MATCHED_FROM_RUNTIME_INSTRUCTION
self_probe:
  identity: HFO_GEN133_S08_RESEARCH_AND_CANDIDATE_SCOUT
  git_connector: READ_WRITE_AVAILABLE
  slack_connector: READ_SEND_AVAILABLE
  web_research: AVAILABLE
wip: 1
canonical_repository: TTaoGaming/hfo-gen-133
canonical_branch: agent/gen133-bootstrap-20260730
valid_time_utc: 2026-08-06T04:32:00Z
lane: grants_jobs_income_opportunities
queue_change_basis: PRIOR_BRAINCO_CANDIDATE_REQUIRED_HYBRID_SF_AND_5_PLUS_YEARS; TEST_ONE_REMOTE_US_LOWER_THRESHOLD_ALTERNATIVE
question: Does Jump's current Application & Product Security Engineer listing clear the published location and experience gates enough to admit it to bounded candidate triage for a Colorado-based operator, without claiming qualification or application readiness?
exact_candidate: Jump (Accio, Inc.) Application & Product Security Engineer, Ashby job 8f96b791-a170-4959-a772-74e1872f5841
candidate_version: EMPLOYER_CONTROLLED_ASHBY_POSTING_ACCESSED_2026-08-06; NO_REVISION_HASH_EXPOSED
prior_internal_card: projects/income-lane/research/20260805T233154Z_S08_BRAINCO_AI_APPLICATION_SECURITY_LOCATION_AND_EXPERIENCE_GATE_EVIDENCE_CARD.md
decision: ADMIT
claim_ceiling: LIVE_REMOTE_US_HIGH_DOMAIN_MATCH_CANDIDATE_FOR_TRIAGE; OPERATOR_FIT_APPLICATION_AND_HIRING_OUTCOME_UNKNOWN
expiry_utc: 2026-08-13T04:32:00Z
```

## Finding

```text
PUBLIC_ROLE_LISTED=true
LOCATION=REMOTE_US
LOCATION_TYPE=REMOTE
EMPLOYMENT_TYPE=FULL_TIME
PUBLISHED_EXPERIENCE_GATE=2_TO_4_YEARS_APPSEC_PRODUCT_SECURITY_OR_SOFTWARE_ENGINEERING_WITH_SIGNIFICANT_SECURITY_RESPONSIBILITIES
BASE_SALARY_USD=130000_TO_170000
AI_LLM_PRODUCT_SECURITY=NICE_TO_HAVE
CODE_LANGUAGES=PYTHON_TYPESCRIPT_JAVASCRIPT_GO_OR_SIMILAR
DOMAIN_MATCH=HIGH_ON_THREAT_MODELING_SECURE_DESIGN_CODE_REVIEW_AUTHN_AUTHZ_CI_CD_SECURITY_INCIDENT_RESPONSE_AND_SECURITY_AUTOMATION
IMMEDIATE_APPLICATION_READY=UNKNOWN
CANDIDATE_TRIAGE_ROUTE=ADMIT_WITH_RESUME_AND_INCIDENT_RESPONSE_GATES
```

The employer-controlled Ashby listing identifies the role as **Remote (US)** and asks for **2–4 years** in application security, product security, or software engineering with significant security responsibilities. The work includes threat modeling, secure design review, security-focused code review, SAST/dependency/secrets tooling in CI/CD, incident response, bug-bounty and penetration-test triage, and building lightweight secure-development patterns. Ability to read and write Python, TypeScript/JavaScript, Go, or similar languages is explicitly relevant; securing AI/LLM-powered products is a nice-to-have rather than a mandatory gate.

Compared with the prior Brain Co. candidate, this exact role removes the published hybrid-San-Francisco gate and lowers the stated experience threshold from five-plus years to two-to-four years. That is enough to **admit the role to bounded candidate triage**, not enough to claim that the operator satisfies the requirements or should submit an application without a resume-and-artifact review.

## Dated primary/current sources

1. Jump employer-controlled Ashby listing, accessed 2026-08-06: exact role ID, Remote (US), full-time status, $130K–$170K base range, 2–4 year experience gate, responsibilities, language examples, incident-response requirement, and AI/LLM nice-to-have. https://jobs.ashbyhq.com/jump-app/8f96b791-a170-4959-a772-74e1872f5841
2. Jump official careers surface, accessed 2026-08-06: current employer hiring surface and company identity. https://jump.ai/careers
3. Jump AI Associate product page, accessed 2026-08-06: current agentic product behavior across connected systems, human approval before actions, and compliance/security positioning. https://jump.ai/operating-system/ai-associate
4. Jump security and compliance article, published 2026-04-07 and accessed 2026-08-06: current product-security context around policy enforcement, human review, consent, retention, redaction, and data-sharing restrictions. https://jump.ai/blog/security-and-compliance
5. Ashby public job-posting API documentation, accessed 2026-08-06: public job-board endpoint contract and optional compensation field. https://developers.ashbyhq.com/docs/public-job-posting-api

## Supported claims

- The exact role is publicly listed on Jump's employer-controlled Ashby board as of 2026-08-06.
- The listing expressly labels the position Remote (US), full-time, and $130K–$170K base salary plus equity.
- The stated experience gate is 2–4 years in AppSec/Product Security or software engineering with significant security responsibilities.
- The role directly covers threat modeling, secure design, code review, CI/CD security tooling, vulnerability triage, incident response, and developer enablement.
- Python, TypeScript/JavaScript, Go, or similar coding ability is relevant.
- AI/LLM product-security experience is a nice-to-have, not a stated mandatory requirement.
- The role is materially more routeable for initial triage than the prior Brain Co. hybrid-SF, five-plus-year candidate.

## Excluded claims

- The operator meets the 2–4 year direct-security requirement.
- Adjacent AI-agent, OPA/Rego, pBFT, multi-agent governance, or software-factory work will automatically count as application/product security experience.
- The operator has sufficient real incident-response evidence.
- Jump accepts Colorado applicants without any unlisted state, payroll, work-authorization, or timezone restriction.
- Visa sponsorship, relocation, equipment stipend, interview timeline, closing date, or active-interview status is available.
- The posting will remain open through expiry.
- An application would be delivered, reviewed, interviewed, shortlisted, or accepted.

## License and terms uncertainty

No software license applies. Public job and company pages were inspected without reproducing substantial protected text. The application is hosted by Ashby; no applicant account was created, no form was submitted, and no terms were accepted. Jump's public product/site agreements and privacy references do not by themselves establish the exact applicant-data controller/processor split, retention period, screening vendors, deletion process, cross-border handling, or automated-decision practices for this Ashby application. Those remain unknown until the application-specific notices are reviewed by the downstream consumer.

## Strongest objection

The lower published threshold and remote-US label can still create false confidence: the role explicitly expects real threat modeling, code review, CI/CD security tooling, and hands-on incident response. If the operator cannot map dated production outcomes to those requirements, this remains a poor application despite strong AI-agent and programming adjacency.

## Falsifier

Revise or retire if the employer removes the listing, changes it away from Remote (US), raises the experience threshold, adds a state/work-authorization restriction excluding the operator, or clarifies that the role requires production AppSec/incident-response evidence the operator cannot substantiate. Promote toward application readiness only after a distinct verifier maps dated resume and portfolio evidence to each mandatory requirement and confirms applicant notices and current role status.

## Verification and consumption

```yaml
verifier: DISTINCT_CURRENT_JUMP_ROLE_AND_RESUME_INCIDENT_RESPONSE_FIT_VERIFIER
consumer:
  primary: JUMP_APPLICATION_PRODUCT_SECURITY_CANDIDATE_TRIAGE_001
  downstream: Var career/outreach reconciliation
producer_research_minutes_estimate: 12-20
resume_and_artifact_gate_minutes_estimate: 20-40
application_minutes_estimate_if_gate_clears: 45-90
external_spend_usd: 0
operator_minutes_this_pass: 0
fitness_credit: 0 pending exact WorkItem consumption and ConsumerAck
```

## No-action receipt

No application, outreach, email access, send, account action, terms acceptance, purchase, spend, deployment, merge, external publication outside the required Git/Slack evidence path, task mutation, or private-data use occurred in this research pass.
