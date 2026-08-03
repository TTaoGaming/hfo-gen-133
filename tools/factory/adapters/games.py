"""
M5 GAMES adapter — curated web-game portals + itch.io game jams.

Two distinct opportunity shapes, because they have different acceptance tests:

  * **Portals** (Poki, CrazyGames, GameDistribution, ...) are the *income* path.
    Canon SIGRUN_5Q §2 ranks M5 #2 at P=0.20 and notes it is the only market
    carrying BOTH the operator's thesis and class-preauthorizability. Portals pay
    revenue share / licensing. The acceptance event is a portal replying with
    terms or a review date.
    Their developer sites are JavaScript SPAs -- probed 2026-08-02T05:0xZ, all
    return 200 with 0-263 chars of extractable text -- so submission requirements
    CANNOT be machine-read. This registry is therefore CURATED and every
    requirement is marked `verified: False` until a human reads the portal docs.
    That is a deliberate honesty flag, not a TODO.

  * **Jams** (itch.io) are a *distribution / audience* path, not income. Most pay
    nothing. They are included because they are the cheapest way to put a
    gesture-controlled browser build in front of players who will actually try a
    novel input, and because a jam host is a real named human running a real
    dated event. The acceptance event is a host confirming a slot or a date.

NO INDIVIDUAL PROFILING. Portal submissions are addressed to the portal's own
published intake channel, not to a named employee assembled from cross-source
searching. Jam hosts are used only as the platform publicly displays them on the
jam's own page.
"""
from __future__ import annotations

import html as _html
import re
from typing import Iterator

from .. import httpcache
from ..core import Opportunity, clean_entity, clean_title, make_uid, strip_html
from .base import OpportunityAdapter

# ---------------------------------------------------------------------------
# CURATED PORTAL REGISTRY
# `requirements_verified: False` everywhere -- see module docstring.
# ---------------------------------------------------------------------------
PORTALS = [
    {
        "slug": "poki",
        "entity": "Poki",
        "submit_url": "https://developers.poki.com/",
        "probe": "HTTP 200, 3,424 B, 44 chars of text (SPA shell)",
        "model": "revenue share on web plays; curated -- an editor reviews each submission",
        "known_requirements": [
            "HTML5, playable in an iframe on their domain",
            "mobile + desktop, touch and mouse",
            "Poki SDK integration for ads/analytics before launch",
            "no third-party ads or external analytics in the build",
        ],
        "requirements_verified": False,
        "why_fit": ("their catalogue is short-session browser games with one legible verb, "
                    "which is exactly the shape of the existing titles"),
    },
    {
        "slug": "crazygames",
        "entity": "CrazyGames",
        "submit_url": "https://developer.crazygames.com/",
        "probe": "HTTP 200, 3,906 B, 263 chars of text (SPA shell)",
        "model": "revenue share; self-serve developer portal with a review queue",
        "known_requirements": [
            "HTML5 build, iframe-embeddable",
            "CrazyGames SDK for ads",
            "mobile-responsive",
        ],
        "requirements_verified": False,
        "why_fit": "self-serve intake, so submission does not depend on knowing an editor",
    },
    {
        "slug": "gamedistribution",
        "entity": "GameDistribution",
        "submit_url": "https://www.gamedistribution.com/",
        "probe": "HTTP 200, 3,485 B, 0 chars of text (SPA shell)",
        "model": "syndication network -- one submission is distributed to many publisher sites",
        "known_requirements": [
            "HTML5, iframe-embeddable",
            "GD SDK integration",
            "no external network calls in the build",
        ],
        "requirements_verified": False,
        "why_fit": "syndication multiplies one repackaged title across many sites",
    },
    {
        "slug": "itch_io",
        "entity": "itch.io",
        "submit_url": "https://itch.io/developers",
        "probe": "HTTP 200 (itch.io serves real HTML, unlike the portal SPAs)",
        "model": "self-publish, pay-what-you-want, developer sets revenue share",
        "known_requirements": [
            "upload an HTML5 zip with index.html at the root",
            "set the viewport dimensions in the project settings",
        ],
        "requirements_verified": False,
        "why_fit": ("zero gatekeeping -- the only channel where the operator can publish "
                    "tonight without anyone's approval, which makes it the control case"),
    },
]


