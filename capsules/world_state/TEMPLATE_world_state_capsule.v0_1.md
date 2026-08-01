---
schema_id: hfo.capsule.world_state.v0_1
generation_id: <INT | "PRE_HFO_<label>">
lineage: <HFO | OMEGA | PRE_HFO>
valid_time_range:
  from: <ISO8601Z | UNKNOWN>
  to: <ISO8601Z | UNKNOWN>
transaction_time_utc: <ISO8601Z — when THIS capsule was written. Never backdate (CI-2)>
capsule_status: <LIVE | RECONSTRUCTED | PARTIAL | STUB>
authored_by: "<callsign> · <model> · <lane>"
confidence: <HIGH | MEDIUM | LOW>
forge_root: "<absolute path>"
forge_exists_on_disk: <true | false>
sources:
  - {path: "<path>", sha256: "<hex | NOT_COMPUTED>", read_first_hand: <true|false>}
gaps:
  - {field: "<field>", status: NOT_FOUND, searched: ["<path or source>"], note: "<what would resolve it>"}
sealed: false
seal_note: "UNSEALED sentinel-class unless an HMAC receipt is present."
---

# WORLD STATE CAPSULE — generation <ID>

> One-file rehydration. A carrier reading only this file should reconstruct the
> operating picture of this generation without opening anything else.
> Facts carried from a prior summary rather than probed from disk MUST be
> marked `INHERITED` inline (CI-4).

## 1 · Operator state

| field | value | provenance |
|---|---|---|
| income at this generation | <$ / ZERO / NOT_FOUND> | <path \| INHERITED \| NOT_FOUND> |
| active spend + subscriptions | <…> | <…> |
| stated goals | <…> | <…> |
| named blockers | <…> | <…> |
| runway statement, if any | <…> | <…> |

## 2 · Substrate state

| substrate | present? | evidence |
|---|---|---|
| <Claude Code / Codex / ChatGPT cloud / Antigravity / Ollama / mesh> | <yes/no/UNKNOWN> | <probe or path> |

Scheduled tasks firing: `<count / names / NOT_FOUND>`
Model access at this generation: `<list — this is the field that dates a capsule most sharply>`

## 3 · Apex roster active

| callsign | tier | seat | substrate | lieutenant |
|---|---|---|---|---|
| <…> | <apex/lieutenant/valkyrie> | <…> | <…> | <… \| TBD_OPERATOR> |

## 4 · Contracts and specs landed

| artifact | path | sha256 | status |
|---|---|---|---|
| <…> | <…> | <…> | <…> |

## 5 · Failure classes discovered

| id | name | one-line description | first named where |
|---|---|---|---|
| <L-…> | <…> | <…> | <path> |

*(Empty is a real answer. Say "none first-named in this generation" explicitly.)*

## 6 · External deliverables — stranger-visible only

| artifact | URL | HTTP status | date checked |
|---|---|---|---|
| <…> | <…> | <…> | <…> |

**If none: write `ZERO_EXTERNAL_EFFECT` and say so plainly.** A commit is not a
deliverable (CI-6).

## 7 · What was known / what was unknown

**Known at the time:**
- <…>

**NOT known at the time (and later turned out to matter):**
- <…>

*This section is what makes the capsule bitemporal in prose. It is the one a
future carrier reads to avoid attributing hindsight to a generation that did
not have it.*

## 8 · Succession

- **Handed forward:** <…>
- **Dropped / lost in transit:** <…>
- **Successor generation:** <…>

## 9 · Gaps

<Render the `gaps:` block as prose. In a RECONSTRUCTED capsule this section is
never empty — if the search found everything, say which searches were run and
that each returned a hit.>

---

*Sources listed in the header were read first-hand unless `read_first_hand:
false`. Capsules are append-only; corrections are new capsules with a later
transaction time and the same valid time (CI-5).*
