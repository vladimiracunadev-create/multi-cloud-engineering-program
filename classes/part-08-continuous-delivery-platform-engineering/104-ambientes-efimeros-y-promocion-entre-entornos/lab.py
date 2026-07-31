"""Executable lab for lesson 104."""

from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "src"))

from multicloud_program.labs import main

if __name__ == "__main__":
    raise SystemExit(main(lesson_id="104", kind="delivery", title='Ambientes efímeros y promoción entre entornos', artifact="flujo-ambientes"))
