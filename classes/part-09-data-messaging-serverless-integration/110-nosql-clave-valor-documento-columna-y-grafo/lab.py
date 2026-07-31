"""Executable lab for lesson 110."""

from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "src"))

from multicloud_program.labs import main

if __name__ == "__main__":
    raise SystemExit(main(lesson_id="110", kind="data", title='NoSQL: clave-valor, documento, columna y grafo', artifact="matriz-nosql"))
