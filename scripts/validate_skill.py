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
    ".env.example",
    ".github/workflows/validate.yml",
    "templates/single-15s.md",
    "templates/multi-clip.md",
    "templates/storyboard-board.md",
    "references/continuity-rules.md",
    "references/character-design.md",
    "references/storyboard-design.md",
    "references/quality-checklist.md",
    "references/style-modes.md",
    "references/dialogue-timing.md",
    "references/shot-language.md",
    "references/3d-cinematic-production.md",
    "references/live-action-cinematography.md",
    "references/prompt-compiler.md",
    "references/runtime-orchestration.md",
    "references/seedance-api.md",
    "examples/api-prompt.txt",
    "examples/example-input-script.md",
    "examples/example-output-single.md",
    "examples/example-output-multi-clip.md",
    "docs/architecture.md",
    "docs/agent-integration.md",
    "docs/api-integration.md",
    "docs/installation.md",
    "docs/visual-showcase.md",
    "tests/acceptance-cases.md",
    "tests/test_seedance_client.py",
    "scripts/seedance_client.py",
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
    "assets/adaptive-storyboard-workflow.png",
    "assets/character-differentiation-board.png",
    "assets/ai-readable-camera-routes.png",
    "assets/segmented-camera-path.png",
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
    for marker in ["_::~OUTPUT_START::~_", "_::~OUTPUT_END::~_", "完整15秒", "剧情分析", "分镜形式决策", "角色多视角设计", "详细分镜图"]:
        if marker not in single:
            fail(f"single template missing marker: {marker}")

    multi = (ROOT / "templates/multi-clip.md").read_text(encoding="utf-8")
    for marker in ["_::~CLIP_START::~_", "_::~CLIP_END::~_", "尾帧接力合约", "全局剧情分析", "分镜形式决策", "全局角色多视角设计", "全局详细分镜图"]:
        if marker not in multi:
            fail(f"multi template missing marker: {marker}")

    storyboard = (ROOT / "templates/storyboard-board.md").read_text(encoding="utf-8")
    for marker in ["标准故事板", "九宫格", "二十五宫格", "智能宫格", "阅读顺序", "镜头使用清单", "USE", "REFERENCE-ONLY", "SKIP", "每格镜头卡", "Seedance 2.0 参考重点", "CAM-A0", "CAM-A1", "CAM-A-END", "HOLD", "俯视/侧视路线小图", "GAZE", "FOCUS", "LIGHT", "READ"]:
        if marker not in storyboard:
            fail(f"storyboard template missing marker: {marker}")

    core_terms = ["原台词", "必要人物", "连续性", "尾帧", "无BGM", "3D国漫", "真人影视级", "状态账本", "真实感门槛", "剧情分析", "智能宫格", "镜头序号", "Seedance 2.0", "角色差异化", "多视角设计", "永久角色ID", "独立参考图编号", "高度相似"]
    for term in core_terms:
        if term not in skill:
            fail(f"SKILL.md missing core rule: {term}")

    single_example = (ROOT / "examples/example-output-single.md").read_text(encoding="utf-8")
    for marker in ["剧情分析", "分镜形式决策", "角色多视角设计", "角色身份注册表", "详细分镜图", "CHAR-001", "导演方案（审阅用，不粘贴到生成器）", "可复制图片提示词", "可复制视频提示词", "摄影与物理合同", "固定服装"]:
        if marker not in single_example:
            fail(f"single example missing field: {marker}")

    multi_example = (ROOT / "examples/example-output-multi-clip.md").read_text(encoding="utf-8")
    for marker in ["全局剧情分析", "分镜形式决策", "全局角色多视角设计", "全局角色身份注册表", "全局详细分镜图", "CHAR-001", "全局声音规则", "全局摄影与物理规则", "转场类型", "状态账本更新", "可复制视频提示词", "负面约束"]:
        if marker not in multi_example:
            fail(f"multi example missing field: {marker}")

    acceptance_cases = (ROOT / "tests/acceptance-cases.md").read_text(encoding="utf-8")
    for marker in ["对白过长且明确禁止拆分", "剧情分析、自适应分镜与多人差异化", "双胞胎例外", "智能宫格", "AI可辨识运镜箭头路线", "独立角色板与身份绑定", "多段转向运镜路线", "四种分镜形式的镜头取舍", "有依据的换场", "匹配剪辑或声音桥", "镜头复杂度过载", "模式隔离", "平台能力未知"]:
        if marker not in acceptance_cases:
            fail(f"acceptance cases missing boundary: {marker}")

    workflow = (ROOT / ".github/workflows/validate.yml").read_text(encoding="utf-8")
    for marker in [
        "actions/checkout@v6",
        "actions/setup-python@v6",
        "python -m unittest discover",
        "--dry-run",
        "python scripts/validate_skill.py",
    ]:
        if marker not in workflow:
            fail(f"validation workflow missing step: {marker}")

    api_client = (ROOT / "scripts/seedance_client.py").read_text(encoding="utf-8")
    for marker in ["ARK_API_KEY", "SEEDANCE_MODEL", "--dry-run", "return_last_frame", "video_url"]:
        if marker not in api_client:
            fail(f"API client missing contract marker: {marker}")

    runtime = (ROOT / "references/runtime-orchestration.md").read_text(encoding="utf-8")
    for marker in ["Codex", "OpenClaw", "--dry-run", "不得无上限自动重试"]:
        if marker not in runtime:
            fail(f"runtime orchestration missing boundary: {marker}")

    openai_yaml = (ROOT / "agents/openai.yaml").read_text(encoding="utf-8")
    for marker in ["display_name:", "short_description:", "default_prompt:", "$seedance-cinemanga-director"]:
        if marker not in openai_yaml:
            fail(f"agents/openai.yaml missing field: {marker}")

    forbidden_repository_strings = ["why200212200212" + "-cmyk", "sk" + "lii"]
    for path in ROOT.rglob("*"):
        if not path.is_file() or path.suffix.lower() not in {".md", ".yaml", ".yml", ".py", ".txt"}:
            continue
        text = path.read_text(encoding="utf-8")
        for forbidden in forbidden_repository_strings:
            if forbidden in text:
                fail(f"obsolete repository string in {path.relative_to(ROOT)}: {forbidden}")

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
