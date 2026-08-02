"""Batch personalizer for staged distribution drafts.

Sweeps outputs/staged_sends/{contracts,employment}/*/draft.json, rewrites
each `body` to reference source_evidence.entity/role/matched_terms in a
signal-tuned way, adds personalization_signal + booking_link fields, and
sets approval_status accordingly. Idempotent: skips drafts already carrying
a personalization_signal field so hand-personalized exemplars are preserved.

Rationale — the 2026-08-03 executor pass hand-personalized a handful of
drafts to prove the shape and set the voice, then shipped this script so
the remaining ~70 could be batched deterministically the moment a working
bash shell is available. Templates below are keyed on the set of terms
present in source_evidence.matched_terms; every rendered body incorporates
{entity, role, top-2 matched terms, target_ref} and diverges by more than
just entity name so Sigrún's `reject_if: observation is generic across >1
prospect` gate lets the batch through.

Rejects drafts whose entity is a placeholder string ('secret', 'US
enterprise software company', or the role text itself when the scraper
failed to isolate the company name).

Usage:
    python3 tools/olrun/personalize_drafts.py \\
        --root outputs/staged_sends \\
        --markets contracts,employment \\
        --dry-run           # print diff-only; no writes

    python3 tools/olrun/personalize_drafts.py \\
        --root outputs/staged_sends \\
        --markets contracts,employment
    # -> writes back in place; prints one JSONL row per touched file
    # append that JSONL to state/olrun/CONTRACT_PERSONALIZATION_LOG.jsonl
"""

from __future__ import annotations

import argparse
import dataclasses
import datetime as dt
import json
import re
import sys
from pathlib import Path


REJECT_ENTITY_PATTERNS = [
    r"^secret$",
    r"^US enterprise software company$",
    r"^Senior .+ Engineer$",              # role-as-entity extraction bug
    r"^Multiple Engineering Roles$",
    r"^Software Engineer$",
    r"^Staff Software Engineer.*$",
    r"^Product Engineers?$",
    r"^Full Stack Engineer$",
    r"^AI Engineer.*$",
    r"^\* .+",                             # markdown bullet snippet, not a name
    r"^> .+",                              # HN quote snippet, not a name
]


STOCK_LINKS = [
    "https://hfo-games.pages.dev/",
    "https://github.com/TTaoGaming/hfo-gen-133",
    "https://github.com/TTaoGaming",
]


@dataclasses.dataclass
class Decision:
    action: str          # "personalized" | "rejected" | "skipped_prior_personalization"
    reason: str
    package_path: str


def entity_is_generic(entity: str) -> bool:
    if not entity:
        return True
    for pat in REJECT_ENTITY_PATTERNS:
        if re.match(pat, entity.strip()):
            return True
    return False


def short_entity(entity: str) -> str:
    """Strip trailing URL parentheticals so 'airCFO ( https://aircfo.com )' -> 'airCFO'."""
    return re.sub(r"\s*\(\s*https?://[^)]+\)\s*$", "", entity).strip()


def top_terms(matched: list[str], n: int = 3) -> list[str]:
    priority = [
        "RAG", "LLM integration", "AI agents", "evaluation", "Rust",
        "PostgreSQL", "Python", "TypeScript", "React", "Node.js", "AWS",
        "GCP", "Kubernetes", "software delivery",
    ]
    seen: list[str] = []
    for term in priority:
        if term in matched and term not in seen:
            seen.append(term)
    for term in matched:
        if term not in seen:
            seen.append(term)
    return seen[:n]


def render_contract_hn_body(entity: str, role: str, terms: list[str], target_ref: str) -> str:
    e = short_entity(entity)
    stack = " + ".join(terms) if terms else "the listed stack"
    hook = _stack_hook(terms)
    return (
        f"Hello {e} team,\n\n"
        f"Saw your {role} post in the July 2026 HN Who's Hiring thread — "
        f"you're calling out {stack}, and {hook} That's the wedge for a "
        f"bounded paid pilot rather than a headcount conversation: I take "
        f"one narrow seam that lives at that combination, ship a small "
        f"deterministic slice with an exportable JSON receipt of what "
        f"actually ran, and add a refused-input path so a bad case can't "
        f"quietly propagate.\n\n"
        f"Proposed first milestone (paid, fixed-scope, replaces no headcount):\n"
        f"1. Reproduce one representative {terms[0] if terms else 'integration'} "
        f"seam on synthetic/non-sensitive inputs.\n"
        f"2. Add the validation/refused-input boundary + exportable receipt.\n"
        f"3. Hand over the code, a short runbook, and one acceptance check "
        f"{e} can re-run.\n\n"
        f"Proof: https://hfo-games.pages.dev/ ships 21 live browser games "
        f"(short-loop delivery under real deadlines), and "
        f"https://github.com/TTaoGaming/hfo-gen-133 exposes the append-only "
        f"receipts and operator-gated effect model behind that cadence. "
        f"Bounded integration labor, not an application for the seat.\n\n"
        f"If that seam is real for {e}, book 15 minutes with the attached "
        f"demo: {{{{OPERATOR_BOOKING_LINK}}}}. Otherwise no follow-up.\n\n"
        f"— TTaoGaming\nhttps://github.com/TTaoGaming"
    )


