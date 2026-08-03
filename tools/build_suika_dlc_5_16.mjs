#!/usr/bin/env node
import { mkdirSync, readFileSync, writeFileSync } from 'node:fs';
import path from 'node:path';

const root = path.resolve('outputs/staged_sends/games');
const variants = [
  { n: 5, slug: 'timer-mode', mechanic: 'timer_mode', title: 'Blitz Orchard', description: 'Three minutes. Merge fast and chase the high score.', controls: 'The clock starts when play begins.' },
  { n: 6, slug: 'gravity-flip', mechanic: 'gravity_flip', title: 'Gravity Reversal', description: 'Invert gravity for five seconds, then survive the thirty-second cooldown.', controls: 'Press SPACE to flip gravity.' },
  { n: 7, slug: 'boss-fruits', mechanic: 'boss_fruits', title: 'Boss Harvest', description: 'Every thirty merges summons a boss fruit. Feed it three matching fruits to clear it.', controls: 'Build thirty merges, then hit the boss three times.' },
  { n: 8, slug: 'character-select', mechanic: 'character_select', title: 'Three Heroes', description: 'Choose an auto-merger, a fruit reaper, or a wildcard trickster.', controls: 'Press 1, 2, or 3 to choose a hero.' },
  { n: 9, slug: 'daily-seed', mechanic: 'daily_seed', title: 'Daily Orchard', description: 'Everyone gets the same date-seeded fruit sequence and a shareable score link.', controls: 'A new deterministic seed arrives each UTC day.' },
  { n: 10, slug: 'combo-burst', mechanic: 'combo_burst', title: 'Combo Burst', description: 'Five merges inside three seconds clear every bottom-tier fruit.', controls: 'Chain five merges before the combo window closes.' },
  { n: 11, slug: 'reverse-suika', mechanic: 'reverse_suika', title: 'Reverse Suika', description: 'Start with giant fruit; matching giants split into smaller tiers.', controls: 'Merge downward until the pot is full of tiny fruit.' },
  { n: 12, slug: 'gauntlet-mode', mechanic: 'gauntlet_mode', title: 'Falling Gauntlet', description: 'Automatic drops accelerate until the orchard becomes a storm.', controls: 'Place fruit between increasingly fast automatic drops.' },
  { n: 13, slug: 'joker-draft', mechanic: 'joker_draft', title: 'Joker Orchard', description: 'Draft a scoring Joker every ten merges, inspired by Balatro.', controls: 'When a draft opens, press 1, 2, or 3.' },
  { n: 14, slug: 'relic-stance', mechanic: 'relic_stance', title: 'Relic Stances', description: 'Slay-style relic stances trade safety, gravity, and score.', controls: 'Press 1 for Anchor, 2 for Glass, or 3 for Feather.' },
  { n: 15, slug: 'evolution-charge', mechanic: 'evolution_charge', title: 'Evolution Charge', description: 'Charge an evolution with ten merges, then empower the next drop.', controls: 'Every tenth merge evolves the next fruit by two tiers.' },
  { n: 16, slug: 'bounty-hunt', mechanic: 'bounty_hunt', title: 'Tier Bounties', description: 'Hunt a rotating target tier for bonus points and a new bounty.', controls: 'Merge the highlighted tier to claim the bounty.' },
];

