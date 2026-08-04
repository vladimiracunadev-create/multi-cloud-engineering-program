"""Pre-render every Mermaid diagram of the course to SVG and PNG.

Why pre-render instead of drawing them in the browser: el manual en PDF no
ejecuta JavaScript —los diagramas salian como texto— y la aplicacion Android
funciona sin conexion, asi que cargar Mermaid desde un CDN los dejaba en blanco.
Renderizados una vez, las tres superficies muestran lo mismo y ninguna depende
de la red.

Los ficheros se nombran por el hash de su fuente, de modo que solo se vuelve a
renderizar lo que cambia y los generadores pueden encontrarlos sin indice.

Usage:
    python scripts/render_diagrams.py [--force] [--mmdc PATH]
"""

from __future__ import annotations

import argparse
import hashlib
import os
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CLASSES = ROOT / "classes"
DIAGRAMS = ROOT / "curriculum" / "diagrams"

MERMAID_BLOCK = re.compile(r"^```mermaid\n(.*?)^```", re.MULTILINE | re.DOTALL)

# Tema claro: las cajas llevan su propio fondo, asi que el mismo dibujo se lee
# sobre el portal oscuro, sobre el portal claro y sobre el papel del manual.
CONFIG = """{
  "theme": "neutral",
  "themeVariables": {
    "fontFamily": "Inter, Segoe UI, Helvetica, sans-serif",
    "fontSize": "15px",
    "primaryColor": "#eef2ef",
    "primaryTextColor": "#12160f",
    "primaryBorderColor": "#59c88b",
    "lineColor": "#5c6b60",
    "tertiaryColor": "#f7f4ea"
  },
  "flowchart": {"htmlLabels": true, "curve": "basis", "padding": 12},
  "sequence": {"useMaxWidth": true},
  "maxTextSize": 90000
}
"""


def digest(source: str) -> str:
    normalized = source.replace("\r\n", "\n").replace("\r", "\n").strip()
    return hashlib.sha256(normalized.encode("utf-8")).hexdigest()[:16]


def collect() -> dict[str, str]:
    """Todos los diagramas del curso, indexados por el hash de su fuente."""
    found: dict[str, str] = {}
    for readme in sorted(CLASSES.rglob("README.md")):
        for block in MERMAID_BLOCK.findall(readme.read_text(encoding="utf-8")):
            found.setdefault(digest(block), block.strip())
    return found


def find_mmdc(explicit: str | None) -> str:
    if explicit:
        return explicit
    for candidate in (
        os.environ.get("MMDC"),
        shutil.which("mmdc"),
        ROOT / "node_modules" / ".bin" / ("mmdc.cmd" if os.name == "nt" else "mmdc"),
    ):
        if candidate and Path(candidate).exists():
            return str(candidate)
    raise SystemExit(
        "no se encontro mmdc; instala @mermaid-js/mermaid-cli "
        "(npm install @mermaid-js/mermaid-cli) o pasa --mmdc"
    )


def render_batch(mmdc: str, items: list[tuple[str, str]], extension: str, background: str) -> int:
    """Un solo proceso para todo el lote: abrir un navegador por diagrama
    tardaba minutos, y en un documento con todos tarda segundos."""
    if not items:
        return 0
    written = 0
    with tempfile.TemporaryDirectory() as tmp:
        work = Path(tmp)
        (work / "config.json").write_text(CONFIG, encoding="utf-8")
        document = "\n".join(f"```mermaid\n{source}\n```\n" for _, source in items)
        (work / "batch.md").write_text(document, encoding="utf-8")
        command = [
            mmdc,
            "-i", str(work / "batch.md"),
            "-o", str(work / "out.md"),
            "-c", str(work / "config.json"),
            "-b", background,
            "-e", extension,
        ]
        if extension == "png":
            command += ["-w", "1600"]
        result = subprocess.run(command, capture_output=True, text=True, cwd=work)
        if result.returncode != 0:
            sys.stderr.write(result.stdout + "\n" + result.stderr + "\n")
            raise SystemExit(f"mmdc fallo al renderizar {extension}")
        for index, (name, _) in enumerate(items, start=1):
            produced = work / f"out-{index}.{extension}"
            if not produced.exists():
                raise SystemExit(f"mmdc no genero {produced.name} para {name}")
            (DIAGRAMS / f"{name}.{extension}").write_bytes(produced.read_bytes())
            written += 1
    return written


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--force", action="store_true", help="rehace todos los diagramas")
    parser.add_argument("--mmdc", help="ruta al ejecutable de mermaid-cli")
    args = parser.parse_args()

    DIAGRAMS.mkdir(parents=True, exist_ok=True)
    diagrams = collect()

    pending_svg = [
        (name, source) for name, source in sorted(diagrams.items())
        if args.force or not (DIAGRAMS / f"{name}.svg").exists()
    ]
    pending_png = [
        (name, source) for name, source in sorted(diagrams.items())
        if args.force or not (DIAGRAMS / f"{name}.png").exists()
    ]

    if pending_svg or pending_png:
        mmdc = find_mmdc(args.mmdc)
        render_batch(mmdc, pending_svg, "svg", "transparent")
        render_batch(mmdc, pending_png, "png", "white")

    # Lo que ya no usa ningun README deja de ocupar sitio en el repositorio.
    keep = {f"{name}.{extension}" for name in diagrams for extension in ("svg", "png")}
    removed = 0
    for stale in DIAGRAMS.iterdir():
        if stale.name not in keep:
            stale.unlink()
            removed += 1

    print(
        f"Diagramas: {len(diagrams)} unicos; "
        f"{len(pending_svg)} SVG y {len(pending_png)} PNG generados, {removed} retirados."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
