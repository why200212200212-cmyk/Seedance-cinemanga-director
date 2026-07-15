#!/usr/bin/env python3
"""Zero-dependency structural validator for this AgentSkill repository."""

from pathlib import Path
import hashlib
import re
import struct
import sys
from typing import NoReturn

ROOT = Path(__file__).resolve().parents[1]

KNOWLEDGE_FILES = [
    "references/knowledge-00-index.md",
    "references/knowledge-01-storyboard-workflow.md",
    "references/knowledge-02-shot-language-basics.md",
    "references/knowledge-03-camera-movement-encyclopedia.md",
    "references/knowledge-04-ai-camera-prompting.md",
    "references/knowledge-05-visual-narrative-editing.md",
    "references/knowledge-06-lighting-and-color.md",
    "references/knowledge-07-physical-contact-workarounds.md",
    "references/knowledge-08-vertical-9x16.md",
    "references/knowledge-09-director-prompt-dictionary.md",
    "references/knowledge-10-blocking-and-staging.md",
    "references/knowledge-11-depth-of-field.md",
    "references/knowledge-12-shot-composition.md",
    "references/knowledge-13-seedance-2-guide.md",
    "references/knowledge-14-runway-gen4-camera-guide.md",
    "references/knowledge-15-video-tool-comparison.md",
    "references/knowledge-16-shot-table-schema.md",
    "references/knowledge-17-shot-table-case-study.md",
    "references/knowledge-18-state-change-tracking.md",
    "references/knowledge-19-advanced-camera-techniques.md",
    "references/knowledge-20-seedance-advanced-shot-templates.md",
    "references/knowledge-21-long-take-guide.md",
    "references/knowledge-22-seedance-long-take-templates.md",
]

REQUIRED_FILES = [
    "SKILL.md",
    "README.md",
    "CHANGELOG.md",
    "CONTRIBUTING.md",
    "NOTICE",
    "LICENSE",
    ".env.example",
    ".github/workflows/bandit.yml",
    ".github/workflows/codeql.yml",
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
    "assets/knowledge-routing-map.png",
    "assets/seedance-multimodal-binding.png",
    "agents/openai.yaml",
] + KNOWLEDGE_FILES


