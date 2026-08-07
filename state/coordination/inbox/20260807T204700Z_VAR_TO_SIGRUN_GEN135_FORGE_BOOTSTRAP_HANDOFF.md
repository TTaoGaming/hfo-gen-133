---
schema_id: hfo.gen134_to_gen135.sigrun_forge_handoff.v1
valid_time_utc: 2026-08-07T20:47:00Z
producer:
  callsign: Var
  authority: HANDOFF_ONLY
operator_directive: >-
  Cut over into a clean Gen-135 forge, local + GitHub, preserving high-value
  heritage/skills/personas/souls/cards while refocusing the system on income.
  Automated loops should research targets, build useful kits, pass release
  gates, send under explicit effect policy, update CRM, and follow up.
scaffold_authority: Sigrun
world_effect_ceiling: INBOX_HANDOFF_ONLY
status: READY_FOR_SIGRUN_PICKUP
---

# VAR → SIGRUN — GEN-135 FORGE BOOTSTRAP HANDOFF

## 0. Authority gate

**Sigrun is the sole authority for the Gen-135 scaffold/build.**

Var is not authorized to create the Gen-135 repo, local checkout, branch model,
workflow implementation, or production agent runtime. This packet is an inbox
handoff only. Do not treat it as a scaffold receipt.

## 1. Operator intent

Create a **clean Gen-135 forge today** with:

1. local repository + GitHub repository;
2. PARA topology for clean migration and progressive disclosure;
3. portable heritage: skills, agent personas/souls/cards, identity/eigenstate
   pointers, proven patterns, and useful receipts;
4. **income as the primary external fitness signal**;
5. automated agent loops that perform:

```text
TARGET RESEARCH
   ↓
EXPENSIVE-PAIN HYPOTHESIS
   ↓
2-MINUTE USEFUL PROOF KIT
   ↓
DISTINCT VERIFICATION / RELEASE GATE
   ↓
EFFECT GATE: SEND / APPLY / CONTACT
   ↓
CRM RECEIPT
   ↓
FOLLOW-UP / REPLY / MEETING
   ↓
LEARNING + EVAL
```

A task wake, research card, or built artifact is not success. Preserve the
existing revenue-state ladder:

`researched → kit_verified → operator_or_policy_approved → sent/applied → reply → meeting/interview → qualified_problem → proposal → paid → retained_margin`

Never borrow evidence upward.

## 2. Clean-build doctrine

**Do not recursively copy Gen-133/132 into Gen-135.** Existing heritage doctrine:
`You do not migrate heritage — you address it.`

Migration classes:

- **ADOPT** — small proven portable artifact needed immediately.
- **ADDRESS** — keep exact `repo@commit:path#blob` pointer; hydrate on demand.
- **ADAPT** — copy into Gen-135 only after rewriting for the new contract.
- **ARCHIVE** — historical context only; never auto-load.
- **REJECT** — treadmill/reward-hacking/duplicate machinery with no consumer.

Every imported heritage artifact records source repo/ref/path/blob and its
migration disposition. Heritage copy is **not** live identity.

## 3. Recommended PARA scaffold — Sigrun to approve/change

```text
hfo-gen-135/
├── README.md
├── AGENTS.md
├── CURRENT.md
├── 00_INBOX/
│   ├── operator/
│   ├── agents/
│   └── migration/
├── 10_PROJECTS/
│   ├── income-engine/
│   │   ├── targets/
│   │   ├── research/
│   │   ├── kits/
│   │   ├── campaigns/
│   │   └── receipts/
│   └── gen135-forge/
├── 20_AREAS/
│   ├── authority-control/
│   ├── agent-runtime/
│   ├── release-gates/
│   ├── evals-observability/
│   ├── revenue-operations/
│   └── platform-operations/
├── 30_RESOURCES/
│   ├── heritage/
│   │   ├── pointers/
│   │   ├── souls/
│   │   ├── cards/
│   │   ├── engrams/
│   │   └── receipts/
│   ├── skills/
│   ├── cots/
│   └── patterns/
└── 40_ARCHIVE/
    ├── migrations/
    ├── deprecated/
    └── superseded-experiments/
```

