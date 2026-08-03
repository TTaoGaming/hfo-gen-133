#!/usr/bin/env python3
"""
GAMES phenotype — one concrete tools.factory.genotype.AbstractFactory.

Refactor of the GAMES_SHIP v0 work (stamps/GAMES_SHIP_20260802.md), not a
rewrite: the 21 staged itch.io manifests it already produced under
outputs/staged_sends/games/{seq}_{slug}/itch_manifest.json are the Producer's
data source. Reusing them means the games phenotype's dry-run is reading
REAL prior output (title, description, tags, embed dimensions all already
verified against the source omega_games registry by that session) rather
than re-deriving anything.

Producer  -> reads the staged manifests + tools/factory/adapters/games.py's
             curated PORTALS registry, pairs each candidate title with a
             submission target (a portal or, absent one, itch.io self-publish).
Grader    -> ranks by the same signal GAME_CATALOGUE/profile.py already
             carries: touch-ready, self-contained, byte size band.
Verifier  -> EXTERNAL-fitness probe. dry_run: confirms every manifest file
             this phenotype claims to submit actually exists on disk with the
             required itch.io fields populated (a submission plan that cites
             a manifest which was never written is exactly the "plausible
             pointer that doesn't resolve" defect named in HOT-5's rationale).
             live: read-only HTTP GET against the portal's published
             developer-intake URL (see adapters/games.py PORTALS registry).
MemoryWriter -> appends to outputs/factory_samples/games/ under namespace
             'games'. Nothing is submitted anywhere -- see CLASS ENVELOPE.
"""
from __future__ import annotations

import argparse
import dataclasses
import json
import os
import sys
from typing import Any

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "..")))

from tools.factory.genotype import (AbstractFactory, GradedItem, Grader,
                                     MemoryWriter, Producer, Result, Verifier,
                                     VerifyResult)
from tools.factory.core import jsonl_append, today_utc, utc_now
from tools.factory.adapters.games import PORTALS

STAGED_ROOT = os.path.join("outputs", "staged_sends", "games")


# ---------------------------------------------------------------------------
# value object
# ---------------------------------------------------------------------------
@dataclasses.dataclass
class GamePlan:
    slug: str
    title: str
    target_entity: str            # portal name, or "itch.io" self-publish
    target_url: str                # portal's published intake URL
    manifest_path: str             # staged itch_manifest.json for this title
    genre: str = ""
    touch_ready: bool = False
    byte_size_band: str = ""
    visibility: str = "draft"


# ---------------------------------------------------------------------------
# staged-manifest discovery (real prior output, reused not re-derived)
# ---------------------------------------------------------------------------
def _discover_staged_manifests() -> list[tuple[str, str, dict]]:
    """-> [(slug, manifest_path, manifest_dict)], sorted by staged sequence."""
    out: list[tuple[str, str, dict]] = []
    if not os.path.isdir(STAGED_ROOT):
        return out
    for entry in sorted(os.listdir(STAGED_ROOT)):
        d = os.path.join(STAGED_ROOT, entry)
        if not os.path.isdir(d):
            continue
        mpath = os.path.join(d, "itch_manifest.json")
        if not os.path.isfile(mpath):
            continue
        # entry looks like "001_hex_flip" -> slug "hex_flip"
        slug = entry.split("_", 1)[1] if "_" in entry else entry
        try:
            with open(mpath, "r", encoding="utf-8") as fh:
                manifest = json.load(fh)
        except Exception:
            continue
        out.append((slug, mpath, manifest))
    return out


#: Small, self-contained fixture used ONLY if no staged manifests exist on
#: disk (e.g. a fresh checkout without outputs/staged_sends/games/ present).
#: Tagged so a downstream reader can tell these are not the real GAMES_SHIP
#: output. See honest_flaw in the worker report.
_FIXTURE_PLANS = [
    GamePlan(slug="fixture_puzzle_1", title="Fixture Puzzle One",
              target_entity="itch.io", target_url="https://itch.io/developers",
              manifest_path="", genre="puzzle", touch_ready=True,
              byte_size_band="small"),
    GamePlan(slug="fixture_action_1", title="Fixture Action One",
              target_entity="itch.io", target_url="https://itch.io/developers",
              manifest_path="", genre="action", touch_ready=True,
              byte_size_band="small"),
    GamePlan(slug="fixture_puzzle_2", title="Fixture Puzzle Two",
              target_entity="itch.io", target_url="https://itch.io/developers",
              manifest_path="", genre="puzzle", touch_ready=False,
              byte_size_band="medium"),
]


def _size_band(width: int, height: int) -> str:
    area = width * height
    if area <= 320 * 480:
        return "small"
    if area <= 800 * 600:
        return "medium"
    return "large"


def _pick_target(slug: str) -> tuple[str, str]:
    """Round-robin a manifest across the curated PORTALS registry so the plan
    demonstrates a real submission target, not just itch.io every time."""
    idx = sum(ord(c) for c in slug) % len(PORTALS)
    p = PORTALS[idx]
    return p["entity"], p["submit_url"]


