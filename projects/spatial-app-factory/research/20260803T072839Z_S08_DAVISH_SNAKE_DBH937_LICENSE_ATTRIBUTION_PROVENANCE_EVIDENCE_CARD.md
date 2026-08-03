---
schema_id: hfo.gen133.s08.evidence_card.v1
seat: S08_RESEARCH_AND_CANDIDATE_SCOUT
carrier_task_id_expected: 6a526109ba348191b5f23ad3172ad568
carrier_task_id_observed: 6a526109ba348191b5f23ad3172ad568
carrier_task_id_match: true
wip: 1
valid_time_utc: 2026-08-03T07:28:39Z
transaction_time_utc: SEE_GITHUB_COMMIT_METADATA
canonical_repository: TTaoGaming/hfo-gen-133
canonical_branch: agent/gen133-bootstrap-20260730
lane: spatial_foss_candidates_and_licenses
question_changed_from: projects/spatial-app-factory/research/20260803T022621Z_S08_DAVISH_SNAKE_CLEAN_CONTINUOUS_CONTROL_CANDIDATE_EVIDENCE_CARD.md
question: Does the dbh937 copyright notice in davish/snake create a material reuse blocker, or can public primary GitHub evidence reduce the attribution uncertainty without rewriting the notice?
candidate_repository: davish/snake
candidate_commit: 13989df94ce227cd6e3ba347e61d3c95ec0279da
candidate_license_blob: ffe85ee0e2942bf425089347b5774821c91ddbc2
decision: REVISE
classification: LICENSE_ATTRIBUTION_AMBIGUITY_REDUCED_PRESERVE_NOTICE_VERBATIM
fitness_credit: 0
privacy_class: PUBLIC_REPOSITORY_METADATA_AND_SOURCE_ONLY
expiry: 2026-09-01T00:00:00Z
sealed: false
---

# S08 evidence card — `davish/snake` attribution boundary

## Bounded result

**REVISE.** The `dbh937` versus `davish` name mismatch should no longer be treated as a standalone blocker to a bounded MIT-preserving repair specimen. The strongest public primary evidence links the historical `dbh937` handle to the current `davish` account and the name Davis Haupt. The safe action is still to preserve the exact 2013 copyright notice verbatim rather than normalize or replace it.

This does **not** admit the candidate as runnable. The startup callback-scope defect identified in the prior S08 card remains unresolved, so `davish/snake@13989df94ce227cd6e3ba347e61d3c95ec0279da` remains `REPAIR_BEFORE_ADMIT`.

## Dated primary evidence

Observed `2026-08-03`:

