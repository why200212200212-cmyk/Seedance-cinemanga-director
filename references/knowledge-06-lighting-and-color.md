# 光影与色彩 — AI电影级光影控制

> 仓库接入说明：本文件是光影与色彩设计参考。数值和风格词应按场景、模式与生成端能力取舍，不得把案例色板或固定参数套用到无关剧本。

## 文档导航

- 一、三点布光
- 二、光比
- 三、电影级光线风格
- 四、色温与情绪
- 五、色彩脚本
- 六、AI 光影控制挑战
- 七、聚焦与景深
- 八、提示词速查

> 光线不是照亮画面的工具，而是定义情绪的语言

---

## 一、三点布光（Three-Point Lighting）

### 1.1 标准配置

| 光源 | 位置 | 功能 |
|---|---|---|
| **主光（Key Light）** | 角色前方45°侧面 | 确定主体亮部和立体感 |
| **辅光（Fill Light）** | 主光的对面 | 补阴影，控制光比 |
| **逆光（Back Light）** | 角色背后 | 分离主体和背景，勾勒轮廓 |

### 1.2 AI提示词
```
cinematic lighting, three-point lighting setup, key light from left, soft fill, rim light on right
```

---

## 二、光比（Lighting Ratio）

### 2.1 定义
主光亮度 : 辅光亮度的比例

| 光比 | 效果 | 应用场景 |
|---|---|---|
| 1:1（平光） | 无阴影，柔和 | 浪漫喜剧、广告 |
| 2:1（柔光） | 轻微立体 | 标准叙事 |
| 4:1（反差） | 明显阴影 | 戏剧、悬疑 |
| 8:1（强反差） | 深黑阴影 | 黑色电影、恐怖 |
| 16:1（极端） | 几乎全黑 | 压抑、绝望 |

### 2.2 文档中的光比设计
**SC01（赤焰石林）**：低调高饱和 → 光比 8:1（极端光比+热浪扭曲）
**SC02（地牢）**：青蓝死寂冷调 → 光比 4:1~8:1（暗部保留焦石纹理）

### 2.3 AI提示词
```
high contrast lighting, deep shadows, single light source, film noir style
low key lighting, 4:1 lighting ratio, dramatic shadows
soft lighting, diffused, 2:1 ratio, gentle shadows
```

---

## 三、五种电影级光线风格

### 3.1 伦勃朗光（Rembrandt Lighting）
- 在面部暗侧形成一个三角形的光斑
- 庄重、深沉、有层次感
- **AI**：`Rembrandt lighting, triangle of light on face, dramatic portrait`

**文档中的使用**：地牢吸血段使用低调强对比打光，"伦勃朗光照在莉拉脸上，金火能量在其皮下如岩浆游走"

### 3.2 侧光（Split Lighting）
- 半张脸完全照亮，半张脸完全在阴影中
- 分裂、对立、内心挣扎
- **AI**：`split lighting, half face in light, half in shadow`

### 3.3 背光/轮廓光（Rim / Backlight）
- 主体轮廓被光勾勒，正面几乎全黑
- 神秘、危险、崇高
- **AI**：`rim lighting, backlit, golden hour silhouette`

### 3.4 底光（Underlighting）
- 光源从下方打上来
- 恐怖、妖魔化、诡异
- **AI**：`underlighting, light from below, eerie, monstrous`

### 3.5 窗光（Window Light）
- 模拟从窗户射入的自然光线
- 孤独、等待、绝望中的一丝希望
- **AI**：`window light, natural light streaming in, cold blue daylight`

**文档中的使用**：地牢铁窗为画左上方唯一光源

---

## 四、色温与情绪

### 4.1 色温刻度

| 色温 | 颜色 | 情绪关联 |
|---|---|---|
| 1000-2000K | 烛火橙红 | 温暖/危险（火场） |
| 2000-3000K | 钨丝灯暖黄 | 舒适/怀旧 |
| 3000-4000K | 日出暖白 | 朝气/自然 |
| 5000-5500K | 日光中性白 | 客观/真实 |
| 6000-7000K | 阴天色温蓝 | 寒冷/忧郁 |
| 7000-10000K | 极地冰蓝 | 死亡/绝望 |

