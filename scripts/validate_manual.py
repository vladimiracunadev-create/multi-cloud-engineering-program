"""Validate that the committed manual covers the current canonical course sources."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path

from pypdf import PdfReader

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "output/pdf/manual-manifest.json"


def aggregate_hash(paths: list[Path]) -> str:
    digest = hashlib.sha256()
    for path in paths:
        digest.update(path.relative_to(ROOT).as_posix().encode("utf-8"))
        digest.update(b"\0")
        digest.update(path.read_bytes())
        digest.update(b"\0")
    return digest.hexdigest()


def main() -> None:
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    catalog = json.loads((ROOT / "curriculum/catalog.json").read_text(encoding="utf-8"))
    sources = [
        ROOT / "docs/STUDENT_GUIDE.md", ROOT / "docs/METHODOLOGY.md",
        ROOT / "docs/SYLLABUS.md", ROOT / "docs/ASSESSMENT_RUBRIC.md",
        ROOT / "docs/PROFESSIONAL_PATHS.md", ROOT / "docs/CERTIFICATION_MAP.md",
        ROOT / "docs/BIBLIOGRAPHY.md",
    ]
    seen_parts = set()
    for item in catalog:
        part = ROOT / "classes" / f"part-{item['part']}-{item['part_slug']}"
        if item["part"] not in seen_parts:
            sources.append(part / "README.md")
            seen_parts.add(item["part"])
        lesson = part / f"{item['id']}-{item['slug']}"
        sources.extend([lesson / "README.md", lesson / "assessment.md"])

    pdf = ROOT / manifest["manual"]
    checks = {
        "part_count": len(seen_parts) == manifest["part_count"] == 24,
        "class_count": len(catalog) == manifest["class_count"] == 288,
        "assessment_count": sum(path.name == "assessment.md" for path in sources) == manifest["assessment_count"] == 288,
        "source_file_count": len(sources) == manifest["source_file_count"],
        "source_sha256": aggregate_hash(sources) == manifest["source_sha256"],
        "pdf_sha256": hashlib.sha256(pdf.read_bytes()).hexdigest() == manifest["pdf_sha256"],
        "page_count": len(PdfReader(str(pdf)).pages) == manifest["page_count"] and manifest["page_count"] >= 500,
    }
    failed = [name for name, valid in checks.items() if not valid]
    if failed:
        raise SystemExit("Manual inválido: " + ", ".join(failed))
    print(
        f"Manual válido: {manifest['page_count']} páginas, "
        f"{manifest['class_count']} clases y {manifest['assessment_count']} evaluaciones"
    )


if __name__ == "__main__":
    main()
