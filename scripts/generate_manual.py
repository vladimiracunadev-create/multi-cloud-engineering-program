"""Build the complete course manual from the canonical Markdown sources."""

from __future__ import annotations

import hashlib
import html
import json
import re
import shutil
from pathlib import Path

from pypdf import PdfReader
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.platypus import (
    BaseDocTemplate,
    Frame,
    PageBreak,
    PageTemplate,
    Paragraph,
    Preformatted,
    Spacer,
    Table,
    TableStyle,
)
from reportlab.platypus.tableofcontents import TableOfContents

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "output/pdf/multi-cloud-engineering-manual-v2.0.pdf"
SITE_OUT = ROOT / "site/downloads" / OUT.name
MANIFEST = ROOT / "output/pdf/manual-manifest.json"
CATALOG_PATH = ROOT / "curriculum/catalog.json"

FRONT_MATTER = [
    ROOT / "docs/STUDENT_GUIDE.md",
    ROOT / "docs/METHODOLOGY.md",
    ROOT / "docs/SYLLABUS.md",
    ROOT / "docs/ASSESSMENT_RUBRIC.md",
    ROOT / "docs/PROFESSIONAL_PATHS.md",
    ROOT / "docs/CERTIFICATION_MAP.md",
    ROOT / "docs/BIBLIOGRAPHY.md",
]

NAVIGATION_RE = re.compile(r"^>.*(?:Índice de la parte|Clase siguiente|Clase anterior|Contrato de clase|Evaluación).*$")
EMOJI_RE = re.compile("[\U00010000-\U0010ffff]", flags=re.UNICODE)
LINK_RE = re.compile(r"\[([^]]+)]\(([^)]+)\)")
MARK_RE = re.compile(r"[*_~]")


def clean_text(value: str) -> str:
    value = EMOJI_RE.sub("", value)
    value = LINK_RE.sub(lambda match: match.group(1), value)
    value = value.replace("<br>", " ").replace("<br/>", " ")
    value = value.replace("`", "")
    return MARK_RE.sub("", value).strip()


def paragraph_text(value: str) -> str:
    return html.escape(clean_text(value), quote=False).replace("\n", "<br/>")


styles = getSampleStyleSheet()
styles.add(ParagraphStyle(
    name="ManualCover", parent=styles["Title"], fontName="Helvetica-Bold",
    fontSize=29, leading=35, textColor=colors.HexColor("#102A43"),
    alignment=TA_CENTER, spaceAfter=16,
))
styles.add(ParagraphStyle(
    name="ManualSubtitle", parent=styles["BodyText"], fontSize=13, leading=19,
    textColor=colors.HexColor("#334E68"), alignment=TA_CENTER,
))
styles.add(ParagraphStyle(
    name="ManualPart", parent=styles["Heading1"], fontName="Helvetica-Bold",
    fontSize=20, leading=25, textColor=colors.HexColor("#007C83"),
    spaceBefore=8, spaceAfter=10, keepWithNext=True,
))
styles.add(ParagraphStyle(
    name="ManualClass", parent=styles["Heading1"], fontName="Helvetica-Bold",
    fontSize=17, leading=22, textColor=colors.HexColor("#102A43"),
    spaceBefore=6, spaceAfter=9, keepWithNext=True,
))
styles.add(ParagraphStyle(
    name="ManualH2", parent=styles["Heading2"], fontName="Helvetica-Bold",
    fontSize=13, leading=17, textColor=colors.HexColor("#007C83"),
    spaceBefore=9, spaceAfter=5, keepWithNext=True,
))
styles.add(ParagraphStyle(
    name="ManualH3", parent=styles["Heading3"], fontName="Helvetica-Bold",
    fontSize=10.5, leading=14, textColor=colors.HexColor("#334E68"),
    spaceBefore=7, spaceAfter=4, keepWithNext=True,
))
styles.add(ParagraphStyle(
    name="ManualBody", parent=styles["BodyText"], fontName="Helvetica",
    fontSize=9.2, leading=13.2, textColor=colors.HexColor("#243B53"),
    alignment=TA_LEFT, spaceAfter=4,
))
styles.add(ParagraphStyle(
    name="ManualList", parent=styles["ManualBody"], leftIndent=7 * mm,
    firstLineIndent=-4 * mm, spaceAfter=2,
))
styles.add(ParagraphStyle(
    name="ManualQuote", parent=styles["ManualBody"], leftIndent=6 * mm,
    rightIndent=4 * mm, borderColor=colors.HexColor("#38B2AC"), borderWidth=1,
    borderPadding=(3, 5, 3, 7), backColor=colors.HexColor("#E6FFFA"),
))
styles.add(ParagraphStyle(
    name="ManualCode", fontName="Courier", fontSize=8, leading=10,
    textColor=colors.black, backColor=colors.HexColor("#F0F4F8"),
    borderPadding=6, leftIndent=2 * mm, rightIndent=2 * mm, spaceBefore=3, spaceAfter=6,
))
styles.add(ParagraphStyle(
    name="ManualSmall", parent=styles["ManualBody"], fontSize=7.7, leading=10.3,
))
styles.add(ParagraphStyle(
    name="ManualTableHead", parent=styles["ManualSmall"], fontName="Helvetica-Bold",
    textColor=colors.white,
))


