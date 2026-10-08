# Pointwise Evaluation vs Polycentric Actuality — MEP Bridge Audit

> 日期：2026-10-08  
> 状态：strict stress test；**未证明 C1 为真，也未证明 C2 为假**。  
> 基于：evaluation-locus-cardinality-gap、plural-opening-manifold、current-position。

## 0. 结论

仓库之前的 Evaluation-Locus Cardinality Gap 方向成立，但需要更精确地表述：

1. **单中心评价点**与**单中心完整现实**是不同层次的命题。
2. 一个有限的两视角结构可以同时满足：每次第一人称评价只使用一个视角、两个第一人称命题不能在同一点合取、只有一个 global actuality carrier、两个视角各自具有局部事实。这为「从语义 pointwise 性质推出整个现实唯一中心」提供**条件反模型**。
3. 反模型还没有证明两个模式的 obtaining 在本体论上不可还原。旧模型 FP2、FP3、FP4 对此主要采用了**原始设定或否定性声明**。
4. 「所有 mode 分别与 W 相容」也不足以保证完整结构满足任意 cross-mode/global bridge constraints。
5. 因此 C1 获得的是 **typed semantic / axiomatic consistency witness**；其 ontic irreducibility、one-actuality unity 与 non-neutralizability 仍是开放问题。

这不是对 Christian List 的 quadrilemma 的反驳：他的 many-worlds 与 fragmentalist alternatives 已把选择空间摆出。本文反对的是**把 centered-point 形式化直接提升为 C2 的全球唯一性定理**。

## 1. 拆分 MEP

### MEP-S — Semantic Pointwise Monocentricity

给定标准 first-person centered evaluation domain：

\[
D_C=\{ \langle\omega,\pi\rangle:\omega\in\Omega,\pi\in\Pi(\omega)\}.
\]

每个评价点 \(\langle\omega,\pi\rangle\) 恰好携带一个 \(\pi\)。

这是一项关于**命题评价点的类型**的限制。它与一个现实内存在多个 conscious subjects 并不冲突。

### MEP-O — Ontological Monocentricity of Complete Actuality

\[
\forall R[Actual(R)\Rightarrow
|\operatorname{FundamentalFirstPersonModes}(R)|=1].
\]

它声称一个完整的实际现实只能有一个 fundamental first-person obtaining mode。

这比 MEP-S 强得多；它排除 C1，也不能仅由对 indexical propositions 采用单视角评价点而得到。此式还预设 actuality 必有 first-person mode；C0 不接受这一前提。

### GCR — Global-to-Centered Reflection

另一个值得明确写出的桥梁是：

\[
GCR:\quad
\forall R,F,G[
Actual(R)\land F,G\in FP(R)
\Rightarrow
\exists\pi\;(\langle R,\pi\rangle\models F\land G)].
\]

含义：共同属于一个实际现实的 first-person facts，必须能够在**同一个** centered evaluation point 联合为真。

**MEP-S 不推出 GCR。** 若用「在同一个 centered point 有非空交集」定义 compossibility，则 GCR 对这种 compossibility 当然成立；但仍需论证「共同属于同一个 actual reality」为什么等于该 compossibility。

因此：MEP-S + intersection semantics 得到的 SPC，是关于*pointwise compossibility*的结果；若要把它用于*global actuality*的唯一性，需要 GCR 或等价的 metaphysical reflection/unity premise。

## 2. 有限两视角反模型：语义上明确可满足

设：

\[
\Omega=\{w\},\qquad \Pi(w)=\{a,b\}.
\]

一个共同的 objective history \(w\) 包含两个主体，分别处于互斥的 complete token states \(X,Y\)：

\[
State_w(a)=X,\quad State_w(b)=Y.
\]

第一人称命题 \(\varphi_X=\text{“I am in }X\text{”}\) 和 \(\varphi_Y=\text{“I am in }Y\text{”}\) 的外延设为：

\[
\llbracket\varphi_X\rrbracket=\{(w,a)\},
\qquad
\llbracket\varphi_Y\rrbracket=\{(w,b)\}.
\]

因此：

\[
\llbracket\varphi_X\rrbracket\cap\llbracket\varphi_Y\rrbracket=\varnothing.
\]

标准 pointwise non-compossibility **完全保留**。

再构造一个 total structure：

\[
R=\langle w,\{(w,a),(w,b)\},F_a,F_b,A\rangle,
\]

赋予**一个** global actuality status：

\[
Actual(R),\qquad
\neg\exists R'\neq R\;Actual(R').
\]

并规定：

\[
R\models_{\rm distributed}
\varphi_X@a\;\wedge\;\varphi_Y@b,
\]

但：

\[
\neg\exists \pi\in\{a,b\}\;
\langle w,\pi\rangle\models
\varphi_X\wedge\varphi_Y.
\]

所以：

\[
MEP\text{-}S + OneActuality +
DistributedSatisfaction \not\Rightarrow GCR.
\]

这一模型没有 cross-perspective logical explosion；两个互斥 token states 也没有落在同一 perspective 上。

