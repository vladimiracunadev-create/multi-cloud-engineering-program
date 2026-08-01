"""Build the complete GitHub Pages site from the curriculum source of truth."""

from __future__ import annotations

import html
import json
import re
import shutil
from pathlib import Path

import markdown

from asset_version import ASSET_VERSION

ROOT = Path(__file__).resolve().parents[1]
SITE = ROOT / "site"
CLASSES_OUT = SITE / "classes"
PARTS_OUT = SITE / "parts"
CATALOG_PATH = ROOT / "curriculum" / "catalog.json"
REPO_URL = "https://github.com/vladimiracunadev-create/multi-cloud-engineering-program"
PAGES_URL = "https://vladimiracunadev-create.github.io/multi-cloud-engineering-program"

MD_EXTENSIONS = ["extra", "toc", "sane_lists"]


def render_markdown(text: str) -> str:
    return markdown.markdown(text, extensions=MD_EXTENSIONS, output_format="html5")


def description(text: str, limit: int = 155) -> str:
    plain = re.sub(r"[`*_>#\[\]()]", " ", text)
    plain = re.sub(r"\s+", " ", plain).strip()
    return plain[:limit].rstrip()


def heading_text(markdown_text: str, fallback: str) -> str:
    match = re.search(r"^#\s+(.+)$", markdown_text, flags=re.MULTILINE)
    return re.sub(r"[*`]", "", match.group(1)).strip() if match else fallback


def toc_from_html(body: str) -> str:
    items = []
    for level, anchor, label in re.findall(r'<h([23]) id="([^"]+)">(.*?)</h\1>', body, flags=re.DOTALL):
        clean = re.sub(r"<[^>]+>", "", label)
        items.append(f'<a class="toc-level-{level}" href="#{anchor}">{clean}</a>')
    return "".join(items)


def page_shell(*, title: str, meta: str, body: str, page_type: str, toc: str = "", canonical: str = "", asset_prefix: str = "../") -> str:
    escaped_title = html.escape(title)
    escaped_meta = html.escape(meta)
    canonical_url = canonical or PAGES_URL
    json_ld = json.dumps(
        {
            "@context": "https://schema.org",
            "@type": "Course",
            "name": title,
            "description": meta,
            "provider": {"@type": "Person", "name": "Vladimir Acuña"},
            "inLanguage": "es",
            "url": canonical_url,
        },
        ensure_ascii=False,
    )
    return f"""<!doctype html>
<html lang="es" data-theme="dark">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width,initial-scale=1">
  <meta name="theme-color" content="#111713">
  <meta name="description" content="{escaped_meta}">
  <meta property="og:type" content="website">
  <meta property="og:title" content="{escaped_title}">
  <meta property="og:description" content="{escaped_meta}">
  <meta property="og:url" content="{canonical_url}">
  <meta property="og:image" content="{PAGES_URL}/assets/og-cover.jpg">
  <meta name="twitter:card" content="summary_large_image">
  <link rel="canonical" href="{canonical_url}">
  <link rel="icon" type="image/svg+xml" href="{asset_prefix}assets/icon.svg">
  <link rel="stylesheet" href="{asset_prefix}assets/class.css?v={ASSET_VERSION}">
  <script type="application/ld+json">{json_ld}</script>
  <title>{escaped_title} · Multi-Cloud Engineering</title>
</head>
<body class="doc-page" data-page-type="{page_type}">
{body}
  <aside class="toc-panel" aria-label="Contenido de la página">
    <strong>En esta página</strong>
    <nav>{toc}</nav>
  </aside>
  <script type="module" src="{asset_prefix}assets/class.js?v={ASSET_VERSION}"></script>
</body>
</html>
"""


def source_path(item: dict) -> Path:
    return (
        ROOT
        / "classes"
        / f"part-{item['part']}-{item['part_slug']}"
        / f"{item['id']}-{item['slug']}"
    )


