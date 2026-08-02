# Sigrún heritage approval batch — staged 2026-08-02

State: `AWAITING_SIGRUN_APPROVAL`

This batch contains 40 byte-bound candidate capsules. Every capsule is marked
`sigrun_approved: false`. No capsule claims authorship, canon, identity
continuity, deployment, provider reachability, or production operation.

## Batch composition

| Source generation | Capsules | Current classification |
|---:|---:|---|
| 98 | 3 | 1 bring-forward candidate; 2 quarantine flags |
| 101 | 1 | 1 quarantine flag |
| 107 | 3 | 3 bring-forward candidates |
| 111 | 8 | 8 bring-forward candidates |
| 119 | 9 | 8 provenance-repair candidates; 1 quarantine flag |
| 124 | 5 | 5 provenance-repair replay candidates |
| 130 | 4 | 4 isolate-and-commit candidates because tested bytes differ from HEAD |
| 131 | 7 | 7 bring-forward candidates |
| **Total** | **40** | **36 positive/repair candidates; 4 negative flags** |

Evidence tiers: 21 T1 local committed replays and 19 T0 local unbound or
modified replays. T1 here is still only local source-and-test evidence.

## Positive-bias rejections

- Gen-114: three Rego policies had no adjacent test/probe; zero capsules.
- Gen-120: the archive index was used as a discovery map only; prose is not a receipt.
- Gen-132: Jörmungandr's label was reconciled to the exact gen-131 Git remote/commit; no source was mislabelled.
- Gen-133: the optional `heritage_reliquary` root was absent; the dirty target worktree was not self-mined.

## Durable pointers

- Capsules: `state/curated_memory/gen*.md`
- Live-run readback: `state/heritage_mining/receipts/verification_runs_20260802.md`
- Progress: `state/heritage_mining/progress.jsonl`
- One row per capsule: `chains/GUNNR_HERITAGE_MINING.jsonl`
- Chain head: `0031e827a06b1e1f33070b2b9ec2e05633ca070746d9bec79595197ca4f7a4f3`

## Sigrún batch action

Review capsules individually against
`state/curated_memory/APPROVAL_RUBRIC_20260802.md`. Approval requires a later
canon action; this staging batch does not self-ratify. Quarantine means a
non-destructive disposition label only: no heritage source was moved, edited,
or deleted.