**证据边界**：这里的 \(Actual(R)\)、mode facts \(F_a,F_b\) 以及 distributed-satisfaction relation 是所构造模型的 primitive clauses。形式满足性本身没有证明它们对应 fundamental irreducible metaphysical obtaining，也没有证明唯一 global actuality 的身份标准完全合理。因此此处不能宣称已经给出“C1 的全部形而上学可满足性证明”。

## 3. 三种判别测试

| 测试 | 旧模型给出的内容 | 严格判断 |
| --- | --- | --- |
| T1：pointwise uniqueness 是否推出 global uniqueness？ | 同一现实下多个 centered loci | **不能直接推出**，形式反模型通过 |
| T2：多元 facts 是否不可还原地 obtain？ | mode 写入 fact identity；否认与第三人称 paraphrase 同一 | **未证明**，仍属本体论 primitive |
| T3：一个实际现实是否真的容纳这些 facts？ | 声明一个 A、一个 W，提出 MPGC | **条件成立**，但独立的 global unity 与 cross-mode constraints 待审计 |

### T2 的关键非蕴涵

\[
\text{metalanguage uses }m\Vdash F
\not\Rightarrow
\text{metaphysically irreducible obtaining mode}.
\]

说 \(\Vdash\) 是 metalanguage notation、而非 object-language predicate，不能独立证明 \(m\) 是现实的不可还原组成部分。

不过反方向也不成立：**可以在第三人称元语言里编码、讨论一个事实，不等于已经把它 metaphysically reduced / grounded in neutral facts。** 需要正面的 ground / individuation / completeness 分析，不能以表述形式直接裁决。

原 FP2（mode essentiality）与 FP3（拒绝 invariant paraphrase identity）至多将不可还原性**作为理论承诺清楚写出**；这对构造一致的候选本体论有用，但不能当成支持其真实性的独立结果。

### T3 的隐藏条件：局部一致性不保证整体一致性

从：

\[
Consistent(F_a\cup W)\land Consistent(F_b\cup W)
\]

不能一般性推出：

\[
Consistent(F_a\cup F_b\cup W).
\]

反例：当 \(W\) 对一个共享 objective claim \(Q\) 未作决定，而 \(F_a\) 包含对 \(Q\) 的非索引断言、\(F_b\) 包含对 \(\neg Q\) 的非索引断言时，两个局部集合可分别一致，合并后却冲突。

因此 MPGC 至少需要 explicit **objective-invariance / cross-mode compatibility** condition，区分 mode-relative opposition 与 shared objective contradiction；有共同 history 和分模式类型并不足以在所有 extension 中保证这一点。

## 4. 对 List 的准确定位

List 的 centered-world 形式化明确以单一 \(\pi\) 来评价 first-person propositions，由此得到 complete first-person perspectives 的 empty-intersection result。他另外区分 many first-personally centered worlds 与 one fragmented world 等选择。

故本文不声称 List 隐藏了一个他自己没有讨论的“全现实唯一主体”公理。更准确的项目内部结论是：

**单点 centered-world semantics 可以服务于 List 的 non-compossibility 论证；把这个论证用于排除 C1、支持项目特有 C2 时，必须追加 global-to-pointwise reflection/unity principle。**

参考：
- Christian List, “A Quadrilemma for Theories of Consciousness”, *The Philosophical Quarterly* 75(3), 2025. https://doi.org/10.1093/pq/pqae053
- Martin A. Lipman, “Subjective Facts about Consciousness”, *Ergo* 10, 2023. https://doi.org/10.3998/ergo.4649

## 5. 当前 verdict 与下一步

- **成立的反例**：对 \(\text{PerspectiveVariance}+\text{MEP-S}+\text{OneActuality}\Rightarrow \text{global single center}\) 的无桥梁推理。
- **尚未成立的主张**：已经证明 C1 的 irreducible modes 不可 third-personize，或已经证明它的 one-actuality unity。
- **C2 状态**：没有新增独立支持；MEP-O/GCR 仍要求实体的、非循环的理由。
- **C0 状态**：没有被这一反模型排除；它仍可以把局部 first-person 表达理解为 ordinary subjects 的现象与索引式事实。

下一步优先级建议：

1. **GCR defense audit**：给出 independently motivated 的 completeness / unity criterion，再检查它是否蕴涵全现实 pointwise reflection；不得直接把「唯一中心」作为 criterion。
2. **C1 non-neutralizability audit**：明确 neutral reduct 的边界、mode fact 的 identity/grounding、可允许的 modal variation；区分 semantic encoding、supervenience 与 metaphysical reduction。
3. **Cross-mode compatibility audit**：给 MPGC 一个可扩展的、处理 shared objective claims 与 interaction 的 consistency rule。
4. 三项都无定论时，将 C1 标记为**形式上清晰、形而上学上仍有重大原始承诺的竞争者**，并对 C0/C1/C2 同尺度比较。

与旧结论的关系：**细化并降低了旧 Plural Opening Manifold “survives third-person collapse” 判定的证据强度**；没有删除旧研究，也没有把它反向改判为不一致。