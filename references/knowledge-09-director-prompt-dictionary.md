# AI导演提示词工程全参数字典

> 仓库接入说明：本文件是查询型词典，不是整段复制模板。只选能改变当前画面的必要参数；案例角色、题材风格、相机品牌、画幅与画质词不得默认注入。

## 文档导航

- 一、Prompt 结构
- 二、景别
- 三、运镜
- 四、角度
- 五、光线
- 六、颜色
- 七、设备与镜头
- 八、风格与质感
- 九、画幅与画质
- 十、案例体系解析
- 十一、题材示例
- 十二、输出格式

> 从景别到运镜、从光线到颜色、从风格到参数——AI导演必用的300+提示词参数

---

## 一、主Prompt结构模板

### 1.1 标准结构
```
[Shots] [Movement] of [Subject], [Action/Expression],
in [Environment], [Lighting], [Colors],
[Equipment/Lens], [Style], [Aspect Ratio], [Quality]
```

### 1.2 文档级完整模板
```
[景别 + 运镜] of [主体], [动作描述],
located in [空间环境],
[光线氛围] lighting, [主色调] and [辅色调] color palette,
shot on [摄影机] with [镜头] lens,
[风格声明] style, [情绪] atmosphere,
9:16 vertical format, 24fps, 4K cinematic quality
```

---

## 二、景别（Shot Size）完整参数集

| 中文 | English Prompt Keyword | 画面截断位置 | 信息重点 |
|---|---|---|---|
| 大远景 | extreme wide shot / EWS | 人物极小 | 环境/空间/史诗 |
| 远景 | wide shot / WS | 全身 | 动作+环境 |
| 全景 | full shot | 头到脚 | 完整肢体语言 |
| 中全景 | american shot / 3/4 shot | 小腿以上 | 牛仔/动作+表情 |
| 中景 | medium shot / MS | 腰部以上 | 对话+手势 |
| 中近景 | medium close-up / MCU | 胸部以上 | 表情+少量环境 |
| 特写 | close-up / CU | 面部 | 情绪/细节 |
| 大特写 | extreme close-up / ECU | 局部（眼/唇/手） | 极致战栗 |
| 插入镜头 | insert shot | 物体局部 | 关键道具 |

---

## 三、运镜（Camera Movement）完整参数集

| 英文 | 中文 | 效果 | 适用场景 |
|---|---|---|---|
| static / locked down | 固定/锁定 | 极致稳定 | 对话、审判、定格 |
| pan left / right | 左摇/右摇 | 水平旋转 | 揭示、跟随 |
| slow pan | 慢摇 | 观望/渐显 | 景观、悬念 |
| tilt up | 上摇 | 从低到高 | 权力、发现 |
| tilt down | 下摇 | 从高到低 | 脆弱、细节 |
| whip pan / swish pan | 甩镜 | 极速横摇 | 转场、活力 |
| push in / dolly in | 推镜 | 物理靠近 | 紧张、情感 |
| pull out / dolly out | 拉镜 | 物理远离 | 孤立、冷漠 |
| tracking / follow | 跟拍 | 平行跟随 | 追逐、探索 |
| truck left / right | 横移 | 平行移动 | 展示环境 |
| boom up / crane up | 上升 | 位置升高 | 宏大、解放 |
| boom down / crane down | 下降 | 位置降低 | 压迫、陷入 |
| arc / orbiting | 弧线/环绕 | 围绕转动 | 审视、能量 |
| handheld / shaky | 手持/晃动 | 不稳定 | 纪实、混乱 |
| dolly zoom / vertigo | 滑动变焦 | 透视扭曲 | 眩晕、内心 |
| zoom in | 变焦推 | 放大不移动 | 聚焦、强行关注 |
| zoom out | 变焦拉 | 缩小不移动 | 揭示环境 |
| POV | 主观视角 | 角色所见 | 代入、限知 |
| aerial / drone | 航拍 | 从上而下 | 史诗、全知 |
| rack focus | 拉焦 | 焦点切换 | 视线转移 |
| snap zoom | 急推 | 极速前推 | 震惊、揭示 |

### 运镜速度修饰语
```
extremely slow creeping camera movement
slow gradual camera push
medium-paced dolly movement
fast aggressive tracking shot
extremely rapid whip pan with motion blur
```

---

