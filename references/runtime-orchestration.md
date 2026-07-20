# Agent 运行编排

本 Skill 的导演能力与执行端分离，因此可被 Codex、OpenClaw 或其他能够读取 AgentSkills、执行 Python 命令的 AI 使用。平台无需实现专有插件，只需把仓库作为 Skill 加载，并在实际生成时提供火山方舟凭证。

## 标准流水线

1. **剧情分析**：读取剧本、参考图与用户约束，建立事实表、人物清单、剧情节拍和时间预算。
2. **分镜形式决策**：按剧情节拍、镜头规模和信息密度选择标准故事板、九宫格、二十五宫格或智能宫格；只决定载体，不提前生成图。
3. **角色设计与注册**：每个必要角色单独生成多视角角色板，建立永久ID、参考图编号和身份注册表。
4. **状态、镜头与九部门会审**：建立状态账本、USE/REFERENCE-ONLY/SKIP清单和镜头合约；按 `references/cinematic-department-review.md` 统一导演/PERF表演因果、视觉构造、摄影、光影、调色、化妆、人物妆造、声音与混音，必要时按 `templates/color-palette-board.md` 生成PAL色卡资产。
5. **双层详细分镜图**：所有执行信息准备完成后，先生成无字无箭头的CLEAN画格/页面，再在同构副本上确定性叠加镜头号、信息栏及CAM/ACT/GAZE/FOCUS/LIGHT/READ，形成REVIEW审阅页；每格建立稳定PANEL-ID并导出独立CLEAN单格。
6. **单格选择与导演编译**：根据小说/剧本、USE状态和当前VID选择需要的视频PANEL-ID；读取REVIEW层路线并转成自然语言，只绑定对应CLEAN单格。随后只加载当前 3D 或真人专项规则，先按 `references/prompt-compiler.md` 优化原提示词，再按 `templates/compiled-video-prompt.md` 编译当前VID唯一可复制视频提示词；电影质感转译为可执行摄影/光色/材质/运动/声音，人物生命感转译为目标—阻碍—刺激—反应及可见微动作；排除SKIP、REVIEW路线层、部门会审表和制作标注。
7. **硬门槛质检**：检查剧情忠实度、角色绑定、镜头取舍、路线、时间预算、物理可信度、STYLE/PAL/LOOK/PERF/LGT/AUD作用域、声音与连续性。
8. **请求预检**：API 由下载者在宿主环境中自行配置。先执行离线 `doctor`，再建立当前条执行素材绑定清单，把可复制视频提示词写入临时 UTF-8 文件；逐项核对角色ID、VID/PANEL/CLEAN-ASSET-ID、PAL-ID、USE镜头和图片编号，再按必要角色板、被选CLEAN单格、场景板、可选REFERENCE-ONLY COLOR色卡和尾帧的声明顺序构建 API 请求，并先执行 `--dry-run`。REVIEW板、箭头、节点、图例和无关格不得提交。
9. **用户授权**：只有用户明确要求实际生成且凭证、模型权限、费用预期均已确认，才创建任务。
10. **异步执行**：创建任务，轮询至终态；成功时下载成片，失败时返回官方错误，不虚构结果。若创建响应在返回任务ID前发生不确定网络错误，先用 `list` 恢复已有任务，不重发可能计费的 POST。
11. **成片复核**：如果执行环境能读取视频或抽帧，按 `references/quality-checklist.md` 复核身份、动作、空间、路线结果、光影、对白与尾帧。需要重试时先指出具体失败项，再最小幅度修订提示词；不得无上限自动重试付费任务。
12. **定点修订**：用户指出某张图、某条视频、镜头号或时间段不满意时，按稳定资产ID和版本号建立修订单；先展示新版完整提示词并等待用户修改或批准，再只生成该图片或该VID的新候选。旧版保留到新候选通过质检；下游影响只标 `REVIEW_REQUIRED`，不自动连锁生成。

## 平台无关调用

若 Codex、OpenClaw 或其他宿主已经提供由用户配置的 Seedance/火山方舟工具，可将下述创建、查询、取消与下载动作映射到该工具，但仍必须遵守同一字段顺序、授权和费用边界。没有现成工具时，在仓库根目录统一调用：

```bash
python scripts/seedance_client.py doctor
# 仅在用户主动要求核验其自有配置时执行；只发起读取任务列表的请求
python scripts/seedance_client.py doctor --remote
python scripts/seedance_client.py create --prompt-file <临时提示词文件> --dry-run
python scripts/seedance_client.py create --prompt-file <临时提示词文件> --wait --output <目标视频路径>
python scripts/seedance_client.py list --status running --filter-model <推理接入点ID>
```

多参考图按执行素材清单顺序重复传入 `--image-url`；参数接受 API 可访问的 HTTPS URL（仅本机环回测试允许 HTTP），也接受已授权可信人物素材的 `asset://asset-id`，客户端会写入 `role: reference_image`。每个角色必须使用独立角色板；宫格/故事板只提交剧情选中的 `PANEL-ID-CLEAN`，REVIEW标注层只用于编译路线；色卡如提交则必须是当前VID的无UI `REFERENCE-ONLY COLOR`，提示词同时写关键P编号/HEX/对象并禁止渲染标签版式。当前条不需要的角色、无关格、其他VID色卡、SKIP镜头与文档装饰图不得提交。首尾帧、视频、音频或账户新增格式使用 `--content-json` 透传当前官方结构，不得自行猜测字段。

## AI 行为边界

- 不在回答、日志或命令行参数中回显 API key；优先从 `.env` 或环境变量读取。
- 不把仓库示例值当成用户凭证或模型权限；API Key、模型/推理接入点和网络授权始终由下载者在自己的宿主环境中配置。
- 不把“导演方案（审阅用）”、状态账本或隐藏推理提交给生成模型。
- 不因用户说“做到极致”而堆叠矛盾镜头、不可拍运动或空泛画质词；极致来自可执行的摄影、表演、材质、光照、声音与连续性约束。
- 不把 API 成功等同于成片合格；生成结果仍需按当前模式专项门槛检查。
- 不在没有用户实际生成指令时调用可能计费的创建接口。
- 不把“不满意”自动解释为授权重生成；先交付 `AWAITING_USER` 提示词预览，收到明确批准后才创建新候选任务。
