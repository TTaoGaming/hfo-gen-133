---
schema_id: hfo.gen133.s08_evidence_card.v1
seat: S08_RESEARCH_AND_CANDIDATE_SCOUT
carrier_task_id_expected: 6a526109ba348191b5f23ad3172ad568
carrier_task_id_observed: 6a526109ba348191b5f23ad3172ad568
carrier_task_id_match: true
wip: 1
valid_time_utc: 2026-08-05T15:31:17Z
canonical_repository: TTaoGaming/hfo-gen-133
canonical_branch: agent/gen133-bootstrap-20260730
lane: spatial_foss_candidates_and_licenses
decision: REVISE
expiry_utc: 2026-08-12T15:31:17Z
consumer: SPATIAL_FACTORY_HTML5_SNAKE_PENDING_DIRECTION_COMMAND_GATE_001_OR_FRESH_SUCCESSOR
verifier: DISTINCT_EXACT_SHA_OFFLINE_NETWORK_REQUEST_AND_LICENSE_INVENTORY_VERIFIER
---

# S08 evidence card — remove the unpinned Google Code HTML5 Shiv reference from the modern package

## Bounded uncertainty

Does the exact pinned HTML5 Snake candidate have a reproducible, license-bound runtime dependency on the remote HTML5 Shiv script referenced by `index.html`, or can that reference be removed from the modern Chromium/Firefox canary package?

## Exact candidate

- Upstream repository: `JDStraughan/html5-snake`
- Exact source SHA: `e3fe18a85a0555f0540cc0978fbab62822262a91`
- Exact `index.html` blob: `61243962bab6846c3e06dba4358a547755dc1379`
- Exact `game.js` blob: `c286389487bd68f15170fbb3add6a060f252d169`
- External executable reference in the pinned `index.html`:

```html
<!--[if IE]>
<script src="http://html5shiv.googlecode.com/svn/trunk/html5.js"></script>
<![endif]-->
```

## Evidence

1. The exact pinned `index.html` contains an Internet Explorer conditional block loading an unversioned `svn/trunk` JavaScript resource over plaintext HTTP. The stylesheet and game script are otherwise referenced locally. Source: https://github.com/JDStraughan/html5-snake/blob/e3fe18a85a0555f0540cc0978fbab62822262a91/index.html (exact blob above; read 2026-08-05).
2. The exact pinned `game.js` immediately obtains a Canvas 2D context through `canvas.getContext("2d")`; the game therefore needs actual Canvas 2D support, not merely recognition or styling of HTML5 sectioning elements. Source: https://github.com/JDStraughan/html5-snake/blob/e3fe18a85a0555f0540cc0978fbab62822262a91/game.js (exact blob above; read 2026-08-05).
3. Google's official shutdown notice states that Google Code project hosting went read-only on 2015-08-24 and closed on 2016-01-25. This makes an unpinned Google Code `svn/trunk` URL unsuitable as a reproducible dependency locator. Source: https://opensource.googleblog.com/2015/03/farewell-to-google-code.html (published 2015-03-12; accessed 2026-08-05).
4. Microsoft's archived browser guidance states that IE8 and older execute matching conditional-comment blocks, while other browsers, including IE10, treat the block as a comment and ignore it. The same guidance distinguishes Canvas polyfills from ordinary HTML5 element shims and says pre-IE9 browsers lack `getContext`. Source: https://learn.microsoft.com/en-us/archive/msdn-magazine/2012/january/building-html5-applications-using-html5-canvas-for-data-visualization (accessed 2026-08-05).
5. The current `aFarkas/html5shiv` project describes HTML5 Shiv as enabling HTML5 sectioning elements, basic styling, and `createElement`/`createDocumentFragment` shims for legacy browsers. It does not claim to implement the Canvas 2D drawing context. Source: https://github.com/aFarkas/html5shiv/blob/daa5fd1169cf8c1b63b0659754b4d13b037c0e54/readme.md (exact blob `3dee669202ae631f3733d0df8d966cd96babcb20`; read 2026-08-05).
6. The current html5shiv repository at that commit contains a dual MIT-or-GPL-2 license file. No evidence found in the Snake pin binds the historical unversioned Google Code `svn/trunk/html5.js` response to that exact repository commit, blob, version, or license choice. Source: https://github.com/aFarkas/html5shiv/blob/daa5fd1169cf8c1b63b0659754b4d13b037c0e54/MIT%20and%20GPL2%20licenses.md (exact blob `a9538ee4ee865ce48a5707cd5b3d906b1819b274`; read 2026-08-05).

## Supported claims

