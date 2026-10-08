# 仓库研究与维护协议

适用于本仓库中的人类与 AI 协作者；`literature/AGENTS.md` 提供文献研究的额外约束。

## 先读什么

1. `README.md` 确认项目目标与目录入口。
2. `synthesis/current-position.md` 获取**当前唯一的综合结论 authority**。
3. `synthesis/README.md` 找最新已合入的 frontier 与 handoff。
4. 进入 `research/` 或 `literature/` 之前先看该目录的导航文件。

不要把历史文档的强断言当成今天的研究结论。尚未纳入 `synthesis/current-position.md` 的新研究材料，也不能自动视作当前结论。

## 研究边界

- 严格区分 ordinary first-personhood、phenomenal mineness、irreducible first-person fact 与 absolute privilege。
- 同时保留 C0（subject-neutral）、C1（plural first-person）、C2（singular centered）作为竞争理论。C2 是原始 target，不能预设它为真。
- 一个支持 C2 的新证据，应当检查其独立性及 C0/C1 能否自然容纳。
- 清晰标记**定义、前提、条件性推论、形式一致性、形而上学可能性、实证证据**；不能把它们当成同一强度的结果。
- 不把语义评价点的单中心性直接等同于完整现实的本体论单中心性；涉及这个桥梁必须写出额外前提。
- 不因术语重新命名或同一结论的新文件数量而升级证据强度。

## 文档职责和状态

| 位置 | 写什么 | 地位 |
| --- | --- | --- |
| `concepts/` | 工作定义与术语 | 定义，允许修订 |
| `research/questions/` | 问题与判别标准 | 开放 |
| `research/arguments/` | 前提、推导、反例与限制 | 独立论证，不自动成定论 |
| `research/models/` | 候选模型及其成本 | 假说/条件模型 |
| `literature/candidates/` | 搜索候选 | 未经完整核验 |
| `literature/*.md` | 文献分析与来源 | 必须记录阅读级别 |
| `synthesis/frontier-*.md` | 某时点的研究前沿 | 历史快照；后续可覆盖 |
| `synthesis/handoff-*.md` | 下一轮任务交接 | 时效性记录 |
| `synthesis/current-position.md` | 当前综合立场 | **唯一 authority** |
| `journal/` | 按时间顺序记录变化 | 历史事实，不自动代表当前立场 |

新论证至少交代：**target、显式前提、得到的结果、适用边界、尚未解决的问题、与旧结果的关系**。建议在开头标记“工作模型 / 条件性结果 / 反例 / 未证”等状态。

## 改动流程

1. 先检查当前 `main` 和相关已有文档；优先扩充既有问题，不无故重复开新 frontier。
2. 实质研究变更先写进 `research/`；只在明确改变综合判定时再更新 `synthesis/current-position.md`，同时同步首页和 handoff。
3. 旧稿原则上保留；通过导航或 `Superseded by` 说明新旧关系。批量重命名/移动必须同时维护全部相对链接。
4. 新文献先按 `literature/AGENTS.md` 核验，不能把机器候选直接当成论证证据。
5. 运行 `python tools/check_repo.py`；链接或 JSON 检查失败时先修复再合入。
6. 默认直接在 `main` 提交经过检查的改动，不主动创建分支或 PR；未经用户要求，不直接重写既有研究结论或删除历史记录。

本文件规范工作流，**不替代** `synthesis/current-position.md` 的哲学结论。
