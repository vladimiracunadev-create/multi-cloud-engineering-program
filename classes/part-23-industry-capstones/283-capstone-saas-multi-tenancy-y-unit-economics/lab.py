"""Executable lab for lesson 283."""

from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "src"))

from multicloud_program.labs import main

if __name__ == "__main__":
    raise SystemExit(main(lesson_id="283", kind="capstone", title='Capstone SaaS: multi-tenancy y unit economics', artifact="saas-capstone"))
