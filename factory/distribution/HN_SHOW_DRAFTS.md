---
schema_id: hfo.gen133.distribution_hn.v0_1
doc_kind: HN_SHOW_DRAFT
subject: 3 Show-HN submissions — one per unit
claim_status: STAGED_UNAPPROVED
created_utc: 2026-08-02T00:00:00Z
sealed: false
---

# Show HN drafts

**Rules of engagement:**
- Title format: `Show HN: <thing> – <one-line pitch>`. Under 80 chars.
- URL is the direct product URL. No blog post redirects.
- Body is a top comment, posted by the same account. 3-5 short paragraphs.
- Best-window: Tue-Thu, 8-11am PT.
- Stay in the comment thread for the first 4 hours. Answer every technical
  question fast. Never argue with tone-of-comment complaints.

---

## Draft 1 — prompt-versioning-lite

**Title:** Show HN: Prompt Versioning Lite – git for prompts, without the git
**URL:** https://prompt-versioning-lite.agentreleasegate.com/
**First comment:**

I've been building AI agents for a year and my "prompt version control" has
been a Google Doc named `prompts_FINAL_final.doc`. This is the smallest thing
that solves the actual pain.

Paste a prompt, get a URL. That URL is the current revision (content-addressed
by SHA-256, so nobody can rewrite history). Edit and save → new revision, new
URL. Click "diff" between any two revisions to get a word-level diff. Hit
"run" to send the current prompt to gpt-4o-mini / claude-haiku-4-5 /
gemini-2.0-flash / llama-3.3-70b (BYOK, we proxy but don't store the key).

Not built to replace Langfuse or Braintrust — those are eval + observability
platforms. This is for the 10× more common case of "wait, what did I change?"

Free for 10 prompts. $9/mo unlimited. The MVP persists to localStorage; the
D1 backend for sync/immutability is next week's milestone if the launch pulls
signups. Source is public, PRs welcome.

---

## Draft 2 — agent-status

**Title:** Show HN: Agent Status – status pages for AI agents, $19/mo, not $79
**URL:** https://agent-status.agentreleasegate.com/
**First comment:**

Statuspage.io is $79/mo and models the world as regions and components. My
customer-support agent is one Modal cron running every 3 minutes. I want one
page for it. That was the whole insight.

Your agent POSTs `/api/heartbeat?token=<yours>` at the end of every run.
Optional body: `{ "ok": true, "latency_ms": 90, "note": "..." }`. From that we
compute uptime, error rate, p95 latency, and a 60-heartbeat bar. Public URL,
shareable, indexable. Auto-incident on 3 consecutive misses. Slack / Discord
webhook alerts on Pro.

Free for 1 agent. $19/mo per agent for RSS + email subscribers + webhook
alerts. Not trying to compete with Statuspage / BetterStack / Instatus —
different price, different UX, different problem.

The demo page renders a synthetic agent so you can see the UI before you wire
yours up. Feedback on the heartbeat schema especially welcome — I want to
freeze it this week.

---

## Draft 3 — agent-changelog

**Title:** Show HN: Agent Changelog – Keep-a-Changelog for AI agents, with RSS
**URL:** https://agent-changelog.agentreleasegate.com/
**First comment:**

Every week I bump a model, rewrite a system prompt, deprecate a tool. My
users notice. GitHub Releases is for code (users don't have GitHub accounts).
A Notion page rots and doesn't offer RSS.

This is the LLM-agent equivalent of keepachangelog.com. Markdown-first,
semver-aware, RSS + JSON feeds, one-line `<script>` tag embed widget
(Shadow-DOM'd, zero CSS collisions).

Write releases in Markdown using standard Keep-a-Changelog sections. Bump the
major version and Pro-tier subscribers get an email — email plumbing is on
our side, not yours.

Free for 1 agent. $12/mo per agent for RSS + embed + email + custom domain.

I originally wanted to build an MCP-server registry, but the space is already
solved by the official modelcontextprotocol/registry, Docker's official
registry, and TensorBlock indexing 7,747 servers. Pivoted to this instead —
the unclaimed adjacency. Would love to know what changelog patterns you've
built ad-hoc for your own agents.

---

## Anti-pattern list (things to NOT do in the top comment)

- Don't paste the pricing table.
- Don't link to the roadmap or the "what's next."
- Don't use marketing verbs ("unleash", "revolutionize").
- Don't apologize for the MVP being an MVP — say what's next in one line, move on.
- Don't @ users. Don't @ yourself.
