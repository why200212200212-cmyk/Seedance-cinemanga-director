# Visual Showcase Placement Guide

本页说明新增图片在 Skill 仓库中的最佳落位，用于“装饰 + 示例”双重用途。

## 推荐落位

### README 顶部

- `assets/cover-banner.png`
- 作用：建立项目识别度，作为仓库封面横幅。

### README / 视觉预览

- `assets/skill-preview.png`
- 作用：一图概括仓库结构、核心模式、核心规则、输出模块和文档资产。

### README / 系统架构总览

- `assets/system-architecture.png`
- 作用：展示从输入材料到连续性质检的完整流程。

### README / 按需知识库与 Seedance 素材绑定

- `assets/knowledge-routing-map.png`：展示剧情分析后如何只加载当前镜头需要的参考资料；
- `assets/seedance-multimodal-binding.png`：展示独立角色板、场景、分镜页、可选运镜参考与音频参考的绑定和SKIP过滤。
- 作用：解释知识调用与运行时素材边界；两图都只用于文档展示，不提交生成端。

### README / 深度架构与质量说明

- `assets/workflow-architecture.png`：十阶段导演工作流与仓库结构；
- `assets/prompt-output-system.png`：单条、多条与尾帧接力输出；
- `assets/visual-assets-qa.png`：视觉资产与连续性质检；
- `assets/feature-overview.png`：双影视引擎、核心规则和交付能力总览。

### README / 分镜板示例资源

- `assets/storyboard-example.png`
- `assets/nine-grid-example.png`
- `assets/twenty-five-grid-example.png`
- `assets/adaptive-storyboard-workflow.png`
- `assets/ai-readable-camera-routes.png`
- `assets/segmented-camera-path.png`
- 作用：让用户直观看到标准分镜板、九宫格、二十五格、智能宫格，以及AI可辨识的运镜/动作/视线/焦点/光线/阅读路线语法和分段转向后的后续方向。

### README / 角色身份与差异化

- `assets/character-differentiation-board.png`
- 作用：展示不同角色的结构性面部差异和多视角设计概念。此图仅作说明；实际运行必须一名角色一张独立角色板。

### README / 文档资产与装饰图标

- `assets/icons-board.png`
- 作用：提供统一的功能图标风格，可作为模块装饰和视觉索引。

## 适合的文档用途

1. **装饰用途**：
   - 封面主视觉
   - 分区头图
   - 模块引导图

2. **示例用途**：
   - 板式参考
   - 输出样例
   - 结构说明
   - 视觉语言库

## 不建议的用途

- 不要把这些图片直接嵌入 `SKILL.md` 的核心规则正文中，避免运行时上下文被文档装饰内容污染；
- 不要把图片当成唯一说明来源，关键规则仍应保留文字版；
- 不保留逐字节相同的图片别名；公开前使用内容哈希去重。
