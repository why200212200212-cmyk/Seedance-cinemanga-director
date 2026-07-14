# Codex、OpenClaw 与其他 AI 接入

此仓库是平台无关的 AgentSkill。AI 负责把素材编译为导演级提示词，`scripts/seedance_client.py` 负责调用火山方舟异步视频 API。两层之间只有明确的“可复制视频提示词 + 有序参考素材”契约。

## 最低运行条件

- AI 能读取本仓库的 `SKILL.md` 及其按需引用文件；
- 执行环境具备 Python 3.10+ 和网络访问；
- 已设置 `ARK_API_KEY`、`SEEDANCE_MODEL`，并确认账户具备相应模型权限；
- 参考图已转为 API 可访问的 HTTP(S) URL，或由宿主平台按官方内容格式提供。

## Codex

把仓库安装到 `$CODEX_HOME/skills/seedance-cinemanga-director` 后重新打开 Codex。让 Codex 先输出导演方案并做 `--dry-run`；只有在你明确要求“实际生成”后，才运行创建任务命令。若 Codex 的执行环境不能访问你的本地 `.env`，请在该环境安全配置密钥，不要粘贴到对话中。

## OpenClaw

按 README 的 Git 或本地目录方式安装 Skill。OpenClaw 代理遵循同一 `SKILL.md`，并通过 Python 脚本执行 API。不同 OpenClaw 版本的命令授权与环境变量注入方式可能不同，以所用版本文档为准；本仓库不要求专有 OpenClaw API。

## 其他 AI / Agent

将 `SKILL.md` 作为入口加载，并保持相对目录结构。宿主只要能执行脚本即可直接使用；若不能执行本地命令，可依据 `docs/api-integration.md` 中的官方接口契约实现等价工具，但必须保留以下安全行为：

- POST 创建任务不自动重试；
- 先 dry-run 再经用户授权创建；
- 密钥不进入模型上下文；
- 参考图编号与内容数组顺序严格一致；
- 轮询只接受官方任务状态，不伪造完成结果。

完整编排规则见 `references/runtime-orchestration.md`，API 命令见 `docs/api-integration.md`。
