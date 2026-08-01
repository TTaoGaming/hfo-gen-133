# Instantly campaign setup checklist — Campaign 01

```yaml
status: TEMPLATE -- no Instantly API key or account access exists in this forge as of
        2026-07-31 (state/ssot/outreach_inventory_20260731.jsonl confirms zero prior
        Instantly references anywhere in the repo). Every step below is a manual
        operator action in the Instantly dashboard, not something a code lane can
        automate without API credentials being explicitly provided and wired.
companion: copy/campaign_01_sequence.md, targets/targets_template.csv,
           ../../DOMAIN_INVENTORY_AND_ROLES.md, RUNBOOK_KILL_SWITCH.md
operator_context: "purchased instantly, started warm up last night; purchased 1 main
                   domain and multiple throwaways" (2026-07-31 operator directive)
```

## 1 · Warmup status verification (do this FIRST, before anything else)

- [ ] Open Instantly → **Warmup** tab for every mailbox connected to this campaign.
- [ ] Confirm each mailbox shows warmup **active for at least 10-14 days** before it
      is added to a live sending campaign. Sending cold volume from a mailbox still in
      early warmup is the single fastest way to burn domain reputation before the
      campaign ever gets a fair test.
- [ ] Check the warmup **health score** / inbox-placement rate for each mailbox (Instantly
      surfaces this per-mailbox). Do not add a mailbox scoring noticeably below its
      peers — investigate first.
- [ ] Confirm SPF / DKIM / DMARC show **green/verified** in Instantly's own domain-health
      panel for whichever domain(s) the mailboxes sit on. Cross-check against
      `../../DOMAIN_INVENTORY_AND_ROLES.md` §3 — that doc's SPF/DKIM/DMARC templates were
      UNAPPLIED as of 2026-07-30; verify they've since been applied via Instantly's own
      onboarding flow (it issues its own DKIM selector/key at connect-time) rather than
      trusting the templates in that doc as already-live.

## 2 · Sending mailboxes

- [ ] Decide which domain sends cold volume. `DOMAIN_INVENTORY_AND_ROLES.md` §3.1
      recommends **not** sending from `hello@agentreleasegate.com` directly — reserve
      that for real replies — and instead sending from a mailbox on
      `obsidianspider.org` (or one of the "multiple throwaways" the operator purchased).
- [ ] Connect 2+ mailboxes if volume will exceed ~20-30/day per mailbox, so no single
      mailbox absorbs the full daily send cap (Instantly's own per-mailbox daily limits
      exist specifically to protect deliverability — respect them, don't override).
- [ ] Set each mailbox's **daily sending limit** conservatively for a first campaign —
      start low (e.g. 15-20/day/mailbox) and ramp, not the mailbox's max ceiling on day one.

## 3 · Target list upload

- [ ] Confirm every row in the upload CSV has `bounce_status = valid` per
      `schemas/target.v0_1.json` — `unknown` or `risky` rows are not upload-eligible for
      a live send; run them through Instantly's built-in verification (or a dedicated
      verifier) first.
- [ ] Map CSV columns to Instantly's custom variables exactly: `first_name` → `{{first_name}}`,
      `company` → `{{company}}`, `personalization_hook` → `{{personalization_hook}}`.
      Do not let Instantly auto-guess column mapping — confirm each field by hand.
- [ ] Confirm the uploaded list excludes anyone already on Instantly's global
      suppression/unsubscribe list from a prior campaign, if one exists.
- [ ] Spot-check 3-5 rows after upload: open the row in Instantly, confirm the merge
      preview renders the real hook text, not a blank or a literal `{{personalization_hook}}`.

## 4 · Sequence configuration

- [ ] Paste Email 1 subject + body from `copy/campaign_01_sequence.md` exactly — do not
      hand-edit inside the Instantly editor without re-running
      `scripts/lint_copy.py` (or its spec, `scripts/lint_copy.SPEC.md`, if not yet
      implemented) against the updated source file first.
- [ ] Set step delays: Email 2 at **+4 days**, Email 3 at **+6 days** after Email 2
      (per the sequence doc).
- [ ] Enable **auto-stop on reply** — a prospect who replies (including "not relevant")
      must not receive Email 2 or 3.
- [ ] Enable **auto-stop on bounce**.

## 5 · Sending limits (campaign-level, on top of per-mailbox limits in §2)

- [ ] Set a campaign-wide daily send cap for the first week that is well under the
      combined mailbox capacity — this is a first campaign against a live account
      still finishing warmup, not a scaled operation.
- [ ] Set sending hours/days to the prospect's business-hours timezone (Instantly
      supports timezone-based scheduling); do not send 24/7.

## 6 · Opt-out link and unsubscribe handling

- [ ] Confirm Instantly's **List-Unsubscribe header** is enabled for this campaign
      (required for CAN-SPAM compliance and for major mailbox providers not to flag
      the domain).
- [ ] Confirm the CAN-SPAM footer block from `copy/campaign_01_sequence.md` renders
      with a real `{{physical_mailing_address_or_po_box}}` — **this field was
      `blocked_missing` in the 2026-07-03 precedent packet
      (`inbox/gunnr/GUNNR_AGENTRELEASEGATE_FIRST_SEND_PACKET_20260703T170353Z.md`)**.
      Do not launch with a placeholder address.
- [ ] Test the unsubscribe link end-to-end from a personal test send before the real
      campaign goes live — click it, confirm it actually removes the test address.

## 7 · Reply detection

- [ ] Confirm Instantly's reply-detection is connected to the sending mailbox's inbox
      (not a separate unmonitored inbox) so "not relevant" replies actually pause the
      sequence per §4.
- [ ] Confirm a human (operator, or whoever is designated) is actually watching the
      Instantly unified inbox or a connected notification channel — a reply nobody
      reads is worse than no reply.

## 8 · Final pre-launch gate

- [ ] `scripts/lint_copy.py copy/campaign_01_sequence.md` (once a code lane
      materializes it from `scripts/lint_copy.SPEC.md`) exits 0.
- [ ] Operator has reviewed and approved the exact copy pasted into Instantly (not
      just the source markdown — the pasted version, in case of hand-edits).
- [ ] Operator has read `RUNBOOK_KILL_SWITCH.md` and knows the pause path before
      clicking launch.
- [ ] Operator clicks **Launch** in Instantly. This is the one manual action this
      whole scaffold exists to reduce everything else down to.