## 四、角度（Camera Angle）完整参数集

| 英文 | 中文 | 情绪 | 权力关系 |
|---|---|---|---|
| eye level | 平视 | 中立、客观 | 平等 |
| low angle | 低角度 | 强权、压迫 | 仰视=力量 |
| extreme low angle | 极限低角度 | 神性、恐怖 | 绝对统治 |
| high angle | 高角度 | 脆弱、渺小 | 俯视=无力 |
| bird's eye / top-down | 俯视/上帝 | 命运、全知 | 彻底支配 |
| dutch angle / canted | 荷兰角 | 不安、扭曲 | 精神错乱 |
| over-the-shoulder / OTS | 过肩 | 连接、空间 | 对话 |
| internal reverse | 内反拍 | 单人正面 | 独白/反应 |
| external reverse | 外反拍 | 过肩交替 | 互动的对话 |
| profile | 侧面 | 轮廓、仪式 | 旁观/思考 |

---

## 五、光线（Lighting）完整参数集

### 5.1 基础光线
```
cinematic lighting
natural lighting
soft diffused lighting
hard direct lighting
low key lighting
high key lighting
practical lighting
available light
```

### 5.2 特殊光效
```
Rembrandt lighting (伦勃朗光 - 面部三角光)
split lighting (侧光 - 半面亮半面暗)
rim light / backlight (轮廓光/背光)
underlighting (底光 - 恐怖感)
silhouette lighting (剪影)
volumetric lighting (体积光/丁达尔效应)
god rays (上帝光柱)
haze / atmosphere (雾化/大气)
lens flare (镜头光晕)
```

### 5.3 光比关键词
```
high contrast, deep shadows (高对比强阴影)
low contrast, soft shadows (低对比柔和)
4:1 lighting ratio (光比4:1)
dramatic lighting (戏剧光效)
```

---

## 六、颜色（Color）完整参数集

### 6.1 色调
```
warm color palette (暖色板)
cold color palette (冷色板)
teal and orange (青橙调 - 好莱坞标准)
monochromatic (单色调)
desaturated / muted (低饱和)
high saturation (高饱和)
```

### 6.2 色温
```
warm golden tones (暖金)
cool blue tones (冷蓝)
neutral daylight (中性日光)
sepia tone (复古棕)
```

### 6.3 风格化调色
```
cinematic color grade
film stock emulation (胶片模拟)
bleach bypass (漂白 - 高反差低饱和)
vintage / retro (复古)
dark and gritty (黑暗粗粝)
dreamy pastel (梦幻粉彩)
```

---

## 七、设备与镜头（Equipment & Lens）

| 设备 | 关键词 | 视觉特征 |
|---|---|---|
| ARRI Alexa 65 | ARRI Alexa 65 | 大画幅、电影质感 |
| Panavision变形宽银幕 | Panavision anamorphic | 水平光晕、椭圆散景 |
| 35mm | 35mm lens | 标准视野 |
| 50mm | 50mm lens | 自然视角 |
| 85mm | 85mm lens | 肖像感、压缩感 |
| 135mm | 135mm lens | 极远压缩 |
| 广角 | wide angle lens | 夸张透视、拉伸 |
| 鱼眼 | fisheye lens | 极端畸变 |
| shallow depth of field | 浅景深 | 主体清晰背景虚化 |
| deep focus | 深焦 | 全景清晰 |

---

## 八、风格与质感（Style & Texture）

### 8.1 风格
```
cinematic (电影级)
hyper-realistic (超写实)
photo-realistic (照片级真实)
epic fantasy (史诗奇幻)
documentary (纪录片风格)
film noir (黑色电影)
gothic (哥特)
fairytale (童话)
```

### 8.2 质感
```
film grain (胶片颗粒)
35mm film texture (35mm胶片质感)
8mm vintage film (8mm复古电影)
digital clean (数码干净)
sharp details (锐利细节)
textured (有纹理感)
```

### 8.3 高级风格描述（文档中的范例）
```
"Fincher precision meets Aster visceral horror"
"ultra-realistic, live-action quality, epic fantasy, physiological oppression"
"no CGI feel, no plastic special effects"
```

---

## 九、画幅与画质（Aspect Ratio & Quality）

