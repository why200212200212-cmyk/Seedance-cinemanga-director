# AI视频运镜控制方法大全 — 主流工具与提示词工程

> 仓库接入说明：本文件中的平台版本、时长、分辨率、功能和效果评级可能随时间变化，只作概念参考。执行前必须以用户提供的信息或当前官方能力为准；不得据此虚构 Seedance 2.0 能力。

## 文档导航

- 一、运镜控制总览
- 二、主流工具运镜能力
- 三、运镜提示词工程
- 四、生成约束
- 五、竖屏运镜
- 六、三步验证法
- 七、运镜决策流程

> 目标：让AI导演智能体知道"怎么让AI实现想要的运镜"

---

## 一、AI视频生成运镜控制总览

目前主流AI视频生成工具的运镜控制能力分为三个等级：

| 等级 | 描述 | 代表工具 | 适合场景 |
|---|---|---|---|
| L1 - 文本描述 | 用自然语言在Prompt中描述运镜 | Runway Gen-3/4, Pika, Kling, Sora, Hailuo | 概念验证、快速原型 |
| L2 - 参数控制 | 提供专门的运镜参数滑块/选项 | Pika Camera Control, Runway Advanced, Kling Pro | 精确控制、量产 |
| L3 - 输入驱动 | 输入参考视频/图像序列/3D场景 | Runway Act-One, Kling Motion Brush, Sora Composer | 专业电影制作、高一致性 |

---

## 二、六大主流AI视频工具运镜能力详解

### 2.1 OpenAI Sora

**基础信息**：OpenAI的文生视频模型，支持最长60秒/1080p视频

**运镜控制方式**：
- **文本描述法**：在Prompt中描述运镜
  - `The camera slowly pushes in on the girl's face as realization dawns`
  - `A dramatic crane shot rises above the castle walls revealing the army below`
  - `Handheld camera follows the soldier through the trench, shaky, chaotic`

**Sora特有功能**：
- 长镜头连续性（极佳的一致性）
- 物理世界理解（光影、反射、重力）
- "重混"能力（Re-mix）：修改已有视频的某个方面
- 故事板模式（Storyboard）：逐帧编辑关键帧

**Sora提示词模板**：
```
[Shot Type], [Camera Movement], [Subject], [Action], [Environment], [Lighting], [Color Grade], [Mood]
```

**示例**：
```
Close-up, slow push-in, a young woman's face, tears streaming down, dark dungeon, single shaft of cold blue light from above, claustrophobic, desperate
```

---

### 2.2 Runway Gen-3 / Gen-4

**基础信息**：Runway Research的视频生成模型，支持多种控制模式

**运镜控制方式**：

#### a) 文本描述法
```
cinematic shot, dolly in, low angle, dramatic lighting, 35mm lens
```

#### b) Advanced Camera Controls（高级运镜控制）
Runway Gen-3/4的 Advanced Mode 提供专业的摄影机参数：

| 参数 | 可选值 | 效果 |
|---|---|---|
| Camera Motion | Static / Pan Left/Right / Tilt Up/Down / Dolly In/Out / Tracking / Crane Up/Down | 基本运镜方向 |
| Zoom | None / In / Out | 变焦推拉 |
| Speed | Slow / Medium / Fast | 运动速度 |
| Rotation | None / Left / Right | 横轴旋转 |

#### c) Act-One
- 用参考视频驱动角色的表情和动作
- 人物表演运镜控制的基础技术

---

### 2.3 Pika 2.0 / Pika 3.0

**基础信息**：以易用性著称的AI视频平台

**运镜控制方式**：

#### a) Camera Control（核心参数）
Pika的参数面板是L2控制中最成熟的：

| 参数 | 范围 | 效果 |
|---|---|---|
| Pan | Left / Right / None | 横摇 |
| Tilt | Up / Down / None | 纵摇 |
| Zoom | In / Out / None | 变焦 |
| Rotate | CW / CCW / None | 旋转 |

#### b) Motion Score（运动强度）
- 1-10级：控制整体运动强度
- 低分（1-3）：静态、克制的镜头
- 中分（4-7）：自然、平衡的运动
- 高分（8-10）：极强烈的动作

#### c) PikaFrame / Scene Ingredients
- 上传参考图作为构图锚定
- 用Image Prompt控制每一帧的视觉风格

**Pika提示词模板**：
```
[Subject], [Environment], Camera: [Pan/Tilt/Zoom], Motion: [Low/Medium/High], [Style Reference]
```

---

### 2.4 可灵AI（Kling AI）

**基础信息**：快手旗下AI视频生成模型，对中文语境的运镜理解极好

**运镜控制方式**：

#### a) 文本描述
```
镜头从女主的特写缓缓向后拉，露出整个阴暗的地牢环境
摄影机围绕祭坛做180度弧线运动
```

