"""Build the split manuals: one per part and one per cloud provider.

El manual integral pasa de 2.800 paginas: sirve para consultar y no para estudiar
una parte en el metro. Estos dos cortes reutilizan exactamente el mismo
generador —mismos estilos, mismos diagramas ya renderizados y mismas fuentes—,
asi que no pueden desincronizarse del manual grande.

  por parte   24 cuadernos de una parte con sus 12 clases y evaluaciones
  por nube    el recorrido completo de AWS, de Azure y de Google Cloud

Usage:
    python scripts/generate_manuals.py [--only parts|clouds]
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import shutil
from pathlib import Path

from pypdf import PdfReader
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import mm
from reportlab.platypus import PageBreak, Paragraph, Spacer
from reportlab.platypus.tableofcontents import TableOfContents

from generate_manual import (
    ManualDocTemplate,
    heading,
    markdown_flowables,
    styles,
    table_flow,
)

ROOT = Path(__file__).resolve().parents[1]
OUT_PARTS = ROOT / "output" / "pdf" / "partes"
OUT_CLOUDS = ROOT / "output" / "pdf" / "nubes"
SITE_PARTS = ROOT / "site" / "downloads" / "partes"
SITE_CLOUDS = ROOT / "site" / "downloads" / "nubes"
MANIFEST = ROOT / "output" / "pdf" / "manuals-manifest.json"
CATALOG_PATH = ROOT / "curriculum" / "catalog.json"

# Cada nube tiene sus partes propias; ademas se recogen las clases sueltas de
# otras partes que tratan ese proveedor, para que el cuaderno este completo.
CLOUDS = {
    "aws": {
        "name": "AWS",
        "title": "Amazon Web Services",
        "parts": ["02", "17"],
        "pattern": r"\baws\b|amazon|\bec2\b|\bs3\b|dynamodb|cloudformation|\beks\b|\brds\b",
        "summary": (
            "La plataforma esencial de AWS y su arquitectura, automatización y operación en "
            "producción, con las clases de otras partes que tratan el proveedor."
        ),
    },
    "azure": {
        "name": "Azure",
        "title": "Microsoft Azure",
        "parts": ["03", "18"],
        "pattern": r"\bazure\b|entra|\baks\b|bicep|cosmos",
        "summary": (
            "La plataforma esencial de Azure y su arquitectura empresarial y operación en "
            "producción, con las clases de otras partes que tratan el proveedor."
        ),
    },
    "google-cloud": {
        "name": "Google Cloud",
        "title": "Google Cloud",
        "parts": ["04", "19"],
        "pattern": r"google cloud|\bgcp\b|\bgke\b|bigquery|cloud run|pub/?sub|firestore|spanner",
        "summary": (
            "La plataforma esencial de Google Cloud y su arquitectura de datos y operación en "
            "producción, con las clases de otras partes que tratan el proveedor."
        ),
    },
}


def class_dir(item: dict) -> Path:
    return (
        ROOT / "classes" / f"part-{item['part']}-{item['part_slug']}"
        / f"{item['id']}-{item['slug']}"
    )


def toc_block() -> TableOfContents:
    toc = TableOfContents()
    toc.levelStyles = [
        ParagraphStyle(
            name="SplitTOC0", fontName="Helvetica-Bold", fontSize=10, leading=14,
            leftIndent=0, firstLineIndent=0, textColor=colors.HexColor("#102A43"), spaceBefore=5,
        ),
        ParagraphStyle(
            name="SplitTOC1", fontName="Helvetica", fontSize=8.3, leading=11,
            leftIndent=7 * mm, firstLineIndent=0, textColor=colors.HexColor("#334E68"),
        ),
    ]
    return toc


def cover(title: str, subtitle: str, facts: list[list[str]], summary: str):
    return [
        Spacer(1, 37 * mm),
        Paragraph("Multi-Cloud Engineering Program", styles["ManualCover"]),
        Paragraph(title, styles["ManualSubtitle"]),
        Spacer(1, 8 * mm),
        Paragraph(subtitle, styles["ManualSubtitle"]),
        Spacer(1, 14 * mm),
        Paragraph(summary, styles["ManualSubtitle"]),
        Spacer(1, 20 * mm),
        Paragraph(
            "Extracto del manual integral, generado desde las mismas fuentes versionadas.",
            styles["ManualSubtitle"],
        ),
        PageBreak(),
        heading("Alcance de este cuaderno", "ManualPart", 0, "alcance"),
        table_flow(facts),
        PageBreak(),
        heading("Índice", "ManualPart", 0, "indice"),
        toc_block(),
        PageBreak(),
    ]


def lesson_flow(item: dict) -> list:
    folder = class_dir(item)
    flow = markdown_flowables(folder / "README.md", top_style="ManualClass", toc_level=1)
    flow.append(Spacer(1, 5 * mm))
    flow.extend(markdown_flowables(folder / "assessment.md", top_style="ManualH2"))
    flow.append(PageBreak())
    return flow


def build_part(catalog: list[dict], part: str, destination: Path) -> dict:
    items = [item for item in catalog if item["part"] == part]
    part_dir = ROOT / "classes" / f"part-{part}-{items[0]['part_slug']}"
    hours = sum(item["estimated_hours"] for item in items)
    story = cover(
        f"Parte {part} — {items[0]['part_title']}",
        f"{len(items)} clases · {hours} horas",
        [
            ["Componente", "Cobertura"],
            ["Parte", f"{part} de 23"],
            ["Clases", f"{items[0]['id']}–{items[-1]['id']}"],
            ["Evaluaciones", str(len(items))],
            ["Horas estimadas", str(hours)],
        ],
        "Cuaderno de una sola parte: su introducción, sus clases completas y sus evaluaciones.",
    )
    story.extend(markdown_flowables(part_dir / "README.md", top_style="ManualPart", toc_level=0))
    story.append(PageBreak())
    for item in items:
        story.extend(lesson_flow(item))

    ManualDocTemplate(
        str(destination),
        footer=f"Parte {part} · {items[0]['part_title']}",
        title=f"Multi-Cloud Engineering Program - Parte {part}",
    ).multiBuild(story)
    return {
        "part": part,
        "title": items[0]["part_title"],
        "file": destination.relative_to(ROOT).as_posix(),
        "class_count": len(items),
        "page_count": len(PdfReader(str(destination)).pages),
        "bytes": destination.stat().st_size,
    }


def cloud_items(catalog: list[dict], spec: dict) -> list[dict]:
    pattern = re.compile(spec["pattern"], re.IGNORECASE)
    selected = [item for item in catalog if item["part"] in spec["parts"]]
    extra = [
        item for item in catalog
        if item["part"] not in spec["parts"]
        and (pattern.search(item["title"]) or pattern.search(" ".join(item.get("keywords", []))))
    ]
    return sorted(selected + extra, key=lambda item: item["id"])


def build_cloud(catalog: list[dict], key: str, spec: dict, destination: Path) -> dict:
    items = cloud_items(catalog, spec)
    hours = sum(item["estimated_hours"] for item in items)
    own = [item for item in items if item["part"] in spec["parts"]]
    story = cover(
        f"Recorrido de {spec['title']}",
        f"{len(items)} clases · {hours} horas",
        [
            ["Componente", "Cobertura"],
            ["Partes propias", ", ".join(spec["parts"])],
            ["Clases de esas partes", str(len(own))],
            ["Clases de otras partes", str(len(items) - len(own))],
            ["Clases totales", str(len(items))],
            ["Horas estimadas", str(hours)],
        ],
        spec["summary"],
    )
    current_part = None
    for item in items:
        if item["part"] != current_part:
            current_part = item["part"]
            story.append(heading(
                f"Parte {current_part} — {item['part_title']}",
                "ManualPart", 0, f"{key}-parte-{current_part}",
            ))
            story.append(Spacer(1, 4 * mm))
        story.extend(lesson_flow(item))

    ManualDocTemplate(
        str(destination),
        footer=f"Recorrido de {spec['title']}",
        title=f"Multi-Cloud Engineering Program - {spec['title']}",
    ).multiBuild(story)
    return {
        "cloud": key,
        "name": spec["name"],
        "file": destination.relative_to(ROOT).as_posix(),
        "parts": spec["parts"],
        "class_count": len(items),
        "class_ids": [item["id"] for item in items],
        "page_count": len(PdfReader(str(destination)).pages),
        "bytes": destination.stat().st_size,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--only", choices=["parts", "clouds"])
    args = parser.parse_args()

    catalog = json.loads(CATALOG_PATH.read_text(encoding="utf-8"))
    for folder in (OUT_PARTS, OUT_CLOUDS, SITE_PARTS, SITE_CLOUDS):
        folder.mkdir(parents=True, exist_ok=True)

    manifest = {"schema_version": 1, "parts": [], "clouds": []}
    if MANIFEST.exists():
        manifest.update(json.loads(MANIFEST.read_text(encoding="utf-8")))

    if args.only != "clouds":
        entries = []
        for part in sorted({item["part"] for item in catalog}):
            slug = next(item["part_slug"] for item in catalog if item["part"] == part)
            destination = OUT_PARTS / f"manual-parte-{part}-{slug}.pdf"
            entry = build_part(catalog, part, destination)
            shutil.copy2(destination, SITE_PARTS / destination.name)
            entries.append(entry)
            print(f"  parte {part}: {entry['page_count']} páginas")
        manifest["parts"] = entries

    if args.only != "parts":
        entries = []
        for key, spec in CLOUDS.items():
            destination = OUT_CLOUDS / f"manual-{key}.pdf"
            entry = build_cloud(catalog, key, spec, destination)
            shutil.copy2(destination, SITE_CLOUDS / destination.name)
            entries.append(entry)
            print(f"  {spec['name']}: {entry['class_count']} clases, {entry['page_count']} páginas")
        manifest["clouds"] = entries

    manifest["total_files"] = len(manifest["parts"]) + len(manifest["clouds"])
    manifest["total_pages"] = sum(
        entry["page_count"] for entry in manifest["parts"] + manifest["clouds"]
    )
    for entry in manifest["parts"] + manifest["clouds"]:
        entry["sha256"] = hashlib.sha256((ROOT / entry["file"]).read_bytes()).hexdigest()
    MANIFEST.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    print(
        f"Manuales divididos: {len(manifest['parts'])} por parte y "
        f"{len(manifest['clouds'])} por nube, {manifest['total_pages']} páginas en total."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
