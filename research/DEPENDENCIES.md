# 论证依赖图 · 2026-10-08

> **用途**：把“逻辑推导”“形式语义模型”“本体论假设”“证据竞争”分别标出，避免旧笔记将后者误写成已获得的定理。  
> 权威判断：[current-position](../synthesis/current-position.md)；全量文件初审：[REVIEW](REVIEW-2026-10-08.md)。

## 1. 总理论空间

| 竞争理论 | 需要增加的不可还原承诺 | 目前最强模型 | 目前最大缺口 |
| --- | --- | --- | --- |
| **C0** | 无须 actuality-level FP mode；允许 ordinary consciousness | [Neutral Actuality Core](models/neutral-actuality-core.md) | 迄今无 neutral incoherence / 独立 FP arity witness |
| **C1** | 多个 ontic first-person obtaining modes + one actual totality | [Plural Opening Manifold](models/plural-opening-manifold.md) | mode irreducibility、MPGC compatibility、global unity |
| **C2** | 一份 reality 的唯一 global opening role / I–NOW orientation | [Role-First Opening](models/role-first-absolute-opening.md) | 必须排除 C0 和 C1；独立 unique privilege witness 尚无 |

“在一个模型内给定原始项”与“该项不可替换且真实存在”是不同证明任务。

## 2. 从第一人称评价到全球唯一性

```mermaid
flowchart TD
    PV["Perspective variance"] --> IDX["需保留 perspective sensitivity"]
    MEP_S["MEP-S：单点 centered 评价"] --> POINT["SPC-pointwise：交集语义"]
    POINT --> FPNC["Pointwise FPNC：不同 complete perspectives 可互斥"]
    IDX -. "不足以推出" .-> MEP_O["MEP-O：完整现实只有一个 fundamental FP mode"]
    POINT -. "本身不足以" .-> GCR["GCR：global facts 反映到同一评价点"]
    UNITY["待证：独立的 actuality-unity / truthmaker 标准"] --> GCR
    GCR --> GLOBAL["全球单中心的互不相容性"]
    LE["LE：同一视角内的排他性"] --> GLOBAL
    FPNC --> GLOBAL
    GLOBAL --> ATMOST["At most one opening"]
    ALO["ALO：至少一个不可还原 opening（待证）"] --> EXACT["Exactly one opening"]
    ATMOST --> EXACT
```

**箭头类型**：

- 实线：在节点写明的定义/额外前提下可做的条件性推导；不代表该前提为真。
- 虚线：无法凭源节点独立证明目标；这是需要被修补的**缺口**，不是已经存在的蕴涵。
- **MEP-O** 已把 one-mode cardinality 写进本体论断言；若直接采用，只能是 C2 的前提，不能重复计算为 C2 的独立证明。

最容易混淆的三步：

1. \(MEP\text{-}S\) 给一个中心的评价点（**语义**）。
2. \(\varphi_a\land\varphi_b\) 在一个评价点无解（**pointwise**）。
3. 整个现实无法具有两个 genuine openings（**本体论**）。

第 2 到第 3 步需要 **GCR 与关于跨中心互斥事实的附加条件**。参考 [Pointwise–Polycentric](arguments/pointwise-polycentric-reflection-audit.md)、[SPC](arguments/perspective-closure-principle.md)、[USL](arguments/unitary-singularity-lemma.md)。

## 3. C1 反模型审计链

```mermaid
flowchart TD
    POLY["两个 centered loci + shared history"] --> DSTR["Distributed satisfaction：可形式建模"]
    DSTR --> COUNTER["反例：MEP-S 不推出 GCR"]
    DSTR --> NEED["仍需候选本体论额外承诺"]
    NEED --> IRE["T2：mode facts 是否 irreducible"]
    NEED --> UNI["T3：一个 actual totality 的统一标准"]
    NEED --> COM["T4：cross-mode objective compatibility"]
    IRE --> C1["C1 ontological adequacy：仍开放"]
    UNI --> C1
    COM --> C1
```

**形式反模型的强度**：在给定语义/结构公理下，通过 pointwise non-compossibility 与 distributed satisfaction 的联合构造；它没有自动建立不可还原性或所有完整性条件。

| 必要验证 | 当前状态 | 主要依据 |
| --- | --- | --- |
| 单点评价不蕴涵全球单中心 | **已有明确有限形式反例** | [MEP-S/GCR 审计](arguments/pointwise-polycentric-reflection-audit.md) |
| mode essentiality ⇒ ontic non-reduction | **没有独立证明**；定义或 primitive | [Plural Model](models/plural-opening-manifold.md) |
| shared history + one A ⇒ metaphysical one-actuality unity | **没有独立完成** | [Pointwise Audit](arguments/pointwise-polycentric-reflection-audit.md) |
| 每个 \(F_i\cup W\) 分别一致 ⇒ 全体一致 | **一般不成立**；需要额外 compatibility | [Pointwise Audit](arguments/pointwise-polycentric-reflection-audit.md) |
| C1 在 List 的论域中应如何分类 | **作为 one-world fragmentalist/pluralist horn 仍可研究** | [FPNC Audit](arguments/first-person-non-compossibility-audit.md) |

## 4. C2 完成条件与证据依赖

```mermaid
flowchart TD
    C2["C2：Singular Centered Actuality"]
    A["前置：存在 actuality-level first-person arity"] --> C2
    S["前置：只有一个 globally privileged mode"] --> C2
    A --> C0F["必须击败 C0：neutral actuality"]
    S --> C1F["必须击败 C1：plural first-person actuality"]
    C0F --> X["独立 witness X / 解释优势"]
    C1F --> X
    X --> VERDICT["改变当前结论（尚未达成）"]
```

