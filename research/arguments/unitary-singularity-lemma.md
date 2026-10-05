# Unitary Singularity Lemma — SPC-Conditional Form

> 状态：2026-10-05 re-audited after Plural Opening Manifold。
>
> 旧版本把 `FPNC` 当作一个整体前提；当前版本进一步分解为 `Local Exclusivity + Single-Perspective Closure`。

## 0. Target

要推出：

\[
ExactlyOneOpening.
\]

拆成：

\[
AtLeastOneOpening
+
AtMostOneOpening.
\]

`ALO` 负责前者；本文件只审计后者。

---

## 1. ALO

在 centered actuality package 内，可以条件接受：

\[
\boxed{ALO:\quad \exists c\;Opening(c).}
\]

这只是 package-relative consequence，不证明 Centered Actuality 优于其他 completion theories。

---

## 2. Local Exclusivity

对 complete first-person states：

\[
X\perp Y
\]

表示 same perspective 不可能同时 instantiate 二者。

### LE

\[
\boxed{
X\perp Y
\Rightarrow
\neg\exists m\;[m\Vdash X\land m\Vdash Y].
}
\]

这是一项 local constraint；Plural Opening Manifold 也接受。

---

## 3. Single-Perspective Closure

### SPC

\[
\boxed{
Compossible_{FP}(F,G)
\Rightarrow
\exists m\;[m\Vdash F\land m\Vdash G].
}
\]

即 genuine first-person facts 若 qua first-person facts globally compossible，必须能从 one perspective jointly obtain。

这正是 Christian List-style compossibility 的核心读取。

---

## 4. FPNC as a derived premise

若：

\[
F_X=m_a\Vdash X,
\qquad
F_Y=m_b\Vdash Y,
\qquad
X\perp Y,
\]

假设：

\[
Compossible_{FP}(F_X,F_Y),
\]

由 SPC：

\[
\exists m\;[m\Vdash X\land m\Vdash Y],
\]

与 LE 冲突。

所以：

\[
\boxed{LE+SPC\Rightarrow FPNC.}
\]

当前不再把 FPNC 当作不可分析的 primitive bridge。

---

## 5. Non-Fragmentation under SPC

定义：

### NF-SPC

一个 actual totality中的 obtaining first-person facts均 globally compossible，且 compossibility 使用 SPC criterion。

于是若存在两个 distinct complete openings：

\[
Opening(a,X)
\land
Opening(b,Y),
\qquad
X\perp Y,
\]

由 NF-SPC 二者必须 compossible；由 LE+SPC 又 non-compossible。

矛盾。

所以：

\[
\boxed{
LE+SPC+NF_{SPC}
\Rightarrow
AtMostOneOpening.
}
\]

---

## 6. Exactly-one corollary

与 ALO 合并：

\[
\boxed{
ALO+LE+SPC+NF_{SPC}
\Rightarrow
ExactlyOneOpening.
}
\]

这保留 **Unitary Singularity Lemma** 的形式核心，但现在必须明确称为：

\[
\boxed{SPC\text{-conditional singularity theorem}.}
\]

---

## 7. Role of OneWorld

`OneWorld` 可以要求：

\[
\exists!R\;ActualWorld(R).
\]

但它本身不规定 reality 内部允许多少 irreducible obtaining modes。

Plural Opening Manifold 是直接 witness：

\[
OneWorld
+PluralIrreducibleFPModes
+ModePreservingGlobalCoherence.
\]

所以：

\[
\boxed{OneWorld\not\Rightarrow SPC.}
\]

`OneWorld` 仍可作为 theory package 的 world-count commitment，但不承担 singularity 的核心工作。

---

## 8. The countermodel

Plural Opening Manifold：

\[
\mathcal P=\langle W,C,M,F,A\rangle
\]

允许：

\[
m_a\Vdash X,
\qquad
m_b\Vdash Y,
\qquad
X\perp Y,
\]

并保持：

\[
\exists!R\;Actual(R).
\]

它使用：

\[
MPGC\text{ — Mode-Preserving Global Coherence}
\]

而非 SPC。

因此它不违反 ordinary logic，只违反 List-style NF / SPC。

这证明：

\[
\boxed{
OneActuality+IrreducibleFP+LE
\not\Rightarrow
AtMostOne.
}
\]

---

## 9. Relation to List quadrilemma

List 的：

\[
FPR+NS+NF+OW
\Rightarrow\bot
\]

仍成立于其 compossibility conception。

Plural model选择：

\[
FPR+NS+OW+\neg NF_{SPC}.
\]

所以它不是 counterexample to List；它是 List landscape 中一个 explicit one-world plural horn。

这也说明：

\[
\boxed{List\ theorem\ does\ not\ by\ itself\ choose\ which\ horn\ reality\ occupies.}
\]

---

## 10. Role-First bookkeeping

当前 strongest `role-first-absolute-opening.md` 规定：

\[
\exists!L_i\;Occupies(L_i,G).
\]

因此其 exact-one 已经是 primitive model essence。

不能同时：

1. 在 model definition 中 hard-code unique occupant；
2. 再把 USL 当作消除 exact-one primitive 的 independent theoretical gain。

若要获得 genuine derivation credit，需要另建：

\[
PreUniqueCenteredActuality
\]

只提供 `ALO/first-person arity`，不预设 one occupant，然后再由 SPC theorem推出 at-most-one。

---

## 11. Current burden

要把 USL 从 conditional theorem 升级为 strong positive result，需要独立 defend 至少一项：

1. genuine first-person compossibility constitutively requires SPC；
2. one actuality itself requires SPC；
3. MPGC / plural-opening model secretly collapses into third-person facts or many worlds；
4. MPGC violates an independently motivated stronger unity principle；
5. a global structure independently yields one perspective and thereby SPC。

当前均未完成。

---

## 12. Verdict

保留：

\[
\boxed{
ALO+LE+SPC+NF_{SPC}
\Rightarrow ExactlyOneOpening.
}
\]

拒绝过强表述：

\[
\boxed{
OneWorld+FirstPersonArity
\Rightarrow ExactlyOneOpening.
}
\]

当前最深 singularity question：

\[
\boxed{Why\ SPC?}
\]

## 关联

- [`perspective-closure-principle.md`](perspective-closure-principle.md)
- [`../models/plural-opening-manifold.md`](../models/plural-opening-manifold.md)
- [`first-person-non-compossibility-audit.md`](first-person-non-compossibility-audit.md)
- [`actuality-arity-singularity-gap.md`](actuality-arity-singularity-gap.md)
