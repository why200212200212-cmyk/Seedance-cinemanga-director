# AI生成物理接触死穴规避体系（完整方案库）

> 仓库接入说明：本文件是高失败风险镜头的备选方案库，不代表所有模型或所有接触动作必然失败。先保留原剧情与动作结果，再按实际风险选择连续拍摄、拆拍、遮挡、反应镜头或声音替代。

## 文档导航

- 一、物理接触风险分类
- 二、蒙太奇替代原理
- 三至七、五类动作方案
- 八、检查清单
- 九、受控快切包

> 核心问题：当前AI视频模型在生成"多人精确物理接触"时必然出现画质崩坏。
> 解决方案：不是"让AI学会拍接触"，而是"用蒙太奇替代接触"。

---

## 一、AI物理接触死穴分类

### 1.1 四大死穴类型

| 类型 | 描述 | 难度 | 常见场景 |
|---|---|---|---|
| **手-脸接触** | 手掌拍脸、抚摸脸颊 | ★★★★★ | 耳光、爱抚 |
| **手-发接触** | 手指拉扯头发 | ★★★★★ | 揪发、梳头 |
| **手-衣接触** | 撕扯、脱衣物 | ★★★★ | 撕衣、换衣 |
| **手-嘴接触** | 喂食、灌药、捂嘴 | ★★★★★ | 灌药、封口 |

### 1.2 死穴产生原因
AI视频模型基于去噪扩散过程生成帧序列。当需要生成"手指精确压在脸颊皮肤上"时：
1. 模型必须同时生成手指的形态+脸颊的凹陷+两者之间的遮挡关系
2. 任何微小的不精确都会导致"手指穿透脸颊"或"手指漂浮在脸颊上方"
3. 跨帧时，手和脸的相对位置必须一致——这对扩散模型极其困难

---

## 二、核心规避原理：蒙太奇替代法

### 2.1 基本原则
```
不拍"接触的瞬间"
    → 拍"接触的前半程" + "接触的结果" + "接触的声音"
    = 观众的大脑自动补全了接触本身
```

### 2.2 三层结构
每一套死穴规避方案都包含三层：

```
L1 - 触发起始帧：接触动作的前半程（安全区内）
L2 - 冲击突变帧：AI最擅长生成的结果状态
L3 - 声音叙事层：音效承担物理冲击的叙事重量
```

---

## 三、方案一：掌掴耳光（Slap）

### 3.1 三拍过程法

| 拍数 | 内容 | 景别 | 时长 |
|---|---|---|---|
| 拍1：挥出 | 施暴者反手挥出，手掌在到达面部前定格/切出 | 中景-手腕特写 | 1.0s |
| 拍2：冲击 | 【冲击帧硬锁】受害者头部剧烈侧偏，蓝血/唾液飞溅 | ECU受击脸 | 0.5s |
| 拍3：反应 | 受害者面部缓慢转回，红肿掌印可见，眼泪滑落 | CU面部 | 1.5-2.0s |

**声音设计**：清脆尖锐的骨肉撞击声（A2级拟音）

**AI提示词模板**：
```
Shot 1 (Pre-impact):
Medium close-up, Lila's hand swinging toward camera, motion blur on hand, angry expression

Shot 2 (Impact - AI safe single frame):
Extreme close-up, Naya's head snapping sideways, blood droplets flying from mouth, freeze frame quality

Shot 3 (Reaction):
Close-up, Naya's cheek with red handprint, tears welling, slow turn back to camera
```

### 3.2 死穴规避说明
**不拍的内容**：手掌贴在脸颊上的画面
**拍的内容**：手掌在空中运动的轨迹 + 头部侧偏的结果 + 红肿掌印

---

## 四、方案二：撕碎衣物（Tearing Clothes）

### 4.1 四段硬锁法

| 段数 | 内容 | 景别 | 时长 |
|---|---|---|---|
| 段1：伸手 | 女仆俯身，手呈爪状伸入画面下半部分 | 中景接手腕特写 | 1.0s |
| 段2：纤维断裂 | 【微距硬锁】粗糙手指发力，布料纤维崩断的特写 | ECU指间布料 | 0.5s |
| 段3：碎布飞散 | 碎裂的沾血白布碎片在冰霜地表上滑过的微镜头 | ECU地面碎片 | 0.5s |
| 段4：受击落点 | 受害者双手抱胸蜷缩，衣料撕裂音效持续 | CU蜷缩 | 2.0s |

**声音设计**：刺耳的布料纤维撕裂声（全程覆盖段2-段4）

**AI提示词模板**：
```
Shot 1 (Approach):
Medium shot, maid B lunging forward, hand reaching toward Naya's dress, fingers curled

Shot 2 (Tearing - macro detail):
Extreme close-up macro, rough fingers grasping white fabric threads, fibers snapping, fabric stretching

Shot 3 (Debris):
Extreme close-up, torn blood-stained fabric piece sliding across frost-covered stone floor

Shot 4 (Aftermath):
Close-up, Naya curling into fetal position, arms wrapped around herself, torn dress hanging, shivering on cold stone
```

### 4.2 死穴规避说明
**不拍的内容**：手指与身体接触拉扯的画面
**拍的内容**：手切入镜头 + 特写布料断裂 + 碎布落在远处 + 蜷缩落点

---

## 五、方案三：揪扯头发（Hair Pulling）

### 5.1 三拍过程法

