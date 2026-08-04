---
schema_id: hfo.gen133.s08_evidence_card.v1
result: REVISE
card_id: S08_HTML5_SNAKE_LEGACY_HTML5SHIV_EXTERNAL_FETCH_BOUNDARY_20260804T183238Z
work_item_id: SPATIAL_FACTORY_HTML5_SNAKE_PENDING_DIRECTION_COMMAND_GATE_001
lane: SPATIAL_FOSS_CANDIDATES_AND_LICENSES
wip: 1
seat: S08_RESEARCH_CANDIDATE_SCOUT
carrier_task_id_expected: 6a526109ba348191b5f23ad3172ad568
carrier_task_id_observed: 6a526109ba348191b5f23ad3172ad568
carrier_task_id_match: true
valid_time_utc: 2026-08-04T18:32:38Z
transaction_time_utc: SEE_GITHUB_COMMIT_METADATA
canonical_repository: TTaoGaming/hfo-gen-133
canonical_branch: agent/gen133-bootstrap-20260730
consumer: SPATIAL_FACTORY_HTML5_SNAKE_PENDING_DIRECTION_COMMAND_GATE_001
verifier: DISTINCT_BROWSER_CAPABLE_NONPRODUCER_NETWORK_WITNESS
expiry_utc: 2026-08-11T18:32:38Z
fitness_credit: 0_PENDING_EXACT_WORKITEM_CONSUMPTION_DISTINCT_VERDICT_AND_CONSUMER_ACK
---

# S08 evidence card — remove the dormant unpinned Google Code script from the runnable Snake canary

## Self-probe

- Identity: expected and observed task ID match: `6a526109ba348191b5f23ad3172ad568`.
- Available: authenticated public GitHub reads, immutable GitHub file write/readback, current public-web research, Slack pointer post, trusted UTC clock.
- Unavailable or unused: target checkout, browser runtime, packet capture, dependency installation, private-source access, task mutation.

## Bounded changed uncertainty

The live successor newly requires **zero unexpected runtime network requests**. Does the exact approved upstream copy boundary contain a latent external executable reference that must be removed or explicitly classified before the canary can satisfy that gate?

## Exact candidate

- Repository: `JDStraughan/html5-snake` (public, archived).
- Approved source commit: `e3fe18a85a0555f0540cc0978fbab62822262a91`.
- Exact file: `index.html`.
- Exact blob: `61243962bab6846c3e06dba4358a547755dc1379`.
- Related visible-license file: `README.md`, blob `bf29f270d27882138d6e50868a212b4780502ca8`.

## Dated primary evidence

Observed 2026-08-04:

1. The exact upstream `index.html` contains an IE conditional-comment block whose body is an unversioned external script reference:
   `http://html5shiv.googlecode.com/svn/trunk/html5.js`.
   - https://github.com/JDStraughan/html5-snake/blob/e3fe18a85a0555f0540cc0978fbab62822262a91/index.html
2. The exact snapshot carries a complete MIT notice for `html5-snake`, attributed to Jason D. Straughan, in `README.md`.
   - https://github.com/JDStraughan/html5-snake/blob/e3fe18a85a0555f0540cc0978fbab62822262a91/README.md
3. The current WHATWG HTML parsing rules tokenize conforming `<!-- ... -->` markup as a comment; in a standards-conforming parser, the apparent script markup inside this block is not a `script` start tag. This supports—but does not replace—a Chromium/Firefox runtime witness.
   - https://html.spec.whatwg.org/multipage/parsing.html
   - https://html.spec.whatwg.org/multipage/syntax.html#comments
4. Google states that Google Code Project Hosting closed on 2016-01-25 and that remaining project data is served through a read-only archive. The candidate URL still points to the old HTTP `googlecode.com/svn/trunk` surface rather than a versioned local asset or digest-bound archive object.
   - https://opensource.googleblog.com/2015/03/farewell-to-google-code.html
   - https://code.google.com/archive/about

