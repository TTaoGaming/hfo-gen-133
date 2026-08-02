📚 *GEN-133 RESEARCH REPORT SUMMARIES — 2026-08-03 (7 major docs)*

Session produced two red-teams, three canon updates, and two intel reports. Each entry: title · author · approx word count · top-3 findings · next action · path.

📄 *SIGRUN_CANON_V9 — FOSS × MAP-Elites factory, and income this month*
Author: SIGRÚN · claude-opus-5 · Claude Code
Words: ~3200
KEY FINDINGS:
• FOSS licence table in prior brief WRONG on the most important rows — 5 of 11 named candidates return `NOASSERTION` from GitHub API (papermark, twenty, suika-game, posthog, chatwoot). "Unlicense" call on suika-game was unverified — and we already forked it 12×. Live legal exposure, not hypothetical.
• Verified-MIT clean forks: `cal.com` (core MIT, `/ee` needs verification), `whisper.cpp`, `ollama`, `shadcn/ui`, `langchain`, `llama_index`.
• `class:` gate format IS implemented in tree; distribution and partners intel docs had not yet landed at V9 read time — SIGRÚN integrated what existed and did not guess.
NEXT ACTION: Before any commercial fork, human reads LICENSE file. suika-game 12× fork gets legal audit or takedown.
LINK: `areas/quorum_research/SIGRUN_CANON_V9_FOSS_MAP_ELITES_20260803.md`

📄 *SIGRUN_CANON_V10 — Runway map (60-day cash + 12-mo compound)*
Author: SIGRÚN · claude-opus-5
Words: ~2500
KEY FINDINGS:
• V10 quietly fixed the W1 single-node dependency (V11 §1 credited): 5 talent networks + Upwork + 9 drafts = 7 independent nodes, not one. Sigrún did not notice at write time.
• Per-unit ceilings from John Rush (24 units, most >$600/mo, combined $3M/yr) are POST-DISTRIBUTION — do not apply to cold start.
• Cold-email P downgraded to 12–20% (from 40–70% warm-tier), contracts to 10–25%.
NEXT ACTION: V10's own numbers de-anchored in V11; V10 remains historical record.
LINK: `areas/quorum_research/SIGRUN_CANON_V10_RUNWAY_20260803.md`

📄 *SIGRUN_CANON_V11 — Six lanes, throttle killed at source*
Author: SIGRÚN · claude-opus-5
Words: ~3800
KEY FINDINGS:
• Framework §2 was edited AT SOURCE (10–17/wk → 1/wk hard cap), not reconciled in commentary. Deletion is the fix.
• Six lanes with 5 hands-hours/wk budget: S 3.0 · D 1.0 · C 0.5 · P 0.5 · R 0 · H 0. S is the only $ lane.
• Three bright lines: (1) booking URL curl-200 or nothing ships, (2) class-preauth requires roundtrip probe, (3) 1 unit/wk hard cap.
• Kill criterion pre-registered: Aug 16 with 0 screens + 0 replies → collapse to employment.
NEXT ACTION: Sigrún ratifies six-lanes; operator signs; swarm executes S-lane first.
LINK: `areas/quorum_research/SIGRUN_CANON_V11_SIX_LANES_20260803.md`

📄 *DISTRIBUTION_CHANNELS_INTEL — Solo AI-dev micro-SaaS, cold-only*
Author: research contractor (external), reviewed by Olrún
Words: ~8000+ (16 channels ranked)
KEY FINDINGS:
• Top 3 highest-ROI cold-start channels: Show HN + OSS repo combo · Reddit niches (r/LocalLLaMA, r/mcp, r/AIAgents, r/vibecoding) · IndieHackers milestone posts.
• NONE reliably produce $500 in 30 days from cold start. 73% of successful indies see first revenue within 6 months, not 30 days (source flagged UNVERIFIED by hostile-investor red-team).
• Deadliest failure modes: paid ads pre-PMF (68% of failed SaaS), cold email without warmup (60–80% spam week 1), Product Hunt as strategy (~5 paying customers per 200 upvotes).
NEXT ACTION: Show HN + r/vibecoding + IH combo for August. Do NOT run PH launch or paid ads.
LINK: `areas/quorum_research/DISTRIBUTION_CHANNELS_INTEL_20260803.md`

