"""Executable lab for lesson 233."""

from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "src"))

from multicloud_program.labs import main

if __name__ == "__main__":
    raise SystemExit(main(lesson_id="233", kind="serverless", title='Cloud Run, Functions, API Gateway y Workflows', artifact="gcp-serverless"))
