import importlib.util
import json
import threading
import unittest
import urllib.error
import urllib.request
from http.server import ThreadingHTTPServer
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("cloudshop", ROOT / "projects/cloudshop/app.py")
cloudshop = importlib.util.module_from_spec(spec); spec.loader.exec_module(cloudshop)

class CloudShopTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.server = ThreadingHTTPServer(("127.0.0.1", 0), cloudshop.Handler)
        threading.Thread(target=cls.server.serve_forever, daemon=True).start()
        cls.base = f"http://127.0.0.1:{cls.server.server_port}"

    @classmethod
    def tearDownClass(cls): cls.server.shutdown()

    def test_health_and_order_lifecycle(self):
        with urllib.request.urlopen(self.base + "/health/ready") as response:
            self.assertEqual("ready", json.load(response)["status"])
        request = urllib.request.Request(self.base + "/api/orders", data=json.dumps({"sku":"book-cloud","quantity":2}).encode(), headers={"Content-Type":"application/json"}, method="POST")
        with urllib.request.urlopen(request) as response:
            self.assertEqual(201, response.status); self.assertEqual("accepted", json.load(response)["status"])

    def test_invalid_order_is_rejected(self):
        request = urllib.request.Request(self.base + "/api/orders", data=b'{}', method="POST")
        with self.assertRaises(urllib.error.HTTPError) as caught: urllib.request.urlopen(request)
        self.assertEqual(400, caught.exception.code)