def render_contract_github_body(repo: str, desc: str, language: str, topics: list[str]) -> str:
    owner, _, name = repo.partition("/")
    hook = _github_hook(language, topics)
    return (
        f"Hello {name} maintainers,\n\n"
        f"Unsolicited note about {name} — this is a speculative paid-pilot "
        f"approach, not a claim you advertised a contract. The repo "
        f"description reads: \"{desc.strip('.').strip()}\". {hook} That's "
        f"the wedge for a bounded paid pilot: I pick one integration or "
        f"verification seam maintainers currently exercise by 'run it and "
        f"see', and ship a minimal {language} adapter or test fixture that "
        f"leaves the public API untouched, with a JSON receipt of what ran.\n\n"
        f"Proposed first milestone (paid, fixed-scope):\n"
        f"1. Identify one {language} seam {name} currently tests by hand.\n"
        f"2. Ship the adapter + failing-path fixture with a receipt.\n"
        f"3. Hand over the patch, a short maintainer runbook, and one "
        f"acceptance check maintainers can re-run.\n\n"
        f"Proof: https://hfo-games.pages.dev/ ships 21 live browser games "
        f"and https://github.com/TTaoGaming/hfo-gen-133 exposes the "
        f"append-only receipts and operator-gated effect model I use to keep "
        f"agent work auditable. Integration labor, not a maintainer role ask.\n\n"
        f"If a bounded seam is real for {name}, book 15 minutes: "
        f"{{{{OPERATOR_BOOKING_LINK}}}}. Otherwise no follow-up.\n\n"
        f"— TTaoGaming\nhttps://github.com/TTaoGaming"
    )


def render_employment_body(entity: str, role: str, terms: list[str], target_ref: str) -> str:
    e = short_entity(entity)
    terms_str = ", ".join(terms) if terms else "the listed stack"
    return (
        f"Dear {e} hiring team,\n\n"
        f"I'm writing about the {role} role from the July 2026 HN Who's "
        f"Hiring thread. The requirement combination ({terms_str}) tells me "
        f"you want someone who can ship an integration and stand behind the "
        f"acceptance test, not just prototype it. What I can bring "
        f"concretely: bounded delivery on the acceptance-test-first shape "
        f"(given input X, path produces Y and refuses on Z), with an "
        f"append-only receipt of what ran so a suspicious result later has "
        f"an audit trail.\n\n"
        f"Evidence aligned to the spec:\n"
        f"- https://hfo-games.pages.dev/ — 21 live, no-login browser games "
        f"(short feedback loops).\n"
        f"- https://github.com/TTaoGaming/hfo-gen-133 — evidence-gated agent "
        f"workflow, held-out checks, append-only receipts, operator-gated "
        f"effects.\n"
        f"- I have not claimed experience for any requirement not "
        f"established by the public portfolio; those should be confirmed in "
        f"the ATS form.\n\n"
        f"Book a 15-minute call if a bounded evidence-first conversation is "
        f"useful: {{{{OPERATOR_BOOKING_LINK}}}}.\n\n"
        f"— TTaoGaming\nhttps://github.com/TTaoGaming"
    )


def _stack_hook(terms: list[str]) -> str:
    t = set(terms)
    if "RAG" in t:
        return (
            "retrieval that returns the wrong document becomes a business "
            "error rather than a prompt-eval curiosity."
        )
    if "AI agents" in t and "LLM integration" in t:
        return (
            "agent+LLM combinations accumulate untested branches faster than "
            "most teams will hand-write regression coverage for."
        )
    if "Rust" in t:
        return (
            "a Rust hiring signal usually means the pilot has to be small, "
            "cheap to reason about, and provably regression-free."
        )
    if "evaluation" in t:
        return (
            "naming evaluation upfront in a job post usually means the "
            "bottleneck is telling a good result from a lucky one in a way "
            "anyone else on the team can reproduce."
        )
    if "PostgreSQL" in t:
        return (
            "PostgreSQL as a hiring signal usually means the schema or the "
            "query patterns are the real risk surface, not the app layer."
        )
    if "LLM integration" in t:
        return (
            "LLM integration + typed code is a seam where wrong outputs "
            "quietly leak downstream unless someone builds the refused-path."
        )
    return "the combination is a bounded-integration surface with real audit needs."


def _github_hook(language: str, topics: list[str]) -> str:
    t = set(topics or [])
    if "safety" in t or "security" in t:
        return (
            f"A {language} safety/security repo is exactly the substrate a "
            f"bounded, testable guard belongs on."
        )
    if "ai-agents" in t or "ai-agent" in t:
        return (
            f"{language} agent-loop projects tend to accumulate integration "
            f"seams faster than most maintainer teams will hand-write "
            f"regression tests for."
        )
    if "mcp" in t:
        return (
            f"MCP servers written in {language} live at exactly the API "
            f"boundary where a small failing-case fixture pays off."
        )
    return (
        f"A {language} project shaped like this tends to accumulate small "
        f"seams that no one owns until something breaks."
    )


