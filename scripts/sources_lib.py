"""Parseo determinista del bloque de Referencias de las clases.

Este modulo es la unica fuente de verdad sobre como se lee una cita en el
programa. Lo comparten el extractor, el verificador offline y el refrescador en
red, de forma que los tres cuenten exactamente lo mismo.

No hace red, no escribe ficheros y no depende de nada fuera de la biblioteca
estandar: el verificador tiene que poder correr en CI sin instalar nada.
"""

from __future__ import annotations

import collections
import hashlib
import json
import re
import unicodedata
from dataclasses import dataclass, field
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / "sources" / "bibliography.json"
SCHEMA_VERSION = 1

# El bloque de referencias de cada clase: encabezado fijo hasta la regla horizontal.
SECTION_RE = re.compile(r"^## \U0001f517 Referencias\s*$(.*?)^---\s*$", re.S | re.M)

# Ultima linea generica de cada clase: es una instruccion al lector, no una obra.
BOILERPLATE = "Documentacion oficial vigente"

URL_RE = re.compile(r"<(https?://[^>\s]+)>")
ITALIC_RE = re.compile(r"\*([^*]{2,})\*")
AUTHOR_YEAR_RE = re.compile(r"^(?P<authors>.+?)\s*\((?P<year>\d{4})\)\.\s*")
EM_DASH = "—"

# Hosts que identifican una obra editorial (libro) mas que una pagina web.
BOOK_HOSTS = ("oreilly.com", "openlibrary.org", "manning.com", "pragprog.com")

# Hosts cuya publicacion es un articulo con DOI o preprint.
PAPER_HOSTS = ("doi.org", "dl.acm.org", "arxiv.org", "ieeexplore.ieee.org", "link.springer.com")

# Hosts que publican normas y especificaciones formales.
STANDARD_HOSTS = (
    "rfc-editor.org",
    "ietf.org",
    "csrc.nist.gov",
    "nvlpubs.nist.gov",
    "iso.org",
    "pubs.opengroup.org",
    "opencontainers.org",
    "w3.org",
    "unicode.org",
    "pcisecuritystandards.org",
)

# Autoridad que responde por cada host. Lo que no este aqui se deriva del dominio.
AUTHORITY_BY_HOST = {
    "docs.aws.amazon.com": "Amazon Web Services",
    "aws.amazon.com": "Amazon Web Services",
    "aws.github.io": "Amazon Web Services",
    "learn.microsoft.com": "Microsoft Azure",
    "azure.microsoft.com": "Microsoft Azure",
    "docs.microsoft.com": "Microsoft Azure",
    "techcommunity.microsoft.com": "Microsoft Azure",
    "cloud.google.com": "Google Cloud",
    "research.google": "Google Cloud",
    "sre.google": "Google Cloud",
    "developers.google.com": "Google Cloud",
    "kubernetes.io": "Kubernetes / CNCF",
    "kubernetes-sigs.github.io": "Kubernetes / CNCF",
    "etcd.io": "Kubernetes / CNCF",
    "helm.sh": "Kubernetes / CNCF",
    "istio.io": "Kubernetes / CNCF",
    "prometheus.io": "Kubernetes / CNCF",
    "opentelemetry.io": "Kubernetes / CNCF",
    "argo-cd.readthedocs.io": "Kubernetes / CNCF",
    "argoproj.github.io": "Kubernetes / CNCF",
    "cilium.io": "Kubernetes / CNCF",
    "www.cncf.io": "Kubernetes / CNCF",
    "cncf.io": "Kubernetes / CNCF",
    "developer.hashicorp.com": "HashiCorp",
    "www.hashicorp.com": "HashiCorp",
    "opentofu.org": "HashiCorp / OpenTofu",
    "docs.docker.com": "Docker / OCI",
    "specs.opencontainers.org": "Docker / OCI",
    "github.com": "Proyecto de codigo abierto",
    "docs.github.com": "GitHub",
    "www.rfc-editor.org": "IETF / RFC Editor",
    "rfc-editor.org": "IETF / RFC Editor",
    "datatracker.ietf.org": "IETF / RFC Editor",
    "csrc.nist.gov": "NIST",
    "nvlpubs.nist.gov": "NIST",
    "www.nist.gov": "NIST",
    "ieeexplore.ieee.org": "IEEE",
    "doi.org": "Editorial academica (DOI)",
    "dl.acm.org": "ACM",
    "arxiv.org": "arXiv",
    "www.oreilly.com": "Editorial (libro)",
    "oreilly.com": "Editorial (libro)",
    "www.usenix.org": "USENIX",
    "owasp.org": "OWASP",
    "cheatsheetseries.owasp.org": "OWASP",
    "www.cisa.gov": "CISA",
    "cisa.gov": "CISA",
    "www.finops.org": "FinOps Foundation",
    "finops.org": "FinOps Foundation",
    "martinfowler.com": "Autor de referencia",
    "man7.org": "Linux man-pages",
    "www.kernel.org": "Linux kernel",
    "git-scm.com": "Proyecto Git",
    "www.postgresql.org": "PostgreSQL",
    "kafka.apache.org": "Apache Software Foundation",
    "www.freedesktop.org": "freedesktop.org / systemd",
}

