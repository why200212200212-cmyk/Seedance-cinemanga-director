# Codex、OpenClaw 与其他 AI 接入

此仓库是平台无关的 AgentSkill。AI 负责完成剧情分析、独立角色板、身份注册、自适应分镜和导演提示词编译，`scripts/seedance_client.py` 负责调用下载者自行配置的火山方舟异步视频 API。仓库不携带用户密钥、账户权限或固定推理接入点；两层之间只有明确的“当前条可复制视频提示词 + 执行素材清单”契约。

## 最低运行条件

- AI 能读取本仓库的 `SKILL.md` 及其按需引用文件；
- 执行环境具备 Python 3.10+ 和网络访问；
- 已设置 `ARK_API_KEY`、`SEEDANCE_MODEL`，并确认账户具备相应模型权限；
- 普通参考图已转为 API 可访问的 HTTPS URL（仅本机环回测试允许 HTTP）；可信人物素材使用账户中已授权的 `asset://asset-id`；其他模态由宿主按当前官方内容格式提供。

## Codex

把仓库安装到 `$CODEX_HOME/skills/seedance-cinemanga-director` 后重新打开 Codex。让 Codex 先输出导演方案并做 `--dry-run`；只有在你明确要求“实际生成”后，才运行创建任务命令。若 Codex 的执行环境不能访问你的本地 `.env`，请在该环境安全配置密钥，不要粘贴到对话中。

## OpenClaw

按 README 的 Git 或本地目录方式安装 Skill，再用 `openclaw skills list` 与 `openclaw skills check` 确认已发现且符合运行条件。OpenClaw 代理遵循同一 `SKILL.md`，并通过 Python 脚本执行用户自行接入的 API。不同 OpenClaw 版本的命令授权与环境变量注入方式可能不同，以[官方 Skills 文档](https://docs.openclaw.ai/skills)和[官方 CLI 文档](https://docs.openclaw.ai/cli/skills)为准；本仓库不要求专有 OpenClaw API。

## 其他 AI / Agent

将 `SKILL.md` 作为入口加载，并保持相对目录结构。宿主只要能执行脚本即可直接使用；若不能执行本地命令，可依据 `docs/api-integration.md` 中的官方接口契约实现等价工具，但必须保留以下安全行为：

- POST 创建任务不自动重试；
- 先 dry-run 再经用户授权创建；
- 密钥不进入模型上下文；
- 参考图编号与内容数组顺序严格一致；
- Seedance 2.0 参考图内容项使用 `role: reference_image`，未授权真人素材不得冒充可信人物资产；
- 每个角色独立角色板与永久ID保持一致，多人合并图不作为身份绑定；
- 只提交当前条USE镜头需要的素材；SKIP不提交，REFERENCE-ONLY不占独立视频时长；
- CAM节点先编译为按时间排序的自然语言运镜，不把箭头图例当成最终画面文字；
- 轮询只接受官方任务状态，不伪造完成结果。

完整编排规则见 `references/runtime-orchestration.md`，API 命令见 `docs/api-integration.md`。

## 宿主工具映射

宿主若要把脚本封装为自己的工具，应保持以下最小能力与权限边界，不需要改变导演流程：

| 能力 | 脚本命令 | 网络/费用边界 |
|---|---|---|
| 本地自检 | `doctor` | 默认不联网，不产生费用 |
| 只读连通性 | `doctor --remote` | 仅由用户主动触发，读取任务列表 |
| 请求预览 | `create ... --dry-run` | 不联网，不创建任务 |
| 创建视频 | `create ...` | 可能计费，必须有用户明确生成指令 |
| 查询/恢复 | `status`、`list`、`wait` | 只读任务状态；不重发创建请求 |
| 取消任务 | `cancel` | 改变远程任务状态，应确认目标任务ID |

无论宿主采用 shell tool、函数调用还是自定义插件，都从宿主自己的秘密存储或环境变量注入凭证，不把密钥放进提示词、工具参数或 Skill 文件。
