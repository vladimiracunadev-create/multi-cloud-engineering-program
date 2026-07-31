"""Executable lab for lesson 067."""

from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "src"))

from multicloud_program.labs import main

if __name__ == "__main__":
    raise SystemExit(main(lesson_id="067", kind="supply-chain", title='Registros, SBOM, firma y procedencia de imágenes', artifact="cadena-suministro-imagen"))