1. Exact candidate repository and version: [`davish/snake@13989df94ce227cd6e3ba347e61d3c95ec0279da`](https://github.com/davish/snake/tree/13989df94ce227cd6e3ba347e61d3c95ec0279da).
2. Exact root license: [`LICENSE`](https://github.com/davish/snake/blob/13989df94ce227cd6e3ba347e61d3c95ec0279da/LICENSE), blob `ffe85ee0e2942bf425089347b5774821c91ddbc2`. It contains the MIT grant, names `Copyright (c) 2013 dbh937`, and requires the copyright and permission notice to remain in copies or substantial portions.
3. Current GitHub identity surface: [`gist.github.com/davish`](https://gist.github.com/davish) identifies the account as `Davis Haupt` / `davish`.
4. The same current `davish` gist surface contains historical source labeled `by Davis Haupt` whose license pointer is `https://raw.github.com/dbh937/files/master/license`. This is direct same-account evidence connecting Davis Haupt with the historical `dbh937` namespace.
5. The same account also exposes a 2013 gist carrying `Copyright (c) Davis Haupt` and an MIT statement, which is consistent with the handle-to-name linkage.
6. GitHub currently detects the candidate repository as MIT licensed and documents that a root license file communicates permission to use, change, and distribute repository code. GitHub also warns that its license information is a starting point rather than legal advice.

Prior unresolved card: [`20260803T022621Z_S08_DAVISH_SNAKE_CLEAN_CONTINUOUS_CONTROL_CANDIDATE_EVIDENCE_CARD.md`](https://github.com/TTaoGaming/hfo-gen-133/blob/4a0f8d20602d0c2fc4ac04a2faef3fdd9b9aa35f/projects/spatial-app-factory/research/20260803T022621Z_S08_DAVISH_SNAKE_CLEAN_CONTINUOUS_CONTROL_CANDIDATE_EVIDENCE_CARD.md), blob `3391c8613f85a1fcbe7df6f2174215177a6b8fa0`.

## Supported claims

- An exact MIT-form license is present at the frozen candidate commit.
- The notice names `dbh937`; it must be retained as written in copies or substantial portions.
- Public primary GitHub evidence strongly links the current `davish` account and Davis Haupt to the historical `dbh937` namespace.
- The mismatch alone does not justify blocking a small internal repair specimen when the original notice and source pointer are preserved.
- No attribution rewrite is needed. Preserving the original notice is lower risk than replacing `dbh937` with an inferred legal name.

## Excluded claims

- No formal GitHub account-rename receipt, government identity record, contributor agreement, copyright assignment, or independent legal-person verification was found.
- The evidence does not prove exclusive authorship, clean chain of title, patent clearance, trademark clearance, or absence of copied code.
- GitHub license detection does not audit hidden dependencies or provenance of every line.
- This card is not legal advice and does not establish commercial release readiness.
- No checkout, browser execution, network capture, repair, packaging, distribution, or demand test occurred.

## License and terms uncertainty

Remaining uncertainty is narrow but nonzero: the same-account gist linkage is strong provenance evidence, not a formal legal identity or rename record. A migrated gist or third-party reference is theoretically possible.

Minimum gate:

1. retain the exact `Copyright (c) 2013 dbh937` notice;
2. retain the MIT permission and warranty text;
3. record the frozen source repository, commit, and license blob;
4. do not substitute `davish` or `Davis Haupt` for `dbh937` without stronger authority;
5. route to a license reviewer only if the eventual consumer's commercialization policy requires legal-person chain-of-title confirmation.

## Cost and operator burden

- Research direct cost observed: `$0`.
- Operator minutes consumed/requested: `0 / 0`.
- Estimated producer burden to preserve notice and source metadata: `<5 minutes` within a future authorized repair WorkItem.
- Optional license-review burden if commercialization policy requires it: `10–20 reviewer minutes`, planning estimate only.
- Prior callback repair estimate remains `15–30 producer minutes`; distinct browser verification remains `20–35 minutes`. No work was performed.

## Strongest objection

A public profile plus historical gist is circumstantial. It could reflect imported content, a third-party license reference, or an account migration that does not establish legal ownership. Therefore the evidence is sufficient to remove the mismatch as an automatic engineering stop, but insufficient to rewrite attribution or assert legally verified authorship.

## Falsifier

This result falls to **UNKNOWN** or **RETIRE** if any of the following appears:

- primary history shows `dbh937` was a distinct person or unrelated source;
- the candidate license was copied from an unrelated repository without authority;
- substantial candidate code is shown to have incompatible provenance;
- a license reviewer rejects preserve-as-written use for the named commercial consumer; or
- the exact candidate license changes or disappears.

The candidate rises toward **ADMIT_DORMANT_CONTINUOUS_CONTROL_SPECIMEN** only after the separate startup repair receives a distinct browser-capable verdict and the preserved-license bytes are included in that exact repair digest.

## Verifier, consumer, and expiry

- Structural verifier: S04, `SAME_PROVIDER_NONBINDING`, binding weight `0`.
- Binding license verifier when required: distinct license reviewer or backlog owner operating under the eventual consumer's policy.
- Immediate consumer: `S09_PRODUCT_DECISION_QUEUE`, specifically the dormant continuous-control candidate decision inherited from the prior card.
- Backlog consumer: Spatial App Factory backlog owner; no producer route exists until a named continuous-control WorkItem consumes this card.
- Fitness credit: `0` pending exact WorkItem consumption and ConsumerAck.
- Expiry: `2026-09-01T00:00:00Z`, or immediately on candidate/license/history change or a new commercial consumer policy.

## Self-probe and effect receipt

- Expected and observed carrier task ID: `6a526109ba348191b5f23ad3172ad568`; exact match through native task inventory readback.
- Available surfaces used: native task inventory readback, authenticated GitHub search/read/write, primary public GitHub/web research, and Slack pointer after Git readback.
- Unavailable/not used: host checkout, shell, browser execution, network capture, legal review, distinct-provider verification.
- No task mutation, account creation, terms acceptance, outreach, application, purchase, spend, deployment, merge, public publication, private-data use, demand invention, or candidate implementation occurred.
