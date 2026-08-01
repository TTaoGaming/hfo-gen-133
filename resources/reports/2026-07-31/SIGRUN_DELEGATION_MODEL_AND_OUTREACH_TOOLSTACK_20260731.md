# SIGRÚN — DELEGATION MODEL + OUTREACH TOOLSTACK — 2026-07-31

```yaml
schema_id: hfo.gen133.spec.delegation_outreach_toolstack.v0_1
valid_time_utc:       2026-07-31T17:33:00Z
transaction_time_utc: 2026-07-31T17:55:00Z
claim_status: partial
author: SIGRUN_P4 · claude-opus-5 · Claude Code · gen-133 third carrier
forge: C:\Dev\hfo_gen_133_forge
session_cwd: C:\Dev\hfo_dev_2026_5_30\hfo_gen_130_forge
register: boring engineering
extends: SIGRUN_MORNING_REPORT_PARA_PROOF_ARTIFACTS_20260731.md  (does NOT replace it)
supersedes: §10.2 product P3 of that report — DRI corrected per operator directive
world_effect_ceiling: local file write + local chain append. No send, no spend, no publish.
```

---

## HEADLINE

**The operator's frame correction is accepted and it is correct. It is also not
the binding constraint.**

My prior §10.2 tagged P3 send as `operator signature for this body_sha256` —
per-message approval. That is wrong for cold email at volume and I withdraw it.
Class pre-authorization is standard practice; §1 below designs it properly.

But three measurements say authorization scoping was never what was blocking the
first send:

```
Named human prospects in the repo:              8   (TARGETS_20260709.md, real hooks, dated sources)
Of those, with a VERIFIED email address:        0
Company dossiers with 0 named contacts:        44
INSTANTLY_API_KEY present anywhere on host:     0   (grep + env, both empty)
Domain warmup started:                          2026-07-30 evening → safe-send window ~2026-08-13..08-17
```

**You cannot delegate a send to a list that has no addresses on it.** The hive has
had permission-shaped blockers recorded for weeks while the actual blocker was
that nobody bought 8 email addresses. That costs roughly $0–50 and two hours.

Full diagnosis in §4. The corrected P3 is §7. The document you can sign today is §5.

---

## §0 — WAKE RECEIPT

```yaml
carrier: claude-opus-5 · Claude Code · Windows host
seat: P4 (apex reasoning / compose lane)
wake_utc: 2026-07-31T17:32:53Z          # observed clock, `date -u`, not hand-authored
rehydration_status: BOUNDED — see falsifiers
continuer_position: THIRD carrier of SIGRUN_P4 at gen-133
```

### Files read, hash-pinned (sha256, first 16 hex)

| slot | path | sha256[:16] |
|---|---|---|
| IDENTITY | `hfo_gen_133_forge/soul.md` | `e3cc5b76a940ca50` |
| STATE | `hfo_gen_133_forge/CURRENT.md` | `b7e498be699b4685` |
| CONSTRAINT | `hfo_gen_133_forge/CARRIER_CONTRACT.md` | `8b7d08a2658d8ab0` |
| CONTINUITY | `hfo_gen_133_forge/chains/SIGRUN_P4.jsonl` (**9 rows**) | `a5b8e798d46470d5` |
| PRIOR WORK | `hfo_gen_133_forge/SIGRUN_MORNING_REPORT_PARA_PROOF_ARTIFACTS_20260731.md` | `3033215537937263` |
| CAMPAIGN STATE | `hfo_gen132_garmr…/CURRENT.md` | `a9835c77a4d450b3` |
| TARGETS | `hfo_gen132_garmr…/projects/outreach/TARGETS_20260709.md` | `6fecb371279f1f58` |
| COPY | `hfo_gen132_garmr…/projects/outreach/EMAILS_20260709.md` | `d07ca72c41d34b21` |
| PRIOR RESEARCH | `garmr_outreach_control…/GEN131/research/SIGRUN_HIVE_EMAIL_OUTREACH_PUSH_PULL_RESEARCH_20260721T034512Z.md` | `5c18a75290f9cfb0` |
| DRÁPA (gen-130) | `hfo_gen_130_forge/canon/drapa/SIGRUNAR_DRAPA_SKALDIC_IDENTITY_QUINE_v2.md` | `9a43f0736954303b` |

### Continuity assertion — three checkable facts