class GamePortalsAdapter(OpportunityAdapter):
    """Standing submission channels. Small N, high intent."""
    name = "game_portals"
    market = "M5"
    surface = "Curated web-game portal submission channels (Poki, CrazyGames, GameDistribution, itch.io)"
    legal_note = ("Portal requirements below are CURATED, not machine-read: every developer "
                  "site is a JavaScript SPA that returns no extractable text. Treat each "
                  "requirement as unverified until read on the portal itself.")

    def search(self) -> Iterator[Opportunity]:
        for p in PORTALS:
            reqs = "\n".join(f"- {r}" for r in p["known_requirements"])
            body = (
                f"{p['entity']} accepts third-party HTML5 web games.\n"
                f"Business model: {p['model']}.\n"
                f"Why this portal fits the existing catalogue: {p['why_fit']}.\n"
                f"Published submission channel: {p['submit_url']}\n"
                f"Requirements (UNVERIFIED -- portal site is a JS SPA, probe: {p['probe']}):\n"
                f"{reqs}\n"
                f"This is a browser HTML5 game portal requiring iframe-embeddable builds "
                f"with mobile touch support and an SDK integration.\n"
            )
            yield Opportunity(
                uid=make_uid(self.name, p["submit_url"], p["slug"]),
                adapter=self.name, market=self.market,
                title=f"HTML5 game submission — {p['entity']}",
                entity=p["entity"], url=p["submit_url"],
                location="web", compensation=p["model"],
                tags=["html5 game", "browser game", "portal", "web"],
                body=body,
                source_payload={"slug": p["slug"], "model": p["model"],
                                "requirements_verified": p["requirements_verified"],
                                "known_requirements": p["known_requirements"],
                                "probe": p["probe"]},
            )


# ---------------------------------------------------------------------------
# ITCH.IO GAME JAMS
# ---------------------------------------------------------------------------
_JAM_CELL = re.compile(
    r'data-jam_id="(\d+)"[^>]*class="jam_cell"[^>]*>.*?'
    r'<a href="(/jam/[^"]+)"[^>]*>(.*?)</a>'
    r'(?:<span class="joined_count">\((\d[\d,]*) joined\)</span>)?',
    re.S)
_HOSTED_BY = re.compile(r'hosted by\s*(.{2,60}?)\s*(?:<|\.|👤|&#)', re.S)


class ItchJamsAdapter(OpportunityAdapter):
    """Game jams with a named host, a live URL and published rules.

    Ranked by participant count, which is the only reach signal itch exposes on
    the index -- and reach is the whole point of entering a jam.
    """
    name = "itch_jams"
    market = "M5"
    surface = "itch.io game jams index + individual jam pages"
    legal_note = "Source: itch.io (https://itch.io/jams), public pages, no auth."
    INDEX = "https://itch.io/jams"
    JAM = "https://itch.io{path}"

    #: how many jam pages to fetch per run (each is one HTTP GET)
    DETAIL_BUDGET = 26

    def search(self) -> Iterator[Opportunity]:
        index = httpcache.fetch(self.INDEX, ttl=self.ttl,
                                accept="text/html,application/xhtml+xml")
        cells = []
        for jam_id, path, title, joined in _JAM_CELL.findall(index):
            n = int((joined or "0").replace(",", ""))
            cells.append((n, jam_id, path, _html.unescape(re.sub("<[^>]+>", "", title)).strip()))
        cells.sort(key=lambda c: -c[0])

        emitted = 0
        for n, jam_id, path, title in cells[: self.DETAIL_BUDGET * 2]:
            if emitted >= min(self.limit, self.DETAIL_BUDGET):
                return
            url = self.JAM.format(path=path)
            try:
                page = httpcache.fetch(url, ttl=self.ttl,
                                       accept="text/html,application/xhtml+xml")
            except httpcache.FetchError:
                continue
            body = self._body(page)
            if len(body) < 200:
                continue
            host = self._host(page)
            yield Opportunity(
                uid=make_uid(self.name, url, jam_id),
                adapter=self.name, market=self.market,
                title=clean_title(title),
                entity=clean_entity(host) or clean_title(title)[:40],
                url=url,
                location="online",
                compensation=("prizes mentioned" if re.search(r"(?i)\bpriz", body) else
                              "no cash prize stated"),
                tags=["game jam", "html5 game", "browser game", "itch.io"],
                body=(f"Game jam '{title}' hosted by {host or 'an itch.io user'}, "
                      f"{n} participants joined.\nThis is a browser game jam; entries are "
                      f"HTML5 games playable on the web.\nJam rules and theme as published:\n"
                      f"{body}"),
                source_payload={"jam_id": jam_id, "joined": n, "host": host,
                                "reach_rank_signal": "participants joined"},
            )
            emitted += 1

    # ------------------------------------------------------------------
    @staticmethod
    def _body(page: str) -> str:
        m = re.search(r'<div class="jam_content[^"]*">(.*?)</div>\s*</div>', page, re.S)
        raw = m.group(1) if m else ""
        if not raw:
            m2 = re.search(r'<div class="user_formatted[^"]*">(.*?)</div>', page, re.S)
            raw = m2.group(1) if m2 else ""
        return strip_html(raw)[:4000]

    @staticmethod
    def _host(page: str) -> str:
        m = _HOSTED_BY.search(page)
        if m:
            return strip_html(m.group(1)).strip()
        m2 = re.search(r'<a[^>]+href="https://([a-z0-9-]+)\.itch\.io/?"[^>]*>', page)
        return m2.group(1).replace("-", " ").title() if m2 else ""
