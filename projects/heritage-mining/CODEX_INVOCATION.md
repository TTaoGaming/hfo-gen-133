# CODEX_INVOCATION.md — exact commands to start the mining loop

```yaml
schema_id: hfo.gen133.codex_invocation.v1_0
audience: the OPERATOR, pasting into a Codex session on the Windows host
valid_time_utc: 2026-07-30T07:00:00Z
```

## 1 · Set up the working tree

```powershell
# clone the canonical public remote (or pull if you already have it)
cd C:\Dev
git clone https://github.com/TTaoGaming/hfo-gen-133.git hfo_gen_133_codex
cd C:\Dev\hfo_gen_133_codex

# branch per session — UTC stamped, never work on main
$utc = (Get-Date).ToUniversalTime().ToString("yyyyMMddTHHmmssZ")
git checkout -b "codex/heritage-mining-$utc"
```

`cwd` for the Codex session: `C:\Dev\hfo_gen_133_codex`

## 2 · The initial prompt (paste verbatim — deliberately short)

```
You are the Codex heritage-mining lane for HFO gen-133, seat P6 ASSIMILATE.

Read these four files before doing anything:
  projects/heritage-mining/CODEX_HERITAGE_DISPATCH.md   <- your playbook
  CARRIER_CONTRACT.md                                   <- your ceiling and refusals
  CRYPTO_CHAIN_SPEC.md                                  <- how a row must verify
  state/GEN133_CLEANLINESS_PASS.md                      <- what is already dirty

Then execute the dispatch in the order given in its section 7, starting with
T1 (gen-130 enforcement organs). Import ONE artifact at a time. Every import
gets an IMPORT_RECEIPT.md with a source_sha256 you computed yourself, plus a row
in state/ssot/heritage_imports.jsonl. Commit per artifact.

Hard rules from section 4: no .sqlite, no credentials, no file over 10 MB
without written justification, no half-written stubs, dedupe by content hash,
no bulk directory copies.

Provenance trap: hfo_gen_131_forge contains gen-132 content at HEAD. Determine
source_gen from git log and schema_id, NEVER from the directory name.

You are READ-ONLY on gen 98-132 and APPEND-ONLY on gen-133. Do not write any
gen-132 chain row -- that forge is quarantined. Do not push to main; push your
codex/heritage-mining-* branch and open a PR for Sigrun to review-merge.

End the session with a row in state/ssot/codex_lane_return.jsonl. Raise an Andon
flag instead of pushing through if a source's provenance cannot be established,
a chain appears forked, or you find a secret in a heritage source.

Report: artifacts imported, artifacts rejected with reasons, Andon flags, and
your honest_flaw.
```

## 3 · Git flow (one commit per artifact, one push per generation)

```powershell
# per artifact
git add resources/heritage/gen130/<path> state/ssot/heritage_imports.jsonl
git commit -m "feat(heritage/gen130): import bb_append no-fake-green write seam - restores the symbolic truth gate"

# per generation mined, push the branch
git push -u origin HEAD

# open the PR for Sigrun / operator review-merge
gh pr create --fill --base main `
  --title "heritage: gen-130 enforcement organs" `
  --body "Per projects/heritage-mining/CODEX_HERITAGE_DISPATCH.md T1. Each artifact carries an IMPORT_RECEIPT.md with a self-computed source_sha256 and C1-C4 criteria verdicts. Anti-dirt rules section 4 honored. See state/ssot/codex_lane_return.jsonl for the lane return."
```

⚠️ **`--base main`:** the initial push landed on branch
`agent/gen133-bootstrap-20260730`. If `main` does not exist yet on the remote,
either set the default branch in GitHub settings or use
`--base agent/gen133-bootstrap-20260730`. Check with:

```powershell
gh repo view TTaoGaming/hfo-gen-133 --json defaultBranchRef -q .defaultBranchRef.name
```

## 4 · Running it as a loop

One generation per session. Do **not** chain generations in a single run — a long
run without a commit boundary is how half-imported state appears, which is the
dirt this dispatch exists to prevent.

Between sessions: `git pull` first. Another lane (or a sibling) may have pushed.
**A sibling lane was confirmed active on this host during the session that wrote
this file** — assume you are not alone.

## 5 · Honest flaw

Untested. No Codex session has run this dispatch. The prompt in §2 is written to
be short enough to survive a context reset, which also means it leans hard on the
dispatch file being read — if Codex skips §0, the anti-dirt rules do not bind it,
and nothing here enforces the reading.
