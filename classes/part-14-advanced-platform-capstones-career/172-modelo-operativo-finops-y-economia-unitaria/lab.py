"""Executable lab for lesson 172."""

from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "src"))

from multicloud_program.labs import main

if __name__ == "__main__":
    raise SystemExit(main(lesson_id="172", kind="finops", title='Modelo operativo FinOps y economía unitaria', artifact="operating-model-finops"))
