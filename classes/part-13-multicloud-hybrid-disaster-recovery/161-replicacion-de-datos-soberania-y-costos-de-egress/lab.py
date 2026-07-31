"""Executable lab for lesson 161."""

from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "src"))

from multicloud_program.labs import main

if __name__ == "__main__":
    raise SystemExit(main(lesson_id="161", kind="data", title='Replicación de datos, soberanía y costos de egress', artifact="estrategia-datos-multicloud"))
