# Spontaneous Absolute-Orientation Breaking (SAOB)

> 状态：2026-10-05 constructive nomological model。
>
> 目标：把 absolute first-person privilege 建模为一种 **symmetry-respecting law + symmetry-broken complete realization**，从而同时绕开 deterministic canonical-selector obstruction 与不必要的 primitive token labels。

## 0. Core idea

此前 deterministic PLP 想从 neutral base：

\[
R
\]

直接计算：

\[
E^*=F(R).
\]

若 \(R\) 有 automorphism交换两个 perfect duplicate subjects：

\[
\phi(E_A)=E_B,
\]

任何 purely invariant deterministic \(F\) 都不能唯一挑出其中一个。

SAOB 改变 architecture：law 不在 symmetric base 中预编码 winner，而只规定 complete realization 必须属于一个 symmetry-broken outcome family。

---

## 1. Candidate set and symmetry group

令 genuine local conscious loci 为：

\[
S(R)=\{E_1,\ldots,E_n\}.
\]

令：

\[
G=Aut(R)
\]

作用在 \(S(R)\) 上。

对于 exact-duplicate orbit：

\[
O=\{E_{i_1},\ldots,E_{i_k}\},
\]

任意成员在 neutral base 中都没有 invariant property 可作为 winner marker。

---

## 2. Absolute-orientation order parameter

引入一个 complete-level order parameter：

\[
A:S(R)\to\{0,1\}.
\]

解释：

\[
A(E_i)=1
\iff
AbsoluteOrientation(E_i).
\]

law-level constraint：

\[
\boxed{
\sum_{E_i\in S(R)}A(E_i)=1.
}
\]

因此任何 admissible complete realization都满足：

\[
\exists!E^*\;A(E^*)=1.
\]

但 law本身不指定哪一个 pre-labelled token必须取 1。

---

## 3. Symmetry-respecting law, asymmetric realization

令 law 为：

\[
\Lambda_{SAOB}.
\]

要求 covariance：若 \(A\) 是一个允许的 realization，则对任何 \(g\in G\)：

\[
A_g(E)=A(g^{-1}E)
\]

也是允许的 realization。

所以 law-space 保留：

\[
G\text{-symmetry}.
\]

而 actual completed world：

\[
\Omega=(R,A^*)
\]

只保留 stabilizer subgroup：

\[
Stab(A^*)\subsetneq G.
\]

即：

\[
\boxed{
LawSymmetry
+
ActualAsymmetry.
}
\]

这是 spontaneous-symmetry-breaking style structure。

---

## 4. Relation to Halvorson D3-style indeterminism

Halvorson–Manchak–Weatherall 2026 的 formal lesson：一个 initial segment的 automorphism未必能延伸成 full-model automorphism。

这里：

\[
g\in Aut(R)
\]

交换两个 candidate subjects，但若其中只有一个满足 \(A=1\)，则通常：

\[
g\notin Aut(\Omega).
\]

因此：

\[
\boxed{
Aut(R)\not\to Aut(\Omega)
}
\]

给一个纯结构意义的 symmetry-breaking completion。

这允许：

\[
\boxed{
AntiHaecceitism
+
AsymmetricCompleteActuality
}
\]

至少 formal 上共存。

---

## 5. Three readings of the outcome space

### H1 — Token-haecceitistic chance

把：

\[
A(E_A)=1
\]

与：

\[
A(E_B)=1
\]

当作由 pre-existing token identities区分的 distinct worlds。

优点：ordinary token-indexed chance直观。

代价：恢复 haecceitistic structure。

### H2 — Quotient outcome

若两个 marked structures只差 base automorphism，则 quotient：

\[
\Omega_A\sim\Omega_B.
\]

于是只有一个 structural outcome type：

\[
\exists!E^*\;Absolute(E^*).
\]

优点：强 anti-haecceitism。

代价：没有普通意义的 `P(A wins)=1/2` token lottery。

### H3 — Structural symmetry-breaking extension

不通过 possible-world token counting定义 indeterminism，而通过：

\[
\boxed{
\text{base symmetries是否能唯一延伸到 completed structure}
}
\]

刻画。

该 reading 最接近 Halvorson formalism，也是目前项目最有希望的 route。

---

## 6. Chance is optional, not automatic

SAOB 可以是：

### SAOB-I — bare indeterministic / symmetry-breaking law

law只允许 symmetry-related asymmetric completions，而不定义 numerical chance。

### SAOB-P — probabilistic law

进一步给 measure：

\[
\mu_R
\]

作用在 admissible extensions / realizations 上。

若 \(g\in G\)，要求：

\[
\mu_R(X)=\mu_R(gX).
\]

在 finite transitive orbit 且无额外 asymmetry时，可得到 equal weighting；但 **equal probability 需要 measure/dynamics，不能从 symmetry alone 推出**。

因此：

\[
\boxed{Symmetry\not\Rightarrow Chance.}
\]

Liu 对 classical SSB/chance 的讨论给这一点现成方法论警告。

---

## 7. Why this improves on deterministic dominance

Kadić-style dominance要求：

\[
R\Rightarrow\exists!E_D\;Dominant(E_D).
\]

perfect symmetry让这一 deterministic derivation失败。

SAOB只要求：

\[
R+\Lambda_{SAOB}
\Rightarrow
\text{allowed completions each contain exactly one root}.
\]

因此：

