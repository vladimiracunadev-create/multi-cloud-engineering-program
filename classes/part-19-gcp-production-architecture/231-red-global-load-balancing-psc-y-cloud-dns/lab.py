"""Executable lab for lesson 231."""

from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "src"))

from multicloud_program.labs import main

if __name__ == "__main__":
    raise SystemExit(main(lesson_id="231", kind="network", title='Red global, load balancing, PSC y Cloud DNS', artifact="gcp-network"))
