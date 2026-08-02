#!/usr/bin/env node
// log-ship.mjs — append a manual chain-row without redeploying.
// Use when you've verified URLs and want to upgrade claim_status to VERIFIED.
//
// Usage:
//   node scripts/log-ship.mjs <TOOL_SLUG> VERIFIED "5/5 curl 200"

import { writeFile, mkdir } from 'node:fs/promises';
import { resolve } from 'node:path';

const [, , slug, status = 'CLAIMED_UNVERIFIED', note = ''] = process.argv;
if (!slug) { console.error('usage: log-ship <slug> [status] [note]'); process.exit(1); }

const SHIPS_DIR = resolve(process.cwd(), '..', '..', '..', 'state', 'factory_ships');
await mkdir(SHIPS_DIR, { recursive: true });
const row = {
  schema_id: 'hfo.gen133.microsaas_ship.v0_1',
  event_type: 'MICROSAAS_UNIT_STATUS_UPDATE',
  ts_utc: new Date().toISOString(),
  tool_slug: slug,
  claim_status: status,
  note
};
await writeFile(resolve(SHIPS_DIR, 'MICROSAAS_SHIPS.jsonl'), JSON.stringify(row) + '\n', { flag: 'a' });
console.log(`[log-ship] appended ${status} for ${slug}`);