def rewrite_class_links(markdown_text: str, class_lookup: dict[str, str], part_id: str) -> str:
    def replace(match: re.Match[str]) -> str:
        label, target = match.group(1), match.group(2)
        if target.startswith(("http://", "https://", "#")):
            return match.group(0)
        class_match = re.search(r"/(\d{3})-[^/)]+/README\.md", "/" + target)
        if class_match and class_match.group(1) in class_lookup:
            return f"[{label}]({class_match.group(1)}.html)"
        if target == "../README.md":
            return f"[{label}](../parts/{part_id}.html)"
        if target.endswith("assessment.md"):
            return f"[{label}](#assessment)"
        if target.endswith(("lab.py", "lesson.yaml")):
            return f"[{label}]({REPO_URL}/blob/main/{class_lookup['source']}/{Path(target).name})"
        return f"[{label}]({REPO_URL}/blob/main/{class_lookup['source']}/{target})"

    return re.sub(r"\[([^]]+)\]\(([^)]+)\)", replace, markdown_text)


def class_page(item: dict, catalog: list[dict], index: int) -> str:
    folder = source_path(item)
    lesson_md = (folder / "README.md").read_text(encoding="utf-8")
    assessment_md = (folder / "assessment.md").read_text(encoding="utf-8")
    lookup = {x["id"]: x["slug"] for x in catalog}
    lookup["source"] = folder.relative_to(ROOT).as_posix()
    lesson_html = render_markdown(rewrite_class_links(lesson_md, lookup, item["part"]))
    assessment_html = render_markdown(assessment_md)
    toc = toc_from_html(lesson_html)
    previous = catalog[index - 1] if index else None
    following = catalog[index + 1] if index + 1 < len(catalog) else None
    previous_link = (
        f'<a class="nav-link" href="{previous["id"]}.html">← {html.escape(previous["title"])}</a>'
        if previous
        else '<span class="nav-link disabled">Inicio del programa</span>'
    )
    following_link = (
        f'<a class="nav-link next" href="{following["id"]}.html">{html.escape(following["title"])} →</a>'
        if following
        else '<span class="nav-link disabled next">Fin del programa</span>'
    )
    command = f"python {folder.relative_to(ROOT).as_posix()}/lab.py --seed 42"
    page_body = f"""
  <header class="doc-topbar">
    <a class="doc-brand" href="../index.html"><span>☁</span> Multi-Cloud Engineering</a>
    <div class="doc-actions">
      <button class="icon-button" id="copy-link" title="Copiar enlace" aria-label="Copiar enlace">⛓</button>
      <button class="icon-button" id="theme-toggle" title="Cambiar tema" aria-label="Cambiar tema">◐</button>
      <a class="icon-button" href="{REPO_URL}/tree/main/{folder.relative_to(ROOT).as_posix()}" title="Ver fuentes" aria-label="Ver fuentes">⌘</a>
    </div>
  </header>
  <div class="doc-layout">
    <main class="lesson-content">
      <nav class="breadcrumbs"><a href="../index.html">Programa</a><span>/</span><a href="../parts/{item['part']}.html">Parte {item['part']}</a><span>/</span><strong>{item['id']}</strong></nav>
      <section class="lesson-status">
        <div><span class="kicker">Parte {item['part']} · {html.escape(item['level'])}</span><strong>{item['estimated_hours']} horas</strong></div>
        <label class="completion"><input type="checkbox" data-lesson-complete="{item['id']}"> Clase completada</label>
      </section>
      <article class="markdown-body">{lesson_html}</article>
      <section class="lab-command" id="laboratorio-ejecutable">
        <div><span class="kicker">Laboratorio ejecutable</span><h2>{html.escape(item['artifact'])}</h2></div>
        <code>{html.escape(command)}</code>
        <button class="copy-command" data-copy="{html.escape(command)}">Copiar comando</button>
      </section>
      <section class="assessment-block markdown-body" id="assessment">
        <div class="assessment-heading"><span class="kicker">Comprobación de dominio</span><strong>Reto y rúbrica de la clase</strong></div>
        {assessment_html}
      </section>
      <nav class="lesson-navigation">{previous_link}{following_link}</nav>
    </main>
  </div>
"""
    return page_shell(
        title=f"{item['id']} — {item['title']}",
        meta=description(lesson_md),
        body=page_body,
        page_type="lesson",
        toc=toc,
        canonical=f"{PAGES_URL}/classes/{item['id']}.html",
    )


