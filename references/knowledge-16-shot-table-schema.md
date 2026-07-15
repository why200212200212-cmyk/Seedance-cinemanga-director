# AI短剧分镜大表 — 完整字段词典与规范

> 仓库接入说明：本文件只在用户要求工业化分镜大表、复杂项目字段规范或跨镜追踪时按需读取。13 个字段是扩展交付结构，不替代 `SKILL.md` 的剧情分析、角色注册、镜头取舍、路线规划和详细分镜图顺序；镜头执行状态仍须使用 `USE / REFERENCE-ONLY / SKIP`，人物仍须绑定永久 `CHAR-ID` 与独立角色板。
> 冲突边界：原文案例的镜号、剧情、时长、对白速度、BGM、平台参数和提示词只作示例。最终镜号应连续且唯一，插入式编号只用于规划与版本追踪；对白预算以 `dialogue-timing.md` 为准，默认无 BGM，单次生成遵守当前 4–15 秒平台合同，运镜路线遵守 `CAM / ACT / GAZE / FOCUS / LIGHT / READ` 标注合同。

## 文档导航

- 一、字段总览
- 二、字段详解
- 三、完整分镜表示例
- 四、三阶段注释法
- 五、AI 分镜智能体使用方式

---

> 用于AI分镜智能体的核心数据规范
> 涵盖13个核心字段：镜号 · SB_ID · Beat_ID · 进度轴 · Shot_T · 镜头功能 · 景别·机位角度 · 运镜 · 光影·C-Look·焦点 · V轨 · A轨 · 生成Prompt · 状态变化

---

## 一、字段总览

| 序号 | 字段 | 英文标识 | 功能 |
|---|---|---|---|
| 1 | **镜号** | Shot_ID | 全片唯一标识，用于追踪和版本控制 |
| 2 | **SB_ID** | Story_Block_ID | 分镜块ID，用于大块拆分 |
| 3 | **Beat_ID** | Beat_ID | 叙事节拍ID，关联剧本结构 |
| 4 | **进度轴** | Timeline | 在全集中的时间位置 |
| 5 | **Shot_T** | Shot_Duration | 单镜时长，精确到0.1s |
| 6 | **镜头功能** | Shot_Function | 这个镜头在叙事中扮演的角色 |
| 7 | **景别·机位角度** | Size_Angle | 景别 + 摄影角度 + 机位侧 |
| 8 | **运镜** | Camera_Movement | 运镜类型 + 速度 + 方向 |
| 9 | **光影·C-Look·焦点** | Light_Color_Focus | 光线/色调/景深三位一体 |
| 10 | **V轨** | Video_Track | 画面内容描述 |
| 11 | **A轨** | Audio_Track | 台词 + 音效 + 音乐 |
| 12 | **生成Prompt** | AI_Prompt | 直接可用的AI视频提示词 |
| 13 | **状态变化** | State_Change | 本镜结束后角色的状态变化 |

---

## 二、字段详解

### 2.1 镜号（Shot_ID）

**格式**：`S[序号]` 或 `[Block_ID]_[序号]`

**规则**：
- 全集顺序编号：S01, S02, S03 ... S68
- 分块内编号：SB01a_01, SB01a_02 ... SB01a_09, SB01b_01 ...
- 插入镜：S12.5（在12和13之间插入）

**AI用途**：版本追踪、重生成目标定位

**示例**：
```
S01 → 全集第一镜
SB02a_03 → SB02a块第三镜
S45.5 → 在45和46之间插入的补拍镜
```

---

### 2.2 SB_ID（Story_Block_ID）

**格式**：`SB[场景号][场景段]`

**规则**：
- SB01a = 第一场前半段
- SB01b = 第一场后半段
- SB02a = 第二场前半段
- 以此类推（a/b/c/d/e/f）

**参考来源**：《炎龙新娘EP01》文档的标准分块法

**AI用途**：分块递进生成，末态快照继承

**全集分块示例**（基于《炎龙新娘》EP01的132.5s标准）：
```
SB01a (20.0s) → SB01b (20.0s) → SB02a (16.5s) → SB02b (19.5s) →
SB02c (18.5s) → SB02d (16.5s) → SB02e (26.0s) → SB02f (14.0s)
```

---

### 2.3 Beat_ID（叙事节拍ID）

**格式**：`B[序号]`