# Agrupacion de autoridades para la tabla del README.
AUTHORITY_GROUPS = [
    ("AWS", ("Amazon Web Services",)),
    ("Azure", ("Microsoft Azure",)),
    ("GCP", ("Google Cloud",)),
    ("Kubernetes y CNCF", ("Kubernetes / CNCF",)),
    ("HashiCorp y OpenTofu", ("HashiCorp", "HashiCorp / OpenTofu")),
    ("Docker y OCI", ("Docker / OCI",)),
    ("RFC e IETF", ("IETF / RFC Editor",)),
    ("NIST, IEEE y normas", ("NIST", "IEEE", "ISO", "The Open Group", "W3C", "PCI SSC")),
    ("Libros", ("Editorial (libro)",)),
    ("Artículos académicos", ("Editorial academica (DOI)", "ACM", "arXiv", "USENIX", "IEEE Xplore", "queue.acm.org")),
    ("Seguridad (OWASP, CISA, MITRE)", ("OWASP", "CISA", "attack.mitre.org")),
    ("FinOps Foundation", ("FinOps Foundation",)),
    (
        "Proyectos de código abierto",
        (
            "Proyecto de codigo abierto",
            "GitHub",
            "Proyecto Git",
            "Linux man-pages",
            "Linux kernel",
            "freedesktop.org / systemd",
            "Apache Software Foundation",
            "PostgreSQL",
        ),
    ),
]


def _strip_accents(text: str) -> str:
    return "".join(c for c in unicodedata.normalize("NFD", text) if unicodedata.category(c) != "Mn")


def slugify(text: str, limit: int = 64) -> str:
    """kebab-case estable, sin acentos ni signos, recortado por palabra."""
    base = _strip_accents(text).lower()
    base = re.sub(r"[^a-z0-9]+", "-", base).strip("-")
    if len(base) <= limit:
        return base or "sin-titulo"
    cut = base[:limit]
    if "-" in cut:
        cut = cut[: cut.rfind("-")]
    return cut.strip("-") or "sin-titulo"


def normalize_url(url: str) -> str:
    """Forma canonica de una URL para comparar identidad de obra.

    Se descarta el fragmento: dos clases que citan secciones distintas de la
    misma pagina citan la misma obra, y el uso concreto queda registrado aparte.
    """
    url = url.strip().rstrip(").,;")
    url = re.sub(r"^http://", "https://", url)
    url = re.sub(r"^https://www\.", "https://", url)
    url = url.split("#")[0]
    return url.rstrip("/")


def host_of(url: str) -> str:
    return re.sub(r"^https?://", "", url).split("/")[0].lower()


def authority_for(url: str | None, kind: str) -> str:
    if not url:
        return "Editorial (libro)" if kind == "book" else "Sin autoridad declarada"
    host = host_of(url)
    if host in AUTHORITY_BY_HOST:
        return AUTHORITY_BY_HOST[host]
    bare = host[4:] if host.startswith("www.") else host
    if bare in AUTHORITY_BY_HOST:
        return AUTHORITY_BY_HOST[bare]
    return bare


