# Evaluation-Locus Cardinality Gap

> 状态：2026-10-05 deeper audit of Single-Perspective Closure。
>
> 目标：检查从 `first-person facts are perspective-sensitive` 到 `first-person compossibility requires one perspective` 的推理是否仍包含一个未显式化的 semantic / metaphysical premise。

## 0. Result

Christian List 的 centered-world formalization使用：

\[
\boxed{\langle \omega,\pi\rangle}
\]

作为 first-person fact 的完整 truth locus，其中：

- \(\omega\)：third-personal world；
- \(\pi\)：一个 first-person perspective。

在该 semantic space 中，一个 maximal evaluation point只有 **one** \(\pi\)。

因此不同主体的 complete first-person fact sets若要求不同 \(\pi\)，其 centered-proposition intersections 可以为空。

这给 non-compossibility 一个干净形式证明。

但需要区分：

\[
\boxed{
PerspectiveSensitivity
\not\Rightarrow
OnePerspectivePerMaximalActualityState.
}
\]

前者要求 valuation/evaluation保留 perspective；后者决定 maximal evaluation locus 的 cardinality。

这就是 **Evaluation-Locus Cardinality Gap (ELCG)**。

---

## 1. Perspective Sensitivity

设 first-person fact \(F\) 的 truth 随 perspective 变化：

\[
\exists \pi_i,\pi_j\;[
V(F,\pi_i)\neq V(F,\pi_j)
].
\]

这说明：

\[
\boxed{F\text{ is not perspective-invariant}.}
\]

从而反对把它简单等同于一个 perspective-invariant third-person fact。

但这个条件只要求 semantic structure能区分 perspectives。

它没有规定 complete reality state必须写成：

\[
\langle\omega,\pi\rangle
\]

而不能写成：

\[
\langle\omega,\Pi,\mathcal V\rangle,
\qquad |\Pi|>1,
\]

其中 \(\mathcal V\) 保留每个 standpoint 的 irreducible obtaining mode。

---

## 2. Monocentric Evaluation Principle

把 List-style centered evaluation architecture 中隐含的 cardinality constraint 显式化：

### MEP — Monocentric Evaluation Principle

\[
\boxed{
Every\ maximal\ first\!\!\text{-}\!person\ truth/evaluation\ locus
contains\ exactly\ one\ perspective.
}
\]

标准 first-personally centred world：

\[
\langle\omega,\pi\rangle
\]

自动满足 MEP。

这不是对 List 的误读；他的 formalism 正是用 one locus of subjectivity \(\pi\) enrich 一个 third-personal world \(\omega\)。

但需要问：

\[
\boxed{Why\ must\ maximal\ actuality\ itself\ obey\ MEP?}
\]

---

## 3. How MEP yields empty intersection

设：

\[
\mathcal F_a
\]

是 subject \(a\) 的 complete first-person fact set，

\[
\mathcal F_b
\]

是 subject \(b\) 的 complete first-person fact set。

在 centered-proposition semantics 中，每个 fact对应一组 centered worlds：

\[
P_F\subseteq \Omega\times\Pi.
\]

complete fact set对应交集：

\[
I_a=\bigcap_{F\in\mathcal F_a}P_F,
\]

\[
I_b=\bigcap_{G\in\mathcal F_b}P_G.
\]

若 \(a,b\) 对应 mutually exclusive complete perspectives，则：

\[
I_a\cap I_b=\varnothing.
\]

因为没有一个 single-centered point：

\[
\langle\omega,\pi\rangle
\]

同时拥有两套 incompatible complete perspectives。

所以 non-compossibility 在 MEP-space 中严格成立。

---

## 4. Polycentric evaluation structure

现在扩展 maximal state type：

\[
\boxed{
\mathfrak R
=
\langle\omega,\Pi,\mathcal V,A\rangle
}
\]

其中：

- \(\omega\)：shared third-person history；
- \(\Pi=\{\pi_a,\pi_b,\ldots\}\)：multiple irreducible standpoint modes；
- \(\mathcal V\)：mode-preserving valuation / obtaining structure；
- \(A\)：one actuality status。

对每个 \(\pi_i\)：

\[
\mathcal V_{\pi_i}
\]

给该 standpoint 的 complete first-person facts。

要求每个 mode-local valuation consistent：

\[
Consistent(\mathcal V_{\pi_i}).
\]

但不要求存在：

\[
\pi^*\in\Pi
\]

使全部 facts 都在 \(\pi^*\) 下 true。

这正是 Plural Opening Manifold 的 semantic analogue。

---

## 5. Perspective variance survives polycentricity

在 polycentric model 中，仍可以有：

\[
V(F,\pi_a)=1,
\qquad
V(F,\pi_b)=0.
\]

所以：

\[
F\text{ remains perspective-sensitive}.
\]

并且若 obtaining mode 对 fact identity constitutive，则：

\[
Fact_{\pi_a}(F)
\]

