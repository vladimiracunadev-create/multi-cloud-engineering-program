"""Validate structural and pedagogical contracts of the repository."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]
REQUIRED = {"README.md", "assessment.md", "lesson.yaml", "lab.py"}
SECTIONS = [
    "## 🎯 Propósito",
    "## 📚 Resultados de aprendizaje",
    "## 🧪 Laboratorio guiado",
    "## 🏆 Reto verificable",
    "## ✅ Criterio de aceptación",
    "## ⚠️ Errores frecuentes",
    "## 🔗 Referencias",
]


def authored_lessons(errors: list[str]) -> set[str]:
    """Check curriculum/lessons/*.json parses and only uses known fields.

    CI never runs generate_course.py — the generated READMEs are committed — so
    a malformed lesson file would otherwise pass every check while its content
    silently failed to reach the curriculum.
    """
    folder = ROOT / "curriculum" / "lessons"
    if not folder.is_dir():
        return set()
    known = {
        "id", "purpose", "outcomes", "concepts", "diagram", "foundations",
        "worked_example", "pitfalls", "checks", "references",
    }
    ids: set[str] = set()
    for path in sorted(folder.glob("*.json")):
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
        except json.JSONDecodeError as exc:
            errors.append(f"curriculum/lessons/{path.name}: invalid JSON ({exc})")
            continue
        unknown = set(data) - known
        if unknown:
            errors.append(f"curriculum/lessons/{path.name}: unknown keys {sorted(unknown)}")
        if data.get("id") != path.stem:
            errors.append(f"curriculum/lessons/{path.name}: id does not match the file name")
        for ref in data.get("references", []):
            if not ref.get("text"):
                errors.append(f"curriculum/lessons/{path.name}: a reference has no text")
        ids.add(path.stem)
    return ids


def validate(strict: bool = False) -> list[str]:
    errors: list[str] = []
    written = authored_lessons(errors)
    catalog_path = ROOT / "curriculum" / "catalog.json"
    if not catalog_path.exists():
        return ["missing curriculum/catalog.json"]
    catalog = json.loads(catalog_path.read_text(encoding="utf-8"))
    expected_lessons = 288
    expected_parts = 24
    if len(catalog) != expected_lessons:
        errors.append(f"expected {expected_lessons} catalog entries, found {len(catalog)}")
    if len({x["id"] for x in catalog}) != len(catalog):
        errors.append("catalog contains duplicate lesson ids")
    if [x["id"] for x in catalog] != [f"{n:03d}" for n in range(1, expected_lessons + 1)]:
        errors.append(f"lesson ids are not contiguous from 001 to {expected_lessons}")

    for item in catalog:
        folder = ROOT / "classes" / f"part-{item['part']}-{item['part_slug']}" / f"{item['id']}-{item['slug']}"
        if not folder.is_dir():
            errors.append(f"missing lesson directory: {folder.relative_to(ROOT)}")
            continue
        found = {p.name for p in folder.iterdir() if p.is_file()}
        missing = REQUIRED - found
        if missing:
            errors.append(f"{item['id']}: missing {sorted(missing)}")
            continue
        readme = (folder / "README.md").read_text(encoding="utf-8")
        for section in SECTIONS:
            if section not in readme:
                errors.append(f"{item['id']}: missing section {section}")
        if item["id"] in written:
            # El README está commiteado, así que hay que comprobar que se
            # regeneró después de escribir el contenido: si no, el curso
            # publicaría la plantilla mientras el JSON dice otra cosa.
            data = json.loads(
                (ROOT / "curriculum" / "lessons" / f"{item['id']}.json").read_text(encoding="utf-8")
            )
            for heading in (f["heading"] for f in data.get("foundations", [])):
                if heading not in readme:
                    errors.append(
                        f"{item['id']}: README no incluye «{heading}»; "
                        "ejecuta scripts/generate_course.py"
                    )
                    break
        yaml_text = (folder / "lesson.yaml").read_text(encoding="utf-8")
        if f"id: '{item['id']}'" not in yaml_text:
            errors.append(f"{item['id']}: lesson.yaml id mismatch")
        if strict and len(readme.split()) < 700:
            errors.append(f"{item['id']}: lesson is too short for strict mode")
        for pack in ("starter", "solution", "evidence"):
            if not (folder / pack / "README.md").exists():
                errors.append(f"{item['id']}: missing {pack} pack")

    part_indexes = list((ROOT / "classes").glob("part-*/README.md"))
    if len(part_indexes) != expected_parts:
        errors.append(f"expected {expected_parts} part indexes, found {len(part_indexes)}")

    for path in ROOT.rglob("*.md"):
        if any(part in {".git", "tmp", "node_modules", ".venv", ".site-deps"} for part in path.parts):
            continue
        text = path.read_text(encoding="utf-8")
        if re.search(r"\b(TODO|TBD|FIXME)\b", text):
            errors.append(f"placeholder marker in {path.relative_to(ROOT)}")
        for target in re.findall(r"(?<!!)\[[^]]+\]\(([^)]+)\)", text):
            target = unquote(target.split("#", 1)[0].strip())
            if not target or "://" in target or target.startswith(("mailto:", "#")):
                continue
            resolved = (path.parent / target).resolve()
            try:
                resolved.relative_to(ROOT.resolve())
            except ValueError:
                errors.append(f"link escapes repository in {path.relative_to(ROOT)}: {target}")
                continue
            if not resolved.exists():
                errors.append(f"broken link in {path.relative_to(ROOT)}: {target}")
    required_surfaces = ["projects/cloudshop/app.py", "assessments/diagnostic.json", "docs/INSTRUCTOR_GUIDE.md", "docs/STUDENT_GUIDE.md", "apps/desktop/app.py", "output/pdf/multi-cloud-engineering-manual-v2.0.pdf", "output/pptx/multi-cloud-engineering-program-v2.0.pptx"]
    for relative in required_surfaces:
        if not (ROOT / relative).exists(): errors.append(f"missing program surface: {relative}")
    dated = json.loads((ROOT / "data/cloud-catalog-2026-07.json").read_text(encoding="utf-8"))
    if not dated.get("as_of") or not dated.get("policy"): errors.append("cloud catalog lacks version policy")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--strict", action="store_true")
    args = parser.parse_args()
    errors = validate(args.strict)
    if errors:
        print("Validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1
    escritas = len(list((ROOT / "curriculum" / "lessons").glob("*.json")))
    print(
        f"Repository valid: 288 lessons, 24 parts, class contracts complete "
        f"({escritas}/288 con contenido propio)."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
