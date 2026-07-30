---
schema_id: hfo.gen133.spell.v0_1
doc_kind: SPELL
spell_id: <kebab-case-id>
name: <the spell's name>
ceiling: <read | local_write | send | spend | publish | seal>
claim_status: <proposed | partial | wired_with_receipts | failed | superseded>
first_proven_gen: <n | null>
sealed: false
---

# <NAME>

## Incantation

<!-- The exact invocable text or command, verbatim and reproducible. -->

```
<incantation>
```

## Effect

<!-- What changes in the world. Concrete. "Improves clarity" is not an effect;
     "writes one hash-linked row to chains/X.jsonl and returns its row_sha256"
     is an effect. -->

## Witness (held-out)

<!-- The check that PROVES the effect. An exit code, a diff, a byte count, a
     fetched status. NOT a claim, NOT a static read. Static PASS ≠ runtime PASS
     (L_DESCRIPTOR_GREEN_IS_NOT_RUNTIME_GREEN). -->

| check | command | expected | last observed |
|---|---|---|---|
| | | | |

**No witness → `claim_status: proposed` → does not count in the spellbook index.**

## Ceiling

<!-- Which world-effect tier. If it is send / spend / publish / seal, name the
     gate that must fire first and who must type the authorization. -->

## Refusal

<!-- What this spell must decline, and the named failure vector it guards. -->

## Provenance

| field | value |
|---|---|
| origin | |
| first proven | |
| superseded by | |
| authored by | |

*Réttu hönd, eigi spyr. Standa.*