@dataclass
class Citation:
    """Una aparicion concreta de una obra dentro de una clase."""

    class_path: str
    raw: str
    authors: list[str] = field(default_factory=list)
    year: str | None = None
    title: str = ""
    detail: str = ""
    use: str = ""
    url: str | None = None

    @property
    def kind(self) -> str:
        """Tipo segun la forma del localizador, no segun el tema."""
        if self.url:
            host = host_of(self.url)
            bare = host[4:] if host.startswith("www.") else host
            if any(bare.endswith(h) for h in BOOK_HOSTS):
                return "book"
            if any(bare.endswith(h) for h in PAPER_HOSTS):
                return "paper"
            if any(bare.endswith(h) for h in STANDARD_HOSTS):
                return "standard"
            return "reference"
        return "book"

    @property
    def identity(self) -> str:
        """Clave que decide si dos citas son la misma obra.

        Los libros se identifican por autor y titulo porque la misma obra se
        cita unas veces con enlace comercial y otras sin el. Todo lo demas se
        identifica por su localizador, que ya es unico.
        """
        if self.kind == "book":
            surname = self.authors[0].split(",")[0].strip() if self.authors else ""
            # El subtitulo se descarta: "Cloud Strategy" y "Cloud Strategy: A
            # Decision-Based Approach" son el mismo libro citado de dos formas.
            main_title = self.title.split(":")[0].strip()
            return "book::" + slugify(f"{surname} {main_title}", 200)
        return "url::" + normalize_url(self.url or "")


def parse_citation(class_path: str, line: str) -> Citation:
    """Convierte una linea de vinneta en una cita estructurada."""
    text = line.strip()
    if text.startswith("- "):
        text = text[2:]
    text = text.strip()

    urls = URL_RE.findall(text)
    url = normalize_url(urls[-1]) if urls else None
    body = URL_RE.sub("", text).strip().rstrip(".").strip()

    cit = Citation(class_path=class_path, raw=line.strip(), url=url)

    match = AUTHOR_YEAR_RE.match(body)
    if match:
        cit.year = match.group("year")
        cit.authors = split_authors(match.group("authors"))
        body = body[match.end() :].strip()
    else:
        # Citas sin anio ("Kerrisk, M. *signal(7)* - ..."): la autoria es el
        # tramo previo a la cursiva, solo si tiene forma de "Apellido, N.".
        head = ITALIC_RE.split(body)[0]
        if re.fullmatch(r"[^*]{0,60}?[A-Z][\w'’.-]+,\s*[A-Z]\.\s*", head or ""):
            cit.authors = split_authors(head)
            body = body[len(head) :].strip()

    italic = ITALIC_RE.search(body)
    if italic:
        cit.title = italic.group(1).strip()
        rest = (body[: italic.start()] + " " + body[italic.end() :]).strip()
    else:
        # Citas sin cursiva (por ejemplo "RFC 8555 - ACME"): el titulo es el
        # texto hasta la nota de uso.
        rest = ""
        cit.title = body.strip()

    if EM_DASH in rest:
        head, _, tail = rest.partition(EM_DASH)
        cit.detail = head.strip(" ,.;:")
        cit.use = tail.strip(" ,.;:")
    elif EM_DASH in cit.title:
        head, _, tail = cit.title.partition(EM_DASH)
        cit.title = head.strip(" ,.;:")
        cit.use = tail.strip(" ,.;:")
        cit.detail = rest.strip(" ,.;:")
    else:
        cit.detail = rest.strip(" ,.;:")

    if not cit.authors and cit.detail and not cit.title:
        cit.title = cit.detail
        cit.detail = ""
    return cit


