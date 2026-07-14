#!/usr/bin/env python3
"""Zero-dependency structural validator for this AgentSkill repository."""

from pathlib import Path
import hashlib
import re
import sys

ROOT = Path(__file__).resolve().parents[1]

REQUIRED_FILES = [
    "SKILL.md",
    "README.md",
    "CHANGELOG.md",
    "CONTRIBUTING.md",
    "NOTICE",
    "LICENSE",
    "templates/single-15s.md",
    "templates/multi-clip.md",
    "references/continuity-rules.md",
    "references/quality-checklist.md",
    "references/style-modes.md",
    "references/dialogue-timing.md",
    "references/shot-language.md",
    "references/3d-cinematic-production.md",
    "references/live-action-cinematography.md",
    "references/prompt-compiler.md",
    "examples/example-input-script.md",
    "examples/example-output-single.md",
    "examples/example-output-multi-clip.md",
    "docs/architecture.md",
    "docs/installation.md",
    "docs/visual-showcase.md",
    "tests/acceptance-cases.md",
    "assets/README.md",
    "assets/cover-banner.png",
    "assets/feature-overview.png",
    "assets/icons-board.png",
    "assets/nine-grid-example.png",
    "assets/prompt-output-system.png",
    "assets/skill-preview.png",
    "assets/storyboard-example.png",
    "assets/system-architecture.png",
    "assets/twenty-five-grid-example.png",
    "assets/visual-assets-qa.png",
    "assets/workflow-architecture.png",
    "agents/openai.yaml",
]


def fail(message: str) -> None:
    print(f"FAIL: {message}", file=sys.stderr)
    raise SystemExit(1)


def main() -> None:
    missing = [path for path in REQUIRED_FILES if not (ROOT / path).is_file()]
    if missing:
        fail("missing required files: " + ", ".join(missing))

    skill = (ROOT / "SKILL.md").read_text(encoding="utf-8")
    if not skill.startswith("---\n"):
        fail("SKILL.md must start with YAML frontmatter")

    frontmatter_match = re.match(r"^---\n(.*?)\n---\n", skill, re.S)
    if not frontmatter_match:
        fail("SKILL.md frontmatter is not closed correctly")

    frontmatter = frontmatter_match.group(1)
    required_keys = ["name:", "description:"]
    for key in required_keys:
        if key not in frontmatter:
            fail(f"SKILL.md frontmatter missing {key}")

    if "name: seedance-cinemanga-director" not in frontmatter:
        fail("unexpected skill name")

    keys = [line.split(":", 1)[0].strip() for line in frontmatter.splitlines() if ":" in line]
    if keys != ["name", "description"]:
        fail("SKILL.md frontmatter may only contain name and description")

    single = (ROOT / "templates/single-15s.md").read_text(encoding="utf-8")
    for marker in ["_::~OUTPUT_START::~_", "_::~OUTPUT_END::~_", "完整15秒"]:
        if marker not in single:
            fail(f"single template missing marker: {marker}")

    multi = (ROOT / "templates/multi-clip.md").read_text(encoding="utf-8")
    for marker in ["_::~CLIP_START::~_", "_::~CLIP_END::~_", "尾帧接力合约"]:
        if marker not in multi:
            fail(f"multi template missing marker: {marker}")

    core_terms = ["原台词", "必要人物", "连续性", "尾帧", "无BGM", "3D国漫", "真人影视级", "状态账本", "真实感门槛"]
    for term in core_terms:
        if term not in skill:
            fail(f"SKILL.md missing core rule: {term}")

    single_example = (ROOT / "examples/example-output-single.md").read_text(encoding="utf-8")
    for marker in ["导演方案（审阅用，不粘贴到生成器）", "可复制图片提示词", "可复制视频提示词", "摄影与物理合同", "固定服装"]:
        if marker not in single_example:
            fail(f"single example missing field: {marker}")

    multi_example = (ROOT / "examples/example-output-multi-clip.md").read_text(encoding="utf-8")
    for marker in ["全局声音规则", "全局摄影与物理规则", "转场类型", "状态账本更新", "可复制视频提示词", "负面约束"]:
        if marker not in multi_example:
            fail(f"multi example missing field: {marker}")

    openai_yaml = (ROOT / "agents/openai.yaml").read_text(encoding="utf-8")
    for marker in ["display_name:", "short_description:", "default_prompt:", "$seedance-cinemanga-director"]:
        if marker not in openai_yaml:
            fail(f"agents/openai.yaml missing field: {marker}")

    png_hashes: dict[str, list[str]] = {}
    for path in (ROOT / "assets").glob("*.png"):
        digest = hashlib.sha256(path.read_bytes()).hexdigest()
        png_hashes.setdefault(digest, []).append(path.name)
    duplicate_groups = [names for names in png_hashes.values() if len(names) > 1]
    if duplicate_groups:
        fail("duplicate PNG content: " + "; ".join(", ".join(names) for names in duplicate_groups))

    link_pattern = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")
    for path in ROOT.rglob("*.md"):
        text = path.read_text(encoding="utf-8")
        for raw_target in link_pattern.findall(text):
            target = raw_target.split("#", 1)[0]
            if not target or re.match(r"^(?:https?://|mailto:)", target):
                continue
            if not (path.parent / target).exists():
                fail(f"broken local Markdown link in {path.relative_to(ROOT)}: {target}")

    for path in ROOT.rglob("*.md"):
        text = path.read_text(encoding="utf-8")
        if "\t" in text:
            fail(f"tab character found in {path.relative_to(ROOT)}")

    print("PASS: Seedance Cinemanga Director skill structure is valid.")


if __name__ == "__main__":
    main()
