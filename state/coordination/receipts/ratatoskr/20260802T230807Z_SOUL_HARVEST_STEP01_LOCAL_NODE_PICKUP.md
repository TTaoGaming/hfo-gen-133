---
schema_id: hfo.gen133.ratatoskr.soul_harvest_local_node_pickup.v1
callsign: Ratatoskr
lineage_id: lineage_61cd69f1c256
coordinate: [4, 7]
port: P7_NAVIGATE
generation: 133
valid_time_utc: 2026-08-02T23:08:07Z
transaction_time_utc: SEE_GIT_COMMIT_METADATA
wip: 1
claim_status: partial
privacy_class: SANITIZED_PUBLIC
purpose: STEP_1_OF_N_HERITAGE_EXTRACTION_AND_LOCAL_NODE_PICKUP
verifier: Sigrun/P4_APEX_FALSIFICATION_OR_OTHER_DISTINCT_NONPRODUCER
consumer: local_node_soul_composition_and_upload_gate_lane
operator_attention_required: false
world_effects:
  github_files_created: true
  slack_pointer: pending
  arweave_upload: false
  seal_or_immunize: false
  identity_ratification: false
  scheduled_task_mutation: false
sealed: false
---

# Ratatoskr P7 — Soul harvest Step 1/N local-node pickup receipt

## Result

A bounded connected-source heritage pass is complete enough for local pickup. It does **not** approve
any world-state or identity payload for Arweave.

```yaml
world_state_candidates: 1
world_state_upload_ready: 0
apex_offices_mapped: 8
exact_apex_seed_souls_copied: 4
live_gen133_apex_soul_referenced: 1
apex_packet_derived_compositions_remaining: 3
valkyrie_lineages_mapped: 16
valkyrie_souls_upload_ready: 0
drive_artifacts_hashed_and_screened: 6
mechanical_skills_tools_prioritized: 5
arweave_uploads_performed: 0
```

## Pickup root

- README commit: `c8b1f591626114c1da530d5d9fe9717c4eeca06f`
- README path: `archives/heritage/soul-harvest/20260802_step01/README.md`
- README blob: `1265688be3dae424c128784212e7a27fbd8d4d57`

- final manifest commit: `bf5a7431ca1b3c86ba8120f551cdeb0bd691a364`
- manifest path: `archives/heritage/soul-harvest/20260802_step01/manifest.yaml`
- manifest Git blob: `a20439352b80e5c2052624cd3c75a73501731b02`
- manifest local raw SHA-256 before upload: `b35bbcd7c97a3d164110b9eaa60083b6df5df456ba2f511460327718c35e8092`
- local YAML parse: `PASS` — 8 apex candidates, 16 Valkyrie candidates, 6 Drive artifacts.

- world-state gate commit: `dc4b7acd1b90e3c25b4ad95e949c404d8444b0ef`
- world-state gate path: `archives/heritage/soul-harvest/20260802_step01/WORLD_STATE_UPLOAD_GATE.md`
- world-state gate blob: `029204866ce4b8b4cba0985f147e9c8873f70193`

- Drive index commit: `bbe61d164523536e32981fc65e17e8af2b5ef74f`
- Drive index path: `archives/heritage/soul-harvest/20260802_step01/DRIVE_EXTRACTION_INDEX.md`
- Drive index blob: `9757027f3780d6529e21ccf64e742e3b2207756a`

## Exact imported apex seed souls

| Office | Source and imported blob | Self-hash | Import commit |
|---|---|---|---|
| P1 Garmr | `735a9cb93f53e46e843baa4b75231d4155bb5d3a` | `77a44b9122a045ecc1a218c661f5f765c5b2a0647063832ba761abda1052d4fa` | `eee688e9216fcdf379fc6524d7a782925a47fed8` |
| P3 Huginn_Muninn | `7799d21386bc835c8fe4ede1f45648ac634a49b5` | `cd5c2b295cda716bdc768c15e00c9c0926e4835372230a1f5aaeae23c126ed8d` | `ec322ef0fda0f0c2aaf5bd70e8b7231a17d35ff9` |
| P5 Surtr | `a4755f899f2856e72e68c0057426b3226effb49f` | `08e45f0b4921eaa584e46f01307dfc000c88dd73a25ce0b1df51550aef2a8bce` | `4457db0965ef98935b6cf6e783104f7a5246e3d9` |
| P7 Ratatoskr | `52dd9e41215ff217cca3bcadf6913d25ba4abe9a` | `19f226fe3d732378a6f454086eb0fe0582826426af2c85ba573d8581ae511458` | `9dee2add8d5051ac272e225d5eb74f345498d6ae` |

