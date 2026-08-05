# S08 Evidence Card — DrSwarm official Careers→HN email-route boundary

```yaml
schema: hfo.gen133.research_evidence_card.v0_1
seat: S08
role: Research and Candidate Scout
task_id_expected: 6a526109ba348191b5f23ad3172ad568
task_id_probe: MATCHED_FROM_RUNTIME_INSTRUCTION
wip: 1
canonical_repository: TTaoGaming/hfo-gen-133
canonical_branch: agent/gen133-bootstrap-20260730
valid_time_utc: 2026-08-05T18:26:32Z
lane: grants_jobs_income_opportunities
question: Does current public evidence support that jobs@drswarm.com with subject "HN Founding Engineer" is an employer-designated application route for DrSwarm's Founding Engineer role, and does it prove the vacancy is still open now?
exact_candidate: DrSwarm Founding Engineer (Full-Stack), Hacker News item 48358793
decision: ADMIT
claim_ceiling: EMPLOYER_DESIGNATED_ROUTE_AS_OF_POSTING_AND_STILL_LINKED_FROM_OFFICIAL_CAREERS_SURFACE; CURRENT_VACANCY_STATUS_UNKNOWN
expiry_utc: 2026-08-12T18:26:32Z
```

## Finding

```text
OFFICIAL_CAREERS_DELEGATES_TO_HACKER_NEWS=true
PUBLIC_ROLE_POST_ID=48358793
EMPLOYER_DESIGNATED_EMAIL_ROUTE=jobs@drswarm.com
REQUIRED_SUBJECT="HN Founding Engineer"
ROLE_OPEN_AS_OF_2026-08-05=UNKNOWN
DEDICATED_ATS_OR_CURRENT_JOB_DETAIL_PAGE_OBSERVED=false
```

DrSwarm's current official website exposes a **Careers** link that delegates to Hacker News rather than a company ATS or dedicated job-detail page. The linked public DrSwarm post identifies a Founding Engineer (Full-Stack) role, names `jobs@drswarm.com`, requires the subject `HN Founding Engineer`, requests GitHub/LinkedIn plus 2–3 projects, and describes a paid-work-trial hiring process. The post was approximately 62 days old at inspection. This admits the route's provenance, not current vacancy status.

## Dated primary/current sources

1. DrSwarm official website, accessed 2026-08-05: current footer exposes `Careers` linking to Hacker News; page identifies DrSwarm and founder Michael Nusimow. https://drswarm.com/
2. Hacker News item `48358793`, accessed 2026-08-05: exact role, work arrangement, stack, process, contact email, required subject, and requested materials. https://news.ycombinator.com/item?id=48358793
3. DrSwarm Privacy Policy v1, effective 2026-01-01 and accessed 2026-08-05: general website/services policy with broad retention language; no applicant-specific notice was observed. https://drswarm.com/privacy
4. DrSwarm Terms of Service v1, effective 2026-01-01 and accessed 2026-08-05: service/customer terms; no applicant-specific application terms were observed. https://drswarm.com/terms

## Supported claims

- The official DrSwarm Careers surface currently delegates users to Hacker News.
- HN item `48358793` is the exact public role post reachable from that official careers route.
- The post designated `jobs@drswarm.com` and subject `HN Founding Engineer` as its application route.
- The post described full-time or contract-to-full-time work, Pacific-hours overlap, and a short paid work trial.

## Excluded claims

- The role remained open or actively reviewed on 2026-08-05.
- An email sent to the route was accepted by the recipient server, delivered to an inbox, read, reviewed, or answered.
- The applicant was eligible, competitive, shortlisted, interviewed, or hired.
- The HN account's legal identity or authority was independently established beyond the official DrSwarm site delegating Careers to the post.
- DrSwarm's general privacy policy or terms constitute a complete applicant-data notice.

## License and terms uncertainty

No software license applies. Public pages were inspected and cited without reproducing substantial protected text. Hacker News and DrSwarm site terms remain applicable to their respective surfaces. DrSwarm's published Privacy Policy and Terms address website/services use but do not clearly provide applicant-specific collection, retention, processor, or deletion terms; applicant-data handling therefore remains uncertain. No terms were accepted and no account was created.

## Strongest objection

The official site still points Careers to the HN post, which could imply the role remains active. That is useful evidence of route provenance but not enough to prove an August vacancy: the explicit role post is roughly two months old, has no stated closing date, and no dedicated current-status field or ATS receipt surface was observed.

## Falsifier

Revise or retire this admission if an authoritative DrSwarm source removes or redirects the Careers link, marks the role filled/closed, replaces the application route or subject, or states that HN item `48358793` is stale or unauthorized. A distinct current-status verification may promote `ROLE_OPEN` only with an authoritative dated role page, employer response, or equivalent provider-side evidence.

## Verification and consumption

```yaml
verifier: DISTINCT_CURRENT_DRSWARM_ROLE_STATUS_AND_EMAIL_ROUTE_VERIFIER
consumer:
  primary: DRSWARM_APPLICATION_DELIVERY_STATUS
  downstream: Var career/outreach reconciliation
producer_research_minutes_estimate: 12-20
followup_verification_minutes_estimate: 5-15
external_spend_usd: 0
fitness_credit: 0 pending exact WorkItem consumption and ConsumerAck
```

## No-action receipt

No application, outreach, email access, send, account action, terms acceptance, purchase, spend, deployment, merge, publication, task mutation, or private-data use occurred in this research pass.
