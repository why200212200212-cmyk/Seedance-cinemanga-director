#!/usr/bin/env python3
"""Minimal, dependency-free client for the Volcengine Ark video task API.

The client deliberately keeps the model/endpoint configurable. Creating a task can
incur charges, so validation and CI use only ``--dry-run``.
"""

from __future__ import annotations

import argparse
import json
import os
from pathlib import Path
import sys
import time
from typing import Any, Iterable
from urllib import error, parse, request


DEFAULT_BASE_URL = "https://ark.cn-beijing.volces.com/api/v3"
PENDING_STATUSES = {"queued", "running"}


class SeedanceError(RuntimeError):
    """Base error for configuration, transport, and API failures."""


class SeedanceAPIError(SeedanceError):
    """An HTTP error returned by the Ark API."""

    def __init__(self, status: int, message: str, details: Any = None) -> None:
        super().__init__(f"Ark API returned HTTP {status}: {message}")
        self.status = status
        self.details = details


def load_dotenv(path: Path) -> None:
    """Load a small, predictable subset of dotenv syntax without dependencies."""

    if not path.is_file():
        return
    for line_number, raw_line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        line = raw_line.strip()
        if not line or line.startswith("#"):
            continue
        if line.startswith("export "):
            line = line[7:].lstrip()
        if "=" not in line:
            raise SeedanceError(f"Invalid dotenv entry at {path}:{line_number}")
        key, value = line.split("=", 1)
        key = key.strip()
        value = value.strip()
        if not key or not key.replace("_", "a").isalnum() or key[0].isdigit():
            raise SeedanceError(f"Invalid dotenv key at {path}:{line_number}")
        if len(value) >= 2 and value[0] == value[-1] and value[0] in {"'", '"'}:
            value = value[1:-1]
        os.environ.setdefault(key, value)


def normalize_base_url(value: str) -> str:
    value = value.strip().rstrip("/")
    parsed = parse.urlparse(value)
    if parsed.scheme not in {"http", "https"} or not parsed.netloc:
        raise SeedanceError("ARK_BASE_URL must be an absolute HTTP(S) URL")
    return value


def read_prompt(path_value: str) -> str:
    text = sys.stdin.read() if path_value == "-" else Path(path_value).read_text(encoding="utf-8")
    text = text.strip()
    if not text:
        raise SeedanceError("Prompt must not be empty")
    return text


def build_content(prompt: str, image_urls: Iterable[str] = ()) -> list[dict[str, Any]]:
    """Build official text + image_url content in deterministic reference order."""

    prompt = prompt.strip()
    if not prompt:
        raise SeedanceError("Prompt must not be empty")
    content: list[dict[str, Any]] = [{"type": "text", "text": prompt}]
    for url in image_urls:
        parsed = parse.urlparse(url)
        if parsed.scheme not in {"http", "https"} or not parsed.netloc:
            raise SeedanceError(f"Reference image URL must be HTTP(S): {url}")
        content.append({"type": "image_url", "image_url": {"url": url}})
    return content


def read_content_json(path_value: str) -> list[dict[str, Any]]:
    text = sys.stdin.read() if path_value == "-" else Path(path_value).read_text(encoding="utf-8")
    try:
        value = json.loads(text)
    except json.JSONDecodeError as exc:
        raise SeedanceError(f"Invalid content JSON: {exc}") from exc
    if not isinstance(value, list) or not value:
        raise SeedanceError("Content JSON must be a non-empty JSON array")
    if not all(isinstance(item, dict) and isinstance(item.get("type"), str) for item in value):
        raise SeedanceError("Every content item must be an object with a string 'type'")
    return value


def build_create_payload(
    model: str,
    content: list[dict[str, Any]],
    callback_url: str | None = None,
    return_last_frame: bool = False,
) -> dict[str, Any]:
    if not model.strip():
        raise SeedanceError("A model or endpoint ID is required (--model or SEEDANCE_MODEL)")
    payload: dict[str, Any] = {"model": model.strip(), "content": content}
    if callback_url:
        parsed = parse.urlparse(callback_url)
        if parsed.scheme not in {"http", "https"} or not parsed.netloc:
            raise SeedanceError("Callback URL must be an absolute HTTP(S) URL")
        payload["callback_url"] = callback_url
    if return_last_frame:
        payload["return_last_frame"] = True
    return payload


