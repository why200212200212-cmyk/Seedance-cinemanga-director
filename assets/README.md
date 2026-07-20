# Visual Assets

本目录存放仓库文档展示图，不参与 Skill 运行。

## 资产清单与推荐位置

### 1. 主视觉装饰

- `cover-banner.png`：仓库封面主视觉，推荐放在 `README.md` 顶部；
- `skill-preview.png`：完整技能预览总览，推荐放在 README 的“视觉预览”区域；
- `feature-overview.png`：双影视引擎、核心规则与输出模式的功能总览。

### 2. 架构说明图

- `system-architecture.png`：系统架构总览，推荐放在 `README.md` 的“系统架构总览”和 `docs/architecture.md`；
- `workflow-architecture.png`：十阶段导演工作流与仓库结构详图。
- `knowledge-routing-map.png`：剧情分析后按镜头问题选择参考知识的路由图，推荐放在知识库与架构说明处；
- `seedance-multimodal-binding.png`：独立角色板、场景、分镜、运镜与音频参考的执行素材绑定图，推荐放在Seedance工作流说明处。
- `multi-fighter-action-system.png`：多人动作角色图、空间拓扑、动作节拍、套路结构、摄影与安全边界总览，推荐放在README和架构文档的动作导演模块处。
- `cinematic-department-review-system.svg`：九部门共享镜头事实、PERF表演合同、九项冲突闸门与最终提示词编译流程；采用确定性矢量文字，推荐放在README的九部门会审说明处。
- `color-palette-reference-example.svg`：STRICT-13结构化色卡、P编号/HEX/职能/对象及REFERENCE-ONLY COLOR引用示例；推荐放在色卡工作流说明处。
- `palette-neon-dressing-room-example.svg`：粉紫霓虹化妆间GUIDED-10色卡，标明环境色、人物光、肤色保护与色彩职责。
- `palette-palace-night-example.svg`：宫廷夜戏STRICT-10色卡，标明暗部、朱红、烛光、服装与生物材质的约束。
- `palette-mojia-flight-example.svg`：云海墨家飞行器STRICT-12色卡，标明云层、朝晖、木/铜机关、人物服装和邀请函的绑定。
- `shot-contract-lighting-blocking-example.svg`：把世界/摄影机/屏幕坐标、人物站位、遮挡链、环境光、人物光和PERF因果收敛到同一镜头合同。

### 3. 分镜板示例图

- `storyboard-example.png`：标准六镜分镜执行板示例；
- `nine-grid-example.png`：九宫格分镜示例；
- `twenty-five-grid-example.png`：二十五格分镜示例。
- `adaptive-storyboard-workflow.png`：剧情分析到标准、九宫格、二十五宫格和智能宫格的自适应分流；
- `ai-readable-camera-routes.png`：CAM、ACT、GAZE、FOCUS、LIGHT、READ路线与箭头图例。
- `segmented-camera-path.png`：分段运镜节点、逐段箭头、转向后方向和俯视/侧视同步路线。

适合放在 README 的“分镜板示例资源”部分，作为用户理解输出形态的视觉样例。

### 4. 功能资产板

- `icons-board.png`：小图标资产板，适合用于 README 的“文档资产与装饰图标”；
- `prompt-output-system.png`：单条与多条提示词交付结构图；
- `visual-assets-qa.png`：视觉资产与连续性质检总览。
- `character-differentiation-board.png`：不同角色结构性面部差异的文档说明图；仅作对比与装饰，不替代运行时每个角色的独立角色板。
- `live-action-performance-example.png`：真人近景的刺激—反应、眼神、气息、手部、倾听、人物光与胶片质感示例。
- `3d-cinematic-performance-example.png`：3D角色眼神、重心、机械足接触、材质与衣发次级运动示例。

## 放置原则

1. **主视觉放顶部**：用于提升识别度与品牌感；
2. **架构图放说明区**：用于讲清工作流和 Skill 结构；
3. **示例图放示例区**：用于说明九宫格、二十五格和执行板等输出板式；
4. **图标板放文档尾部或模块说明区**：用于装饰与功能索引。
5. **知识库与绑定图放架构区**：只解释调用和素材关系，不作为运行时输入图片。
6. **动作模块图放专项说明区**：用于解释FTR/ZONE/ACT与动作节拍，不作为现实格斗训练或现场特技执行图。
7. **会审、色卡、镜头合同与表演示例放对应说明区**：它们解释编译规则和质量目标，不自动进入用户项目的API执行素材清单。
8. **分镜双层严格分开**：REVIEW资产用于识别CAM/ACT/GAZE/FOCUS/LIGHT/READ；视频生成只提交选中的PANEL-ID-CLEAN，不提交制作标记。

所有 PNG 均为内容唯一文件；流程图与色卡使用SVG确保部门名称和HEX可精确读取。仓库不保留逐字节相同的兼容别名，以减少克隆和安装体积。
