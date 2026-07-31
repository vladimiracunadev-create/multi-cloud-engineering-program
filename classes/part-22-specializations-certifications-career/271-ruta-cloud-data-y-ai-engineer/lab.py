"""Executable lab for lesson 271."""

from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "src"))

from multicloud_program.labs import main

if __name__ == "__main__":
    raise SystemExit(main(lesson_id="271", kind="decision", title='Ruta Cloud Data y AI Engineer', artifact="data-ai-plan"))
