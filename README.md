# self

关于**第一人称、绝对第一人称、I–NOW 与现实结构**的个人哲学研究。

起点是一个问题：

> 为什么偏偏是这个人、这个时代、这个当前经验？

这是开放研究：目前既没有证明存在唯一绝对第一人称，也没有证明它不存在。仓库保存候选理论、支持与反驳、文献证据，以及结论如何变化的过程。

## 研究地图

| 代号 | 候选理论 | 简述 |
| --- | --- | --- |
| **C0** | Subject-Neutral Actuality | 现实可以包含多个意识主体，但 actuality 无须不可还原的第一人称实现方式 |
| **C1** | Plural First-Person Actuality | 现实可包含多个不可还原的第一人称实现方式，无全局特权中心 |
| **C2** | Singular Centered Actuality | 完整现实具有唯一的绝对第一人称 opening / orientation |

最初研究目标是 **C2**。目前 C0、C1 均未被排除。现阶段最大的困难是：**第一人称事实依赖视角，为什么意味着整个现实只能有一个绝对中心？**

最新已合入的前沿是 [Evaluation-Locus Cardinality Gap](synthesis/frontier-2026-10-05-evaluation-locus-gap.md)。核心问题涉及 MEP（Monocentric Evaluation Principle）与多中心现实模型；形式模型的存在本身不算对其形而上学真实性的证明。

## 从哪里读起

1. **[当前研究立场](synthesis/current-position.md)**：当前有效结论、开放问题和证据强度；发生冲突时以它为准。
2. **[面向读者的核心论证](synthesis/core-argument-neutral-vs-centered-actuality.md)**：理解原始问题与研究进程。
3. **[最新前沿](synthesis/frontier-2026-10-05-evaluation-locus-gap.md)**：仍未跨越的关键推理。
4. **[下一轮研究交接](synthesis/handoff-2026-10-05-evaluation-locus.md)**：下一步任务与旧路线边界。

按主题浏览：

| 目录 | 职责 |
| --- | --- |
| [concepts/](concepts/) | 基础概念和术语区分 |
| [research/](research/README.md) | 原创问题、[论证](research/arguments/README.md)、[模型](research/models/README.md) |
| [literature/](literature/README.md) | 外部文献、核验层级和自动检索 |
| [synthesis/](synthesis/README.md) | 当前立场、阶段前沿、历史交接 |
| [journal/](journal/README.md) | 按日期保留的研究轨迹 |
| [tools/](tools/) | 文献检索和仓库检查脚本 |

## 阅读与维护约定

- **权威层级**：`synthesis/current-position.md` ＞ 最新已合入 frontier ＞ 原创论证/模型 ＞ 旧 frontier 与 handoff。日期新不自动意味着论证强。
- **历史不删除**：旧模型、旧前沿即使被修正，也保留为研究记录；以状态说明和导航区分。
- **证据与假设分离**：一个形式上可构造的模型，并不因此获得本体论真实性；文献摘要也不等于全文证据。
- **研究草稿独立于结论**：新结果未经审查并同步到 `synthesis/current-position.md` 前，不自动更新当前 authority。

维护细则见 [AGENTS.md](AGENTS.md)，文献流水线见 [literature/pipeline.md](literature/pipeline.md)。用 `python tools/check_repo.py` 检查本地 Markdown 相对链接及 JSON 格式。