def split_authors(blob: str) -> list[str]:
    """Separa la cadena de autoria en nombres individuales."""
    blob = blob.strip()
    if not blob:
        return []
    # Primero los separadores explicitos, luego la coma que separa dos unidades
    # "Apellido, N." consecutivas (sin tocar la coma interna de cada nombre).
    parts: list[str] = []
    for chunk in re.split(r"\s+y\s+|\s*;\s*|\s+and\s+", blob):
        # La coma solo separa si lo que sigue es otro "Apellido, N." completo;
        # se exige minuscula en el apellido para no partir "Brealey, R.".
        parts.extend(re.split(r",\s*(?=[A-ZÀ-Ý][\w'’-]*[a-zà-ÿ][\w'’-]*,\s*[A-ZÀ-Ý]\.)", chunk))
    out: list[str] = []
    for part in parts:
        part = part.strip(" ,.").strip()
        if not part:
            continue
        # Se restituye el punto de la inicial: "Ross, K" -> "Ross, K."
        if re.search(r",\s*[A-Z](\.\s*[A-Z])*$", part):
            part += "."
        out.append(part)
    return out


def class_readmes(root: Path = ROOT) -> list[Path]:
    """Las 288 clases, en orden estable. Solo el README de la clase, no los packs."""
    return sorted(p for p in root.glob("classes/*/*/README.md"))


def references_block(text: str) -> str | None:
    match = SECTION_RE.search(text)
    return match.group(1) if match else None


def read_citations(root: Path = ROOT) -> tuple[list[Citation], dict[str, str]]:
    """Devuelve todas las citas del programa y el bloque literal de cada clase."""
    citations: list[Citation] = []
    blocks: dict[str, str] = {}
    for path in class_readmes(root):
        rel = path.relative_to(root).as_posix()
        block = references_block(path.read_text(encoding="utf-8"))
        if block is None:
            blocks[rel] = ""
            continue
        lines = [ln.strip() for ln in block.splitlines() if ln.strip().startswith("- ")]
        blocks[rel] = "\n".join(lines)
        for line in lines:
            if _strip_accents(line).startswith("- " + BOILERPLATE) or BOILERPLATE in _strip_accents(line):
                continue
            citations.append(parse_citation(rel, line))
    return citations, blocks


def isbn13_ok(value: str) -> bool:
    """Digito de control de un ISBN-13 (EAN-13)."""
    digits = re.sub(r"[^0-9]", "", value or "")
    if len(digits) != 13:
        return False
    total = sum(int(d) * (1 if i % 2 == 0 else 3) for i, d in enumerate(digits[:12]))
    return (10 - total % 10) % 10 == int(digits[12])


def canonical_locator(entry: dict) -> str | None:
    """Forma canonica exigida por el tipo de la entrada."""
    kind = entry.get("type")
    if kind == "book":
        isbn = entry.get("isbn13")
        return f"https://openlibrary.org/isbn/{isbn}" if isbn else None
    if kind == "paper":
        doi = entry.get("doi")
        return f"https://doi.org/{doi}" if doi else None
    if entry.get("doi"):
        return f"https://doi.org/{entry['doi']}"
    return entry.get("locator")


def part_titles(root: Path = ROOT) -> dict[str, str]:
    """Titulo legible de cada parte, leido de su propio indice."""
    titles: dict[str, str] = {}
    for path in sorted(root.glob("classes/part-*/README.md")):
        first = path.read_text(encoding="utf-8").splitlines()[0]
        titles[path.parent.name] = first.lstrip("# ").strip()
    return titles


