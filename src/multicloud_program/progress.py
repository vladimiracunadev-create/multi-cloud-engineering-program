"""Portable learning progress and completion certificates."""
from __future__ import annotations
import html
import json
from datetime import date
from pathlib import Path

def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8")) if path.exists() else {"completed": [], "checkpoints": []}

def mark(path: Path, lesson_id: str) -> dict:
    data = load(path); data["completed"] = sorted(set(data["completed"] + [lesson_id])); path.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8"); return data

def certificate(path: Path, learner: str, completed: int, total: int = 288) -> Path:
    if completed < total: raise ValueError(f"completion required: {completed}/{total}")
    path.write_text(f'''<!doctype html><meta charset="utf-8"><title>Certificado</title><style>body{{font-family:Arial;text-align:center;padding:10vh;color:#102a43}}main{{border:8px double #007c83;padding:8vh}}h1{{font-size:42px}}p{{font-size:20px}}</style><main><h1>Certificado de finalización</h1><p>Se certifica que</p><h2>{html.escape(learner)}</h2><p>completó 24 partes, 288 clases, checkpoints y defensa del Multi-Cloud Engineering Program.</p><p>{date.today().isoformat()} · Verificación mediante paquete de evidencia</p></main>''', encoding="utf-8")
    return path