**规则**：
- B01-B14：全集被拆分为14个核心叙事Beat（基于《炎龙新娘》标准）
- 每个Beat包含1-3个镜头
- Beat是最小的叙事单元

**14 Beat 标准结构**：

| Beat_ID | 名称 | 情绪 | 功能 | 包含镜数 |
|---|---|---|---|---|
| B01 | 逃亡拉锯 | 极度恐慌 ↗ | 开场钩子，建立危机 | 3-4 |
| B02 | 火舌截断 | 恐慌升级 ↗ | 展示敌人力量 | 2-3 |
| B03 | 体力崩溃 | 绝望升级 ↗ | 展示主角极限 | 2-3 |
| B04 | 恶龙降临 | 恐惧顶点 ↗↗ | 高潮反转 | 2-3 |
| B05 | 掐喉压制 | 绝对绝望 ↗↗ | 力量对比确认 | 2-3 |
| B06 | 地牢冰封 | 痛苦沉降 ↘ | 场景转换，新威胁 | 2-3 |
| B07 | 割脉吸血 | 生理战栗 | 曝露核心设定（蓝血） | 2-3 |
| B08 | 耳光重击 | 精神摧毁 ↗ | 尊严剥夺 | 2-3 |
| B09 | 母亲登场 | 阶级威压 | 新权力位引入 | 2-3 |
| B10 | 代嫁宣判 | 惊恐升级 ↗↗ | 致命命运转折 | 3-4 |
| B11 | 撕衣羞辱 | 尊严崩塌 | 肉体+精神双重剥夺 | 2-3 |
| B12 | 吸血恐吓 | 恐惧加码 ↗↗↗ | 渲染世仇恐怖 | 3-4 |
| B13 | 揪发凌虐 | 亲情粉碎 | 最终精神摧毁 | 3-4 |
| B14 | 强灌紫药 | 死寂定格 ● | Cliffhanger死钩 | 4-5 |

**AI用途**：检测叙事节奏是否合理，情绪曲线是否完整

---

### 2.4 进度轴（Timeline）

**格式**：`[分:秒.帧] → [分:秒.帧]` 或 `秒.帧`

**规则**：
- 以秒为单位，精确到0.1s（帧近似于24fps的0.04s）
- 记录本镜在全集中的起始时间和结束时间
- 用于跨镜时间连续性检查

**示例**：
```
00:00.0 → 00:02.5    (2.5s, 全集第1镜)
00:02.5 → 00:05.0    (2.5s, 全集第2镜)
01:52.5 → 02:00.0    (7.5s, 包含大段台词)
02:12.5 → 02:12.5    (0.0s → 转场标记)
```

**累计时间校验**：
```
∑(所有Shot_T) = 全集总时长（应在120-180s标准区间内）
单块累计 = 块目标时长（误差 ±0.5s）
```

---

### 2.5 Shot_T（镜头时长）

**格式**：`[数值]s`（精确到0.1s）

**标准时长参照表**：

| 场景类型 | 标准时长 | 理由 |
|---|---|---|
| 全景建制（Scene-First） | 3.0-5.0s | 需要足够时间看清空间 |
| 中景对话 | 2.0-3.5s | 信息量适中 |
| 特写/微表情 | 1.5-2.5s | 短而有力 |
| 大特写（ECU生理） | 1.0-2.0s | 冲击力强 |
| 动作快切 | 0.5-1.5s | 快节奏视觉冲击 |
| 受控快切包内 | 0.5-1.0s | 极高密度 |
| 情绪停顿（尾气口） | 0.5-1.5s | 留白让情绪沉降 |
| 台词段（密集） | 3.0-6.0s | 需要覆盖台词时长 |
| 集尾Cliffhanger定格 | 3.0-6.0s | 死钩停留 |

**时长匹配规则**：
```
台词需求时长 ≤ 分配的Shot_T总和
台词需求 ≈ 词数 × 语速系数
  中文：3-4字/秒 → 0.25-0.33s/字
  英文：0.25-0.30s/词
尾气口：0.5-1.5s（台词结束后的情绪呼吸空间）
```

---

### 2.6 镜头功能（Shot_Function）

**镜头的叙事角色分类**：