### 4.2 文档中的色温脚本
```
SC01：2000-3000K（熔岩橘红）
SC02：6000-8000K（冰极青蓝）
两者硬切 = 极热 vs 极寒的终极视听反差
```

### 4.3 AI提示词
```
color temperature [value]K, warm orange tones, cold blue tones
cinematic color grading, teal and orange, color contrast
```

---

## 五、色彩脚本（Color Script）

### 5.1 定义
整个故事中颜色的系统性变化，反映角色的心路历程和叙事走向。

### 5.2 颜色-情绪映射

| 颜色 | 情绪 | 在文档中的使用 |
|---|---|---|
| 橘红/橙 | 灼烧、危险、生命力 | SC01赤焰石林 |
| 焦黑 | 死亡、终结 | 石林焦石 |
| 青蓝 | 寒冷、绝望、死亡 | SC02地牢 |
| 金色 | 权力、反噬、痛苦 | 莉拉皮下金火 |
| 亮蓝 | 异能、抗拒、希望 | 奈雅的蓝血 |
| 深紫 | 中毒、控制、诡异 | 集尾紫药 |
| 纯白 | 纯洁（讽刺）、祭品 | 婚纱 |
| 鲜红 | 暴虐、权力 | 莉拉红裙 |

### 5.3 AI提示词
```
color palette: deep orange and black, volcanic wasteland
color palette: ice blue and shadow black, frozen dungeon
isolated color accent: bright blue blood against dark background
vivid purple glow against cold blue background, surreal
```

---

## 六、AI光影控制的特殊挑战

### 6.1 AI的常见光影问题

| 问题 | 表现 | 原因 |
|---|---|---|
| 光源不一致 | 同一场景中阴影方向乱飞 | AI不理解光源位置连续性 |
| 缺乏阴影逻辑 | 角色脸上光斑莫名其妙 | AI未学习物理光照模型 |
| 光色漂移 | 同一段视频暖光变冷光 | 帧间一致性不足 |

### 6.2 AI光影控制策略

1. **在Prompt中锁死光源位置**
   - `single light source from top left, cold blue` → 明确、不模棱两可

2. **每块前置全局声明**
   - 文档的做法：每块开头都写清楚"光影基信"
   - SB01a：`deep orange low-key heatwave lighting`
   - SB02a：`icy blue desaturated cold tone lighting`

3. **有限颜色调色板**
   - 限制色板范围（2-3种主色），AI出错的概率更低

4. **连续快照中标记光源**
   - 末态快照不仅标记角色位置，还要标记"光源方向未变"

---

## 七、聚焦与景深控制

### 7.1 焦平面

| 类型 | 效果 | AI提示词 |
|---|---|---|
| 浅景深 | 背景虚化，注意力集中在主体 | `shallow depth of field, bokeh background` |
| 深景深 | 全画面清晰，空间全景 | `deep focus, everything in focus` |
| 拉焦（Rack Focus） | 焦点从一个物体切换到另一个 | `rack focus, shift focus from foreground to background` |

### 7.2 文档中的景深设计
- ARRI Alexa 65 + Panavision变形宽银幕 + 默认中长焦
- "景深极浅，焦点精细分离"
- 微距大特写硬锁（ECU）：只拍物理部件，不拍接触

---

## 八、AI光影提示词速查表

| 效果 | 提示词 |
|---|---|
| 好莱坞级电影光 | `cinematic lighting, Hollywood grade, dramatic` |
| 自然光 | `natural lighting, soft diffused, overcast day` |
| 逆光剪影 | `backlit silhouette, golden rim light` |
| 极低照度 | `extremely low light, near darkness, single candle` |
| 霓虹夜景 | `neon lighting, cyberpunk, blue and pink` |
| 月光 | `moonlight, cold blue, silver glow, deep shadows` |
| 阳光/日景 | `bright sunlight, hard shadows, high contrast` |
| 顶光 | `top lighting, overhead light, harsh shadows on face` |
| 体积光/丁达尔 | `volumetric lighting, god rays, light beams through fog` |
| 暖炉光 | `firelight, warm orange flickering, dynamic shadows` |

---

*本文档作为AI导演智能体的光影控制知识库*