| 参数 | 关键词 |
|---|---|
| 竖屏 | 9:16 vertical format, portrait aspect ratio |
| 横屏 | 16:9 widescreen |
| 宽银幕 | 2.35:1 cinemascope, anamorphic |
| 分辨率 | 4K, 8K, ultra HD |
| 帧率 | 24fps cinematic, 30fps standard, 60fps smooth |
| 快门 | 180 degree shutter, motion blur |

---

## 十、文档中的提示词体系解析

《炎龙新娘》文档虽然不直接写AI Prompt，但它每块包含的**前置全局块**本质上是AI提示词的前置参数声明：

### 10.1 前置全局块 = Prompt参数注入
```
风格核心：超写实·真人实景·史诗奇幻·生理级压迫 → hyper-realistic, live-action, epic fantasy
镜头胶片模拟：ARRI Alexa 65 + Panavision变形宽银幕 + 默认中长焦 → equipment declaration
色彩影调：焦黑怪石与深橘色天空的高饱和低调对比 → color palette declaration
```

### 10.2 运镜控制指令
```
视觉approach = 【奇观狩猎流】低位滑轨跟随配合火舌切断镜
→ low tracking shot + fire tongue cutting off path
```

### 10.3 每镜时长控制
```
Shot04(2.5s) + Shot05(2.5s) + Shot06(2.5s) = 承载L01台词7.5s
→ 精确时长分配到每一个AI生成视频片段
```

---

## 十一、女频暗黑玄幻题材的AI提示词风格指南

基于《炎龙新娘》文档分析的题材专用提示词：

### 11.1 场景提示词
**熔岩石林（SC01）**：
```
Volcanic wasteland, charred black rocks, thousand-meter lava waterfall in center,
deep orange sky, heat haze distorting air, suspended volcanic rocks in background,
deathly hot, suffocating atmosphere, cinematic wide angle
```

**冰封地牢（SC02）**：
```
Frozen stone dungeon, circular altar in center, thick frost on walls and floor,
four heavy ice chains from ceiling, iron window with frost bars top left,
sole source of cold blue light, icy breath visible, claustrophobic
```

### 11.2 角色提示词
**奈雅（女主）**：
```
Pale young woman, white tattered dress covered in burn marks and blood,
visible layered cuts on both wrists, deep dark circles under eyes,
exhausted, desperate, trembling from cold
```

**莉拉（长姐）**：
```
Tall beautiful woman in vibrant red dress, sharp features,
half-retracted jagged dragon horns like lightning-struck branches,
golden fire energy pulsing under skin, cruel smirk
```

**索菲亚（母亲）**：
```
Middle-aged woman, dark embroidered high priestess robe,
holding ornate golden dragon scepter, cold regal authority,
standing tall, emotionless, commanding presence
```

### 11.3 动作提示词
**逃亡奔跑**：
```
Desperate running through volcanic rocks, stumbling, gasping for air,
sweat-soaked red skin, bare feet on hot stones, looking back in fear
```

**割脉吸血**：
```
Lila's clawed fingers slicing across Naya's wrist,
bright blue blood welling up, cold steam rising from wound,
Lila pressing lips to wound, drinking, golden fire in her skin extinguishing
```

**走马灯（痛苦回忆快速蒙太奇）**：
```
Fast montage, quick cuts: childhood abuse, forced blood draining,
sister's cruel laugh, mother turning away, cage, chains, darkness,
each frame 0.5 seconds, rapid emotional assault
```

---

## 十二、AI导演提示词输出格式

AI导演智能体最终输出的分镜提示词应包含：

```
─── Shot 04 (2.5s) ───
景别：MCU（中近景）
角度：Eye Level → Slight Low Angle
运镜：Static（固定）
画面：奈雅踉跄穿过乱石缝，左手擦拭额头的汗水和血迹，
      身后远处天空暗红色的龙影掠过
光线：Low key, deep orange backlight, heat haze
色调：深橘+焦黑
镜头：85mm, shallow DOF
风格：hyper-realistic, live-action quality
Prompt：
"Medium close-up, Naya stumbling through narrow gap between charred rocks,
wiping sweat and blood from forehead, distant dark red dragon silhouette
flying across deep orange sky behind her, heat haze distorting air,
85mm lens, shallow depth of field, low key lighting,
hyper-realistic, live-action quality, 9:16 vertical"
```

---

*本文档作为AI导演智能体的提示词工程全参数词典*
