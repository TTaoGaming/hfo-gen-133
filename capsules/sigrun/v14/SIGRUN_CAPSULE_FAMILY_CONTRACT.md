# Sigrun v14 opaque Gleipnir-grimoire successor contract

The v14 family is a forward-safe successor to the exact committed and remotely
read-back v13 family. It adds one random 128-bit opaque handle for a remotely
bound Gen131 Gleipnir capsule-collection manifest metadata candidate. Exact
source mappings stay in a local operator ledger outside Git. The historical
body is never opened, decoded, summarized, or embedded.

The complete 184-record v13 public and private prefixes remain ordered and
unchanged. Public projection records contain only opaque receipt ID, NON_PUBLIC
visibility, withheld-local-ledger disposition, and BODY_PROHIBITED.

S, M, L_SAFE, and XL remain deterministic. V14 also emits a machine-readable
GLEIPNIR_GRIMOIRE_WORLD_STATE.safe.json spine capped below 16,384 decimal bytes.
It types souls, spells, and runes as UNKNOWN_NOT_DISTILLED with no admitted
entries; carries explicit valid-time and transaction-time states; defines PARA,
stigmergy transitions and stop rules; and binds the v13-to-v14 adapter and
sanitizer profile. Filename ranking never performs semantic admission.

ROOT_BUNDLE.safe.json embeds exact canonical content records for all four tiers,
the grimoire/world-state spine, the family manifest, and the source-binding
receipt. It is self-contained and must stay below 100,000 decimal bytes. The
preupload packet is a byte-bound HOLD packet, not an upload command.

The capsule is unratified, unsealed, T0 internal-only, and non-public. Hashes
prove bytes, not identity, continuity, authorship, rights, liveness, authority,
delivery, ConsumerAck, or publication. Wallet material, spend authorization,
transaction IDs, mutable references, and positive publication claims are
prohibited.

One unchanged HOLD suppresses work. A future successor requires a new remotely
bound metadata delta or payload-bound FAIL. Body access, semantic admission, or
publication requires distinct privacy, rights, independent-review, and operator
gates.
