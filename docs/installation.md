# Installation

## 推荐：构建最小安装包

仓库根目录同时包含 GitHub 文档、测试和展示图片。给 AI 宿主安装时可先构建精简包：

```bash
python scripts/build_skill_package.py
```

解压 `dist/seedance-cinemanga-director.zip` 后，目录根部会直接包含 `SKILL.md`。安装包只保留运行所需的参考资料、模板、Agent 元数据、API 客户端、空白环境变量示例和许可证；不会打包真实 `.env`、测试、展示图片或项目维护文档。

## Codex 手动安装

将仓库克隆或复制到：

```text
$CODEX_HOME/skills/seedance-cinemanga-director
```

未设置 `CODEX_HOME` 时使用：

```text
~/.codex/skills/seedance-cinemanga-director
```

目录根部必须直接包含 `SKILL.md`。重新打开 Codex 后即可发现该 Skill。

## OpenClaw Git 安装

```bash
openclaw skills install git:juebai-aigc/Seedance-cinemanga-director@main
```

需要本机已安装兼容的 OpenClaw CLI；本仓库的校验器不验证该第三方命令的安装、认证或网络行为。

## 本地安装

```bash
git clone https://github.com/juebai-aigc/Seedance-cinemanga-director.git
openclaw skills install ./Seedance-cinemanga-director
```

## 手动放置

将整个仓库目录复制到一个受支持的 Skill 根目录，例如：

```text
<workspace>/skills/seedance-cinemanga-director
```

目录根部必须直接包含 `SKILL.md`，不能再多套一层文件夹。

## 验证

```bash
python scripts/validate_skill.py
```

成功时输出：

```text
PASS: Seedance Cinemanga Director skill structure is valid.
```

安装到 OpenClaw 后还可执行：

```bash
openclaw skills list
openclaw skills check
```

命令及支持路径以 [OpenClaw 官方 Skills CLI 文档](https://docs.openclaw.ai/cli/skills)为准。