const GAME_TEMPLATE = String.raw`/* SUIKA_MECHANIC_HOOK:__MECHANIC__ */
(function (root, factory) {
  const api = factory();
  if (typeof module !== 'undefined' && module.exports) module.exports = api;
  if (root) root.SuikaMechanic = api;
  if (typeof window !== 'undefined' && typeof Game !== 'undefined') {
    api.install({ Game, engine, render, Composite, Bodies, Events, GameStates });
  }
})(typeof globalThis !== 'undefined' ? globalThis : this, function () {
  'use strict';
  const config = __CONFIG__;
  const state = {};

  function daySeed(dateText) {
    let h = 2166136261 >>> 0;
    for (const c of String(dateText)) {
      h ^= c.charCodeAt(0);
      h = Math.imul(h, 16777619) >>> 0;
    }
    return h >>> 0;
  }

  function seededStep(seed) {
    let t = (seed + 0x6D2B79F5) >>> 0;
    t = Math.imul(t ^ (t >>> 15), t | 1);
    t ^= t + Math.imul(t ^ (t >>> 7), t | 61);
    return { seed: (seed + 0x6D2B79F5) >>> 0, value: ((t ^ (t >>> 14)) >>> 0) / 4294967296 };
  }

  function snapshot() { return JSON.parse(JSON.stringify(state)); }

  function reset(options) {
    const o = options || {};
    for (const key of Object.keys(state)) delete state[key];
    Object.assign(state, {
      started: false,
      nowMs: Number(o.nowMs || 0),
      bonusScore: 0,
      merges: 0,
      drops: 0,
      remainingMs: 180000,
      expired: false,
      gravity: 1,
      flipUntil: 0,
      cooldownUntil: 0,
      boss: null,
      character: 'auto',
      date: o.date || new Date(Number(o.nowMs || Date.now())).toISOString().slice(0, 10),
      rngState: 0,
      comboTimes: [],
      bursts: 0,
      intervalMs: 4000,
      selectedJokers: [],
      draftChoices: [],
      relic: 'anchor',
      evolutionCharge: 0,
      evolvedReady: false,
      bountyTier: 0,
      bountyClaims: 0,
    });
    state.rngState = daySeed(state.date);
    return snapshot();
  }

  function transition(type, payload) {
    const p = payload || {};
    const effect = {};
    if (Number.isFinite(p.nowMs)) state.nowMs = p.nowMs;

    switch (config.mechanic) {
      case 'timer_mode':
        if (type === 'start') state.started = true;
        if (type === 'tick' && !state.expired) {
          state.remainingMs = Math.max(0, state.remainingMs - Math.max(0, Number(p.deltaMs || 0)));
          if (state.remainingMs === 0) { state.expired = true; effect.gameOver = true; }
        }
        break;

      case 'gravity_flip':
        if (type === 'key' && (p.key === ' ' || p.key === 'Space') && state.nowMs >= state.cooldownUntil) {
          state.gravity = -1;
          state.flipUntil = state.nowMs + 5000;
          state.cooldownUntil = state.nowMs + 30000;
          effect.gravityY = -1;
        }
        if (type === 'tick' && state.gravity < 0 && state.nowMs >= state.flipUntil) {
          state.gravity = 1;
          effect.gravityY = 1;
        }
        break;

      case 'boss_fruits':
        if (type === 'merge') {
          state.merges += 1;
          if (state.merges % 30 === 0 && !state.boss) {
            state.boss = { tier: Number.isInteger(p.tier) ? Math.min(p.tier, 4) : 0, hits: 0, required: 3 };
            effect.spawnBoss = { ...state.boss };
          }
        }
        if (type === 'boss_hit' && state.boss && p.tier === state.boss.tier) {
          state.boss.hits += 1;
          if (state.boss.hits >= state.boss.required) {
            effect.clearBoss = true;
            effect.scoreBonus = 100;
            state.bonusScore += 100;
            state.boss = null;
          }
        }
        break;

      case 'character_select': {
        const chars = ['auto', 'reaper', 'wildcard'];
        if (type === 'select' && chars.includes(p.character)) state.character = p.character;
        if (type === 'drop') {
          state.drops += 1;
          if (state.drops % 6 === 0) {
            if (state.character === 'auto') effect.autoMerge = true;
            if (state.character === 'reaper') effect.deleteOne = true;
            if (state.character === 'wildcard') effect.wildcard = true;
          }
        }
        break;
      }

      case 'daily_seed':
        if (type === 'next') {
          const step = seededStep(state.rngState);
          state.rngState = step.seed;
          effect.tier = Math.floor(step.value * 5);
        }
        if (type === 'share') {
          const base = String(p.baseUrl || 'https://example.invalid/').split('?')[0];
          effect.shareUrl = base + '?date=' + encodeURIComponent(state.date) + '&score=' + Math.max(0, Number(p.score || 0));
        }
        break;

      case 'combo_burst':
        if (type === 'merge') {
          const t = Number(p.nowMs || state.nowMs || 0);
          state.comboTimes = state.comboTimes.filter(x => t - x <= 3000);
          state.comboTimes.push(t);
          if (state.comboTimes.length >= 5) {
            state.comboTimes = [];
            state.bursts += 1;
            effect.clearTier = 0;
            effect.scoreBonus = 50;
            state.bonusScore += 50;
          }
        }
        break;

      case 'reverse_suika':
        if (type === 'next') {
          const tiers = [8, 9, 10];
          effect.tier = tiers[state.drops % tiers.length];
          state.drops += 1;
        }
        break;

      case 'gauntlet_mode':
        if (type === 'start') { state.started = true; state.startedAt = Number(p.nowMs || 0); }
        if (type === 'tick') {
          const elapsed = Math.max(0, Number(p.elapsedMs || 0));
          state.intervalMs = Math.max(800, 4000 - Math.floor(elapsed / 10000) * 250);
          effect.intervalMs = state.intervalMs;
        }
        if (type === 'auto_drop') { state.drops += 1; effect.autoDrop = true; }
        break;

      case 'joker_draft':
        if (type === 'merge') {
          state.merges += 1;
          if (state.merges % 10 === 0) {
            state.draftChoices = ['pair-bonus', 'odd-bonus', 'flat-five'];
            effect.draft = state.draftChoices.slice();
          }
          let bonus = 0;
          if (state.selectedJokers.includes('pair-bonus') && Number(p.tier || 0) % 2 === 0) bonus += 10;
          if (state.selectedJokers.includes('odd-bonus') && Number(p.tier || 0) % 2 === 1) bonus += 10;
          if (state.selectedJokers.includes('flat-five')) bonus += 5;
          state.bonusScore += bonus;
          effect.scoreBonus = bonus;
        }
        if (type === 'choose' && state.draftChoices.includes(p.joker)) {
          state.selectedJokers.push(p.joker);
          state.draftChoices = [];
          effect.selected = p.joker;
        }
        break;

      case 'relic_stance': {
        const relics = {
          anchor: { gravityY: 1.35, scoreBonus: 0, tierBoost: 0 },
          glass: { gravityY: 1.0, scoreBonus: 8, tierBoost: 1 },
          feather: { gravityY: 0.55, scoreBonus: 2, tierBoost: 0 },
        };
        if (type === 'select' && relics[p.relic]) state.relic = p.relic;
        if (type === 'select') Object.assign(effect, relics[state.relic]);
        if (type === 'merge') {
          const r = relics[state.relic];
          state.bonusScore += r.scoreBonus;
          effect.scoreBonus = r.scoreBonus;
        }
        if (type === 'drop') effect.tierBoost = relics[state.relic].tierBoost;
        break;
      }

      case 'evolution_charge':
        if (type === 'merge') {
          state.evolutionCharge = Math.min(10, state.evolutionCharge + 1);
          if (state.evolutionCharge === 10) state.evolvedReady = true;
        }
        if (type === 'drop' && state.evolvedReady) {
          effect.tierBoost = 2;
          state.evolvedReady = false;
          state.evolutionCharge = 0;
        }
        break;

      case 'bounty_hunt':
        if (type === 'merge') {
          state.merges += 1;
          if (Number(p.tier) === state.bountyTier) {
            state.bountyClaims += 1;
            state.bonusScore += 25;
            effect.scoreBonus = 25;
            state.bountyTier = (state.bountyTier + 1 + (state.bountyClaims % 3)) % 6;
            effect.nextBountyTier = state.bountyTier;
          }
        }
        break;
    }
    return effect;
  }

  function resolveMergeSize(sizeIndex) {
    return config.mechanic === 'reverse_suika' ? Math.max(0, Number(sizeIndex) - 1) : Number(sizeIndex) + 1;
  }

  function statusText() {
    switch (config.mechanic) {
      case 'timer_mode': return 'TIME ' + Math.ceil(state.remainingMs / 1000) + 's';
      case 'gravity_flip': return state.gravity < 0 ? 'GRAVITY UP' : 'FLIP ' + Math.max(0, Math.ceil((state.cooldownUntil - state.nowMs) / 1000)) + 's';
      case 'boss_fruits': return state.boss ? 'BOSS ' + state.boss.hits + '/3' : 'BOSS IN ' + (30 - (state.merges % 30)) + ' MERGES';
      case 'character_select': return 'HERO ' + state.character.toUpperCase() + ' · PASSIVE IN ' + (6 - (state.drops % 6));
      case 'daily_seed': return 'DAILY ' + state.date;
      case 'combo_burst': return 'COMBO ' + state.comboTimes.length + '/5 · BURSTS ' + state.bursts;
      case 'reverse_suika': return 'BIG → SMALL';
      case 'gauntlet_mode': return 'AUTO DROP ' + (state.intervalMs / 1000).toFixed(2) + 's';
      case 'joker_draft': return state.draftChoices.length ? 'DRAFT: PRESS 1 / 2 / 3' : 'JOKERS ' + state.selectedJokers.length + ' · NEXT ' + (10 - (state.merges % 10));
      case 'relic_stance': return 'RELIC ' + state.relic.toUpperCase();
      case 'evolution_charge': return state.evolvedReady ? 'EVOLVED DROP READY' : 'EVOLUTION ' + state.evolutionCharge + '/10';
      case 'bounty_hunt': return 'BOUNTY TIER ' + state.bountyTier + ' · CLAIMS ' + state.bountyClaims;
      default: return config.mechanic;
    }
  }

  function install(ctx) {
    const { Game, engine, render, Composite, Bodies, Events, GameStates } = ctx;
    reset({ nowMs: Date.now() });
    Game.dlc = api;

    const hud = document.createElement('section');
    hud.id = 'mechanic-status';
    hud.dataset.mechanicHook = config.mechanic;
    hud.style.cssText = 'position:absolute;z-index:20;top:8px;left:8px;right:8px;padding:9px 12px;border:2px solid #fff8;background:#111d;color:#fff;font:700 13px/1.35 monospace;pointer-events:none;border-radius:10px;text-shadow:1px 1px #000';
    hud.innerHTML = '<strong>' + config.title + '</strong><br><span id="mechanic-live"></span><br><small>' + config.controls + '</small>';
    Game.elements.canvas.appendChild(hud);
    const live = hud.querySelector('#mechanic-live');

    const baseCalculateScore = Game.calculateScore.bind(Game);
    Game.calculateScore = function () {
      baseCalculateScore();
      Game.score += state.bonusScore;
      Game.elements.score.innerText = Game.score;
    };

    const baseSetNext = Game.setNextFruitSize.bind(Game);
    Game.setNextFruitSize = function () {
      if (config.mechanic === 'daily_seed' || config.mechanic === 'reverse_suika') {
        const e = transition('next', { nowMs: Date.now() });
        Game.nextFruitSize = e.tier;
        Game.elements.nextFruitImg.src = './assets/img/circle' + Game.nextFruitSize + '.png';
      } else baseSetNext();
    };

    const dynamicBodies = () => Composite.allBodies(engine.world).filter(b => !b.isStatic && !b.popped && !b.isBoss);
    const removeTier = tier => Composite.remove(engine.world, dynamicBodies().filter(b => b.sizeIndex === tier));
    const removeOne = () => {
      const bodies = dynamicBodies().sort((a, b) => a.sizeIndex - b.sizeIndex);
      if (bodies[0]) { bodies[0].popped = true; Composite.remove(engine.world, bodies[0]); }
    };

    function apply(effect, meta) {
      if (!effect) return;
      if (Number.isFinite(effect.gravityY)) engine.gravity.y = effect.gravityY;
      if (Number.isInteger(effect.clearTier)) removeTier(effect.clearTier);
      if (effect.deleteOne) removeOne();
      if (effect.autoMerge) {
        const tier = Number(meta && meta.tier || 0);
        Composite.add(engine.world, Game.generateFruitBody(Number(meta && meta.x || Game.width / 2) + 3, 42, tier));
      }
      if (effect.spawnBoss) {
        const boss = Bodies.circle(Game.width / 2, 180, 52, { restitution: 0.4, render: { fillStyle: '#5c1b8f', strokeStyle: '#fff', lineWidth: 5 } });
        boss.isBoss = true; boss.bossTier = effect.spawnBoss.tier; boss.sizeIndex = 99; boss.popped = false;
        state.bossBodyId = boss.id;
        Composite.add(engine.world, boss);
      }
      if (effect.clearBoss && state.bossBodyId) {
        const boss = Composite.allBodies(engine.world).find(b => b.id === state.bossBodyId);
        if (boss) Composite.remove(engine.world, boss);
        state.bossBodyId = null;
      }
      if (effect.gameOver && Game.stateIndex !== GameStates.LOSE) Game.loseGame();
      Game.calculateScore();
    }

    const baseAddFruit = Game.addFruit.bind(Game);
    Game.addFruit = function (x) {
      if (Game.stateIndex !== GameStates.READY) return baseAddFruit(x);
      const originalTier = Game.currentFruitSize;
      const pre = transition('drop', { nowMs: Date.now(), tier: originalTier, x });
      if (pre.wildcard) {
        const candidate = dynamicBodies()[0];
        if (candidate) Game.currentFruitSize = candidate.sizeIndex;
      }
      if (Number.isInteger(pre.tierBoost)) Game.currentFruitSize = Math.min(10, Game.currentFruitSize + pre.tierBoost);
      const droppedTier = Game.currentFruitSize;
      const result = baseAddFruit(x);
      apply(pre, { x, tier: droppedTier });
      return result;
    };

    const baseStartGame = Game.startGame.bind(Game);
    Game.startGame = function () {
      reset({ nowMs: Date.now(), date: new Date().toISOString().slice(0, 10) });
      transition('start', { nowMs: Date.now() });
      if (config.mechanic === 'reverse_suika' || config.mechanic === 'daily_seed') {
        Game.setNextFruitSize(); Game.currentFruitSize = Game.nextFruitSize; Game.setNextFruitSize();
      }
      return baseStartGame();
    };

    Events.on(engine, 'collisionStart', function (event) {
      for (const pair of event.pairs) {
        const a = pair.bodyA, b = pair.bodyB;
        const boss = a.isBoss ? a : (b.isBoss ? b : null);
        const fruit = boss === a ? b : a;
        if (boss && fruit && !fruit.isStatic && !fruit.popped && fruit.sizeIndex === boss.bossTier) {
          fruit.popped = true;
          Composite.remove(engine.world, fruit);
          apply(transition('boss_hit', { tier: fruit.sizeIndex, nowMs: Date.now() }));
          continue;
        }
        if (!a.isStatic && !b.isStatic && !a.isBoss && !b.isBoss && a.sizeIndex === b.sizeIndex && (a.popped || b.popped)) {
          apply(transition('merge', { tier: a.sizeIndex, nowMs: Date.now() }));
        }
      }
    });

    document.addEventListener('keydown', function (event) {
      let effect = null;
      if (config.mechanic === 'gravity_flip' && (event.code === 'Space' || event.key === ' ')) {
        event.preventDefault(); effect = transition('key', { key: 'Space', nowMs: Date.now() });
      }
      if (config.mechanic === 'character_select' && ['1', '2', '3'].includes(event.key)) {
        effect = transition('select', { character: ['auto', 'reaper', 'wildcard'][Number(event.key) - 1] });
      }
      if (config.mechanic === 'joker_draft' && ['1', '2', '3'].includes(event.key) && state.draftChoices.length) {
        effect = transition('choose', { joker: state.draftChoices[Number(event.key) - 1] });
      }
      if (config.mechanic === 'relic_stance' && ['1', '2', '3'].includes(event.key)) {
        effect = transition('select', { relic: ['anchor', 'glass', 'feather'][Number(event.key) - 1] });
      }
      apply(effect);
    });

    let lastTick = Date.now();
    let nextAutoDrop = lastTick + state.intervalMs;
    setInterval(function () {
      const now = Date.now();
      const delta = now - lastTick;
      lastTick = now;
      const tick = transition('tick', { nowMs: now, deltaMs: delta, elapsedMs: state.startedAt ? now - state.startedAt : 0 });
      apply(tick);
      if (config.mechanic === 'gauntlet_mode' && Game.stateIndex === GameStates.READY && now >= nextAutoDrop) {
        transition('auto_drop', { nowMs: now });
        Game.addFruit(80 + Math.random() * (Game.width - 160));
        nextAutoDrop = now + state.intervalMs;
      }
      if (config.mechanic === 'daily_seed') {
        const share = transition('share', { score: Game.score, baseUrl: location.href });
        live.innerHTML = statusText() + ' · <a style="color:#ffd166;pointer-events:auto" href="' + share.shareUrl + '">share score</a>';
      } else live.textContent = statusText();
    }, 250);
  }

  const api = {
    variantId: config.n,
    variant: config.n,
    slug: config.slug,
    mechanic: config.mechanic,
    theme: config.slug,
    marker: 'SUIKA_MECHANIC_HOOK:' + config.mechanic,
    title: config.title,
    description: config.description,
    controls: config.controls,
    state,
    reset,
    transition,
    resolveMergeSize,
    handlesMergeWrap: config.mechanic === 'reverse_suika',
    statusText,
    daySeed,
    seededStep,
    install,
  };
  reset({ nowMs: 0, date: '2026-08-02' });
  return api;
});
`;

