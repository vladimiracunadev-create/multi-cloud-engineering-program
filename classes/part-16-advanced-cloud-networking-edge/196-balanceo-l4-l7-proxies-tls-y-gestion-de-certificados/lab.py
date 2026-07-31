"""Executable lab for lesson 196."""

from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "src"))

from multicloud_program.labs import main

if __name__ == "__main__":
    raise SystemExit(main(lesson_id="196", kind="network", title='Balanceo L4/L7, proxies, TLS y gestión de certificados', artifact="traffic-entry"))