def part_page(part_id: str, items: list[dict]) -> str:
    part_folder = source_path(items[0]).parent
    md_path = part_folder / "README.md"
    md_text = md_path.read_text(encoding="utf-8")
    rendered = render_markdown(md_text)
    cards = "".join(
        f"""<article class="part-class" data-class-id="{item['id']}">
          <label><input type="checkbox" data-lesson-complete="{item['id']}"><span>{item['id']}</span></label>
          <div><a href="../classes/{item['id']}.html">{html.escape(item['title'])}</a><small>{html.escape(item['lab_kind'])} · {item['estimated_hours']} h</small></div>
        </article>"""
        for item in items
    )
    body = f"""
  <header class="doc-topbar">
    <a class="doc-brand" href="../index.html"><span>☁</span> Multi-Cloud Engineering</a>
    <div class="doc-actions"><button class="icon-button" id="theme-toggle" title="Cambiar tema" aria-label="Cambiar tema">◐</button></div>
  </header>
  <main class="part-content">
    <nav class="breadcrumbs"><a href="../index.html">Programa</a><span>/</span><strong>Parte {part_id}</strong></nav>
    <article class="markdown-body part-intro">{rendered}</article>
    <section class="part-class-list"><div class="section-title"><span class="kicker">Recorrido</span><h2>Clases de la parte</h2></div>{cards}</section>
  </main>
"""
    return page_shell(
        title=f"Parte {part_id} — {items[0]['part_title']}",
        meta=description(md_text),
        body=body,
        page_type="part",
        toc=toc_from_html(rendered),
        canonical=f"{PAGES_URL}/parts/{part_id}.html",
    )


def build() -> None:
    catalog = json.loads(CATALOG_PATH.read_text(encoding="utf-8"))
    shutil.rmtree(CLASSES_OUT, ignore_errors=True)
    shutil.rmtree(PARTS_OUT, ignore_errors=True)
    CLASSES_OUT.mkdir(parents=True)
    PARTS_OUT.mkdir(parents=True)

    for index, item in enumerate(catalog):
        (CLASSES_OUT / f"{item['id']}.html").write_text(class_page(item, catalog, index), encoding="utf-8")

    for part_id in sorted({item["part"] for item in catalog}):
        items = [item for item in catalog if item["part"] == part_id]
        (PARTS_OUT / f"{part_id}.html").write_text(part_page(part_id, items), encoding="utf-8")

    urls = [f"{PAGES_URL}/"]
    urls.extend(f"{PAGES_URL}/parts/{part_id}.html" for part_id in sorted({x['part'] for x in catalog}))
    urls.extend(f"{PAGES_URL}/classes/{item['id']}.html" for item in catalog)
    sitemap = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    sitemap += "\n".join(f"  <url><loc>{url}</loc></url>" for url in urls)
    sitemap += "\n</urlset>\n"
    (SITE / "sitemap.xml").write_text(sitemap, encoding="utf-8")
    (SITE / "robots.txt").write_text(f"User-agent: *\nAllow: /\nSitemap: {PAGES_URL}/sitemap.xml\n", encoding="utf-8")
    (SITE / "404.html").write_text(
        page_shell(
            title="Página no encontrada",
            meta="La página solicitada no existe en el programa.",
            body='<main class="not-found"><span>404</span><h1>Página no encontrada</h1><a href="./index.html">Volver al programa</a></main>',
            page_type="404",
            asset_prefix="",
        ),
        encoding="utf-8",
    )
    print(f"Generated {len(catalog)} class pages, {len({x['part'] for x in catalog})} part pages and SEO assets.")


if __name__ == "__main__":
    build()
