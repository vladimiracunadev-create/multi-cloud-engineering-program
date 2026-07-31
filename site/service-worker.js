const CACHE = "multicloud-program-v2.0.0-r2";
const CORE = [
  "./", "./index.html", "./styles.css?v=2.0.0-r2", "./app.js?v=2.0.0-r2", "./catalog.json",
  "./manifest.webmanifest", "./assets/icon.svg", "./assets/class.css",
  "./assets/class.js", "./assets/multicloud-topology.png"
];

self.addEventListener("install", (event) => {
  event.waitUntil((async () => {
    const cache = await caches.open(CACHE);
    await cache.addAll(CORE);
    await self.skipWaiting();
  })());
});

self.addEventListener("activate", (event) => {
  event.waitUntil((async () => {
    const keys = await caches.keys();
    await Promise.all(keys.filter((key) => key !== CACHE).map((key) => caches.delete(key)));
    await self.clients.claim();
  })());
});

self.addEventListener("fetch", (event) => {
  if (event.request.method !== "GET") return;
  event.respondWith((async () => {
    try {
      const response = await fetch(event.request);
      const url = new URL(event.request.url);
      const cacheableDestination = ["document", "script", "style", "image", "font"].includes(event.request.destination);
      const cacheableData = url.pathname.endsWith("/catalog.json");
      if (response.ok && url.origin === self.location.origin && (cacheableDestination || cacheableData)) {
        const cache = await caches.open(CACHE);
        await cache.put(event.request, response.clone());
      }
      return response;
    } catch (error) {
      const cached = await caches.match(event.request);
      if (cached) return cached;
      if (event.request.mode === "navigate") return caches.match("./index.html");
      return Response.error();
    }
  })());
});

self.addEventListener("message", (event) => {
  if (event.data === "SKIP_WAITING") self.skipWaiting();
});
