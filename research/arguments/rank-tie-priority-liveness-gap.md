# Rank-Tie Obstruction 与 Priority–Liveness Gap

> 状态：工作论证。目标是检验 `global fundamentality minimum` 能否同时承担 global singleton 与 absolute liveness。

## 0. 背景

此前最强候选之一是：在全局 grounding structure 中给所有 experiential events 一个 relative-fundamentality rank，再选唯一最低者：

\[
E^*=\operatorname*{arg\,min}_{E\in\mathcal E_C} rank(E).
\]

这条路线看起来同时具有三项优势：

1. 所有候选进入同一个 global comparison；
2. rank 来自 grounding，而非任意分数；
3. fundamentality 自带 metaphysical priority。

进一步检查后，需要把这三点拆开。Grounding literature 可以较好支持第 1 点，但没有自动给出第 2、3 点所需的强结论。

---

## 1. Grounding rank 真正能给什么

若 partial grounding relation 是 well-founded，可以给 domain 中每个元素赋 ordinal rank：

\[
rank(x)=\sup\{rank(y)+1:y\prec x\}.
\]

minimal elements 的 rank 为 0。

Michael Bevan 的 foundationalist 结果进一步表明，在这类 grounding structures 中，rank comparison 可以成为满足一组自然条件的唯一 priority order，并且该 priority order 是 strongly connected。

所以 grounding 的确可以提供：

\[
\boxed{\text{global priority comparability}}
\]

而不必任意指定一个 scalar score。

这一点对本项目很有价值。

---

## 2. Rank-Tie Obstruction

但 rank comparison 是一个 total / strongly-connected priority preorder，并不等于存在唯一最低元素。

如果有两个 experiential events：

\[
rank(E_a)=rank(E_b)=r_{min},
\qquad E_a\neq E_b,
\]

则：

\[
\operatorname*{arg\,min}_{E\in\mathcal E_C}rank(E)
=
\{E_a,E_b,\dots\}.
\]

所以：

\[
\boxed{\text{unique priority order}\not\Rightarrow\text{unique minimum}}
\]

暂称 **Rank-Tie Obstruction**。

这不是边缘情况。一个 well-founded grounding structure 可以有很多 minimal / rank-0 elements，也可以有很多处在相同更高 rank 的 facts。

因此 global rank 解决的是“如何比较优先性”，没有自动解决 singleton。

---

## 3. Base-Uniqueness ≠ Element-Uniqueness

Grounding literature 有时要求 fundamental base 具有 completeness、minimality，甚至 unique minimal completeness。

设唯一 fundamental base 为：

\[
B^*=\{f_1,f_2,\dots,f_n\}.
\]

即使：

\[
\exists !B^*\;FundamentalBase(B^*),
\]

也完全不推出：

\[
|B^*|=1.
\]

所以：

\[
\boxed{\text{unique base}\not\Rightarrow\text{singleton fundamentale}}
\]

这和项目此前反复遇到的模式同构：

- 一个 universe 不推出一个 experiential center；
- 一个 process 不推出一个 live center；
- 一个 actual history 不推出一个 conscious center；
- 一个 unique grounding base 也不推出一个 fundamental experiential item。

因此不能把 `unique foundation` 当作 absolute first-person uniqueness 的答案。

---

## 4. Priority–Liveness Gap

即使更强地假设：

\[
\exists !E^*\;MostFundamentalExperiential(E^*),
\]

还没有得到：

\[
LIVE_{simpliciter}(E^*).
\]

原因是 standard grounding / priority theories 主要编码：

\[
\text{dependence / explanation / ontological priority}.
\]

它们一般不把 derivative entities 当成不真实。

Priority monism 是最清楚的例子：cosmos 可以是唯一 fundamental concrete object，其余 objects 依赖 cosmos，同时其余 objects 仍然真实存在。

所以：

\[
\boxed{\text{more fundamental}\not\Rightarrow\text{more live / more actual}}
\]

暂称 **Priority–Liveness Gap**。

这意味着此前的桥：

\[
Fundamental(E^*)\Rightarrow Absolute(E^*)
\]

不能由 grounding 概念本身提供。

---

## 5. Priority Presentism 为什么仍然有启发

Sam Baron 的 Priority Presentism 有意使用 fundamentality 来保留 present 的 ontological import：

- present entities fundamental；
- past / future entities derivative；
- 由此试图捕捉“now is special”以及 present 的 reality intuition。

这证明：

\[
\text{fundamentality can be recruited into a theory of privilege}.
\]

但这里的关键桥接属于该时间理论的 substantive metaphysical interpretation，不是 grounding relation 的一般逻辑后果。

换到绝对第一人称以后，我们仍需独立论证：

\[
\boxed{\text{为什么 experiential fundamentality 应该意味着 absolute liveness}}
\]

不能仅仅引用 grounding vocabulary。

2025 年对 Priority Presentism 的批评还说明，若 fundamentality 随时间迁移，会产生 ontological instability；这一压力对动态 I–NOW 模型更严重。

---

## 6. 对 Experiential Dominator 的影响

