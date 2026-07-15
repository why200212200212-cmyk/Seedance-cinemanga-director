from contextlib import redirect_stderr, redirect_stdout
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from io import StringIO
import json
import math
import os
from pathlib import Path
import sys
import tempfile
import threading
from typing import Any
import unittest
from unittest.mock import patch
from urllib import error


sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

from seedance_client import (  # noqa: E402
    SeedanceAPIError,
    SeedanceClient,
    SeedanceError,
    build_content,
    build_create_payload,
    extract_video_url,
    load_dotenv,
    main,
    normalize_base_url,
    read_content_json,
)


class SeedanceClientTests(unittest.TestCase):
    def test_build_content_preserves_reference_order_and_role(self) -> None:
        urls = ["https://example.com/a.png?signature=ok", "asset://asset-20260715-demo"]
        content = build_content("图片1是角色，图片2是授权资产", urls)
        self.assertEqual(
            content[0], {"type": "text", "text": "图片1是角色，图片2是授权资产"}
        )
        self.assertEqual([item["image_url"]["url"] for item in content[1:]], urls)
        self.assertTrue(all(item["role"] == "reference_image" for item in content[1:]))

    def test_reference_image_rejects_unsafe_or_malformed_urls(self) -> None:
        invalid_urls = [
            "file:///tmp/reference.png",
            "http://example.com/reference.png",
            "https://user:secret@example.com/reference.png",
            "https://example.com/reference.png#fragment",
            "asset://",
            "asset://asset-id/",
            "asset://asset-id/path",
            "asset://asset-id?version=1",
            "asset://asset:id",
        ]
        for url in invalid_urls:
            with self.subTest(url=url), self.assertRaises(SeedanceError):
                build_content("prompt", [url])

    def test_create_payload_uses_only_requested_optional_fields(self) -> None:
        payload = build_create_payload(
            "endpoint-id", build_content("prompt"), return_last_frame=True
        )
        self.assertEqual(payload["model"], "endpoint-id")
        self.assertTrue(payload["return_last_frame"])
        self.assertNotIn("callback_url", payload)

        callback_payload = build_create_payload(
            "endpoint-id",
            build_content("prompt"),
            callback_url="https://example.com/callback?job=1",
        )
        self.assertEqual(
            callback_payload["callback_url"], "https://example.com/callback?job=1"
        )

    def test_network_url_boundaries_reject_credentials_and_fragments(self) -> None:
        self.assertEqual(
            normalize_base_url("https://example.com/api/"), "https://example.com/api"
        )
        invalid_base_urls = [
            "https://user:secret@example.com/api",
            "https://example.com/api?version=3",
            "https://example.com/api#fragment",
            "https://example.com:invalid/api",
            "http://example.com/api",
        ]
        for url in invalid_base_urls:
            with self.subTest(url=url), self.assertRaises(SeedanceError):
                normalize_base_url(url)

        for callback_url in [
            "https://user:secret@example.com/callback",
            "https://example.com/callback#fragment",
        ]:
            with (
                self.subTest(callback_url=callback_url),
                self.assertRaises(SeedanceError),
            ):
                build_create_payload(
                    "model", build_content("prompt"), callback_url=callback_url
                )

    def test_content_json_requires_non_empty_typed_array(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "content.json"
            path.write_text(
                '[{"type":"text","text":"hello"},'
                '{"type":"image_url","image_url":{"url":"asset://asset-demo"},'
                '"role":"reference_image"}]',
                encoding="utf-8",
            )
            self.assertEqual(read_content_json(str(path))[1]["role"], "reference_image")

            for invalid_json in ["[]", "{}", '[{"text":"missing type"}]', "not-json"]:
                path.write_text(invalid_json, encoding="utf-8")
                with self.subTest(value=invalid_json), self.assertRaises(SeedanceError):
                    read_content_json(str(path))

    def test_dotenv_is_strict_and_does_not_override_existing_environment(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / ".env"
            path.write_text(
                "TEST_SEEDANCE_ENV=file-value\nQUOTED='ok'\n", encoding="utf-8"
            )
            old_existing = os.environ.get("TEST_SEEDANCE_ENV")
            old_quoted = os.environ.get("QUOTED")
            try:
                os.environ["TEST_SEEDANCE_ENV"] = "existing"
                os.environ.pop("QUOTED", None)
                load_dotenv(path)
                self.assertEqual(os.environ["TEST_SEEDANCE_ENV"], "existing")
                self.assertEqual(os.environ["QUOTED"], "ok")

                path.write_text("INVALID LINE\n", encoding="utf-8")
                with self.assertRaises(SeedanceError):
                    load_dotenv(path)
            finally:
                if old_existing is None:
                    os.environ.pop("TEST_SEEDANCE_ENV", None)
                else:
                    os.environ["TEST_SEEDANCE_ENV"] = old_existing
                if old_quoted is None:
                    os.environ.pop("QUOTED", None)
                else:
                    os.environ["QUOTED"] = old_quoted

    def test_video_url_and_timeout_validation(self) -> None:
        valid_url = "https://example.com/video.mp4?signature=ok"
        self.assertEqual(
            extract_video_url({"content": {"video_url": valid_url}}), valid_url
        )
        invalid_tasks: list[dict[str, Any]] = [
            {"content": {}},
            {"content": {"video_url": "file:///tmp/video.mp4"}},
            {"content": {"video_url": "http://example.com/video.mp4"}},
            {"content": {"video_url": "https://user:secret@example.com/video.mp4"}},
        ]
        for task in invalid_tasks:
            with self.subTest(task=task), self.assertRaises(SeedanceError):
                extract_video_url(task)

        for invalid_timeout in [0.0, -1.0, math.nan, math.inf]:
            with (
                self.subTest(timeout=invalid_timeout),
                self.assertRaises(SeedanceError),
            ):
                SeedanceClient("local-test-key", timeout=invalid_timeout)

        with self.assertRaises(SeedanceError):
            SeedanceClient("invalid key with spaces")

    def test_wait_rejects_invalid_status_and_stops_at_deadline(self) -> None:
        client = SeedanceClient("local-test-key")
        for task in [
            {"status": "failed", "error": {"message": "generation failed"}},
            {"status": "cancelled"},
            {"status": "mystery"},
            {},
        ]:
            with (
                self.subTest(task=task),
                patch.object(client, "get", return_value=task),
                self.assertRaises(SeedanceError),
            ):
                client.wait("cgt-test")

        for invalid_value in [0.0, -1.0, math.nan, math.inf]:
            with self.subTest(value=invalid_value), self.assertRaises(SeedanceError):
                client.wait("cgt-test", interval=invalid_value)
            with self.subTest(value=invalid_value), self.assertRaises(SeedanceError):
                client.wait("cgt-test", timeout=invalid_value)

        with (
            patch.object(
                client, "get", return_value={"status": "queued"}
            ) as mocked_get,
            patch("seedance_client.time.monotonic", side_effect=[0.0, 0.0, 0.5, 1.0]),
            patch("seedance_client.time.sleep") as mocked_sleep,
            self.assertRaisesRegex(SeedanceError, "Timed out"),
        ):
            client.wait("cgt-deadline", interval=1.0, timeout=1.0)
        mocked_get.assert_called_once_with("cgt-deadline")
        mocked_sleep.assert_called_once_with(0.5)

    def test_local_server_exercises_transport_retry_download_and_no_post_retry(
        self,
    ) -> None:
        calls: list[tuple[str, str]] = []
        authorizations: list[str | None] = []
        post_models: list[str] = []
        status_attempts = 0
        video_bytes = b"mock-seedance-video"

        class Handler(BaseHTTPRequestHandler):
            def _send_json(
                self,
                status: int,
                payload: dict[str, Any],
                headers: dict[str, str] | None = None,
            ) -> None:
                body = json.dumps(payload).encode("utf-8")
                self.send_response(status)
                self.send_header("Content-Type", "application/json")
                self.send_header("Content-Length", str(len(body)))
                for key, value in (headers or {}).items():
                    self.send_header(key, value)
                self.end_headers()
                self.wfile.write(body)

            def do_POST(self) -> None:
                calls.append(("POST", self.path))
                authorizations.append(self.headers.get("Authorization"))
                body = self.rfile.read(int(self.headers.get("Content-Length", "0")))
                payload = json.loads(body)
                model = str(payload["model"])
                post_models.append(model)
                if model == "fail-model":
                    self._send_json(500, {"error": {"message": "intentional failure"}})
                    return
                self._send_json(200, {"id": "cgt-retry"})

            def do_GET(self) -> None:
                nonlocal status_attempts
                calls.append(("GET", self.path))
                if self.path == "/video.mp4":
                    self.send_response(200)
                    self.send_header("Content-Type", "video/mp4")
                    self.send_header("Content-Length", str(len(video_bytes)))
                    self.end_headers()
                    self.wfile.write(video_bytes)
                    return
                if self.path == "/video-redirect":
                    self.send_response(302)
                    self.send_header(
                        "Location",
                        f"http://127.0.0.1:{server.server_port}/video.mp4",
                    )
                    self.end_headers()
                    return
                if self.path.endswith("/cgt-redirect"):
                    authorizations.append(self.headers.get("Authorization"))
                    self.send_response(302)
                    self.send_header(
                        "Location",
                        f"http://127.0.0.1:{server.server_port}/api/v3/contents/"
                        "generations/tasks/cgt-retry",
                    )
                    self.end_headers()
                    return
                authorizations.append(self.headers.get("Authorization"))
                if self.path.endswith("/cgt-invalid-json"):
                    body = b"\xff\xfe"
                    self.send_response(200)
                    self.send_header("Content-Length", str(len(body)))
                    self.end_headers()
                    self.wfile.write(body)
                    return
                status_attempts += 1
                if status_attempts == 1:
                    self._send_json(
                        429, {"error": {"message": "retry"}}, {"Retry-After": "999999"}
                    )
                    return
                self._send_json(200, {"id": "cgt-retry", "status": "succeeded"})

            def do_DELETE(self) -> None:
                calls.append(("DELETE", self.path))
                authorizations.append(self.headers.get("Authorization"))
                self._send_json(200, {"id": "cgt-retry"})

            def log_message(self, format: str, *args: object) -> None:
                pass

        server = ThreadingHTTPServer(("127.0.0.1", 0), Handler)
        thread = threading.Thread(target=server.serve_forever, daemon=True)
        thread.start()
        try:
            base_url = f"http://127.0.0.1:{server.server_port}/api/v3"
            client = SeedanceClient("secret-for-local-test", base_url)
            payload = build_create_payload("model-id", build_content("prompt"))
            self.assertEqual(client.create(payload)["id"], "cgt-retry")
            with patch("seedance_client.time.sleep") as mocked_sleep:
                self.assertEqual(client.wait("cgt-retry")["status"], "succeeded")
            mocked_sleep.assert_called_once_with(8.0)
            self.assertEqual(client.cancel("cgt-retry")["id"], "cgt-retry")

            with self.assertRaises(SeedanceAPIError):
                client.create(
                    build_create_payload("fail-model", build_content("prompt"))
                )
            self.assertEqual(post_models.count("fail-model"), 1)

            with self.assertRaisesRegex(SeedanceError, "invalid JSON"):
                client.get("cgt-invalid-json")

            get_count_before_redirect = len(
                [call for call in calls if call[0] == "GET"]
            )
            with self.assertRaises(SeedanceAPIError) as redirect_error:
                client.get("cgt-redirect")
            self.assertEqual(redirect_error.exception.status, 302)
            self.assertEqual(
                len([call for call in calls if call[0] == "GET"]),
                get_count_before_redirect + 1,
            )

            with tempfile.TemporaryDirectory() as directory:
                output = Path(directory) / "video.mp4"
                result = client.download(
                    {
                        "content": {
                            "video_url": f"http://127.0.0.1:{server.server_port}/video-redirect"
                        }
                    },
                    output,
                )
                self.assertEqual(result.read_bytes(), video_bytes)
                self.assertFalse(output.with_name("video.mp4.part").exists())
        finally:
            server.shutdown()
            server.server_close()
            thread.join(timeout=2)

        self.assertTrue(
            all(value == "Bearer secret-for-local-test" for value in authorizations)
        )
        self.assertIn(("DELETE", "/api/v3/contents/generations/tasks/cgt-retry"), calls)

    def test_download_failure_removes_partial_file(self) -> None:
        client = SeedanceClient("local-test-key")
        with tempfile.TemporaryDirectory() as directory:
            destination = Path(directory) / "video.mp4"
            partial = destination.with_name("video.mp4.part")
            partial.write_bytes(b"stale partial data")
            with (
                patch.object(
                    client._download_opener,
                    "open",
                    side_effect=error.URLError("offline"),
                ),
                self.assertRaises(SeedanceError),
            ):
                client.download(
                    {"content": {"video_url": "https://example.com/video.mp4"}},
                    destination,
                )
            self.assertFalse(partial.exists())

    def test_cli_dry_run_needs_no_api_key_and_emits_reference_role(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            prompt_path = Path(directory) / "prompt.txt"
            prompt_path.write_text("一条安全的测试提示词", encoding="utf-8")
            stdout = StringIO()
            stderr = StringIO()
            with (
                patch.dict(os.environ, {"ARK_API_KEY": "", "SEEDANCE_API_KEY": ""}),
                redirect_stdout(stdout),
                redirect_stderr(stderr),
            ):
                result = main(
                    [
                        "--env-file",
                        str(Path(directory) / "missing.env"),
                        "--model",
                        "model-id",
                        "create",
                        "--prompt-file",
                        str(prompt_path),
                        "--image-url",
                        "asset://asset-cli-test",
                        "--dry-run",
                    ]
                )
            self.assertEqual(result, 0, stderr.getvalue())
            payload = json.loads(stdout.getvalue())
            self.assertEqual(payload["content"][1]["role"], "reference_image")


if __name__ == "__main__":
    unittest.main()
