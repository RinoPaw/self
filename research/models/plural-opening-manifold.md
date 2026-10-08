# Plural Opening Manifold

> **2026-10-08 状态修正**：本模型提供 distributed / typed semantic 反例与明确的候选本体论承诺；FP2–FP4 的不可还原性和 MPGC 的 global unity 仍需独立证明。原有“通过 collapse 检验”是截至当时的条件判定，不应读作非还原性的已证定理。详见 [后续审计](../arguments/pointwise-polycentric-reflection-audit.md)。


> 状态：2026-10-05 FPNC stress test / constructive countermodel。
>
> 目标：构造一个 **one actuality + multiple irreducible first-person openings** 的最强模型，检查它是否必然坍塌为 third-person meta-facts、many worlds，或直接 contradiction。

## 0. Target

我们要测试的不是：

\[
\text{many ordinary subjects}
\]

而是更强的：

\[
\boxed{
OneActuality
+PluralIrreducibleFirstPersonModes
+NoGlobalPrivilegedCenter.
}
\]

如果这样的模型 coherent-looking，则：

\[
OneActuality+FirstPersonArity
\not\Rightarrow
ExactlyOneOpening.
\]

任何 singularity theorem 都必须增加额外 unity / compossibility premise。

---

## 1. Structure

构造：

\[
\boxed{
\mathcal P=\langle W,C,M,F,A\rangle
}
\]

其中：

- \(W\)：一个 objective / causal history；
- \(C=\{a,b\}\)：两个 genuine conscious centers；
- \(M=\{m_a,m_b\}\)：两个 irreducible first-person modes of obtaining；
- \(F=F_0\cup F_a\cup F_b\)：objective 与 first-person fact system；
- \(A\)：一个 actuality operator / obtaining status，作用于整个 \(\mathcal P\)。

要求：

\[
\boxed{Actual(\mathcal P)}
\]

而不是：

\[
Actual_a(\mathcal P_a)\land Actual_b(\mathcal P_b).
\]

所以 model 从一开始只有 **one actual totality**。

---

## 2. Objective common layer

\(W\) 包含双方共享的 ordinary facts：

\[
BrainState(a,X),
\qquad
BrainState(b,Y),
\]

以及全部 causal / physical / behavioural facts。

允许：

\[
X\neq Y
\]

且 \(X,Y\) 是两个主体各自的 complete token conscious states。

第三人称层面完全无冲突：

\[
a\text{ is in }X,
\qquad
b\text{ is in }Y.
\]

---

## 3. Irreducible first-person modes

对 \(a,b\) 分别有：

\[
m_a,
\qquad
m_b.
\]

写：

\[
m_a\Vdash X,
\qquad
m_b\Vdash Y.
\]

这里 `\(m\Vdash p\)` 是 **metalanguage notation**，表示 `p` 以 mode `m` fundamental 地 obtain。

关键不是把 `m` 当作 object-language relation argument：

\[
Obtains(m,p).
\]

模型明确拒绝这种自动 reduction。

`m` 属于 fact 的 constitutive obtaining manner，而不是 neutral fact-content 里的附加参数。

因此：

\[
\boxed{
Erase(m_a,m_a\Vdash X)
\neq
\text{preserve the same fact in neutral form}.
}
\]

删掉 mode 会删掉 fact 的 first-person identity。

---

## 4. Genuine-first-person test

为了避免模型偷偷退回 `(1*) there is a perspective from which...`，要求每个 \(m_i\) 通过四项测试。

### FP1 — Perspective variance

\[
m_a\Vdash X
\]

不要求：

\[
m_b\Vdash X.
\]

first-person obtaining 随 standpoint 变化。

### FP2 — Mode essentiality

事实 identity 包含 obtaining mode：

\[
Fact(m_a\Vdash X)
\neq
Fact(m_b\Vdash X).
\]

### FP3 — No invariant paraphrase identity

允许第三人称 meta-fact：

\[
ThereIsPerspective(a,X)
\]

但否认：

\[
Fact(m_a\Vdash X)
=
Fact(ThereIsPerspective(a,X)).
\]

后者在 perspective shift 下 invariant；前者不是。

### FP4 — World-side status

\(m_a\Vdash X\) 与 \(m_b\Vdash Y\) 都是 reality 的 constitutive facts，而不只是 subject 的 representation / data structure。

因此该模型保留：

\[
\boxed{IrreducibleFirstPersonFact(a)\land IrreducibleFirstPersonFact(b).}
\]

---

## 5. Local classicality

模型不允许每个 standpoint 内部任意爆炸。

对每个 \(m\)：

