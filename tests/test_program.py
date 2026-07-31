import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
sys.path.insert(0, str(ROOT / "scripts"))

from multicloud_program.labs import run_lab
from validate_repository import validate


class ProgramTests(unittest.TestCase):
    def test_catalog_has_180_contiguous_lessons(self):
        catalog = json.loads((ROOT / "curriculum" / "catalog.json").read_text(encoding="utf-8"))
        self.assertEqual(180, len(catalog))
        self.assertEqual([f"{n:03d}" for n in range(1, 181)], [x["id"] for x in catalog])

    def test_lab_is_deterministic(self):
        first = run_lab("001", "foundation", 42)
        second = run_lab("001", "foundation", 42)
        self.assertEqual(first, second)
        self.assertTrue(first["evidence"])
        self.assertTrue(first["limitations"])

    def test_negative_test_is_explicit(self):
        result = run_lab("132", "capstone", 7)
        self.assertEqual("simulated-denial", result["negative_test"]["observed"])

    def test_repository_contract(self):
        self.assertEqual([], validate(strict=True))


if __name__ == "__main__":
    unittest.main()
