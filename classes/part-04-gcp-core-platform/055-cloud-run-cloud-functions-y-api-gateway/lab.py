"""Executable lab for lesson 055."""

from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "src"))

from multicloud_program.labs import main

if __name__ == "__main__":
    raise SystemExit(main(lesson_id="055", kind="serverless", title='Cloud Run, Cloud Functions y API Gateway', artifact="api-serverless-gcp"))