def registry_stats(data: dict, citations: list[Citation], root: Path = ROOT) -> dict:
    """Todas las cifras que el README publica. Nadie las escribe a mano."""
    entries = data.get("entries", [])
    by_status = collections.Counter(e.get("status") for e in entries)
    by_type = collections.Counter(e.get("type") for e in entries)

    cites_per_entry: collections.Counter[str] = collections.Counter()
    ident_to_entry = {e.get("identity"): e for e in entries}
    for cit in citations:
        entry = ident_to_entry.get(cit.identity)
        if entry:
            cites_per_entry[entry["id"]] += 1

    grouped: list[dict] = []
    assigned: set[str] = set()
    for label, authorities in AUTHORITY_GROUPS:
        members = [e for e in entries if e.get("authority") in authorities]
        if not members:
            continue
        assigned.update(e["id"] for e in members)
        grouped.append(
            {
                "label": label,
                "entries": len(members),
                "citations": sum(cites_per_entry[e["id"]] for e in members),
                "verified": sum(1 for e in members if e.get("status") == "verificada"),
            }
        )
    rest = [e for e in entries if e["id"] not in assigned]
    if rest:
        grouped.append(
            {
                "label": "Otras autoridades",
                "entries": len(rest),
                "citations": sum(cites_per_entry[e["id"]] for e in rest),
                "verified": sum(1 for e in rest if e.get("status") == "verificada"),
            }
        )

    # Obras rectoras: los libros mas citados de cada parte, derivados del uso real.
    titles = part_titles(root)
    books = [e for e in entries if e.get("type") == "book"]
    areas: list[dict] = []
    for part, title in titles.items():
        ranked = []
        for book in books:
            hits = sum(1 for u in book.get("used_in", []) if f"/{part}/" in u)
            if hits:
                ranked.append((hits, book))
        if not ranked:
            continue
        ranked.sort(key=lambda p: (-p[0], p[1]["title"]))
        areas.append({"part": part, "title": title, "books": [b for _, b in ranked[:3]]})

    return {
        "entries": len(entries),
        "citations": len(citations),
        # Cobertura real: citas cuya obra tiene entrada, no entradas sobre si mismas.
        "resolved": sum(1 for c in citations if c.identity in ident_to_entry),
        "classes": len({c.class_path for c in citations}),
        "verified": by_status.get("verificada", 0),
        "pending": by_status.get("pendiente", 0),
        "by_type": dict(by_type),
        "groups": grouped,
        "areas": areas,
        "with_use": sum(1 for c in citations if c.use),
        "verified_on": data.get("verified_on"),
    }


def _thousands(value: int) -> str:
    return f"{value:,}".replace(",", ".")


def render_badge(stats: dict) -> str:
    """Insignia con el total de obras del registro."""
    total = _thousands(stats["entries"])
    return (
        f"[![Fuentes](https://img.shields.io/badge/fuentes-{total.replace('.', '.')}"
        f"%20obras%20trazadas-1f6feb?style=for-the-badge)](sources/bibliography.json)"
    )


def render_block(stats: dict) -> str:
    """Tabla por autoridad y obras rectoras. Salida determinista."""
    lines: list[str] = []
    lines.append(
        f"El programa cita **{_thousands(stats['citations'])} veces** un total de "
        f"**{_thousands(stats['entries'])} obras distintas** a lo largo de las "
        f"**{stats['classes']} clases**. Cada una tiene entrada con localizador resoluble en "
        f"[`sources/bibliography.json`](sources/bibliography.json): "
        f"**{_thousands(stats['verified'])} verificadas** contra su autoridad y "
        f"**{_thousands(stats['pending'])} pendientes** con el motivo declarado."
    )
    lines.append("")
    verified_on = stats.get("verified_on") or "sin ejecutar"
    lines.append(f"Última comprobación en red: **{verified_on}**.")
    lines.append("")
    lines.append("| Autoridad | Obras | Citas | Verificadas |")
    lines.append("|---|---:|---:|---:|")
    for group in stats["groups"]:
        lines.append(
            f"| {group['label']} | {_thousands(group['entries'])} | "
            f"{_thousands(group['citations'])} | {_thousands(group['verified'])} |"
        )
    lines.append(
        f"| **Total** | **{_thousands(stats['entries'])}** | "
        f"**{_thousands(stats['citations'])}** | **{_thousands(stats['verified'])}** |"
    )
    lines.append("")
    lines.append("<details>")
    lines.append("<summary><b>Obras rectoras por parte</b> — libros que ordenan cada área</summary>")
    lines.append("")
    lines.append("| Parte | Obras rectoras |")
    lines.append("|---|---|")
    for area in stats["areas"]:
        works = " · ".join(f"*{b['title']}*" for b in area["books"])
        lines.append(f"| {area['title']} | {works} |")
    lines.append("")
    lines.append("</details>")
    return "\n".join(lines)


def load_registry(path: Path = REGISTRY) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def dump_registry(data: dict, path: Path = REGISTRY) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
