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

## 放置原则

1. **主视觉放顶部**：用于提升识别度与品牌感；
2. **架构图放说明区**：用于讲清工作流和 Skill 结构；
3. **示例图放示例区**：用于说明九宫格、二十五格和执行板等输出板式；
4. **图标板放文档尾部或模块说明区**：用于装饰与功能索引。
5. **知识库与绑定图放架构区**：只解释调用和素材关系，不作为运行时输入图片。

所有 PNG 均为内容唯一文件；仓库不保留逐字节相同的兼容别名，以减少克隆和安装体积。