- `REMOTE_EXECUTABLE_REFERENCE_PRESENT_IN_PINNED_INDEX=true`
- `REMOTE_REFERENCE_SCHEME=PLAINTEXT_HTTP`
- `REMOTE_REFERENCE_VERSION=UNPINNED_SVN_TRUNK`
- `GOOGLE_CODE_PROJECT_HOSTING_CLOSED_2016_01_25=true`
- `MODERN_CHROMIUM_FIREFOX_RUNTIME_DEPENDENCY_ON_THIS_CONDITIONAL_BLOCK=NOT_SUPPORTED`
- `EXACT_HISTORICAL_HTML5SHIV_VERSION_BLOB_AND_LICENSE_BINDING=UNKNOWN`
- `CANVAS_2D_COMPATIBILITY_FROM_HTML5SHIV=NOT_SUPPORTED`
- For the declared modern Chromium/Firefox canary, remove the entire conditional block rather than preserve an unpinned remote executable reference.
- If a separate legacy-IE variant is ever authorized, vendor an exact dependency locally with hash and license inventory, then separately prove the required Canvas 2D behavior; HTML5 Shiv alone is not that proof.

## Excluded claims

- No claim that the historical URL currently resolves, fails, redirects, or serves malicious content; no network request was made.
- No claim about the exact bytes Google Code served in 2013 or at any later date.
- No claim that every Internet Explorer document mode handles this exact `[if IE]` block identically.
- No claim that removing the block proves all application bytes are third-party-free, secure, accessible, or public-distribution-ready.
- No claim that the current html5shiv repository's dual license automatically governs the unknown historical `svn/trunk` response.
- No claim of legacy IE compatibility, modern-browser conformance, or zero external requests without an exact packaged-byte browser trace.

## License and terms uncertainty

- Snake exact-pin license evidence remains the complete MIT notice in its `README.md`.
- The remote html5shiv artifact has no version, immutable blob, integrity digest, vendored notice, or license-selection record in the Snake pin.
- The current html5shiv repository offers MIT or GPL-2, but applicability to the unknown historical remote bytes is `NOT_BOUND`.
- Removing the remote script reference and copying no html5shiv bytes avoids claiming that unknown artifact as part of the modern package.
- Vendoring any chosen html5shiv version would require a new exact-SHA byte and notice inventory; this card does not select a version or license.
- Public-distribution chain of title remains `NOT_STOOD`.

## Strongest objection

Modern browsers ignore Internet Explorer conditional comments, so the line is dead code in the current canary and causes no modern runtime request. Correct: that is why removal is low-risk. Keeping the line still leaves the source bundle with an unpinned executable locator, an undeclared legacy-support branch, and no exact dependency or license binding. The modern package should express its real support boundary by deleting the block, not by relying on browser-specific nonexecution.

## Falsifier

Revise this decision if a distinct verifier shows that the exact target package intentionally supports a named legacy IE mode and that all of the following are bound and reproduced:

- an exact local html5shiv or other compatibility dependency blob, version, hash, and applicable license notice;
- a typed support matrix explaining why that dependency is necessary;
- an exact-browser test proving required Canvas 2D behavior, not only HTML5 element recognition;
- an offline package trace showing no unapproved remote executable retrieval.

For the modern-only route, this card is falsified only if exact-sha Chromium and Firefox tests show removal of the conditional block changes accepted application behavior.

## Verification contract

A distinct verifier should:

1. fetch `index.html` and `game.js` from the exact Snake SHA and verify the declared blobs;
2. inventory every executable and stylesheet reference in the produced package;
3. confirm the Google Code conditional block is absent from modern packaged bytes;
4. run the package in Chromium and Firefox with network logging and prove zero remote executable requests for the application path;
5. confirm the complete Snake MIT notice is packaged locally;
6. fail closed if any unpinned remote executable locator, copied unlicensed dependency, byte mismatch, or undeclared legacy-support path remains.

## Cost and operator-minute estimate

- This research pass: `$0`; `0 operator minutes`.
- Producer amendment to remove the conditional block and update the dependency inventory: `5–15 minutes`.
- Exact-package inventory plus Chromium/Firefox offline network trace: `15–30 minutes`.
- A separately authorized legacy-browser compatibility path: `60–180+ minutes`; environment and legal-review costs unknown.

## Decision

`REVISE`

Remove the unpinned plaintext-HTTP Google Code HTML5 Shiv reference from the modern package. Do not claim that it is a modern runtime dependency, a Canvas polyfill, or license-bound to the current html5shiv repository. A future legacy route must vendor exact bytes and independently prove Canvas compatibility.

## Fitness

`0` until an exact WorkItem consumes this card and a distinct verifier returns a bound verdict plus ConsumerAck.

## Effect boundary

No implementation, browser execution, network fetch of the remote dependency, dependency download, task mutation, account action, terms acceptance, outreach, application, purchase, send, spend, deployment, merge, release, public publication, or private-data use occurred. The only authorized effects are this internal Git evidence write, exact readback, and one material Slack pointer after readback.
