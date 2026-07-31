"""Generate the concise program manual PDF from the canonical catalog."""
import json
from pathlib import Path
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.platypus import PageBreak, Paragraph, SimpleDocTemplate, Spacer, Table, TableStyle

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "output/pdf/multi-cloud-engineering-manual-v2.0.pdf"
catalog = json.loads((ROOT / "curriculum/catalog.json").read_text(encoding="utf-8"))
styles = getSampleStyleSheet()
styles.add(ParagraphStyle(name="Cover", parent=styles["Title"], fontSize=28, leading=34, textColor=colors.HexColor("#102A43"), alignment=TA_CENTER, spaceAfter=16))
styles.add(ParagraphStyle(name="Part", parent=styles["Heading1"], fontSize=19, leading=24, textColor=colors.HexColor("#007C83"), spaceAfter=10))
styles.add(ParagraphStyle(name="Small", parent=styles["BodyText"], fontSize=8.5, leading=11))

def footer(canvas, doc):
    canvas.saveState(); canvas.setFillColor(colors.HexColor("#64748B")); canvas.setFont("Helvetica", 8)
    canvas.drawString(18*mm, 10*mm, "Multi-Cloud Engineering Program v2.0")
    canvas.drawRightString(192*mm, 10*mm, str(doc.page)); canvas.restoreState()

OUT.parent.mkdir(parents=True, exist_ok=True)
doc = SimpleDocTemplate(str(OUT), pagesize=A4, leftMargin=18*mm, rightMargin=18*mm, topMargin=18*mm, bottomMargin=17*mm, title="Multi-Cloud Engineering Program v2.0")
story = [Spacer(1, 45*mm), Paragraph("Multi-Cloud Engineering Program", styles["Cover"]), Paragraph("24 partes · 288 clases · 1.288 horas", styles["Heading2"]), Spacer(1, 12*mm), Paragraph("Manual de recorrido, evaluación y práctica desde fundamentos hasta arquitectura cloud experta.", styles["BodyText"]), PageBreak()]
story += [Paragraph("Cómo estudiar", styles["Part"]), Paragraph("Diagnostica, estudia el modelo, predice el resultado, ejecuta, provoca un fallo, recupera y conserva evidencia. Los despliegues cloud reales requieren cuenta autorizada, identidad temporal, presupuesto, etiquetas y destrucción verificada.", styles["BodyText"]), Spacer(1, 8*mm)]
story.append(Table([["Evidencia", "Debe demostrar"], ["Diseño", "Requisitos, límites, alternativas y ADR"], ["Implementación", "Código o configuración reproducible"], ["Operación", "Señal, fallo, recuperación y runbook"], ["Economía", "Unidad de costo, presupuesto y sensibilidad"]], colWidths=[40*mm, 125*mm], style=TableStyle([("BACKGROUND",(0,0),(-1,0),colors.HexColor("#102A43")),("TEXTCOLOR",(0,0),(-1,0),colors.white),("GRID",(0,0),(-1,-1),0.5,colors.HexColor("#CBD5E1")),("VALIGN",(0,0),(-1,-1),"TOP"),("FONTNAME",(0,0),(-1,0),"Helvetica-Bold"),("FONTSIZE",(0,0),(-1,-1),9),("PADDING",(0,0),(-1,-1),6)])))
for part in sorted({x["part"] for x in catalog}):
    items = [x for x in catalog if x["part"] == part]
    story += [PageBreak(), Paragraph(f"Parte {part} · {items[0]['part_title']}", styles["Part"]), Paragraph(f"Nivel: {items[0]['level']} · {sum(x['estimated_hours'] for x in items)} horas", styles["BodyText"]), Spacer(1, 4*mm)]
    rows = [["Clase", "Tema", "Práctica", "h"]] + [[x["id"], Paragraph(x["title"], styles["Small"]), x["lab_kind"], str(x["estimated_hours"])] for x in items]
    story.append(Table(rows, colWidths=[14*mm, 98*mm, 38*mm, 10*mm], repeatRows=1, style=TableStyle([("BACKGROUND",(0,0),(-1,0),colors.HexColor("#007C83")),("TEXTCOLOR",(0,0),(-1,0),colors.white),("GRID",(0,0),(-1,-1),0.35,colors.HexColor("#CBD5E1")),("VALIGN",(0,0),(-1,-1),"TOP"),("FONTSIZE",(0,0),(-1,-1),8),("PADDING",(0,0),(-1,-1),4)])))
    story += [Spacer(1, 5*mm), Paragraph("Resultado de etapa: " + items[-1]["artifact"].replace("-", " ") + ".", styles["BodyText"])]
doc.build(story, onFirstPage=footer, onLaterPages=footer)
print(OUT)
