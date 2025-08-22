import json
from http.server import BaseHTTPRequestHandler, HTTPServer
import threading

from framework.backend.base_api_test import APIClient
from framework.config import AppConfig


class Handler(BaseHTTPRequestHandler):
    def do_GET(self) -> None:  # pragma: no cover - trivially tested
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps({"url": self.path}).encode())

    def log_message(self, format: str, *args: object) -> None:  # pragma: no cover - silence server
        return


def test_get_example() -> None:
    server = HTTPServer(("localhost", 0), Handler)
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()
    base_url = f"http://{server.server_address[0]}:{server.server_address[1]}"
    try:
        client = APIClient(AppConfig(api_base_url=base_url))
        response = client.get("/sample")
        assert response.status_code == 200
        data = response.json()
        assert data["url"] == "/sample"
    finally:
        server.shutdown()
        thread.join()
