"""Executable lab for lesson 166."""

from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "src"))

from multicloud_program.labs import main

if __name__ == "__main__":
    raise SystemExit(main(lesson_id="166", kind="reliability", title='Backup, RTO, RPO y patrones de disaster recovery', artifact="plan-dr"))
