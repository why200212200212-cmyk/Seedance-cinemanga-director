# AI 导演参考知识库索引

> 来源范围：用户提供的 00–22 号分镜参考资料，接入日期 2026-07-15。
> 本知识库只用于辅助导演判断，不是执行硬规则，也不得替代 `SKILL.md`、模板、质量门槛或平台能力合同。

## 1. 使用优先级

发生冲突时，按以下顺序处理：

1. 用户当前明确要求、原剧本事实与原台词；
2. `SKILL.md` 的流程、身份绑定、连续性、分镜字段和执行门槛；
3. 当前任务适用的模板与 `quality-checklist.md`；
4. 已验证的当前平台能力；
5. 本知识库中的方法、案例、词表与经验判断。

案例中的人物、故事、镜号、题材风格、相机型号和固定参数不得自动迁移到其他剧本。涉及平台版本、最长时长、分辨率、控制项和效果强弱时，必须重新核对当前官方能力或用户提供的生成端条件。

## 2. 按任务读取

不要一次读取全部资料。先完成剧情分析，再只读取与当前决策直接相关的文件。

| 当前任务 | 读取资料 | 用途 |
|---|---|---|
| 长篇或复杂剧本拆解、质量门禁、资产账本 | [01 分镜工作流](knowledge-01-storyboard-workflow.md) | 补充问题驱动、因果链、音画账本和快照方法 |
| 选择景别、角度、基础构图或轴线 | [02 镜头语言基础](knowledge-02-shot-language-basics.md) | 查询镜头语言术语与基础适用情境 |
| 选择摄影机运动 | [03 运镜百科](knowledge-03-camera-movement-encyclopedia.md) | 比较固定、摇、推拉、移、升降、弧线等运动 |
| 把运镜编译为生成提示词 | [04 AI 运镜提示词](knowledge-04-ai-camera-prompting.md) | 参考运镜句式、速度分段和验证流程 |
| 多镜组接、节奏、视线和屏幕方向 | [05 视觉叙事与剪辑](knowledge-05-visual-narrative-editing.md) | 检查轴线、30 度、匹配剪辑和节奏 |
| 设计光源、色温、光比和色彩脚本 | [06 光影与色彩](knowledge-06-lighting-and-color.md) | 补充光线与色彩选择依据 |
| 高风险物理接触镜头 | [07 物理接触规避](knowledge-07-physical-contact-workarounds.md) | 参考拆拍、反应镜头与声音替代方案 |
| 9:16 竖屏短剧 | [08 竖屏 9:16](knowledge-08-vertical-9x16.md) | 调整垂直构图、Z 轴调度和多人布局 |
| 查询中英摄影参数词汇 | [09 提示词参数字典](knowledge-09-director-prompt-dictionary.md) | 作为词典查用，不整段堆叠进提示词 |
| 人物走位、权力关系和出入口 | [10 场面调度](knowledge-10-blocking-and-staging.md) | 设计 Blocking、Staging 与 XYZ 调度 |
| 景深、焦平面和拉焦 | [11 景深控制](knowledge-11-depth-of-field.md) | 校验光圈感、焦距感、距离与焦点变化 |
| 精细构图选择 | [12 镜头构图](knowledge-12-shot-composition.md) | 比较三分、对称、引导线、框架和负空间 |
| Seedance 2.0 多模态素材与分镜参考 | [13 Seedance 2.0 指南](knowledge-13-seedance-2-guide.md) | 了解已核验的分镜、角色、场景、运镜与音视频参考方式 |
| 用户明确要求 Runway 提示词或跨平台运镜翻译 | [14 Runway Gen-4 运镜](knowledge-14-runway-gen4-camera-guide.md) | 只参考运动描述方法，不覆盖 Seedance 主流程 |
| 用户明确要求比较或选择生成工具 | [15 工具能力对比](knowledge-15-video-tool-comparison.md) | 建立待核验候选项，不自动替用户选型 |
| 工业化分镜大表、完整字段词典或复杂项目追踪 | [16 13字段分镜大表](knowledge-16-shot-table-schema.md) | 扩展镜头字段与状态变化交付，不改变核心流程 |
| 需要查看13字段的局部映射实例 | [17 分镜大表案例](knowledge-17-shot-table-case-study.md) | 只学习字段映射；隔离案例剧情、人物、镜号与参数 |
| 多镜、多场、多条视频或状态变化密集 | [18 状态变化追踪](knowledge-18-state-change-tracking.md) | 补充位置、身体、情绪、视线、道具和块间快照 |
| 剧本明确需要超现实、时空扭曲、身体变形或强VFX难镜头 | [19 高难度运镜技术库](knowledge-19-advanced-camera-techniques.md) | 先做可执行性闸门，再选择实现或降级方案 |
| 已通过闸门的高难度镜头需要Seedance提示词骨架 | [20 高难度Seedance模板](knowledge-20-seedance-advanced-shot-templates.md) | 按当前角色、镜头、路线和平台合同重写模板 |
| 用户明确要求一镜到底，或剧情适合实时连续行动 | [21 一镜到底实现指南](knowledge-21-long-take-guide.md) | 判断真/伪一镜、规划路径、接缝与连续性 |
| 已通过长镜头闸门并进入Seedance提示词编译 | [22 一镜到底Seedance模板](knowledge-22-seedance-long-take-templates.md) | 绑定CAM节点、分段箭头、末帧锚点与执行素材 |