function testBody(v) {
  const prelude = `import test from 'node:test';\nimport assert from 'node:assert/strict';\nimport { createRequire } from 'node:module';\nconst require = createRequire(import.meta.url);\nconst M = require('../game.js');\n\ntest('variant metadata binds the mechanic', () => {\n  assert.equal(M.variantId, ${v.n});\n  assert.equal(M.mechanic, '${v.mechanic}');\n  assert.match(M.marker, /${v.mechanic}/);\n});\n\n`;
  const bodies = {
    timer_mode: `test('timer decrements and expires at three minutes', () => {\n  M.reset({ nowMs: 0 });\n  M.transition('start', { nowMs: 0 });\n  M.transition('tick', { deltaMs: 1000, nowMs: 1000 });\n  assert.equal(M.state.remainingMs, 179000);\n  const effect = M.transition('tick', { deltaMs: 179000, nowMs: 180000 });\n  assert.equal(M.state.expired, true);\n  assert.equal(effect.gameOver, true);\n});\n`,
    gravity_flip: `test('SPACE flips gravity for five seconds and enforces cooldown', () => {\n  M.reset({ nowMs: 0 });\n  assert.equal(M.transition('key', { key: 'Space', nowMs: 0 }).gravityY, -1);\n  assert.equal(M.state.gravity, -1);\n  assert.equal(M.transition('key', { key: 'Space', nowMs: 1000 }).gravityY, undefined);\n  assert.equal(M.transition('tick', { nowMs: 5000 }).gravityY, 1);\n  assert.equal(M.transition('key', { key: 'Space', nowMs: 30000 }).gravityY, -1);\n});\n`,
    boss_fruits: `test('the thirtieth merge spawns a three-hit boss', () => {\n  M.reset({ nowMs: 0 });\n  for (let i = 1; i < 30; i++) assert.equal(M.transition('merge', { tier: 0 }).spawnBoss, undefined);\n  assert.equal(M.transition('merge', { tier: 0 }).spawnBoss.required, 3);\n  assert.equal(M.transition('boss_hit', { tier: 0 }).clearBoss, undefined);\n  assert.equal(M.transition('boss_hit', { tier: 0 }).clearBoss, undefined);\n  const cleared = M.transition('boss_hit', { tier: 0 });\n  assert.equal(cleared.clearBoss, true);\n  assert.equal(M.state.boss, null);\n});\n`,
    character_select: `test('three characters expose distinct sixth-drop passives', () => {\n  for (const [character, key] of [['auto','autoMerge'], ['reaper','deleteOne'], ['wildcard','wildcard']]) {\n    M.reset({ nowMs: 0 });\n    M.transition('select', { character });\n    let effect; for (let i = 0; i < 6; i++) effect = M.transition('drop', {});\n    assert.equal(effect[key], true, character);\n  }\n});\n`,
    daily_seed: `test('same UTC date produces the same sequence and share URL', () => {\n  const sequence = date => { M.reset({ date, nowMs: 0 }); return Array.from({ length: 8 }, () => M.transition('next').tier); };\n  assert.deepEqual(sequence('2026-08-02'), sequence('2026-08-02'));\n  assert.notDeepEqual(sequence('2026-08-02'), sequence('2026-08-03'));\n  M.reset({ date: '2026-08-02', nowMs: 0 });\n  assert.equal(M.transition('share', { baseUrl: 'https://game.example/', score: 42 }).shareUrl, 'https://game.example/?date=2026-08-02&score=42');\n});\n`,
    combo_burst: `test('five merges within three seconds fire a bottom-tier burst', () => {\n  M.reset({ nowMs: 0 });\n  let effect; for (let i = 0; i < 5; i++) effect = M.transition('merge', { nowMs: i * 500 });\n  assert.equal(effect.clearTier, 0);\n  assert.equal(M.state.bursts, 1);\n  M.reset({ nowMs: 0 });\n  for (let i = 0; i < 5; i++) effect = M.transition('merge', { nowMs: i * 4000 });\n  assert.equal(effect.clearTier, undefined);\n});\n`,
    reverse_suika: `test('drops start large and merges split downward', () => {\n  M.reset({ nowMs: 0 });\n  assert.deepEqual([M.transition('next').tier, M.transition('next').tier, M.transition('next').tier], [8, 9, 10]);\n  assert.equal(M.resolveMergeSize(9), 8);\n  assert.equal(M.resolveMergeSize(1), 0);\n  assert.equal(M.resolveMergeSize(0), 0);\n});\n`,
    gauntlet_mode: `test('automatic drop interval accelerates to a safe floor', () => {\n  M.reset({ nowMs: 0 }); M.transition('start', { nowMs: 0 });\n  assert.equal(M.transition('tick', { elapsedMs: 20000 }).intervalMs, 3500);\n  assert.equal(M.transition('tick', { elapsedMs: 999999 }).intervalMs, 800);\n  assert.equal(M.transition('auto_drop').autoDrop, true);\n  assert.equal(M.state.drops, 1);\n});\n`,
    joker_draft: `test('ten merges open a three-Joker draft and choice affects scoring', () => {\n  M.reset({ nowMs: 0 });\n  let effect; for (let i = 0; i < 10; i++) effect = M.transition('merge', { tier: 0 });\n  assert.deepEqual(effect.draft, ['pair-bonus', 'odd-bonus', 'flat-five']);\n  M.transition('choose', { joker: 'pair-bonus' });\n  effect = M.transition('merge', { tier: 2 });\n  assert.equal(effect.scoreBonus, 10);\n});\n`,
    relic_stance: `test('relic choices have distinct upside/downside state effects', () => {\n  M.reset({ nowMs: 0 });\n  assert.equal(M.transition('select', { relic: 'anchor' }).gravityY, 1.35);\n  assert.equal(M.transition('select', { relic: 'glass' }).tierBoost, 1);\n  assert.equal(M.transition('merge', { tier: 0 }).scoreBonus, 8);\n  assert.equal(M.transition('select', { relic: 'feather' }).gravityY, 0.55);\n});\n`,
    evolution_charge: `test('ten merges evolve exactly the next drop by two tiers', () => {\n  M.reset({ nowMs: 0 });\n  for (let i = 0; i < 10; i++) M.transition('merge', { tier: 0 });\n  assert.equal(M.state.evolvedReady, true);\n  assert.equal(M.transition('drop', { tier: 1 }).tierBoost, 2);\n  assert.equal(M.state.evolvedReady, false);\n  assert.equal(M.transition('drop', { tier: 1 }).tierBoost, undefined);\n});\n`,
    bounty_hunt: `test('only the highlighted tier claims a bounty and rotates the target', () => {\n  M.reset({ nowMs: 0 });\n  assert.equal(M.transition('merge', { tier: 1 }).scoreBonus, undefined);\n  const hit = M.transition('merge', { tier: 0 });\n  assert.equal(hit.scoreBonus, 25);\n  assert.equal(M.state.bountyClaims, 1);\n  assert.notEqual(M.state.bountyTier, 0);\n});\n`,
  };
  return prelude + bodies[v.mechanic];
}

