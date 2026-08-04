# S08 Evidence Card — HTML5 Snake external-anchor network boundary

- **valid_time_utc:** `2026-08-04T23:32:03Z`
- **task_id_expected:** `6a526109ba348191b5f23ad3172ad568`
- **task_id_observed:** `6a526109ba348191b5f23ad3172ad568` from the automation runtime envelope
- **task_id_match:** `true`
- **seat / WIP:** `S08 Research and Candidate Scout / 1`
- **lane:** `spatial FOSS candidates and licenses`
- **decision:** `REVISE`
- **bounded uncertainty:** After removing the already-rejected html5shiv block, is the approved Snake snapshot fully zero-network, or only startup dependency-local?

## Exact candidate

- Repository: `JDStraughan/html5-snake`
- Approved commit: `e3fe18a85a0555f0540cc0978fbab62822262a91`
- Approved files and blobs:
  - `README.md` — `bf29f270d27882138d6e50868a212b4780502ca8`
  - `index.html` — `61243962bab6846c3e06dba4358a547755dc1379`
  - `page.css` — `f380cefc081c1bac889330465f311195dbb83ab4`
  - `game.js` — `c286389487bd68f15170fbb3add6a060f252d169`
- Current consumer claim: `SPATIAL_FACTORY_HTML5_SNAKE_PENDING_DIRECTION_COMMAND_GATE_001`, successor commit `33d008a06da0f1c6256c62f882a735db2d5ff691`.

## Evidence

Primary snapshot reads on `2026-08-04`:

1. `index.html` contains the known cleartext html5shiv script block, plus local automatic-load references to `page.css` and `game.js`. It also contains four external navigation anchors: two `http://en.wikipedia.org/...`, one `http://JDStraughan.com`, and one `https://github.com/JDStraughan/html5-snake`. Source: https://github.com/JDStraughan/html5-snake/blob/e3fe18a85a0555f0540cc0978fbab62822262a91/index.html
2. `page.css` contains no `url()`, `@import`, font-face, image, audio, or other resource reference. Source: https://github.com/JDStraughan/html5-snake/blob/e3fe18a85a0555f0540cc0978fbab62822262a91/page.css
3. `game.js` uses canvas, timers, animation-frame aliases, keyboard input, and in-memory objects only. It contains no `fetch`, XHR, WebSocket, EventSource, Worker, dynamic import, module import, `require`, image/audio constructor, service-worker registration, or storage-backed dependency. Source: https://github.com/JDStraughan/html5-snake/blob/e3fe18a85a0555f0540cc0978fbab62822262a91/game.js
4. The exact README embeds the complete MIT notice naming Jason D. Straughan and requires preservation of the notice in copies or substantial portions. Source: https://github.com/JDStraughan/html5-snake/blob/e3fe18a85a0555f0540cc0978fbab62822262a91/README.md
5. Browser contract: `<link rel="stylesheet">` and `<script src>` load referenced resources, while `<a href>` creates a hyperlink activated by user action such as click or Enter. Sources retrieved `2026-08-04`: https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/link ; https://developer.mozilla.org/en-US/docs/Web/HTML/How_to/Add_JavaScript_to_your_web_page ; https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/a

## Supported claims

- Once the entire html5shiv conditional block is removed, the exact snapshot has no remaining **automatic remote code or asset dependency visible in the four approved files**.
- The remaining startup resources are the local sibling files `page.css` and `game.js`.
- The runnable page is **not interaction-closed zero-network** while the four external anchors remain active: a click or keyboard activation can navigate away and initiate network activity.
- Therefore `ZERO_REMOTE_STARTUP_DEPENDENCY` is supportable from static inspection; unrestricted `ZERO_NETWORK_SURFACE` is not.

## Excluded claims

- No browser execution or packet capture occurred; no claim is made that Chromium or Firefox emitted zero requests.
- This card does not prove absence of browser favicon probes, extension traffic, service-worker interference, target-host rewrites, CSP behavior, or user-agent-specific requests.
- It does not prove source-code authorship, contributor assignments, or public-distribution chain of title.
- It does not license or authenticate bytes that might have been returned by the removed Google Code URL.
- It does not authorize publication, deployment, or distribution.

## Required revision

For the internal deterministic canary:

1. Preserve the exact upstream `index.html` only in the provenance inventory.
2. In the runnable derivative, remove the html5shiv block as already required.
3. Replace the four external `<a href>` elements with inert text or local provenance-only references. Do not replace them with redirects, tracking URLs, CDN URLs, or runtime fetches.
4. Add two separate static assertions:
   - `AUTOLOAD_REMOTE_REF_COUNT == 0` for `script[src]`, stylesheet links, imports, CSS URLs, media, workers, and network APIs.
   - `EXTERNAL_NAVIGATION_REF_COUNT == 0` for runnable anchors/forms.
5. Retain distinct Chromium and Firefox network capture on the exact final checkout. Any request outside the exact local document, stylesheet, and script inventory is `FAIL` or typed `UNKNOWN`, not silently ignored.

## License / terms uncertainty

- **Visible license signal:** complete MIT notice is present in exact `README.md`; preserve it verbatim in the derivative and provenance inventory.
- **Bundled third-party asset finding:** none found in the exact four-file snapshot after excluding the html5shiv reference.
- **Still open:** preexisting file-origin history and public-distribution chain of title remain `NOT_STOOD`; this card narrows dependency surface only.
- **Repository state:** public and archived/read-only at observation; archival status does not revoke the visible MIT grant but also does not cure provenance uncertainty.

## Economics and verification

- **research spend surfaced:** `$0`
- **operator minutes consumed:** `0`
- **producer revision estimate:** `5–15 minutes`
- **static-test estimate:** `10–20 minutes`
- **two-browser network verification estimate:** `20–40 minutes`
- **strongest objection:** External anchors are ordinary attribution/documentation links, not runtime dependencies, so removing them may be unnecessary. Response: correct for a normal website, but the current canary requires deterministic zero-unexpected-network evidence; leaving activatable external navigation makes that broader claim false or underspecified.
- **falsifier:** A distinct verifier demonstrates, on the exact final checkout, that active external anchors are intentionally permitted by a narrower named contract and cannot be activated by any tested native or spatial path, with zero out-of-inventory requests in Chromium and Firefox. That would permit revising this card to `ADMIT_WITH_NAVIGATION_EXCEPTION`.
- **verifier:** `DISTINCT_STATIC_RESOURCE_INVENTORY_AND_CHROMIUM_FIREFOX_NETWORK_CAPTURE`
- **consumer:** `SPATIAL_FACTORY_HTML5_SNAKE_PENDING_DIRECTION_COMMAND_GATE_001` and its exact unexpired successor only
- **expiry_utc:** `2026-08-11T23:32:03Z`
- **fitness:** `0` until exact WorkItem consumption, distinct verification, and ConsumerAck

No implementation, browser execution, task mutation, account action, terms acceptance, outreach, application, purchase, send, spend, deployment, merge, publication, or private-data use occurred.
