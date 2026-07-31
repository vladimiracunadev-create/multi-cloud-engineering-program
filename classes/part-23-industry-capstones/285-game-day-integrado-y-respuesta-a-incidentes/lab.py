"""Executable lab for lesson 285."""

from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "src"))

from multicloud_program.labs import main

if __name__ == "__main__":
    raise SystemExit(main(lesson_id="285", kind="chaos", title='Game day integrado y respuesta a incidentes', artifact="final-gameday"))
