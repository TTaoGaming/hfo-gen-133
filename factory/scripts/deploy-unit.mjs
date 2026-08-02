#!/usr/bin/env node
// deploy-unit.mjs — build + wrangler deploy + chain-row for one unit.
//
// Usage (from repo root):
//   node factory/scripts/deploy-unit.mjs <slug> [subdomain]
//
// Requires:
//   - `wrangler` on PATH (npm i -g wrangler, or use `npx wrangler`)
//   - CLOUDFLARE_API_TOKEN in env, or a completed `wrangler login`

import { spawn } from 'node:child_process';
import { writeFile, mkdir, readFile } from 'node:fs/promises';
import { existsSync } from 'node:fs';
import { join, dirname, resolve } from 'node:path';
import { fileURLToPath } from 'node:url';

const [, , slug, subArg] = process.argv;
if (!slug) { console.error('usage: deploy-unit <slug> [subdomain]'); process.exit(1); }

const HERE = dirname(fileURLToPath(import.meta.url));
const FACTORY = resolve(HERE, '..');
const REPO = resolve(FACTORY, '..');
const UNIT = join(FACTORY, 'units', slug);
const CFG_PATH = join(UNIT, '.placeholder-config.json');
const cfg = existsSync(CFG_PATH) ? JSON.parse(await readFile(CFG_PATH, 'utf8')) : {};
const SUBDOMAIN = subArg || cfg.SUBDOMAIN || slug;
const ROOT_DOMAIN = cfg.ROOT_DOMAIN || process.env.ROOT_DOMAIN || 'agentreleasegate.com';
cfg.SUBDOMAIN = SUBDOMAIN; cfg.ROOT_DOMAIN = ROOT_DOMAIN;
await writeFile(CFG_PATH, JSON.stringify(cfg, null, 2) + '\n');

function run(cmd, args) {
  return new Promise((res, rej) => {
    const p = spawn(cmd, args, { stdio: 'inherit', shell: process.platform === 'win32' });
    p.on('close', c => c === 0 ? res() : rej(new Error(`${cmd} exited ${c}`)));
  });
}

await run(process.execPath, [join(HERE, 'build-unit.mjs'), slug]);
await run('wrangler', ['pages', 'deploy', join(UNIT, 'dist'),
  '--project-name', slug, '--branch', 'main']);

const SHIPS_DIR = join(REPO, 'state', 'factory_ships');
await mkdir(SHIPS_DIR, { recursive: true });
const now = new Date().toISOString();
const row = {
  schema_id: 'hfo.gen133.microsaas_ship.v0_1',
  event_id: `MICROSAAS_SHIP_${slug.toUpperCase().replace(/-/g, '_')}_${now.replace(/[-:.]/g, '').slice(0, 15)}Z`,
  event_type: 'MICROSAAS_UNIT_DEPLOYED',
  ts_utc: now,
  tool_slug: slug,
  subdomain: SUBDOMAIN,
  root_domain: ROOT_DOMAIN,
  pages_dev: `https://${slug}.pages.dev/`,
  custom_domain: `https://${SUBDOMAIN}.${ROOT_DOMAIN}/`,
  claim_status: 'CLAIMED_UNVERIFIED',
  next_step: 'Verify 5 canonical URLs return 200, then upgrade via log-ship.'
};
await writeFile(join(SHIPS_DIR, 'MICROSAAS_SHIPS.jsonl'),
  JSON.stringify(row) + '\n', { flag: 'a' });
console.log(`[deploy-unit] ✔ ${slug} → https://${slug}.pages.dev/`);
console.log(`[deploy-unit] chain-row appended → state/factory_ships/MICROSAAS_SHIPS.jsonl`);