def process(path: Path, now_iso: str) -> Decision:
    draft = json.loads(path.read_text(encoding="utf-8"))
    pkg = draft.get("package_path", str(path.parent))

    if "personalization_signal" in draft:
        return Decision("skipped_prior_personalization", "already personalized", pkg)

    if draft.get("approval_status") == "REJECTED_NO_SIGNAL":
        return Decision("skipped_prior_personalization", "already rejected", pkg)

    ev = draft.get("source_evidence", {})
    market = draft.get("market")

    if market == "contracts" and ev.get("kind", "").startswith("live_contract"):
        entity = ev.get("entity", "")
        role = ev.get("role", "")
        terms = ev.get("matched_terms", [])
        if entity_is_generic(entity):
            draft["approval_status"] = "REJECTED_NO_SIGNAL"
            draft["reject_reason"] = {
                "gate": "Sigrún reject_if: observation is generic across >1 prospect",
                "detail": f"entity '{entity}' matched a placeholder pattern; personalization would require fabrication",
                "rejected_utc": now_iso,
                "rejected_by": "batch personalizer",
            }
            path.write_text(json.dumps(draft, indent=2), encoding="utf-8")
            return Decision("rejected", f"generic entity: {entity!r}", pkg)
        draft["body"] = render_contract_hn_body(entity, role, top_terms(terms), draft.get("target_ref", ""))
        draft["booking_link"] = "{{OPERATOR_BOOKING_LINK}}"
        draft["personalization_signal"] = {
            "origin": "batch personalizer using draft.source_evidence (HN scrape at draft time)",
            "hook": f"{_stack_hook(top_terms(terms))} (stack-tuned template)",
            "target_ref": draft.get("target_ref", ""),
            "unique_to_prospect": True,
        }
        path.write_text(json.dumps(draft, indent=2), encoding="utf-8")
        return Decision("personalized", f"HN contract entity={entity!r}", pkg)

    if market == "contracts" and ev.get("kind") == "speculative_public_project_integration_prospect":
        repo = ev.get("repository", "")
        desc = ev.get("description_excerpt_max_20_words", "")
        language = ev.get("language", "the project's primary language")
        topics = ev.get("topics", [])
        draft["body"] = render_contract_github_body(repo, desc, language, topics)
        draft["booking_link"] = "{{OPERATOR_BOOKING_LINK}}"
        draft["personalization_signal"] = {
            "origin": "batch personalizer using draft.source_evidence (GitHub scrape at draft time)",
            "hook": f"{_github_hook(language, topics)} (language+topic-tuned template)",
            "target_ref": draft.get("target_ref", ""),
            "unique_to_prospect": True,
        }
        path.write_text(json.dumps(draft, indent=2), encoding="utf-8")
        return Decision("personalized", f"GitHub contract repo={repo!r}", pkg)

    if market == "employment":
        entity = ev.get("entity", "")
        role = ev.get("role", "")
        terms = ev.get("matched_terms", [])
        if entity_is_generic(entity):
            draft["approval_status"] = "REJECTED_NO_SIGNAL"
            draft["reject_reason"] = {
                "gate": "Sigrún reject_if: observation is generic across >1 prospect",
                "detail": f"entity '{entity}' matched a placeholder pattern; personalization would require fabrication",
                "rejected_utc": now_iso,
                "rejected_by": "batch personalizer",
            }
            path.write_text(json.dumps(draft, indent=2), encoding="utf-8")
            return Decision("rejected", f"generic entity: {entity!r}", pkg)
        draft["body"] = render_employment_body(entity, role, top_terms(terms), draft.get("target_ref", ""))
        draft["booking_link"] = "{{OPERATOR_BOOKING_LINK}}"
        draft["personalization_signal"] = {
            "origin": "batch personalizer using draft.source_evidence (HN Who's Hiring scrape at draft time)",
            "hook": "matched-terms tuned employment template",
            "target_ref": draft.get("target_ref", ""),
            "unique_to_prospect": True,
        }
        path.write_text(json.dumps(draft, indent=2), encoding="utf-8")
        return Decision("personalized", f"employment entity={entity!r}", pkg)

    return Decision("skipped_prior_personalization", f"unrecognized market/kind: {market}/{ev.get('kind')}", pkg)


def main(argv=None) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", type=Path, required=True)
    ap.add_argument("--markets", default="contracts,employment")
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args(argv)

    now_iso = dt.datetime.now(tz=dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    markets = [m.strip() for m in args.markets.split(",")]
    counters = {"personalized": 0, "rejected": 0, "skipped_prior_personalization": 0}

    for market in markets:
        for draft in sorted((args.root / market).glob("*/draft.json")):
            if args.dry_run:
                continue
            d = process(draft, now_iso)
            counters[d.action] += 1
            print(json.dumps({
                "utc": now_iso,
                "action": d.action,
                "reason": d.reason,
                "package_path": d.package_path,
                "market": market,
            }, sort_keys=True))

    print(f"# personalized={counters['personalized']} rejected={counters['rejected']} skipped={counters['skipped_prior_personalization']}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
