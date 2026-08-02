# License Verification Report

Verified 2026-08-02 from current upstream root license bytes and, for selected bases, from each local fork's checked-out `LICENSE` file.

## Used bases

| Repository | Commit used | Root-license readback | Decision |
|---|---|---|---|
| Activepieces | `8d29bbe6fdd572b15398adc67dff74b2e30d3a3d` | Split license: content outside `packages/ee/` and `packages/server/api/src/app/ee` is MIT; enterprise paths have separate terms | **USED_CORE_ONLY** - no enterprise path added or materialized for this batch |
| Cal.com | `038381aeca6261635357957d66b8ba85cdb29737` | MIT License | **USED** - this corrects the intake note that classified current Cal.com as AGPL |
| Trigger.dev | `8f66af6e18b73ceaf4a8c2d198bb662a7bb85202` | Apache License 2.0 | **USED** |

## Skipped bases

| Repository | Current root-license evidence | Decision |
|---|---|---|
| Papermark | AGPLv3 for content outside separately commercial enterprise paths | **AGPL_SKIPPED** |
| Documenso | GNU Affero General Public License v3 | **AGPL_SKIPPED** |
| Twenty CRM | Mostly AGPLv3, with marked commercial files and specific MIT packages | **AGPL_SKIPPED** |
| Formbricks | AGPLv3 core, with specified MIT client/API packages and separate enterprise terms | **AGPL_SKIPPED** |

No legal opinion is asserted. This report applies the operator's conservative rule: skip an AGPL-root application unless explicitly permitted. The landing pages are original static offer pages and do not ship code from the skipped repositories.
