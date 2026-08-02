🚨 *GEN-133 ANDON — active blockers 2026-08-03*

Every blocker below is a HALT condition or ship-gate that will trip on Tuesday if not addressed. Operator-owned unless otherwise noted.

⛔ *BOOKER-01 — booking URL still unbound on all landing pages.* Four canons flagged (V8/V9/V10/V11). Every CTA on `hfo-games.pages.dev` and micro-SaaS units is `href="#book"`. V11 §3 bright-line 1: no unit ships and no cold-email envelope fires until `curl -sSf $BOOKING_URL` returns 200. Owner: operator. Fix ETA: 20 min (Cal.com free tier signup).

⛔ *INSTANTLY-01 — no Instantly API key found in any known credential store.* Checked gen-133 `.env`, `sigrun-secrets/` (missing), and gen-131 `sigrun-secrets/.env` key inventory. Every downstream verification (domain warm state, mailbox count, warmup completion, suppression list) requires this key. Cannot probe live. Owner: operator. Fix ETA: 30 min (log in Instantly UI, verify tryagentreleasegate.com warmup ≥30d + rep ≥70, generate API key, paste into `.env`). Full runbook: `state/outreach/INSTANTLY_STATE_20260803.md` steps 1–11.

⛔ *INSTANTLY-02 — HALT preregistered.* Cold-email envelope §I: reply rate <2% after 50 sends → HALT and burn domain analysis. Un-warmed or under-warmed domain will trip within 2 days at 25/day. Preferred safe ramp: 5/day W1, 10/day W2, 25/day thereafter. Owner: operator to enforce.

⛔ *SANDBOX-01 — executor sandbox VM will not boot this session.* "Workspace unavailable. The isolated Linux environment failed to start (VM service not running)." Blocks: cold-email dry-run execution, live Instantly probes, factory deploy commands. Fallback: operator runs the 3 pwsh commands in `state/outreach/DRY_RUN_VERIFICATION_20260803.md` from a normal shell Tuesday morning before pasting the class-preauth line.

⛔ *CLOUDFLARE-METRIC-01 — GraphQL API endpoint missing.* Codex D2 poller records `unknown_metric_not_exposed` for the Cloudflare Pages visitor metric being queried. Cause: metric name or GraphQL query path is wrong. Impact: cannot measure organic impressions on the 53 live Cloudflare Pages projects, which is one of the two conditions to lift the 1-unit/week cap (per V11 §3 bright-line 3). Owner: Codex, but needs prompt correction from Olrún. Fix ETA: unknown until endpoint is corrected.

⛔ *REDDIT-KARMA-01 — unknown karma on all target subs.* r/vibecoding, r/LocalLLaMA, r/mcp, r/AIAgents, r/SideProject all have minimum-karma or account-age posting gates. Zero probe run against the operator's Reddit account this session. Cannot pre-verify posting eligibility. Owner: operator can `Reddit → user profile → karma` in 2 min per account.

⛔ *CLASS-PREAUTH-01 — documented, not executed.* V9 §A claimed `class:` gate format is implemented (`class:<name>:quota=<N>:seq_range=<a-b>:expires=<UTC>`). V11 §3 bright-line 2 (adopted from Jörmungandr §A row 3): counts as working ONLY after a roundtrip probe writes one line, runs one loop, receives one echo. Zero probe run this session. Owner: swarm on Tuesday, gated on INSTANTLY-01 landing.

⛔ *CODEX-D3-01 — daily drafter bootstrap-fixed but empty.* 0 fitness rows, no publications, empty curated_memory. Blocks: LinkedIn/X/Substack daily content pipeline (option 4 in TOP-10). Owner: Codex, needs re-fire after INSTANTLY-01 lands.

⛔ *SLACK-BROADCASTER-01 — this broadcaster itself.* No webhook or bot token available on substrate. All five staged messages sitting in `state/olrun/slack_outbox_20260803/`. Full recovery runbook: `state/olrun/SLACK_CREDENTIAL_BLOCKER_20260803.md`. Owner: operator (2 min Slack webhook creation OR install Slack MCP via `/mcp` in interactive Claude Code).

⚠️ *SUIKA-LICENSE-01 (legal exposure, not HALT).* moonfloof/suika-game returns `NOASSERTION` on GitHub API license classification. We have already forked it 12× (`hfo-suika-dlc-{5..16}-*.pages.dev`). Owner: operator must read the LICENSE file by hand or take those variants down.

*Not currently a HALT but on the wall for visibility:* `agentreleasegate-oss` public 27+ days with 0 stars/forks/subscribers — either relaunch with studio-aligned positioning or delete and restart clean.
