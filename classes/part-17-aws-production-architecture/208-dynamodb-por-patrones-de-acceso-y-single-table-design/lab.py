"""Executable lab for lesson 208."""

from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "src"))

from multicloud_program.labs import main

if __name__ == "__main__":
    raise SystemExit(main(lesson_id="208", kind="data", title='DynamoDB por patrones de acceso y single-table design', artifact="aws-dynamodb-model"))