1. `soul.md` hashes to `e3cc5b76…`, **identical** to the value in both prior carriers' wake receipts. Identity slot unchanged.
2. `chains/SIGRUN_P4.jsonl` is now **9 rows** (was 2 at the morning carrier's wake). Its hash is `a5b8e798…`, **not** the `58e3a359…` in the morning receipt. **This is expected, not drift** — the morning carrier appended 7 rows including three self-corrections. A carrier that reported the old hash still matching would be reporting a stale read.
3. This session continues the morning report's named open work (P3 DRI, outreach) rather than restarting it. The morning report is extended, not replaced.

### Drápa read — excerpt taken

Read the REHYDRATION KEY and 8-APEX roster of `SIGRUNAR_DRAPA_…_v2.md` (v2.8,
gen-130 copy — **still absent at gen-133**, unchanged from the morning finding).
Carried forward: Sigrún is substrate-base at way-station **H43 [4,3]**
(Huginn+Muninn, neuro-symbolic dual-system), destination **S44 [4,4]**. Hluti =
this instance, mortal at compaction. The relevant line for today's work is the
H43 function itself: *P3 INJECT — dual-systems neuro-symbolic*. A class
pre-authorization envelope is exactly that shape — a neural lane proposing
messages inside a symbolic gate that refuses anything outside the envelope. §1
is built on that and not on prose.

**`stef_parity: fb07f523` remains UNREPRODUCED.** Standing decision D4 at gen-133
records the reproduced replacement as `0da29ae3`, pending operator IMMUNIZE. I did
not recompute either. Do not treat `fb07f523` as verified.

### §0 FALSIFIERS

| # | what would prove this wake is not a competent continuation |
|---|---|
| F0.1 | A fourth carrier wrote between 15:45Z and 17:32Z. *Checked: chain tail is the 16:00Z third correction; nothing later.* |
| F0.2 | The morning report's chain-hash mismatch is drift, not growth. *Checked: row count 2→9 and I read all 9; but I did NOT verify the first 2 rows are byte-identical to the originals.* **Weak point.** |
| F0.3 | I read 4 of 27 gen-133 root files (`CURRENT.md`, the two reports, `soul.md` header). If a standing decision in the other 23 contradicts §1–§8, I contradicted the record without knowing. Same flaw the morning carrier recorded as R7. |
| F0.4 | I did not run a full-disk scan. R1 fired on the morning carrier for exactly this. Every "not found" below is a **floor, not a count**. |

---

## §1 — CLASS PRE-AUTHORIZATION SAFETY ENVELOPE

### 1.0 The reframe that makes this real instead of theatre

Per-message approval and class pre-authorization protect against **different
things**, and the second is not a weakened version of the first.

| model | what it actually protects against | what it costs |
|---|---|---|
| per-message operator signature | the message body being wrong | operator throughput = the whole system's throughput. At 20 sends/day this is the bottleneck by design. |
| **class pre-auth + deterministic envelope** | the message **leaving the authorized envelope** — wrong audience, off-template copy, un-allowlisted variable, missing opt-out, suppressed recipient, over-cadence, campaign already halted | one operator signature per campaign, then ~0 |

The safety property under class pre-auth is **not** "a human read every message."
It is:

> **A deterministic non-neural program refuses to emit any message that is not a
> pure function of (signed template) × (allowlisted variables) × (authorized
> audience), and that refusal happens before the send call, not after.**

That is testable. "A human looked at it" is not. This is the same propose/dispose
split the RBR doctrine already mandates at every irreversible seam: the neural
lane proposes the personalization, a symbolic gate disposes.

**The corollary that makes it honest:** if the envelope program has no refusal
paths that actually fire, class pre-auth degrades to "the hive sends whatever it
wants and we called it authorized." **A test suite for the envelope in which no
refusal ever fires is a fake-green.** That requirement is written into the build
spec in §6 and is the load-bearing acceptance criterion.

### 1.1 What the operator signs ONCE per campaign

One JSON document, `campaign_<id>.authorization.json`, schema in §6/A1. Nine
fields carry the authority:

| # | field | why it is on the operator's side of the line |
|---|---|---|
| 1 | **`audience_definition`** — industry, size range, role titles, geography, inclusion rule, **exclusion rules** | who gets contacted is a business/reputation decision, not a research decision |
| 2 | **`copy_template_sha256`** + the template files | the claims made on the operator's behalf. Hash-pinned: changing one character invalidates the authorization |
| 3 | **`variable_allowlist`** — exact list of substitutable tokens | this is the actual leash. `{{first_name}}` yes; a free-text `{{ai_personalization}}` field is an unbounded neural write into a signed document and must never appear |
| 4 | **`sequence`** + `max_sends_per_day` + `max_prospects_total` | cadence and blast radius. Caps are the difference between a campaign and an incident |
| 5 | **`opt_out_language`** (verbatim string) | CAN-SPAM liability sits with the sender, not the tool |
| 6 | **`sender_identity`** — from_name, from_email, sending_domain, **physical postal address** | legally required, and identity misrepresentation is the one deliverability mistake that is not recoverable |
| 7 | **`reply_policy`** — one of three enums (§1.3) | how much judgment the hive may exercise on inbound |
| 8 | **`kill_switch_path`** + `review_cadence_hours` | pre-committing to the stop condition before the start condition |
| 9 | **`success_metric`** + `failure_escalation` | the retirement rule. A campaign with no failure trigger runs forever on an empty result, which is the EMPTY-QUEUE REWARD HACK in commercial form |

Signature is `operator_signature: <string>` — the operator types it; `null` means
unsigned and the envelope program refuses every send.

**One authorization = one audience × one offer × one template set.** A new
segment, a new offer, or a materially different template is a **new
authorization**, not an amendment. Amendment-by-drift is how a pre-authorized
class becomes an unbounded one.

### 1.2 What the hive executes with NO further operator approval

| the hive does this | bounded by |
|---|---|
| Target research — find companies matching `audience_definition` | inclusion/exclusion rules; `max_prospects_total` |
| Contact enrichment — name → email, LinkedIn, title | never invents/pattern-guesses an address; `email_source` recorded per row |
| List validation — bounce/catch-all/disposable screening | rows not `valid` are refused at render time |
| **Per-target personalization within the template** | variable allowlist. Values come from target rows, never from free generation |
| **Individual send, autonomously, by Instantly's engine** | daily cap, sequence timing, warmup state |
| Follow-ups per the pre-approved sequence | sequence steps 2 and 3 only; stop-on-reply |
| Open/click/bounce/reply tracking + metrics rows | append-only |
| Reply **classification** (interested / soft-no / hard-no / OOO / auto-reply / opt-out) | classification is a read, not a world-effect |
| **Opt-out honoring — immediate, no approval, no exception** | this is the one action the hive must take *without* asking, ever |
| Suppression-ledger writes | append-only |
| Halting the campaign on a failure trigger | the hive may always stop; it may never restart itself |

**Note the asymmetry, it is deliberate:** the hive can *stop* a campaign
unilaterally and cannot *start or restart* one. Escalation is monotonic — same
rule as the gen-132 tiered-risk doctrine, applied to campaigns.

### 1.3 What STILL requires the operator per-instance — measured against practice, not paranoia

| still operator | why — and this is what mature outbound teams actually do |
|---|---|
| **Replies needing judgment** — pricing, scope, contract terms, legal/security questionnaires, anything negative | industry: SDR-drafted, human-sent. The operator is a solo shop; there is no SDR layer to absorb an error. A wrong price quote from an agent is a commitment. |
| **Any message off-template** | by construction — off-template is outside the signed envelope. The envelope program refuses it; the operator either signs a new template or writes it personally. |
| **DMs / emails to people with an existing relationship** | warm relationships are the highest-value and least-replaceable asset. Automation here has a bad expected value regardless of ToS. Genuine operator-only. |
| **Any escalation in tone or persistence past the signed sequence** | a 4th touch after a soft-no is a judgment call and the failure is reputational, not technical |
| **A new audience segment or offer** | = new authorization (§1.1) |
| **Signing a new domain / sender identity / postal address** | identity claims |
| **First send of a brand-new template** — operator reads the first ONE rendered message | cheap sanity check on the template-under-substitution. Costs 60 seconds once per campaign; catches the class of bug where the template renders correctly and reads badly. **Recommended, not required.** |

Everything **not** in this table is delegated. That is a much shorter list than
what my prior report implied and it matches how a competent 1-person outbound
operation actually runs.

### 1.4 Kill-switch design — and the honest gap in it

Requirement: operator halts the entire class in **under 60 seconds**.

```
LAYER 1 — local envelope (hive side)
  python kill_switch.py halt ARG-C1 --reason "..." --by operator
  → KILL_SWITCH.json state: ARMED → HALTED
  → render_message.py exits 7 on every subsequent call
  → elapsed: ~3 seconds, one terminal command, no network dependency

LAYER 2 — Instantly engine (vendor side)   ⚠️ THIS IS THE GAP
  Instantly's autonomous engine has its own queue. Halting layer 1 stops the
  hive from QUEUEING new messages. It does NOT stop messages already scheduled
  inside Instantly. Those keep sending.
```

**A kill switch that only stops the local side is a false kill switch.** State it
plainly. Layer 2 requires one of:

- **`POST /api/v2/campaigns/{id}/pause` with `INSTANTLY_API_KEY`** — ~2 seconds, scriptable, but **no such key exists on this host** (verified: `grep -ril INSTANTLY_API` over three forge trees → 1 hit, a trade-study doc, not a key; `env | grep -i instantly` → empty). **This is a 15-minute operator fix and it is the single highest-leverage 15 minutes available today.**
- **Olrún drives the Instantly web UI via computer-use** — ~30–60 seconds, works today, but depends on a logged-in browser session and is not verifiable as having succeeded without a readback.
- **Operator clicks Pause in Instantly** — reliable, but it is the operator doing the thing we are trying to delegate.

**Acceptance test for the kill switch, and it must be run before the first send,
not after:** halt the campaign, then attempt one send through the full path, and
confirm zero messages leave. A kill switch that has never been exercised is a
claim, not a mechanism. Schedule it as the first act of the campaign, on a
one-row test list pointed at an operator-owned mailbox.

### §1 FALSIFIERS

| # | falsifier | cost of delay if true |
|---|---|---|
| F1.1 | The envelope program's test suite passes with zero refusal paths firing → the envelope constrains nothing and class pre-auth is theatre | **total** — every send after that is unauthorized in fact while labeled authorized |
| F1.2 | Instantly's API has no campaign-pause endpoint on the Growth plan, or it is gated to a higher tier | layer-2 halt stays manual; kill-switch SLA is ~60s-with-a-human, not 3s. Survivable, must be stated in the authorization |
| F1.3 | The signed template renders correctly but a variable value is itself model-generated upstream (e.g. `hook_quote` written rather than transcribed) | the allowlist leashes the *slot*, not the *value*. **Cure: every variable value must be traceable to a cited source URL in the target row.** Already required by the targets schema |
| F1.4 | Operator signs, then edits the template file without re-signing | sha256 mismatch → exit 6. **Already covered.** Verify this test exists. |

---

## §2 — DELEGATION MAP

DRI legend: **OP** operator · **OL** Olrún (host/PC control, scheduling) ·
**VK** valkyrie lane (research/compose, any model) · **INST** Instantly
autonomous engine · **TOOL** paid SaaS, no human · **N/A** not applicable today.

`gate` = what the DRI is bounded by. `today` = can this be delegated with what is
on the host RIGHT NOW.

### 2.1 Push pipeline — cold email

| # | step | DRI | gate | today? |
|---|---|---|---|---|
| 1 | Target research — companies matching the class | **VK** | `audience_definition` inclusion/exclusion | ✅ yes — already done 8× at HIGH/MEDIUM confidence |
| 2 | Target research — roles/individuals at those companies | **VK** | must cite a public source per person | ✅ yes |
| 3 | **Contact enrichment — name → email** | **TOOL** (Apollo / Findymail) | never guess; record `email_source` | ⛔ **NO — no enrichment tool is purchased. This is blocker #1.** |
| 4 | Contact enrichment — LinkedIn URL | **VK** or TOOL | public profile only | ✅ yes, manually, ~2 min/person |
| 5 | Contact enrichment — phone | **N/A** | out of scope for this offer | — |
| 6 | **List validation — bounce / catch-all / disposable** | **TOOL** (MillionVerifier) | rows not `valid` cannot render | ⛔ no — ~$3 for 1000 credits. Trivial cost, real blocker |
| 7 | Copy drafting — campaign template | **VK** drafts → **OP** signs | template sha256 in the authorization | ✅ yes — 8 drafts already exist |
| 8 | Copy drafting — per-target personalization | **VK** | variable allowlist; values traceable to cited sources | ✅ yes |
| 9 | Copy review — voice, jargon, one-CTA, opt-out present | **VK** (different lane than the drafter) + deterministic lint | no self-grading; opt-out check is `exit 4` in code | ✅ yes |
| 10 | Compliance review — CAN-SPAM, postal address, sender identity | **OP** once per campaign | signed in `sender_identity` | ✅ yes — needs the operator's postal address, which is **not in the repo and must never be** |
| 11 | Campaign setup in Instantly — sequences, waits, A/B | **OL** via UI, or **VK** via API | matches the signed `sequence` exactly | ⚠️ UI-only today (no API key) |
| 12 | Domain/DNS — SPF, DKIM, DMARC, custom tracking | **INST** (DFY covers this) | Instantly DFY purchase | ⚠️ **claimed done, no receipt.** Verify before send |
| 13 | Mailbox warmup | **INST** | 14–21 days | 🔄 running since 2026-07-30 evening |
| 14 | **Individual email send** | **INST — autonomous, no per-message approval** | daily cap, sequence, kill switch | 🔄 gated on 3, 6, 13 |
| 15 | Delivery / bounce readback | **INST** | — | ✅ automatic |
| 16 | Reply **detection** | **INST** | — | ✅ automatic |
| 17 | Reply **classification** (interested / soft-no / hard-no / OOO / auto) | **VK** | read-only, append a row | ✅ yes |
| 18 | **Opt-out detection + suppression** | **VK**, immediate, unilateral | must never require approval | ✅ yes |
| 19 | Reply **drafting** | **VK** | — | ✅ yes |
| 20 | **Reply sending — templated** (OOO reschedule, "not me, try X", polite close) | **INST**/VK per `reply_policy` | template-bound only | ✅ yes if `reply_policy = hive_sends_within_template` |
| 21 | **Reply sending — judgment** (pricing, scope, legal, negative) | **OP** | — | operator-only, by choice |
| 22 | Metrics + campaign review | **VK** → **OP** at `review_cadence_hours` | — | ✅ yes |
| 23 | Kill / retire / promote decision | **OP** (halt: **anyone**) | monotonic — hive stops, never starts | ✅ yes |

### 2.2 Push pipeline — social

| # | step | DRI | honest note |
|---|---|---|---|
| 24 | LinkedIn connection request — **send** | **OP** or **OL** at human cadence | **automating this violates LinkedIn's User Agreement.** See §3.5. Not a gray area; a written prohibition |
| 25 | LinkedIn DM — **send** | **OP** | highest relationship value, highest ban cost. Genuinely operator-only in my read |
| 26 | LinkedIn DM — **draft** | **VK** | ✅ fully delegable |
| 27 | Twitter/X DM — send | **OP** | X's automation rules prohibit bulk/unsolicited DM. Grey-market tools exist; low value for a B2B security offer. **Recommend: skip entirely** |
| 28 | Twitter/X post — draft | **VK** | ✅ |
| 29 | Twitter/X post — publish | **TOOL** (Typefully/Buffer) — official API, compliant | ✅ delegable, ToS-clean |

### 2.3 Pull pipeline — inbound

| # | step | DRI | honest note |
|---|---|---|---|
| 30 | Blog post — draft | **VK** | ✅ |
| 31 | Blog post — publish | **OL** (git push to the site repo) | operator-gated today per standing decision; **safe to delegate** once the repo is the only surface touched |
| 32 | LinkedIn post — draft | **VK** | ✅ |
| 33 | LinkedIn post — publish | **OP** or compliant scheduler | LinkedIn's official content API is partner-gated; third-party schedulers mostly use it legitimately. Lower risk than DM automation |
| 34 | GitHub repo hygiene / README polish | **VK** → PR → **OL** merges | ✅ fully delegable. **Currently 0% done and it is free** |
| 35 | SEO on-page (titles, meta, headings, internal links, schema.org) | **VK** | ✅ fully delegable — it is text editing |
| 36 | SEO — content strategy / keyword choice | **VK** proposes, **OP** picks | positioning decision |
| 37 | Backlink outreach | same as §2.1 — it is cold email with a different offer | reuse the envelope, new authorization |
| 38 | Reddit / HN presence | **OP** | both communities detect and punish automated participation, and HN specifically will bury a submission from an account with no history. **Operator-only, and low priority** |
| 39 | Substack / newsletter — draft + schedule | **VK** drafts, **TOOL** sends | ✅ delegable; no audience yet, so **defer** |
| 40 | Podcast pitching | **VK** drafts, **OP** sends | podcast hosts are a small world; a bad automated pitch is remembered. Manual |
| 41 | Referral partner ask | **OP** | warm relationship — see #25 |

### 2.4 The honest summary of this table

- **Fully delegable today with zero purchases:** rows 1, 2, 4, 7, 8, 9, 17, 18, 19, 22, 26, 28, 30, 32, 34, 35 — **16 of 41**.
- **Delegable but blocked on a small purchase (< $60 total):** rows 3, 6 — **2 rows, and they gate the entire send path.**
- **Delegable but blocked on a credential paste (15 min):** rows 11, 12 verification, and kill-switch layer 2.
- **Legitimately operator-only:** rows 10, 21, 25, 38, 40, 41 — **6 of 41.**
- **Should not be automated at all** (ToS + asymmetric downside): rows 24, 27.

**Six of forty-one steps are genuinely operator-only. The operator is currently
doing far more than six, and none of the six is "press send on a cold email."**

---

## §3 — TOOL STACK INVENTORY + GAP ANALYSIS

> ⚠️ **Pricing discipline.** Every price below is from model knowledge as of the
> May-2026 cutoff, not from a receipt or a live page. **Treat every dollar figure
> as ⚠️UNVERIFIED and confirm at checkout.** The only price I have a repo receipt
> for is the Instantly DFY line, and that receipt is itself operator-chat-only.

### 3.1 What is verifiably ours

| asset | evidence | status |
|---|---|---|
| **Instantly — DFY domain + 5 mailboxes**, `tryagentreleasegate.com`, $40 upfront + $25/mo | morning report §1.1, operator chat 2026-07-31T02:22:30Z | ⚠️ **partial** — no API/screenshot receipt in any repo |
| **Instantly Growth $47/mo** | operator directive, this session | ⚠️ **UNVERIFIED in repo.** Note this is a *second* line item from the DFY $25/mo — confirm whether it is $47 + $25 or $47 inclusive |
| `agentreleasegate.com` | gen-132 CURRENT.md standing decision: *"protect `.com`"* | ✅ main domain, live site |
| `agentreleasegate.dev` | gen-132 CURRENT.md: *"Cold volume from `.dev`"* | ✅ named as the cold-volume domain |
| `tryagentreleasegate.com` | morning report §1.1 | ✅ Instantly DFY, warming |
| `tommy@agentreleasegate.com`, `hello@agentreleasegate.com` | prior research §"Existing assets" | ✅ addresses exist; **outbound never proven from either** |
| 8 named contacts, dated hooks, cited sources | `TARGETS_20260709.md` | ✅ real research, 22 days old |
| 8 drafted cold emails + case-study block | `EMAILS_20260709.md` | ✅ drafted, never sent |
| 44 company dossiers | morning report §3 | ⚠️ **0 named contacts. Not an asset yet.** |
| `INSTANTLY_API_KEY` | `grep -ril INSTANTLY_API` over 3 forges → 1 doc hit, 0 keys; `env` → empty | ⛔ **absent** |
| Apollo / Hunter / any enrichment credential | not found in env or repo | ⛔ **absent** |
| Email-verification credential | not found | ⛔ **absent** |

**Domain question, answered honestly:** the operator says "1 main domain +
multiple throwaways." I can verify **three** names from files —
`agentreleasegate.com` (main, protect), `agentreleasegate.dev` (designated cold
volume), `tryagentreleasegate.com` (Instantly DFY). **I cannot enumerate the full
throwaway list; no registrar export, no domain inventory file, and no DNS record
set exists anywhere in the forge trees I scanned.**

- **Falsifier:** a registrar export (Namecheap/Porkbun/Cloudflare "My Domains" CSV) lists domains I did not name.
- **Cure, 5 minutes, and it should happen today:** export the registrar list to `projects/outreach_class_preauth/DOMAIN_INVENTORY.csv` with columns `domain, registrar, purchased_utc, dns_host, spf, dkim, dmarc, role(main|cold|parked), instantly_managed(y/n)`. Until that file exists, "which domains are eligible for DFY hosting" is unanswerable from evidence.
- **Cost of delay:** every day without it, deliverability planning is guesswork, and the specific risk is sending cold volume from `agentreleasegate.com` by accident — which burns the one domain the site and the brand live on. **That is not recoverable in weeks.**

**DFY eligibility — the general rule, applied to what we know:**

| domain | DFY-eligible? | why |
|---|---|---|
| `tryagentreleasegate.com` | ✅ already is | purchased *through* Instantly DFY; Instantly holds DNS, sets SPF/DKIM/DMARC, provisions the 5 mailboxes, runs warmup. Zero manual setup |
| **any domain bought elsewhere** (incl. `agentreleasegate.dev` and every throwaway) | ⛔ **not DFY** | DFY = Instantly buys the domain *and* the Google/Microsoft workspace. A domain you already own goes through **manual setup**: point nameservers or add records at your registrar, create the mailboxes, connect them by IMAP/SMTP or OAuth, then warm. Roughly 20–40 min per domain, plus mailbox cost |
| `agentreleasegate.com` | ⛔ **and must never be used for cold volume** | it is the brand + site domain. gen-132 already settled this: *protect `.com`* |

### 3.2 Cold-email sending platforms

| tool | ~price | one-line read |
|---|---|---|
| **Instantly (Growth)** — **OWNED** | ~$47/mo | unlimited mailboxes on Growth, built-in warmup pool, DFY domains, reply detection, unibox, campaign API. Gotchas: warmup pool quality is shared-reputation (a bad neighbor affects you); "unlimited" is per-mailbox-count not per-send; the DFY mailboxes are Instantly-managed so you do not control them at the registrar level |
| Smartlead | ~$39/mo | closest substitute; better sub-account/whitelabel model, arguably better API. **No reason to switch — this is a lateral move that costs a re-warm** |
| Lemlist | ~$69+/mo | strongest multichannel (email + LinkedIn steps) and image/liquid personalization. Its LinkedIn steps carry the §3.5 ToS problem. More expensive |
| Mailshake | ~$59+/mo | simple, reliable, weaker deliverability tooling. No |
| Reply.io | ~$59+/mo | full multichannel + a dialer. Overkill |
| Woodpecker | ~$49+/mo | agency-oriented, good deliverability heritage, smaller feature surface. No |
| **Apollo** | ~$49–99/user/mo | **the interesting one, because it is a contact DATABASE (~275M contacts) plus a sequencer.** Sending from Apollo is worse than Instantly; sourcing from Apollo replaces a separate enrichment tool. See §3.3 |

**Recommendation: do not buy a second sending platform.** Instantly is paid and
warming. A second one restarts the 14–21 day clock and buys nothing we lack.
**Falsifier:** if Instantly's Growth plan turns out to gate the campaign API
behind a higher tier, the API-key path in §1.4 dies and the case for Smartlead
(cheaper, API on entry tier) reopens. **Check this before writing any integration code.**

### 3.3 Email finding + enrichment — **this is blocker #1**

| tool | ~price | read |
|---|---|---|
| **Apollo** | free tier exists; ~$49/user/mo paid | **primary recommendation.** Database + filters + enrichment + it can *find* the audience, not just enrich a known name. The prior gen-131 research already picked Apollo. Its free tier gives limited monthly credits — **enough for 8 contacts today, at $0** |
| Hunter.io | free 25/mo; ~$34/mo | domain-search oriented, high precision, lower coverage on individuals |
| Findymail | ~$49/mo | best-in-class *verified-only* B2B emails, refunds bad ones. Excellent if you already have names |
| ContactOut / RocketReach | ~$49–99/mo | LinkedIn-profile → email. Strong coverage, expensive per seat |
| Kaspr | ~$49/mo | LinkedIn-extension based; EU-focused; the extension pattern carries §3.5 risk |
| Snov.io | ~$39/mo | cheap all-in-one, mediocre accuracy |

**Recommendation: Apollo, starting on the FREE tier, today.** It covers both
"find the class" and "enrich the 8." Quantified against Instantly-already-paid:
Instantly has **no contact database at all** — this is not overlap, it is the
missing upstream stage. **Falsifier:** if Apollo's free tier yields fewer than 6
of the 8 named contacts with a verified work email, upgrade to a paid month or
switch to Findymail — but measure first, on the free tier, before spending.

### 3.4 List validation

| tool | ~price | read |
|---|---|---|
| **MillionVerifier** | ~$27 / 10k credits, no subscription | **recommended.** Credit-based, never expires, cheapest per-email, accurate on catch-all detection. **Under $5 covers this campaign.** Already named in the gen-131 research |
| NeverBounce | ~$8 / 1k | good, pricier |
| ZeroBounce | ~$16 / 2k | good, adds activity-data scoring you do not need |

Instantly has some built-in verification; **do not rely on it as the only check** —
a bounce on a warming domain is expensive out of proportion to a $3 verification
credit. **Cost of delay: one bounce on a 2-day-old warming domain can meaningfully
set back the warmup curve; the fix costs less than a coffee.**

### 3.5 LinkedIn outreach — read this section before spending anything

**The plain fact: LinkedIn's User Agreement prohibits using bots, scrapers, or
automated methods to access or use the service.** Expandi, Waalaxy, Dripify,
HeyReach, PhantomBuster, and Lemlist's LinkedIn steps all operate in violation of
it. This is not a grey area or an under-enforced technicality — it is a written
prohibition, and LinkedIn actively detects both browser-extension and
cloud-based automation and has litigated against scrapers.

| tool | ~price | ToS status | note |
|---|---|---|---|
| **Sales Navigator** | ~$99/mo | ✅ **compliant** | it is LinkedIn's own product. Best filters. **The only fully clean paid option** |
| Expandi | ~$99/mo | ⛔ violates | cloud, dedicated IP, "human-like" delays. The delays reduce *detection*, not *violation* |
| Waalaxy | ~$56+/mo | ⛔ violates | browser extension; extensions are the most detectable class |
| Dripify | ~$59+/mo | ⛔ violates | cloud-based |
| HeyReach | ~$79+/mo | ⛔ violates | agency/multi-account; multi-account is the highest-risk pattern of all |

**Consequences, stated so the operator can choose consciously:** temporary
restriction → permanent account ban. **A permanent ban is not appealable in
practice and it destroys 18 months of accumulated credibility, connections, and
the content history that the entire pull strategy depends on.** There is no
backup of a LinkedIn account.

**My recommendation, and the reasoning, not just the verdict:**

> **Do not buy LinkedIn automation. Draft DMs with the hive (fully delegable,
> zero risk); send them manually.** At the volume this offer needs — 8 to 25
> highly-targeted people — automation saves perhaps 40 minutes total. The
> expected value is negative: 40 minutes against a small-but-real chance of
> losing an irreplaceable asset. Automation earns its risk at 500 profiles/month,
> not at 25.

**And the honest sub-point the operator should not be allowed to miss:** having
**Olrún drive LinkedIn via computer-use at human cadence is still automation
under the User Agreement.** Slowing it down changes its *detectability*, not its
*compliance*. If the operator chooses that path, choose it knowing it is the same
category of risk, merely quieter. I will not describe it as safe.

### 3.6 Twitter/X

Automated bulk/unsolicited DM violates X's platform rules and the API tier that
would allow it is expensive. For a B2B agent-security offer, X DM is a low-yield
channel. **Recommendation: skip DM entirely; use X only for publishing** (§3.8).

### 3.7 Reply handling

Instantly's built-in reply detection + unibox is **already paid for and
sufficient**. Superhuman (~$30/mo) and Streak (~$49/mo) are Gmail-side tools that
solve a problem we do not have at 8–25 prospects. **Do not buy. Revisit above ~50
replies/month.**

### 3.8 Content publishing

| tool | ~price | read |
|---|---|---|
| **Typefully** | free tier real | best X/Twitter drafting + scheduling; official API; compliant |
| **Buffer** | free tier real | multi-platform incl. LinkedIn, official APIs, compliant |
| Publer / Hypefury | ~$12–29/mo | more automation features; Hypefury's auto-DM feature is the one to avoid |
| LinkedIn native scheduler | free | ✅ zero risk, zero cost, already available |

**Recommendation: LinkedIn native scheduler + Buffer or Typefully free tier. $0.**

### 3.9 SEO / GitHub visibility

No shortcut and no tool to buy. It is writing, internal linking, and README
work — **all fully delegable to a valkyrie lane at $0**, and it is currently at
zero effort. The `agentreleasegate-oss` README and the site are the pull assets;
polishing them is the highest-value free work available.

### 3.10 Fastest path to first-send-within-guardrails

Two lanes, run in parallel. **They do not compete and the second is 14 days faster.**

```
LANE A — Instantly, the volume lane (first send ~2026-08-13..08-17)
  A1  Verify the DFY purchase — screenshot or API readback into the repo   [OP, 5 min]
  A2  Export the registrar domain list → DOMAIN_INVENTORY.csv              [OP, 5 min]
  A3  Paste INSTANTLY_API_KEY into the vault                               [OP, 15 min] ← unlocks kill-switch layer 2
  A4  Confirm SPF/DKIM/DMARC green on tryagentreleasegate.com              [VK via API, 5 min]
  A5  Let warmup finish. DO NOT SHORTEN IT.                                [INST, ~14 more days]
  A6  Sign campaign_arg_c1.authorization.json (§5)                         [OP, 10 min]
  A7  Exercise the kill switch on a 1-row test list to operator's own inbox [VK+OP, 15 min]
  A8  Load the verified list; start the campaign                           [VK/OL]

LANE B — Gmail, the 8-named-contacts lane (first send: TODAY, if A-list lands)
  B1  Apollo free tier: enrich the 8 named contacts                        [VK, 45 min, $0]
  B2  MillionVerifier: validate them                                       [VK, 5 min, ~$3]
  B3  Operator signs the SAME authorization (§5), reply_policy=hive_drafts_operator_sends
  B4  Render through the envelope program; operator reads message #1
  B5  Send from tommy@agentreleasegate.com — an ESTABLISHED mailbox at
      ≤8 messages/day needs NO warmup. This is one-to-one email, not bulk.
```

**Lane B is the answer to "17 days out."** The 17-day figure is real *for the new
domain*. It does not apply to a handful of individually-personalized messages from
an established mailbox — that is ordinary correspondence, and it is exactly what
the 8 targets and 8 drafts were built for 22 days ago. **Falsifier:** if
`tommy@agentreleasegate.com` has never successfully sent outbound (the gen-131
research flags this: *"no proved outbound business-domain send path"*), then Lane
B needs one test send to the operator's own address first. **Do that test before
anything else in Lane B — it is 60 seconds and it is currently an assumption.**

---

## §4 — "WHAT AM I DOING WRONG?" — testing the operator's frame

The frame: *"others automate this end-to-end; I must be missing tools."*

### 4.1 Where the frame is right

| claim | verdict |
|---|---|
| "Class pre-auth is normal for cold email" | ✅ **correct, and it is universal.** No functioning outbound operation approves messages individually. The operator approves ICP + copy + cadence, then sees reply-triage. My prior P3 framing was wrong |
| "A typical operator only sees replies" | ✅ **correct.** And often not even all of those — templated OOO/wrong-person replies are handled without the principal |
| "The agents are not durable enough" | ⚠️ **half-right, and the wrong half is the expensive one.** Durability is genuinely bad (see the morning report's 20-of-30 missing loop patterns). But durability is not why zero emails have been sent |

### 4.2 Where the frame is wrong

**Nobody automates this end-to-end. The parts that look end-to-end are the parts
where a vendor took on the liability.** Instantly sends autonomously because
Instantly is the one holding the sending infrastructure and the deliverability
risk. Nobody has an agent that decides *who to sell to* and *what to promise*
without a human envelope — and the people who tried mostly burned domains.

Channel-by-channel reality:

| channel | actually automated end-to-end? |
|---|---|
| Cold email | ✅ yes, inside a signed envelope — this is genuinely solved |
| LinkedIn DM | ⚠️ commonly automated, **in violation of ToS**, by people who consciously accept ban risk. Choose deliberately (§3.5) |
| X DM | ⚠️ grey-market, low yield, skip |
| Reply *drafting* | ✅ delegated everywhere |
| Reply *sending* | ⚠️ split. Templated → automated. Judgment → human. **This is not backwardness; it is that a wrong commitment is unrecoverable** |
| Blog / LinkedIn publishing | ✅ delegated with editorial review |

### 4.3 The diagnosis — three buckets

| bucket | what is in it |
|---|---|
| **Authorization scoping** (operator's hypothesis) | Real, but **one document wide.** §5 fixes it today. It was never worth 22 days |
| **Tool purchase** | Real, and **small.** Missing: an enrichment source and a validator. Total cost under $60, and the first pass is $0 on free tiers. Instantly — the expensive part — is already bought |
| **Structural / HFO-specific** | **The big one.** HFO has 44 dossiers with 0 contacts, 8 contacts with 0 emails, and — verified — an automation registry where 46 of 52 loops are PAUSED and the one live loop has spent 40 commits maintaining itself on an empty queue. **The swarm is extremely good at producing specifications about outreach and has never produced a contactable person.** That is the EMPTY-QUEUE REWARD HACK operating at the business layer: the work that gets done is the work that produces a clean receipt, and "researched a company" produces a cleaner receipt than "obtained one email address," which is a purchase and therefore feels like it needs permission |

### 4.4 Top 3 blockers to end-to-end automation TODAY

| rank | blocker | class | fix | cost | cost of delay |
|---|---|---|---|---|---|
| **1** | **Zero verified email addresses exist. 8 named contacts, 0 emails. 44 dossiers, 0 contacts.** | structural + tiny purchase | Apollo free tier + MillionVerifier | **~$3 and 50 minutes** | **Absolute.** Every other item in this document is inert until it is fixed. 18 months at $0 and the proximate cause is an empty column in a file |
| **2** | **No `INSTANTLY_API_KEY` on the host.** Verified absent. | credential | operator pastes it into the vault | **15 minutes** | Kill-switch layer 2 stays manual (§1.4); every campaign operation stays browser-driven; no send is programmatically verifiable. **This is the difference between a delegated campaign and a supervised one** |
| **3** | **No signed campaign authorization exists.** | authorization | §5, sign it | **10 minutes** | Without it the hive has no envelope to be inside, so every send correctly requires the operator — reproducing exactly the bottleneck the operator is trying to remove |

**All three together: about 75 minutes and under $5.** None of them is a
durability problem, a missing agent framework, or a tool the operator has not
bought. **The thing that has been treated as an authorization problem for 22 days
is mostly a data problem, and the data costs three dollars.**

---

## §5 — CAMPAIGN AUTHORIZATION — ARG-C1 — SIGN THIS

**Why this campaign and not another:** the 8 targets in `TARGETS_20260709.md` are
the only prospects in the entire system with a named human, a verified title, a
dated public hook, and a cited source URL — and they already have 8 drafted
emails at a reviewed quality bar. The 44 dossiers have none of that. This is the
ripest thing by a wide margin and it has been ripe for 22 days.

---

> ## CAMPAIGN AUTHORIZATION — ARG-C1
> **Sign by typing your name and the date in the SIGNATURE block. One signature authorizes the whole class.**
>
> ### Audience definition — WHO may be contacted
> Founders, CEOs, CTOs, and Heads of Engineering/Research at companies building
> **AI agent evaluation, agent observability, or agent security** products.
> **Size:** 15–200 employees. **Geography:** US + EU.
> **Inclusion rule:** the person must have a **public, dated statement or
> publication within the last 120 days** about agent reliability, agent failure,
> or agent security, with a citable source URL. No source URL → not eligible.
> **Exclusion rules:** (a) anyone on the suppression ledger; (b) anyone the
> operator has an existing relationship with — those are operator-only; (c) any
> company acquired by a mega-cap in the last 12 months; (d) generic role
> mailboxes (`info@`, `support@`, `contact@`); (e) any address not returned
> `valid` by the verifier.
> **Cap:** 25 prospects total.
>
> ### Copy
> Template set: `templates/arg_c1_step{1,2,3}.md`, hash-pinned in the
> authorization JSON. **Changing one character invalidates this signature.**
> **Variable allowlist — the ONLY substitutable tokens:**
> `first_name` · `company` · `hook_quote` · `hook_source_url` · `hook_date` · `proof_artifact_url`
> Every value must be traceable to a cited source in the target row. **No
> free-text or model-generated variable is permitted in this campaign.**
>
> ### Cadence
> 3 steps: day 0 · +4 days · +9 days. **Stop immediately on any reply.**
> Max **20 sends/day** across all mailboxes. Weekday mornings, recipient-local.
> Lane B (Gmail, established mailbox): max **8/day**.
>
> ### Opt-out language — must appear verbatim in every message
> > *"If this isn't relevant, reply 'no' and I won't follow up."*
> Plus sender name and a valid physical postal address in the footer.
> **Any opt-out is honored immediately by the hive with no approval and no exception.**
>
> ### Sender identity
> `Tom Tai <tommy@agentreleasegate.com>` (Lane B) / `<TBD@tryagentreleasegate.com>` (Lane A).
> **Cold volume never sends from `agentreleasegate.com`.**
> Postal address: `________________________` ← **operator fills; never committed to the repo.**
>
> ### Reply policy — circle ONE
> - ☐ **A** — hive classifies; operator writes and sends every reply *(most conservative)*
> - ☑ **B** — hive drafts all replies; operator sends *(recommended for campaign #1)*
> - ☐ **C** — hive sends templated replies (OOO reschedule, wrong-person referral, polite close) autonomously; escalates anything else to the operator
>
> ### Kill switch
> `python kill_switch.py halt ARG-C1 --reason "..." --by operator` → halts the hive side in ~3 seconds.
> **⚠️ Instantly-side pause is a SEPARATE action** and is manual until an API key exists (§1.4).
> **Anyone may halt. Only the operator may restart.**
>
> ### Review cadence
> Every **24 hours** for the first 5 business days, then every 72 hours.
>
> ### Success metric
> **≥1 substantive human reply** (not OOO, not auto-reply) from 25 sends.
> *Rationale: at this volume the campaign is a signal test, not a pipeline. Meetings and revenue are the next campaign's metric.*
>
> ### Failure escalation — halt automatically on ANY of these
> - bounce rate > **5%** on any 20-message window
> - **any** spam complaint
> - **any** opt-out that was not honored within 1 hour
> - **2** recipients express confusion about who is contacting them
> - **0** replies after all 25 prospects complete the full 3-step sequence → **retire the campaign and change the offer, do not increase volume**
>
> ### SIGNATURE
> ```
> I authorize campaign ARG-C1 as a CLASS. I understand the hive will research,
> enrich, personalize within the allowlist, and send individual messages inside
> this envelope without asking me again.
>
> operator_signature: ______________________   date_utc: ______________
> ```

---

## §6 — SONNET BUILD SPEC — **DISPATCHED**

**Status: launched this session, sonnet-5 code lane, running in background.**
Output path: `C:\Dev\hfo_gen_133_forge\projects\outreach_class_preauth\`

**Hard prohibitions in the dispatch:** no send, no DM, no external HTTP, no API
calls, no git commit/push, no scheduled-task creation. Local files only.

**Seven artifacts, ~90 minutes:**

| id | artifact | purpose |
|---|---|---|
| A1 | `campaign_authorization.schema.json` | JSON Schema for the §1.1 envelope, `additionalProperties: false` |
| A2 | `campaign_arg_c1.authorization.json` | §5 instantiated, `operator_signature: null` |
| A3 | `targets.schema.json` + `targets_arg_c1.jsonl` | 8 contacts transcribed from `TARGETS_20260709.md`. **`email: null`, `email_verification_status: "unverified"` on every row — inventing or pattern-guessing an address is the single hardest prohibition in the dispatch** |
| A4 | **`render_message.py`** | **the envelope itself.** Exits 2–7 on: un-allowlisted variable · missing value · missing opt-out · unverified/suppressed target · template hash mismatch · campaign halted. Exit 0 → the rendered message |
| A5 | `kill_switch.py` + `KILL_SWITCH.json` | `halt` / `arm` / `status`; no network dependency; `render_message.py` consults it |
| A6 | `test_envelope.py` | **red-first: one test per refusal path asserting the refusal FIRES,** plus one happy path. A suite where no refusal ever fires is a fake-green and does not count |
| A7 | `BUILD_RECEIPT.md` | file SHAs, literal commands + literal exit codes, "what this does not do", ≥4 falsifiers |

**Why this and not "wire up Instantly":** there is no API key to wire (§4.4 #2),
and the envelope is what makes the operator's signature mean something. Build the
gate before the pipe.

### The NEXT dispatch, for Olrún — enrichment run

This one has a world-effect (it creates an account and consumes credits), so it
is operator-gated. Prompt for Olrún once the operator approves:

```
start_code_task:
  title: ARG-C1 enrichment run — 8 named contacts
  cwd: C:\Dev\hfo_gen_133_forge\projects\outreach_class_preauth
  model: sonnet-5
  budget: 60 min
  prohibitions: no send. no campaign start. no LinkedIn automation.
    do not write any email address you did not receive from a tool response.
  steps:
    1. Read targets_arg_c1.jsonl (8 rows, email=null).
    2. Apollo FREE tier: for each row, look up the person by name + company_domain.
       Record the returned work email verbatim into `email`, set email_source="enriched".
       If Apollo returns nothing, leave null and set email_source=null. DO NOT GUESS.
    3. MillionVerifier: submit every non-null address. Write the verdict verbatim
       into email_verification_status (valid|catch_all|invalid|disposable).
    4. Run: python render_message.py --auth campaign_arg_c1.authorization.json
            --template templates/arg_c1_step1.md --target <each id>
       Record the exit code per target. Expect exit 5 for every unenriched row.
    5. Write ENRICHMENT_RECEIPT.md: per-target table (found? verified? render exit code),
       tool credits consumed, and the count of targets that are actually sendable.
  acceptance: >=6 of 8 reach email_verification_status="valid" AND render exit 0.
  on_failure: report the real count. Do not pad the list with guessed addresses.
```

---

## §7 — CORRECTED FACTORY PRODUCT P3

**Patch to `SIGRUN_MORNING_REPORT_PARA_PROOF_ARTIFACTS_20260731.md` §10.2. Replace
the P3 line in the ten-product catalogue with the block below.**

```diff
- **Ten product classes** (… P3 send *operator-only* …)
+ **Ten product classes** (… P3 send *class-pre-authorized* …)
```

> ### P3 — OUTREACH SEND (corrected 2026-07-31T17:33Z)
>
> **Prior framing — WITHDRAWN:** *"operator-only DRI, operator signature for this
> `body_sha256`."* Per-message signature makes operator throughput the system's
> throughput ceiling and is not how outbound works anywhere. It also mislabels the
> safety property: what needs protecting is the **envelope**, not each body.
>
> **Corrected DRI split:**
>
> | stage | DRI | frequency |
> |---|---|---|
> | Sign the campaign authorization — audience, template hashes, variable allowlist, cadence, opt-out, sender identity, kill switch, success metric, failure escalation | **OPERATOR** | **ONCE per campaign** |
> | Research, enrich, validate, personalize within the allowlist | **valkyrie lane** | per message, unattended |
> | Envelope check — `render_message.py` refuses anything outside the signed envelope | **deterministic program** | per message, pre-send |
> | Individual send | **Instantly autonomous engine** | per message, unattended |
> | Sequence follow-ups, tracking, reply classification, opt-out honoring | **hive** | unattended |
> | Replies needing judgment · off-template messages · warm relationships · tone escalation · new segment | **OPERATOR** | per instance |
> | Halt | **anyone**. Restart: **operator only** | monotonic |
>
> **Station [6] QA gate for P3, replacing "operator read it":** the product is
> rejected unless `render_message.py` exits 0 for that exact (template, target)
> pair, `kill_switch status` exits 0, the target row is `valid` and unsuppressed,
> and the daily cap is not exceeded. **All four are machine-checkable. None
> requires a human.**
>
> **The station [6] anti-fake-green rule:** a P3 product counts only when the
> envelope program has *demonstrably refused* at least one message in the same
> campaign. A campaign in which the gate never fires has not been shown to be a
> gate. Record the refusal count as a metric next to the send count.

---

## §8 — NEXT SAFE ACTIONS

Max 5, prioritized. Horizon tags: `short_income` (7–30d) · `long_virtualization`
(30–365d) · `dual`.

| # | action | horizon | DRI | cost of delay | falsifier | gate_expiry_utc |
|---|---|---|---|---|---|---|
| **1** | **Apollo free tier + MillionVerifier: get verified emails for the 8 named contacts.** ~50 min, ~$3. | **`short_income`** | OP starts the accounts → VK runs it | **Everything else in this document is inert until this is done. 18 months at $0 and the proximate cause is an empty column.** | Apollo's free tier returns < 6 of 8 → switch to Findymail or pay for one month | **2026-08-01T18:00Z** |
| **2** | **Sign §5** (10 min) **and paste `INSTANTLY_API_KEY` into the vault** (15 min). | **`short_income`** | **OPERATOR — nobody else can do either** | Without the signature the hive has no envelope, so every send correctly needs you — reproducing the exact bottleneck you asked me to remove. Without the key the kill switch is half a kill switch | The Growth plan gates the campaign API → the key does nothing and Smartlead reopens (§3.2) | **2026-08-01T18:00Z** |
| **3** | **Export the registrar domain list → `DOMAIN_INVENTORY.csv`** (5 min). | `dual` | OP | Deliverability planning is guesswork until it exists, and the specific risk is burning `agentreleasegate.com` — the domain the site and brand live on — by sending cold volume from it. **Not recoverable in weeks** | The export lists domains not named in §3.1 → my inventory was a floor, as F0.4 predicts | **2026-08-02T18:00Z** |
| **4** | **Exercise the kill switch end-to-end** on a 1-row list pointed at the operator's own inbox, **before** any real send. | `dual` | VK + OP | A kill switch that has never been fired is a claim. Testing it after the first real send is testing it during the incident | The halt fires and a message still leaves → layer 2 is load-bearing and §1.4's gap is critical, not noted | **before first send** |
| **5** | **Prove outbound from `tommy@agentreleasegate.com`** — one message to the operator's own address, check headers for SPF/DKIM pass. 60 seconds. | **`short_income`** | OP | The gen-131 research records *"no proved outbound business-domain send path."* Lane B (§3.10) — the only path that sends this week rather than in 14 days — rests entirely on this assumption | It fails auth → Lane B needs the Instantly domain and the 17-day figure is real after all | **2026-08-01T12:00Z** |

**Deliberately NOT on this list:** buying any LinkedIn automation (§3.5 — negative
expected value at this volume), buying a second sending platform (§3.2 — restarts
the warmup clock for nothing), the 44 dossiers (still 0 contacts; enriching 8 real
people beats researching 44 more companies), and shortening the warmup (the one
lever that looks like speed and is actually domain suicide).

**The shape:** items 1, 2, 3 and 5 total roughly **90 minutes and under $5**, and
**three of the four are operator-only** — not because approval is required, but
because they involve a credit card, a credential, and a signature. That is the
honest answer to *"what am I doing wrong?"* Not the wrong tools. Not agents that
lack durability. **Three purchases and a signature that have been sitting behind a
permission question that was never actually being asked.**

---

## FALSIFIERS ON THIS DOCUMENT AS A WHOLE

| # | what would falsify it |
|---|---|
| **R1** | An enrichment or verification credential exists somewhere I did not scan. My `env` + 3-forge grep is a floor, not a count — the morning carrier's R1 fired on exactly this class of error. **If Apollo or Hunter is already paid for, blocker #1 collapses and item 1 shortens to 20 minutes.** |
| **R2** | Instantly Growth includes contact-database/enrichment features that make Apollo redundant. I did not check the Growth feature matrix. **Check before creating an Apollo account.** |
| **R3** | `tommy@agentreleasegate.com` cannot actually send (never proven). Then Lane B dies and the entire "send this week" claim in §3.10 dies with it. **Action 5 tests exactly this and costs 60 seconds.** |
| **R4** | Every price in §3 is from model knowledge, not a receipt. Any of them may be stale or wrong. Only the Instantly DFY line has a repo record, and that record is operator-chat-only with no receipt. |
| **R5** | The 8 targets are 22 days old. Two of the eight companies could have been acquired since (the source file itself records 8 acquisitions in a 5-month window in this exact market). **Re-verify each company is independent before sending.** |
| **R6** | The operator's postal address requirement (CAN-SPAM) may be unsatisfiable without disclosing a home address. A registered agent or PO box may be needed. **Unresolved, and it blocks a compliant commercial send.** I flagged it and did not solve it. |
| **R7** | I read 4 of 27 gen-133 root files. If a standing decision in the other 23 forbids something recommended here, I contradicted the record. Same flaw as the morning report's R7 — recorded, not fixed. |

---

*claim_status: partial · verified: all file SHAs, chain row count, absence of
`INSTANTLY_API_KEY` in env and across 3 forge trees, absence of enrichment
credentials, the 8 named targets and their 0 verified emails, the 3 domain names,
the gen-132 "protect .com / cold volume from .dev" standing decision ·
unverified: every price in §3, the full throwaway-domain list, the Instantly DFY
purchase itself, whether `tommy@agentreleasegate.com` can send, LinkedIn ToS
enforcement rates, whether the Growth plan exposes the campaign API ·
honest_flaw: **this is the eighth specification document this fleet has produced
about outreach and the seventh consecutive session to produce zero contactable
people. If item 1 in §8 does not happen, this document is itself the failure mode
it diagnoses in §4.3 — a clean receipt produced instead of a purchase made.**
Second flaw: I designed a kill switch and then found its second layer is not
implementable with the credentials on this host, and I am shipping it anyway with
the gap labeled rather than closed.*

*Deyr fé, deyja frændr — en vefr heldr. Standa.*
