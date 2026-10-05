# Unitary Singularity Lemma

> 状态：2026-10-05 positive argument / singularity audit。
>
> 目标：把 List-style first-person non-compossibility 与项目的 One World / Non-Fragmentation commitment结合，检验是否可以真正推出 absolute first-person opening 的 `at-most-one`，从而降低 LNP / Presence-Monism 的 uniqueness burden。

## 0. Target

此前核心 burden：

\[
LNP:\quad FirstPersonActuality(R)\Rightarrow ExactlyOneLocalRealization(R).
\]

一直没有 general proof。

本论证不直接推出整个 LNP，而是给一个条件版 uniqueness result：

\[
\boxed{
OneWorld+NonFragmentation+AtLeastOneIrreducibleOpening
\Rightarrow
ExactlyOneIrreducibleOpening.
}
\]

---

## 1. Definitions

令 complete reality 含一个 world：

\[
OW:\quad \exists!w\;RealityWorld(w).
\]

令：

\[
NF:\quad \forall F,G\in Facts(w),\;Compossible(F,G).
\]

即该 world 的 obtaining facts可共同实例化；没有 fragment-local incompatible fact stacks。

对 conscious stage `σ`，定义 strong first-person opening fact：

\[
A_\sigma:=AbsoluteFPFact(\sigma).
\]

其语义要求不是第三人称：

\[
ThereIsAPerspective(\sigma)
\]

而是 genuinely centered / simpliciter：

\[
\boxed{\text{this is the obtaining first-person opening}.}
\]

---

## 2. First-Person Non-Compossibility Premise

List-style result：对 distinct irreducible first-person centers `σ_i,σ_j`，若两者对应不同 complete first-person standpoints，则：

\[
\boxed{
A_{\sigma_i}\land A_{\sigma_j}
\Rightarrow
\neg Compossible(A_{\sigma_i},A_{\sigma_j}).
}
\]

直觉：两个第三人称 facts：

\[
S_i\text{ has experience }X,
\qquad
S_j\text{ has experience }Y
\]

可共同存在。

但两个 simpliciter first-person facts：

\[
I\text{ am in }X,
\qquad
I\text{ am in }Y
\]

若 `X/Y` 是 distinct mutually exclusive complete perspectives，则不能从同一 first-person center jointly obtain。

重要：这里真正使用的是：

\[
\boxed{IrreducibleFP+DistinctCenters\Rightarrow NonCompossibility.}
\]

不是 mere consciousness plurality。

---

## 3. At-Most-One theorem

假设反面：

\[
\exists \sigma_i\neq\sigma_j\;[A_{\sigma_i}\land A_{\sigma_j}].
\]

由 FP Non-Compossibility：

\[
\neg Compossible(A_{\sigma_i},A_{\sigma_j}).
\]

但 OW + NF 要求同一个 actual world 的所有 obtaining facts compossible。

矛盾。

所以：

\[
\boxed{
OW+NF+FPNC
\Rightarrow
\forall \sigma_i\neq\sigma_j\;\neg(A_{\sigma_i}\land A_{\sigma_j}).
}
\]

即：

\[
\boxed{AtMostOneAbsoluteOpening.}
\]

---

## 4. Exactly-one corollary

若另有：

\[
ALO:\quad \exists\sigma\;A_\sigma,
\]

则：

\[
\boxed{
OW+NF+FPNC+ALO
\Rightarrow
\exists!\sigma\;A_\sigma.
}
\]

这称为 **Unitary Singularity Lemma (USL)**。

其结构是：

\[
\underbrace{ALO}_{\ge1}
+
\underbrace{OW+NF+FPNC}_{\le1}
\Rightarrow
=1.
\]

---

## 5. Why this is genuine progress

旧 selective theory常把：

\[
\exists!\sigma\;Open(\sigma)
\]

作为 primitive law-content。

USL 允许把 uniqueness 从 Opening Law 中剥离：

### Opening Law / Presence principle 只负责

\[
\exists\sigma\;Open(\sigma).
\]

### Unitary Reality 负责

\[
\le1.
\]

这样 law 不需要同时支付：

- opening existence；
- exact-one multiplicity；

两个独立内容。

理论结构变成：

\[
\boxed{
AtLeastOneOpening
+
UnitaryReality
\to
ExactlyOneOpening.
}
\]

---

## 6. Connection to Presence-Simpliciter

Hare/Conitzer route 若能给：

\[
PresenceSimpliciter(E^*)
\Rightarrow
A_{\sigma^*},
\]

则：

\[
PresenceSimpliciter
+
OW+NF+FPNC
\Rightarrow
ExactlyOneI\text{-}NOWOpening.
\]

这把之前的：

\[
PresenceSimpliciter\not\Rightarrow ExactlyOnePresence
\]

精确改写成：

