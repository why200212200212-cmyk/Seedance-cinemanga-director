# 一镜到底Prompt模板库 — 8种经典长镜头的AI实现

> 仓库接入说明：本文件只在 `knowledge-21-long-take-guide.md` 的长镜头适用闸门通过后读取，作为 Seedance 长镜头提示词骨架。模板中的平台适配表、固定时长和效果描述不是当前能力合同。
> 编译边界：每次使用必须绑定当前剧本的永久 `CHAR-ID`、独立角色板、镜头号与 `USE` 状态；建立 CAM 节点、分段箭头、进入/离开方向、HOLD、起止构图、轴线、焦点、动作、声音和 `block_end_snapshot`。伪一镜到底还须为每个接缝记录末帧锚点、遮挡物、运动方向和状态连续性；不得复制案例人物、剧情、暴力或音乐。

## 文档导航

- 模板 1：斯坦尼康跟拍
- 模板 2：升降揭示
- 模板 3：环绕审视
- 模板 4：穿越转场
- 模板 5：主观沉浸
- 模板 6：空间串联
- 模板 7：升降情绪弧
- 模板 8：快节奏动作一镜
- 工具适配参考

---

> 全部以 Seedance 2.0 为主引擎优化
> 每套包含：中英文Prompt + 分段策略 + 技术参数

---

## 模板1：斯坦尼康跟拍（Steadicam Follow）

**经典来源**：《好家伙》夜总会入场、《1917》战壕行走

**效果**：摄影机紧跟在角色身后/身侧，穿过不同空间，展示环境的层次感。

**Seedance分段Prompt**：

```
Segment 1 (5s):
Wide shot, Steadicam following subject from behind
Subject walks through narrow corridor
Warm practical lighting from ceiling fixtures
Slight natural sway, shoulder-height camera
Continuous movement, no cuts

Segment 2 (5s) - continue from seg1 last frame:
Camera maintains same distance and height
Subject pushes through double doors
Lighting shifts from warm to cool
New space revealed: large open hall
Camera does NOT decelerate at segment end

Segment 3 (5s) - continue from seg2 last frame:
Camera arcs left as subject turns
Revealing crowd, activity, spectacle
Ambient light from large windows
Completed 3-segment 15-second Steadicam take
```

**在短剧中的应用**：女主从地牢被拖行到祭坛——紧跟在拖拽者身后的跟拍。

---

## 模板2：升降揭示（Crane Reveal）

**经典来源**：《历劫佳人》开场、《触不可及》主题揭示

**效果**：摄影机从高空下降或从低处上升，揭示宏大场景或权力关系。

**Seedance Prompt**：
```
Continuous crane shot, single take

0-3s: Camera starts at ceiling height, looking down
View: Dungeon floor from above, tiny figure in center
Lighting: Cold blue ambient, single beam from above

3-6s: Camera begins slow descent
Movement: Vertical drop, no lateral drift
Focus: Deep focus entire scene

6-9s: Camera reaches eye level
Subject: Naya kneeling on altar, chains visible
Composition: Her face centered, chains framing bottom

9-12s: Camera continues to lower, now slightly below eye level
Angle shifts from eye level to low angle
Her figure becomes imposing against ceiling light
Power dynamic: Subject appears larger, more dominant

12-15s: Camera stops, holds low angle for 3 seconds
Complete emotional arc: small victim → central figure
```

---

## 模板3：环绕审视（Orbital Examination）

**效果**：摄影机围绕角色180-360°弧线运动，审视其处境。

**Seedance Prompt**：
```
Arc shot, 180-degree orbit around subject
Single continuous movement, no cuts

Subject: Naya, kneeling on frost-covered altar
Camera begins at her left side, MCU
Orbits in front of her (close pass, 2ft distance)
Completes orbit at her right side

During orbit:
- Camera maintains constant speed
- Focus stays locked on her face
- Background elements rotate behind her:
  L: Frost-covered chains
  Center: Distant iron window with blue light
  R: Stone wall with candle sconces
- Lighting on her face remains consistent
- Her expression: devastating stillness

Duration: 8s for 180° orbit
Speed: Slow and deliberate
Style: Ghostly observer POV
```

---

## 模板4：穿越转场（Dimensional Crossing）

**效果**：穿过一个障碍物（门/窗帘/阴影），进入完全不同的时空。

**Seedance Prompt**：
```
Single continuous shot, dimensional crossing

Part 1 (0-4s):
Camera approaches heavy iron door
Door begins to open from the other side
Crack of light appears, widening

Part 2 (4-5s): CROSSING POINT
Door swings fully open
Blinding white light fills frame completely (0.5s)
Sound: Muffled, then clear

Part 3 (5-10s):
Light fades
Camera continues through doorway
ON THE OTHER SIDE: Completely different space
Dungeon → Wedding hall
Cold blue → Warm golden
Chains → Flowers and candles
Camera movement uninterrupted
Same speed, same height, same focus

Technical:
- Crossing point acts as transition anchor
- Light bloom masks the spatial jump
- Lighting color temperature shifts during bloom
```

---

## 模板5：主观沉浸（First-Person / POV Take）

**效果**：全片以角色主观视角呈现，观众所见即角色所见。

