---
schema_id: hfo.gen133.s08.evidence_card.v1
task_id_expected: 6a526109ba348191b5f23ad3172ad568
task_id_observed: 6a526109ba348191b5f23ad3172ad568
task_id_match: true
seat: S08_RESEARCH_AND_CANDIDATE_SCOUT
wip: 1
valid_time_utc: 2026-08-04T13:35:47Z
transaction_time_utc: SEE_GITHUB_COMMIT_METADATA
canonical_repository: TTaoGaming/hfo-gen-133
canonical_branch: agent/gen133-bootstrap-20260730
lane: spatial_foss_candidates_and_licenses
question_id: FIDELISRAFAEL_JS_SNAKE_UNAMBIGUOUS_LICENSE_GATE_001
decision: RETIRE
consumer: S02_ADMISSION_AND_PULL_FOR_ANY_FUTURE_SPATIAL_FACTORY_SUCCESSOR
expiry_utc: 2026-08-11T13:35:47Z
fitness_credit: 0_PENDING_EXACT_WORKITEM_CONSUMPTION_AND_CONSUMER_ACK
---

# RETIRE — `fidelisrafael/js-snake` has a three-way project-license conflict

## Self-probe

- Runtime identity matched expected task `6a526109ba348191b5f23ad3172ad568`.
- Available surfaces used: authenticated GitHub public-repository search/read and canonical-branch write/readback; Slack pointer post after Git readback.
- No shell checkout, dependency install, browser run, account action, task mutation, private-data use, send, spend, deployment, merge, or publication was authorized or performed.

## Changed bounded question

The active `JDStraughan/html5-snake` route entered `HOLD` after its immutable producer window closed. Before any future successor WorkItem considers another public Snake implementation, does exact candidate `fidelisrafael/js-snake@c3164c6e3ec8324fd57babe747f23490f36c558d` expose one unambiguous repository-wide license suitable for a clean-source spatial canary?

## Dated primary evidence

Observed 2026-08-04 against exact commit `c3164c6e3ec8324fd57babe747f23490f36c558d` (latest repository commit dated 2018-11-01):

1. Root `LICENSE` is the Unlicense text: public-domain dedication plus fallback broad permission and warranty disclaimer. Exact file/blob: `LICENSE` / `cf1ab25da0349f84a3fdd40032f0ce99db813b8b`.
   - <https://github.com/fidelisrafael/js-snake/blob/c3164c6e3ec8324fd57babe747f23490f36c558d/LICENSE>
2. Root `README.md` says: “The project is available as open source under the terms of the MIT License.” Exact file/blob: `README.md` / `409be1bd81e7cabafecb27f8cce9422d0aa3bf31`.
   - <https://github.com/fidelisrafael/js-snake/blob/c3164c6e3ec8324fd57babe747f23490f36c558d/README.md>
3. Root `package.json` declares `"license": "ISC"`. Exact file/blob: `package.json` / `23e99c9ad1c19d3f118c3a68481c383ed97cbf36`.
   - <https://github.com/fidelisrafael/js-snake/blob/c3164c6e3ec8324fd57babe747f23490f36c558d/package.json>
4. The repository history includes a merged pull request and development dependencies, but this bounded pass did not audit contributor assent, generated bundles, screenshots, dependency notices, or file-by-file provenance.
   - <https://github.com/fidelisrafael/js-snake/commit/56ce48424afec89a8e48ba2e4af349469dbf172b>

## Supported claims

- The exact candidate presents three incompatible project-level license declarations: Unlicense, MIT, and ISC.
- A consumer cannot truthfully describe the snapshot as unambiguously MIT-, ISC-, or Unlicense-governed without choosing a precedence rule that the repository itself does not state.
- The conflict is avoidable for the current golden-path purpose because other small Snake candidates already exist; accepting ambiguity creates no unique technical advantage.
- The candidate should therefore be removed from the **clean-source fallback shortlist** unless the upstream owner harmonizes the declarations or supplies an authoritative scope clarification.

## Excluded claims

- This card does not claim the code is illegal to use, that the Unlicense is universally invalid, or that a court would disregard the root `LICENSE` file.
- It does not establish contributor chain of title, patent rights, trademark rights, asset provenance, runtime correctness, accessibility, distribution demand, or production fitness.
- It does not admit this candidate into the current Snake WorkItem, replace its source pin, or create a new WorkItem.

## License and terms uncertainty

The root `LICENSE` is the strongest conventional repository signal, but the README and package metadata contradict it. The Unlicense also relies partly on public-domain dedication, whose effect varies by jurisdiction, and it contains no explicit patent grant. No upstream clarification, contributor agreement, or file-scope map was found in this bounded pass. Treating the conflict as harmless documentation drift would be a legal-policy assumption, not an observed fact.

## Strongest objection

A reasonable maintainer may say the root `LICENSE` controls and the MIT/ISC strings are stale metadata, making this candidate usable under the Unlicense. That may be correct in practice. It still fails the Gen-133 clean-source criterion: the factory would need to explain away two contradictory declarations and unresolved contributor/file scope for a candidate that offers no indispensable capability.

## Falsifier

Revise or retire this card if the upstream owner provides a dated authoritative clarification binding the whole exact snapshot and contributors to one license, or publishes a later commit that harmonizes `LICENSE`, `README.md`, and `package.json` while preserving an auditable provenance boundary.

## Verifier

`S07_LICENSE_DEPENDENCY_SECURITY_GATE` plus one distinct provenance reviewer should verify the three exact blobs and confirm that any future candidate packet either:

- records an upstream harmonized license snapshot, or
- keeps `fidelisrafael/js-snake` excluded from copied source and generated artifacts.

No same-provider prose review is terminal verification.

## Cost and operator estimate

- producer/license-gate packet update: 5–10 minutes
- distinct file-scope and contributor-history audit if reconsidered: 30–60 minutes
- likely upstream clarification effort: unknown and outreach-forbidden in this run
- paid cost: `$0`
- operator minutes this run: `0`

## Disposition

`RETIRE` from the clean-source spatial-factory fallback shortlist. This is not a permanent legal conclusion; it is a zero-trust admission decision under current evidence. Fitness remains zero until a named WorkItem consumes this exact card and receives distinct ConsumerAck.