## 3. 调用约束

- 先分析剧情与镜头功能，再查资料；不得从词典反向堆砌剧情。
- 每个镜头只选择能改变画面的必要参数，避免同时调用相互冲突的运镜、焦距、景深和构图。
- 将资料中的绝对表述视为经验提示，结合当前模型、素材和实际测试判断。
- 平台专属资料只在用户使用该平台或明确要求比较时读取；普通 Seedance 任务不得加载 Runway 或竞品参数。
- 物理接触方案是失败风险较高时的备选，不得擅自改变剧情烈度或删除用户要求的动作结果。
- 分镜图中的路线仍使用仓库既定的 `CAM / ACT / GAZE / FOCUS / LIGHT / READ` 语法、分段节点和逐段箭头；知识库只辅助选择路线，不修改标注合同。
- 角色身份仍以永久 `CHAR-ID`、独立多视角角色板和镜头绑定清单为准；案例角色描述不得进入当前剧本。
- 13字段大表是可选扩展交付；实际执行仍必须补充 `USE / REFERENCE-ONLY / SKIP`、角色ID、分镜页和执行素材映射，案例插入镜号不得直接作为最终镜号。
- 高难度镜头不得由资料反向触发；只有剧情或用户明确需要且通过叙事、空间、物理、身份和复杂度闸门时才调用，否则拆镜或降级。
- 一镜到底必须明确是真一镜还是伪一镜；伪一镜逐接缝记录末帧、遮挡、运动方向与状态锚点，每个独立生成任务仍遵守当前4–15秒合同。

## 4. 资料清单

- [01 分镜工作流引擎—方法论总结](knowledge-01-storyboard-workflow.md)
- [02 镜头语言基础—景别、角度、构图](knowledge-02-shot-language-basics.md)
- [03 运镜技术百科—16 种核心运动](knowledge-03-camera-movement-encyclopedia.md)
- [04 AI 视频运镜控制—提示词工程](knowledge-04-ai-camera-prompting.md)
- [05 视觉叙事法则—剪辑、轴线、节奏](knowledge-05-visual-narrative-editing.md)
- [06 光影与色彩—AI 电影级光控](knowledge-06-lighting-and-color.md)
- [07 AI 生成物理接触规避方案库](knowledge-07-physical-contact-workarounds.md)
- [08 竖屏 9:16 构图与短剧导演专项](knowledge-08-vertical-9x16.md)
- [09 AI 导演提示词工程参数字典](knowledge-09-director-prompt-dictionary.md)
- [10 电影调度—Blocking 与 Staging](knowledge-10-blocking-and-staging.md)
- [11 景深控制—Depth of Field](knowledge-11-depth-of-field.md)
- [12 镜头构图法则—Shot Composition](knowledge-12-shot-composition.md)
- [13 Seedance 2.0 AI 视频生成工具指南](knowledge-13-seedance-2-guide.md)
- [14 Runway Gen-4 运镜控制提示词指南](knowledge-14-runway-gen4-camera-guide.md)
- [15 AI 视频工具运镜能力对比选型](knowledge-15-video-tool-comparison.md)
- [16 AI短剧分镜大表—完整字段词典与规范](knowledge-16-shot-table-schema.md)
- [17 分镜大表实战示例—局部全表映射案例](knowledge-17-shot-table-case-study.md)
- [18 状态变化追踪系统—连续性与块间指令](knowledge-18-state-change-tracking.md)
- [19 AI高难度运镜与难镜头技术库](knowledge-19-advanced-camera-techniques.md)
- [20 AI高难度镜头—Seedance提示词模板](knowledge-20-seedance-advanced-shot-templates.md)
- [21 AI一镜到底—长镜头实现指南](knowledge-21-long-take-guide.md)
- [22 AI一镜到底—Seedance提示词模板](knowledge-22-seedance-long-take-templates.md)
