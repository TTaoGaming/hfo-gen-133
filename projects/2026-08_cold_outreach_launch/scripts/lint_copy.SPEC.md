# lint_copy.py — spec for a code lane to implement

```yaml
status: SPEC ONLY -- not executable code. Claude Lane Policy blocked direct .py authoring
        this session: hfo-gate denied with "code_authoring: no valid lease for
        code_authoring (required verb=EMERGENCY_FORGE)". The operator's directive said
        "launch sonnet to build it" in conversational framing, not the literal typed
        verb=EMERGENCY_FORGE token the gate requires -- so this session did not
        self-authorize past a fired symbolic gate (per CLAUDE.md "Enforcement Teeth in
        Force: trust the symbolic gate, not the neural claim").
route: hand this spec to a code lane (Codex / Antigravity / vendor mesh) OR have the
       operator type verb=EMERGENCY_FORGE to unblock direct authoring in a Claude
       compose-lane session.
target_path: projects/2026-08_cold_outreach_launch/scripts/lint_copy.py
run_as: python lint_copy.py copy/campaign_01_sequence.md   (from the project root)
```

## Purpose

Lint a cold-email campaign sequence markdown file (shape: `campaign_01_sequence.md`)
before it is eligible to be pasted into Instantly. Exit 0 = pass, non-zero = fail with
reasons on stderr. No network calls, no file writes, read-only against the one path
given on argv[1].

## Expected input shape

The target markdown file has:
- A `## Email 1` section containing a `**Subject** ...:` fenced code block (the raw
  subject line) and a `**Body** ...:` fenced code block (the raw body text, blank
  lines preserved).
- A `## Email 2 ...` section containing a `**Body** ...:` fenced code block.
- A `## Email 3 ...` section containing a `**Body** ...:` fenced code block.
- Sections end at the next line starting with `## ` or end of file.

## Checks to enforce

1. **Subject length** — Email 1 subject, stripped, must be `<= 60` characters.
2. **Word limits per email** — word count = `len(text.split())` on the raw body text:
   - Email 1 body `<= 120` words
   - Email 2 body `<= 80` words
   - Email 3 body `<= 60` words
3. **Exactly one CTA in Email 1** — count either literal occurrences of `{{cta}}`, or
   (if none) lines in the Email 1 body whose stripped text ends in `?`. Must equal
   exactly 1.
4. **Opt-out present in Email 1** — the substring `not relevant` (case-insensitive)
   must appear somewhere in the Email 1 body.
5. **Required variables in Email 1** — `{{first_name}}`, `{{company}}`, and
   `{{personalization_hook}}` must each appear at least once in the Email 1 body.
6. **Variable allowlist, all sections** — every `{{...}}` token (regex
   `\{\{[a-zA-Z0-9_]+\}\}`) found in the subject or any of the three bodies must be
   one of:
   `{{first_name}}`, `{{company}}`, `{{personalization_hook}}`, `{{sender_name}}`,
   `{{operator_name}}`, `{{sender_company}}`,
   `{{physical_mailing_address_or_po_box}}`, `{{unsubscribe_link}}`.
   Anything else (e.g. a typo'd `{{firstname}}`) is a fail.
7. **Banned phrases, all sections** — case-insensitive substring match against subject
   and all three bodies. Fail if any of these appear (HFO/Norse mythic-register leakage,
   since prospect-facing copy must stay in boring/technical register):
   `valkyrie`, `sigrun`, `hluti`, `drapa`, `blodfraendi`, `hive fleet obsidian`,
   `hfo ` (with trailing space), `kin-band`, `obsidian spider`, `reflex-before-reason`.
   Plus generic spam-trigger phrases: `act now`, `limited time`, `risk-free`,
   `100% free`, `guarantee`, `no obligation`, `click here`, `buy now`,
   `once in a lifetime`.
   Note: this list is a reasonable default, not a substitute for a real brand-jargon
   audit — none was found in-forge as of 2026-07-31
   (`state/ssot/outreach_inventory_20260731.jsonl`). Update this list if/when Sigrún's
   delegation spec or a dedicated jargon audit lands.

## Output contract

- All violations collected (don't stop at first failure) and printed to stderr as a
  bulleted list, prefixed with a `FAIL: N issue(s) in <path>` line.
- On success, print `PASS: <path>` to stdout and exit 0.
- Exit 2 (not 1) for usage errors (missing arg, file not found) so CI can distinguish
  "lint failed" from "lint mis-invoked."

## Reference implementation for the code lane

A complete draft implementation (regex-based section/code-block extraction, all seven
checks above) was written in full during this session and is preserved verbatim in
this project's build history for the code lane to use as a starting point rather than
writing from scratch — ask the operator or check this session's transcript for the
`lint_copy.py` content that was attempted before the gate fired, or re-derive directly
from the check list above; it is a small, self-contained ~150-line script with no
external dependencies (stdlib `re`, `sys`, `pathlib` only).