\[
\boxed{
ExactSymmetry
\not\Rightarrow
NoUniqueAbsoluteRealization.
}
\]

它只意味着：winner不能由 symmetric base **预先决定**。

---

## 8. The `why this one?` question splits in two

SAOB迫使原问题分层。

### Q1 — Why is there exactly one absolute root?

回答候选：

\[
\Lambda_{SAOB}
\]

本身要求 one-hot order parameter。

这是 law-explanation。

### Q2 — Why did this pre-existing numerical token receive the root?

在 H1 下：fundamental chance / brute law-outcome可以终止 why-chain。

在 H2/H3 anti-haecceitist reading 下，更激进的回答是：

\[
\boxed{
\text{there is no additional pre-role transworld token fact to explain}.}
\]

complete world只包含：

\[
\text{one role-bearing subject and the rest non-role-bearing},
\]

并不另含：

> A as numerically pre-labelled across worlds happened to win.

因此部分 `why A rather than B?` 可能依赖一个 project并不需要接受的 haecceitistic cross-world question。

---

## 9. But the deepest problem survives: privilege content

即使 SAOB 完美解决：

- exact-one；
- symmetry；
- anti-haecceitism；
- chance / indeterminism；

仍要问：

\[
\boxed{
Why\ is\ A=1\ interpreted\ as\ AbsoluteOrientation?
}
\]

如果 `A` 只是一个 arbitrary metaphysical mark，那么理论没有解释 first-person privilege。

所以 SAOB 必须把 order parameter的 role与一个 **privilege-sensitive job** 绑定。

候选：

1. actuality realization；
2. Bitbol-style Mind-identification；
3. direct / factive acquaintance with absolute status；
4. I–NOW unity；
5. special psychophysical role。

目前没有任何一项独立强制：

\[
A=AbsoluteI.
\]

这叫 **Order-Parameter Semantics Gap**。

---

## 10. Epistemic coupling option

一个加强版 law package：

\[
\Lambda_{SAOB+K}
\]

除 one absolute root 外还规定：

\[
Absolute(E^*)
\Rightarrow
FactiveAcquaintance(E^*,Absolute(E^*)).
\]

这会让 selected subject具有 winner-specific epistemic status。

它可利用普通 acquaintance theory的结构先例：某些 self-knowledge可以来自 direct awareness，而不是推理。

但必须区分两种版本。

### Phenomenally distinctive acquaintance

若 acquaintance本身产生可识别 phenomenal signature：

\[
\sigma_\Omega,
\]

则 potentially：

\[
P(\sigma_\Omega\mid Absolute)=1,
\quad
P(\sigma_\Omega\mid\neg Absolute)=0.
\]

这会成为真正 privilege-sensitive evidence channel。

当前没有独立 evidence 证明我们拥有这种 signature。

### Non-phenomenal factive entitlement

若 winner只是 epistemic status不同，但 ordinary evidence完全相同，则仍可能：

\[
SameEvidence\not\Rightarrow SameKnowledge,
\]

但 Bayes likelihood不变：

\[
BF=1.
\]

因此只改善 knowability，不改善 evidential support。

---

## 11. Comparison with Role-First Ω

### Role-First Ω

\[
\Omega[R;E^*]
\]

center/orientation直接 constitutive。

### SAOB

\[
R
+
\Lambda_{SAOB}
\to
(R,A^*)
\]

其中 complete world contains one symmetry-breaking absolute root。

SAOB新增的 explanatory structure：

- why exactly-one is law-governed；
- why symmetric candidates need no deterministic differentiator；
- modal / counterfactual outcome space；
- optional objective chance；
- formal anti-haecceitist reading via extension symmetry。

Role-First Ω 更 ontologically economical；SAOB 更 dynamically / nomologically articulated。

二者真正竞争点现在不是 primitive count，而是：

\[
\boxed{
Does\ law-governed\ symmetry\ breaking\ explain\ anything\ that\ constitutive\ centered\ actuality\ leaves\ brute?
}
\]

---

## 12. Current verdict

SAOB 是目前项目最强的 **nomological PLP architecture**。

它真实地解决/缓解了此前两个障碍：

\[
\boxed{
DeterministicCanonicalityObstruction
}
\]

和：

\[
\boxed{
AsymmetryRequiresHaecceitism
}
\]

至少后者不再是 exhaustive objection。

所以：

\[
\boxed{
DerivedPLPNearClosure
\text{ is genuinely reopened by structural symmetry breaking}.
}
\]

但它没有独立证明 absolute-first-person thesis，因为核心 burden已收缩成：

\[
\boxed{
OrderParameterSemanticsGap:
\quad
Why\ should\ the\ one\ broken\ root\ be\ AbsoluteI?
}
\]

如果这个 gap只能由 definition关闭，SAOB最终仍只是对 primitive privilege 的 law-shaped packaging。

## 关联

- [`../../literature/halvorson-2026-symmetry-indeterminism.md`](../../literature/halvorson-2026-symmetry-indeterminism.md)
- [`../../literature/psychophysical-subject-selection-laws.md`](../../literature/psychophysical-subject-selection-laws.md)
- [`../arguments/stochastic-absolute-orientation-law.md`](../arguments/stochastic-absolute-orientation-law.md)
- [`../arguments/dominance-privilege-bridge-audit.md`](../arguments/dominance-privilege-bridge-audit.md)
- [`maximal-fusion-dominant-locus.md`](maximal-fusion-dominant-locus.md)