def extract_video_url(task: dict[str, Any]) -> str:
    content = task.get("content")
    url = content.get("video_url") if isinstance(content, dict) else None
    if not isinstance(url, str) or not url:
        raise SeedanceError("Succeeded task does not contain content.video_url")
    parsed = parse.urlparse(url)
    if parsed.scheme not in {"http", "https"} or not parsed.netloc:
        raise SeedanceError("Task returned an invalid video URL")
    return url


class SeedanceClient:
    def __init__(self, api_key: str, base_url: str = DEFAULT_BASE_URL, timeout: float = 60.0) -> None:
        if not api_key.strip():
            raise SeedanceError("ARK_API_KEY is required for network operations")
        self.api_key = api_key.strip()
        self.base_url = normalize_base_url(base_url)
        self.timeout = timeout

    def _request_json(
        self,
        method: str,
        path: str,
        payload: dict[str, Any] | None = None,
        get_retries: int = 3,
    ) -> dict[str, Any]:
        url = f"{self.base_url}/{path.lstrip('/')}"
        body = json.dumps(payload, ensure_ascii=False).encode("utf-8") if payload is not None else None
        headers = {"Authorization": f"Bearer {self.api_key}", "Accept": "application/json"}
        if body is not None:
            headers["Content-Type"] = "application/json"

        attempts = get_retries + 1 if method == "GET" else 1
        for attempt in range(attempts):
            req = request.Request(url, data=body, headers=headers, method=method)
            try:
                with request.urlopen(req, timeout=self.timeout) as response:
                    raw = response.read()
                    if not raw:
                        return {}
                    value = json.loads(raw.decode("utf-8"))
                    if not isinstance(value, dict):
                        raise SeedanceError("Ark API response must be a JSON object")
                    return value
            except error.HTTPError as exc:
                raw = exc.read().decode("utf-8", errors="replace")
                try:
                    details = json.loads(raw) if raw else None
                except json.JSONDecodeError:
                    details = raw
                retryable = method == "GET" and (exc.code == 429 or 500 <= exc.code < 600)
                if retryable and attempt + 1 < attempts:
                    retry_after = exc.headers.get("Retry-After") if exc.headers else None
                    delay = float(retry_after) if retry_after and retry_after.isdigit() else min(2**attempt, 8)
                    time.sleep(delay)
                    continue
                message = "request failed"
                if isinstance(details, dict):
                    api_error = details.get("error")
                    if isinstance(api_error, dict):
                        message = str(api_error.get("message") or api_error.get("code") or message)
                    else:
                        message = str(details.get("message") or message)
                elif details:
                    message = str(details)
                raise SeedanceAPIError(exc.code, message, details) from exc
            except error.URLError as exc:
                raise SeedanceError(f"Unable to reach Ark API: {exc.reason}") from exc
            except json.JSONDecodeError as exc:
                raise SeedanceError("Ark API returned invalid JSON") from exc
        raise AssertionError("unreachable")

    def create(self, payload: dict[str, Any]) -> dict[str, Any]:
        # POST is intentionally not retried: a repeated request may create a paid duplicate task.
        return self._request_json("POST", "contents/generations/tasks", payload)

    def get(self, task_id: str) -> dict[str, Any]:
        task_id = task_id.strip()
        if not task_id:
            raise SeedanceError("Task ID must not be empty")
        return self._request_json("GET", f"contents/generations/tasks/{parse.quote(task_id, safe='')}")

    def cancel(self, task_id: str) -> dict[str, Any]:
        task_id = task_id.strip()
        if not task_id:
            raise SeedanceError("Task ID must not be empty")
        return self._request_json("DELETE", f"contents/generations/tasks/{parse.quote(task_id, safe='')}")

    def wait(self, task_id: str, interval: float = 5.0, timeout: float = 900.0) -> dict[str, Any]:
        if interval <= 0 or timeout <= 0:
            raise SeedanceError("Polling interval and timeout must be positive")
        deadline = time.monotonic() + timeout
        while True:
            task = self.get(task_id)
            status = str(task.get("status", "")).lower()
            if status == "succeeded":
                return task
            if status in {"failed", "cancelled"}:
                details = task.get("error") or "no error details"
                raise SeedanceError(f"Task {task_id} ended with status {status}: {details}")
            if status not in PENDING_STATUSES:
                raise SeedanceError(f"Task {task_id} returned unknown status: {status or '<missing>'}")
            remaining = deadline - time.monotonic()
            if remaining <= 0:
                raise SeedanceError(f"Timed out waiting for task {task_id}")
            time.sleep(min(interval, remaining))

    def download(self, task: dict[str, Any], destination: Path) -> Path:
        url = extract_video_url(task)
        destination = destination.expanduser().resolve()
        destination.parent.mkdir(parents=True, exist_ok=True)
        temporary = destination.with_name(destination.name + ".part")
        try:
            req = request.Request(url, headers={"Accept": "video/*"})
            with request.urlopen(req, timeout=self.timeout) as response, temporary.open("wb") as output:
                while chunk := response.read(1024 * 1024):
                    output.write(chunk)
            temporary.replace(destination)
            return destination
        except (error.URLError, OSError) as exc:
            temporary.unlink(missing_ok=True)
            raise SeedanceError(f"Unable to download generated video: {exc}") from exc


