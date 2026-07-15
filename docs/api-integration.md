# Seedance API 接入与运行

仓库提供零第三方依赖的 `scripts/seedance_client.py`，对接火山方舟视频生成异步任务接口。它负责创建、查询、等待、取消和下载；提示词质量仍由 `SKILL.md`、模式规范、连续性账本和编译器规则负责。

> 创建视频任务可能产生费用。CI、结构校验和本文示例默认只做 `--dry-run`，不会调用生成服务。

## 1. 配置

需要 Python 3.10 或更高版本。在仓库根目录复制环境变量示例：

```bash
cp .env.example .env
```

Windows PowerShell：

```powershell
Copy-Item .env.example .env
```

编辑 `.env`：

```dotenv
ARK_API_KEY=你的火山方舟API_Key
SEEDANCE_MODEL=你的模型ID或推理接入点ID
ARK_BASE_URL=https://ark.cn-beijing.volces.com/api/v3
```

`.env` 已被 Git 忽略。不要把真实密钥提交到仓库、聊天记录或提示词。示例中的 `doubao-seedance-2-0-260128` 是当前公开资料使用的模型标识；是否可用、具体能力和配额以你的方舟账户为准，也可改为已开通的推理接入点 ID。

## 2. 先检查请求，不产生任务

把 Skill 输出中的“可复制视频提示词”单独保存为 UTF-8 文本，然后执行：

```bash
python scripts/seedance_client.py --model doubao-seedance-2-0-260128 create --prompt-file examples/api-prompt.txt --dry-run
```

普通参考图必须是 API 可访问的 HTTPS URL；已获本人授权并进入火山方舟可信素材库的人物，也可使用官方 `asset://asset-id` URI。只有本机环回测试允许 HTTP。两者都按“图片1、图片2……”的语义顺序传入，客户端会为每项写入 `role: reference_image`：

```bash
python scripts/seedance_client.py create --prompt-file prompt.txt --image-url https://example.com/character.png --image-url https://example.com/location.png --dry-run
```

可信人物资产示例（只使用账户中确实可用且已授权的 Asset ID）：

```bash
python scripts/seedance_client.py create --prompt-file prompt.txt --image-url asset://asset-你的授权资产ID --dry-run
```

提交前先建立执行素材清单，例如：

```text
图片1 = CHAR-001角色A独立多视角角色板（当前条USE镜头S01、S03）
图片2 = CHAR-002角色B独立多视角角色板（当前条USE镜头S02、S03）
图片3 = 当前条执行分镜页（只含USE与必要REFERENCE-ONLY）
图片4 = 固定场景板或上一条尾帧
```

不得提交SKIP镜头、弃用分镜页、多人角色对比装饰图或与当前条无关的角色板。若参考素材数量受账户能力限制，优先保留当前条出镜角色的独立角色板、执行分镜页和连续接力尾帧；不要通过多人拼图规避限制。

## 3. 创建并等待结果

确认 dry-run 请求体后，以下命令才会创建真实任务并可能产生费用：

```bash
python scripts/seedance_client.py create --prompt-file prompt.txt --wait --output outputs/seedance.mp4
```

也可以分步操作：

```bash
python scripts/seedance_client.py create --prompt-file prompt.txt
python scripts/seedance_client.py list --status running --filter-model ep-你的推理接入点ID
python scripts/seedance_client.py status cgt-你的任务ID
python scripts/seedance_client.py wait cgt-你的任务ID --output outputs/seedance.mp4
python scripts/seedance_client.py cancel cgt-你的任务ID
```

创建命令支持 `--callback-url` 与 `--return-last-frame`。创建请求不会自动重试，以免重复产生付费任务；状态查询只对 429 和服务端错误做有限重试。如果创建时断网且无法确定服务端是否已接收，先用 `list` 按状态、任务ID或推理接入点找回已有任务，不要直接再次创建。API 请求拒绝重定向，避免鉴权头被转发到其他地址；视频下载只跟随通过同一 HTTPS/环回地址规则验证的重定向。

## 4. 官方内容数组透传

当账户开放新的图像、音频或视频输入格式时，把官方定义的 `content` 数组保存为 JSON：

```json
[
  {"type": "text", "text": "这里放可复制视频提示词"},
  {
    "type": "image_url",
    "image_url": {"url": "https://example.com/reference.png"},
    "role": "reference_image"
  }
]
```

然后先检查、再创建：

```bash
python scripts/seedance_client.py create --content-json content.json --dry-run
python scripts/seedance_client.py create --content-json content.json --wait
```

客户端只验证通用结构，不虚构尚未核实的多模态字段；实际字段、大小、数量、分辨率、时长和音频开关以官方文档及账户控制台为准。

## 5. 官方资料

- [创建视频生成任务](https://api.volcengine.com/api-docs/view?action=CreateContentsGenerationsTasks&serviceCode=ark&version=2024-01-01)
- [查询视频生成任务](https://api.volcengine.com/api-docs/view?action=GetContentsGenerationsTask&serviceCode=ark&version=2024-01-01)
- [查询视频生成任务列表](https://api.volcengine.com/api-docs/view?action=ListContentsGenerationsTasks&serviceCode=ark&version=2024-01-01)
- [取消/删除视频生成任务](https://api.volcengine.com/api-explorer/debug?action=DeleteContentsGenerationsTasks&groupName=%E8%A7%86%E9%A2%91%E7%94%9F%E6%88%90API&serviceCode=ark&version=2024-01-01)
- [Seedance 2.0 提示词指南](https://www.volcengine.com/docs/82379/2222480?lang=zh)
- [Seedance 2.0 可信人物素材与 Asset URI](https://www.volcengine.com/docs/82379/2315856?lang=zh)

本执行层使用火山方舟公开 API 契约；它不改变仓库的非官方社区项目性质，也不代表即梦、Seedance 或火山引擎的授权或背书。