| 拍数 | 内容 | 景别 | 时长 |
|---|---|---|---|
| 拍1：探手 | 施暴者下蹲，手呈爪状恶狠狠向下探入 | 中景接爪状手 | 1.0s |
| 拍2：头皮变形 | 【冲击帧】受害者面部肌肉因暴力向上变形 | ECU面部变形 | 0.5s |
| 拍3：发丝特写 | 【微距特写】红色蔻丹指缝间勒紧的粗糙发丝 | ECU指间发丝 | 1.0s |

**声音设计**：发根撕裂的密集细碎声响（微拟音）+ 受害者的闷哼

**AI提示词模板**：
```
Shot 1 (Reach):
Medium shot, Lila crouching down, right hand with red nails reaching down aggressively toward camera bottom

Shot 2 (Impact - head pulled back):
Extreme close-up, Naya's face yanked upward, skin stretching around eyes, mouth open in silent scream, tears streaming sideways from upward force

Shot 3 (Hair detail):
Extreme close-up macro, red fingernails embedded in black hair strands, hair pulled taut, individual strands visible
```

### 5.2 死穴规避说明
**不拍的内容**：手指在发根处拉扯的穿透画面
**拍的内容**：手呈爪状 + 面部变形反应 + 指间发丝拉力线

---

## 六、方案四：强灌药水（Force-Feeding Liquid）

### 6.1 终极四段法（最复杂的死穴）

| 段数 | 内容 | 景别 | 时长 |
|---|---|---|---|
| 段1：端药 | 女仆端碗俯身，手呈虎口卡入镜头边缘 | 碗特写转手部 | 1.0s |
| 段2：液体倾泻 | 【微距硬锁】深粘稠紫色液体从碗沿倾斜拉出水线 | ECU液体线条 | 1.0s |
| 段3：吞咽过程 | 【喉部微镜头】液体溢过嘴唇、喉结V字骨被迫上下耸动 | ECU脖颈 | 2.0s |
| 段4：瞳孔死寂 | 【最终定格】单只失焦瞳孔，紫色烟雾在眼球表面反射 | ECU眼睛 | 3.0s |

**声音设计**：抽真空——静音 + 沉重吞咽声 + 液体在喉间的咕噜声

**AI提示词模板**：
```
Shot 1 (Approach with bowl):
Extreme close-up, rough stone bowl filled with thick purple liquid, purple vapor rising, maid's hands holding bowl on edges

Shot 2 (Pouring - macro):
Extreme close-up macro, viscous purple liquid overflowing from bowl edge, pouring over cracked pale lips, liquid stream in slow motion

Shot 3 (Swallowing - neck detail):
Extreme close-up macro, female throat, Adam's apple convulsing in V-shape, purple liquid running down neck to collarbone, wet skin texture

Shot 4 (Eye - final frame):
Extreme close-up extreme, single wide eye, pupil completely dilated, purple smoke reflection in cornea, tear forming at corner, completely still
```

### 6.2 死穴规避说明
**不拍的内容**：手指在口腔内部和嘴唇上的拉扯
**拍的内容**：液体流动线条 + 喉结的外部运动 + 瞳孔反应

---

## 七、方案五：掐喉（Choking）

| 拍数 | 内容 | 景别 | 时长 |
|---|---|---|---|
| 拍1：伸手 | 施暴者手呈掐握状伸入画面 | MS→CU | 1.0s |
| 拍2：冲击 | 面部充血通红+被提起的体态 | ECU面部 | 1.0s |
| 拍3：反应 | 挣扎的双手、蹬地的双脚 | CU局部 | 1.5s |
| 拍4：卸力 | 手松开后的喘息和瘫软 | MS全景 | 2.0s |

**AI提示词**：
```
Shot 1: Lila's hand reaching toward Naya's throat, fingers spread in choking grip position
Shot 2: Extreme close-up, Naya's face turning red, veins on neck bulging, gasping for air
Shot 3: Naya's hands weakly pulling at arm, feet scraping ground
Shot 4: Lila releases, Naya collapses to ground gasping, chest heaving
```

---

## 八、死穴规避检查清单

每一段需要物理接触的剧情都必须经过以下检查：

```
□ 1. 这段剧情是否有"多人精确物理接触"？
    如果是——
    □ a. 识别接触类型（手-脸/手-发/手-衣/手-嘴/掐喉）
    □ b. 选择对应的规避方案
    □ c. 是否需要升级为"受控快切包"模式？
    □ d. 声音设计是否已经覆盖了物理冲击的叙事重量？
    □ e. 生成的Prompt中是否拍的是"接触前后"而非"接触本身"？
```

---

## 九、受控快切包（Controlled Fast-Cut Package）

当一段剧情的物理接触密度极高时（如集尾强灌紫药），将所有死穴规避镜头打包成一个"受控快切包"，统一管理节奏：

### 9.1 文档中的三处快切包

| 位置 | 内容 | 性质 |
|---|---|---|
| SC01·B05 | 莉拉化人身截获女主 | 动作高潮 |
| SC02·B11 | 女仆暴蛮撕碎衣服 | 尊严剥夺 |
| SC02·B14 | 紫药强灌吞咽 | 集尾Cliffhanger |

### 9.2 快切包内部结构
每包4-5个微镜头，每个0.5-1.5s，总时长不超过5s。
```
触发(0.5s) → 过程1(0.5s) → 过程2(0.5s) → 结果(1.5s) → 音效落点
```

---

*本文档是AI导演智能体最核心的技术知识库——没有它，任何物理接触场景都会生成失败*