仍不等同于：

\[
ThereExistsPerspective(\pi_a,F).
\]

因此：

\[
\boxed{
PolycentricEvaluation
\not\Rightarrow
ThirdPersonReduction.
}
\]

至少这一 reduction 需要额外 argument。

---

## 6. The formal gap

从：

\[
PerspectiveVariance(F)
\]

可以推出：

\[
NeedPerspectiveSensitiveEvaluation(F).
\]

但不能单靠它推出：

\[
MaximalEvaluationLocusHasExactlyOnePerspective.
\]

所以：

\[
\boxed{
PerspectiveVariance
\not\Rightarrow
MEP.
}
\]

这是一个结构层级差异：

- variance 决定 **valuation depends on perspective**；
- MEP 决定 **maximal state contains how many perspective slots/modes**。

两者逻辑上不同。

---

## 7. Relation to SPC

SPC：

\[
Compossible_{FP}(F,G)
\Rightarrow
\exists\pi\;[\pi\Vdash F\land\pi\Vdash G].
\]

在标准 centered-world semantics 中非常自然，因为 candidate joint-instantiation points 都是：

\[
\langle\omega,\pi\rangle.
\]

因此可以理解为：

\[
\boxed{
MEP
+StandardIntersectionCompossibility
\Rightarrow
SPC.
}
\]

这进一步解释旧 FPNC chain：

\[
MEP
+IntersectionCompossibility
+LE
\Rightarrow FPNC.
\]

所以 singularity burden 可以继续下压到：

\[
\boxed{MEP.}
\]

---

## 8. Is MEP merely semantic?

不能因为 MEP 出现在 formal representation 中，就立刻说它是错误或 question-begging。

一种 possible defense 是：

> genuine first-person actuality 的 maximal truthmaker 本质上就是 one standpoint totality；任何多-perspective object都只是从外部收集多个 standpoint facts 的 third-person structure。

如果这个 defense 成功，MEP 有 metaphysical motivation。

但它需要独立论证：

\[
\boxed{
Polycentric\ actuality\ structure
\Rightarrow
ThirdPersonization\ or\ incompleteness.
}
\]

当前 Plural Opening Manifold 正是对此的 counterpressure。

---

## 9. A useful analogy, not an argument

若某性质随 spatial location 变化：

\[
V(P,x)\neq V(P,y),
\]

这说明描述 field state需要保留 location dependence。

它不自动要求 complete field state只能包含一个 spatial point。

first-person case当然更强，因为 perspective可能是 constitutive rather than parameter-like；所以不能把它简单还原为空间 field。

但 analogy 显示一个纯形式 lesson：

\[
\boxed{
Dependence\ on\ an\ index/mode
\not\Rightarrow
singleton\ cardinality\ of\ the\ complete\ structure.
}
\]

MEP 需要 first-person-specific metaphysical defense。

---

## 10. Three semantic architectures

### A. Uncentred semantics

\[
\omega
\]

only。

适合 C0；难以容纳 irreducible first-person facts。

### B. Monocentric semantics

\[
\langle\omega,\pi\rangle.
\]

适合 List many-worlds / singular standpoint realizers；自然产生 SPC。

### C. Polycentric / manifold semantics

\[
\langle\omega,\Pi,\mathcal V\rangle.
\]

适合 C1；多个 first-person modes共同属于一个 actual totality。

当前没有纯逻辑理由从 B 排除 C。

---

## 11. Strongest current singularity chain

现在应写：

\[
\boxed{
MEP
+IntersectionCompossibility
\Rightarrow SPC
}
\]

\[
\boxed{
SPC+LE\Rightarrow FPNC
}
\]

\[
\boxed{
FPNC+NF_{SPC}\Rightarrow AtMostOneOpening
}
\]

\[
\boxed{
AtMostOne+ALO\Rightarrow ExactlyOne.
}
\]

这把“exactly one”一路拆到了最底层 evaluation-locus choice。

---

## 12. Current verdict

List 的 non-compossibility proof 在 monocentric centered-world semantics 内有效且清楚。

但：

\[
\boxed{
FirstPersonIrreducibility
+PerspectiveVariance
\not\Rightarrow
MonocentricEvaluation.
}
\]

因此当前 deepest uniqueness question 进一步变成：

\[
\boxed{
Why\ must\ complete\ first\!\!\text{-}\!person\ actuality\ have\ a\ monocentric\ maximal\ evaluation\ locus?
}
\]

如果 MEP 无独立 defense，Plural Opening Manifold / polycentric semantics remain live。

## 关联

- [`perspective-closure-principle.md`](perspective-closure-principle.md)
- [`../models/plural-opening-manifold.md`](../models/plural-opening-manifold.md)
- [`first-person-non-compossibility-audit.md`](first-person-non-compossibility-audit.md)
- [`../../literature/list-2025-quadrilemma-unitary-opening.md`](../../literature/list-2025-quadrilemma-unitary-opening.md)
