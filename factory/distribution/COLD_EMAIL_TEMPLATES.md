---
schema_id: hfo.gen133.distribution_cold_email.v0_1
doc_kind: COLD_EMAIL_TEMPLATE
subject: 3 cold-email templates — AI startup CTOs and OSS AI maintainers
claim_status: STAGED_UNAPPROVED
created_utc: 2026-08-02T00:00:00Z
sealed: false
---

# Cold-email templates

**Rules:**
- Target one persona per unit, listed below. Aim for 20-40 recipients per
  unit for the launch — cold email works on volume, but only if it stays
  personal at each recipient.
- Personalize the first line (recent tweet, recent release, blog post).
- One clear CTA per email. Not "would love to chat" — a specific action.
- Never attach anything. Never say "just checking in."
- Follow-up 1 sent +4 days if no reply. Follow-up 2 sent +7 days from FU1. Done.

---

## Template 1 — prompt-versioning-lite

**Persona:** heads of AI / staff engineers at series-A AI-tooling companies
(Elicit, Cursor, Perplexity, Codeium, You.com, Warp, Replit, etc.),
open-source LLM-app framework maintainers (LangChain, LlamaIndex, DSPy).

**Subject:** Prompt versioning without Langfuse overhead — 60 seconds

**Body:**

Hi {first_name},

I saw {specific_recent_thing_they_shipped} last week — nice work on {detail}.

Quick question, then out of your inbox: how do you version prompts today?

I built the smallest possible answer for my own team's pain — paste a prompt,
get a content-addressed URL, edit → new revision, word-level diff between any
two versions, one-click rerun on any model. No accounts on the free tier.
Live demo (works without login): https://prompt-versioning-lite.agentreleasegate.com/

The wedge is "URL you paste into Slack" — Langfuse and Braintrust cover the
eval + observability tier, this is the 10×-more-common "wait, what did I
change?" tier below it.

If you or your team ever tweaks a prompt, would love 5 minutes to hear how
you handle it today, and whether this shape is useful. Cal link if easier:
{cal_link}

— Tao

**Follow-up 1 (+4 days if no reply):**
> Hi {first_name} — small nudge. Are you the right person for this or should
> I ask someone on your team? Happy to be pointed elsewhere.

**Follow-up 2 (+7 days from FU1):**
> Understood — closing the loop. If prompt-versioning ever becomes acute
> feel free to reply to this thread. Best of luck with {recent_thing}.

---

## Template 2 — agent-status

**Persona:** solo devs / small teams shipping AI agents on production traffic
— MCP server maintainers, indie AI SaaS founders (indiehackers.com filter),
Modal / Cloudflare Workers / Vercel AI SDK power users.

**Subject:** Status page for {their_agent_name} — thoughts?

**Body:**

Hi {first_name},

Been using {their_agent_or_tool} for {specific_thing}. When it hiccupped last
{week/month}, I couldn't tell if it was you, my key, or upstream — which is
the whole problem I'm trying to solve.

I built Agent Status — one URL per agent, one heartbeat POST from your
handler, and users get a real-time status page instead of a Discord DM
storm. Uptime, last-run, error rate, p95, incident log. Auto-incident on 3
consecutive misses. Free for 1 agent, $19/mo/agent for RSS / email /
webhook alerts.

Live demo (synthetic agent so you can see the shape):
https://agent-status.agentreleasegate.com/app.html

Two asks:
1. Would you use this for {their_agent_name}? Why / why not?
2. What's your current answer to "is it down?" from users?

Reply here or grab 15 min: {cal_link}

— Tao

---

## Template 3 — agent-changelog

**Persona:** OSS AI agent / framework maintainers (LangChain, LlamaIndex,
CrewAI, AutoGen, DSPy, Continue.dev, Aider, Cursor), founders of vertical
AI agents whose behavior changes weekly.

**Subject:** How do you tell {agent_name} users what changed this week?

**Body:**

Hi {first_name},

You ship {agent_name} updates weekly (I follow the {repo_url} commits). How
do users find out what changed — GitHub releases, changelog markdown,
Twitter thread, something else?

I built Agent Changelog because none of those quite fit for me. It's the
LLM-agent equivalent of keepachangelog.com — hosted markdown-first
changelog, semver-aware, RSS + one-line embed widget, and email subscribers
on major-version bumps. So your users get "hey, we deprecated tool X"
without you managing a mailing list.

Free for 1 agent, $12/mo/agent for RSS + embed + email + custom domain.
Live demo: https://agent-changelog.agentreleasegate.com/app.html

Would you want this for {agent_name}? What am I missing about how you
communicate changes today?

Cal link if easier: {cal_link}

— Tao

---

## Where to find recipients

- **CTOs / staff engineers at AI startups:** filter LinkedIn for "AI"
  + "series A/B" + "engineering leader"; verify emails with Hunter.io.
- **OSS AI maintainers:** GitHub Insights → contributors on the top 200
  AI-agent / MCP repos. Use their commit email or `git log --format=%ae`.
- **Indie AI SaaS founders:** indiehackers.com/products?filter=ai + Twitter
  bio-search for "founder" + "AI".

## Volume + reply-rate targets

- 30 sends per unit
- ~15% reply rate on well-personalized cold (skew high because the pitch is
  targeted). If you're seeing < 5%, your first line isn't personal enough.
- 30% of replies → Cal booking. Target: 3-5 bookings per unit in launch week.