def print_json(value: dict[str, Any]) -> None:
    print(json.dumps(value, ensure_ascii=False, indent=2, sort_keys=True))


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Create and manage Seedance tasks through Volcengine Ark.")
    parser.add_argument("--env-file", default=".env", help="dotenv file to load (default: .env)")
    parser.add_argument("--base-url", help="override ARK_BASE_URL")
    parser.add_argument("--model", help="override SEEDANCE_MODEL with a model or endpoint ID")
    parser.add_argument("--request-timeout", type=float, default=60.0)
    subparsers = parser.add_subparsers(dest="command", required=True)

    create_parser = subparsers.add_parser("create", help="create a video generation task")
    source = create_parser.add_mutually_exclusive_group(required=True)
    source.add_argument("--prompt-file", help="UTF-8 prompt file, or - for stdin")
    source.add_argument("--content-json", help="raw official content array JSON, or - for stdin")
    create_parser.add_argument("--image-url", action="append", default=[], help="ordered reference URL")
    create_parser.add_argument("--callback-url")
    create_parser.add_argument("--return-last-frame", action="store_true")
    create_parser.add_argument("--dry-run", action="store_true", help="print payload without any API call")
    create_parser.add_argument("--wait", action="store_true", help="wait for a terminal task result")
    create_parser.add_argument("--interval", type=float, default=5.0)
    create_parser.add_argument("--timeout", type=float, default=900.0)
    create_parser.add_argument("--output", type=Path, help="wait and download the resulting video")

    status_parser = subparsers.add_parser("status", help="get task status")
    status_parser.add_argument("task_id")

    wait_parser = subparsers.add_parser("wait", help="wait for a task and optionally download it")
    wait_parser.add_argument("task_id")
    wait_parser.add_argument("--interval", type=float, default=5.0)
    wait_parser.add_argument("--timeout", type=float, default=900.0)
    wait_parser.add_argument("--output", type=Path)

    cancel_parser = subparsers.add_parser("cancel", help="cancel/delete a task")
    cancel_parser.add_argument("task_id")
    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    try:
        load_dotenv(Path(args.env_file))
        base_url = args.base_url or os.environ.get("ARK_BASE_URL", DEFAULT_BASE_URL)
        api_key = os.environ.get("ARK_API_KEY") or os.environ.get("SEEDANCE_API_KEY", "")
        model = args.model or os.environ.get("SEEDANCE_MODEL", "")

        if args.command == "create":
            if args.content_json:
                if args.image_url:
                    parser.error("--image-url cannot be combined with --content-json")
                content = read_content_json(args.content_json)
            else:
                content = build_content(read_prompt(args.prompt_file), args.image_url)
            payload = build_create_payload(model, content, args.callback_url, args.return_last_frame)
            if args.dry_run:
                if args.wait or args.output:
                    parser.error("--dry-run cannot be combined with --wait or --output")
                print_json(payload)
                return 0
            client = SeedanceClient(api_key, base_url, args.request_timeout)
            result = client.create(payload)
            task_id = result.get("id")
            if not isinstance(task_id, str) or not task_id:
                raise SeedanceError("Create response does not contain a task id")
            if args.wait or args.output:
                result = client.wait(task_id, args.interval, args.timeout)
                if args.output:
                    destination = client.download(result, args.output)
                    result = {**result, "downloaded_to": str(destination)}
            print_json(result)
            return 0

        client = SeedanceClient(api_key, base_url, args.request_timeout)
        if args.command == "status":
            result = client.get(args.task_id)
        elif args.command == "wait":
            result = client.wait(args.task_id, args.interval, args.timeout)
            if args.output:
                destination = client.download(result, args.output)
                result = {**result, "downloaded_to": str(destination)}
        else:
            result = client.cancel(args.task_id)
        print_json(result)
        return 0
    except (SeedanceError, OSError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
