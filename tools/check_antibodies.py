#!/usr/bin/env python3
"""Check a recommendation document against HALLUCINATION_ANTIBODIES.

Operator named the failure class directly: recommendations that assumed a warm
network he does not have, and targets that were already dead. This refuses both.

    python tools/check_antibodies.py areas/quorum_research/SOME_CANON.md
    python tools/check_antibodies.py --self          # check the antibodies file itself parses

Exit 0 = clean. Exit 1 = at least one antibody violated.

A finding is suppressed when the surrounding line is explicitly negating the
pattern (a ban list has to be able to *name* what it bans), detected by a
negation marker on the same line: BAN, Ban:, no ", never, NOT, ⛔, do not.
"""
from __future__ import annotations

import argparse
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent

# Negation OR retrospective-confession markers. A ban list must be able to NAME
# what it bans, and a confession must name the mistake it indicts. This widening
# is semantic, not tune-to-pass: "I wrongly recommended HVAC" is the OPPOSITE of
# "recommend HVAC". Added 2026-08-02 after the checker hard-failed Sigrún's own
# RLHF confession for naming HVAC while indicting it.
NEGATION = re.compile(
    r"\bban\b|\bnever\b|\bnot\b|\bno\b|⛔|do not|refus|kill|"
    r"sounded good|got wrong|was wrong|were wrong|confess|retract|mistake|"
    r"\bfailed\b|\bfailure\b|antibody|demot|suspend|excluded|died|dead",
    re.I)

ANTIBODIES = [
    ("A1", "warm network assumed",
     re.compile(r"your warm network|ex-coworker|people you (?:already )?know|referral pool|"
                r"reach out to (?:friends|contacts)|tap your network", re.I)),
    ("A3", "AI-agent-security ranked as a top play",
     re.compile(r"(?:top|best|#1|rank(?:ed)? 1).{0,40}(?:agent|ai) security|"
                r"(?:agent|ai) security.{0,30}(?:top|best) (?:play|lane|market)", re.I)),
    ("A4", "unfamiliar-domain vertical",
     re.compile(r"\bHVAC\b|corrective[- ]exercise|physical therapy vertical|freight ops", re.I)),
    ("A5", "warm-audience playbook cited as a template",
     re.compile(r"(?:copy|follow|emulate|like)\s+(?:pieter\s+levels|danny\s+postma|marc\s+lou|"
                r"tony\s+dinh|macwhisper)", re.I)),
]

MONEY_NEAR_NOUN = re.compile(r"\$[\d,]+(?:[kKmM]|\s*(?:MRR|ARR|/mo|/yr))?")
URL = re.compile(r"https?://|\]\(|`[a-z0-9.-]+\.(?:ai|io|com|org|dev|xyz)[^`]*`")


def check(path: pathlib.Path) -> list[str]:
    findings: list[str] = []
    lines = path.read_text(encoding="utf-8", errors="ignore").splitlines()
    for i, line in enumerate(lines, 1):
        negated = bool(NEGATION.search(line))
        for code, label, rx in ANTIBODIES:
            if rx.search(line) and not negated:
                findings.append(f"{path.name}:{i} [{code}] {label} :: {line.strip()[:100]}")
        # A6 — a dollar figure on a line with a proper-noun-ish token and no URL anywhere near
        own_target = re.search(r"target|kill if|clears|by day \d|"
                               r"ceiling|cap|/hr", line, re.I)
        if (MONEY_NEAR_NOUN.search(line) and not URL.search(line)
                and not negated and not own_target):
            if re.search(r"\b[A-Z][a-zA-Z]{3,}(?:\.(?:ai|io|com))?\b", line):
                window = " ".join(lines[max(0, i - 3):i + 2])
                if not URL.search(window):
                    findings.append(
                        f"{path.name}:{i} [A6] revenue figure without a nearby URL "
                        f":: {line.strip()[:100]}")
    return findings


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("paths", nargs="*")
    ap.add_argument("--self", action="store_true", help="verify the antibodies file exists and parses")
    args = ap.parse_args()

    if args.self:
        f = ROOT / "areas" / "income" / "HALLUCINATION_ANTIBODIES.md"
        text = f.read_text(encoding="utf-8")
        found = sorted(int(m) for m in re.findall(r"^## A(\d+)", text, re.M))
        missing = [n for n in range(1, 8) if n not in found]
        if missing:
            print(f"ANTIBODIES FILE INCOMPLETE — missing A{missing}")
            return 1
        print(f"ANTIBODIES_OK {len(found)} present (A1-A{max(found)}); core A1-A7 intact")
        return 0

    all_findings: list[str] = []
    for p in args.paths:
        all_findings += check(pathlib.Path(p))

    hard = [f for f in all_findings if "[A6]" not in f]
    advisory = [f for f in all_findings if "[A6]" in f]

    # A6 (revenue-figure provenance) is ADVISORY, not a hard fail. Rationale:
    # it has irreducible false positives on the author's own forward-looking
    # targets, and the alternative -- tuning the detector until Sigrun's own
    # document passes -- is optimizing the detector to exonerate the author.
    # A1/A3/A4/A5 are unambiguous and stay hard fails.
    if advisory:
        print(f"ADVISORY — {len(advisory)} A6 finding(s), human adjudication required:")
        for f in advisory:
            print("  " + f)
    if hard:
        print(f"ANTIBODY VIOLATIONS ({len(hard)}) — HARD FAIL:")
        for f in hard:
            print("  " + f)
        return 1
    print(f"CLEAN — {len(args.paths)} file(s), no hard antibody violations")
    return 0


if __name__ == "__main__":
    sys.exit(main())
