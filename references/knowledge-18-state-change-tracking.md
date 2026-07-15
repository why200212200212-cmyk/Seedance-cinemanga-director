# 状态变化追踪系统 — 分镜间连续性保证

> 仓库接入说明：本文件只在多镜、多场、多条视频或状态变化密集时读取，用于补充位置、身体、情绪、视线与道具的状态追踪。执行时必须把姓名键替换为永久 `CHAR-ID`，并并入仓库既有状态账本、尾帧接力与摄影机路线最终节点。
> 冲突边界：`continuity-rules.md` 的角色身份、服装、伤势、道具手性、空间、轴线、光影、天气、相机路径和尾帧合同优先。文中的案例状态不能迁移，Python 片段只是概念伪代码，不得当作已实现或直接执行的程序。

## 文档导航

- 一、状态追踪目的
- 二、状态变化字段
- 三、六个追踪维度
- 四、块间连续性指令
- 五、状态机概念与检查规则

---

> 用于AI分镜智能体：防止"角色位置漂移 + 情绪跳变 + 道具消失"

---

## 一、为什么需要状态变化追踪

AI视频生成模型的最大痛点：**跨帧不一致性**。具体表现为：

| 问题 | 表现 | 原因 |
|---|---|---|
| **位置漂移** | 上一镜在画左，下一镜在画右 | 模型没有"位置记忆" |
| **情绪跳变** | 上一镜还在哭，下一镜突然笑 | 模型不理解情绪连续性 |
| **道具消失** | 上一镜手里拿着剑，下一镜空了 | 模型不维护道具状态 |
| **服装变化** | 白裙→红裙 | 模型没记录战损 |
| **伤痕跳动** | 红肿位置随意变化 | 没记录物理标记 |

**状态变化追踪系统**就是用来解决这些问题的——在每个镜头结束后记录所有角色的精确状态，下一镜从该状态出发。

---

## 二、状态变化字段详解

### 2.1 角色状态（Position + Status + Emotion）

每个角色分三个维度追踪：

```yaml
[角色名]:
  position:               # 空间位置（精确到画面分区）
    screen_x: "left/center/right/mid-left/mid-right"  # 横向
    screen_y: "top/mid/bottom"                         # 纵向
    z_depth: "foreground/midground/background"         # 景深
    posture: "standing/kneeling/sitting/lying/stumbling/hanging"  # 姿态
  
  status:                 # 生理状态
    face: "red_swollen/tearful/pale/bloody/soot"      # 面部
    clothing: "torn/intact/wet/burned/muddy"           # 衣着
    injuries: ["left_cheek_red", "wrist_cut", ...]     # 伤痕列表
    props: ["chains", "bowl"]                          # 持有的道具
  
  emotion:                # 情绪状态
    primary: "fear/despair/anger/resignation/hope"     # 主要情绪
    intensity: 1-10                                     # 强度
    direction: "looking_screen_left/right/up/down"     # 视线方向
```

### 2.2 变化记录格式

```yaml
# 镜头前的状态 → 镜头中的变化 → 镜头后的状态
奈雅:
  before: "跪缚祭坛, 意识涣散, 左脸红肿"
  change: "被放血 → 头部垂落 → 蓝血滴落"
  after: "头部垂落, 左手腕流血, 半昏迷"
  
  position_before: "画中祭坛中心, 跪姿, 中景"
  position_after: "画中祭坛中心, 头部垂向画左, 中景"
  
  emotion_before: "恐惧(强度7), 看向画右"
  emotion_after: "涣散(强度4), 视线向下"
```

---

## 三、状态变化追踪的6个维度

### 3.1 空间位置（Spatial Position）

**XYZ轴坐标化**：

| 轴 | 分区 | 在文档中的应用 |
|---|---|---|
| X轴（横向） | 画左/画中/画右 | 奈雅在画左地表, 莉拉在画右中景 |
| Y轴（纵向） | 上/中/下 | 红龙在高位Y轴, 奈雅在低位Y轴 |
| Z轴（景深） | 前/中/后 | 前景铁窗虚化→中景祭坛→后景冰墙 |

### 3.2 权力位置（Power Position）

| 权力位 | 定义 | 在文档中的使用 |
|---|---|---|
| 画右高位 | 绝对权力位 | 索菲亚在画右大门处 |
| 画中高位 | 施暴位 | 莉拉在祭坛上方 |
| 画左低位 | 受难位 | 奈雅在地表最低位 |

### 3.3 身体状态（Physical Status）

按照《炎龙新娘》文档的"动态战损"系统：