class ManualDocTemplate(BaseDocTemplate):
    def __init__(self, filename: str):
        super().__init__(
            filename, pagesize=A4, leftMargin=17 * mm, rightMargin=17 * mm,
            topMargin=18 * mm, bottomMargin=17 * mm, title="Multi-Cloud Engineering Program - Manual completo",
            author="Vladimir Acuña", subject="Programa completo de ingeniería multi-cloud",
        )
        frame = Frame(self.leftMargin, self.bottomMargin, self.width, self.height, id="body")
        self.addPageTemplates(PageTemplate(id="manual", frames=frame, onPage=self._decorate_page))

    def _decorate_page(self, canvas, doc):
        canvas.saveState()
        canvas.setStrokeColor(colors.HexColor("#D9E2EC"))
        canvas.line(17 * mm, 14 * mm, 193 * mm, 14 * mm)
        canvas.setFillColor(colors.HexColor("#627D98"))
        canvas.setFont("Helvetica", 7.5)
        canvas.drawString(17 * mm, 9.5 * mm, "Multi-Cloud Engineering Program · Manual integral")
        canvas.drawRightString(193 * mm, 9.5 * mm, f"Página {doc.page}")
        canvas.restoreState()

    def afterFlowable(self, flowable):
        level = getattr(flowable, "toc_level", None)
        if level is None:
            return
        text = flowable.getPlainText()
        key = getattr(flowable, "bookmark_key", f"section-{self.seq.nextf('bookmark')}")
        self.canv.bookmarkPage(key)
        self.canv.addOutlineEntry(text, key, level=level, closed=level > 0)
        self.notify("TOCEntry", (level, text, self.page, key))


def heading(text: str, style_name: str, level: int | None = None, key: str | None = None) -> Paragraph:
    item = Paragraph(paragraph_text(text), styles[style_name])
    if level is not None:
        item.toc_level = level
        item.bookmark_key = key or re.sub(r"[^a-z0-9]+", "-", clean_text(text).lower()).strip("-")
    return item


def table_flow(rows: list[list[str]]):
    if not rows:
        return Spacer(1, 1)
    width = 176 * mm
    columns = max(len(row) for row in rows)
    normalized = [row + [""] * (columns - len(row)) for row in rows]
    weights = []
    for col in range(columns):
        longest = max(len(clean_text(row[col])) for row in normalized)
        weights.append(max(12, min(longest, 48)))
    total = sum(weights)
    col_widths = [width * weight / total for weight in weights]
    data = []
    for row_index, row in enumerate(normalized):
        cell_style = styles["ManualTableHead"] if row_index == 0 else styles["ManualSmall"]
        data.append([Paragraph(paragraph_text(cell), cell_style) for cell in row])
    return Table(
        data, colWidths=col_widths, repeatRows=1, hAlign="LEFT",
        style=TableStyle([
            ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#102A43")),
            ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
            ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
            ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, colors.HexColor("#F0F4F8")]),
            ("GRID", (0, 0), (-1, -1), 0.35, colors.HexColor("#BCCCDC")),
            ("VALIGN", (0, 0), (-1, -1), "TOP"),
            ("LEFTPADDING", (0, 0), (-1, -1), 4),
            ("RIGHTPADDING", (0, 0), (-1, -1), 4),
            ("TOPPADDING", (0, 0), (-1, -1), 4),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
        ]),
    )