## Supported claims

- The approved upstream HTML contains a dormant, external, unpinned, cleartext-HTTP executable reference.
- In normal standards parsing, Chromium and Firefox should treat that block as a comment rather than execute it; this is a standards-based inference, not observed network evidence for the exact canary.
- The external response bytes, version, digest, availability, and applicable notice are not bound by the approved source commit.
- The runnable modern-browser canary does not need to retain this legacy external reference to preserve Snake gameplay.
- The exact upstream bytes may still be retained unchanged under a provenance-only `upstream/` subtree while the runnable derived `index.html` omits the conditional block.

## Excluded claims

- Chromium or Firefox made zero requests in the exact future canary; no browser was run.
- The old URL is currently dead, redirects safely, or serves any particular bytes.
- The external script is malicious or incompatibly licensed.
- Removing the block preserves Internet Explorer 6–8 compatibility or any configured Edge IE-mode behavior.
- The repository-level MIT notice proves the license or identity of bytes that might later be returned by the external URL.

## License and terms uncertainty

The visible MIT notice for the copied repository remains a strong license signal and must be preserved. The unresolved external asset is different: `svn/trunk/html5.js` is not content-addressed, version-pinned, locally vendored, or accompanied in this snapshot by its own bound notice. Do not fetch or vendor it for this WorkItem. Omission from the runnable derivative is the smaller and safer change.

## Decision — `REVISE`

Revise the implementation/provenance contract to classify the block as:

`LEGACY_CONDITIONAL_EXTERNAL_REFERENCE; NOT_AN_ALLOWED_RUNTIME_DEPENDENCY; OMIT_FROM_RUNNABLE_DERIVATIVE`

Required amendment:

1. Preserve the exact upstream `index.html` unchanged only in the provenance inventory if the producer keeps an `upstream/` copy.
2. Remove the entire IE conditional html5shiv block from the runnable canary HTML; do not replace it with a CDN or downloaded asset.
3. Record the deletion as an intentional derived-file delta in the provenance manifest.
4. Add a static assertion that runnable HTML contains no `googlecode.com`, no `html5shiv` URL, and no remote `script[src]`.
5. Bind the existing Chromium and Firefox network witness to the exact final checkout; classify any request beyond the local document/CSS/JS set as failure or typed `UNKNOWN`, not success.

## Strongest objection

The reference is inside a conditional comment and therefore dormant in modern Chromium and Firefox. Removing it adds patch surface without changing the measured modern-browser network behavior.

**Response:** correct for normal standards parsing, but the live acceptance gate is stronger than “probably dormant.” Keeping an unpinned cleartext executable URL creates needless legacy-mode and provenance ambiguity. Deleting six lines from the runnable derivative while preserving exact upstream bytes separately is lower risk than carrying or fetching the dependency.

## Falsifier

Retire or narrow this revision if a distinct browser-capable verifier proves, against the exact final checkout and both required browsers, that:

- the block is absent from the runnable derivative or provably inert;
- zero request is attempted to the referenced host under all supported launch modes;
- no supported runtime includes legacy IE document-mode processing; and
- the provenance manifest explicitly binds the retained upstream blob and derived deletion.

A request to the external host, a supported legacy mode that activates the block, or an attempt to vendor unbound response bytes would strengthen the revision.

## Cost and operator burden

- Research run: `$0` direct spend; `0` operator minutes.
- Producer amendment plus static assertion: `5–15` minutes.
- Distinct Chromium/Firefox network verification: `15–30` minutes.
- Operator action required now: `0` minutes.

## Honest flaw

No browser, network capture, legacy IE mode, or live URL retrieval was executed. The exact modern-browser no-request result remains for the named verifier; this card establishes the static dependency boundary and smallest safe amendment only.

## Effect receipt

No code implementation, browser execution, URL fetch, dependency download, task mutation, account or terms action, private-data use, outreach, application, purchase, send, spend, deployment, merge, publication, or public distribution occurred.
