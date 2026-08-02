#!/usr/bin/env node
// deploy.mjs — one-command deploy for a factory unit.
//
// Usage (from a per-unit directory that has copied this template):
//   pnpm run deploy TOOL_SLUG SUBDOMAIN
//   pnpm run deploy prompt-versioning-lite prompt-versioning-lite
//
// What it does:
//   1. Reads/updates .placeholder-config.json with TOOL_SLUG / SUBDOMAIN.
//   2. Runs `build.mjs` → dist/.
//   3. Invokes wrangler to create/publish the Cloudflare Pages project
//      named after TOOL_SLUG. First deploy publishes to <slug>.pages.dev;
//      custom-domain wiring (<slug>.<root-domain>) happens in the CF UI.
//   4. Appends a chain-row to ../../state/factory_ships/MICROSAAS_SHIPS.jsonl.
//
// Requires: `wrangler` on PATH and `CLOUDFLARE_API_TOKEN` in env
// (or a logged-in `wrangler login` session).

import { spawn } from 'node:child_process';
import { readFile, writeFile, mkdir } from 'node:fs/promises';
import { existsSync } from 'node:fs';
import { join, resolve } from 'node:path';

const [, , slugArg, subArg] = process.argv;
if (!slugArg) {
  console.error('usage: pnpm run deploy <TOOL_SLUG> [SUBDOMAIN]');
  process.exit(1);
}
const TOOL_SLUG = slugArg;
const SUBDOMAIN = subArg || slugArg;
const ROOT = process.cwd();
const CFG_PATH = join(ROOT, '.placeholder-config.json');
const cfg = existsSync(CFG_PATH) ? JSON.parse(await readFile(CFG_PATH, 'utf8')) : {};
cfg.TOOL_SLUG = TOOL_SLUG;
cfg.SUBDOMAIN = SUBDOMAIN;
cfg.ROOT_DOMAIN = cfg.ROOT_DOMAIN || process.env.ROOT_DOMAIN || 'agentreleasegate.com';
await writeFile(CFG_PATH, JSON.stringify(cfg, null, 2) + '\n');

function run(cmd, args, opts = {}) {
  return new Promise((res, rej) => {
    const p = spawn(cmd, args, { stdio: 'inherit', shell: process.platform === 'win32', ...opts });
    p.on('close', code => code === 0 ? res() : rej(new Error(`${cmd} exited ${code}`)));
  });
}

console.log(`[deploy] building ${TOOL_SLUG}`);
await run(process.execPath, ['scripts/build.mjs']);

console.log(`[deploy] publishing to Cloudflare Pages project: ${TOOL_SLUG}`);
// --project-name creates the project on first run.
await run('wrangler', ['pages', 'deploy', 'dist', '--project-name', TOOL_SLUG, '--branch', 'main']);

// Chain-row the ship. Path is resolved relative to the forge root, walking up
// from the current unit dir: factory/units/<slug>/ → forge root.
const SHIPS_DIR = resolve(ROOT, '..', '..', '..', 'state', 'factory_ships');
await mkdir(SHIPS_DIR, { recursive: true });
const row = {
  schema_id: 'hfo.gen133.microsaas_ship.v0_1',
  event_id: `MICROSAAS_SHIP_${TOOL_SLUG.toUpperCase()}_${new Date().toISOString().replace(/[-:.]/g, '').replace(/T/, 'T').slice(0, 15)}Z`,
  event_type: 'MICROSAAS_UNIT_DEPLOYED',
  ts_utc: new Date().toISOString(),
  tool_slug: TOOL_SLUG,
  subdomain: SUBDOMAIN,
  pages_dev: `https://${TOOL_SLUG}.pages.dev/`,
  custom_domain: `https://${SUBDOMAIN}.${cfg.ROOT_DOMAIN}/`,
  claim_status: 'CLAIMED_UNVERIFIED',
  verification: 'curl the URLs listed above; upgrade to VERIFIED when 5/5 return 200.'
};
const jsonl = JSON.stringify(row) + '\n';
await writeFile(join(SHIPS_DIR, 'MICROSAAS_SHIPS.jsonl'), jsonl, { flag: 'a' });
console.log(`[deploy] ✔ ${TOOL_SLUG} → https://${TOOL_SLUG}.pages.dev/`);
console.log(`[deploy] chain-row appended → state/factory_ships/MICROSAAS_SHIPS.jsonl`);
