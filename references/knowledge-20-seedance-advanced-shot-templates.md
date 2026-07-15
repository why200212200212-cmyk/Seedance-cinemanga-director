# AI高难度镜头 — Seedance 2.0 专用提示词模板库

> 仓库接入说明：本文件仅在 `knowledge-19-advanced-camera-techniques.md` 的高难度闸门通过后读取，用作 Seedance 提示词改写骨架。模板不是能力承诺，也不是可直接复制的成品提示词。
> 编译边界：必须替换为当前剧本的永久 `CHAR-ID`、独立角色板、镜头号、`USE` 映射、CAM 节点、时间段、起止构图、空间锚点和声音规则；不得迁移案例人物、剧情、伤害、音乐与固定风格。固定帧率、时长、画幅、种子和平台效果以当前生成端为准，并接受提示词编译器、复杂度预算与连续性质检。

## 文档导航

- 模板 1：时空穿越推镜
- 模板 2：镜像分裂
- 模板 3：环绕时间冻结
- 模板 4：无限下降摇镜
- 模板 5：情绪光照变色
- 模板 6：镜像世界穿越
- 模板 7：分身同步
- 模板 8：记忆闪切蒙太奇
- 高难度镜头使用决策树

---

> 所有提示词以 Seedance 2.0 为主引擎优化
> 每个模板包含：中英文提示词 + 关键技术参数 + 使用场景

---

## 模板1：时空穿越推镜（Time-Space Push）

**难度**：⭐⭐⭐⭐
**场景**：女频虐恋——从回忆到现实的穿越

```
Shot description [中文]：
中近景，极慢推镜，女主站在原地，背景从当前场景逐渐过渡到回忆场景，
光线从冷蓝渐变到暖黄，女主表情从绝望渐变为希望。

Seedance Prompt [English]：
Medium close-up, extremely slow push-in
Subject: Woman standing still, expression shifting from despair to hope
Background: Gradually transitions from current dungeon (icy blue, frost)
  to memory of childhood garden (warm gold, soft sunlight)
Transition: Continuous, seamless blend over 5 seconds
Lighting: Cold blue (3200K) → warm amber (4500K) gradient
Focus: Shallow DOF on face, background blur shifts with scene
Duration: 5s | Aspect: 9:16 | FPS: 24

Keywords: temporal transition, emotional push-in, memory flashback seamless
```

---

## 模板2：镜像分裂（Mirror Fracture）

**难度**：⭐⭐⭐⭐
**场景**：揭示角色的隐藏身份/真实自我

```
Shot description [中文]：
中景，固定镜头，女主站在破镜子前。
镜中倒影与本人做出不同动作——倒影在微笑，本人在哭泣。
摄影机缓慢推近，镜中影像逐渐变成另一种状态的自己。

Seedance Prompt [English]：
Medium shot, static camera
Subject: Woman standing before cracked mirror
Mirror reflection: Shows SAME woman but with different expression 
  (reflection smiles while real self weeps)
Action: Reflection moves independently, reaching toward glass
Camera: Slow push-in beginning at 2-second mark
Transition: As camera pushes in, reflection gradually transforms 
  into regal version of herself (crown, white dress, healed scars)
Lighting: Real side - cold blue / Reflection side - warm golden
Focus: Shallow DOF, locked on reflection's face
Duration: 6s | Aspect: 9:16 | FPS: 24

Keywords: mirror reflection split, dual identity reveal, independent reflection
```

---

## 模板3：环绕时间冻结（Arc Freeze Frame）

**难度**：⭐⭐⭐⭐⭐
**场景**：命运转折瞬间——环绕角色时周围世界冻结