def markdown_flowables(path: Path, *, top_style: str = "ManualPart", toc_level: int | None = None):
    lines = path.read_text(encoding="utf-8").splitlines()
    result = []
    paragraph = []
    code = []
    table = []
    in_code = False
    first_heading = True

    def flush_paragraph():
        if paragraph:
            text = " ".join(line.strip() for line in paragraph)
            if text:
                result.append(Paragraph(paragraph_text(text), styles["ManualBody"]))
            paragraph.clear()

    def flush_table():
        if table:
            rows = [
                [cell.strip() for cell in row.strip().strip("|").split("|")]
                for row in table
                if not re.fullmatch(r"\|?[\s|:-]+\|?", row)
            ]
            if rows:
                result.extend([table_flow(rows), Spacer(1, 3 * mm)])
            table.clear()

    for raw in lines:
        line = raw.rstrip()
        if line.startswith("```"):
            flush_paragraph(); flush_table()
            if in_code:
                result.append(Preformatted("\n".join(code) or " ", styles["ManualCode"], maxLineLength=102))
                code.clear()
            in_code = not in_code
            continue
        if in_code:
            code.append(line)
            continue
        if NAVIGATION_RE.match(line):
            continue
        if line.startswith("|"):
            flush_paragraph(); table.append(line); continue
        flush_table()
        match = re.match(r"^(#{1,4})\s+(.+)$", line)
        if match:
            flush_paragraph()
            depth, title = len(match.group(1)), clean_text(match.group(2))
            if first_heading:
                result.append(heading(title, top_style, toc_level, f"{path.parent.name}-{path.stem}"))
                first_heading = False
            else:
                style = "ManualH2" if depth <= 2 else "ManualH3"
                result.append(heading(title, style))
            continue
        if re.match(r"^\s*(?:[-*]|\d+\.)\s+", line):
            flush_paragraph()
            body = re.sub(r"^\s*(?:[-*]|\d+\.)\s+", "", line)
            marker = "•" if re.match(r"^\s*[-*]", line) else re.match(r"^\s*(\d+)\.", line).group(1) + "."
            result.append(Paragraph(paragraph_text(f"{marker} {body}"), styles["ManualList"]))
            continue
        if re.match(r"^\s*- \[[ xX]\]", line):
            flush_paragraph()
            checked = "[x]" if "[x]" in line.lower() else "[ ]"
            result.append(Paragraph(paragraph_text(checked + " " + re.sub(r"^\s*- \[[ xX]\]\s*", "", line)), styles["ManualList"]))
            continue
        if line.startswith(">"):
            flush_paragraph()
            result.append(Paragraph(paragraph_text(line.lstrip("> ")), styles["ManualQuote"]))
            continue
        if line.strip() in {"---", "***"}:
            flush_paragraph(); result.append(Spacer(1, 3 * mm)); continue
        if not line.strip():
            flush_paragraph(); continue
        paragraph.append(line)

    flush_paragraph(); flush_table()
    if code:
        result.append(Preformatted("\n".join(code), styles["ManualCode"], maxLineLength=102))
    return result


def source_paths(catalog: list[dict]) -> list[Path]:
    paths = list(FRONT_MATTER)
    seen_parts = set()
    for lesson in catalog:
        part_dir = ROOT / "classes" / f"part-{lesson['part']}-{lesson['part_slug']}"
        if lesson["part"] not in seen_parts:
            paths.append(part_dir / "README.md")
            seen_parts.add(lesson["part"])
        class_dir = part_dir / f"{lesson['id']}-{lesson['slug']}"
        paths.extend([class_dir / "README.md", class_dir / "assessment.md"])
    return paths


def aggregate_hash(paths: list[Path]) -> str:
    digest = hashlib.sha256()
    for path in paths:
        digest.update(path.relative_to(ROOT).as_posix().encode("utf-8"))
        digest.update(b"\0")
        digest.update(path.read_text(encoding="utf-8").replace("\r\n", "\n").replace("\r", "\n").encode("utf-8"))
        digest.update(b"\0")
    return digest.hexdigest()