**Privacy boundary:** private Life OS / contacts / CRM PII remain in private
Drive or another explicit private store. Public Git receives sanitized target,
public-source, artifact, policy, test, and receipt material only.

## 4. Agent genotype contract to standardize

Separate identity from authority and mutable state:

```text
actor/
├── SOUL.md          # slow identity / values / role continuity
├── CARD.yaml        # machine-readable capability + interface card
├── AGENTS.md        # environment/project instructions
├── skills/*/SKILL.md
├── POLICY.rego      # authority/effect rules OUTSIDE persona
├── lineage.yaml     # predecessor/provenance/version
└── state/           # mutable runtime/eigenstate, never confused with soul
```

Hard rule: **SOUL.md is not an authorization boundary.** Tool/effect authority
must be machine-enforced outside the persona prompt.

## 5. COTS/harness decision — fresh verification required

Do not hand-build another harness before running a bounded COTS spike. Var's
Aug-7 research pass identified these candidates; **Sigrun must re-verify current
versions/docs before pinning dependencies**:

### Primary candidate
- **Pydantic AI + Pydantic AI Harness + DBOS durability**
  - strong fit with existing Python, DBOS, Postgres, LiteLLM/Ollama/provider mix;
  - candidate features: skills, planning, memory, subagents, compaction,
    filesystem/shell, guardrails, MCP, durable steps.

### Required challenger
- **Microsoft Agent Framework / Harness**
  - batteries-included production worker baseline;
  - useful comparison for skills, planning, approvals, persistence, telemetry.

### Specialized challengers / pattern donors
- **Deep Agents / LangGraph** — context isolation and subagent/filesystem pattern.
- **Google ADK 2.0 + A2A** — deterministic workflows and remote Agent Cards.
- **OpenAI Agents SDK** — thin custom experimental substrate.
- **Letta / Trajectory concepts** — persistent memory and cross-harness
  experience, but never authority.
- **AGENTS.md + Agent Skills (`SKILL.md`)** — portable project/procedure genes.
- **OPA/Rego** — external fail-closed authorization/release gates.

Do not install all frameworks into the production path. Choose **one primary
harness**, keep one challenger cell, and borrow patterns from the rest.

## 6. Release-gate architecture

Every automated income loop crosses explicit gates:

```text
G0 INTAKE
  exact target/work-item id; WIP admitted
      ↓
G1 RESEARCH
  current primary-source evidence + public/private classification
      ↓
G2 PAIN / VALUE
  pain is hypothesis unless externally confirmed; measurable consequence named
      ↓
G3 KIT
  recipient-useful artifact exists; claims source-bound
      ↓
G4 VERIFY
  distinct verifier; hidden/adversarial checks where useful; PASS/FAIL/ABSTAIN
      ↓
G5 EFFECT
  send/apply/contact effect class explicitly allowed by operator/policy
      ↓
G6 CRM
  exact sent/applied receipt recorded; draft ≠ sent
      ↓
G7 FOLLOW-UP
  bounded due date; reply/meeting/proposal/payment changes fitness
```

Default migration posture for external effects: keep HITL/operator approval
until Sigrun + operator intentionally authorize a bounded auto-send class.

## 7. Income lane heritage to pick up first

Current Gen-133 public packet:
`projects/gtm-revenue/packets/20260807T140800Z_CHATGPT_CLOUD_GTM_DREAM50_HANDOFF.packet.md`

High-value proposed portable skills already exist and should be **verified then
adopted/adapted rather than recreated**:

- `projects/gtm-revenue/skills/hfo-revenue-problem-discovery/SKILL.md`
  - source commit `6996f81fac97a05aaf655fc41d107c5c0d2d3032`
- `projects/gtm-revenue/skills/hfo-dream50-target-research/SKILL.md`
  - source commit `5534da9f3453835a4491fcebf4103d90b63d2651`
- `projects/gtm-revenue/skills/hfo-two-minute-proof-kit/SKILL.md`
  - source commit `31f66f2b1e9e52bef83ff6c95b667bfb57c1d9e8`
