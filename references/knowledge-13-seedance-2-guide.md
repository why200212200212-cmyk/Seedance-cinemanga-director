# Seedance 2.0（字节跳动）AI视频生成工具全指南

> 仓库接入说明：本文件是 Seedance 2.0 参考资料，不是 API 或界面能力合同。官方核验日期为 2026-07-15；未被官方资料明确确认的距离、角度、半径、速度曲线、种子锁定、分辨率和时长参数均标为待验证，不得直接承诺可用。

## 官方核验摘要（优先于下方原资料）

- 已确认支持文本、图片、音频和视频四种输入模态；可同时参考最多 9 张图片、3 段视频和 3 段音频。
- 已确认可参考输入素材的构图、镜头语言、运镜、动作节奏、视觉效果与声音，并可直接参考文字分镜。
- 当前官方页面明确生成时长为 4–15 秒、最高分辨率为 1080p；具体 API 可选档位、画幅和账户配额仍以当前生成端为准。
- 已确认多主体一致性、文字渲染和复杂编辑仍可能失败，因此详细分镜、独立角色板和执行素材清单仍需保留。
- 使用已授权的可信人物素材时，API 参考项使用 `asset://asset-id`，并在内容项顶层标记 `role: reference_image`；普通角色板使用生成端可访问的 HTTPS URL（仅本机环回测试允许 HTTP）。