```
Shot description [中文]：
摄影机环绕女主做180度弧线运动，
当摄影机转到角色侧面时，周围一切冻结（悬浮的眼泪、飘动的头发），
只有女主和摄影机继续运动。

Seedance Prompt [English]：
Arc shot, 180-degree orbit around subject
Subject: Woman at moment of emotional climax
During orbit: When camera reaches 90°, TIME FREEZES
  - Tears freeze mid-air
  - Hair strands suspend
  - Falling objects stop
  - Only camera continues movement
  - Subject retains ability to blink and breathe
After full orbit: Time resumes normally at original speed
Lighting: Single dramatic key light from above, volumetric beams
Focus: Deep focus for frozen elements, shallow on subject
Duration: 8s | Aspect: 16:9 | FPS: 24

Keywords: bullet time variant, emotional climax freeze, arc with temporal stop
```

---

## 模板4：无限下降摇镜（Infinite Descent Crane）

**难度**：⭐⭐⭐⭐⭐
**场景**：坠入绝望深渊——象征性的无限下降

```
Shot description [中文]：
摄影机从塔顶开始下降，穿过层层楼板
（每层展现不同的人生阶段：童年→囚禁→受虐→婚礼），
最终到达地心深处，女主的身影越来越小。

Seedance Prompt [English]：
Crane shot, continuous descent
Camera: Starts at tower top, descends through multiple floors
Each floor cross-section reveals different life stage:
  Floor 1: Childhood (warm, golden, laughter)
  Floor 2: Prison (cold blue, bars, shadows)
  Floor 3: Torture (dark red, chains, blood)
  Floor 4: Wedding (pale white, forced smile, purple mist)
Transition: Seamless floor penetration, material shift per layer
  (wood → stone → iron → silk)
Lighting: Gradual darkening, each floor unique color accent
End: Figure becomes tiny speck in infinite darkness
Duration: 10s | Aspect: 9:16 | FPS: 24

Keywords: symbolic descent, life stages cross-section, infinite crane
```

---

## 模板5：情绪光照变色（Emotional Color Shift）

**难度**：⭐⭐⭐
**场景**：情绪转变的外化——不需运镜，全靠光影和色彩说话

```
Shot description [中文]：
大特写，完全固定镜头，女主的一只眼睛。
5秒内，光照从暖金色渐变到冰冷蓝。
眼珠中的倒影从"微弱的希望之光"变为"彻底的死寂"。
不需要任何运镜，光和色的变化讲完整个情绪弧线。

Seedance Prompt [English]：
Extreme close-up, fully static, locked tripod
Subject: Single eye of woman
Duration: 5 seconds
Color shift: Warm amber (3500K) → cold blue (7500K) gradient across full duration
  - 0-1s: Warm glow, pupil slightly dilated (hope)
  - 1-2s: Mixed temperature (uncertainty)
  - 2-3s: Blue begins dominating (fear)
  - 3-4s: Cold blue, pupil constricting (despair)
  - 4-5s: Pure ice blue, pupil fixed (death of hope)
Reflection in eye: Small warm light fading to complete stillness
Lighting: Only the changing key light, everything else black
Focus: Extremely shallow DOF, only eye surface in focus
No camera movement whatsoever
Aspect: 9:16 | FPS: 24

Keywords: emotional color script, static storytelling, eye reflection
```

---

## 模板6：镜像世界穿越（Through The Looking Glass）

**难度**：⭐⭐⭐⭐⭐
**场景**：穿越水面/镜面进入另一个世界

```
Shot description [中文]：
摄影机推近水面，接触水面的瞬间过渡到水下世界。
水下世界是完全不同的时空——光影倒转，颜色反转。
角色从水面穿越，进入"镜像世界"。

Seedance Prompt [English]：
Push-in toward water surface
Moment of contact: Camera crosses water plane
  - Ripple distortion effect at boundary
Underwater world: Complete spatial inversion
  - Colors inverted (cold becomes warm, dark becomes light)
  - Gravity reversed (falling upward)
  - Sound muffled, then new world sounds emerge
  - Character emerges from above, falling into new landscape
Transition: Seamless, single continuous take
  - Water surface acts as dimensional barrier
Lighting: Above water - harsh direct / Below water - soft diffuse
Focus: Rack focus at moment of crossing
Duration: 7s | Aspect: 9:16 | FPS: 24

Keywords: dimensional crossing, water plane transition, inverted world
```

