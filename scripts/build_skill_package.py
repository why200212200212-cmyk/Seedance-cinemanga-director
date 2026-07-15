#!/usr/bin/env python3
"""Build a deterministic, minimal AgentSkill distribution archive."""

from __future__ import annotations

import argparse
import hashlib
from pathlib import Path
import zipfile


ROOT = Path(__file__).resolve().parents[1]
SKILL_NAME = "seedance-cinemanga-director"
FIXED_TIMESTAMP = (2026, 1, 1, 0, 0, 0)


def runtime_files() -> list[Path]:
    """Return only files required to run the installed skill."""

    files = [
        ROOT / "SKILL.md",
        ROOT / "agents" / "openai.yaml",
        ROOT / "scripts" / "seedance_client.py",
        ROOT / ".env.example",
        ROOT / "LICENSE",
        ROOT / "NOTICE",
    ]
    files.extend(sorted((ROOT / "references").glob("*.md")))
    files.extend(sorted((ROOT / "templates").glob("*.md")))
    missing = [path for path in files if not path.is_file()]
    if missing:
        raise FileNotFoundError(
            "missing runtime files: " + ", ".join(str(path) for path in missing)
        )
    return files


def build_package(output: Path) -> tuple[Path, str, int]:
    """Write the archive and return its path, SHA-256, and file count."""

    output = output.expanduser().resolve()
    output.parent.mkdir(parents=True, exist_ok=True)
    temporary = output.with_name(output.name + ".tmp")
    temporary.unlink(missing_ok=True)
    files = runtime_files()
    try:
        with zipfile.ZipFile(
            temporary,
            "w",
            compression=zipfile.ZIP_DEFLATED,
            compresslevel=9,
        ) as archive:
            for source in files:
                relative = source.relative_to(ROOT).as_posix()
                info = zipfile.ZipInfo(f"{SKILL_NAME}/{relative}", FIXED_TIMESTAMP)
                info.compress_type = zipfile.ZIP_DEFLATED
                mode = 0o755 if source.suffix == ".py" else 0o644
                info.external_attr = mode << 16
                archive.writestr(info, source.read_bytes(), compresslevel=9)
        temporary.replace(output)
    except Exception:
        temporary.unlink(missing_ok=True)
        raise

    digest = hashlib.sha256(output.read_bytes()).hexdigest()
    return output, digest, len(files)


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Build a minimal installable Seedance Cinemanga Director skill ZIP."
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=ROOT / "dist" / f"{SKILL_NAME}.zip",
    )
    args = parser.parse_args()
    output, digest, count = build_package(args.output)
    print(f"built: {output}")
    print(f"files: {count}")
    print(f"sha256: {digest}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
