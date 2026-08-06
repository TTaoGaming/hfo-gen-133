# S08 Evidence Card — Monarch Money Senior Application Security experience and tooling gate

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
valid_time_utc: 2026-08-06T09:28:47Z
lane: grants_jobs_income_opportunities
queue_change_basis: LAST_S08_LANE_WAS_DISTRIBUTION_BUYER_EVIDENCE; EXPLICIT_ROTATION_ADVANCES_TO_GRANTS_JOBS_INCOME; EXACT_MONARCH_ROLE_NOT_PREVIOUSLY_CARDED
question: Does Monarch Money's current Senior Application Security Engineer role clear the published location and domain gates enough for immediate candidate triage, or must it be revised behind a direct-experience and tooling evidence gate?
exact_candidate: Monarch Money Senior Application Security Engineer, Ashby job 8942e89d-1bf9-4911-bc33-cf89bde6e997
candidate_version: EMPLOYER_CONTROLLED_ASHBY_POSTING_ACCESSED_2026-08-06; NO_REVISION_HASH_EXPOSED
decision: REVISE
claim_ceiling: LIVE_REMOTE_US_HIGH_DOMAIN_MATCH_ROLE; LOW_FRICTION_APPLICATION_AND_OPERATOR_QUALIFICATION_NOT_SUPPORTED
expiry_utc: 2026-08-13T09:28:47Z
```

## Finding

```text
PUBLIC_ROLE_LISTED=true
LOCATION=REMOTE_US_AND_CANADA
EMPLOYMENT_TYPE=FULL_TIME
BASE_SALARY_USD=180000_TO_215000
PUBLISHED_EXPERIENCE_GATE=5_PLUS_YEARS_SECURITY_ENGINEERING_WITH_DEMONSTRATED_APPSEC_AND_AI_SECURITY_DEPTH
REQUIRED_STACK=PYTHON_DJANGO_WEB_API_AUTHN_AUTHZ_SAST_DAST_SEMGREP_BURP_NUCLEI_OR_EQUIVALENTS
OPERATIONAL_DUTY=WEEKLY_SECURITY_ON_CALL
AGENTIC_AI_SECURITY_DOMAIN_MATCH=HIGH
IMMEDIATE_LOW_FRICTION_ROUTE=false
CANDIDATE_TRIAGE_ROUTE=REVISE_BEHIND_DATED_DIRECT_APPSEC_TOOLING_AND_ON_CALL_EVIDENCE_GATE
```

The employer-controlled listing is live and labels the role remote in the United States and Canada. It directly covers threat modeling, secure code review, SAST/DAST, vulnerability management, penetration testing, Python/Django web and API security, authentication and authorization, LLM-integrated features, prompt injection, data leakage, model abuse, agentic attack surfaces, AI-powered security automation, and a weekly security on-call rotation.

The bounded uncertainty is not domain relevance; that is high. The blocker is the published mandatory gate: **5+ years in security engineering with demonstrated depth in Application and AI security**, plus hands-on use of named AppSec tools or equivalents. Without a dated resume-and-artifact mapping, this role must not be presented as a low-friction or qualification-cleared opportunity. Remote status and topical overlap are insufficient.

## Dated primary/current source

1. Monarch Money employer-controlled Ashby listing, accessed 2026-08-06: exact role ID, remote-US/Canada status, full-time employment, $180K–$215K US base range, five-plus-year experience requirement, Python/Django and AppSec tooling requirements, AI/agentic security scope, weekly on-call duty, interview stages, and benefits. https://jobs.ashbyhq.com/monarchmoney/8942e89d-1bf9-4911-bc33-cf89bde6e997/

## Supported claims

- The exact role is publicly listed on Monarch Money's employer-controlled Ashby board as of 2026-08-06.
- The listing labels it remote in the United States and Canada, full-time, with a published US base range of $180K–$215K plus equity and bonus.
- The role has unusually strong topical overlap with AI-agent security: prompt injection, data leakage, model abuse, agentic attack surfaces, LLM supply-chain risk, and security automation are explicit.
- The mandatory experience gate is five-plus years in security engineering with demonstrated depth in Application and AI security.
- Python, Django/web/API security, threat modeling, secure code review, SAST/DAST, vulnerability management, penetration testing, and hands-on AppSec tooling are explicit requirements.
- The role includes a weekly security on-call rotation.
- The role is suitable for evidence-gated candidate review, not immediate application routing.

## Excluded claims

- The operator satisfies the five-plus-year direct security-engineering requirement.
- Adjacent AI-agent architecture, policy-as-code, governance, orchestration, or general software engineering automatically counts as demonstrated AppSec depth.
- The operator has production evidence for Semgrep, Burp Suite, Nuclei, SAST/DAST operations, penetration testing, vulnerability backlog ownership, or weekly incident/on-call response.
- Remote-US wording proves Colorado payroll eligibility, sponsorship, work authorization, or absence of unlisted state restrictions.
- The posting is actively interviewing, has no internal candidate, or will remain open through expiry.
- The published compensation is guaranteed for any candidate.
- An application would be reviewed, interviewed, shortlisted, or accepted.

## License and terms uncertainty

No software license applies. The public job page was inspected without reproducing substantial protected text. No applicant account was created, no application form was opened or submitted, and no terms were accepted. The application-specific privacy notice, applicant-data controller/processor split, retention period, screening vendors, automated-decision practices, deletion route, and cross-border handling were not stood and remain downstream gates.

## Strongest objection

Senior job descriptions are often aspirational, and strong adjacent engineering plus AI-security evidence may substitute for an exact AppSec title history. That is plausible, but the listing does not merely request broad security interest; it asks for five-plus years and demonstrated operational depth across AppSec review, tooling, vulnerability management, penetration testing, and on-call duties. Treating adjacency as qualification without dated evidence would be demand invention and false green.

## Falsifier

Revise toward `ADMIT` only if a distinct verifier can map dated, attributable production outcomes to the mandatory five-plus-year AppSec/AI-security gate, including Python/web/API security, threat modeling or secure code review, SAST/DAST or equivalent tooling, vulnerability remediation ownership, and incident/on-call evidence. Retire if the employer removes the listing, excludes the operator's location or authorization, or the evidence review cannot substantiate the mandatory operational requirements.

## Verification and consumption

```yaml
verifier: DISTINCT_CURRENT_MONARCH_ROLE_AND_DATED_APPSEC_TOOLING_ON_CALL_FIT_VERIFIER
consumer:
  primary: MONARCH_MONEY_SENIOR_APPSEC_CANDIDATE_TRIAGE_001
  downstream: Var career/outreach reconciliation
producer_research_minutes_estimate: 15-25
resume_and_artifact_gate_minutes_estimate: 30-60
application_minutes_estimate_if_gate_clears: 60-120
external_spend_usd: 0
operator_minutes_this_pass: 0
fitness_credit: 0 pending exact WorkItem consumption and ConsumerAck
```

## No-action receipt

No application, outreach, account creation, email access, send, terms acceptance, purchase, spend, deployment, merge, public publication outside the required Git/Slack evidence path, task mutation, or private-data use occurred in this research pass.