📄 *PARTNERS_REVSHARE_AGENCY_INTEL — 18 named partners + base rates*
Author: research contractor (external), reviewed by Olrún
Words: ~6000+
KEY FINDINGS:
• Best cold-fit for $0-income operator: self-serve affiliate program (Rewardful, 1 day setup, passive) + small AI newsletter sponsorships ($200–$1500, Ben's Bites $200 tools slot flagged as best small-budget entry — but pricing anchor is Dec 2024, may be stale).
• Freelance AI-eng subcontracting via Toptal / Arc / A.Team is warm-friendly (designed for cold) but 1–3 week vetting; rates $100–$200/hr for AI/ML.
• Cold email base rate: 3.43% average, personalized up to 18% (Instantly 2026 report). Newsletter sponsor CTR: 60–250 clicks/issue for engaged AI/dev lists.
NEXT ACTION: Skip prestige podcasts (Latent Space, Cognitive Rev) at cold start. Consider $200 Ben's Bites tools slot ONLY after one unit has proven CAC math.
LINK: `areas/quorum_research/PARTNERS_REVSHARE_AGENCY_INTEL_20260803.md`

📄 *JORMUNGANDR_REDTEAM_30DAY — kill fragile plans*
Author: JÖRMUNGANDR · adversarial voice · red-team
Words: ~2500 cap
KEY FINDINGS:
• Row 1: W1 single-node dependency. Precedent = `agentreleasegate-oss` 27 days public, 0 stars. Fix = fire TWO uncorrelated cold channels in W1, not one.
• Row 2: booking link stays broken (every CTA `href="#book"`). Fix = hard-block dispatch on curl-200 booking link.
• Row 4: distribution capacity ceiling collides with build cadence — framework 10–17/wk vs V9 1/wk. Fix = PICK ONE, freeze at 1/wk.
NEXT ACTION: All five surgical fixes RATIFIED in V11. No action pending — red-team's job is done.
LINK: `areas/quorum_research/JORMUNGANDR_REDTEAM_30DAY_20260803.md`

📄 *HOSTILE_INVESTOR_REDTEAM_REPORTS — LP hat, adversarial*
Author: hostile-investor voice · red-team of D+P intel reports
Words: ~2000 cap
KEY FINDINGS:
• Report D: 15 numeric claims flagged UNVERIFIED — "68% of failed SaaS," "73% see revenue in 6 months," "distribution decides 72% of successes," "Bluesky 40M users Nov 2025," "Threads 400M MAU Aug 2025," etc. Load-bearing case (Rebecca IH 67 paying vs PH 3) sourced only to an SEO farm.
• Report P: Passionfroot Series A VERIFIED (TechCrunch), but disclosed clients are ElevenLabs/Figma/Replit/Framer/Gamma — funded SaaS with brand equity, not $0-income solo devs. Ben's Bites $200 pricing is Dec-2024, currency in Aug 2026 unverified.
• Base rate exaggeration B1: IH median first-year MRR is $0, not the 8–15% P(first $500/30d) implied by report D for Show HN.
NEXT ACTION: Re-derive channel probabilities from primary sources before any investor conversation. Do not quote D/P intel numbers as fact.
LINK: `areas/quorum_research/HOSTILE_INVESTOR_REDTEAM_REPORTS_20260803.md`

*Not yet landed / missing:* `SESSION_INDEX_20260803.md`, `OPPORTUNITY_SCAN_TLDR_20260803.md`, `READY_TO_FIRE_TUESDAY.md`. Broadcaster flagged as MISSING per V11 §5 note.