---

## 模板7：分身同步（Splitting Self）

**难度**：⭐⭐⭐⭐
**场景**：角色做出选择时——两个分身分别走向不同命运

```
Shot description [中文]：
中景固定，女主站在画面中央。
画面从中间分裂（垂直分屏），左右两边呈现她做出不同选择后的命运：
左边：选择反抗→被折磨的更惨
右边：选择服从→被献祭
两个分身同时动作，表情各异
最后画面合并，回到她做决定的瞬间。

Seedance Prompt [English]：
Medium shot, static camera
Subject: Woman standing center frame
Frame SPLITS vertically at 1-second mark:
  LEFT HALF: Woman chooses resistance
    - Dragged away by guards
    - Torn dress, bruises
    - Cold blue lighting
    - Desaturated colors
  RIGHT HALF: Woman chooses submission
    - Dressed in white wedding gown
    - Crown placed on head
    - Warm golden lighting
    - Saturated, dreamy colors
Both versions act independently, different expressions
At 4-second mark: Frame MERGES back to single woman
  - Expression of determination (decision made)
  - Neutral lighting, midpoint between two futures
Duration: 6s | Aspect: 16:9 (horizontal split works best in wide)

Keywords: split screen fate, parallel destiny, decision moment
```

---

## 模板8：记忆闪切蒙太奇（Memory Flash Montage）

**难度**：⭐⭐⭐⭐
**场景**：女主濒死/觉醒时的记忆闪回

```
Shot description [中文]：
密集蒙太奇——1.5秒内闪过8个记忆碎片。
每个碎片0.15-0.2s，以心跳声为节奏。
碎片按时间顺序从童年到当下排列。

Seedance Prompt [English]：
Rapid montage sequence, 8 fragments in 1.5 seconds
Each fragment 0.15-0.2s, beat-synced to heartbeat sound

Fragment 1 (0-0.18s): Five-year-old girl laughing (EXTREME WARMTH)
Fragment 2 (0.18-0.36s): First time chained, crying (BLUE PAIN)
Fragment 3 (0.36-0.54s): Sister's face contorted in rage (RED ACCENT)
Fragment 4 (0.54-0.72s): Blue blood dripping from wrist (CLOSE-UP)
Fragment 5 (0.72-0.90s): Mother turning away, cold back (DUTCH ANGLE)
Fragment 6 (0.90-1.08s): White wedding dress on floor (DEAD SILENCE)
Fragment 7 (1.08-1.26s): Crown falling into mud (SLOW MOTION IN QUICK CUT)
Fragment 8 (1.26-1.50s): Eye snapping open in present (RETURN TO REALITY)

Each fragment: Shallow DOF, isolated color accent, single clear image
Transition: Hard cuts only, no dissolves
Audio: Heartbeat pounding throughout

Keywords: life flash, memory montage, emotional recall
```

---

## 高难度镜头使用决策树

```
这镜想要达到什么效果？
├── 世界观揭示 → 模板1(时空穿越推镜)
│                  模板4(无限下降摇镜)
├── 角色内心展现 → 模板2(镜像分裂)
│                  模板5(情绪光照变色)
├── 命运/选择展示 → 模板3(环绕时间冻结)
│                     模板7(分身同步)
├── 世界穿越 → 模板6(镜像世界穿越)
├── 情绪高潮 → 模板5(情绪光照变色)
│                模板3(环绕时间冻结)
└── 记忆觉醒/濒死 → 模板8(记忆闪切)
```

---

*本文档是AI分镜智能体的高难度镜头提示词模板库*
*所有模板以Seedance 2.0为主引擎优化*