**Seedance Prompt**：
```
First-person POV, continuous single take

Visual: Slight head bob, natural human movement
Breathing sound throughout

0-3s: Looking down at own hands
Hands bound with rough rope
Bare feet on frost-covered stone
Standing up slowly, vision blurs then clears

3-7s: Look up, raise head
View of dungeon materializes
Frost on walls, iron window high on left
Chain sounds from movement

7-10s: Turn head left
Sister Lila enters frame, red dress
Her face: cruel smirk, dragon horn remnants
Looking down at viewer (POV)

10-12s: Sister reaches toward camera (POV)
Hand extends, fingers toward lens
BLACK (hand covers lens) - end of take

Style: Raw, immersive, subjective
Breathing intensifies with emotion
```

---

## 模板6：空间串联（Connected Spaces）

**效果**：在一个连续镜头中穿越多个不同的空间，展示空间的关联。

**Seedance Prompt**：
```
Continuous spatial journey, 15 seconds, 3 spaces

SPACE 1 (0-5s) - DUNGEON:
Camera starts on frost-covered floor, tilts up
Naya chained to altar, guards flanking
Cold blue light, iron, stone
Camera moves LEFT toward dark corridor

TRANSITION (5s):
Camera enters corridor, darkness briefly covers frame (0.3s)
When light returns:

SPACE 2 (5-10s) - THRONE ROOM:
Camera emerges in grand hall
Queen Sophya on throne, courtiers lining walls
Warm torch light, gold, crimson banners
Camera continues LEFT toward side door

TRANSITION (10s):
Camera passes through curtain, silk brushing lens

SPACE 3 (10-15s) - WEDDING CHAMBER:
Camera enters private chamber
White wedding dress laid out on bed
Purple potion on nightstand, vapor rising
Silence, loneliness, anticipation
Camera settles on dress, holds 3 seconds

Each space: Distinct lighting, color, mood
Movement: Constant speed, purposeful direction
Connectivity: Spaces feel like real adjacent rooms
```

---

## 模板7：升降情绪弧（Vertical Emotion Arc）

**效果**：摄影机从低到高（或反之）的升降与角色的情绪变化同步。

**Seedance Prompt**：
```
Vertical camera movement mirroring emotional arc

START (0s):
Camera: Lying on floor, ground level (as if fallen)
View: Naya's face pressed to stone floor
One tear pooling on stone
Emotion: Rock bottom despair

RISE BEGINS (3s):
Camera slowly BOOMS UP from floor
As camera rises, her face comes into view
She begins to push herself up
Emotion: Faint resolve

CONTINUED RISE (6s):
Camera at knee level as she kneels
She raises head, looks forward
Light catches her face for first time
Emotion: Determination forming

PEAK (9s):
Camera at eye level as she stands fully
She is framed against iron window
Cold blue light behind her creates silhouette
Emotion: Defiance, transformation

HOLD (12-15s):
Static on her face, 3 second hold
Eyes burn with new resolve
Complete emotional journey in one vertical take
```

---

## 模板8：快节奏动作一镜（Action Oner）

**经典来源**：《老男孩》走廊锤战、《夺宝奇兵》追逐

**效果**：侧视或跟拍的连续动作，穿越多个障碍/敌人。

**Seedance Prompt**：
```
Action long take, continuous horizontal tracking

CAMERA: Side-scrolling, tracks left to right
Consistent speed, locked on action

SUBJECT: Naya running through palace corridor

0-2s: Camera trucks right alongside running figure
Breathing heavy, footsteps on stone
Desperation visible

2-5s: She grabs wall edge, swings around corner
Camera follows, same speed
Second corridor, longer

5-8s: Guards appear from doorway ahead
She slides under reaching arm
Camera drops to match her low position
Then rises as she stands

8-10s: She pushes through heavy curtain at corridor end
Camera passes through curtain
NEW SPACE: Open courtyard, daylight

10-12s: Sky, wind, freedom glimpsed
Camera holds wide as she slows to stop
Then: Shadow falls across frame
Sister Lila lands in front of her

End: 12-second continuous action take
No cuts, steady horizontal track
```

---

## 原资料工具适配速查表（时间敏感，使用前核验）

| 模板 | Seedance 2.0 | Runway Gen-4 | Kling 3.0 | 即梦AI |
|---|---|---|---|---|
| 斯坦尼康跟拍 | ✅ 分段续写 | ✅ Motion Brush | ✅ 首尾帧 | ✅ 多帧 |
| 升降揭示 | ✅ 时间戳控制 | ✅ Camera Control | ✅ 多镜叙事 | ✅ |
| 环绕审视 | ✅ 弧线控制 | ✅ Orbit preset | ⚠️ 基础环绕 | ✅ |
| 穿越转场 | ✅ FLF2V最佳 | ⚠️ 需遮挡物 | ✅ 首尾帧升级 | ✅ 帧间 |
| 主观沉浸 | ✅ POV控制 | ✅ 参考视频 | ⚠️ | ⚠️ |
| 空间串联 | ✅ 15s分段 | ✅ 场景一致性 | ✅ 多镜连接 | ✅ 智能多帧 |
| 升降情绪弧 | ✅ 垂直运镜 | ✅ Vertical move | ✅ 升降 | ✅ |
| 动作一镜 | ⚠️ 需快切 | ⚠️ 长动作难 | ✅ 动作最好 | ⚠️ |

---

*本文档是AI分镜智能体的一镜到底提示词模板库*
*所有模板以Seedance 2.0为主引擎优化*
