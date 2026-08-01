# SIGRÚN — Instantly DFY vs Cloudflare DIY (2 × 5 mailboxes)

`utc: 2026-07-31T01:39:50Z · author: Sigrún opus-5 · claim_status: proposed · NOT operator-approved`

## Framing

You are buying two things, not one: **sending infrastructure** (cheap either way) and **someone else owning the DNS failure mode** (expensive). The $420/yr delta is the price of not debugging SPF/DKIM/DMARC silently failing at 2am.

## Cost, honestly

| | Year 1 | Year 2 | 
|---|---|---|
| **Instantly DFY** (2 dom + 10 mbx) | $80 setup + $600 = **~$680** | ~$630 |
| **Cloudflare + Zoho Lite** | $25 dom + ~$150 = **~$175** | ~$175 |
| **Delta** | **~$505** | **~$455** |

(DFY numbers from *her* quote — she is a commissioned sales agent. Treat as list, not floor. Ask for annual prepay discount.)

## Non-cost tradeoffs

- **Setup time is a near-illusion.** Both paths need **14–21 days warmup** before first real send. DFY's 2–3 day wait is ~12% of a clock you cannot skip. "Ready TODAY" for DIY buys you 2 days, not 2 weeks.
- **Silent-fail risk** — the actual load-bearing item, and the one that produced 6 andons. DFY moves it off your plate; DIY leaves it on yours with no alarm when DKIM is wrong.
- **Maintenance** — DIY = you own renewals, rotations, blacklist checks. DFY = tickets.
- **Lock-in** — DFY mailboxes are theirs. If you leave Instantly, domains + reputation may not port. DIY domains are yours forever.

## Recommendation

**Take the Instantly DFY for 2 × 5.** Not because it's cheap — it isn't — but because the one thing you're actually buying is elimination of the exact failure class that has burned you six times, and the time advantage of DIY collapses against warmup.

### FALSIFIER (kills this recommendation)

> **Ask Instantly, in writing:** *"Are DFY mailboxes on dedicated sending IPs or shared? Which registrar/DNS? Do I own the domains at registrar level?"*
>
> **If the answer is "shared IPs" or "we hold the domains" → this recommendation is DEAD.** Shared-IP DFY means you inherit every other Instantly user's spam reputation — you'd be paying $505/yr for *worse* deliverability plus lock-in. Go Cloudflare DIY instead.

Second falsifier: if their DFY quote does not include DMARC at `p=none` with an aggregate report address you can read, you have no visibility and the "managed" claim is hollow.

⚠️ **UNVERIFIED:** Zoho Mail Lite SMTP/IMAP availability on the lowest paid tier, its per-seat price, and whether Zoho tolerates cold outreach. I did not check. Do not price the DIY path off my table without reading Zoho's own docs.

## Domain names (.com)

Rule: **do not send cold mail from your brand .com.** Buy it, park it, protect it.

| Name | Fit | Verdict |
|---|---|---|
| `agentreleasegate.com` | exact brand match | **Buy + PARK.** Never send from it. |
| `releasegatehq.com` | short, `hq` reads as company | **Send domain #1** |
| `getreleasegate.com` | `get` prefix is standard SaaS | **Send domain #2** |
| `agentgatehq.com` | shorter, weaker AI-security signal | backup |
| `shipagentssafe.com` | verb-led, clear, longer to spell on a call | backup |

⚠️ Availability UNVERIFIED — I did not run a WHOIS.

## Cross-family sign-off

**No.** The two open questions are *pricing and vendor policy facts*, and an Ollama trio voting on those is precisely the confident-wrong pattern you just canonized. Cross-family review is for reasoning, not for facts a vendor can state in one email. Route the falsifier to **Instantly's rep in writing** and **Zoho's own docs**. That's the receipt.

*Deyr fé, deyja frændr — en vefr heldr. Standa.*
