# Unitary Singularity Lemma — Re-audited

> 状态：2026-10-05 re-audit 后的条件性结果。
>
> 旧版本把 singularity 的正面分量写高了。当前保留形式推导，但把 `First-Person Non-Compossibility`（FPNC）明确恢复为独立 burden。

## 0. Target

令预唯一性的 opening predicate 为：

\[
Open(\sigma),
\]

它只表示 `σ` 是一个 irreducible first-person opening，不包含 `unique`。

当前要检验：在什么额外条件下能从：

\[
\exists\sigma\;Open(\sigma)
\]

得到：

\[
\exists!\sigma\;Open(\sigma).
\]

---

## 1. Premises

### ALO — At Least One Opening

\[
\exists\sigma\;Open(\sigma).
\]

在 current Centered Actuality package 内，这可以作为 constitutive consequence：

\[
CenteredActuality\Rightarrow ALO.
\]

### OW — One World

\[
\exists!w\;RealityWorld(w).
\]

### NF — Non-Fragmentation

actuality 中共同 obtaining 的 facts 满足所采用的 compossibility criterion。

注意：`NF` 的具体 compossibility 标准本身不能模糊处理；它与 FPNC 的内容紧密相关。

### FPNC — First-Person Non-Compossibility

对 distinct irreducible openings：

\[
\boxed{
\sigma_i\neq\sigma_j
\land Open(\sigma_i)
\land Open(\sigma_j)
\Rightarrow
\neg Compossible(Open_i,Open_j).
}
\]

---

## 2. Conditional theorem

若：

\[
OW+NF+FPNC,
\]

则同一 nonfragmented actuality 中不能有两个 distinct openings。

所以：

\[
\boxed{
OW+NF+FPNC\Rightarrow AtMostOneOpening.
}
\]

再加 ALO：

\[
\boxed{
ALO+OW+NF+FPNC\Rightarrow ExactlyOneOpening.
}
\]

这一形式条件式保留，称为 **Unitary Singularity Lemma (USL)**。

---

## 3. 这次 re-audit 改了什么

以前容易把结果概括为：

\[
AtLeastOneOpening+UnitaryReality\Rightarrow ExactlyOneOpening.
\]

这会隐藏真正的 substantive premise。

更准确：

\[
\boxed{
AtLeastOneOpening
+UnitaryReality
+FPNonCompossibility
\Rightarrow ExactlyOneOpening.
}
\]

其中 anti-plurality content 主要来自：

\[
FPNC.
\]

`NF` 的作用是：如果两个 opening 按 FPNC 不可共存，那么 one nonfragmented actuality 不能同时包含它们。

所以 `OneWorld + NF` 不能单独计作 uniqueness theorem。

---

## 4. List-style support 的准确范围

Christian List 的 quadrilemma 为 FPNC 提供一个认真来源，但它依赖 genuine first-person fact 的 compossibility 概念。

可抽成：

\[
\boxed{
Compossible_{FP}(F,G)
\Rightarrow
\exists p\;[ObtainsFrom(F,p)\land ObtainsFrom(G,p)].
}
\]

即两个 first-person facts qua first-person facts 若共同成立，必须能从同一个 perspective 共同 obtain。

对于 mutually exclusive complete conscious states，这会推出 non-compossibility。

但本项目不能把这个标准当作 theory-neutral truth。Standpoint pluralism / constitutional perspectivalism 正会挑战：complete reality 是否可以 fundamental 地包含多个 perspective-constituted modes of obtaining。

因此：

\[
\boxed{
List\ provides\ a\ conditional\ FPNC\ route,
\ not\ a\ premise-free\ global\ singularity\ theorem.
}
\]

详见 [`first-person-non-compossibility-audit.md`](first-person-non-compossibility-audit.md)。

---

## 5. Plural-opening stress test

考虑：

\[
R_P=\langle W,C,M,A\rangle
\]

其中 `W` 是 one objective history，`C` 是 multiple centers，`M` 是 multiple irreducible perspectival obtaining modes，`A` 是 one actuality structure。

若该模型 coherent，则：

\[
OneReality+PluralIrreducibleCenters
\]

至少不是由 `OneWorld` alone 排除。

List-style theorist可以把它分类为 fragmented；但这只说明：

\[
PluralOpening\Rightarrow\neg NF_{List}
\]

而不是：

\[
PluralOpening\vdash\bot
\]

simpliciter。

所以当前真正问题是 unity/compossibility criterion，而非形式推导本身。

---

## 6. 与 Role-First centered model 的关系

当前 Role-First model 直接规定：

\[
\exists!L_i\;Occupies(L_i,G)
\]

以及：

\[
|Occupants(G)|=1.
\]

因此它已经是一种 primitive exact-one architecture。

要让 USL 真正承担 derivational work，有两种干净做法：

### Route A — Weaken the positive model

先只 postulate：

\[
\exists G\;GlobalOpening(G)
\]

以及至少一个 occupant，不预设唯一性；再尝试由 FPNC + NF 得到 exactly-one。

### Route B — Keep Role-First exact-one primitive

承认 strongest positive model 本身把 exact-one 放进 essence；USL 只提供与 List-style unitary metaphysics 的 reconstruction / consistency support，不再计算为独立 parsimony gain。

当前仓库不得同时使用两种 bookkeeping。

---

## 7. 与 Arity–Singularity Gap 的关系

已有结果：

\[
SubjectiveArity\not\Rightarrow Singularity,
\]

以及：

\[
ConstitutionalPerspectivality\not\Rightarrow PerspectiveSingleton.
\]

USL 不否定这些结果。它增加的是：

\[
FPNC.
\]

所以统一后的结构为：

\[
\boxed{
Perspectival/first\!\!\text{-}\!person\ arity
\not\Rightarrow Singularity;
\quad
Arity+FPNC+NF\Rightarrow AtMostOne.
}
\]

singularity burden 因此转化为：**FPNC 是否有独立依据？**

---

## 8. Current status

### Proven conditionally

\[
\boxed{
ALO+OW+NF+FPNC\Rightarrow ExactlyOneOpening.
}
\]

### Not established

\[
\boxed{
ALO+OW+NF\Rightarrow ExactlyOneOpening.
}
\]

### Also not established

\[
\boxed{
CenteredActuality\Rightarrow ExactlyOneOpening
}
\]

unless exact-one is simply built into that centered package.

---

## 9. New research burden

以后 singularity 只在以下结果出现时升级：

1. independent defense of List-style first-person compossibility；
2. proof that plural irreducible perspective modes cannot belong to one complete actuality；
3. proof that attempts to index the two centers necessarily demote them to merely relative/meta facts；
4. independent unity theorem that fixes the relevant compossibility standard。

在此之前：

\[
\boxed{
Singularity\text{ is reopened at FPNC, not solved.}
}
\]

## 关联

- [`first-person-non-compossibility-audit.md`](first-person-non-compossibility-audit.md)
- [`actuality-arity-singularity-gap.md`](actuality-arity-singularity-gap.md)
- [`obtaining-mode-pluralization.md`](obtaining-mode-pluralization.md)
- [`../models/role-first-absolute-opening.md`](../models/role-first-absolute-opening.md)
- [`../../literature/list-2025-quadrilemma-unitary-opening.md`](../../literature/list-2025-quadrilemma-unitary-opening.md)
