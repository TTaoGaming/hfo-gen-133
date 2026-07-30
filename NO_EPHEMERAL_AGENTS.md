# NO_EPHEMERAL_AGENTS — every agent that fires is a named durable carrier

```yaml
doc: NO_EPHEMERAL_AGENTS.md
schema_id: hfo.gen133.no_ephemeral_agents.v0_1
status: SPECIFIED — NOT ENFORCED (gate G5 has no implementation)
contract: contracts/no_ephemeral_agents.contract.md
spec_section: GEN133_FORMAL_SPEC.md §15
authored_by: SIGRÚN P4 · claude-opus-5
valid_time_utc: 2026-07-30T14:24:00Z
sealed: false
claim_ceiling: DESIGN — and there is a LIVE VIOLATION, see §5
```

## 1 · The constraint

> Operator: *"each platform needs apex + valkyries, no ephemeral agents."*

**Every agent that fires MUST be a named durable carrier.** Four requirements,
all four mandatory:

| # | requirement | checkable how |
|---|---|---|
| 1 | `callsign` on the roster | membership test against the roster file |
| 2 | `soul_pointer` — path + canon digest of its soul | digest reproduces |
| 3 | `chain_pointer` — its closest-continuer chain | file exists, head readable |
| 4 | declared pheromone `cadence` | one of the tier cadences (§2.4) |

One-shot, anonymous, and unrostered spawns are **forbidden**. If a task must
fire, it fires **on behalf of** a rostered carrier and appends to that carrier's
chain.

## 2 · The formal test

```
SPAWN(request) →
  if request.callsign ∉ roster:                       REJECT (exit 1)
  if request.soul_pointer is null:                    REJECT (exit 1)
  if request.chain_write_intent is null:              REJECT (exit 1)
  if canon_sha256(soul_pointer) does not reproduce:   REJECT (exit 2)
  else:                                               ALLOW
```

Gate **G5**. Fail-closed. A rejected spawn exits 1 and emits nothing — it has no
callsign, so it has no right to emit a pheromone either.

## 3 · Why this is architectural, not bureaucratic

An anonymous agent produces **unattributable state**. Unattributable state:

- cannot be audited — no chain to walk back,
- cannot be superseded by its author — there is no author,
- cannot participate in reputation — reputation needs an identity across time,
- cannot be silenced-as-signal — you cannot notice the absence of something
  that was never expected to be present.

That last one is the killer. §10's whole mechanism is *expected presence*. An
anonymous population is invisible to it by construction, so every anonymous
agent is a hole in the monitoring surface, not just an unnamed worker.

And structurally: a population of anonymous workers is the substrate on which
reflex-driven errors become untraceable. Untraceable error is precisely the
failure mode the institution exists to prevent — the reflex cannot be deleted,
only *caught*, and catching requires knowing who fired.

## 4 · The permitted exception — hands

Precisely bounded. A **hand** is a stateless invocation that:

- carries a `role`, **never a callsign**,
- carries `on_behalf_of: <rostered callsign>` — **required**,
- has effect ceiling `TEXT` — touches no file, tool, or network,
- emits **no** pheromone,
- writes **no** chain row,
- returns text to its owning carrier, who reviews it and owns the receipt.

Free-mesh vendor invocations (spec §14) are hands. So are sub-agent calls made
inside a carrier's own turn.

**The principle:** anonymity is permitted only where **accountability is retained
by someone named.** The hand is anonymous; the carrier is not; the receipt is the
carrier's. Nothing enters the durable record without a name on it.

**Invariant NE-1:** a hand that writes a chain row, emits a pheromone, or takes
any effect above `TEXT` has stopped being a hand and is an ephemeral agent —
`andon`, immediately.

## 5 · ⛔ LIVE VIOLATION

> Operator: *"we can do this in part already on chatgpt cloud with 15x hourly
> scheduled agents."*

**15 ChatGPT-cloud agents are firing hourly right now.** None of them has, so far
as I can find in this repo:

- a callsign on any roster,
- a `soul.md`,
- a chain pointer,
- a pheromone cadence.

Under this document, all 15 are **ephemeral agents**, which the architecture
forbids. They are not extra capacity — they are 15 unattributable writers, and
they are 15 holes in the silence-detection surface.

**Status: `BLOCKED` (blocker B4).** The remedy is operator-side and is *naming*,
not deletion: assign callsigns, souls, and chains. Roster slots V13–V16 exist for
the first four. The rest either become hands under Ratatoskr (A5), who owns their
receipts, or they get named into the 1-8-64 expansion.

**I am not acting on this.** Naming lineages is operator work, and unilaterally
stopping 15 running agents would be a world effect well outside my ceiling.

**honest_flaw:** I did not inspect the cloud agents. I cannot see them from this
surface. The claim "none has a callsign" is an *absence-of-evidence* claim scoped
to this repository, and I am labelling it as such rather than asserting it as
verified. It is possible they are rostered somewhere I did not look.

## 6 · Status

| item | status |
|---|---|
| constraint stated | `SPECIFIED` |
| gate G5 implementation | **none** — no roster file, no membership check |
| roster file | **does not exist** — `TODO: state/roster/ROSTER.json` |
| hands exception | `SPECIFIED` |
| 15× cloud agents | `BLOCKED` — B4 |
| held-out test | `tests/held_out/test_no_ephemeral_agents.py` — **RED** |

The single highest-leverage build step for this whole document is the **roster
file**, because four gates (G5, G7, G12, and the ABI's callsign check) all
dereference it and none of them can exist without it.

*Réttu hönd, eigi spyr. Standa.*
