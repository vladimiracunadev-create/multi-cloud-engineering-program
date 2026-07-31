"""Executable lab for lesson 214."""

from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "src"))

from multicloud_program.labs import main

if __name__ == "__main__":
    raise SystemExit(main(lesson_id="214", kind="finops", title='Budgets, Cost Explorer, etiquetado y FinOps automatizado', artifact="aws-cost-control"))