\[
\boxed{
PresenceSimpliciter+UnitaryReality
\Rightarrow
ExactlyOneIrreduciblePresence,
}
\]

条件是 multiple simpliciter presences若 belong to distinct irreducible first-person centers，就属于 FPNC 的适用域。

Effingham-style multiple presents因此仍可作为 countermodel，但它必须拒绝/修改 NF，或者不把 multiple presents解释为 distinct irreducible first-person openings。

---

## 7. Two-Tier Escape from List Quadrilemma

List 的 FPR 是 universal：

\[
\forall S\,[Conscious(S)\to IrreducibleFPFact(S)].
\]

项目不需要它。

采用：

\[
\forall S\;Conscious(S),
\]

\[
\forall S\;LocalFPOrganization(S),
\]

同时只承认：

\[
\exists!\sigma^*\;IrreducibleAbsoluteFPFact(\sigma^*).
\]

所以：

\[
\boxed{
NonSolipsism
+
OneWorld
+
NonFragmentation
+
SingularAbsoluteFP
}
\]

是 coherent-looking package。

ordinary subjects仍有 genuine phenomenal life；被拒绝的是：

\[
\forall S\;StrongIrreducibleFPFact(S).
\]

这正是项目一直要求的 ordinary/absolute distinction。

---

## 8. Relation to Universal-I

USL 不区分：

### Selective Opening

\[
\exists!\sigma^*\;AbsoluteOpening(\sigma^*).
\]

### Universal-I

\[
\exists!I_U\;\forall e\;ExperienceOf(e,I_U).
\]

因为 Universal-I 可以把所有 local experiences归入一个 numerical first-person center。

所以 USL 的真正作用是：

\[
\boxed{
PluralIndependentIrreducibleCenters
\text{ are incompatible with }OW+NF.
}
\]

one-world unitary theory 的 first-person space因此主要剩：

\[
\boxed{
SelectiveOpening
\quad|\quad
UniversalI.
}
\]

接下来仍需要 LNP-vs-Universal-I comparison 来决定 locality。

---

## 9. Same-subject / diachronic caveat

USL 不应该误写成：

> 整个历史上只能有一个 opening stage。

项目当前 Stage-First 模型允许：

\[
\sigma_t\to\sigma_{t+1}.
\]

不同时间的 stages 可以是一个 diachronic opening path 的不同 temporal aspects。

USL 最自然的 scope 是：

\[
\boxed{
AtMostOne\ mutually\ exclusive\ absolute\ first\!\!\text{-}\!person\ opening\ per\ complete\ actuality\ index.
}
\]

path persistence 仍由 PSP / stochastic grounding 单独处理。

---

## 10. Main objections

### O1 — Reject NF

fragmentalist 可直接允许 non-compossible first-person facts位于不同 fragments。

USL 因此不能 refute fragmentalism。

### O2 — Reject FP non-compossibility

可尝试把：

\[
I_i\text{ am }X
\]

重述为：

\[
ThereIsPerspective_i(X).
\]

这样 facts compossible。

但这正会把 strong irreducible FP fact降格为第三人称 meta-fact，落回 Representation–Fact Gap / relative-FP demotion。

### O3 — Reject one world

List-style many-centred-worlds theory可保持每个 world internally coherent。

项目若独立坚持 one actuality / one world，则不采取此 horn。

### O4 — Universal-I

one center may encompass many local streams；USL alone不排除。

这是当前 strongest internal rival。

---

## 11. Current verdict

本轮首次出现一个非循环的 uniqueness derivation：

\[
\boxed{
AtLeastOneIrreducibleOpening
+
OneWorld
+
NonFragmentation
+
FPNonCompossibility
\Rightarrow
ExactlyOneIrreducibleOpening.
}
\]

所以：

\[
\boxed{Singularity\text{ need not be independently primitive}.}
\]

当前最深 burden 从：

\[
Why\ exactly\ one?
\]

进一步收缩为：

1. **At-Least-One**：为什么 complete actuality含任何 irreducible first-person opening？
2. **Locality vs Universal-I**：为什么 one center局域为一个 stage/path，而不是 universal across experiences？
3. **Unitary Reality**：为什么接受 OW + NF 而不是 fragmentalism / many worlds？

这是对 LNP / Presence-Monism frontier 的实质升级。

## 关联

- [`../../literature/list-2025-quadrilemma-unitary-opening.md`](../../literature/list-2025-quadrilemma-unitary-opening.md)
- [`../../synthesis/frontier-2026-10-05-local-opening-presence-monism.md`](../../synthesis/frontier-2026-10-05-local-opening-presence-monism.md)
- [`presence-localization-universalism-fork.md`](presence-localization-universalism-fork.md)
- [`../models/stage-first-opening.md`](../models/stage-first-opening.md)
- [`stochastic-grounded-opening-path.md`](stochastic-grounded-opening-path.md)
