"""Executable lab for lesson 284."""

from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "src"))

from multicloud_program.labs import main

if __name__ == "__main__":
    raise SystemExit(main(lesson_id="284", kind="capstone", title='Capstone datos e IA: plataforma gobernada', artifact="data-ai-capstone"))
