# Perspective Closure Principle

> 状态：2026-10-05 re-audited after Evaluation-Locus Cardinality Gap。
>
> 目标：说明 SPC 在 singularity chain 中的角色，并明确它现在不是 deepest primitive：MEP / monocentric evaluation 位于其上游。

## 0. Core

旧：

\[
FPNC:\quad DistinctIrreducibleOpenings\Rightarrow NonCompossibility.
\]

当前拆分：

\[
\boxed{LE+SPC\Rightarrow FPNC.}
\]

其中：

- `LE` = Local Exclusivity；
- `SPC` = Single-Perspective Closure。

再往上：

\[
\boxed{MEP+Pointwise/IntersectionCompossibility\Rightarrow SPC.}
\]

所以完整 chain：

\[
\boxed{
MEP\to SPC\to FPNC\to AtMostOne\to ExactlyOne(+ALO).
}
\]

---

## 1. Local Exclusivity

对 mutually exclusive complete first-person states：

\[
X\perp Y.
\]

### LE

\[
\boxed{
X\perp Y
\Rightarrow
\neg\exists m\;[m\Vdash X\land m\Vdash Y].
}
\]

LE 只限制 **one standpoint**；Plural Opening Manifold 也接受。

---

## 2. Single-Perspective Closure

### SPC

对 genuine first-person facts \(F,G\)：

\[
\boxed{
Compossible_{global}(F,G)
\Rightarrow
\exists m\;[m\Vdash F\land m\Vdash G].
}
\]

即：若两个 first-person facts qua first-person facts globally compossible，则必须有一个 single perspective 从中它们 jointly obtain。

这是 List-style first-person compossibility 的核心。

---

## 3. SPC + LE yields FPNC

设：

\[
F_X=m_a\Vdash X,
\qquad
F_Y=m_b\Vdash Y,
\qquad
X\perp Y.
\]

若二者 compossible，由 SPC：

\[
\exists m\;[m\Vdash X\land m\Vdash Y].
\]

由 LE：

\[
\neg\exists m\;[m\Vdash X\land m\Vdash Y].
\]

矛盾。

所以：

\[
\boxed{LE+SPC\Rightarrow FPNC.}
\]

---

## 4. FPNC + List-style NF yields at-most-one

定义：

### NF-SPC

actual totality中的 first-person facts 全部 globally compossible，且 compossibility 使用 SPC criterion。

若有两个 distinct complete openings，FPNC 说二者 non-compossible；NF-SPC 又要求 compossible。

所以：

\[
\boxed{
LE+SPC+NF_{SPC}
\Rightarrow AtMostOneOpening.
}
\]

再加：

\[
ALO:\quad \exists c\;Opening(c),
\]

得到：

\[
\boxed{ExactlyOneOpening.}
\]

---

## 5. Mode-Preserving alternative

Plural Opening Manifold 使用：

### MPGC — Mode-Preserving Global Coherence

一个 single actual structure 可以包含多个 mode-local consistent first-person fact sets，并保留 mode typing。

所以：

\[
\boxed{
MPGC(F,G)
\not\Rightarrow
\exists m\;[m\Vdash F\land m\Vdash G].
}
\]

从而：

\[
LE+MPGC\not\Rightarrow FPNC.
\]

这说明 SPC 是 substantive unity condition，不是 ordinary logic theorem。

---

## 6. Why SPC is natural in List semantics

List 表示 first-personally centred world 为：

\[
\langle\omega,\pi\rangle.
\]

first-person facts对应 sets of such centered worlds。

若 compossibility由 proposition intersection / one evaluation point joint satisfaction 表示，则 joint witness 必然是一个：

\[
\langle\omega,\pi\rangle
\]

而只含 one \(\pi\)。

因此在该 architecture 中：

\[
SPC
\]

非常自然。

---

## 7. MEP upstream of SPC

显式定义：

### MEP — Monocentric Evaluation Principle

\[
\boxed{
Every\ maximal\ first\!\!\text{-}\!person\ evaluation\ locus
contains\ exactly\ one\ perspective.
}
\]

配合 standard pointwise/intersection compossibility：

\[
\boxed{MEP\Rightarrow SPC.}
\]

更准确说：

\[
MEP+PointwiseJointSatisfaction\Rightarrow SPC.
\]

所以 SPC 的自然性部分来自 **candidate joint truth loci 被预先限定为 monocentric**。

详见 [`evaluation-locus-cardinality-gap.md`](evaluation-locus-cardinality-gap.md)。

---

## 8. Perspective variance does not yield MEP

first-person fact 非 perspective-invariant：

\[
\exists\pi_i,\pi_j\;[V(F,\pi_i)\neq V(F,\pi_j)].
\]

这只要求 evaluation 保留 perspective dependence。

它没有规定 complete actuality state 的 perspective cardinality。

所以：

\[
\boxed{
PerspectiveVariance\not\Rightarrow MEP.
}
\]

这也是为什么 SPC 不能仅由 `first-person facts are subjective` 免费得到。

---

## 9. Polycentric alternative

允许 maximal actuality：

\[
\mathfrak R=\langle\omega,\Pi,\mathcal V,A\rangle,
\qquad |\Pi|>1.
\]

其中每个 \(\pi_i\) 仍有 irreducible first-person valuation / obtaining mode。

若这种结构 genuine，而非 third-personized collection，则：

\[
\boxed{\neg MEP\land OneActuality\land PluralIrreducibleFP}
\]

coherent-looking。

因此当前真正 positive burden 是证明 polycentric structure不够资格成为 complete actuality。

---

## 10. OneWorld remains weaker

\[
OneWorld:\quad \exists!R\;ActualWorld(R)
\]

不规定 \(R\) 内部有 one perspective 还是 many perspective modes。

所以：

\[
\boxed{OneWorld\not\Rightarrow MEP\not\Rightarrow SPC.}
\]

world-count 与 evaluation-locus cardinality 必须分开。

---

## 11. Current singularity theorem

保留条件式：

\[
\boxed{
ALO+LE+SPC+NF_{SPC}
\Rightarrow ExactlyOneOpening.
}
\]

更底层：

\[
\boxed{
ALO+MEP+PointwiseCompossibility+LE+NF_{SPC}
\Rightarrow ExactlyOneOpening.
}
\]

但当前没有独立 proof：

\[
CompleteActuality\Rightarrow MEP.
\]

---

## 12. Current verdict

SPC 仍是有效、重要的 singularity bridge，但不再是 deepest unexplained premise。

最新层级：

\[
\boxed{
MEP\text{ is upstream of SPC.}
}
\]

所以 current question：

\[
\boxed{
Why\ must\ maximal\ first\!\!\text{-}\!person\ actuality\ be\ monocentric?
}
\]

在 MEP 或 polycentric-collapse theorem 建立前，Plural Opening Manifold remains live。

## 关联

- [`evaluation-locus-cardinality-gap.md`](evaluation-locus-cardinality-gap.md)
- [`../models/plural-opening-manifold.md`](../models/plural-opening-manifold.md)
- [`first-person-non-compossibility-audit.md`](first-person-non-compossibility-audit.md)
- [`unitary-singularity-lemma.md`](unitary-singularity-lemma.md)