官方来源：[Seedance 2.0 发布说明](https://seed.bytedance.com/en/blog/seedance-2-0-official-launch)、[火山引擎提示词指南](https://www.volcengine.com/docs/82379/2222480?lang=zh)、[火山引擎 Seedance 2.0 页面](https://www.volcengine.com/activity/seedance2)、[可信人物素材 API 说明](https://www.volcengine.com/docs/82379/2315856?lang=zh)。

## 文档导航

- 一、产品定位
- 二、创作模式
- 三、运镜控制
- 四、多模态参考
- 五、提示词结构
- 六、输出规格
- 七、工作流程
- 八、经验建议
- 九、竞品对比

> 收集时间：2026-07-15 | 来源：官方API文档 + 社区资料

---

## 一、产品定位

Seedance 2.0 是字节跳动（ByteDance）推出的AI视频生成模型。原资料将其概括为“导演级自动摄影机”；执行时把这句话视为能力定位，不把它当成精确运镜必然成功的保证。

**参考优势**：可联合理解剧情、运镜、灯光、动作和声音；复杂结果仍须通过分镜、独立角色板、执行素材清单与成片质检约束。

---

## 二、三大创作模式

| 模式 | 英文 | 适用场景 |
|---|---|---|
| **文生视频** | Text to Video (T2V) | 无参考图直接生成，擅长真人角色 |
| **参考转视频** | Reference to Video (R2V) | 融合多张图片/视频的元素 |
| **首尾帧控制** | First-Last-Frame to Video (FLF2V) | 精确控制镜头的起始和结束画面 |

---

## 三、运镜控制能力

### 3.1 原资料列举的运镜表达

下表用于把视觉意图写清楚。距离、角度、半径、速度曲线和主体锁定精度尚未逐项获得官方参数合同确认，不得承诺数值一定被严格执行。

| 运镜 | 中文 | 控制参数 |
|---|---|---|
| **Dolly In/Out** | 推/拉镜头 | 距离（英尺/米），速度，加速曲线 |
| **Pan Left/Right** | 横摇 | 方向，速度 |
| **Tilt Up/Down** | 纵摇 | 角度（度数），速率 |
| **Orbit / Arc** | 环绕/弧线 | 方向（顺时针/逆时针），半径（英尺），时长 |
| **Tracking** | 跟拍 | 跟随目标，速度 |
| **Crane Up/Down** | 升降 | 高度（英尺），地平线控制 |
| **Whip Pan** | 甩镜 | 时长，模糊强度，同步点 |
| **Handheld** | 手持模拟 | 漂移强度，随机模式 |
| **Slow Zoom + Follow** | 慢推+跟踪 | 变焦幅度，主体检测 |
| **Parallax Lateral Pan** | 视差横移 | 多层景深分离，视差强度 |

### 3.2 高级电影技法

| 技法 | 说明 | 提示词示例 |
|---|---|---|
| **Dolly Zoom（滑动变焦）** | 推/拉同时反向变焦 | `dolly forward 15 feet while zooming back 1.5x, maintain subject size` |
| **Dutch Angle（荷兰角）** | 摄影机倾斜制造不安 | `Dutch angle 15 degrees, tense atmosphere` |
| **Rack Focus（拉焦）** | 焦点在不同距离间切换 | `rack focus from foreground to background` |
| **多镜叙事序列** | 单次Prompt生成连贯多镜头 | `0-3s: wide shot; 3-7s: push-in; 7-12s: POV` |

---

## 四、多模态参考控制系统

Seedance 2.0 的核心特色——用参考素材精确控制生成：

| 输入类型 | 数量限制 | 用途 |
|---|---|---|
| **图片参考** | 最多9张 | 锁定构图和角色外观 |
| **视频参考** | 最多3个；单段时长以生成端为准 | 参考运镜轨迹、动作模式和节奏，不承诺逐帧复制 |
| **音频参考** | 最多3个；单段时长以生成端为准 | 参考声画节奏和声音特征 |

**素材引用**：按生成端显示的 `@素材编号` 或 API `content` 顺序绑定；不得自行假定固定英文编号格式。

---

## 五、标准提示词结构

### 5.1 官方推荐结构
```
[Subject] + [Action] + [Setting] + [Cinematics]
```

| 层级 | 内容 | 示例 |
|---|---|---|
| **主体** | 谁/什么 | "A young woman in a red coat" |
| **动作** | 他们在做什么 | "walks slowly through falling snow" |
| **环境** | 在哪里 | "in a quiet European street at dusk" |
| **电影化** | 运镜/灯光/风格 | "Tracking shot, shallow depth of field, cinematic color grading" |

### 5.2 运镜控制Prompt结构
```
Camera: [move] + [speed] + [subject lock]
Lens (optional): [focal length/feel]
Stability: [tripod/handheld/gimbal]
```

**示例**：
```
Camera: Slow 4-second dolly push-in + subtle tilt up 5 degrees.
Subject lock: Keep woman centred in medium shot.
Lens: 50mm cinematic feel.
Stability: Gimbal-stabilized, no shake.
```

### 5.3 时间控制Prompt

```
"0-3 seconds: character looks up suddenly
3-7 seconds: camera pushes in to close-up
7-12 seconds: rain begins, character turns and walks away"
```

---

## 六、输出规格

| 参数 | 规格值 |
|---|---|
| **时长** | 当前官方页面为4–15秒；具体可选步长以生成端为准 |
| **帧率** | 当前核验来源未确认固定可选档位；以生成端为准 |
| **分辨率** | 当前官方页面最高1080p |
| **画幅比** | 以当前生成端可选项为准 |
| **生成速度** | 受模型、分辨率、排队和账户资源影响，必须实测 |
| **原生音频** | 已确认支持音视频联合输出；具体语种与开关以生成端为准 |

---

## 七、工作流程

```
Step 1: 选择模型与模式
    → Seedance 2.0 → T2V/R2V/FLF2V
Step 2: 编写Prompt
    → 遵循标准结构 → 避免负面描述
Step 3: 配置输出设置
    → 质量分级（Basic/High）→ 画幅 → 时长 → 音频
Step 4: 提交并等待
    → 轮询任务状态
Step 5: 后处理（可选）
    → 链式生成 → 视频拼接 → 多段整合
```

### 多段/长内容工作流

| 技术 | 方法 |
|---|---|
| **链式生成** | 用相同角色参考图生成连续片段 |
| **视频扩展** | 上传完成片段作为参考继续扩展 |
| **外部拼接** | 在剪辑软件中拼接（CapCut等） |

---

## 八、Pro Tips

### 运镜注意事项
| 问题 | 解决方案 |
|---|---|
| 随机变焦乱入 | 显式声明 `no zoom` 或 `maintain subject size` |
| 画面抖动 | 添加稳定性提示：`tripod stable`, `smooth gimbal` |
| AI忽略指令 | 每次最多2-3个运镜组合 |
| 背景几何扭曲 | 减少同镜主体与运动层级，缩短复杂运镜，固定空间锚点并优先提供场景/运镜参考；胶片颗粒和镜头风格词不能修复几何错误 |
| 滑动变焦效果 | 参考视频复制法远好于纯文本描述 |

### 最佳实践
1. ✅ **先用强动词开头**："rotates", "drifts", "accelerates"
2. ✅ **用全句描述**，不是零散的关键词列表
3. ✅ **先简单后复杂**：先测试5秒单一动作，再逐步加要素
4. ✅ **用参考视频复制运镜**——比文本描述精确得多
5. ✅ 仅当当前生成端明确提供种子或一致性控制时才启用；否则依靠独立角色板、永久ID和连续性账本

---

## 九、原资料竞品对比（时间敏感，待逐项核验）

| 维度 | Seedance 2.0 | Runway Gen-4 | Kling 3.0 |
|---|---|---|---|
| 运镜精度 | ★★★★ 复杂路径 | ★★★★★ Motion Brush | ★★★ 基础运镜 |
| 运动物理 | ★★★★★ 最佳 | ★★★★ | ★★★★ |
| 原生音频 | ✅ 7+语言唇同步 | ❌ 需后期 | ⚠️ 3.0 Omni部分支持 |
| 多镜叙事 | 2-3镜 | 有限 | 最多6镜 |
| 生成速度 | ★★★★★ 最快 | ★★★ 慢 | ★★★★ |
| 分辨率 | 当前官方页面最高1080p | 待核验 | 待核验 |
| AI理解力 | ★★★★★ 电影语言 | ★★★★ 精确控制 | ★★★★ 中文优先 |

---

*本文档供AI导演智能体参考，基于网络搜索收集整理*
