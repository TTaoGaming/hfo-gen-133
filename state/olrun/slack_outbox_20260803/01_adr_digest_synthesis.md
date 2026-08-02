🧭 *GEN-133 ADR DIGEST — 2026-08-03 (batch of 6)*

Session ratified six decisions today. Each entry: CONTEXT · DECISION · AUTHOR · LINK. Full ADR file backlog does not exist in `canon/adr/` (only ADR-0001 lives there); these are session-level rulings written into canon documents.

📌 *ADR-20260803-throttle-killed-at-source*
CONTEXT: FRAMEWORK v1 §2 targeted 10–17 shipped units/week; V9 canon and Jörmungandr red-team both flagged the war between framework and 1/wk cap
DECISION: The 10–17 figure is DELETED from FRAMEWORK at source (not reconciled in commentary). New target: 1 shipped unit/week HARD CAP. Cap lifts only on ≥1 paying customer OR ≥100 organic impressions.
AUTHOR: SIGRÚN V11 (claude-opus-5)
LINK: `areas/quorum_research/SIGRUN_CANON_V11_SIX_LANES_20260803.md` §Preamble+§3+§6

📌 *ADR-20260803-hvac-demoted-ai-dev-promoted*
CONTEXT: Multiple HVAC verticals in candidate pool; operator confirmed unfamiliar-domain (Q1–Q7 answers, no-warm-network anchor); AI-dev-tools identified as ICP fit
DECISION: HVAC row killed everywhere in candidate pool. ICP locked to AI developers / agent builders / indie devs / small AI-ML consultancies. Elite kills also ratified: `dev/$29–49/marketplace` (cal.com booking), `prosumer/$9–19/directory` (podcast), `prosumer/free/directory` (clipboard).
AUTHOR: SIGRÚN V11 §1 (accepting Jörmungandr elite kills 1–3)
LINK: `areas/quorum_research/SIGRUN_CANON_V11_SIX_LANES_20260803.md` §1

📌 *ADR-20260803-class-preauth-gate-roundtrip-required*
CONTEXT: V9 §A claimed `class:` gate format was implemented (`class:<name>:quota=<N>:seq_range=<a-b>:expires=<UTC>`); Jörmungandr red-team §A row 3 challenged: no parser verified end-to-end
DECISION: `class:` preauth counts as working ONLY after a roundtrip probe (write test line, run one dry loop, receive one echo). Until then it is documented, not executed. Extended to all `class:` lines, not just the first.
AUTHOR: SIGRÚN V11 §3 bright-line 2 (adopting Jörmungandr §A row 3 verbatim)
LINK: `areas/quorum_research/SIGRUN_CANON_V11_SIX_LANES_20260803.md` §3

📌 *ADR-20260803-booking-url-hard-block*
CONTEXT: V8 §5 measured every CTA is `href="#book"`; V9 §A still lists `booking links on landers = 0`; four canons old, still unbuilt
DECISION: No unit ships and no cold-email envelope fires until `curl -sSf $BOOKING_URL` returns 200 on a real Cal.com/Calendly page. Bright line, adopted from Jörmungandr §A row 2 verbatim.
AUTHOR: SIGRÚN V11 §3 bright-line 1
LINK: `areas/quorum_research/SIGRUN_CANON_V11_SIX_LANES_20260803.md` §3

📌 *ADR-20260803-six-lanes-with-hands-hours-budget*
CONTEXT: V10 two-lane shape criticized by Jörmungandr §A row 5 as under-budgeted for support burden and lane discipline
DECISION: Six lanes (S/D/P/R/C/H) with explicit operator hands-hours budget: S=3.0, D=1.0, C=0.5, P=0.5, R=0, H=0 (R and H are swarm-only, must never consume operator time in August). S is the only lane with a $ target; other five feed it or keep it honest. Fallback: if lane discipline costs S hours, collapse to two lanes (S+D).
AUTHOR: SIGRÚN V11 §2
LINK: `areas/quorum_research/SIGRUN_CANON_V11_SIX_LANES_20260803.md` §2

📌 *ADR-20260803-recurring-loops-auto-pause-on-empty-queue*
CONTEXT: `RECURRING_FOSS_CANDIDATE_SCAN` / `RECURRING_DEMAND_SIGNAL_MINE` / `RECURRING_SEO_DIRECTORIES` all likely to emit `target_queue_empty` by day 14; classic Fenrir Potemkin-loop pattern
DECISION: All three loops auto-pause on the SECOND consecutive `target_queue_empty` event. Pre-registered kill, Fenrir pattern pre-empted rather than re-run.
AUTHOR: SIGRÚN V11 §4
LINK: `areas/quorum_research/SIGRUN_CANON_V11_SIX_LANES_20260803.md` §4

*Broadcaster caveat:* This message is staged, not sent — see credential blocker. When posted, thread the six ADRs as replies to a single parent (`ADR digest 2026-08-03, 6 entries below`) once webhook variant supports threading; otherwise send as one long message.
