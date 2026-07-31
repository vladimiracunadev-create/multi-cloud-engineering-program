"""Executable lab for lesson 182."""

from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "src"))

from multicloud_program.labs import main

if __name__ == "__main__":
    raise SystemExit(main(lesson_id="182", kind="architecture", title='Contexto, contenedores, componentes y código con C4', artifact="c4-model"))