```yaml
奈雅的身体状态演进:
  SB01a(逃亡): skin_red + sweat_soaked + dress_sooty
  SB01b(截获): face_congested + neck_grip_mark  
  SB02a(吸血): wrist_cut + blue_blood + pale
  SB02b(耳光): left_cheek_swollen + lip_blood
  SB02d(撕衣): dress_torn + half_naked + shivering
  SB02e(揪发): hair_disheveled + scalp_pain + tears_blue_blood
  SB02f(灌药): mouth_purple_liquid + throat_wet + eyes_dilated
```

### 3.4 情绪状态（Emotional Arc）

```
SB01a: 恐慌(8) → 恐惧(9)
SB01b: 绝望(9) → 被压制(10)
SB02a: 痛苦(8) → 涣散(6)
SB02b: 被摧毁(7) → 亲情粉碎(9)
SB02d: 屈辱(10) → 绝望抗辩(8)
SB02e: 彻底绝望(10) → 死寂(10)
SB02f: 空洞(10) ← 终极定格
```

### 3.5 视线向量（Eye-Line）

```
奈雅: 看画右(莉拉) → 看画左上方(恶龙) → 看画右(母亲) → 看画上方(空洞) → 失焦(无方向)
莉拉: 俯视画左(奈雅) → 看画右(母亲撒娇) → 俯视画左(嘲讽)
索菲亚: 俯视画左(奈雅) → 看向画中(下令) → 俯视(完成)
```

### 3.6 道具状态（Prop Tracking）

| 道具 | 出场Beat | 状态变化 |
|---|---|---|
| 冰质铁链 | B06 | 完整冰封 → 被融解断落 → 焦黑散落 |
| 蓝色血液 | B07 | 流出 → 被吸食 → 滴落 → 擦在婚纱上 |
| 祭司权杖 | B09 | 顿地 → 握持 → 始终在索菲亚手中 |
| 奢华婚纱 | B11 | 被抛掷 → 平铺 → 被蓝血抓皱 |
| 诡异紫药 | B14 | 碗中翻滚 → 倾泻 → 被吞咽 → 嘴角残留 |

---

## 四、块间连续性指令

每块结尾必须写"下一块首镜续写要求"，这是状态变化追踪的对外接口：

```yaml
# SB02e → SB02f 的连续性指令
next_block: "SB02f"
block_end_snapshot:
  奈雅: "侧趴于画左地表最低位，衣衫破碎，长发散乱沾霜雪，左脸高度肿胀"
  索菲亚: "高大如雕塑般矗立于画右远景高位，右手执权杖"
  莉拉: "直立画中偏右，面带满足讥讽"
  奢华婚纱: "平铺地表，被右手抓出的蓝血褶皱"

first_shot_requirement: 
  "首镜必须从女仆布鞋踏入画中、双手端着散发翻滚诡异紫气药碗的特写切入，严禁状态漂移"
```

---

## 五、AI智能体实现此系统的方式

### 5.1 状态维护（State Machine）

```python
class StateTracker:
    """状态变化追踪器"""
    
    def __init__(self):
        self.states = {}  # {角色名: 当前状态}
        
    def update(self, shot_result):
        """根据镜头的状态变化更新"""
        for char, changes in shot_result.get("state_changes", {}).items():
            if char not in self.states:
                self.states[char] = {}
            # before → change → after
            self.states[char] = changes.get("after", self.states[char])
    
    def get_end_snapshot(self):
        """获取当前所有角色的末态快照"""
        return self.states
    
    def validate_continuity(self, shot, prev_shot):
        """检查连续性：位置/情绪/道具是否跳变"""
        issues = []
        # 检查位置漂移
        if self._position_jumped(shot, prev_shot):
            issues.append("位置漂移")
        # 检查情绪跳变
        if self._emotion_jumped(shot, prev_shot):
            issues.append("情绪跳变")
        # 检查道具连续性
        if self._prop_missing(shot, prev_shot):
            issues.append("道具丢失")
        return issues
```

### 5.2 检查规则

| 规则 | 触发条件 | 严重程度 |
|---|---|---|
| 位置漂移 | 角色在画左→画右无过渡 | ★★★★★ (致命) |
| 情绪跳变 | 愤怒→喜悦无中间状态 | ★★★★ (严重) |
| 道具消失 | 持剑→空手无放下动作 | ★★★★ (严重) |
| 服装突变 | 白裙→蓝裙无更换动作 | ★★★ (中等) |
| 伤痕跳动 | 红肿→消退无治疗过程 | ★★★ (中等) |

---

*本文档作为AI分镜智能体的连续性管理核心规范*