\[
\boxed{
\neg\exists p\;[m\Vdash p\land m\Vdash\neg p].
}
\]

并要求每个 mode-local fact set 与 objective common layer \(W\) 一致。

所以：

\[
F_a\cup W
\]

和：

\[
F_b\cup W
\]

分别 classical-consistent。

---

## 6. Mode-Preserving Global Coherence

真正关键的定义是 global unity。

定义 **MPGC — Mode-Preserving Global Coherence**：

\[
\boxed{
MPGC(F)
}
\]

当且仅当存在一个单一结构 \(\mathcal P\)，使得：

1. 所有 objective facts \(F_0\) 在同一个 \(W\) 中 obtain；
2. 对每个 mode \(m_i\)，该 mode 下的 facts jointly obtain；
3. 所有 mode 都属于同一个 actual structure，而不是各自形成 complete actual worlds；
4. cross-mode conjunction 保留 mode type，不把：
   \[
   m_a\Vdash X,
   \quad m_b\Vdash Y
   \]
   强制改写成：
   \[
   m\Vdash X\land Y.
   \]

所以只要：

\[
Consistent(F_a\cup W)
\land
Consistent(F_b\cup W),
\]

则可以有：

\[
\boxed{
MPGC(F_a\cup F_b\cup W).
}
\]

即使：

\[
X\land Y
\]

对**同一个 perspective** impossible。

---

## 7. Explicit two-opening instance

取：

\[
C=\{a,b\}.
\]

设：

\[
m_a\Vdash I\text{-am-in-}X,
\]

\[
m_b\Vdash I\text{-am-in-}Y,
\]

其中：

\[
X\perp Y
\]

表示一个 subject 不可能同时处于两种 complete token conscious states。

模型满足：

\[
\neg(m_a\Vdash Y),
\qquad
\neg(m_b\Vdash X),
\]

但这不产生：

\[
\bot.
\]

因为没有任何公理把：

\[
m_a,m_b
\]

identifies 成同一个 obtaining mode。

因此存在一个直接 model-theoretic witness：

\[
\boxed{
OneActuality
+TwoIrreducibleFPModes
+LocalConsistency
+MPGC.
}
\]

---

## 8. 为什么这不是 many worlds

模型明确不满足：

\[
\exists R_a\neq R_b\;[Actual(R_a)\land Actual(R_b)].
\]

而只满足：

\[
\exists!R\;Actual(R).
\]

并且：

- \(a,b\) 属于同一个 physical history；
- 两个 centers 可以 causal interaction；
- objective facts 是共享的；
- 删除任一 mode 都会删除实际 reality 的一部分 first-person structure；
- 没有一个 mode 自己携带一份 complete independent world-history。

所以 plurality 位于：

\[
\boxed{mode\ layer}
\]

而不是：

\[
\boxed{world\ count}.
\]

---

## 9. 为什么这也不是简单 relationalism

一个 neutral relationalist 可以写：

\[
PerspectiveOf(a,X),
\qquad
PerspectiveOf(b,Y).
\]

这些是 invariant third-person facts。

本模型更强：

\[
\boxed{
Perspective\ is\ in\ the\ manner\ of\ obtaining,
not\ merely\ represented\ in\ content.
}
\]

这正是 constitutional perspectivalism 的结构类比：perspective 可以属于 constituting facts **如何 obtain**，而不被分析成更底层 neutral fact 的 argument。

因此该模型是：

\[
\boxed{plural\ first\!\!\text{-}\!person\ realism}
\]

而不是：

\[
\boxed{third\!\!\text{-}\!person\ realism+quoted\ I\text{-sentences}}.
\]

---

## 10. 与 List Non-Fragmentation 的直接碰撞

List-style compossibility 要求：

\[
\boxed{
Compossible_{FP}(F,G)
\Rightarrow
\exists m\;[m\Vdash F\land m\Vdash G].
}
\]

称为：

### SPC — Single-Perspective Closure

对本模型：

\[
m_a\Vdash X,
\qquad
m_b\Vdash Y
\]

但不存在：

\[
\exists m\;[m\Vdash X\land m\Vdash Y].
\]

所以：

\[
\boxed{\mathcal P\text{ violates SPC/List-style NF}.}
\]

这与 List quadrilemma 完全一致。

因此该模型**没有 refute List**。

它证明的是另一件更重要的事：

\[
\boxed{
OneActuality+GlobalStructuralCoherence
\not\Rightarrow
SPC.
}
\]

把 one reality 理解成一个 mode-preserving structured totality，不自动要求全部 first-person facts 从 one perspective co-obtain。

---

