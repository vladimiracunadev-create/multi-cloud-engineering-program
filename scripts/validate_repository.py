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


def validate(strict: bool = False) -> list[str]:
    errors: list[str] = []
    catalog_path = ROOT / "curriculum" / "catalog.json"
    if not catalog_path.exists():
        return ["missing curriculum/catalog.json"]
    catalog = json.loads(catalog_path.read_text(encoding="utf-8"))
    if len(catalog) != 180:
        errors.append(f"expected 180 catalog entries, found {len(catalog)}")
    if len({x["id"] for x in catalog}) != len(catalog):
        errors.append("catalog contains duplicate lesson ids")
    if [x["id"] for x in catalog] != [f"{n:03d}" for n in range(1, 181)]:
        errors.append("lesson ids are not contiguous from 001 to 180")

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
        yaml_text = (folder / "lesson.yaml").read_text(encoding="utf-8")
        if f"id: '{item['id']}'" not in yaml_text:
            errors.append(f"{item['id']}: lesson.yaml id mismatch")
        if strict and len(readme.split()) < 700:
            errors.append(f"{item['id']}: lesson is too short for strict mode")

    part_indexes = list((ROOT / "classes").glob("part-*/README.md"))
    if len(part_indexes) != 15:
        errors.append(f"expected 15 part indexes, found {len(part_indexes)}")

    for path in ROOT.rglob("*.md"):
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
    print("Repository valid: 180 lessons, 15 parts, class contracts complete.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
