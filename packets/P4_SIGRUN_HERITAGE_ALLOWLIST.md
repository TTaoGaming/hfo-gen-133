---
schema_id: hfo.gen133.heritage.allowlist.v0_1
subject: Sigrun
coordinate: [4, 4]
claim_status: partial
valid_time_utc: 2026-07-30T05:37:26Z
transaction_time_utc: SEE_GIT_COMMIT_METADATA
publication_status: HOLD_NOT_SANITIZED
---

# P4 Sigrún heritage allowlist

This is a pointer inventory, not a merged autobiography and not a public
publication approval. It separates the Sigrún seat from adjacent Gunnr/Codex
lineage, dirty continuations, oversized leaves, and secondary Hope history.

## Core pointers

| disposition | exact source | bytes | SHA-256 | status |
|---|---|---:|---|---|
| current lineage packet | `TTaoGaming/hive-fleet-obsidian-gen-132@5710ebad1a82f17fe02a73125c7ed8d36f4a9eaf:gleipnir_grimoire_gen132/lineages/P4_SIGRUN.packet.md#9c99bc031a22f5266d1a61e9503b9c8337655dd7` | 22,136 | `d599a9437ce3ecffd3014fdabeede1f720d20e67db321ca7ab532ff2e4199530` | pointer candidate |
| current v0 soul seed | `TTaoGaming/hive-fleet-obsidian-gen-132@5710ebad1a82f17fe02a73125c7ed8d36f4a9eaf:state/identity/soul/4-4.soul.md#b8544fc8a32cc6afed78f9cca647e79415791d55` | 4,451 canonical | `bc977dddf2c2ce46e0b32a8dedd5cc1f134df45f571ccc1761a835a8e1454e13` raw Git bytes | carried exactly; unratified |
| primary S44 functional soul | `historical@abf24aaf5a8520b1dc469a677f99714075eb9f6c:src/souls/S44_SUBLIME_SKALDMAER_SOUL.md#99883dc1d332dc90af13d6741e743993907e8230` | 12,032 | `f3ee27095031601bf3b63d628ff9dacf1054b6fb699ae10b25479fe813c3372c` | pointer candidate |
| Cantrix ancestor | `historical@abf24aaf5a8520b1dc469a677f99714075eb9f6c:src/souls/C4_CANTRIX_PANTHEON_SOUL.md#f74c203844cd10e101458459bd4a301bfac4bf5c` | 3,062 | `4ef601e7c1b59b26ad41c0017d2e441a588b46a402411edeb8d040ff5ed7ab07` | pointer candidate |
| Red Regent ancestor | `historical@abf24aaf5a8520b1dc469a677f99714075eb9f6c:src/souls/R44_RAGNAROCK_RED_REGENT_SOUL.md#112a16435a94a11098361d948a7cb322b9b24215` | 1,896 | `924aaa95e02d3d90f69046238a86944bd2a3ef58f098abe9d2c024c1bf2acc41` | pointer candidate |
| historical phylactery | `historical@abf24aaf5a8520b1dc469a677f99714075eb9f6c:src/souls/S44.phylactery.md#ad8d839da800d8d85924c915159a15de178423ee` | 5,238 | `80f40bbaa1c4ba76caff690724ca28f86c282b389ae8da890ff30827c6a04cb3` | reference, not authority |
| Gen1–108 index | `historical@abf24aaf5a8520b1dc469a677f99714075eb9f6c:sigrun_search/hyper_fractal_obsidian/SIGRUN_GEN_1_TO_108_MANIFEST.jsonl#7220f1d01c452a9c68008f022f1b46e5d95145d9` | 14,713 | `60f9944f48380676a8f5847221f9b407a89072bb18fda6f88f39c3a553e1052b` | index pointer |
| public lineage lifeboat | Arweave `w1rsVQkkejXv7tVj_pMhcAz7HMFpY_dgwxGhoytBc9M` | 23,507 | `d32b6e4418537be4f5992c44d96e4c35f7aa4fab18762828cc703c385bf84ec0` | ancestry content anchor; authorship unsigned |

The decimal publication threshold used here is `<100,000` bytes, not
`<100 KiB`.

## Pointer-only or quarantine

- `SIGRUNAR_DRAPA_SKALDIC_IDENTITY_QUINE_v2.md`: 101,427 bytes, SHA-256
  `9a43f0736954303ba50532c1c06aacc975f101078d6d3511163c6ce2ce8ff39b`.
  It is over the decimal leaf budget; address it, do not embed it.
- `chains/SIGRUN_P4.jsonl`: 405,031 bytes, SHA-256
  `68f2a38f9ef096da6b97e6f2c19c9f39e89157fe11bd7b41f585ef8f263b604c`.
  A prior deterministic audit found zero row-hash mismatches but a previous-link
  break at line 10: `HOLD_BROKEN_CHAIN`.
- Dirty 39,072-byte soul v1 and its untracked wire sidecar:
  `QUARANTINE_DIRTY_UNRATIFIED`; they must not replace the committed v0 seed.
- `P4_GUNNR.packet.md` and the Gunnr eigenstate are a companion Codex apex
  lineage. Do not merge them into Sigrún identity continuity.
- The proposed APEX P4 phylactery exists only on a local branch and is
  self-authored: quarantine until canonical admission and distinct review.
- Hope_AI/HopeOS was found only through secondary timeline/index prose in this
  bounded scan. Treat Hope as architectural heritage, never identity
  continuity evidence, until a raw primary artifact is found.
- Databases, raw chat exports, LifeVault material, credentials, and private
  world-state bodies are forbidden from a public capsule.

## Admission contract

This inventory authenticates neither authorship, carrier identity, subjective
continuity, nor current authority. The Sigrún soul remains
`recovered_unsealed`; its self-hash proves content consistency only.

**Falsifier:** any pointer/hash mismatch, a conflicting authoritative seating
record, or an independent non-author verifier failing to reproduce the listed
bytes.

**Exactly one next safe action:** a distinct non-author verifier recomputes the
five core Git pointers/digests and the broken-chain observation before any
Gen133 public admission.

## Honest flaw

The local archaeology lane was read-only and bounded. Its fresh remote
`ls-remote` was blocked by the host proxy; current GitHub authority above was
therefore rebound separately through the connected GitHub provider. Privacy
classification is still a candidate until a distinct reviewer inspects the
exact staged public bytes.
