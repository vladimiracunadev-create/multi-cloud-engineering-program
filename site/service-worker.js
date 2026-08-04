const CACHE = "multicloud-program-v2.2.0-r1";
const NETWORK_TIMEOUT_MS = 3500;

// Shell mínimo para arrancar sin red. Se precachea uno por uno: si alguno
// falla, la instalación continúa en vez de abortar entera y dejar al portal
// sin service worker. La topología de 1,7 MB queda fuera a propósito.
const CORE = [
  "./", "./index.html", "./app.js?v=2.2.0-r1", "./catalog.json",
  "./manifest.webmanifest", "./assets/icon.svg", "./assets/class.css?v=2.2.0-r1",
  "./assets/class.js?v=2.2.0-r1"
];

self.addEventListener("install", (event) => {
  event.waitUntil((async () => {
    const cache = await caches.open(CACHE);
    await Promise.allSettled(CORE.map((url) => cache.add(url)));
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

// fetch() no rechaza en una red lenta o en un portal cautivo: se queda colgado.
// Sin límite de tiempo el portal nunca llega a pintar, aunque exista la copia
// en caché. Esto convierte "lento" en "usa la caché".
function fetchWithTimeout(request, ms) {
  return new Promise((resolve, reject) => {
    const timer = setTimeout(() => reject(new Error("network-timeout")), ms);
    fetch(request).then(
      (response) => { clearTimeout(timer); resolve(response); },
      (error) => { clearTimeout(timer); reject(error); }
    );
  });
}

// La escritura en caché no debe bloquear la respuesta al navegador.
function store(event, request, response) {
  if (!response || !response.ok) return;
  const copy = response.clone();
  event.waitUntil(caches.open(CACHE).then((cache) => cache.put(request, copy)));
}

self.addEventListener("fetch", (event) => {
  const { request } = event;
  if (request.method !== "GET") return;

  const url = new URL(request.url);
  if (url.origin !== self.location.origin) return;

  const isAsset = ["script", "style", "image", "font"].includes(request.destination);
  const isCatalog = url.pathname.endsWith("/catalog.json");
  const isDocument = request.destination === "document" || request.mode === "navigate";
  if (!isAsset && !isCatalog && !isDocument) return;

  event.respondWith((async () => {
    // Estáticos versionados por query string: la caché manda y la red revalida
    // por detrás. Nunca bloquean el pintado.
    if (isAsset) {
      const cached = await caches.match(request);
      if (cached) {
        event.waitUntil((async () => {
          try {
            store(event, request, await fetchWithTimeout(request, NETWORK_TIMEOUT_MS));
          } catch (error) {
            /* sin red: la copia en caché sigue sirviendo */
          }
        })());
        return cached;
      }
    }

    try {
      const response = await fetchWithTimeout(request, NETWORK_TIMEOUT_MS);
      store(event, request, response);
      return response;
    } catch (error) {
      const cached = await caches.match(request);
      if (cached) return cached;
      if (isDocument) {
        const shell = await caches.match("./index.html");
        if (shell) return shell;
      }
      return new Response("Sin conexión y sin copia en caché.", {
        status: 503,
        headers: { "Content-Type": "text/plain; charset=utf-8" }
      });
    }
  })());
});

self.addEventListener("message", (event) => {
  if (event.data === "SKIP_WAITING") self.skipWaiting();
});
