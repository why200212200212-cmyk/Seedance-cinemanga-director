# Runway Gen-4 运镜控制与提示词完全指南

> 仓库接入说明：本文件只在用户明确使用 Runway 或要求跨平台翻译时读取。版本名称、预设、时长、帧率、种子和参数面板可能变化；未核对当前官方文档前，不得视为可用能力，也不得覆盖 Seedance 的提示词与素材绑定合同。

## 文档导航

- 一、图像与提示词分工
- 二、提示词结构
- 三、运镜关键词
- 四、时间戳控制
- 五、内置预设
- 六、最佳实践
- 七、技术参数
- 八、迭代工作流
- 九、常见问题

> 收集时间：2026-07-15 | 来源：官方文档 + 社区最佳实践

---

## 一、核心理念：图像与提示词的分工

| 输入 | 负责范围 | 核心规则 |
|---|---|---|
| **参考图像** | 所有视觉身份：主体外观、环境、颜色、光线、构图、风格 | 图像已经是第一帧 |
| **文本提示词** | **仅描述运动**：运镜、主体动作、环境变化、时间推进 | 不要描述图像已经有的内容 |

> **关键规则**：图像是Frame 1，提示词描述的是"接下来发生什么"

---

## 二、提示词结构公式

### 2.1 标准公式
```
[Camera Motion] + [Subject Motion] + [Scene Motion] + [Style/Pacing]
```

### 2.2 四类核心运动

| 类别 | 描述 | 示例 |
|---|---|---|
| **主体运动** | 角色/物体如何移动 | `The subject slowly looks toward camera` |
| **摄影机运动** | 镜头如何移动 | `Camera drifts slightly right, keeping subject centered` |
| **场景运动** | 环境动态 | `Fog rolls through, leaves rustle in breeze` |
| **风格描述符** | 视觉基调与节奏 | `Soft morning light, documentary feel, film grain` |

---

## 三、运镜关键词大全

### 3.1 基础运镜
| 英文 | 中文 | 效果 | 示例 |
|---|---|---|---|
| slow push-in | 慢推 | 逐步靠近主体 | `Camera slowly pushes in on the subject's face` |
| tracking shot | 跟拍 | 跟随运动主体 | `Handheld tracking shot following the runner` |
| pan left/right | 横摇 | 水平旋转 | `Smooth pan right revealing the city skyline` |
| tilt up/down | 纵摇 | 垂直旋转 | `Camera tilts up from feet to face` |
| dolly in/out | 推拉 | 物理移动 | `Slow dolly in, shallow depth of field` |
| crane shot | 升降 | 大范围垂直+水平 | `Crane shot descending to street level` |
| static/locked off | 固定 | 零运镜 | `Camera holds completely static` |
| handheld drift | 手持漂移 | 轻微自然晃动 | `Subtle handheld drift, documentary feel` |
| whip pan | 甩镜 | 快速方向突变 | `Quick whip pan to the action` |

### 3.2 高级技巧
| 技巧 | 提示词示例 |
|---|---|
| **速度调制** | `Gentle start, accelerating push-in` |
| **拉焦** | `Rack focus from foreground to background` |
| **镜头模拟** | `24mm wide-angle feel, slight distortion` |
| **视差** | `Handheld with natural parallax between layers` |
| **FPV/POV** | `First-person POV, slight head bob` |

---

## 四、时间戳控制（Gen-4.5特性）

对复杂序列使用显式时间戳：

```
00:00 - 00:02: Camera holds wide, subject enters frame left
00:02 - 00:05: Slow push-in to medium shot as subject turns
00:05 - 00:07: Camera orbits 180° around subject
00:07 - 00:10: Quick zoom out to reveal full environment
```

> 适用场景：多动作连续序列 → 推荐使用10秒时长

---

## 五、Gen-4.5内置运镜预设

Runway Gen-4.5 提供预置的运镜参数模板：

| 预设 | 效果 | 适用 |
|---|---|---|
| Camera Presets | 预测试过的运镜Prompt模式 | 快速原型 |
| Movement Presets | 主体运动模式 | 角色动画 |
| Action Presets | 动作序列模式 | 动态场景 |

---

## 六、最佳实践

### DO:
- ✅ 用动词开头：`rotates`, `drifts`, `accelerates`, `settles`
- ✅ 用肯定表达：`Camera holds still`（不说 `no camera movement`）
- ✅ 精确描述速度：`slowly`, `gradually`, `quick snap`
- ✅ 用完整句子，不用关键词列表
- ✅ 先简单后复杂，逐步添加要素
- ✅ 锁种子（Lock seeds）保持风格一致

### DON'T:
- ❌ 不要描述图像已有的内容（冗余，可能混淆模型）
- ❌ 不要使用负面提示（`no blur`, `don't move`）
- ❌ 不要要求单段生成多个场景
- ❌ 不要给出矛盾指令（`static camera` + `fast orbit`）
- ❌ 不要用对话式语言（`Can you make...`）

---

## 七、技术参数

| 设置 | 建议值 |
|---|---|
| **时长** | 5s（简单动作）；10s（复杂序列） |
| **FPS** | 24fps（电影）；25fps（广播电视） |
| **速度** | Low（干净边缘）；Medium（电影化）；High（可能有崩坏） |
| **画幅** | 16:9（叙事）；9:16（社交-居中构图） |

---

## 八、迭代工作流

```
Step 1: 简单运动测试（5秒）
    ↓
Step 2: 添加运镜
    ↓
Step 3: 添加场景/环境运动
    ↓
Step 4: 添加风格描述符
    ↓
Step 5: 扩展到10秒（如需）
    ↓
Step 6: 锁种子，优化运动强度
```

---

## 九、常见问题解决

| 问题 | 解决方案 |
|---|---|
| 运动太快 | 缩小景深范围（`tight medium shot`） |
| 高速崩坏 | 降一档速度，简化纹理 |
| 背景蠕动 | 避免细小重复图案，降低速度 |
| 风格不一致 | 锁种子，只改变运动参数 |
| 竖屏（9:16） | 居中构图，横向运动更明显 |

---

*本文档供AI导演智能体参考*