| 功能ID | 名称 | 英文 | 用途 | 典型时长 |
|---|---|---|---|---|
| F01 | **空间建置** | Establishing | 确立环境/空间/时代 | 3-5s |
| F02 | **权力展示** | Power_Display | 展示力量/地位/威胁 | 2-4s |
| F03 | **主体引入** | Subject_Intro | 第一次展示角色/物体 | 2-4s |
| F04 | **动作展示** | Action_Show | 展示角色的动作/运动 | 1-3s |
| F05 | **生理受击** | Physical_Impact | 展示被攻击/受伤/痛苦 | 1-2s |
| F06 | **情绪反应** | Emotional_Reaction | 展示面部的情绪变化 | 2-3s |
| F07 | **信息揭示** | Info_Reveal | 展示新信息/关键证据 | 2-4s |
| F08 | **权力反转** | Power_Shift | 权力关系的转变 | 2-3s |
| F09 | **道具强调** | Prop_Focus | 强调关键道具/细节 | 1-2s |
| F10 | **视线连接** | Eye_Line_Match | 视线-对象的交替 | 1-2s |
| F11 | **悬念建立** | Suspense_Build | 展示未知/恐怖/危机 | 2-4s |
| F12 | **主体反应** | Subject_Reaction | 对他人动作的反应 | 1.5-3s |
| F13 | **转场连接** | Transition | 场景/时间切换 | 1-2s |
| F14 | **集尾定格** | Cliffhanger | 全集的最终画面 | 3-6s |

**AI用途**：确保每一镜都有明确的叙事目的，消除冗余镜头

---

### 2.7 景别·机位角度（Size_Angle）

#### 2.7.1 景别（Shot Size）

| 代码 | 名称 | 英文 | 截断位置 | 心理距离 |
|---|---|---|---|---|
| EWS | 大远景 | Extreme Wide Shot | 人物极小 | 极远·客观·史诗 |
| WS | 远景 | Wide Shot | 人物全身 | 远·环境+人 |
| FS | 全景 | Full Shot | 头到脚 | 中远·完整肢体 |
| AS | 中全景 | American Shot | 膝盖以上 | 中·动作+表情 |
| MS | 中景 | Medium Shot | 腰部以上 | 适中·对话+手势 |
| MCU | 中近景 | Medium Close-Up | 胸部以上 | 近·表情+少量环境 |
| CU | 特写 | Close-Up | 面部 | 很近·情绪/细节 |
| ECU | 大特写 | Extreme Close-Up | 局部（眼/唇/手） | 极近·极致战栗 |
| INS | 插入镜 | Insert Shot | 物体局部 | 聚焦·关键道具 |

#### 2.7.2 机位角度（Camera Angle）

| 代码 | 名称 | 英文 | 情绪 | 权力关系 |
|---|---|---|---|---|
| EL | 平视 | Eye Level | 中立·客观 | 平等 |
| LA | 低角度 | Low Angle | 压迫·力量 | 仰视=强者 |
| HA | 高角度 | High Angle | 脆弱·渺小 | 俯视=弱者 |
| BE | 俯视 | Bird's Eye | 上帝·命运 | 全知·掌管 |
| DA | 荷兰角 | Dutch Angle | 不安·扭曲 | 精神错乱 |
| POV | 主观视角 | Point of View | 代入·临场 | 角色所见 |
| OTS | 过肩 | Over Shoulder | 连接·对话 | 互动观察 |

#### 2.7.3 机位侧（Camera Side）

| 代码 | 名称 | 用途 |
|---|---|---|
| A侧 | 轴线外侧 | 石林/开放空间 |
| B侧 | 轴线内侧 | 对话内反拍 |
| C侧 | 正面中位 | 祭坛/三角形构图 |

**AI用途**：景别+角度+机位侧 → 完整描述摄影机位置

---

### 2.8 运镜（Camera Movement）

#### 2.8.1 运镜类型

| 代码 | 名称 | 英文 | 叙事功能 |
|---|---|---|---|
| ST | 固定 | Static | 专注/压迫/仪式 |
| PN | 横摇 | Pan | 揭示/跟随 |
| TL | 纵摇 | Tilt | 垂直权力/发现 |
| WP | 甩镜 | Whip Pan | 快速转场/能量 |
| PI | 推镜 | Push In / Dolly In | 靠近/紧张/内心 |
| PO | 拉镜 | Pull Out / Dolly Out | 远离/孤立/揭示 |
| TR | 跟拍 | Tracking | 跟随/沉浸 |
| AR | 弧线 | Arc / Orbit | 环绕/审视 |
| CR | 升降 | Crane / Boom | 高度权力/宏大 |
| HH | 手持 | Handheld | 纪实/混乱/真实 |
| DZ | 滑动变焦 | Dolly Zoom | 眩晕/内心冲突 |
| ZI | 变焦推 | Zoom In | 强行关注/不安 |
| ZO | 变焦拉 | Zoom Out | 揭示环境 |

