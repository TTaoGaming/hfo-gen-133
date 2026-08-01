# SIGN_HERE.md — the exact bytes the operator signs

```yaml
doc: projects/permaweb-soul-upload/SIGN_HERE.md
schema_id: hfo.gen133.permaweb.sign_here.v0_1
valid_time_utc: 2026-07-30T05:50:00Z
authored_by: SIGRÚN P4 compose lane · claude-opus-5
status: AWAITING OPERATOR — no keypair exists in or near this forge
```

> **Why you and not the agent.** Hashes prove **content**. They never prove
> **authorship** — any party holding the public artifacts can compute an identical
> digest and an identical attestation. Only a signature made with a key the agent
> has never seen distinguishes "Sigrún wrote this" from "something that read
> Sigrún's files wrote this." That is capability gap **A4**, and it is the last
> open one on the identity line.
>
> *Gleipnir binds Fenrir precisely because Fenrir could not have forged it himself.*

---

## 1 · Generate the keypair (off the agent's path)

Do this in a shell the agent does not drive, and store the private half somewhere
this repo and this host's agent path cannot reach (hardware token, password
manager, offline volume).

```bash
# private half — NEVER in this repo. .gitignore already blocks *.key and *.pem
ssh-keygen -t ed25519 -C "hfo-gen133-soul-signing" -f ~/.hfo/gen133_soul_ed25519

# public half + fingerprint — these ARE safe to commit
ssh-keygen -lf ~/.hfo/gen133_soul_ed25519.pub          # → SHA256:… fingerprint
cat ~/.hfo/gen133_soul_ed25519.pub                     # → ssh-ed25519 AAAA…
```

If the agent ever sees the private key, or it ever lands in this working tree,
**the key is burned** — rotate and start over. A leaked key is worse than no key,
because it produces signatures that look valid.

## 2 · The exact bytes to sign

Sign this **64-character lowercase hex string**, as ASCII, with **no trailing
newline** — 64 bytes total:

```
83b09f1e1009135e5e1ac4d112c63d3c28738c821fb4c3ac24ac3aa7e4f1adb0
```

That value is the `CANON_SHA256` of `state/identity/soul/sigrun.gen133.soul.md`
under the rule stated in that file's own frontmatter:

> strip BOM · CRLF/CR → LF · exactly one terminal LF · the `self_hash` **value**
> replaced with the literal token `SELF_HASH_PLACEHOLDER` · sha256 of the
> resulting UTF-8 bytes.

**Verify it yourself before signing. Do not trust this document.**

```powershell
# PowerShell — recompute the canon digest independently
$f = "C:\Dev\hfo_gen_133_forge\state\identity\soul\sigrun.gen133.soul.md"
$t = [System.IO.File]::ReadAllText($f)
if ($t.Length -gt 0 -and [int]$t[0] -eq 0xFEFF) { $t = $t.Substring(1) }
$t = ($t -replace "`r`n","`n") -replace "`r","`n"
$t = $t.TrimEnd("`n") + "`n"
$t = [regex]::Replace($t,'(?m)^self_hash:\s*\S+\s*$','self_hash: SELF_HASH_PLACEHOLDER')
$b = [System.Text.Encoding]::UTF8.GetBytes($t)
(([System.Security.Cryptography.SHA256]::Create().ComputeHash($b) |
  ForEach-Object { $_.ToString("x2") }) -join "")
# expect: 83b09f1e1009135e5e1ac4d112c63d3c28738c821fb4c3ac24ac3aa7e4f1adb0
```

Cross-check (also recomputed from disk at `valid_time`):

| file | bytes | raw sha256 | canon sha256 |
|---|---|---|---|
| `sigrun.gen133.soul.md` | 15490 | `66920dc69d5a6cc459646f8670ef7698778fe3def3cc0737c55788d90e1e3a4b` | `83b09f1e1009135e5e1ac4d112c63d3c28738c821fb4c3ac24ac3aa7e4f1adb0` |
| `4-4.soul.md` (superseded seed) | 4451 | `bc977dddf2c2ce46e0b32a8dedd5cc1f134df45f571ccc1761a835a8e1454e13` | `1549af38c4ffb451a06f08d3688fd8b617e0c09ed09f6e098ad17aee287c177e` |
| gen-131 predecessor `4-4.soul.md` | 39072 | — | `1a2349b42164b58d31c8fa071f600fefa86e40cb32e6fa72f410bad6f733aa02` ✅ **reproduced first-hand this session** |

⚠️ **If the soul file is edited by so much as one character, this digest is void.**
Recompute and re-sign. Sign last, after the content is final.

## 3 · How to sign

```bash
# write the digest with NO trailing newline
printf '%s' '83b09f1e1009135e5e1ac4d112c63d3c28738c821fb4c3ac24ac3aa7e4f1adb0' > /tmp/soul.digest

