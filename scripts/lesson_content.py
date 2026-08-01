"""Per-lesson authored content, kept apart from the generator template.

The 288 lessons started life as a single f-string with the title interpolated
into it: every class shared the same three "Desarrollo" headings, the same
worked example numbers and the same four books. That reads as 288 lessons and
measures as one.

Authored content lives in ``curriculum/lessons/<id>.json`` and is merged by
``generate_course.py``. A lesson without a file keeps the old template, so the
curriculum stays buildable while the rewrite advances part by part.

JSON on purpose: CI installs only the ``site`` and ``manual`` extras, so the
generator must not grow a YAML dependency.

Schema (every key optional; absent keys fall back to the template):

    {
      "purpose":  "one paragraph stating what the lesson makes the reader able to do",
      "outcomes": ["verb-first, verifiable", ...],
      "concepts": [{"term": "...", "definition": "its own definition, not the title"}],
      "diagram":  "mermaid body, without the ```mermaid fence",
      "foundations": [{"heading": "...", "body": "markdown, topic specific"}],
      "worked_example": "markdown with real numbers worked through",
      "pitfalls": [{"symptom": "...", "cause": "...", "fix": "..."}],
      "checks":   ["comprehension question", ...],
      "references": [{"text": "Author, Title (year), chapter", "url": "https://..."}]
    }
"""

from __future__ import annotations

import json
from functools import lru_cache
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LESSONS = ROOT / "curriculum" / "lessons"

FIELDS = (
    "purpose", "outcomes", "concepts", "diagram", "foundations",
    "worked_example", "pitfalls", "checks", "references",
)


@lru_cache(maxsize=1)
def _index() -> dict[str, dict]:
    if not LESSONS.is_dir():
        return {}
    out: dict[str, dict] = {}
    for path in sorted(LESSONS.glob("*.json")):
        data = json.loads(path.read_text(encoding="utf-8"))
        unknown = set(data) - set(FIELDS) - {"id"}
        if unknown:
            raise ValueError(f"{path.name}: unknown keys {sorted(unknown)}")
        out[path.stem] = data
    return out


def content(lesson_id: str) -> dict:
    """Authored content for a lesson, or an empty dict when not written yet."""
    return _index().get(lesson_id, {})


def authored_ids() -> set[str]:
    return set(_index())


def coverage() -> tuple[int, int]:
    """(lessons with authored content, lessons on disk)."""
    total = len(list((ROOT / "classes").glob("part-*/*/README.md")))
    return len(_index()), total