#### 2.8.2 速度修饰

| 速度 | 英文 | 适合场景 |
|---|---|---|
| 极慢 | Extremely Slow / Creeping | 悬念、不安 |
| 慢 | Slow / Gradual | 情绪积累 |
| 适中 | Medium / Natural | 标准叙事 |
| 快 | Fast / Rapid | 动作、紧张 |
| 极快 | Extremely Fast / Aggressive | 恐慌、打斗 |

#### 2.8.3 AI提示词格式

```
Camera: [movement_type], [speed], [direction] (optional)
稳定：tripod/gimbal/handheld
```

---

### 2.9 光影·C-Look·焦点（Light_Color_Focus）

#### 2.9.1 光线（Lighting）

**光位**：
```
Key: 45°L/R（主光方向）
Fill: 对侧/补光强度
Rim: 有/无/强度
```

**光比**：
| 光比 | 效果 | 提示词 |
|---|---|---|
| 1:1 | 平光柔和 | `soft flat lighting` |
| 2:1 | 自然立体 | `natural lighting` |
| 4:1 | 戏剧 | `dramatic lighting` |
| 8:1 | 强反差 | `high contrast, deep shadows` |
| 16:1 | 极端 | `film noir, extreme low key` |

**光线风格**：
```
Rembrandt → 伦勃朗光（面部三角光）
Split → 侧光（半面亮半面暗）
Rim → 轮廓光
Underlighting → 底光（恐怖感）
Volumetric → 体积光（丁达尔效应）
God Rays → 上帝光柱
```

#### 2.9.2 C-Look（色彩脚本 Color Look）

**整场调色方案**：
```
SC01：deep orange + charcoal black（熔岩红+焦黑）
SC02：icy blue + shadow black（冰极青蓝+阴影深黑）
```

**单镜调色**：
```yaml
color_palette: ["icy_blue", "deep_purple"]  # 主色调1+主色调2
contrast: high                              # 对比度
saturation: desaturated                      # 饱和度
temperature: cold                            # 色温
```

#### 2.9.3 焦点（Focus）

| 类型 | 效果 | 提示词 |
|---|---|---|
| Shallow DOF | 浅景深，背景虚化 | `shallow depth of field` |
| Deep Focus | 深焦，全清晰 | `deep focus` |
| Rack Focus | 拉焦，焦点切换 | `rack focus from [A] to [B]` |
| Soft Focus | 柔焦，梦境感 | `soft focus, dreamy` |
| Selective Focus | 选择焦点 | `selective focus on [subject]` |

**AI提示词格式**：
```
Lighting: [光位], [光比], [风格]
Color: [主色调], [对比度], [饱和度], [色温]
Focus: [景深类型], [焦点位置]
```

---

### 2.10 V轨（Video Track / 画面内容描述）

**V轨 = 镜头里"看到"什么**

**标准描述格式**：
```
[主体] [动作描述] [方向] [状态]
环境：[空间描述]
构图：[主体位置] + [其他元素位置]
```

**详细程度分级**：

| 级别 | 描述 | 适用 |
|---|---|---|
| L1: 简略 | "奈雅在逃跑" | 概念草图 |
| L2: 标准 | "奈雅踉跄穿过焦黑乱石，白裙被磨破" | 分镜表 |
| L3: 详细 | "奈雅从画左向右踉跄穿过焦黑乱石缝，左手扶石，右手垂落，白裙袖口撕裂，呼吸急促" | AI生成 |

**V轨要点**：
1. 角色位置（画左/画右/画中 + X/Y/Z轴）
2. 动作（动词+对象+方向）
3. 状态（情绪+生理+服装损伤）
4. 环境（空间特征+氛围）
5. 画面中的其他元素

---

### 2.11 A轨（Audio Track / 声音轨道）

**A轨 = 镜头里"听到"什么**

**三层结构**：

