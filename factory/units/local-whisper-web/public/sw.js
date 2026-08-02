// Local Whisper Web — service worker (app shell cache).
// Model weights are cached separately by Transformers.js via IndexedDB.
const CACHE = 'lww-shell-v1';
const SHELL = ['/', '/app.html', '/styles.css', '/app.js', '/whisper-tool.js', '/manifest.json', '/icon-192.svg', '/icon-512.svg'];

self.addEventListener('install', ev => {
  ev.waitUntil(caches.open(CACHE).then(c => c.addAll(SHELL)).then(() => self.skipWaiting()));
});
self.addEventListener('activate', ev => {
  ev.waitUntil(
    caches.keys().then(keys => Promise.all(keys.filter(k => k !== CACHE).map(k => caches.delete(k))))
      .then(() => self.clients.claim())
  );
});
self.addEventListener('fetch', ev => {
  const url = new URL(ev.request.url);
  // Only cache same-origin GETs — leave HF/CDN alone (Transformers.js handles those).
  if (ev.request.method !== 'GET' || url.origin !== location.origin) return;
  ev.respondWith(
    caches.match(ev.request).then(hit => hit || fetch(ev.request).then(res => {
      const copy = res.clone();
      caches.open(CACHE).then(c => c.put(ev.request, copy)).catch(() => {});
      return res;
    }).catch(() => caches.match('/app.html')))
  );
});
