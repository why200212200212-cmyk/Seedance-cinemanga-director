# 景深控制（Depth of Field）— AI电影级景深技

> 仓库接入说明：本文件是景深与焦点参考。光圈、焦距和距离必须共同成立；提示词中的数值表达只描述视觉意图，不保证生成端执行真实光学参数。

## 文档导航

- 一、景深定义
- 二、三个控制因素
- 三、情绪价值
- 四、拉焦
- 五、提示词词表

> 来源：StudioBinder Depth of Field Guide 专业资料

---

## 一、景深的定义

景深（Depth of Field / DOF）是指在画面Z轴方向上的**清晰区域的大小**。

- **浅景深（Shallow DOF）**：清晰区域小，背景虚化
- **深景深（Large DOF / Deep Focus）**：清晰区域大，前后景都清晰

---

## 二、景深的三个控制因素

### 2.1 光圈（Aperture）
| 光圈值 | 景深 | 进光量 |
|---|---|---|
| f/1.4（大光圈） | 极浅 | 极多 |
| f/2.8 | 浅 | 多 |
| f/5.6 | 中 | 中 |
| f/11 | 深 | 少 |
| f/22（小光圈） | 极深 | 极少 |

**规律**：光圈越大（f值越小）→ 景深越浅

### 2.2 焦距（Focal Length）
| 焦距 | 景深效果 | AI实现 |
|---|---|---|
| 广角（16-35mm） | 较深 | `wide angle lens, deep focus` |
| 标准（35-70mm） | 适中 | `50mm lens, natural DOF` |
| 中长焦（85-135mm） | 较浅 | `85mm lens, shallow DOF` |
| 长焦（200mm+） | 极浅 | `telephoto lens, very shallow DOF` |

### 2.3 拍摄距离（Focus Distance）
**规律**：离被摄体越近 → 景深越浅（微距拍摄景深极浅）

---

## 三、景深的情绪价值

| 景深 | 情绪效果 | 适用场景 |
|---|---|---|
| 极浅（Selective Focus） | 孤立、隐私、内心 | 大特写、微表情 |
| 浅 | 专注、亲密 | 对话、单人镜头 |
| 适中 | 正常叙事 | 中景对话 |
| 深 | 客观、宏大、全员 | 全景、群像 |
| 极深（Deep Focus） | 全知、史诗 | 大远景、复杂调度 |

### 3.1 经典案例
- **《公民凯恩》**：深焦摄影（Deep Focus）让前景、中景、后景全部清晰——观众自己选择看哪里
- **《教父》**：浅景深隔离角色，强化孤独感
- **《闪灵》**：中长焦浅景深跟踪骑车的孩子，制造不安

### 3.2 文档中的景深使用
- ARRI Alexa 65 + Panavision变形宽银幕 + **默认中长焦**
- "景深极浅，焦点精细分离"（浅景深是竖屏短剧的默认配置）
- 微距大特写硬锁（ECU）——极浅景深的极致

---

## 四、拉焦（Rack Focus）

### 4.1 定义
在同一个镜头中，焦点从一个物体切换到另一个物体。

### 4.2 功能
- 转移观众注意力（强制看哪里）
- 揭示隐藏信息（前景模糊→后景清晰）
- 表现角色的认知变化

### 4.3 AI实现
```
rack focus, shift focus from foreground chains to her face
focus pull from blurry background to sharp subject
```

---

## 五、AI景深控制提示词

| 效果 | 英文提示词 |
|---|---|
| 浅景深 | `shallow depth of field, bokeh background` |
| 深景深 | `deep focus, everything in focus` |
| 极浅/选择性焦点 | `selective focus, only face in sharp focus` |
| 拉焦 | `rack focus, focus shift from [A] to [B]` |
| 前景虚 | `out of focus foreground, blurred foreground elements` |
| 背景虚 | `creamy bokeh background` |
| 大光圈 | `wide aperture, f/1.4 look` |
| 缩小光圈 | `stopped down, large DOF` |

---

*本文档补充自StudioBinder景深控制专业资料*
*原始资料链接：studiobinder.com/blog/depth-of-field/*
