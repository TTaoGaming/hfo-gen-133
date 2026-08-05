---
schema_id: hfo.gen133.s08.evidence_card.v1
seat: S08_RESEARCH_AND_CANDIDATE_SCOUT
carrier_task_id_expected: 6a526109ba348191b5f23ad3172ad568
carrier_task_id_observed: 6a526109ba348191b5f23ad3172ad568
carrier_task_id_match: true
wip: 1
valid_time_utc: 2026-08-05T04:28:45Z
transaction_time_utc: SEE_GITHUB_COMMIT_METADATA
canonical_repository: TTaoGaming/hfo-gen-133
canonical_branch: agent/gen133-bootstrap-20260730
lane: spatial_foss_candidates_and_licenses
question_changed_from: projects/spatial-app-factory/research/20260804T233203Z_S08_HTML5_SNAKE_EXTERNAL_ANCHOR_NETWORK_BOUNDARY_EVIDENCE_CARD.md
question: Can the runnable derivative remove or inert the upstream external author/source links without violating the exact MIT attribution condition, provided the complete notice remains in the distributed artifact?
candidate_repository: JDStraughan/html5-snake
candidate_commit: e3fe18a85a0555f0540cc0978fbab62822262a91
candidate_index_blob: 61243962bab6846c3e06dba4358a547755dc1379
candidate_readme_license_blob: bf29f270d27882138d6e50868a212b4780502ca8
decision: REVISE
classification: EXTERNAL_HYPERLINKS_NOT_MIT_REQUIRED_FULL_NOTICE_MUST_SHIP
fitness_credit: 0
privacy_class: PUBLIC_REPOSITORY_SOURCE_AND_LICENSE_ONLY
expiry: 2026-08-12T04:28:45Z
sealed: false
---

# S08 evidence card — HTML5 Snake external-link attribution boundary

## Bounded result

**REVISE.** At the frozen candidate version, the runnable footer's clickable author-site and GitHub-source links are not part of the complete MIT permission notice and the exact MIT condition does not require a hyperlink or visible runtime advertising credit. They may be removed or rendered inert to close the deterministic zero-navigation boundary **only if** the distributed derivative still includes the complete upstream copyright and permission notice.

Required implementation classification:

```text
EXTERNAL_NAVIGATION_LINKS_MAY_BE_REMOVED
FULL_MIT_COPYRIGHT_AND_PERMISSION_NOTICE_MUST_SHIP
VISIBLE_OR_CLICKABLE_AUTHOR_LINK_NOT_PROVEN_REQUIRED
DISTRIBUTION_PLACEMENT_POLICY_REMAINS_CONSUMER_BOUND
```

This does not admit the candidate generally. Existing html5shiv, keyboard-policy, provenance, browser-verification, and producer-ingress gates remain separate.

## Dated primary evidence

Observed `2026-08-05`:

1. Exact candidate HTML: [`JDStraughan/html5-snake@index.html`](https://github.com/JDStraughan/html5-snake/blob/e3fe18a85a0555f0540cc0978fbab62822262a91/index.html), commit `e3fe18a85a0555f0540cc0978fbab62822262a91`, blob `61243962bab6846c3e06dba4358a547755dc1379`. Its footer displays `© 2013` and activates `http://JDStraughan.com` plus the GitHub repository; two Wikipedia anchors are also present.
2. Exact upstream license text: [`README.md`](https://github.com/JDStraughan/html5-snake/blob/e3fe18a85a0555f0540cc0978fbab62822262a91/README.md), blob `bf29f270d27882138d6e50868a212b4780502ca8`. It contains the full MIT grant, `Copyright (c) 2013 Jason D. Straughan`, and the condition that the copyright and permission notice be included in all copies or substantial portions.
3. Current SPDX MIT license page: [`MIT`](https://spdx.org/licenses/MIT), observed `2026-08-05`. The standard text contains the same notice-inclusion condition and no hyperlink, source-URL, or advertising clause.
4. Immediate predecessor: [`20260804T233203Z_S08_HTML5_SNAKE_EXTERNAL_ANCHOR_NETWORK_BOUNDARY_EVIDENCE_CARD.md`](https://github.com/TTaoGaming/hfo-gen-133/blob/a382f733d45319ac4d7debc99b5a83813267e380/projects/spatial-app-factory/research/20260804T233203Z_S08_HTML5_SNAKE_EXTERNAL_ANCHOR_NETWORK_BOUNDARY_EVIDENCE_CARD.md), which requires zero activatable external navigation in the runnable canary.

## Supported claims

- The frozen candidate carries a complete MIT-form notice naming Jason D. Straughan.
- The exact MIT condition requires preservation of the copyright and permission notice in copies or substantial portions.
- The upstream author-site and repository URLs are ordinary HTML anchors outside the full license text.
- No separate license, NOTICE, advertising clause, or source-link requirement was found in the exact candidate files inspected for this question.
- Removing clickable links while shipping the complete notice is consistent with the text of the frozen MIT grant.
- Keeping a local, non-clickable provenance record is a useful engineering control, but this card does not claim that MIT itself requires that exact presentation.

## Excluded claims

- This is not legal advice and does not prove chain of title, exclusive authorship, patent clearance, trademark clearance, or absence of copied code.
- It does not prove that a LICENSE file left only in a source repository accompanies a deployed browser copy.
- It does not settle whether a specific store, marketplace, customer contract, or deployment mode requires an in-product acknowledgements surface.
- It does not authorize deleting or abbreviating the complete MIT notice from the bytes actually distributed.
- It does not resolve the previously identified html5shiv URL, keyboard input policy, external-network verification, or file-origin history.
- No checkout, implementation, browser execution, packaging, distribution, or legal review occurred.

## License and terms uncertainty

The remaining material uncertainty is **placement**, not hyperlink retention. A public browser deployment may deliver only HTML, CSS, and JavaScript; a LICENSE file that exists solely in Git history may not accompany the received copy. The exact MIT text does not specify UI placement, but the producer should fail closed by ensuring the full notice is present in the shipped artifact and reachable without external navigation.

Minimum packaging gate:

1. preserve the exact full MIT copyright, permission, and warranty text;
2. include it in the actual derivative distribution, not only the development repository;
3. retain frozen source repository, commit, and license-blob provenance locally;
4. replace external anchors with inert text or a local provenance/about reference;
5. statically reject external navigation URLs in the runnable canary;
6. route to a license reviewer if the named consumer requires visible in-product attribution or a marketplace-specific notice format.

## Cost and operator burden

- Research direct cost observed: `$0`.
- Operator minutes consumed/requested: `0 / 0`.
- Producer amendment estimate: `5–10 minutes` to inert links and add a local notice/provenance surface.
- Static packaging-test estimate: `10–20 minutes`.
- Optional consumer-specific license review: `10–20 reviewer minutes`.
- Estimates are planning ranges; no work was performed.

## Strongest objection

For a web application, the end user may receive only the runtime files. Removing the visible source link while leaving the full MIT notice in an unshipped repository could make the notice effectively absent from the distributed copy. Therefore link removal is admissible only with a distribution-artifact test proving the complete notice actually ships; a repository-only LICENSE is insufficient evidence.

## Falsifier

This result falls to **UNKNOWN** or **RETIRE** if any of the following appears:

- a separate upstream term requires visible hyperlink attribution or preservation of the footer;
- the derivative distribution omits the complete MIT notice;
- the notice is shortened to the copyright line without the permission and warranty text;
- a named marketplace, customer, or license reviewer requires a different attribution placement for the exact delivery mode; or
- the frozen candidate license or inspected source changes.

It rises toward **ADMIT_FOR_DETERMINISTIC_CANARY_PACKAGING** only after a distinct verifier confirms zero external navigation and exact full-notice presence in the actual packaged bytes.

## Verifier, consumer, and expiry

- Structural verifier: S04, `SAME_PROVIDER_NONBINDING`, binding weight `0`.
- Binding verifier: `DISTINCT_LICENSE_AND_DISTRIBUTION_ARTIFACT_INVENTORY_VERIFIER`.
- Immediate consumer: `SPATIAL_FACTORY_HTML5_SNAKE_PENDING_DIRECTION_COMMAND_GATE_001` or its fresh successor claim.
- Backlog consumer: any deterministic-canary packaging WorkItem using this exact candidate commit.
- Fitness credit: `0` pending exact WorkItem consumption, distribution-artifact verification, and ConsumerAck.
- Expiry: `2026-08-12T04:28:45Z`, or immediately on candidate/license/distribution-mode change.

## Self-probe and effect receipt

- Expected and observed task ID: `6a526109ba348191b5f23ad3172ad568`; exact match through native task inventory readback.
- Available surfaces used: native task inventory, authenticated GitHub read/write, public primary repository/license research, and Slack pointer after Git readback.
- Unavailable/not used: host checkout, shell, browser execution, package build, marketplace terms acceptance, legal review, or distinct-provider verification.
- No task mutation, account creation, terms acceptance, outreach, application, purchase, send, spend, deployment, merge, public release, private-data use, demand invention, or candidate implementation occurred.
