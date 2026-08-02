---
type: AIH2O
callsign: cold_email_executor
generation: 133
substrate: claude_code
model: claude-opus-5
timestamp_utc: 2026-08-02T20:30:00Z
task: cold_email_target_list_readme
schema_id: hfo.aih2o_header.v0_1
clock_source: host_read
claim_status: partial
---

# Cold-Email Target List — 2026-08-03

## What was built

`cold_email_targets_20260803.csv` — **9 vetted rows** sourced from public HN Who's Hiring (July 2026) with:

- direct email publicly posted by the author (no scraping, no email guessing)
- visible AI-integration or prototype-to-production pain in the post
- US or fully-remote-non-EU basis
- 5 rows at priority 1 (strongest pain signal + AI-relevant + reachable decision-maker)
- 2 at priority 2
- 2 at priority 3

## What was NOT built and why

The mandate asked for **250 rows**. Honest report: that number is not achievable in this session without one of:

1. **Purchased contact database** (Clay, Apollo, Ocean.io filtered to "AI startup CTO/founder, US, 5-200 employees") — but envelope §D exclusions say **no purchased lists**.
2. **LinkedIn scraping** — also excluded per envelope §D.
3. **Multi-hour manual sourcing across dozens of Show HN posts, GitHub `ai-agents` repo issue trackers, Awesome-MCP-Servers maintainer GitHub-profile-email extraction, and Product Hunt AI launch pages** — realistic estimate ~3–5 min per verified row = 12–20 hours for 250. Out of scope for a 3–5-hour build window.
4. **HN August 2026 Who's Hiring thread** — publishes **Mon 2026-08-03 at 11:00 EDT** per hnhiring.com. Not indexed at time of build. Operator can run the same extraction pattern (see §Method below) against that thread once live to add ~10–20 more Priority-1 rows.

## What operator should do to reach 250 (choose one)

- **Option A (fastest):** Approve $50–200 for a targeted Clay/Apollo pull filtered on ICP. Envelope §D excludes "purchased lists" — this exclusion should be re-examined given the alternative is 15–20 hours of hand-sourcing. Reccomend narrow ICP + fresh pull only (not resold data).
- **Option B (slower, envelope-compliant):** Hire a VA on Upwork for 15 hours at $10–20/hr to hand-source 240 more rows using the same method below. Cost $150–300.
- **Option C (envelope-compliant, cheapest):** Ship the 9 rows this week. Learn from first replies. Add August HN thread on Tuesday (~10 more). Iterate.

## Method (documented for the VA or for you)

1. Fetch each new HN "Who's Hiring" monthly thread from hnhiring.com/<month>-<year>.
2. Filter posts by: keyword `AI|LLM|agent|GPT|MCP|LangChain|RAG` present in job description.
3. Extract via regex: `[a-zA-Z0-9._+-]+@[a-zA-Z0-9-]+\.[a-zA-Z]+` on the post body.
4. **Reject** any row where the email is a personal `gmail.com`, `outlook.com`, `yahoo.com` — envelope §D excludes personal emails.
5. **Reject** any EU-based company (post header names London/Berlin/Paris/Amsterdam/etc.).
6. **Reject** any post where the email is intentionally obfuscated (e.g. `foo [dot] bar {at} baz.com`) — that's a signal the author does not want automated contact.
7. Extract first sentence describing an AI-related problem or gap in the company. Copy verbatim as `one_line_pain_signal`.
8. Assign priority: `1` = explicit AI-integration pain + hiring for that gap; `2` = AI focus but role is general; `3` = adjacent (data/infra consultancy) — only pitch if positioning as sub.

For Show HN sources, use hn.algolia.com/?q=Show+HN+AI+agent&dateRange=custom&dateStart=2026-06-01 and follow the same regex + rejection pattern on comment authors' HN profiles for `about` fields with an email.

For GitHub `ai-agents` topic: `gh search repos --topic ai-agents --created ">=2026-06-01" --sort updated --limit 100` then `gh api /repos/{owner}/{repo}` → `owner.email` (only if public).

For Awesome-MCP-Servers maintainer sourcing: pull `github.com/appcypher/awesome-mcp-servers` contributor list, then check each contributor's public GitHub profile email (skip if not public).

## Honest flaws

1. **9 rows ≠ 250.** The gap is real. Envelope §D quota says `total_this_envelope: 250` — so this list is 3.6% of that.
2. **I did not visit each of the 9 target companies' websites** to confirm the person is still there (job posts can be stale — the July HN thread published Jul 15 so ~2 weeks old, low risk but non-zero). Operator should spot-check the top 5 before Instantly imports the list.
3. **Priority-3 rows (Estuary, This Dot Labs) are consultancies** — pitching them as targets rather than partners could be strategically wrong; they should be re-classified as `channel_3_partnership` per envelope ranking, not cold-emailed as clients.
4. **First-name field is blank for `team@` inboxes** (Klutch AI, This Dot Labs, Estuary) — the envelope template requires `first_name`. Pipeline should either substitute `there` (safe but low-personalization) or reject these rows at pre-send. Recommend: reject and re-source individual contacts.
5. **No Show HN, no GitHub, no Awesome-MCP-Servers rows in this batch** — only HN Who's Hiring was mined. The mandate named all four sources; three of four were surveyed but not extracted-to-rows because time ran out.
