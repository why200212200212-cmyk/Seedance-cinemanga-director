from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
import json
import os
from pathlib import Path
import sys
import tempfile
import threading
import unittest


sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

from seedance_client import (  # noqa: E402
    SeedanceError,
    SeedanceClient,
    build_content,
    build_create_payload,
    extract_video_url,
    load_dotenv,
    normalize_base_url,
    read_content_json,
)


class SeedanceClientTests(unittest.TestCase):
    def test_build_content_preserves_reference_order(self):
        urls = ["https://example.com/a.png", "https://example.com/b.png"]
        content = build_content("图片1是角色，图片2是场景", urls)
        self.assertEqual(content[0], {"type": "text", "text": "图片1是角色，图片2是场景"})
        self.assertEqual([item["image_url"]["url"] for item in content[1:]], urls)

    def test_create_payload_uses_only_requested_optional_fields(self):
        payload = build_create_payload("endpoint-id", build_content("prompt"), return_last_frame=True)
        self.assertEqual(payload["model"], "endpoint-id")
        self.assertTrue(payload["return_last_frame"])
        self.assertNotIn("callback_url", payload)

    def test_content_json_requires_non_empty_typed_array(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "content.json"
            path.write_text('[{"type":"text","text":"hello"}]', encoding="utf-8")
            self.assertEqual(read_content_json(str(path))[0]["type"], "text")
            path.write_text("[]", encoding="utf-8")
            with self.assertRaises(SeedanceError):
                read_content_json(str(path))

    def test_dotenv_does_not_override_existing_environment(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / ".env"
            path.write_text("TEST_SEEDANCE_ENV=file-value\nQUOTED='ok'\n", encoding="utf-8")
            old_existing = os.environ.get("TEST_SEEDANCE_ENV")
            old_quoted = os.environ.get("QUOTED")
            try:
                os.environ["TEST_SEEDANCE_ENV"] = "existing"
                os.environ.pop("QUOTED", None)
                load_dotenv(path)
                self.assertEqual(os.environ["TEST_SEEDANCE_ENV"], "existing")
                self.assertEqual(os.environ["QUOTED"], "ok")
            finally:
                if old_existing is None:
                    os.environ.pop("TEST_SEEDANCE_ENV", None)
                else:
                    os.environ["TEST_SEEDANCE_ENV"] = old_existing
                if old_quoted is None:
                    os.environ.pop("QUOTED", None)
                else:
                    os.environ["QUOTED"] = old_quoted

    def test_url_and_result_validation(self):
        self.assertEqual(normalize_base_url("https://example.com/api/"), "https://example.com/api")
        self.assertEqual(extract_video_url({"content": {"video_url": "https://example.com/v.mp4"}}), "https://example.com/v.mp4")
        with self.assertRaises(SeedanceError):
            extract_video_url({"content": {}})

    def test_local_server_exercises_create_status_and_cancel_contract(self):
        calls = []

        class Handler(BaseHTTPRequestHandler):
            def _send(self, status, payload):
                body = json.dumps(payload).encode("utf-8")
                self.send_response(status)
                self.send_header("Content-Type", "application/json")
                self.send_header("Content-Length", str(len(body)))
                self.end_headers()
                self.wfile.write(body)

            def do_POST(self):
                body = self.rfile.read(int(self.headers["Content-Length"]))
                calls.append(("POST", self.path, self.headers.get("Authorization"), json.loads(body)))
                self._send(200, {"id": "cgt-local"})

            def do_GET(self):
                calls.append(("GET", self.path, self.headers.get("Authorization"), None))
                self._send(200, {"id": "cgt-local", "status": "succeeded", "content": {"video_url": "https://example.com/video.mp4"}})

            def do_DELETE(self):
                calls.append(("DELETE", self.path, self.headers.get("Authorization"), None))
                self._send(200, {"id": "cgt-local"})

            def log_message(self, format, *args):
                pass

        server = ThreadingHTTPServer(("127.0.0.1", 0), Handler)
        thread = threading.Thread(target=server.serve_forever, daemon=True)
        thread.start()
        try:
            client = SeedanceClient("secret-for-local-test", f"http://127.0.0.1:{server.server_port}/api/v3")
            payload = build_create_payload("model-id", build_content("prompt"))
            self.assertEqual(client.create(payload)["id"], "cgt-local")
            self.assertEqual(client.wait("cgt-local")["status"], "succeeded")
            self.assertEqual(client.cancel("cgt-local")["id"], "cgt-local")
        finally:
            server.shutdown()
            server.server_close()
            thread.join(timeout=2)

        self.assertEqual([call[0] for call in calls], ["POST", "GET", "DELETE"])
        self.assertTrue(all(call[1].endswith("/contents/generations/tasks" + ("/cgt-local" if call[0] != "POST" else "")) for call in calls))
        self.assertTrue(all(call[2] == "Bearer secret-for-local-test" for call in calls))
        self.assertEqual(calls[0][3]["model"], "model-id")


if __name__ == "__main__":
    unittest.main()
