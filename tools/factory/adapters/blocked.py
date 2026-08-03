"""
Surfaces that were probed and are NOT usable at v0. Each records the exact
receipt so the PDCA states a fact, not an assumption, and so tomorrow's run can
re-probe cheaply instead of re-deriving.

All probes: 2026-08-02T04:00-04:12Z, clock_source host_read, plain curl, no auth.
"""
from __future__ import annotations

from typing import Iterator

from .. import httpcache
from ..core import Opportunity
from .base import OpportunityAdapter

# name -> (url, observed_status, diagnosis, what unblocks it)
PROBED: dict[str, tuple[str, str, str, str]] = {
    "upwork": (
        "https://www.upwork.com/ab/feed/jobs/rss?q=computer%20vision",
        "410 GONE on ALL THREE RSS forms + 403 on search "
        "(/ab/feed/jobs/rss -> 410 · /jobs/rss -> 410 · "
        "/api/profiles/v2/search/jobs.json -> 410 · /nx/search/jobs -> 403)",
        "Re-probed on operator request 2026-08-02T05:0xZ after the first 410. Upwork "
        "retired every public job feed; 410 is 'permanently gone', not a transient "
        "error or a bad query string. There is no URL that makes this work.",
        "Upwork has no free public search API. An approved API client (OAuth2 partner "
        "application) is the only programmatic route -- OPERATOR SIGN NEEDED, do not "
        "auth autonomously. In the meantime `hn_contracts` covers the same market (M1) "
        "with named buyers and published contact addresses, which Upwork RSS never had.",
    ),
    "wellfound": (
        "https://wellfound.com/jobs",
        "403 (Cloudflare bot challenge); api.wellfound.com/graphql -> 404",
        "Wellfound serves a bot challenge to any non-browser client and exposes no "
        "public jobs API. Scraping it would need headless-browser evasion, which is "
        "both ToS-breaking and a detection-evasion technique -- not something to build.",
        "No free route exists. M2 employment is already covered by 5 working boards; "
        "the marginal value of Wellfound over those is low. Recommend NOT pursuing.",
    ),
    "sbir": (
        "https://api.www.sbir.gov/public/api/solicitations?open=1",
        "429 on /solicitations and /awards, 403 on /topics, 404 on both RSS paths "
        '(body: {"Code":"TooManyRequestsError","Message":"The SBIR Public API is not '
        'available at this time."}) -- re-probed twice, 04:00Z and 05:0xZ',
        "Server-side outage on sbir.gov's own API, not a local rate limit: the FIRST "
        "call of each session already returned 429. The RSS feeds the brief asked for "
        "(/rss/solicitations.xml, /solicitations/rss) return 404 -- they do not exist.",
        "SUPERSEDED, not blocked: `grants_gov` covers this market and is strictly "
        "larger -- SBIR/STTR topics are a subset of federal opportunities and "
        "grants.gov carries NSF and DOD directly. Re-probe SBIR later if the "
        "agency-specific topic numbers are wanted.",
    ),
    "usajobs": (
        "https://data.usajobs.gov/api/search?Keyword=computer+vision",
        "401 Unauthorized",
        "USAJobs requires Authorization-Key + User-Agent email registration.",
        "Free key, 1 form at developer.usajobs.gov. OPERATOR SIGN NEEDED (2 min). "
        "Would add federal CV roles -- but these are M2 employment, already covered "
        "by 5 working boards.",
    ),
    "linkedin": (
        "n/a -- not probed, deliberately",
        "NOT ATTEMPTED",
        "Scraping LinkedIn violates their ToS and would be a reward-hack: it "
        "manufactures volume on a channel that bans on first detection.",
        "Use the linkedin_cached adapter: operator pastes real targets into "
        "state/factory_input/linkedin_targets.jsonl.",
    ),
    "poki_spec": (
        "https://developers.poki.com/",
        "200, 3,424 B, 44 chars of extractable text (JS SPA shell). "
        "CrazyGames 200/3,906 B/263 chars · GameDistribution 200/3,485 B/0 chars",
        "PROMOTED TO TIER-1 and shipped as the `game_portals` adapter. The portals "
        "themselves are live and reachable, but every developer site renders "
        "client-side, so submission REQUIREMENTS cannot be machine-read. The registry "
        "in adapters/games.py is therefore curated with requirements_verified=False.",
        "A human (or a browser-driving pass) must read each portal's current spec and "
        "flip requirements_verified. Until then every portal artifact says so in the "
        "body rather than guessing at the spec.",
    ),
}


class BlockedAdapter(OpportunityAdapter):
    """Yields nothing; carries the receipt."""
    market = "M0"

    def __init__(self, key: str, **kw) -> None:
        super().__init__(**kw)
        url, status, diagnosis, unblock = PROBED[key]
        self.name = f"blocked_{key}"
        self.surface = url
        self.observed_status = status
        self.diagnosis = diagnosis
        self.unblock = unblock
        self.blocked_reason = f"{status} | {diagnosis} | UNBLOCK: {unblock}"

    def search(self) -> Iterator[Opportunity]:
        return iter(())

    def reprobe(self) -> str:
        """Re-run the probe live so the PDCA can quote a fresh status."""
        if not self.surface.startswith("http"):
            return self.observed_status
        code = httpcache.probe(self.surface)
        return f"{code} (re-probed)" if code else f"{self.observed_status} (unreachable)"


def all_blocked() -> list[BlockedAdapter]:
    return [BlockedAdapter(k) for k in PROBED]
