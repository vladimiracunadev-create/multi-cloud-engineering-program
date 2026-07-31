"""Executable lab for lesson 190."""

from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "src"))

from multicloud_program.labs import main

if __name__ == "__main__":
    raise SystemExit(main(lesson_id="190", kind="architecture", title='ADRs, fitness functions y gobierno de decisiones', artifact="adr-library"))