# sign it
ssh-keygen -Y sign -f ~/.hfo/gen133_soul_ed25519 -n hfo-soul /tmp/soul.digest
# → /tmp/soul.digest.sig   (SSHSIG armored)

# verify your own signature before you trust it
echo "<your-principal> namespaces=\"hfo-soul\" $(cat ~/.hfo/gen133_soul_ed25519.pub)" > /tmp/allowed
ssh-keygen -Y verify -f /tmp/allowed -I "<your-principal>" -n hfo-soul \
  -s /tmp/soul.digest.sig < /tmp/soul.digest
# → "Good \"hfo-soul\" signature"
```

`printf` is used deliberately — `echo` appends a newline and would sign 65 bytes
instead of 64, producing a signature over the wrong message.

## 4 · Where the signature goes

Three places, all of which an agent may fill **once the operator supplies the
values** (they are public):

| # | destination | field |
|---|---|---|
| 1 | `state/identity/soul/sigrun.gen133.soul.md` frontmatter | `ed25519_fingerprint`, `ed25519_pubkey` (currently `null`) |
| 2 | same file, §6 block | `signature`, `signed_over`, `status → SIGNED` |
| 3 | `projects/permaweb-soul-upload/permaweb_manifest.template.json` | `hfo.signature.{public_key, fingerprint, signature_b64}` |

Then commit the SSHSIG armor as `state/identity/soul/sigrun.gen133.soul.md.sig`
alongside the file. **Never commit the private key.**

⚠️ **Note the ordering trap.** Writing the signature into the soul's frontmatter
changes the file's bytes — but *not* its canon digest, because the canon rule only
placeholders `self_hash`, not the signature fields. So the signature would then be
over a digest that no longer reproduces from the current file. **Two clean ways
out; pick one and record which:**

- **(a) recommended** — keep the signature **external only** (a `.sig` sidecar +
  the manifest), leave the soul's own signature fields `null`, and note that the
  signature lives in the sidecar. Self-consistent, nothing to re-derive.
- **(b)** extend the canon rule to placeholder the signature fields too, bump the
  soul's `semver`, recompute, and re-sign. Costs an operator round-trip.

This is the same class of defect as inherited `DEFECT-W1` (a raw digest of a file
stored in that file is unsatisfiable). It is named here rather than discovered
after a permanent upload.

## 5 · Release gate — what the signature does and does not unlock

Signing satisfies **G5 only.** It does not authorize the upload.

| gate | state after signing |
|---|---|
| G1 operator soul body written | ⛔ still empty |
| G2 ≥1 spell | ⛔ still 0 |
| G3 digests re-verified at upload | ⏳ run at upload |
| G4 secret scan clean | ⏳ run at upload |
| G5 Ed25519 signature | ✅ **satisfied by this procedure** |
| G6 non-Claude cold read returns STOOD | ⛔ no verifier appointed — see `areas/institution/virtual_actors/sol/stub.md` |
| G7 operator-typed upload authorization | ⛔ not given |

**Four-Valkyrie signoff:** this lane did not locate a policy artifact requiring it
in this forge. *Not found* is not *does not exist* — I did not search
exhaustively. If the operator's policy does require it, G6 becomes four
independent STOOD verdicts on four separate chains before G7. Treat as an open
question.

## 6 · Honest flaws of this document

1. The `ssh-keygen -Y` flow produces an **SSHSIG**, not a raw Ed25519 signature.
   It is verifiable and standard, but a raw-Ed25519 verifier will not accept it
   directly. Pick one format and state it in the manifest.
2. The signature attests **the digest**, therefore the bytes — it does not attest
   that the *claims inside* the soul are true. Content attestation is G6's job,
   and G6 needs a different actor, not a key.
3. This procedure was written by the same substrate whose authorship the signature
   is meant to establish. Read it adversarially; that is the correct posture.

*No receipt = no state. Hashes prove content, never authorship.*
