// Cloudflare Pages Function stub — Pro-tier /api/v1/events endpoint.
// Operator wires D1 + bearer-token auth Tuesday. Until then this returns 501
// and the free tier (localStorage) covers 100% of MVP need.
//
// Contract (documented in FAQ + README):
//   POST /api/v1/events
//   Authorization: Bearer <workspace_token>
//   Content-Type: application/json
//   Body: { agent, model, input_tokens, output_tokens, ts?, meta? }
//   Response: { id, cost_usd, ts }

export const onRequest = async (ctx) => {
  const { request } = ctx;
  if (request.method === 'OPTIONS') {
    return new Response(null, {
      status: 204,
      headers: {
        'access-control-allow-origin': '*',
        'access-control-allow-methods': 'POST, OPTIONS',
        'access-control-allow-headers': 'authorization, content-type'
      }
    });
  }
  if (request.method !== 'POST') return new Response('POST only', { status: 405 });
  return new Response(JSON.stringify({
    error: 'not_yet_implemented',
    hint: 'Pro tier API opens Tuesday post-deploy. Free tier is fully client-side — no server call needed.',
    schema: {
      agent: 'string, required',
      model: 'string, required',
      input_tokens: 'integer, required',
      output_tokens: 'integer, required',
      ts: 'ISO8601, optional',
      meta: 'object, optional'
    }
  }, null, 2), {
    status: 501,
    headers: {
      'content-type': 'application/json',
      'access-control-allow-origin': '*'
    }
  });
};
