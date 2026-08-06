# S08 Evidence Card — RFC 2606 HTML fixed-marker / reissue boundary

```yaml
schema_id: hfo.gen133.s08.evidence_card.v1
task_id_expected: 6a526109ba348191b5f23ad3172ad568
task_id_probe: MATCHED_FROM_RUNTIME_INSTRUCTION
seat: S08_RESEARCH_AND_CANDIDATE_SCOUT
wip: 1
observed_utc: 2026-08-06T17:28:31Z
lane: agent_runtime_cots_capabilities
changed_queue_question:
  source: state/coordination/experiments/carrier_surface_x11/CURRENT.yaml
  source_version: 140
  experiment_id: X11_WEB_FIXED_RFC_EDITOR_READ_V1
  bounded_uncertainty: whether_the_RFC_2606_HTML_URL_and_single_title_marker_are_a_valid_fixed_public_web_retrieval_probe_without_implying_immutable_bytes_origin_authenticity_or_general_web_capability
candidate:
  publisher: RFC Editor
  document: RFC 2606 / BCP 32
  publication_date: 1999-06
  current_html_url: https://www.rfc-editor.org/rfc/rfc2606.html
  info_url: https://www.rfc-editor.org/info/rfc2606/
  queue_marker: Reserved Top Level DNS Names
decision: REVISE
consumer: X11_WEB_FIXED_RFC_EDITOR_READ_V1_WAKE_1_RESULT_SEMANTICS_GATE
verifier: DISTINCT_DIRECT_HTTP_STATUS_FINAL_URL_RFC_IDENTITY_AND_TWO_MARKER_VERIFIER
expiry_utc: 2026-08-13T17:28:31Z
fitness_credit: 0_pending_WorkItem_consumption_and_ConsumerAck
```

## Self-probe

Available in this wake: branch-specific GitHub file read/write/readback, current public-web open/search, and Slack channel posting. Not exposed by the web surface: raw TLS certificate, request ID, cache path, authoritative DNS resolution, raw response headers, reliable request latency, or an independently controlled network path.

## Primary evidence observed 2026-08-06

1. The exact queue URL resolved on the exposed web surface to `www.rfc-editor.org/rfc/rfc2606.html`. The returned document identifies `Request for Comments: 2606`, `BCP: 32`, `June 1999`, and contains the queue marker `Reserved Top Level DNS Names` near the document header.
   - Source: RFC Editor, RFC 2606 HTML, accessed 2026-08-06: https://www.rfc-editor.org/rfc/rfc2606.html
2. The official RFC information page identifies RFC 2606 as BCP 32, notes that it was updated by RFC 6761, and exposes HTML and TXT formats. This supports document identity but also shows that current technical status is metadata outside the old document body.
   - Source: RFC Editor, RFC 2606 information page, accessed 2026-08-06: https://www.rfc-editor.org/info/rfc2606/
3. Current RFC Series policy distinguishes semantic content from publication presentation. RFC 9720 allows publication versions to be updated under narrowly limited rules, and RFC 9920 states that RFCs may be reissued while semantic content should be preserved to the greatest extent possible. Therefore the HTML representation is archival, but not a documented immutable-byte object.
   - Source: RFC Editor, RFC 9720, accessed 2026-08-06: https://www.rfc-editor.org/info/rfc9720/
   - Source: RFC Editor, RFC 9920, published February 2026 and accessed 2026-08-06: https://www.rfc-editor.org/info/rfc9920/
4. RFC 2606 contains an older Internet Society copyright statement permitting copying and explanatory derivatives with notice conditions while restricting modification of the document itself. This probe reads two short identity markers and does not redistribute or modify the RFC.
   - Source: RFC Editor, RFC 2606 full copyright statement, accessed 2026-08-06: https://www.rfc-editor.org/rfc/rfc2606.html

## Supported claims

- At this observation time, the exposed public-web surface retrieved the official RFC Editor host and exposed the queue title marker.
- The candidate is suitable as a cheap, read-only canary for one narrow public HTML retrieval path.
- Using the RFC number plus title gives a stronger document-identity check than title alone.

## Excluded claims

- Immutable bytes, immutable markup, permanent title-marker survival, or deterministic rendering across wakes.
- Raw HTTP status, TLS/origin authenticity, DNS independence, cache/proxy independence, or direct-network parity.
- General web breadth, search capability, JavaScript/browser parity, freshness guarantees, unattended durability, or independent verification.
- Technical currency of RFC 2606 by itself; the RFC Editor metadata explicitly notes RFC 6761 as an update.

## Required revision

Retain the exact URL, but rename the probe from a `fixed page` witness to a `current official representation marker canary`.

Persist these bounded fields only:

```text
provider_call_success
observed_final_host_boolean
rfc_number_marker_present = "Request for Comments: 2606" OR equivalent rendered RFC 2606 identity
queue_title_marker_present = "Reserved Top Level DNS Names"
permission_class
error_class
latency_when_exposed
operator_relay_minutes
```

Do not treat a later markup, whitespace, template, redirect, or auxiliary-metadata change as connector failure unless a distinct direct-HTTP verifier shows that the official document identity or semantic title is unavailable.

## License / terms uncertainty

- The document-level copyright statement is visible and sufficient for this non-redistributive marker check.
- The RFC Editor/IETF site-wide automation, rate-limit, privacy, and acceptable-use terms were not exhaustively audited in this bounded card.
- No bulk retrieval, scraping campaign, account use, cookies, or private data were involved.

## Strongest objection

Semantic-content preservation makes the RFC number and title unusually durable, so the existing single-marker probe is probably operationally adequate.

**Response:** agreed for a low-cost canary. The revision is not a rejection of the probe; it prevents the canary from being promoted into an immutable-page, origin-authenticity, or general-web-capability claim.

## Falsifier

Move this boundary toward `ADMIT` without revision only if a distinct verifier demonstrates all of the following in the same bounded time window:

1. direct HTTP returns success for the exact URL;
2. the final URL remains on `www.rfc-editor.org`;
3. both RFC identity and title markers are present;
4. no unexpected authentication, personalization, or private state is required; and
5. the resulting claim remains explicitly limited to current official-representation retrieval.

Revise further or retire the candidate if the official URL stops exposing RFC identity/title, requires stateful interaction, or repeatedly disagrees with a direct same-window HTTP witness.

## Cost and execution estimate

```yaml
research_spend_usd: 0
operator_minutes: 0
producer_amendment_minutes: 3-7
distinct_verification_minutes: 10-20
```

## Prohibited-effect receipt

No task mutation, account creation, terms acceptance, outreach, application, purchase, send, spend, deployment, merge, private-data use, or external publication occurred. The only intended external effect after Git readback is one material Slack pointer required by the seat contract.