#### b) 高级模式参数
- 相机运镜：左摇/右摇/上摇/下摇/推/拉/左移/右移/上升/下降
- 运动速度：慢/中/快
- 构图参考：上传参考图

#### c) 图生视频（Image to Video）
- 上传静态分镜图，让AI按照设定运镜生成动态视频
- 可实现极高的构图一致性

**Kling提示词模板**：
```
[主视觉描述]，摄影机[运镜]，[氛围]，[光线]，[画幅比例]
```

---

### 2.5 Vidu / 海螺AI（MiniMax）

**基础信息**：国内的AI视频生成工具，参考功能优异

**运镜控制方式**：
- **参考视频驱动**：上传参考视频控制运镜轨迹
- **文本描述**：中文自然语言描述
- **图转视频**：保持参考图构图

**海螺AI特点**：
- 极其精准的中文Prompt理解
- 高一致性的角色保持
- 支持长视频生成

---

### 2.6 生数科技（Vidu）

**基础信息**：国内AI视频工具，理解中文Prompt

**运镜控制方式**：
- **文字转视频**：文本描述运镜
- **图转视频**：上传参考图
- **分段控制（待发布）**：不同Segment设置不同运镜

---

## 三、AI运镜提示词工程（核心技能）

### 3.1 提示词语法结构

一条有效的AI运镜提示词应包含以下要素：

```
[镜头景别] + [运镜方式] + [被摄主体] + [动作描述] + [环境/空间] + [光线氛围] + [色调风格] + [帧率/画质]
```

**专业示例**：
```
Medium close-up, slow push-in on the kneeling princess, her white dress torn and blood-stained, stone dungeon covered in frost, single beam of cold blue light, cinematic, volumetric fog, 4K, 24fps
```

### 3.2 运镜关键词汇库（English / Chinese）

#### 景别关键词
| English | 中文 | AI模型理解度 |
|---|---|---|
| extreme wide shot | 大远景/超大景 | ★★★★ |
| wide shot / full shot | 全景/远景 | ★★★★★ |
| medium shot / waist shot | 中景 | ★★★★★ |
| medium close-up | 中近景/胸景 | ★★★★★ |
| close-up | 特写 | ★★★★★ |
| extreme close-up | 大特写/微距 | ★★★★ |
| insert shot | 插入镜头/细节 | ★★★ |

#### 运镜关键词
| English | 中文 | AI模型理解度 |
|---|---|---|
| static / locked down | 固定镜头 | ★★★★★ |
| pan left / pan right | 左摇/右摇 | ★★★★★ |
| tilt up / tilt down | 上摇/下摇 | ★★★★ |
| whip pan / swish pan | 甩镜 | ★★★ |
| push in / dolly in | 推镜 | ★★★★★ |
| pull out / dolly out | 拉镜 | ★★★★★ |
| dolly zoom / vertigo | 滑动变焦 | ★★★ |
| tracking / follow | 跟拍 | ★★★★★ |
| crane shot | 升降镜头 | ★★★★ |
| arc shot / orbiting | 环绕/弧线 | ★★★★ |
| handheld / shaky | 手持/晃动 | ★★★★ |
| POV | 主观视角 | ★★★★ |
| aerial / drone | 航拍 | ★★★★ |
| dutch angle / canted | 荷兰角/倾斜 | ★★★★ |

### 3.3 运镜链式提示（Chain Prompting）

对于复杂的多段运镜，使用**链式提示**——每一段视频的Prompt以上一段的末帧为起点：

```
Block 1 Prompt: 
Extreme wide shot of a volcanic wasteland, orange sky, slow pan left to right

Block 1 Output → Block 2 takes its last frame:

Block 2 Prompt:
Push in towards a running figure in the distance, maintaining the same orange sky, tracking shot
```

### 3.4 节奏控制词汇

| 速度词汇 | 英文 | 适用 |
|---|---|---|
| 极慢 | extremely slow, creeping | 悬念、不安 |
| 慢 | slow, gradual | 情绪积累 |
| 适中 | medium pace, natural | 标准叙事 |
| 快 | fast, rapid | 动作 |
| 极快 | extremely fast, aggressive | 打斗、恐慌 |

---

## 四、AI视频生成中的运镜约束

### 4.1 AI运镜的物理限制

| 约束 | 原因 | 解决方案 |
|---|---|---|
| 透视跳跃 | AI不理解光学透视的连续性 | 控制Z轴变化幅度不要过大 |
| 背景扭曲 | 大范围移动时背景不稳定 | 限制运镜范围，优先使用平移而非推拉 |
| 角色漂移 | 角色在画面中位置不稳定 | 锁定角色在画面中的构图位 |
| 物体消失 | 运动到画外后重新出现的物体可能变形 | 确保所有关键物体始终保持在画内 |
| 反向运镜不一致 | 同一场景正反打出现空间矛盾 | 严格遵守180度轴线 |