此前提出 **experiential dominator / bottleneck**：某个 \(E^*\) 位于 fundamental base 到其他 experiential facts 的所有 grounding paths 上。

该模型比 rank minimum 强，因为它赋予 \(E^*\) 一个全局依赖拓扑角色。

但它现在受到两类压力。

### 6.1 Dominance 仍不等于 liveness

即使：

\[
E^*\text{ dominates all experiential grounding paths},
\]

也只得到：

\[
E^*\text{ is indispensable in the dependence structure}.
\]

还需证明：

\[
\text{metaphysical indispensability}\Rightarrow LIVE_{simpliciter}.
\]

所以 Priority–Liveness Gap 仍然存在。

### 6.2 Grounding branching 本身有争议

Noël Saenz 的 `Grounding Uniqueness` 原则主张，一个 ground 不能 ground 多于一个 groundee，并明确指出该原则排除 grounding branches。若接受这一强原则，priority monism 式“一个 ground 产生许多 derivative items”也会受到直接压力。

该原则在 grounding literature 中并非无争议公理；Saenz 自己也承认它很强，并讨论较弱版本。

所以 Experiential Dominator 不能把 branching grounding 当成免费的背景假设。

它至少需要明确：

- 使用哪一种 grounding relation；
- 是否接受 transitivity；
- 是否允许 branching；
- `dominator` 表达 full ground、partial ground、dependence，还是更一般的 metaphysical explanation relation。

---

## 7. 一个意外的相关先例：`me-ish` grounding facts

Saenz 在讨论 priority monism 如何区分 cosmos 的不同 proper parts 时，给出一个非常贴近本项目的示意：priority monist 可以诉诸关于 cosmos 的不同 facts——例如 cosmos 在这里具有 `me-ish`、在那里具有 `you-ish` 的方式——分别 grounding 不同的人。

这不是 absolute-first-person theory，也没有主张某个 `me-ish` fact 更 privileged。

但它暴露了一个重要结构：

\[
\text{one global whole}
+
\text{location/person-specific grounding facts}
\to
\text{many distinct local persons}.
\]

因此，即使 grounding source 是 one cosmos，细化 grounding facts 往往自然得到**多个** `me-ish / you-ish` local manifestations。

这再次支持：

\[
\text{global source unity}\not\Rightarrow\text{global first-person singleton}.
\]

---

## 8. 新的四段式要求

Grounding 路线现在需要完成四段，而非此前以为的两段：

### A. Global ordering

\[
\mathcal G\Rightarrow\sqsubseteq
\]

用 grounding structure 生成全局 priority order。

这一段已有成熟支持。

### B. Singleton theorem

\[
\sqsubseteq\Rightarrow\exists !E^*\;Minimal_{Exp}(E^*).
\]

这一段目前失败于 Rank-Tie Obstruction，除非加入新的结构条件。

### C. Liveness generation

\[
G\Rightarrow Live(E^*).
\]

可由 fundamental becoming 等 process theory 提供候选。

### D. Priority-to-Absolute bridge

\[
Minimal_{Exp}(E^*)\land Live(E^*)
\Rightarrow
AbsoluteLive(E^*).
\]

这一段目前失败于 Priority–Liveness Gap，仍缺独立原则。

因此：

\[
\boxed{
\text{grounding rank is a useful global comparator, not yet an absolute-first-person mechanism}
}
\]

---

## 9. 当前方向调整

`global fundamentality minimum` 仍保留，但不再称为“最强 singleton + privilege 完整候选”。

它更准确的角色是：

\[
\boxed{\text{最成熟的 global comparator 候选}}
\]

下一步真正需要找的是两个额外机制：

1. **Tie breaker with metaphysical relevance**：为什么 experiential priority order 有唯一最低者；
2. **Priority–Liveness Bridge**：为什么最低者拥有 absolute liveness，而非仅仅更基础。

任何纯粹增加 secondary score 的 tie-breaker 都会退回 arbitrary canonical selector。

因此最有价值的新目标是：寻找一种性质 \(Q\)，使它同时：

\[
Q\Rightarrow\text{unique experiential minimum}
\]

并且：

\[
Q\Rightarrow\text{liveness-relevant privilege}.
\]

如果找不到这样的 \(Q\)，grounding 路线将只能解释 ontological priority，无法解释 absolute first-personhood。

## 文献入口

- Fabrice Correia, “Fundamentality from grounding trees” (Synthese, 2021).
- Fabrice Correia, “A kind route from grounding to fundamentality” (Synthese, 2021).
- Michael Bevan, “Metaphysical foundationalism” (Philosophical Studies, 2025/2026 online publication).
- Stanford Encyclopedia of Philosophy, “Metaphysical Grounding” and “Fundamentality”.
- Sam Baron, “The Priority of the Now” (Pacific Philosophical Quarterly, 2015).
- Gustavo Lyra, “The Priority of the Past” (2025).
- Noël Blas Saenz, “The Taming of the Grounds” (Canadian Journal of Philosophy, 2023).
- Ricki Bliss, “What Work the Fundamental?” (Erkenntnis, 2019).
