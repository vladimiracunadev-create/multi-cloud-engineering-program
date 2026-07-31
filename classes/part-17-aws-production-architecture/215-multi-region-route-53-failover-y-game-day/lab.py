"""Executable lab for lesson 215."""

from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "src"))

from multicloud_program.labs import main

if __name__ == "__main__":
    raise SystemExit(main(lesson_id="215", kind="reliability", title='Multi-región, Route 53, failover y game day', artifact="aws-dr-drill"))
