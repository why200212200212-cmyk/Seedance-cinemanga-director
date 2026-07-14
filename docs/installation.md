# Installation

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
openclaw skills install git:why200212200212-cmyk/Seedance-cinemanga-director@main
```

需要本机已安装兼容的 OpenClaw CLI；本仓库的校验器不验证该第三方命令的安装、认证或网络行为。

## 本地安装

```bash
git clone https://github.com/why200212200212-cmyk/Seedance-cinemanga-director.git
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
