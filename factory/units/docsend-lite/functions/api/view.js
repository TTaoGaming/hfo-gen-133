// Cloudflare Pages Function — POST /api/v1/view (analytics beacon).
// Free tier: returns 202, no storage (viewer counts stored client-side).
// Pro tier: operator binds env.DOCSEND_KV Tuesday, we start writing rollups.
//
// Contract:
//   POST /api/v1/view
//   Body: { docId, ts, event: 'open'|'page_view', page?, elapsed_ms?, pages_total? }
//   Response: 202 (accepted)

export const onRequestPost = async ({ request, env }) => {
  let payload;
  try { payload = await request.json(); }
  catch { return new Response('bad json', { status: 400 }); }

  const now = new Date().toISOString();
  const docId = String(payload.docId || 'unknown').slice(0, 32);
  const event = String(payload.event || '').slice(0, 16);

  // Free tier — no KV bound. Log to Cloudflare's console for spot-check.
  if (!env.DOCSEND_KV) {
    console.log('[view]', now, docId, event, payload.page || '');
    return new Response(null, { status: 202 });
  }

  // Pro tier — write to KV.
  const key = `doc:${docId}:events`;
  const existing = (await env.DOCSEND_KV.get(key, { type: 'json' })) || [];
  existing.push({ ts: now, event, page: payload.page || null, elapsed_ms: payload.elapsed_ms || null });
  // Cap at 1000 events per doc to keep KV values small.
  const trimmed = existing.slice(-1000);
  await env.DOCSEND_KV.put(key, JSON.stringify(trimmed));

  return new Response(null, { status: 202 });
};

export const onRequestOptions = () => new Response(null, {
  status: 204,
  headers: {
    'access-control-allow-origin': '*',
    'access-control-allow-methods': 'POST, OPTIONS',
    'access-control-allow-headers': 'content-type'
  }
});
