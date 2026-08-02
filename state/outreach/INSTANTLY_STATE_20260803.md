---
type: AIH2O
callsign: cold_email_executor
generation: 133
substrate: claude_code
model: claude-opus-5
timestamp_utc: 2026-08-02T20:00:00Z
task: instantly_account_state_probe
schema_id: hfo.aih2o_header.v0_1
clock_source: host_read
claim_status: partial_blocked
---

# Instantly Account State — 2026-08-03

## HEADLINE: BLOCKED — no Instantly API key found anywhere in known credential stores.

Every downstream verification (domain warm state, sending-account count, mailbox count, daily-limit config, suppression list) requires this key. Cannot probe live.

## What was checked

| location | result |
|---|---|
| `C:\Dev\hfo_gen_133_forge\.env` | placeholder only (SLACK_WEBHOOK_URL={{FROM_SIGRUN_SECRETS}}). No INSTANTLY_API_KEY. |
| `C:\Dev\hfo_gen_133_forge\sigrun-secrets\` | **does not exist** (confirmed via `inbox/olrun/20260801T180312Z_sigrun_secrets_inventory.md`) |
| `C:\Dev\hfo_gen_131_forge\state\sigrun_secrets\.env` | key names cataloged in gen-131 inventory row of `state/ssot/grimoire_secrets_locations_20260801.jsonl` — **INSTANTLY_API_KEY is NOT among the listed keys** (only Cerebras / Cohere / Google / Groq / Mistral / OpenRouter / SambaNova / Sarvam / HuggingFace / Slack keys). |
| `C:\Dev\hfo_gen_130_forge\state\sigrun_secrets\` | same story per inventory. |
| Grep across gen-133 for `INSTANTLY\|instantly` | 30 matches — all doctrine/reference text; zero secret values. |

## What the operator must do — in the Instantly UI, before Tuesday 08:00 CT

Preconditions to fire `ENV_COLD_EMAIL_001` at 25/day:

1. **Log in to Instantly** (app.instantly.ai).
2. **Confirm workspace ownership of `tryagentreleasegate.com`** — under *Email Accounts*, verify the domain is listed as active and DKIM/SPF/DMARC show green.
3. **Verify warmup status** — under *Email Accounts → [mailbox] → Warmup* — confirm:
   - Warmup enabled and running ≥ 30 days
   - Daily warmup send count ≥ 20
   - Reputation score ≥ 70 (Instantly's own metric)
   - If ANY of these fails, **do not send 25/day** — start at 5–10/day and ramp weekly.
4. **Count sending mailboxes on `tryagentreleasegate.com`** — for 25 sends/day, you want ≥ 2 mailboxes at 12–13/day each (industry rule of thumb: max 30 cold sends per mailbox per day). If only 1 mailbox exists, cap the envelope at 15/day and add a second mailbox this week.
5. **Set daily-limit config on each mailbox** — *Settings → Sending Limit* — cap at 25/day per mailbox max (Instantly hard-recommends this; going higher trips their safety net).
6. **Generate API key** — *Settings → Integrations → API* → *Generate New Key*. Copy it.
7. **Paste key into `C:\Dev\hfo_gen_133_forge\.env`** at a new line:
   ```
   INSTANTLY_API_KEY=<paste-here>
   INSTANTLY_CAMPAIGN_ID=<paste-here>  # created below
   ```
8. **Create campaign** in Instantly UI: *Campaigns → New* → name `hfo_cold_email_ai_rescue_001` → attach mailboxes on `tryagentreleasegate.com` → configure schedule (weekdays only, 09:00–16:00 recipient local time, ≥ 90 sec spacing between sends). Copy the campaign ID into env above.
9. **Upload suppression list** (initially empty) — *Campaign → Leads → Suppression*. The reply-triage worker will append to this via API as unsubscribes come in.
10. **Physical postal address** — CAN-SPAM requires this in every message. Confirm the address you will use (personal / studio / mailbox-service address) and paste into `.env` as `POSTAL_ADDRESS=`.
11. **Booking link** — decide the calendar link (Cal.com / SavvyCal / Google Calendar Appointment Schedules). Paste into `.env` as `BOOKING_LINK=`. This is §G item 1 from the envelope doc — also flagged as a hard blocker there.

## Env vars the pipeline will read (fill all four)

```env
INSTANTLY_API_KEY=            # step 6 above
INSTANTLY_CAMPAIGN_ID=        # step 8 above
BOOKING_LINK=                 # step 11 above (must return HTTP 200)
POSTAL_ADDRESS=               # step 10 above (single-line, e.g. "123 Main St, Austin, TX 78701, USA")
SENDER_NAME=                  # e.g. "Tao" — first name only signs the message
```

## If the domain is NOT warm

Per envelope §I: reply-rate <2% after 50 sends → HALT. A cold or under-warmed domain will produce that HALT within 2 days and burn the domain in the process. **Do not ship 25/day until step 3 shows all-green.** Preferred safe ramp: 5/day for week 1, 10/day for week 2, 25/day thereafter.

## Independent verification (once API key is set)

The pipeline (`tools/outreach/cold_email_send.py --probe`) will call:

- `GET /api/v2/accounts` → confirm mailbox count + status
- `GET /api/v2/campaigns/{id}` → confirm daily limit config
- `GET /api/v2/campaigns/{id}/analytics` → confirm no pre-existing bounces/complaints
- `GET /api/v2/blocklist` → confirm suppression list is loaded

Output goes to `state/outreach/INSTANTLY_PROBE_RESULT_20260804.md` when operator runs it Tuesday.

## Honest flaws

1. I did not directly `Read` gen-131's `.env` — I trusted the key-name inventory in `grimoire_secrets_locations_20260801.jsonl` (row 20) + `inbox/olrun/20260801T180312Z_sigrun_secrets_inventory.md`. If either misreports the key list, the "no Instantly key" conclusion is wrong. Operator can `grep -i instantly C:\Dev\hfo_gen_131_forge\state\sigrun_secrets\.env` in 5 sec to double-check.
2. I did not attempt an unauthenticated request against `app.instantly.ai/api/v2` to confirm the API surface exists at that path in August 2026 — the endpoint set above is from Instantly's public docs as of early 2026 and may have changed.
3. The "≥ 30 days warmup, reputation ≥ 70, 30 cold sends per mailbox" thresholds are industry conventions, not values I verified against Instantly's current in-app guidance.
