"""Executable lab for lesson 194."""

from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "src"))

from multicloud_program.labs import main

if __name__ == "__main__":
    raise SystemExit(main(lesson_id="194", kind="network", title='Routing, BGP, tránsito y propagación de rutas', artifact="routing-lab"))
