# Skill Architecture

<p align="center">
  <img src="../assets/system-architecture.png" alt="System Architecture" width="100%">
</p>

## 设计目标

本仓库采用“薄入口、强参考、可复用模板、可验证示例”的结构，使主 `SKILL.md` 保持清晰，同时允许后续扩展题材、镜头规则和输出格式。

## 分层

### 1. 入口层：`SKILL.md`

负责：

- 触发条件；
- 最高优先级规则；
- 双影视模式；
- 模式选择；
- 总体导演流程；
- 引用模板与规则库。

### 2. 输出层：`templates/`

- `single-15s.md`：完整15秒单条；
- `multi-clip.md`：连续多条4–15秒与尾帧合约。
- `storyboard-board.md`：标准故事板、九宫格、二十五宫格和智能宫格的详细分镜图。

模板只定义成品结构，不承载所有解释性规则。

### 3. 规则层：`references/`

- 连续性；
- 质量检查；
- 风格模式；
- 对白时长；
- 镜头语言；
- 自适应分镜形式与 Seedance 2.0 详细分镜图；
- 角色多视角设计与不同角色面部差异化；
- 3D影视级制作；
- 真人摄影与表演；
- 提示词编译与冲突消解。

规则文件可独立迭代，避免主入口无限膨胀。

### 4. 示例层：`examples/`

使用完全原创、无私人信息的样例验证：

- 输入如何表达；
- 单条模式如何输出；
- 多条模式如何建立尾帧接力。

### 5. 资产层：`assets/`

存放项目主视觉、架构图、技能总览、图标资产板，以及九宫格、二十五宫格、智能宫格、标准故事板和角色差异化等示例图片。图片用于文档展示和视觉说明；生成任务仍以文字规则、角色板与当前分镜图为执行依据。

### 6. 验证层：`scripts/` 与 `tests/`

- `validate_skill.py`：结构与关键字段静态校验；
- `acceptance-cases.md`：人工验收场景。

## 数据流

```text
用户素材
  ↓
剧情分析：事实、原台词、关系、节拍与时间预算
  ↓
必要人物过滤
  ↓
模式判断（单条 / 多条）
  ↓
分镜形式决策（标准 / 九宫格 / 二十五宫格 / 智能宫格）
  ↓
角色多视角设计与差异化锁定
  ↓
详细分镜图：镜头序号、阅读顺序与执行标注
  ↓
镜头合约与表演调度
  ↓
状态账本与复杂度预算
  ↓
对白时长、光影、声音设计
  ↓
3D / 真人专项真实感校验
  ↓
连续性与尾帧校验
  ↓
模板化最终输出
```

## 与视觉资产的对应关系

- `cover-banner.png`：品牌封面；
- `skill-preview.png`：功能总览；
- `system-architecture.png`：流程架构图；
- `storyboard-example.png`：标准执行板示例；
- `nine-grid-example.png`：九宫格板式示例；
- `twenty-five-grid-example.png`：长序列板式示例；
- `adaptive-storyboard-workflow.png`：自适应分镜形式决策；
- `character-differentiation-board.png`：角色差异化说明（非运行时合并角色板）；
- `ai-readable-camera-routes.png`：AI可辨识运镜与动作路线语法；
- `segmented-camera-path.png`：多段运镜节点、逐段箭头与同步俯视/侧视路线；
- `icons-board.png`：视觉语言与模块化图标资产板。
- `workflow-architecture.png`：十阶段工作流与仓库结构详图；
- `prompt-output-system.png`：单条、多条及尾帧交付结构；
- `visual-assets-qa.png`：视觉资产和质检门槛总览。

## 扩展约定

新增规则时：

- 通用硬规则放 `references/`；
- 新输出形态放 `templates/`；
- 可复现用例放 `examples/` 或 `tests/`；
- 主入口只增加导航和最高优先级原则；
- 不引入不必要的脚本依赖。
