# S08 Evidence Card — Brain Co. AI Application Security location and experience gate

```yaml
schema: hfo.gen133.research_evidence_card.v0_1
seat: S08
role: Research and Candidate Scout
task_id_expected: 6a526109ba348191b5f23ad3172ad568
task_id_probe: MATCHED_FROM_RUNTIME_INSTRUCTION
wip: 1
canonical_repository: TTaoGaming/hfo-gen-133
canonical_branch: agent/gen133-bootstrap-20260730
valid_time_utc: 2026-08-05T23:31:54Z
lane: grants_jobs_income_opportunities
question: Does the current Brain Co. AI Application Security Engineer listing support treating the role as a remote-US, immediately routeable candidate for a Colorado-based operator without a location or experience gate?
exact_candidate: Brain Co. AI Application Security Engineer, Ashby job 46cacd55-81d9-414c-9fcb-c8be15d94e4a
decision: REVISE
claim_ceiling: LIVE_HIGH_DOMAIN_MATCH_ROLE; HYBRID_SAN_FRANCISCO_BAY_AREA; REMOTE_AND_RELOCATION_NOT_SUPPORTED; OPERATOR_EXPERIENCE_FIT_NOT_VERIFIED
expiry_utc: 2026-08-12T23:31:54Z
```

## Finding

```text
PUBLIC_ROLE_LISTED=true
LOCATION=SAN_FRANCISCO_BAY_AREA
LOCATION_TYPE=HYBRID
REMOTE_US_SUPPORTED=false
RELOCATION_SUPPORT_STATED=false
EXPLICIT_EXPERIENCE_GATE=5_PLUS_YEARS_APPLICATION_OR_PRODUCT_SECURITY
DOMAIN_MATCH=HIGH_ON_AGENT_AUTHORIZATION_TOOL_SCOPING_OUTPUT_VALIDATION_AND_SECURITY_AUTOMATION
IMMEDIATE_LOW_FRICTION_ROUTE=NOT_SUPPORTED
```

The current employer-controlled Ashby listing is unusually aligned with agent-security work: application-layer AuthN/AuthZ, tool scoping, permission boundaries, output validation, third-party integration security, automated security checks, regulated-data controls, and Python/Go/TypeScript security tooling. However, the same listing identifies the position as **hybrid in the San Francisco Bay Area** and asks for **5+ years of application or product security on production systems at scale**. No remote-US or relocation language was observed.

Therefore this candidate should remain in the income queue only behind two explicit gates: location willingness/feasibility and evidence-backed experience mapping. It must not be labeled remote, immediately actionable from Colorado, or already qualified.

## Dated primary/current sources

1. Brain Co. employer-controlled Ashby listing, accessed 2026-08-05: exact role ID, hybrid San Francisco Bay Area location, full-time status, responsibilities, 5+ years experience requirement, bonus languages, and application surface. https://jobs.ashbyhq.com/brainco/46cacd55-81d9-414c-9fcb-c8be15d94e4a
2. Brain Co. Atlas product page, accessed 2026-08-05: platform positioning around deployment control, data sovereignty, least-privilege access controls, traceability, and regulated-environment security. https://brain.co/atlas
3. Brain Co. official site, accessed 2026-08-05: current agent-native institutional-product positioning and active company hiring surface. https://brain.co/
4. Brain Co. website privacy policy, updated 2026-07-21 and accessed 2026-08-05: applies to the public website and does not clearly provide applicant-specific Ashby collection, retention, processor, or deletion terms. https://brain.co/privacy-policy

## Supported claims

- The exact job is publicly listed on Brain Co.'s employer-controlled Ashby board as of 2026-08-05.
- The listing classifies the role as hybrid in the San Francisco Bay Area, not remote-US.
- The role directly covers agent authorization, tool and permission scoping, output validation, third-party integrations, security automation, regulated data, and secure SDLC work.
- The listing explicitly requests 5+ years in application security or product security with production systems at scale.
- Python, Go, or TypeScript proficiency is bonus evidence rather than a substitute for the core experience gate.

## Excluded claims

- Brain Co. will permit permanent remote work from Colorado.
- Brain Co. provides relocation assistance, travel reimbursement, or a defined in-office cadence.
- The operator satisfies the 5+ year production AppSec/Product Security requirement.
- Adjacent work in AI agents, OPA/Rego, multi-agent governance, or software factories will be accepted as equivalent without resume- and artifact-level evidence.
- The role is actively interviewing, has a fixed closing date, or will remain open through this card's expiry.
- An application would be delivered, reviewed, shortlisted, interviewed, or accepted.

## License and terms uncertainty

No software license applies. Public role and company pages were inspected without reproducing substantial protected text. Brain Co.'s public website privacy policy expressly scopes itself to the website and does not clearly establish applicant-specific handling for the Ashby application flow. Applicant-data processors, retention, cross-border transfer, deletion, and screening terms remain unknown until the application surface and linked notices are reviewed. No terms were accepted and no account was created.

## Strongest objection

The domain fit is unusually strong and may justify relocation or a location exception request. That is true, but it does not erase the published hybrid location or the explicit experience threshold. Treating the role as remote-ready would create false-green routing and waste application effort before the two largest gates are checked.

## Falsifier

Promote or revise this card if an authoritative Brain Co. source changes the role to remote-US, explicitly permits Colorado-based work, states relocation support, or confirms an acceptable hybrid cadence. Separately, a distinct resume-and-artifact verifier may clear the experience gate only by mapping dated production AppSec/Product Security outcomes to the listing's requirements; self-description alone is insufficient.

## Verification and consumption

```yaml
verifier: DISTINCT_CURRENT_BRAINCO_ROLE_LOCATION_AND_RESUME_ARTIFACT_FIT_VERIFIER
consumer:
  primary: BRAINCO_AI_APPLICATION_SECURITY_CANDIDATE_TRIAGE_001
  downstream: Var career/outreach reconciliation
producer_research_minutes_estimate: 10-18
location_and_resume_gate_minutes_estimate: 15-30
application_minutes_estimate_if_gates_clear: 45-90
external_spend_usd: 0
fitness_credit: 0 pending exact WorkItem consumption and ConsumerAck
```

## No-action receipt

No application, outreach, email access, send, account action, terms acceptance, purchase, spend, deployment, merge, publication outside the required Git/Slack evidence path, task mutation, or private-data use occurred in this research pass.