### 4.2 AI提示词中的运镜精确度分级

| 级别 | 描述 | 适用场景 |
|---|---|---|
| **宽松** | `dynamic camera movement` | 概念预览、氛围测试 |
| **标准** | `camera slowly pushes in` | 一般叙事生成 |
| **精确** | `slow dolly in from medium shot to close-up over 3 seconds` | 分镜精确执行 |
| **专业** | `35mm lens, dolly in from waist level, rack focus from foreground chains to her face, 24fps, 180° shutter` | 电影级AI生成 |

### 4.3 专业级提示词示例

根据《炎龙新娘》文档中的分镜描述转化的AI提示词：

**SB01a-01（赤焰石林全景建制）**：
```
Extreme wide shot, establishing, thousand-meter lava waterfall in center frame,  
charred black rocks scattered, deep orange sky, volcanic ash, heat haze distorting air,  
cinematic, ARRI Alexa 65, Panavision anamorphic, 9:16 vertical, film grain
```

**SB01b-05（莉拉化人身掐喉）**：
```
Medium shot, low angle, Lila in human form with half-retracted dragon horns,  
red dress, right hand gripping Naya's throat, lifting her off ground,  
Naya's face congested with blood, fire ring around them,  
Dutch angle, intense, claustrophobic, golden fire energy in skin veins,  
dark orange and black color palette, deep shadows
```

**SB02a-01（冰地牢Scene-First）**：
```
Extreme close-up, frost-covered iron window bars, thick ice crystals,  
cold blue light, frost creeping on metal, chains scraping sound implied,  
J-Cut audio transition from previous scene,  
polar blue and deep black color palette, shallow depth of field
```

**SB02f-04（强灌紫药Cliffhanger）**：
```
Extreme close-up macro, purple viscous liquid pouring from stone bowl edge,  
overflowing cracked pale lips, trickling down chin to collarbone,  
deep purple with glowing vapor, cold blue background,  
zero camera movement, suffocating silence,  
trachea/Adam's apple convulsing in V-shape swallowing,  
single tear falling into purple puddle
```

---

## 五、竖屏（9:16）运镜特殊处理

### 5.1 竖屏构图差异
- 横向空间≈1/3横屏
- 垂直空间≈2倍横屏
- 传统"土地平线分配法"失效

### 5.2 竖屏运镜策略

| 横屏运镜 | 竖屏等价 | 调整说明 |
|---|---|---|
| Pan（横摇） | Tilt（纵摇） | 竖屏横向窄，纵摇更适合揭示垂直空间 |
| Tracking（横移） | Boom/Crane（升降） | 竖屏垂直方向才是主要运动轴 |
| Wide Shot（全景） | Medium Full Shot（中全景） | 竖屏的全景信息密度太低 |
| Dolly In（推） | 仍有效但加强Z轴 | 纵深比横向更适合竖屏 |

### 5.3 文档中的竖屏运镜设计
- 默认使用中长焦，"将人物从环境里剥离，强化微表情"
- "极度克制压缩人物横向生存空间，制造窒息感"
- 红龙火舌在竖屏下方形成火焰边界——利用垂直空间

---

## 六、AI运镜三步验证法

### Step 1：文本验证
在写Prompt之前，先用语言验证运镜是否合理：
> "推镜3秒从中景到特写，透视关系改变了吗？角色位置漂移了吗？"

### Step 2：分段测试
- 首镜先让AI生成静态图（确认构图和空间）
- 再用短Prompt测试运镜（确认运动效果）
- 最后生成完整视频

### Step 3：一致性核对
生成后检查：
- 角色位置是否符合连续快照的要求？
- 轴线是否被遵守（左右关系是否反转）？
- 道具是否保持一致的视觉特征？
- 时长是否匹配音画双账本的预期？

---

## 七、AI导演运镜决策流程图

```
输入：分镜表中对本镜的描述
    ↓
1. 确定景别（EWS/WS/MS/CU/ECU）
    ↓
2. 确定角度（Eye/Low/High/Dutch/POV）
    ↓
3. 确定运镜类型（Static/Pan/Tilt/Push/Pull/Track/Boom/Handheld）
    ↓
4. 确定运镜速度（Slow/Medium/Fast）
    ↓
5. 检查是否触发AI死穴（物理接触？）
   ├── 是 → 启用死穴规避方案（过程化分段 + 蒙太奇）  
   └── 否 → 直接使用标准提示词
    ↓
6. 生成完整Prompt（景别+运镜+主体+环境+光线+色调+参数）
    ↓
7. 音画时长匹配检查（台词时间 vs 镜头时间）
    ↓
输出：AI视频生成Prompt
```

---

*本文档作为AI导演智能体的运镜控制方法知识库*
