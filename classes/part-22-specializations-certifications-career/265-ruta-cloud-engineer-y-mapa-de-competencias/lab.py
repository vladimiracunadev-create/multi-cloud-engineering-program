"""Executable lab for lesson 265."""

from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "src"))

from multicloud_program.labs import main

if __name__ == "__main__":
    raise SystemExit(main(lesson_id="265", kind="decision", title='Ruta Cloud Engineer y mapa de competencias', artifact="cloud-engineer-plan"))