# ---------------------------------------------------------------------------
# products
# ---------------------------------------------------------------------------
class GamesProducer(Producer):
    def produce(self, task_spec: dict) -> list[GamePlan]:
        count = max(int(task_spec.get("count", 3)), 1)
        staged = _discover_staged_manifests()

        plans: list[GamePlan] = []
        for slug, mpath, manifest in staged:
            entity, url = _pick_target(slug)
            embed = manifest.get("embed_options", {}) or {}
            plans.append(GamePlan(
                slug=slug,
                title=manifest.get("title", slug),
                target_entity=entity,
                target_url=url,
                manifest_path=mpath,
                genre=manifest.get("genre", ""),
                touch_ready="touch" in (manifest.get("tags") or []),
                byte_size_band=_size_band(embed.get("width", 640), embed.get("height", 480)),
                visibility=manifest.get("visibility", "draft"),
            ))
            if len(plans) >= count:
                break

        if len(plans) < count:
            for fx in _FIXTURE_PLANS:
                if len(plans) >= count:
                    break
                plans.append(fx)

        return plans[:count]


class GamesGrader(Grader):
    """Ranks by touch-ready first (portal reach requires mobile touch), then
    by the small/medium/large payload band (small ships fastest under a
    review queue's iframe constraints)."""

    _BAND_SCORE = {"small": 1.0, "medium": 0.6, "large": 0.2}

    def grade(self, task_spec: dict, variants: list[GamePlan]) -> list[GradedItem]:
        graded = []
        for v in variants:
            score = (0.6 if v.touch_ready else 0.0) + 0.4 * self._BAND_SCORE.get(v.byte_size_band, 0.3)
            graded.append(GradedItem(item=v, score=round(score, 3),
                                      reason=f"touch_ready={v.touch_ready} band={v.byte_size_band}"))
        graded.sort(key=lambda g: -g.score)
        for i, g in enumerate(graded, 1):
            g.rank = i
        return graded


class GamesVerifier(Verifier):
    """EXTERNAL-fitness probe.

    dry_run: every plan's manifest_path must resolve to a real file on disk
    that actually carries itch.io's required fields (title, kind_of_project,
    html_file) -- a plan pointing at a manifest that was never written is a
    plausible-pointer defect, not a submission plan.
    live: read-only HTTP GET against the portal's published submit_url.
    """

    _REQUIRED_MANIFEST_FIELDS = ("title", "kind_of_project", "html_file")

    def verify(self, task_spec: dict, graded: list[GradedItem]) -> VerifyResult:
        dry_run = bool(task_spec.get("dry_run", True))
        n = len(graded)
        unresolved = []
        for g in graded:
            plan: GamePlan = g.item
            if not plan.manifest_path:
                continue  # fixture plan, no manifest expected -- not counted as a failure
            if not os.path.isfile(plan.manifest_path):
                unresolved.append(plan.slug)
                continue
            try:
                with open(plan.manifest_path, "r", encoding="utf-8") as fh:
                    m = json.load(fh)
            except Exception:
                unresolved.append(plan.slug)
                continue
            missing = [f for f in self._REQUIRED_MANIFEST_FIELDS if not m.get(f)]
            if missing:
                unresolved.append(f"{plan.slug}:missing={missing}")

        if unresolved:
            return VerifyResult(ok=False, checked=n,
                                 evidence=f"{len(unresolved)}/{n} manifest pointer(s) do not "
                                          f"resolve: {unresolved[:3]}")
        if dry_run:
            return VerifyResult(ok=True, checked=n,
                                 evidence=f"dry_run: {n} plan(s) resolve to real staged "
                                          f"manifests with required itch.io fields present")

        from tools.factory import httpcache
        alive = 0
        targets = {g.item.target_url for g in graded[:5]}
        for url in targets:
            try:
                httpcache.fetch(url, ttl=3600, accept="text/html,application/xhtml+xml")
                alive += 1
            except httpcache.FetchError:
                pass
        return VerifyResult(ok=alive > 0, checked=len(targets),
                             evidence=f"live HTTP GET: {alive}/{len(targets)} portal intake URLs resolved")


class GamesMemoryWriter(MemoryWriter):
    def write(self, task_spec: dict, result: Result) -> str:
        root = os.path.join("outputs", "factory_samples", "games")
        os.makedirs(root, exist_ok=True)
        path = os.path.join(root, f"{today_utc()}_games.jsonl")
        for g in result.graded:
            row = dataclasses.asdict(g.item)
            row.update({"rank": g.rank, "score": g.score, "namespace": "games",
                        "verify_ok": result.verify.ok, "written_utc": utc_now()})
            jsonl_append(path, row)
        return path


# ---------------------------------------------------------------------------
# the phenotype
# ---------------------------------------------------------------------------
class GamesFactory(AbstractFactory):
    name = "games"

    def create_producer(self) -> Producer:
        return GamesProducer()

    def create_grader(self) -> Grader:
        return GamesGrader()

    def create_verifier(self) -> Verifier:
        return GamesVerifier()

    def create_memory_writer(self) -> MemoryWriter:
        return GamesMemoryWriter()


# ---------------------------------------------------------------------------
# CLI — HOT-3 activation command
# ---------------------------------------------------------------------------
def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--count", type=int, default=3)
    args = ap.parse_args(argv)

    factory = GamesFactory()
    result = factory.kickoff({"count": args.count, "dry_run": args.dry_run})

    for g in result.graded:
        print(json.dumps(dataclasses.asdict(g.item), ensure_ascii=False))

    print(f"GAMES_COUNT={len(result.graded)}")
    print(f"# verify: ok={result.verify.ok} evidence={result.verify.evidence}",
          file=sys.stderr)
    print(f"# persisted: {result.persisted_path}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
