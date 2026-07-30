# Sigrun v13 opaque heritage-delta contract

The v13 family is a forward-safe successor to the exact committed v12 family.
It adds one random 128-bit opaque handle for a remotely bound Gen131 heritage-index
metadata candidate. Exact source mappings stay in a local operator ledger
outside Git. Historical bodies are never opened, decoded, or embedded.

The complete 183-record v12 public and private prefixes remain ordered and
unchanged. Public projection records contain only opaque receipt ID, NON_PUBLIC
visibility, withheld-local-ledger disposition, and BODY_PROHIBITED.

S, M, L_SAFE, and XL are deterministic. ROOT_BUNDLE.safe.json embeds exact
canonical content records for all four tiers plus the family manifest and
source-binding receipt. It is self-contained and must stay below 100,000 decimal
bytes. The preupload packet is a byte-bound HOLD packet, not an upload command.

The capsule is unratified, unsealed, T0 internal-only, and non-public. Hashes
prove bytes, not identity, continuity, authorship, rights, liveness, authority,
delivery, ConsumerAck, or publication. Wallet material, spend authorization,
transaction IDs, mutable references, and publication claims are prohibited.

One unchanged HOLD suppresses work. A future successor requires a new remotely bound
metadata delta or payload-bound FAIL. Any body access or publication requires separate
privacy, rights, independent-review, and operator gates.