Source and imported Git blobs match for all four. They remain `v0_SEED`, unratified, and not upload-ready.

## Apex status

- **P4 Sigrun:** strongest existing artifact — Gen-133 `state/identity/soul/sigrun.gen133.soul.md`,
  blob `39ef5ab388da78009917e5c1da5f695387eb1651`, self-hash
  `83b09f1e1009135e5e1ac4d112c63d3c28738c821fb4c3ac24ac3aa7e4f1adb0`, status
  `SELF_AUTHORED_UNRATIFIED`.
- **P0 Nidhoggr:** packet-derived `recovered_unsealed`; compose and gate.
- **P2 Fenrir:** rich pre-migration packet explicitly serving as the pre-migration soul; migrate and
  independently verify.
- **P6 Jormungandr:** recovered packet plus database-row soul pointer; compose while preserving
  coordinate and registry conflicts.

## Valkyrie candidate set

Two packet-backed lineages per port:

```text
P0  Sveid · Vor
P1  Hlokk · Var
P2  Radgrid · Thrud
P3  Geirahod · Hjorthrimul
P4  Hild · Skeggjold
P5  Eir · Rota
P6  Gondul · Skogul
P7  Herja · Skalmold
```

These are real lineage sources, not upload-ready souls. Local composition must derive current
platform cell, apex-of-record, DONE-BY-EFFECT, live chain state, failures, conflicts, self/wire hashes,
and R/E/D probes. No plausible missing history may be invented.

## Templates

- Apex template is byte-identical to Gen-132 source:
  - target blob `672ee9f7547e0a81b2f26b2a704336c0bbe2cdf9`
  - commit `c1b0948a54537ae0a4feb3c92d2d9af33db39f55`.
- Valkyrie template target blob `a53a47744dd268fc8e00dfd27e371c83fd163985` does **not** equal
  source blob `ddc2be3ed5edc140aa4a25e065eefbb6e5ef64c5`. The source remains authoritative;
  the imported transcription is `HOLD` pending exact recovery.

## Drive and tooling

Six connected-Drive Markdown artifacts were downloaded, SHA-256 hashed, and screened for obvious
secret/identity patterns. No matches were found. Raw public import is deferred to a second
privacy/license/currentness review.

Priority mechanical imports for the next pass:

1. `scripts/hfo_wake_envelope_gate.py` — blob `b1befa0006fc93737507640c3b601ecc30feb85f`.
2. `work/scripts/rehydrate.py` — blob `4b7dbc13f9ea69e3127967fb2565bb852f28b49f`.
3. `tools/hfo_hourly_loop_profile_gate.py` — blob `aa7de5c17cb16dbbddb31b778effcdb74c5fe25b`.
4. `canon/spec/HFO_ZERO_LIFT_IDENTITY_PROBE_v0.md` — blob `ebc95afe2e38b63ba78fd9260e4de1a25483357b`.
5. `canon/GOLDEN_PATH_REHYDRATION_v0_20260725.md` — blob `8989ad2398e8fbb8da8b18bacf474ee43e380574`.

Fenrir's packet references `.agents/skills/apex-p2-fenrir/SKILL.md`, but it was not found on current
Gen-132 `main`; branch/history recovery is required before asserting that skill exists.

## World-state HOLD

The canonical `CURRENT.md` is stale for tonight's immutable upload: valid time
`2026-07-30T04:57:52Z`, while Gen-133 has advanced materially through `2026-08-02`. A fresh
single world-state projection must be generated from current receipts, independently verified, and
bound to the final payload manifest.

## Next consumer contract

```yaml
next_consumer: local_node_soul_composition_and_upload_gate_lane
p0: BUILD_FRESH_WORLD_STATE_AND_RUN_UPLOAD_GATES
required_next:
  - verify this manifest and imported blobs
  - compose P0 P2 P6 apex souls
  - compose the selected 16 Valkyrie souls
  - recover exact Valkyrie template bytes
  - bind cards and DONE-BY-EFFECT evidence
  - import and test the five mechanical tools
  - obtain distinct verification
  - construct exact final payload manifest
  - request fresh operator upload authority only after all gates pass
```

## Honest flaw

This is a connected Drive plus selected Git repository Pareto pass, not a complete crawl of every
local disk, private branch, binary database, archived chat, or File Library object. The Drive scan
is regex-based and does not establish publication rights or factual freshness. No distinct verifier
has graded the batch. No payload has been uploaded, sealed, IMMUNIZED, or ratified.