function patchIndexHtml(source, v) {
  if (source.includes(`data-mechanic-hook="${v.mechanic}"`) && source.includes('./game.js?v=1')) return source;
  if (source.includes('data-mechanic-hook=')) throw new Error('index.html already modified for another mechanic: ' + v.n);
  let out = source.replace('<title>Suika / Watermelon Game Clone</title>', `<title>${v.title} · HFO Suika DLC ${v.n}</title>\n  <meta name="description" content="${v.description}" />\n  <meta name="suika-mechanic" content="${v.mechanic}" />`);
  out = out.replace('<body>', `<body data-mechanic-hook="${v.mechanic}">\n  <h1 style="position:absolute;left:-9999px">${v.title} Suika</h1>`);
  out = out.replace('  <script type="text/javascript" src="./index.js?v=4"></script>', '  <script type="text/javascript" src="./index.js?v=4"></script>\n  <script type="text/javascript" src="./game.js?v=1"></script>');
  if (!out.includes('./game.js?v=1')) throw new Error('index.html script marker not found for ' + v.n);
  return out;
}

function patchIndexJs(source, v) {
  source = source.replace(/\r\n/g, '\n');
  const oldBlock = `\t\t\t\tlet newSize = bodyA.sizeIndex + 1;\n\n\t\t\t\t// Go back to smallest size\n\t\t\t\tif (bodyA.circleRadius >= Game.fruitSizes[Game.fruitSizes.length - 1].radius) {\n\t\t\t\t\tnewSize = 0;\n\t\t\t\t}`;
  const newBlock = `\t\t\t\tlet newSize = Game.dlc && typeof Game.dlc.resolveMergeSize === 'function'\n\t\t\t\t\t? Game.dlc.resolveMergeSize(bodyA.sizeIndex)\n\t\t\t\t\t: bodyA.sizeIndex + 1;\n\n\t\t\t\t// Default mode wraps the largest fruit. Reverse mode owns its merge boundary.\n\t\t\t\tif (!(Game.dlc && Game.dlc.handlesMergeWrap) && bodyA.circleRadius >= Game.fruitSizes[Game.fruitSizes.length - 1].radius) {\n\t\t\t\t\tnewSize = 0;\n\t\t\t\t}`;
  if (!source.includes(oldBlock)) throw new Error('merge block not found for ' + v.n);
  return source.replace(oldBlock, newBlock);
}