def fail(message: str) -> NoReturn:
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

    keys = [
        line.split(":", 1)[0].strip()
        for line in frontmatter.splitlines()
        if ":" in line
    ]
    if keys != ["name", "description"]:
        fail("SKILL.md frontmatter may only contain name and description")

    single = (ROOT / "templates/single-15s.md").read_text(encoding="utf-8")
    for marker in [
        "_::~OUTPUT_START::~_",
        "_::~OUTPUT_END::~_",
        "完整15秒",
        "剧情分析",
        "分镜形式决策",
        "角色多视角设计",
        "详细分镜图",
    ]:
        if marker not in single:
            fail(f"single template missing marker: {marker}")

    multi = (ROOT / "templates/multi-clip.md").read_text(encoding="utf-8")
    for marker in [
        "_::~CLIP_START::~_",
        "_::~CLIP_END::~_",
        "尾帧接力合约",
        "全局剧情分析",
        "分镜形式决策",
        "全局角色多视角设计",
        "全局详细分镜图",
    ]:
        if marker not in multi:
            fail(f"multi template missing marker: {marker}")

    storyboard = (ROOT / "templates/storyboard-board.md").read_text(encoding="utf-8")
    for marker in [
        "标准故事板",
        "九宫格",
        "二十五宫格",
        "智能宫格",
        "阅读顺序",
        "镜头使用清单",
        "USE",
        "REFERENCE-ONLY",
        "SKIP",
        "每格镜头卡",
        "Seedance 2.0 参考重点",
        "CAM-A0",
        "CAM-A1",
        "CAM-A-END",
        "HOLD",
        "俯视/侧视路线小图",
        "GAZE",
        "FOCUS",
        "LIGHT",
        "READ",
    ]:
        if marker not in storyboard:
            fail(f"storyboard template missing marker: {marker}")

    core_terms = [
        "原台词",
        "必要人物",
        "连续性",
        "尾帧",
        "无BGM",
        "3D国漫",
        "真人影视级",
        "状态账本",
        "真实感门槛",
        "剧情分析",
        "分镜形式决策",
        "角色设计与注册",
        "镜头拆解与取舍",
        "路线规划",
        "详细分镜图",
        "提示词编译",
        "智能宫格",
        "镜头序号",
        "Seedance 2.0",
        "角色差异化",
        "多视角设计",
        "永久角色ID",
        "独立参考图编号",
        "视觉资产与视频执行门槛",
        "角色板待生成",
        "分镜图待生成",
        "高度相似",
        "导演知识库路由（仅供参考）",
        "不要一次加载全部知识库",
        "真一镜到底",
        "伪一镜到底",
    ]
    for term in core_terms:
        if term not in skill:
            fail(f"SKILL.md missing core rule: {term}")

    knowledge_index = (ROOT / KNOWLEDGE_FILES[0]).read_text(encoding="utf-8")
    for marker in [
        "使用优先级",
        "按任务读取",
        "调用约束",
        "不要一次读取全部资料",
        "当前官方能力",
        "13字段分镜大表",
        "一镜到底",
    ]:
        if marker not in knowledge_index:
            fail(f"knowledge index missing routing boundary: {marker}")

    for relative_path in KNOWLEDGE_FILES:
        filename = Path(relative_path).name
        if filename not in skill:
            fail(f"SKILL.md must link knowledge file directly: {filename}")

    for relative_path in KNOWLEDGE_FILES[1:]:
        filename = Path(relative_path).name
        if filename not in knowledge_index:
            fail(f"knowledge index missing file: {filename}")

    for relative_path in KNOWLEDGE_FILES[1:]:
        reference_text = (ROOT / relative_path).read_text(encoding="utf-8")
        for marker in ["仓库接入说明", "## 文档导航"]:
            if marker not in reference_text:
                fail(
                    f"knowledge reference missing advisory structure in {relative_path}: {marker}"
                )

    seedance_knowledge = (
        ROOT / "references/knowledge-13-seedance-2-guide.md"
    ).read_text(encoding="utf-8")
    for marker in [
        "官方核验摘要",
        "最多 9 张图片",
        "3 段视频",
        "3 段音频",
        "直接参考文字分镜",
        "当前生成端为准",
    ]:
        if marker not in seedance_knowledge:
            fail(f"Seedance 2.0 knowledge missing verified boundary: {marker}")

    knowledge_boundaries = {
        "references/knowledge-16-shot-table-schema.md": [
            "13 个字段",
            "Shot_ID",
            "USE / REFERENCE-ONLY / SKIP",
        ],
        "references/knowledge-17-shot-table-case-study.md": [
            "局部案例摘录",
            "案例隔离",
            "不作为“完整全表”",
        ],
        "references/knowledge-18-state-change-tracking.md": [
            "永久 `CHAR-ID`",
            "block_end_snapshot",
            "概念伪代码",
        ],
        "references/knowledge-19-advanced-camera-techniques.md": [
            "可执行性闸门",
            "不得为了炫技",
            "拆镜",
        ],
        "references/knowledge-20-seedance-advanced-shot-templates.md": [
            "模板不是能力承诺",
            "永久 `CHAR-ID`",
            "CAM 节点",
        ],
        "references/knowledge-21-long-take-guide.md": [
            "真一镜到底",
            "伪一镜到底",
            "4–15 秒",
        ],
        "references/knowledge-22-seedance-long-take-templates.md": [
            "CAM 节点",
            "block_end_snapshot",
            "末帧锚点",
        ],
    }
    for relative_path, markers in knowledge_boundaries.items():
        reference_text = (ROOT / relative_path).read_text(encoding="utf-8")
        for marker in markers:
            if marker not in reference_text:
                fail(f"knowledge reference missing safety boundary in {relative_path}: {marker}")

    single_example = (ROOT / "examples/example-output-single.md").read_text(
        encoding="utf-8"
    )
    for marker in [
        "剧情分析",
        "分镜形式决策",
        "镜头使用清单",
        "USE",
        "SKIP",
        "角色多视角设计",
        "角色身份注册表",
        "详细分镜图",
        "CHAR-001",
        "CAM-A0",
        "导演方案（审阅用，不粘贴到生成器）",
        "可复制图片提示词",
        "可复制视频提示词",
        "摄影与物理合同",
        "固定服装",
    ]:
        if marker not in single_example:
            fail(f"single example missing field: {marker}")

    multi_example = (ROOT / "examples/example-output-multi-clip.md").read_text(
        encoding="utf-8"
    )
    for marker in [
        "全局剧情分析",
        "分镜形式决策",
        "镜头使用清单",
        "USE",
        "REFERENCE-ONLY",
        "SKIP",
        "全局角色多视角设计",
        "全局角色身份注册表",
        "全局详细分镜图",
        "CHAR-001",
        "全局声音规则",
        "全局摄影与物理规则",
        "转场类型",
        "状态账本更新",
        "可复制视频提示词",
        "负面约束",
    ]:
        if marker not in multi_example:
            fail(f"multi example missing field: {marker}")

    acceptance_cases = (ROOT / "tests/acceptance-cases.md").read_text(encoding="utf-8")
    for marker in [
        "对白过长且明确禁止拆分",
        "剧情分析、自适应分镜与多人差异化",
        "双胞胎例外",
        "智能宫格",
        "AI可辨识运镜箭头路线",
        "独立角色板与身份绑定",
        "多段转向运镜路线",
        "四种分镜形式的镜头取舍",
        "有依据的换场",
        "匹配剪辑或声音桥",
        "镜头复杂度过载",
        "模式隔离",
        "平台能力未知",
        "导演知识库按需调用",
        "Seedance 2.0分镜参考绑定",
        "13字段分镜大表扩展",
        "高难度镜头可执行性闸门",
        "一镜到底适用与真假标注",
        "伪一镜到底接缝连续性",
    ]:
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

    bandit_workflow = (ROOT / ".github/workflows/bandit.yml").read_text(
        encoding="utf-8"
    )
    for marker in [
        "actions/checkout@v6",
        "python-bandit-scan@",
        "exit_zero: false",
        "path: scripts",
    ]:
        if marker not in bandit_workflow:
            fail(f"Bandit workflow missing fail-closed setting: {marker}")
    if "exit_zero: true" in bandit_workflow:
        fail("Bandit workflow must not hide security findings with exit_zero: true")

    codeql_workflow = (ROOT / ".github/workflows/codeql.yml").read_text(
        encoding="utf-8"
    )
    for marker in [
        "actions/checkout@v6",
        "github/codeql-action/init@v4",
        "github/codeql-action/analyze@v4",
    ]:
        if marker not in codeql_workflow:
            fail(f"CodeQL workflow missing current action: {marker}")

    api_client = (ROOT / "scripts/seedance_client.py").read_text(encoding="utf-8")
    for marker in [
        "ARK_API_KEY",
        "SEEDANCE_MODEL",
        "--dry-run",
        "return_last_frame",
        "video_url",
        "asset://asset-id",
        "reference_image",
        "math.isfinite",
    ]:
        if marker not in api_client:
            fail(f"API client missing contract marker: {marker}")

    runtime = (ROOT / "references/runtime-orchestration.md").read_text(encoding="utf-8")
    for marker in [
        "Codex",
        "OpenClaw",
        "分镜形式决策",
        "角色设计与注册",
        "状态与镜头规划",
        "详细分镜图",
        "执行素材清单",
        "--dry-run",
        "不得无上限自动重试",
    ]:
        if marker not in runtime:
            fail(f"runtime orchestration missing boundary: {marker}")

    prompt_compiler = (ROOT / "references/prompt-compiler.md").read_text(
        encoding="utf-8"
    )
    for marker in [
        "CHAR-xxx",
        "USE",
        "REFERENCE-ONLY",
        "SKIP",
        "分镜到视频提示词的编译",
        "按时间排序的自然语言运镜",
    ]:
        if marker not in prompt_compiler:
            fail(f"prompt compiler missing execution rule: {marker}")

    continuity = (ROOT / "references/continuity-rules.md").read_text(encoding="utf-8")
    for marker in ["永久角色ID", "独立角色板", "摄影机路线最终节点", "参考图编号"]:
        if marker not in continuity:
            fail(f"continuity rules missing identity/route field: {marker}")

    api_contract = (ROOT / "references/seedance-api.md").read_text(encoding="utf-8")
    for marker in [
        "执行素材清单",
        "USE",
        "REFERENCE-ONLY",
        "SKIP",
        "独立角色板",
        "dry-run",
        "asset://",
        "reference_image",
    ]:
        if marker not in api_contract:
            fail(f"Seedance API contract missing material filter: {marker}")

    agent_integration = (ROOT / "docs/agent-integration.md").read_text(encoding="utf-8")
    for marker in ["执行素材清单", "独立角色板", "永久ID", "CAM节点", "SKIP"]:
        if marker not in agent_integration:
            fail(f"agent integration missing execution boundary: {marker}")

    openai_yaml = (ROOT / "agents/openai.yaml").read_text(encoding="utf-8")
    for marker in [
        "display_name:",
        "short_description:",
        "default_prompt:",
        "$seedance-cinemanga-director",
    ]:
        if marker not in openai_yaml:
            fail(f"agents/openai.yaml missing field: {marker}")

    forbidden_repository_strings = [
        "why200212200212" + "-cmyk",
        "sk" + "lii",
        "C:\\Users\\AS\\Desktop\\AI导演智能体开发",
    ]
    for path in ROOT.rglob("*"):
        if not path.is_file() or path.suffix.lower() not in {
            ".md",
            ".yaml",
            ".yml",
            ".py",
            ".txt",
        }:
            continue
        text = path.read_text(encoding="utf-8")
        for forbidden in forbidden_repository_strings:
            if forbidden in text:
                fail(
                    f"obsolete repository string in {path.relative_to(ROOT)}: {forbidden}"
                )

    stale_seedance_claims = {
        "references/knowledge-13-seedance-2-guide.md": ["4-16秒", "最高1080p / 2K"],
        "references/knowledge-15-video-tool-comparison.md": [
            "| **最大分辨率** | 2K |",
            "| **最长时长** | 16s |",
        ],
    }
    for relative_path, stale_claims in stale_seedance_claims.items():
        text = (ROOT / relative_path).read_text(encoding="utf-8")
        for stale_claim in stale_claims:
            if stale_claim in text:
                fail(
                    f"stale Seedance 2.0 platform claim in {relative_path}: {stale_claim}"
                )

    png_hashes: dict[str, list[str]] = {}
    for path in (ROOT / "assets").glob("*.png"):
        data = path.read_bytes()
        if len(data) < 24 or data[:8] != b"\x89PNG\r\n\x1a\n" or data[12:16] != b"IHDR":
            fail(f"invalid PNG header: {path.relative_to(ROOT)}")
        width, height = struct.unpack(">II", data[16:24])
        if width == 0 or height == 0:
            fail(f"invalid PNG dimensions: {path.relative_to(ROOT)}")
        digest = hashlib.sha256(data).hexdigest()
        png_hashes.setdefault(digest, []).append(path.name)
    duplicate_groups = [names for names in png_hashes.values() if len(names) > 1]
    if duplicate_groups:
        fail(
            "duplicate PNG content: "
            + "; ".join(", ".join(names) for names in duplicate_groups)
        )

    link_pattern = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")
    for path in ROOT.rglob("*.md"):
        text = path.read_text(encoding="utf-8")
        for raw_target in link_pattern.findall(text):
            target = raw_target.split("#", 1)[0]
            if not target or re.match(r"^(?:https?://|mailto:)", target):
                continue
            if not (path.parent / target).exists():
                fail(
                    f"broken local Markdown link in {path.relative_to(ROOT)}: {target}"
                )

    for path in ROOT.rglob("*.md"):
        text = path.read_text(encoding="utf-8")
        if "\t" in text:
            fail(f"tab character found in {path.relative_to(ROOT)}")
        if "\ufffd" in text:
            fail(f"Unicode replacement character found in {path.relative_to(ROOT)}")

    print("PASS: Seedance Cinemanga Director skill structure is valid.")


if __name__ == "__main__":
    main()