## 11. 两种 Non-Fragmentation 必须分开

### NF-L — List / single-perspective non-fragmentation

\[
AllFacts(R)\text{ are compossible under SPC}.
\]

它与 plural complete first-person openings冲突。

### NF-M — manifold non-fragmentation

\[
AllFacts(R)\text{ are jointly embeddable in one mode-preserving actual structure}.
\]

它与 plural openings相容。

因此：

\[
\boxed{NF\text{ is not a neutral label until the compossibility criterion is fixed}.}
\]

如果项目选择 NF-L，singularity pressure 很强；如果选择 NF-M，plural opening manifold survives。

真正争议不再是：

> facts 会不会 contradiction？

而是：

\[
\boxed{
What\ kind\ of\ unity\ must\ one\ actuality\ possess?
}
\]

---

## 12. Fragmentalism classification

Fine/List/Lipman-style vocabulary 会把该模型归入 fragmentalist family，因为：

- multiple perspectival facts genuinely constitute reality；
- reality does not privilege one perspective；
- some facts fail single-perspective co-obtainment。

这不是 objection 的结束，而是 taxonomy。

模型仍可坚持：

\[
\exists!R\;Actual(R)
\]

并把 fragmentation 理解成：

\[
\text{plural internal obtaining modes of one reality},
\]

而不是：

\[
\text{many actual worlds}.
\]

因此 List 的 four-way landscape 中，该模型明确走：

\[
FPR+NS+OW+\neg NF\text{-L}.
\]

---

## 13. “absolute” 的词义警戒

若定义：

\[
AbsoluteOpening(c)
:=
\text{the unique globally privileged opening},
\]

则：

\[
\exists!c\;AbsoluteOpening(c)
\]

已经被定义进 predicate。

这种定义不能用于证明 singularity。

在 pre-singularity 阶段应使用：

\[
IrreducibleOpening(c)
\]

只表示：

- genuinely first-person；
- world-side；
- irreducible to third-person representation/facts；
- actuality-constituting。

然后独立问：

\[
\exists!c\ ?
\]

Plural Opening Manifold 证明：

\[
\boxed{
IrreducibleOpening\not\Rightarrow AbsoluteSingleton.
}
\]

---

## 14. Current verdict

该 countermodel **survives** 当前四项压力：

1. **third-person collapse**：未发生；mode 是 constitutive obtaining manner；
2. **many-world collapse**：未发生；只有 one actual totality / shared history；
3. **formal contradiction**：未发生；每个 mode local-classical，global structure preserves mode typing；
4. **List challenge**：模型明确拒绝 SPC / NF-L，因此进入 fragmentalist/pluralist horn，而非反驳 List。

所以得到：

\[
\boxed{
OneActuality
+PluralIrreducibleFPModes
+MPGC
\text{ is coherent-looking}.
}
\]

这把 singularity burden 压缩成：

\[
\boxed{
Why\ Single\!\!\text{-}\!Perspective\ Closure
rather\ than\ Mode\!\!\text{-}\!Preserving\ Global\ Coherence?
}
\]

在这个问题解决前：

\[
\boxed{ExactlyOneOpening\text{ is not independently derived}.}
\]

## Literature anchors

- Christian List, “A Quadrilemma for Theories of Consciousness”, *The Philosophical Quarterly* 75(3), 2025 — defines the one-world / non-fragmentation pressure and explicitly uses same-perspective compossibility for first-person facts.
- Martin A. Lipman, “Subjective Facts about Consciousness”, *Ergo* 10 (2023) — subjects as metaphysical standpoints; subjective facts vary across subjects.
- Martin Lipman, *Standpoints: Time and Subjectivity* (OUP, 2026) — developed standpoint pluralism / fragmentalist metaphysics.
- Bahadır Eker, “Perspectivalism about temporal reality”, *Synthese* 202 (2023) — constitutional perspectivality: facts can fundamentally obtain from perspectives without reduction to atemporal neutral facts.
- Giovanni Merlo, “Fragmentalism We Can Believe In”, *The Philosophical Quarterly* 73(1), 2023 — fragmentalism as perspectival realism + neutrality + absolute constitution of reality by perspectival facts.

## 关联

- [`../arguments/first-person-non-compossibility-audit.md`](../arguments/first-person-non-compossibility-audit.md)
- [`../arguments/perspective-closure-principle.md`](../arguments/perspective-closure-principle.md)
- [`../arguments/obtaining-mode-pluralization.md`](../arguments/obtaining-mode-pluralization.md)
- [`../arguments/actuality-arity-singularity-gap.md`](../arguments/actuality-arity-singularity-gap.md)
