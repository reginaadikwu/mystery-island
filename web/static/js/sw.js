const CACHE_NAME = "mystery-island-v2";

const ASSETS = [
    "/",
    "/static/css/style.css",
    "/static/manifest.json",
    "/static/images/icon.svg",
    "/static/images/icon-192.png",
    "/static/images/icon-512.png"
];

self.addEventListener("install", event => {
    event.waitUntil(
        caches.open(CACHE_NAME).then(cache => cache.addAll(ASSETS))
    );
});

self.addEventListener("activate", event => {
    event.waitUntil(
        caches.keys().then(keys =>
            Promise.all(
                keys
                    .filter(key => key !== CACHE_NAME)
                    .map(key => caches.delete(key))
            )
        )
    );
});

self.addEventListener("fetch", event => {
    if (event.request.method !== "GET") return;

    event.respondWith(
        fetch(event.request).catch(() => caches.match(event.request))
    );
});
