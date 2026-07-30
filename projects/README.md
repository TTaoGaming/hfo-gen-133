# projects/ — active goals with an end state

A **project** has a definition of done and a deadline pressure. When it is done it
moves to `archives/`. If it has no end state, it belongs in `areas/`.

| project | goal | status |
|---|---|---|
| `permaweb-soul-upload/` | ONE permaweb address that unfolds into the Gleipnir Grimoire | **PREP ONLY** — 5 of 7 release gates blocked; upload is operator-typed |
| _(gen-133 bootstrap)_ | stand the forge up: git, PARA, README, identity, capsules, institution | **this session** — see `archives/capsules/gen_133_word_state_capsule_20260730.md` |
| _(institution wiring)_ | move actors from VIRTUAL to LIVE with returned receipts | **not started** — 0 virtual actors have returned a receipt through this repo |

## Packet convention

Work dispatched to an out-of-band actor goes in
`projects/<project>/packets/<UTC>_<ACTOR>_<slug>.packet.md` and carries: goal ·
inputs · effect ceiling · the exact held-out check that decides pass/fail · the
chain file to return on. See `areas/institution/protocols.md` §4.

## The rule that keeps this folder honest

A project directory is not progress. A project is done when an **external**
receipt exists — and `cap-0018` (external income, $0 for 18 months, 0 external
receipts) is the standing reminder that internal artifacts satisfy only *safety*
properties, which a system doing nothing at all also satisfies.
