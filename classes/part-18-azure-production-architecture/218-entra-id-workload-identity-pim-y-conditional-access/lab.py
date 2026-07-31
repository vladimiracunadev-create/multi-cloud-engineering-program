"""Executable lab for lesson 218."""

from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "src"))

from multicloud_program.labs import main

if __name__ == "__main__":
    raise SystemExit(main(lesson_id="218", kind="iam", title='Entra ID, workload identity, PIM y Conditional Access', artifact="azure-identity"))
