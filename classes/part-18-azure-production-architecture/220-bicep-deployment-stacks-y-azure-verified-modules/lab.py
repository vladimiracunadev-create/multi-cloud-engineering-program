"""Executable lab for lesson 220."""

from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "src"))

from multicloud_program.labs import main

if __name__ == "__main__":
    raise SystemExit(main(lesson_id="220", kind="iac", title='Bicep, deployment stacks y Azure Verified Modules', artifact="azure-bicep-stack"))
