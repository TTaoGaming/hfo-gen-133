# LOOP-F test vectors

## Vector 1 — happy path (dry-run)

MICROSAAS_SHIPS.jsonl:
```
{"slug":"promptbin","name":"PromptBin","deploy_url":"https://promptbin.pages.dev","icp":"solo AI builders","one_liner":"Save prompts you regret losing"}
```
keywords.json:
```
{"promptbin": ["organize chatgpt prompts"]}
```

Invocation:
```
python factory/loops/seo_content_draft/run.py \
  --units .../MICROSAAS_SHIPS.jsonl --keywords .../keywords.json --dry-run
```

Expected:
- chain row `drafted:promptbin:organize-chatgpt-prompts` wired_with_receipts
- File at `content/blog/promptbin/organize-chatgpt-prompts.md` with
  frontmatter and stub article body
- Checkbox appended to `content/PUBLISH_QUEUE.md`

## Vector 2 — unknown unit

keywords.json references `"ghost-unit": ["kw1"]` but no such slug in ships.

Expected: chain row `skip_unknown_unit:ghost-unit` partial, no file written.

## Vector 3 — idempotency

Run V1 twice.

Expected on second run:
- chain row `skip_exists:promptbin:organize-chatgpt-prompts` proposed
- File NOT overwritten
- No new checkbox in PUBLISH_QUEUE.md (append happens on skip? no — only on drafted)

## Vector 4 — word count out of band

Live LLM call returns 200 words (below MIN_WORDS=500).

Expected: chain row `reject:promptbin:kw` failed with reason `word_count=200 < 500`,
no file staged.

## Vector 5 — LLM missed the landing link

Live LLM returns a valid article but omits the deploy_url.

Expected: pipeline still stages — code appends
`See PromptBin → https://promptbin.pages.dev` before writing.
Verify by grepping the staged file for the URL.
