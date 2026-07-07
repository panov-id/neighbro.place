// Service worker for the neighbro.place PWA shell. Versioned cache pattern
// adapted from noisen-app: precache the shell, stale-while-revalidate GETs.
// The deploy step replaces __BUILD__ with the git hash so a new deploy
// invalidates the old cache.
const CACHE = 'neighbro-__BUILD__';
// config.js is deliberately NOT precached: it carries the environment's
// Supabase target and can change without a new build hash, so it is served
// network-first (see the fetch handler) to avoid pinning a stale backend.
const PRECACHE = [
  '/',
  '/fonts.css',
  '/manifest.json',
  '/icons/icon.svg',
  '/icons/icon-192.png',
  '/icons/icon-512.png',
];

self.addEventListener('install', (event) => {
  event.waitUntil(
    caches.open(CACHE).then((c) => c.addAll(PRECACHE)).then(() => self.skipWaiting())
  );
});

self.addEventListener('activate', (event) => {
  event.waitUntil(
    caches.keys()
      .then((keys) => Promise.all(keys.filter((k) => k !== CACHE).map((k) => caches.delete(k))))
      .then(() => self.clients.claim())
  );
});

self.addEventListener('fetch', (event) => {
  if (event.request.method !== 'GET') return;

  // config.js: network-first so an environment/target change takes effect
  // without waiting for a new build hash; fall back to cache when offline.
  const url = new URL(event.request.url);
  if (url.origin === location.origin && url.pathname === '/config.js') {
    event.respondWith(
      fetch(event.request).then((res) => {
        if (res.ok) {
          const clone = res.clone();
          caches.open(CACHE).then((c) => c.put(event.request, clone));
        }
        return res;
      }).catch(() => caches.match(event.request))
    );
    return;
  }

  event.respondWith(
    caches.match(event.request).then((cached) => {
      const net = fetch(event.request).then((res) => {
        if (res.ok && new URL(event.request.url).origin === location.origin) {
          const clone = res.clone();
          caches.open(CACHE).then((c) => c.put(event.request, clone));
        }
        return res;
      }).catch(() => {
        // Offline and uncached: for a page navigation, fall back to the
        // precached app shell ('/') so we never show the browser error page.
        if (event.request.mode === 'navigate') return caches.match('/');
        return cached;
      });
      return cached || net;
    })
  );
});

// Web Push: show the notification and focus/open the app on click.
self.addEventListener('push', (event) => {
  let data = {};
  try { data = event.data ? event.data.json() : {}; } catch (e) {}
  const title = data.title || 'NEIGHBRO.PLACE';
  event.waitUntil(
    self.registration.showNotification(title, {
      body: data.body || '',
      icon: '/icons/icon-192.png',
      badge: '/icons/icon-192.png',
      data: { url: data.url || '/' },
    })
  );
});

self.addEventListener('notificationclick', (event) => {
  event.notification.close();
  const url = (event.notification.data && event.notification.data.url) || '/';
  event.waitUntil(
    self.clients.matchAll({ type: 'window', includeUncontrolled: true }).then((cls) => {
      for (const c of cls) { if ('focus' in c) return c.focus(); }
      return self.clients.openWindow(url);
    })
  );
});