| 层 | 名称 | 内容 | 格式 |
|---|---|---|---|
| A1 | **台词** | 对白/旁白/独白 | `[角色]: "[台词内容]"  [时长]` |
| A2 | **音效** | 环境音/动作音/拟音 | `SFX: [描述]  [强度]` |
| A3 | **音乐** | 配乐/氛围/节奏 | `MUS: [风格] → [情绪]  [节奏]` |

**台词格式**（音画双账本用）：
```
L01: (旁白OS) "在炎龙族的领地上..."  6.5s
L02: (同期喘息) "...哈...哈..."   3.0s
L03: (龙鸣) GROWL + "逃不了的"  4.0s
L04: (锁喉威胁) "你以为你能去哪？"  7.5s
```

**A轨与V轨的时间匹配**：
```yaml
# L01 台词 6.5s，由以下镜头共同承载
Shot04: 2.5s (画面A) + L01前段
Shot05: 2.5s (画面B) + L01中段
Shot06: 2.5s (画面C) + L01后段
总容器: 7.5s > 6.5s需求 ✅ (预留0.5s尾气口)
```

**音效标签**：
```
SFX: 金属链条在冰面拖拽的刺耳刮擦声
SFX: 布料纤维撕裂声 (高锐度)
SFX: 喉咙吞咽的沉重咕噜声
SFX: 厚重的金属牢门轰鸣开启
MUS: 生理级低频压音 (持续)
MUS: 抽真空静音 → 仅留吞咽声
```

---

### 2.12 生成Prompt（AI_Prompt — AI可用的提示词）

**标准格式**（以Seedance 2.0为默认）：
```
[Shot Size], [Angle], [Camera Movement]
Subject: [Video Track content]
Cinematics: [Visual Approach]
Lighting: [Light type], [Ratio], [Style]
Color: [Palette]
Audio: [Dialogue] / [SFX]

Aspect: [Ratio] | FPS: [fps] | Duration: [seconds]
```

**完整示例**（从《炎龙新娘》SB02f转换）：
```
Shot 64 | SB02f_01 | 2.5s

Prompt:
Extreme close-up, eye level, static shot
Subject: Rough stone bowl filled with thick purple liquid, 
purple vapor rising from surface, maid's hands holding bowl edges
Cinematics: 幽闭凌虐流, claustrophobic, suffocating
Lighting: Low key, cold blue key light from upper left, 8:1 ratio
Color: icy blue background, deep purple liquid vapor contrast
Focus: Selective on bowl surface, shallow DOF, bokeh background
Audio: SFX - heavy breathing, liquid bubbling

Aspect: 9:16 | FPS: 24 | Duration: 2.5s
```

**多引擎适配标签**：
```
# Seedance 格式（主引擎）
Camera: [movement] Duration: [s]
Subject: [V轨内容]
渲染: [风格]

# Runway Gen-4 格式
[动作描述], [运镜], [光线], [色彩], [风格] — 完整句子

# Kling 3.0 格式
[镜头景别]，[运镜]，[主体动作]，[环境]，[光线]，[色调]
```

---

### 2.13 状态变化（State_Change）

**功能**：记录每个镜头结束后角色的状态变化，用于连续性检查

**格式**：
```yaml
# 当前末态
奈雅:
  position: "画左地表, 侧趴"
  status: "左脸红肿, 嘴角紫药水+蓝血"
  emotion: "彻底绝望, 眼神空洞"
  clothing: "白裙被撕碎"
  
莉拉:
  position: "画右中景, 直立"
  status: "龙角完全隐去, 金火收敛"
  emotion: "满足的狞笑"
  
索菲亚:
  position: "画右远景, 大门处"
  status: "右手执权杖顿地"
  emotion: "冷酷威严"
```

**状态变化追踪**：
```
Shot前 → 变化 → Shot后
奈雅(跪缚祭坛) → 被放血后意识涣散 → 奈雅(头部垂落, 蓝血滴落)
```

**AI用途**：防止角色位置/状态/情绪在镜头间跳变

---

## 三、完整分镜表示例

基于《炎龙新娘》SB02f（强灌紫药Cliffhanger块）的完整分镜表：

