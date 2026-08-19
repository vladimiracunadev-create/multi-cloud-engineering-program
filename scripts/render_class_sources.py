"""Vista legible de que fuentes fundamentan cada clase.

El registro `sources/bibliography.json` es la fuente de verdad, pero esta
pensado para el verificador, no para leerlo. Esto produce la vista humana:
por parte, clase a clase, cada obra con el uso que esa clase hace de ella y su
localizador resoluble.

Se genera; no se escribe a mano. `scripts/verify-sources --write` lo regenera y
`scripts/verify-sources` falla si queda desincronizado del registro.
"""

from __future__ import annotations

import collections
import re
from pathlib import Path

from sources_lib import ROOT, Citation, part_titles

INDEX = ROOT / "docs" / "FUENTES.md"
PARTS_DIR = ROOT / "docs" / "fuentes"

ESTADO = {"verificada": "✅", "pendiente": "⏳"}


def class_titles(root: Path = ROOT) -> dict[str, str]:
    """Titulo de cada clase, leido de su propio encabezado."""
    titles: dict[str, str] = {}
    for path in sorted(root.glob("classes/*/*/README.md")):
        first = path.read_text(encoding="utf-8").splitlines()[0]
        titles[path.relative_to(root).as_posix()] = first.lstrip("# ").strip()
    return titles


def _locator_link(entry: dict) -> str:
    """Enlace al localizador, en la forma que corresponde a su tipo."""
    locator = entry.get("locator") or entry.get("source_url")
    if not locator:
        return "_sin localizador_"
    if entry.get("isbn13"):
        return f"[ISBN {entry['isbn13']}]({locator})"
    if entry.get("doi"):
        return f"[doi:{entry['doi']}]({locator})"
    host = re.sub(r"^https?://(www\.)?", "", locator).split("/")[0]
    return f"[{host}]({locator})"


def _source_line(cit: Citation, entry: dict | None) -> str:
    autor = ""
    if cit.authors:
        autor = cit.authors[0].split(",")[0].strip()
        if len(cit.authors) > 1:
            autor += " et al."
    anio = f" ({cit.year})" if cit.year else ""
    cabeza = f"**{autor}{anio}, " if autor else "**"
    titulo = cit.title.replace("|", "/")
    obra = f"{cabeza}*{titulo}***" if autor else f"***{titulo}***"

    uso = cit.use.strip() or "_uso no declarado_"
    if entry is None:
        return f"- {obra} — {uso}"
    marca = ESTADO.get(entry.get("status"), "")
    tipo = {"book": "libro", "paper": "artículo", "standard": "norma"}.get(entry.get("type"), "documentación")
    return f"- {obra} — {uso}<br>  ↳ {tipo} · {_locator_link(entry)} {marca}"


def render_parts(data: dict, citations: list[Citation], root: Path = ROOT) -> dict[Path, str]:
    """Un fichero por parte, con sus 12 clases y las fuentes de cada una."""
    by_identity = {e.get("identity"): e for e in data.get("entries", [])}
    titles = class_titles(root)
    parts = part_titles(root)

    per_class: dict[str, list[Citation]] = collections.OrderedDict()
    for cit in citations:
        per_class.setdefault(cit.class_path, []).append(cit)

    grouped: dict[str, list[str]] = collections.OrderedDict()
    for class_path in per_class:
        grouped.setdefault(class_path.split("/")[1], []).append(class_path)

    out: dict[Path, str] = {}
    for part, class_paths in grouped.items():
        total = sum(len(per_class[c]) for c in class_paths)
        lines = [
            f"# Fuentes de la {parts.get(part, part)}",
            "",
            "Generado por `python scripts/verify-sources --write`. No editar a mano.",
            "",
            f"{len(class_paths)} clases · **{total} fuentes citadas**. Cada una indica el uso que esa",
            "clase hace de la obra y su localizador resoluble. ✅ verificada contra su autoridad ·",
            "⏳ pendiente, con el motivo en [`sources/PENDING.md`](../../sources/PENDING.md).",
            "",
            f"[← Índice de fuentes](../FUENTES.md) · [Índice de la parte](../../classes/{part}/README.md)",
            "",
        ]
        for class_path in class_paths:
            titulo = titles.get(class_path, class_path)
            rel = "../../" + class_path
            lines.append(f"## [{titulo}]({rel})")
            lines.append("")
            for cit in per_class[class_path]:
                lines.append(_source_line(cit, by_identity.get(cit.identity)))
            lines.append("")
        out[PARTS_DIR / f"{part}.md"] = "\n".join(lines).rstrip() + "\n"
    return out


def render_index(data: dict, citations: list[Citation], root: Path = ROOT) -> str:
    """Indice: que fundamenta cada parte y donde mirar clase a clase."""
    by_identity = {e.get("identity"): e for e in data.get("entries", [])}
    parts = part_titles(root)

    per_part: dict[str, list[Citation]] = collections.OrderedDict()
    for cit in citations:
        per_part.setdefault(cit.class_path.split("/")[1], []).append(cit)

    total_ok = sum(1 for e in data.get("entries", []) if e.get("status") == "verificada")
    lines = [
        "# Fuentes que fundamentan cada clase",
        "",
        "Generado por `python scripts/verify-sources --write`. No editar a mano.",
        "",
        "Las 288 clases del programa no afirman nada por su cuenta: cada afirmación se apoya en una",
        "obra citada, y cada obra tiene aquí su localizador. Esta es la vista legible; la fuente de",
        "verdad comprobable es [`sources/bibliography.json`](../sources/bibliography.json), que",
        "`python scripts/verify-sources` valida en CI sin tocar la red.",
        "",
        f"**{len(citations)} citas** sobre **{len(data.get('entries', []))} obras distintas**. "
        f"**{total_ok} verificadas** contra su autoridad; el resto figura, con su motivo, en "
        "[`sources/PENDING.md`](../sources/PENDING.md).",
        "",
        "| Parte | Clases | Fuentes citadas | Obras que la ordenan | Detalle |",
        "|---|---:|---:|---|---|",
    ]
    for part, cits in per_part.items():
        clases = len({c.class_path for c in cits})
        libros: collections.Counter[str] = collections.Counter()
        otras: collections.Counter[str] = collections.Counter()
        for cit in cits:
            entry = by_identity.get(cit.identity)
            if not entry:
                continue
            if entry.get("type") == "book":
                libros[entry["title"]] += 1
            else:
                otras[f"{entry['authority']}: {entry['title']}"] += 1
        # Hay partes que se apoyan en documentacion oficial y no en libros. Decir
        # "—" ahi seria falso: lo que las funda existe, solo que no es un libro.
        top = libros.most_common(2) or otras.most_common(2)
        rectoras = " · ".join(f"*{t}*" for t, _ in top) or "—"
        titulo = parts.get(part, part).replace("Parte ", "")
        lines.append(f"| {titulo} | {clases} | {len(cits)} | {rectoras} | [ver](fuentes/{part}.md) |")
    lines.append("")
    return "\n".join(lines).rstrip() + "\n"
