# seo_content_draft

Per shipped unit, draft one SEO article per target long-tail. Stage in
`content/blog/<unit>/<keyword-slug>.md` for operator to publish weekly.

## One-shot

```powershell
python factory\loops\seo_content_draft\run.py `
  --units state\factory_ships\MICROSAAS_SHIPS.jsonl `
  --keywords content\keywords.json
```

## Mon/Wed/Fri 04:00

```powershell
schtasks /Create /TN "hfo-loop-F-seo-mon" `
  /TR "python C:\Dev\hfo_gen_133_forge\factory\loops\seo_content_draft\run.py --units C:\Dev\hfo_gen_133_forge\state\factory_ships\MICROSAAS_SHIPS.jsonl --keywords C:\Dev\hfo_gen_133_forge\content\keywords.json" `
  /SC WEEKLY /D MON /ST 04:00 /F

schtasks /Create /TN "hfo-loop-F-seo-wed" `
  /TR "python C:\Dev\hfo_gen_133_forge\factory\loops\seo_content_draft\run.py --units C:\Dev\hfo_gen_133_forge\state\factory_ships\MICROSAAS_SHIPS.jsonl --keywords C:\Dev\hfo_gen_133_forge\content\keywords.json" `
  /SC WEEKLY /D WED /ST 04:00 /F

schtasks /Create /TN "hfo-loop-F-seo-fri" `
  /TR "python C:\Dev\hfo_gen_133_forge\factory\loops\seo_content_draft\run.py --units C:\Dev\hfo_gen_133_forge\state\factory_ships\MICROSAAS_SHIPS.jsonl --keywords C:\Dev\hfo_gen_133_forge\content\keywords.json" `
  /SC WEEKLY /D FRI /ST 04:00 /F
```

## Dry-run

```powershell
python factory\loops\seo_content_draft\run.py `
  --units .\ships.jsonl --keywords .\keywords.json --dry-run
```

## Prereqs

- Python 3.11+
- `MICROSAAS_SHIPS.jsonl` populated (LOOP-A runs first)
- `keywords.json` — mapping `{unit_slug: [long_tail, ...]}`
- Optional: `LITELLM_PROXY_URL` for real drafts (falls back to stub otherwise)

## Where things land

- Article: `content/blog/<unit_slug>/<keyword-slug>.md`
- Publish queue: `content/PUBLISH_QUEUE.md`
- Receipts: `state/loop_receipts/seo_content_draft_<YYYYMMDD>.jsonl`
