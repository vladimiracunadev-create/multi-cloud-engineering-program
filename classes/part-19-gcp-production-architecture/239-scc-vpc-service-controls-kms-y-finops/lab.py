"""Executable lab for lesson 239."""

from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "src"))

from multicloud_program.labs import main

if __name__ == "__main__":
    raise SystemExit(main(lesson_id="239", kind="security", title='SCC, VPC Service Controls, KMS y FinOps', artifact="gcp-security-finops"))