def build_story(catalog: list[dict]):
    total_hours = sum(item["estimated_hours"] for item in catalog)
    story = [
        Spacer(1, 37 * mm),
        Paragraph("Multi-Cloud Engineering Program", styles["ManualCover"]),
        Paragraph("Manual integral del curso", styles["ManualSubtitle"]),
        Spacer(1, 8 * mm),
        Paragraph(f"24 partes · 288 clases · {total_hours:,} horas".replace(",", "."), styles["ManualSubtitle"]),
        Spacer(1, 14 * mm),
        Paragraph(
            "De fundamentos de computación a arquitectura de sistemas, AWS, Azure, Google Cloud, "
            "Kubernetes, IaC, datos e IA, seguridad, SRE, FinOps, operación y capstones por industria.",
            styles["ManualSubtitle"],
        ),
        Spacer(1, 22 * mm),
        Paragraph("Contenido íntegro generado desde las fuentes versionadas del repositorio.", styles["ManualSubtitle"]),
        PageBreak(),
        heading("Alcance e integridad", "ManualPart", 0, "alcance-integridad"),
        Paragraph(
            "Este manual no es un catálogo. Incluye las guías pedagógicas centrales, los 24 módulos, "
            "las 288 lecciones completas y sus 288 evaluaciones. El laboratorio ejecutable y sus "
            "plantillas permanecen en el repositorio para conservar su carácter reproducible.",
            styles["ManualBody"],
        ),
        table_flow([
            ["Componente", "Cobertura"],
            ["Partes", "24 de 24"], ["Lecciones", "288 de 288"],
            ["Evaluaciones", "288 de 288"], ["Horas estimadas", str(total_hours)],
            ["Fuentes", "Markdown canónico + curriculum/catalog.json"],
        ]),
        PageBreak(),
        heading("Índice general", "ManualPart", 0, "indice-general"),
    ]
    toc = TableOfContents()
    toc.levelStyles = [
        ParagraphStyle(name="TOC0", fontName="Helvetica-Bold", fontSize=10, leading=14, leftIndent=0, firstLineIndent=0, textColor=colors.HexColor("#102A43"), spaceBefore=5),
        ParagraphStyle(name="TOC1", fontName="Helvetica", fontSize=8.3, leading=11, leftIndent=7 * mm, firstLineIndent=0, textColor=colors.HexColor("#334E68")),
    ]
    story.extend([toc, PageBreak(), heading("Guías pedagógicas", "ManualPart", 0, "guias-pedagogicas")])
    for source in FRONT_MATTER:
        story.extend(markdown_flowables(source, top_style="ManualClass", toc_level=1))
        story.append(PageBreak())

    for part in range(24):
        items = [item for item in catalog if int(item["part"]) == part]
        part_dir = ROOT / "classes" / f"part-{part:02d}-{items[0]['part_slug']}"
        story.extend(markdown_flowables(part_dir / "README.md", top_style="ManualPart", toc_level=0))
        story.append(PageBreak())
        for item in items:
            class_dir = part_dir / f"{item['id']}-{item['slug']}"
            story.extend(markdown_flowables(class_dir / "README.md", top_style="ManualClass", toc_level=1))
            story.append(Spacer(1, 5 * mm))
            story.extend(markdown_flowables(class_dir / "assessment.md", top_style="ManualH2"))
            story.append(PageBreak())
    return story


def main() -> None:
    catalog = json.loads(CATALOG_PATH.read_text(encoding="utf-8"))
    if len(catalog) != 288 or [item["id"] for item in catalog] != [f"{n:03d}" for n in range(1, 289)]:
        raise RuntimeError("El catálogo debe contener las clases continuas 001-288")
    sources = source_paths(catalog)
    missing = [str(path.relative_to(ROOT)) for path in sources if not path.is_file()]
    if missing:
        raise FileNotFoundError("Fuentes faltantes: " + ", ".join(missing))

    OUT.parent.mkdir(parents=True, exist_ok=True)
    SITE_OUT.parent.mkdir(parents=True, exist_ok=True)
    ManualDocTemplate(str(OUT)).multiBuild(build_story(catalog))
    shutil.copy2(OUT, SITE_OUT)

    reader = PdfReader(str(OUT))
    page_count = len(reader.pages)
    if page_count < 500:
        raise RuntimeError(f"Manual incompleto: solo {page_count} páginas")
    sample_text = "\n".join(
        reader.pages[index].extract_text() or ""
        for index in [0, min(20, page_count - 1), page_count - 1]
    )
    if "Multi-Cloud Engineering Program" not in sample_text or "Defensa final" not in sample_text:
        raise RuntimeError("No se encontraron los extremos esperados del contenido")

    manifest = {
        "schema_version": 1,
        "manual": OUT.relative_to(ROOT).as_posix(),
        "page_count": page_count,
        "part_count": 24,
        "class_count": 288,
        "assessment_count": 288,
        "source_file_count": len(sources),
        "source_sha256": aggregate_hash(sources),
        "pdf_sha256": hashlib.sha256(OUT.read_bytes()).hexdigest(),
    }
    MANIFEST.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"{OUT} ({page_count} páginas, {OUT.stat().st_size / 1024 / 1024:.1f} MiB)")


if __name__ == "__main__":
    main()