支持 C2 的 datum \(X\) 应满足

\[
Independent(X)\land NaturalFit(C2,X)
\land\neg CheapNonSingularAccommodation(X).
\]

目前并无通过全部环节的 \(X\)。[Non-Singular Accommodation Test](arguments/neutral-accommodation-test.md) 给判别规则；[Completion Underdetermination](arguments/completion-underdetermination-result.md) 和 [Primitive Replacement](arguments/primitive-actuality-replacement-test.md) 是旧审计结果。

## 5. 已归入条件或下游的依赖簇

| 问题簇 | 条件或前置门槛 | 当前定位 |
| --- | --- | --- |
| Subject unity → global subject | 强 unity / subject-individuation theory；不能凭多个 local modes 自动得到 | [Global Unity](arguments/global-experiential-unity-audit.md)；[Bearer Discrimination](arguments/bearer-discrimination-principle.md) |
| Global subject → privileged local event | 需要独立 localization / privilege principle | [Global Subject Localization](arguments/global-subject-localization-quadrilemma.md) |
| Presence / NOW → absolute I–NOW | 需要本体的 PresenceSimpliciter 及其 singularity | [Presence Closure](arguments/presence-route-four-way-closure.md) |
| Symmetry / unique structural point → privilege | symmetry constraints 仅约束 non-haecceitistic structural selector | [No Natural Pointing](arguments/no-natural-pointing-theorem.md) |
| Stochastic / process → absolute center | 需要额外 privilege bridge 和时间结构 | [Stochastic Law](arguments/stochastic-absolute-orientation-law.md) |
| C2 → Selective Local vs Universal-I → trajectory | C2 上游尚未确立；不可反向用下游精致程度证明它 | [Locality](arguments/locality-from-subject-unity.md) |

## 5.1. 2026-10-08 的补充推导与模型检验

[进一步 GCR 审计](arguments/gcr-unity-principle-audit.md) 已给：

\[
OCC+SEP+GCR_2\Rightarrow AtMostOne,\qquad
AtMostOne+ALO\Rightarrow ExactlyOne.
\]

还确认 \(GCR_2\not\Rightarrow GCR_{All}\)：pairwise supports 可以两两相交却全体交集为空。共享 history、因果互动、甚至单一共同 truthmaker 也需要额外条件才能产生 GCR。

[C1 跨模式审计](models/mode-amalgamation-neutral-reduct.md) 则明确：

- **固定 objective assignment + 各 private vocabularies 可联合延拓 + 无冲突跨模式约束** ⇒ 形式 SAT；
- **各局部分别 SAT** ⇏ **全局 SAT**（共享 objective variable 或跨模式规则可冲突）；
- neutral projection \(N_0\) 不可恢复 local values；enriched \(N_+\) 可以编码 local values。两者都不足以给出 ontic non-reducibility / reduction theorem。

[代码](../tools/model_audit.py) 和 [回归测试](../tests/test_model_audit.py) 固定这些**有限的形式实例**，不能替代哲学论证。

## 5.2. U3/U4 的新依赖与 C1 的 neutral baseline

\[
GlobalCoConsciousCover
\xrightarrow{+MI,\;realization} OneMode
\xrightarrow{+Reflection} GCR,
\]

其中第一箭头是显式条件证明；第二箭头仍属假说，可能需要额外的 centered truthmaking 条件。一个 global mode 本身也没有保证 singular privileged local I–NOW。

\[
OneUltimateActualizer
\xrightarrow{+AIM} OneMode,
\]

AIM（同一实际化源头只产生同一第一人称模式）尚未获得非循环论证。纯粹 \(\forall F\exists\pi\) 不蕴涵 \(\exists\pi\forall F\)。

C1 / C0 比较新增强中立基底 **B1**（共享客观历史 + 所有主体的 local phenomenality、心理物理关系）；只有在清楚指定 metaphysical possibility class 与 fact identity / grounding 后，才能评价 B1 是否使 C1 的 modes 可还原。有限非决定性结果不等于形而上学独立性证明。

参见 [U3](arguments/co-conscious-unity-to-mode-audit.md)、[U4](arguments/actuality-quantifier-scope-audit.md)、[B1 grounding](models/neutral-contrast-grounding-audit.md) 与 [可执行模型](../tools/model_audit.py)。

## 6. 开放依赖关口与停止条件

| ID | 目标 | 不能当作证明的替代品 |
| --- | --- | --- |
| **G1** | 独立辩护 U3-MI 与 U4-AIM（U0–U2 不足，定义循环需排除） | centered-world 交集的重新书写 |
| **G2** | 相对于包含 local phenomenality 的 B1，验证 mode fact identity、admissible worlds 与 grounding | 单纯把 mode 设为 primitive |
| **G3** | MPGC 的 shared facts 与 cross-mode 逻辑规范 | 两个 local sets 各自 consistent |
| **G4** | C0/C1/C2 同尺度 explanatory comparison | 单纯原始符号的数量、旧论文/论证的数量 |
| **G5** | 找到能抵抗 C0 与 C1 的新 witness | 现象学强烈感受或“为什么是我”的疑问本身 |

**默认顺序 G1 → G2/G3（可并行）→ G4/G5。** 没有给其中任一条提供可复核的实质内容，就不要创建新的“突破”文件或宣称 C2 已得证。
