"""Executable lab for lesson 282."""

from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "src"))

from multicloud_program.labs import main

if __name__ == "__main__":
    raise SystemExit(main(lesson_id="282", kind="capstone", title='Capstone industria: IoT, edge y operación desconectada', artifact="industry-capstone"))
