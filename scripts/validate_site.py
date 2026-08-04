"""Validate the generated GitHub Pages artifact."""

from __future__ import annotations

import json
import re
from pathlib import Path

from asset_version import ASSET_VERSION

ROOT = Path(__file__).resolve().parents[1]
SITE = ROOT / "site"


def validate() -> list[str]:
    errors: list[str] = []
    catalog = json.loads((ROOT / "curriculum" / "catalog.json").read_text(encoding="utf-8"))
    required = [
        SITE / "index.html",
        SITE / "app.js",
        SITE / "service-worker.js",
        SITE / "manifest.webmanifest",
        SITE / "sitemap.xml",
        SITE / "robots.txt",
        SITE / "assets" / "multicloud-topology.webp",
        SITE / "assets" / "og-cover.jpg",
        SITE / "assets" / "class.css",
        SITE / "assets" / "class.js",
    ]
    for path in required:
        if not path.exists() or path.stat().st_size == 0:
            errors.append(f"missing or empty: {path.relative_to(ROOT)}")

    class_pages = sorted((SITE / "classes").glob("*.html"))
    part_pages = sorted((SITE / "parts").glob("*.html"))
    if len(class_pages) != len(catalog):
        errors.append(f"expected {len(catalog)} class pages, found {len(class_pages)}")
    if len(part_pages) != 24:
        errors.append(f"expected 24 part pages, found {len(part_pages)}")

    for item in catalog:
        page = SITE / "classes" / f"{item['id']}.html"
        if not page.exists():
            errors.append(f"missing class page {item['id']}")
            continue
        text = page.read_text(encoding="utf-8")
        for marker in (
            item["title"],
            "assessment",
            "data-lesson-complete",
            "application/ld+json",
            'figure class="diagram"',
            f"class.js?v={ASSET_VERSION}",
        ):
            if marker not in text:
                errors.append(f"{page.relative_to(ROOT)} missing {marker}")
        if "language-mermaid" in text:
            errors.append(f"{page.relative_to(ROOT)} tiene un diagrama sin renderizar")
        for reference in re.findall(r'assets/diagrams/([0-9a-f]+\.svg)', text):
            if not (SITE / "assets" / "diagrams" / reference).exists():
                errors.append(f"{page.relative_to(ROOT)} apunta a un diagrama inexistente: {reference}")

    index = (SITE / "index.html").read_text(encoding="utf-8")
    for marker in ("og:title", "twitter:card", "curriculum-view", "analytics-view", "roadmap-view", "load-more", f"v={ASSET_VERSION}"):
        if marker not in index:
            errors.append(f"site/index.html missing {marker}")
    if re.search(r"\b(TODO|TBD|FIXME)\b", index):
        errors.append("site/index.html contains placeholder text")

    app = (SITE / "app.js").read_text(encoding="utf-8")
    if 'updateViaCache: "none"' not in app:
        errors.append("site/app.js must bypass HTTP cache when updating the service worker")
    for marker in ("visibleLessons: 60", "function renderView(view)", "function refreshCurriculum()"):
        if marker not in app:
            errors.append(f"site/app.js missing responsive curriculum marker: {marker}")

    worker = (SITE / "service-worker.js").read_text(encoding="utf-8")
    if f"multicloud-program-v{ASSET_VERSION}" not in worker:
        errors.append("site/service-worker.js has an obsolete cache version")
    if 'cached || caches.match("./index.html")' in worker:
        errors.append("site/service-worker.js must not return HTML for failed asset requests")

    # Los diagramas van pre-renderizados: si volviera una dependencia externa,
    # el portal sin conexion y la aplicacion Android se quedarian sin ellos.
    class_script = (SITE / "assets" / "class.js").read_text(encoding="utf-8")
    for forbidden in ("cdn.jsdelivr.net", "unpkg.com", "cdnjs.cloudflare.com"):
        if forbidden in class_script:
            errors.append(f"site/assets/class.js depende de un CDN externo: {forbidden}")

    svgs = sorted((SITE / "assets" / "diagrams").glob("*.svg"))
    if len(svgs) < 200:
        errors.append(f"faltan diagramas renderizados: solo {len(svgs)} SVG publicados")
    for svg in svgs:
        if svg.stat().st_size == 0 or "<svg" not in svg.read_text(encoding="utf-8")[:400]:
            errors.append(f"diagrama invalido: {svg.name}")
    return errors


def main() -> int:
    errors = validate()
    if errors:
        print("Site validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1
    print("Site valid: 288 classes, 24 parts, PWA and SEO assets complete.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
