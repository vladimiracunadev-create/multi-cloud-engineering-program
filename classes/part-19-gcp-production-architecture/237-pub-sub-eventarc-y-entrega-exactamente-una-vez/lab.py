"""Executable lab for lesson 237."""

from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "src"))

from multicloud_program.labs import main

if __name__ == "__main__":
    raise SystemExit(main(lesson_id="237", kind="messaging", title='Pub/Sub, Eventarc y entrega exactamente-una-vez', artifact="gcp-event-platform"))