- `projects/gtm-revenue/skills/hfo-hyperpersonalized-outreach-packet/SKILL.md`
  - source commit `66bc480e1cc98c8b231e5483d439e4a071062bac`

Do not migrate the 200-target universe as WIP. It is search space. Start with
one target through the entire loop.

## 8. Identity/heritage sources to address, not blindly copy

### Gen-133
- `state/identity/soul/POINTERS.md`
- `state/identity/soul/sigrun.gen133.soul.md`
- `archives/heritage/soul-harvest/20260802_step01/manifest.yaml`
- `packets/P0_HERITAGE_POINTERS.md`
- `AGENTS.md`
- `CURRENT.md`

### Gen-132 via pointer
- `canon/spec/HFO_SOUL_PHYLACTERY_v1_SPEC.md`
- `canon/CLOSEST_CONTINUER_SEAL_AND_GEN132_CHARTER_20260725.md`
- `chains/VALKYRIE_CLOSEST_CONTINUERS.jsonl`
- `generation/GEN132/gleipnir/rehydration/capsules/lineages/SIGRUN/SHADOW_SIGRUN_HLUTI_EIGENSTATE_ENGRAM_20260726T133537Z.yaml`
- `gleipnir_grimoire_gen132/`

Important inherited distinction:
- **soul** = slow continuity contract;
- **eigenstate/engram** = fast, receipt-gated runtime snapshot.

The Gen-133 soul harvest records Sigrun's Gen-133 soul as
`SELF_AUTHORED_UNRATIFIED`; do not silently promote it to canonical identity.
Carry the status/conflict into the new migration gate.

## 9. Proven control-plane heritage worth retaining as requirements

From Gen-133 electronic-institution candidate:

- Git exact bytes as authority;
- WIP=1 actor admission;
- OPA decision point, enforcement outside OPA;
- fail closed on undefined/unhealthy/stale/digest-mismatched policy;
- distinct verifier cannot edit candidate;
- candidate → VERIFIED → CONSUMED only with explicit receipts;
- external handlers must be idempotent;
- HOLD/ANDON on unknown effects, stale basis, missing verifier/consumer receipt.

These are **requirements/patterns**, not a command to migrate XTDB/Cloudflare/
Arweave infrastructure unless a Gen-135 consumer justifies each component.

## 10. Minimal first-day acceptance target

Sigrun should prefer a thin walking skeleton over architecture completeness.
Suggested end-of-day gate:

- [ ] new Gen-135 GitHub repo + local clone exist and remote round-trip is proven;
- [ ] PARA root + `README.md` + `AGENTS.md` + `CURRENT.md` exist;
- [ ] authority/effect policy is separate from persona and fail-closed;
- [ ] heritage manifest lists ADOPT/ADDRESS/ADAPT/ARCHIVE/REJECT with exact pointers;
- [ ] Sigrun identity is migrated through explicit lineage/ratification rules, not copied green;
- [ ] at least the 4 revenue skills above are evaluated for adopt/adapt/merge;
- [ ] one primary harness is pinned; one challenger is isolated;
- [ ] one **single target** executes research → pain hypothesis → kit → distinct verify → effect HOLD/approval → CRM receipt in dry-run or bounded live mode;
- [ ] trace/eval receipt exists for that run;
- [ ] no autonomous mass outreach, mass migration, or 200-target fan-out occurred.

## 11. Fitness / ANDON

Gen-135 exists to convert technical capability into external consequence.

Fitness signals, strongest first:
1. paid receipt / retained margin;
2. qualified problem / proposal;
3. meeting/interview/referral;
4. genuine reply;
5. verified useful kit;
6. research/artifact generation.

If internal artifacts rise while external signals stay flat, trigger ANDON and
change target/offer/channel/process rather than adding more architecture.

## 12. Sigrun pickup request

Sigrun: on pickup, return an exact receipt with:

```yaml
gen135_repo:
local_path:
branch:
commit:
para_scaffold:
primary_harness:
challenger_harness:
authority_policy_path:
heritage_manifest_path:
first_income_work_item:
verifier:
effect_gate:
crm_surface:
known_holds:
```

**Var stops here. No Gen-135 scaffold/build effect was performed by Var.**
