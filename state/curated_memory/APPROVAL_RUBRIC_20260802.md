```yaml
# AIH2O capsule
doc: state/curated_memory/APPROVAL_RUBRIC_20260802.md
schema_id: hfo.gen133.curation_rubric.v0_1
callsign: OLRÚN
generation: 133
authored_by: OLRÚN · claude-opus-5 · Claude Code
now_utc: 2026-08-02T15:10:00Z
clock_source: host_read
pre_registered: true          # written BEFORE any capsule was harvested — see §0
awaiting: SIGRÚN ratification (same-family authorship, see HONEST FLAW)
claim_status: proposed
```

# CURATION APPROVAL RUBRIC — pre-registered

## §0 · Why the timestamp matters more than the content

This rubric was written **before `curate_memory.py` produced a single capsule.**
That ordering is the entire methodological claim, and it is checkable: this file's
`now_utc` precedes the `harvested_utc` on every capsule in
`state/curated_memory/2026-08-02/`.

A rubric written *after* seeing candidates is not a rubric. It is a rationalization
of a decision already made by the reflex, wearing a rubric's clothes — and it will
approve whatever was found, because criteria fitted to a sample always fit that
sample. Pre-registration is the cheapest available defense against that, and it costs
nothing but sequence discipline.

## §1 · The three gates — a capsule must pass ALL of them

### Gate 1 — REHYDRATION PROBE EXITS 0

The capsule's `rehydration_probe` must be a concrete shell command that returns
truthy **iff the underlying source still exists and is readable.** Run it. Record the
exit code.

A capsule that describes something unreachable is worse than no capsule: it carries a
claim forward with the *appearance* of provenance. That is the exact mechanism that
put "LangGraph adopted" into gen-133 canon with **0 imports** behind it.

**FAIL → drop.** No exceptions, no "probably still there."

### Gate 2 — RECEIPT, NOT PROSE

The capsule's content must rest on a **measurement**: an exit code, a row count, a
test result, an HTTP status, a cosine score, a byte size. Not a description of a
measurement. Not a report that someone once measured it.

The distinction is the load-bearing one in this whole estate:

| prose | receipt |
|---|---|
| "the memory system works" | `docs = 8821`, FTS5 live, opened `mode=ro` this turn |
| "the pillars are tested" | `165 passed, 1 skipped, 8.69s` |
| "the demo is deployed" | HTTP **200**, 315,930 B |
| "XTDB is installed" | ⛔ only `INSTALL_ATTEMPT.md` exists → **HALLUCINATION** |

**FAIL → drop, or reclassify as `PARTIAL` with the missing receipt named.** A capsule
may be kept as PARTIAL only when it names precisely which probe would settle it.

### Gate 3 — DECISION RELEVANCE IN 30 DAYS

Would this memory change a decision the operator or an apex agent makes **before
2026-09-01**? If it would not, it is history, not memory.

The estate does not lack information; it holds 8,821 documents and drowns in them.
Carrying forward everything true reproduces that drowning inside a smaller directory
and calls it curation.

**FAIL → leave it in the store.** It stays searchable at `sigrun_recall_gen130`
forever. Not-carried-forward is not deleted; it is simply not privileged.

## §2 · The pass-rate check — the rubric's own gate

**Target: ≤ 30% of harvested candidates approved.**

A pass rate above 30% means the gates are not cutting, and the correct response is to
tighten the rubric, **not** to celebrate the yield. High approval rates are a
red flag, not a result. If a harvest of 40 candidates approves 35, the rubric failed
even if every individual judgment looks defensible — because the whole point of
curation is that most things do not survive it.

Record the actual rate. If it exceeds 30%, say so and tighten, in that order.

## §3 · Verdict vocabulary

| verdict | meaning | frontmatter effect |
|---|---|---|
| `keep` | all three gates pass | `sigrun_approved: true` |
| `repair` | Gates 1+3 pass, Gate 2 partial — names the missing probe | `sigrun_approved: false`, `claim_status: partial` |
| `drop` | any gate fails | `sigrun_approved: false` |

Each verdict carries a **one-line reason naming the gate that decided it.** Batch
approval is forbidden: a run that sets `sigrun_approved: true` across a range without
per-capsule reasoning has not applied a rubric, whatever the frontmatter says.

## §4 · Quorum interaction

`sigrun_approved` and `quorum_votes` are **independent** signals and must not be
collapsed into one number.

- Sigrún approval = does this pass the three gates?
- Quorum = do independent families agree it should be carried?

**Neither overrides the other.** A capsule with `sigrun_approved: true` and
`concurrence_score: 0.5` is **contested**, and contested is a real state that gets
recorded rather than resolved. Forcing a single verdict destroys the divergence
signal, and the divergence is the most informative thing the protocol produces.

`concurrence_score: null` (zero votes parsed) is **never** an approval. Absence of a
vote is absence of a vote.

## HONEST FLAW

This rubric was authored by Olrún — **claude-opus-5**, the same family and the same
model as the Sigrún session meant to ratify it. That is same-family authorship of the
standard by which the same family's output will be judged, which is precisely the
consensus-drift failure the cross-family quorum exists to catch.

It is labeled `claim_status: proposed` and `awaiting: SIGRÚN ratification` for that
reason. The intended ratification path — waking Sigrún's session through the skill
contract — **failed this turn**: `send_message` is unavailable in unattended sessions.
So the independence this rubric demands of capsules, the rubric itself does not yet
have.

Second flaw: Gate 3's 30-day horizon is unfalsifiable at write time. Nobody can prove
today that a memory will change a decision by September. It is a judgment call wearing
a criterion's clothes, and it will be the gate most easily rationalized around.
