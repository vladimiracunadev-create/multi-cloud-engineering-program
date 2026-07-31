"""CloudShop reference service using only the Python standard library."""

from __future__ import annotations

import json
import os
import time
import uuid
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

ORDERS: dict[str, dict] = {}


class Handler(BaseHTTPRequestHandler):
    server_version = "CloudShop/2.0"

    def _send(self, status: int, body: dict) -> None:
        payload = json.dumps(body).encode()
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(payload)))
        self.send_header("X-Content-Type-Options", "nosniff")
        self.send_header("X-Request-Id", self.headers.get("X-Request-Id", str(uuid.uuid4())))
        self.end_headers()
        self.wfile.write(payload)

    def do_GET(self) -> None:
        if self.path == "/health/live":
            self._send(200, {"status": "alive"})
        elif self.path == "/health/ready":
            self._send(200, {"status": "ready", "orders": len(ORDERS)})
        elif self.path == "/api/orders":
            self._send(200, {"items": list(ORDERS.values())})
        else:
            self._send(404, {"error": "not_found"})

    def do_POST(self) -> None:
        if self.path != "/api/orders":
            self._send(404, {"error": "not_found"})
            return
        try:
            size = int(self.headers.get("Content-Length", "0"))
            body = json.loads(self.rfile.read(min(size, 65536)))
            if not isinstance(body.get("sku"), str) or int(body.get("quantity", 0)) < 1:
                raise ValueError("sku and positive quantity required")
        except (ValueError, json.JSONDecodeError):
            self._send(400, {"error": "invalid_order"})
            return
        order_id = str(uuid.uuid4())
        order = {"id": order_id, "sku": body["sku"], "quantity": int(body["quantity"]), "status": "accepted", "created_at": int(time.time())}
        ORDERS[order_id] = order
        self._send(201, order)

    def log_message(self, fmt: str, *args: object) -> None:
        print(json.dumps({"event": "http_request", "message": fmt % args, "time": int(time.time())}))


def main() -> None:
    port = int(os.getenv("PORT", "8080"))
    ThreadingHTTPServer(("0.0.0.0", port), Handler).serve_forever()


if __name__ == "__main__":
    main()