for (const v of variants) {
  const dir = path.join(root, `suika_dlc_${v.n}_${v.slug}`);
  const indexHtmlPath = path.join(dir, 'index.html');
  const indexJsPath = path.join(dir, 'index.js');
  const indexHtml = readFileSync(indexHtmlPath, 'utf8');
  const indexJs = readFileSync(indexJsPath, 'utf8');
  const gameJs = GAME_TEMPLATE
    .replace('__MECHANIC__', v.mechanic)
    .replace('__CONFIG__', JSON.stringify(v));

  writeFileSync(indexHtmlPath, patchIndexHtml(indexHtml, v));
  writeFileSync(indexJsPath, patchIndexJs(indexJs, v));
  writeFileSync(path.join(dir, 'game.js'), gameJs);
  writeFileSync(path.join(dir, 'package.json'), JSON.stringify({
    name: `hfo-suika-dlc-${v.n}-${v.slug}`,
    version: '1.0.0',
    private: true,
    description: v.description,
    license: 'Unlicense',
    scripts: { test: 'node --test test/mechanic.test.mjs' },
  }, null, 2) + '\n');
  mkdirSync(path.join(dir, 'test'), { recursive: true });
  writeFileSync(path.join(dir, 'test', 'mechanic.test.mjs'), testBody(v));
  writeFileSync(path.join(dir, 'README.md'), `# ${v.title}\n\nSuika DLC ${v.n}: **${v.mechanic}**. ${v.description}\n\nControls: ${v.controls}\n\n- Upstream: moonfloof/suika-game at c30848ed79f7c23e54a89e3e58a993b4fd991d14\n- License: Unlicense (public domain)\n- Test: \`npm test\`\n- Deploy project: \`hfo-suika-dlc-${v.n}-${v.slug}\`\n`);
  console.log(`built ${v.n} ${v.mechanic} -> ${path.basename(dir)}`);
}
