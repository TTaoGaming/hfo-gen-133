---
schema_id: hfo.gen133.distribution_reddit.v0_1
doc_kind: REDDIT_DRAFT
subject: 3 Reddit posts — AppAlchemy pattern (pain → build → single tool mention at end)
claim_status: STAGED_UNAPPROVED
created_utc: 2026-08-02T00:00:00Z
sealed: false
---

# Reddit drafts — one per unit

**AppAlchemy pattern:** open with a real pain, describe the janky path you
walked before building, list the two-line thing you built, mention the tool
by name **once**, at the end. 150-400 words. No links in the body — link in a
top-level comment or in the sidebar-approved way for the sub.

**Sub-specific rules** (verify before posting; subreddit rules drift):
- **r/mcp** — allows self-promo with substantive context.
- **r/AIAgents** — allows tool posts if they're framed as build lessons.
- **r/LocalLLaMA** — self-promo tolerated when the tool works with local models.
- **r/SideProject** — explicitly for launch posts.

---

## Draft 1 — prompt-versioning-lite

**Title:** I versioned my prompts in Google Docs for a year. Then I built the
                  worst thing that could possibly replace it.
**Subs:** r/SideProject (primary), r/AIAgents, r/LocalLLaMA
**Body:**

For the last year, my "prompt version control" was a Google Doc titled
`prompts_FINAL_final_v3.doc`. Every time I tweaked the system prompt for one
of my agents and the output got worse, I'd spend 20 minutes hunting through
Docs revision history trying to figure out what changed.

I tried Langfuse. Great tool, but the overhead-to-value ratio for someone
running two prompts is bad — you spend an hour on setup to log something you
edit once a week. I tried Notion; same problem plus the sync latency.

So I built the smallest thing that solves the actual pain:

- Paste a prompt.
- Get a URL. That URL is the current version.
- Edit the prompt, hit save, you get a new revision hash. Every revision has
  its own URL.
- Click "diff vs" between any two revisions and see a word-level diff.
- One-click rerun against gpt-4o-mini / claude-haiku-4-5 / gemini-2.0-flash /
  llama-3.3-70b (BYOK, we don't store keys).

That's it. No accounts on the free tier. 10 prompts, 7-day history.

I share the URL in Slack. When someone says "the agent got dumber this week,"
we open the diff. It's not sophisticated. It just works.

It's called Prompt Versioning Lite. Free tier at
prompt-versioning-lite.agentreleasegate.com. Would love to know what breaks it.

---

## Draft 2 — agent-status

**Title:** My AI agent went down for 6 hours and nobody told me. So I built a
                  status page for it (and then for everyone else's).
**Subs:** r/AIAgents (primary), r/mcp, r/SideProject
**Body:**

Last month, my customer-support agent (Modal cron, runs every 3 min) started
returning 500s from an upstream model at ~2am. Nobody paged me because it's a
side project. Users just… stopped getting responses. I found out from a
support DM at 8am the next day.

Statuspage.io wants $79/mo and is built for AWS-region-scale multi-component
outages. I have one agent. I want one page. One URL.

So I built it:

- Your agent POSTs `/api/heartbeat?token=xxx` at the end of every run (any
  language, any host, one HTTP call).
- We compute uptime, last-run, error rate, and p95 latency from that.
- Users get a public URL: `agent-status.agentreleasegate.com/status/<slug>`.
- Green dot / yellow dot / red dot at a glance. 60-heartbeat bar underneath.
- Auto-incident on 3 consecutive misses. Slack webhook alerts on Pro.

The demo is live now — the page shows a synthetic agent so you can see the
UI before you wire yours up.

Free for 1 agent. Pro is $19/mo per agent (RSS + email subscribers + webhook
alerts). Would love feedback on the heartbeat schema before I freeze it.

---

## Draft 3 — agent-changelog

**Title:** "What changed in your agent this week?" was the most common user
                  question. So I built a Keep-a-Changelog for AI agents.
**Subs:** r/AIAgents (primary), r/mcp, r/LocalLLaMA
**Body:**

Every week I bump the model, rewrite the system prompt, add or deprecate a
tool. My power users notice. My regular users get confused when behavior
shifts under them. GitHub Releases is for code — users don't have GitHub
accounts. A Notion page rots.

I wanted the LLM-agent equivalent of `keepachangelog.com` — a hosted,
markdown-first, semver-aware changelog with RSS and an embed widget.

So I built it:

- Write releases in Markdown, using standard Keep-a-Changelog sections
  (Added / Changed / Deprecated / Removed / Fixed / Security).
- Public URL: `agent-changelog.agentreleasegate.com/changelog/<agent-slug>`.
- RSS feed at `/changelog/<slug>/rss.xml`.
- One-line `<script>` tag embeds a "What's new?" popover in your agent's UI.
- Bump the major version (BREAKING) and Pro-tier subscribers get an email —
  no email plumbing on your side.

Free for 1 agent, $12/mo per agent for RSS + embed + email subscribers +
custom domain.

Would love to know: how do you tell your agent's users something changed
today?

---

## Post-comment kit (use in the top comment, after the mods approve)

- **Link:** `https://<slug>.agentreleasegate.com/`
- **GitHub:** `https://github.com/TTaoGaming/<slug>`
- **Feedback form:** the Cal.com link in the footer — 15 min, real conversation.
- **What I want feedback on:** [pick one specific decision — e.g. "the free
  tier cap" or "the heartbeat POST schema" or "the semver-BREAKING behavior"]