| 镜号 | SB_ID | Beat_ID | 进度轴 | Shot_T | 镜头功能 | 景别·机位·角度 | 运镜 | 光影·C-Look·焦点 | V轨 | A轨 | 生成Prompt | 状态变化 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| S64 | SB02f | B14 | 01:58.5→02:01.0 | 2.5s | F09(道具强调) | ECU·EL·C侧 | ST | Low Key·冰蓝+深紫·浅景深 | 粗糙石碗特写, 深紫粘稠药液翻滚淡紫烟雾, 女仆双手持碗边缘 | L21前段:"防止乱喊乱叫"(V.O.) | `ECU, eye level, static... Rough stone bowl with thick purple liquid...` | 道具出场 |
| S65 | SB02f | B14 | 02:01.0→02:03.5 | 2.5s | F08(权力展示) | CU·LA·C侧 | ST(慢推) | 伦勃朗光·冰蓝·深焦 | 索菲亚正脸, 冷酷开口下令, 权杖顿地声 | L21中段:"惹他心烦" | `CU, low angle... Sophya giving order...` | 索菲亚下令 |
| S66 | SB02f | B14 | 02:03.5→02:05.5 | 2.0s | F12(主体反应) | CU·HA·C侧 | ST | 侧光·冰蓝+紫·浅景深 | 奈雅被迫抬头, 紫药碗靠近嘴部, 恐惧的眼睛 | SFX: 药水咕噜声 | `CU, high angle... Purple bowl approaching mouth...` | 奈雅恐惧 |
| S67 | SB02f | B14 | 02:05.5→02:07.0 | 1.5s | F05(生理受击) | ECU·EL·C侧 | ST(硬锁) | 顶光·深紫+冰蓝·极浅 | 紫色液体从碗沿倾泻, 溢过干裂嘴唇流淌 | SFX: 液体冲击嘴唇 | `ECU macro... Purple liquid overflowing from bowl...` | 灌药开始 |
| S68 | SB02f | B14 | 02:07.0→02:09.5 | 2.5s | F05(生理受击) | ECU·EL·C侧 | ST(硬锁) | 微光·紫·极浅 | 喉结V字剧烈上下耸动, 紫液顺锁骨流下 | SFX: 沉重吞咽声 | `ECU macro... Throat convulsing, liquid streaming...` | 被吞咽 |
| S69 | SB02f | B14 | 02:09.5→02:12.5 | 3.0s | F14(集尾定格) | ECU·EL·C侧 | ST(零运镜) | 抽真空·瞳孔紫雾·极浅 | 单只失焦瞳孔放大, 紫色烟雾在眼球表面反射, 泪水滑落 | MUS: 完全的静默 | `ECU extreme... Single dilated eye, purple vapor reflection...` | 终极绝望 |

---

## 四、三阶段注释法

在《炎龙新娘》中使用的三阶段注释法可以作为分镜表补充：

### 4.1 第一层：镜头前（Setup）
```
🎬 [镜头前状态]
奈雅: 侧趴在地表, 白裙破碎, 左脸红肿
索菲亚: 画右远景高位, 权杖顿地
轴线: Axis_SC02_02 (C侧)
```

### 4.2 第二层：镜头中（Action）
```
🎥 [拍摄内容]
女仆B端药碗蹲跪 → 捏开奈雅下颌 → 紫色药液倾泻而入
奈雅喉头被迫吞咽 → 液体溢出嘴角
```

### 4.3 第三层：镜头后（Result）
```
📌 [镜头后状态]
奈雅: 嘴角紫药水, 眼神失焦, 喉头仍在痉挛
索菲亚: 位置不变, 完成政治资产封口
轴线: Axis_SC02_02 维持不变
下一镜强制: 瞳孔大特写硬锁
```

---

## 五、AI分镜智能体使用此规范的方式

```
输入：剧本
    ↓
智能体解析 → 确定Beat_ID分布 → 确定SB_ID分块
    ↓
每块逐镜生成：
    1. 确定 Shot_ID（顺序编号）
    2. 确定 镜头功能（从14种选择）
    3. 确定 景别·角度·机位侧（从映射矩阵）
    4. 确定 运镜（从映射矩阵）
    5. 确定 时长（台词时长+尾气口）
    6. 填写 V轨（画面描述）
    7. 填写 A轨（台词+音效+音乐）
    8. 设定 光影·C-Look·焦点
    9. 检查 状态变化（连续性）
    10. 生成 Prompt（Seedance为主）
    11. 更新时间轴
    ↓
输出：完整分镜大表（13字段全填）
```

---

*本文档作为AI分镜智能体的核心数据规范参考*
*基于《炎龙新娘EP01》的工业化分镜标准 + 电影制作行业标准*

