"""Localiza los diagramas ya renderizados.

Fuente unica para los tres consumidores —el portal, el manual y el
pre-renderizador—, para que el nombre de un diagrama se calcule igual en todos
y no haya que mantener un indice.
"""

from __future__ import annotations

import hashlib
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DIAGRAMS = ROOT / "curriculum" / "diagrams"

MERMAID_BLOCK = re.compile(r"^```mermaid\n(.*?)^```", re.MULTILINE | re.DOTALL)


def digest(source: str) -> str:
    normalized = source.replace("\r\n", "\n").replace("\r", "\n").strip()
    return hashlib.sha256(normalized.encode("utf-8")).hexdigest()[:16]


def rendered(source: str, extension: str) -> Path | None:
    path = DIAGRAMS / f"{digest(source)}.{extension}"
    return path if path.exists() else None
