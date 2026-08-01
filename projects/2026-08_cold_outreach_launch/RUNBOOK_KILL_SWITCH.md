# Kill-switch runbook — Campaign 01 (and any future Instantly campaign)

```yaml
status: TEMPLATE -- written before any campaign has launched. Steps below describe
        Instantly's dashboard as documented by Instantly's own product; verify exact
        button locations against the live dashboard the first time this runbook is
        used, since UI details drift and this was authored without live account access.
companion: INSTANTLY_CAMPAIGN_SETUP_CHECKLIST.md, copy/campaign_01_sequence.md
```

## 1 · How to pause in under 60 seconds

**Fastest path — pause the one campaign:**
1. Log into Instantly.
2. Go to **Campaigns**.
3. Open the running campaign.
4. Click **Pause Campaign** (top-right of the campaign view). This stops all future
   sends immediately; emails already queued/sent are not recalled.

**Backup path — pause everything on the account:**
1. Instantly → **Account Settings** (or the workspace-level settings menu).
2. Look for a global **Pause all campaigns** / **Pause sending** control, or pause each
   active campaign individually from the Campaigns list if no single global toggle
   exists at the account's current plan tier.
3. As a hard backup with zero dependency on finding the right button: disconnect the
   sending mailbox(es) from **Mailboxes → [mailbox] → Disconnect**. This physically
   stops Instantly from being able to send through that account, independent of any
   campaign-level setting.

Whichever path is used, **confirm the pause took effect** — check the campaign status
badge flips to "Paused" and no new sends appear in the Instantly activity log in the
next few minutes.

## 2 · Trigger conditions — pause immediately if any of these fire

| Trigger | Threshold | Where to check |
|---|---|---|
| Spam complaint rate | `> 0.1%` of sends in any rolling 24h window | Instantly campaign analytics → Spam/Complaints |
| Bounce rate | `> 3%` of sends in any rolling 24h window | Instantly campaign analytics → Bounces |
| Negative reply spike | any cluster of 2+ hostile/angry replies in a short window (not just "not relevant") | Instantly unified inbox |
| Domain reputation drop | mailbox health score drops noticeably from its warmup baseline, or a mailbox provider (Gmail/Outlook) starts routing sends to spam | Instantly domain-health panel; ask a colleague to check their own spam folder |
| Operator says halt | any explicit "stop", "pause", "halt" from the operator, in any channel | — always highest priority, overrides all other judgment |

**When in doubt, pause first, investigate second.** A paused campaign that turns out
fine costs a few hours of delay. A campaign left running past a real trigger costs
domain reputation that takes weeks to rebuild.

## 3 · Post-kill checklist

- [ ] **Record the exact trigger** — which threshold fired, the actual number observed,
      and the timestamp. Do not rely on memory; write it down before analyzing.
- [ ] **Pull the last 20 sends** before the pause and read them for an obvious copy
      problem (a broken merge field, a tone mismatch, a factual error in a
      personalization hook).
- [ ] **Check bounce_status on the specific rows that bounced** — was it a data-quality
      problem (stale/invalid emails that should have been caught in validation) or a
      deliverability problem (the mailbox itself getting blocked)?
- [ ] **Patch copy** if the trigger points to copy — re-run
      `scripts/lint_copy.py` (or the spec at `scripts/lint_copy.SPEC.md` if not yet
      implemented) against the revised sequence before it goes back out.
- [ ] **Patch the target list** if the trigger points to data quality — tighten the
      `email_confidence` / `bounce_status` bar in `schemas/target.v0_1.json` before
      re-uploading.
- [ ] **Get explicit operator sign-off before resuming.** A paused campaign does not
      restart itself — resuming is the same class of decision as the original launch
      approval, not a default.
- [ ] **Log the incident** — a short note (trigger, root cause, fix, resume decision)
      belongs in this project's history so the next campaign doesn't repeat the same
      failure mode.
