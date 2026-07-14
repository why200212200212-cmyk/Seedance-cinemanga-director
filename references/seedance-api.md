# Seedance API 执行契约

仅当用户明确要求实际生成、已配置凭证并理解可能产生费用时，才调用 API。只请求提示词或分镜时不要创建任务。

## 当前接口

- 鉴权：`Authorization: Bearer $ARK_API_KEY`。
- 创建：`POST /api/v3/contents/generations/tasks`。
- 查询：`GET /api/v3/contents/generations/tasks/{id}`。
- 取消：`DELETE /api/v3/contents/generations/tasks/{id}`。
- 创建必填字段：`model`、`content`；模型 ID 或推理接入点 ID由用户账户决定，不在 Skill 内锁死。
- 任务状态：`queued`、`running`、`succeeded`、`failed`、`cancelled`；成功结果读取 `content.video_url`。

## 素材映射

便捷模式把可复制视频提示词作为第一个 `text` 内容项，再按用户给定顺序追加 `image_url`。提示词中的“图片1、图片2……”必须与该顺序严格一致，不要把本地资产 ID 或文件名冒充为模型可见编号。

需要官方新增或账户特定的多模态字段时，使用 `--content-json` 透传官方 `content` 数组，不猜测字段。先用 `--dry-run` 检查最终请求体。

## 运行边界

- 创建请求不自动重试，避免网络不确定时重复创建付费任务。
- 查询遇到 429 或 5xx 可有限重试。
- API 密钥只从环境变量或本地 `.env` 读取，不写进提示词、日志、仓库或示例。
- 实际运行前确认模型权限、分辨率、时长、画幅、音频、参考素材数量和账户配额；未知能力不凭空承诺。
- 只把“可复制视频提示词”提交给生成端，不提交导演审阅说明、状态账本或内部检查记录。

完整命令与官方文档入口见 `docs/api-integration.md`。
