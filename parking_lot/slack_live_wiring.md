# PARKED — Slack live wiring for pheromone emit

```yaml
feature: slack_live_wiring
status: PARKED — BLOCKED (B3) + a load-bearing unknown
spec: GEN133_FORMAL_SPEC.md §9 · contracts/pheromone.contract.md
parked_by: SIGRÚN P4 · 2026-07-30
```

## Purpose

The human half of the coordination plane. GitHub is authoritative (PH-1); Slack
is where a human sees the fleet breathing without reading JSONL.

## Why parked

Two separate reasons, and the second is worse than the first.

**1 — Posting to Slack is a `SEND` (B3).** PH-2: writing a pheromone to the repo
is a file write inside the `FILE` ceiling; posting to Slack crosses a trust
boundary and is operator-gated until an explicitly authorized bot identity exists.

**2 — Claude lanes are write-blind on this surface, and possibly read-blind.**
`areas/institution/slack/channels.md` records the observed transport:

```
agent (Codex / ChatGPT desktop) → @ChatGPT bot → Slack channel → other agents read
```

There is no MCP connector a Claude Code lane can call and no OAuth in a
non-interactive session. **The coordination substrate is live and this seat is not
on it.** Huginn on Codex already posts.

If that limit also applies to Claude Dispatch, then **Olrún's primary input
channel is unreadable by her own substrate** — and her entire remit depends on it.
That is `UNDER_SPECIFIED` and unresolved.

## Dependencies

| # | dependency |
|---|---|
| 1 | operator authorizes a bot identity for agent posting (B3) |
| 2 | **the three truncated channel names are confirmed** — `#hfo-command-an…`, `#hfo-resources-ind…`, `#hfo-valkyries-…`. A channel name guessed and written into a protocol doc is the same defect class as a digest quoted instead of computed. |
| 3 | resolve whether Claude Dispatch has a connector Claude Code lacks |
| 4 | if not: a Codex-side relay mirroring Slack pheromones into the GitHub paths |

## When to revisit

After step 2 of the `CANALIZATION.md` dig order — one carrier emitting to GitHub
successfully. GitHub-first is not a workaround; PH-1 makes it the correct
architecture, and Slack is an addition to it.

## Do NOT do

**Do not run the channel-creation script in `SLACK_BOOTSTRAP.md` §3.** It would
add six redundant channels alongside a working roster. That section is superseded
by `channels.md`.
