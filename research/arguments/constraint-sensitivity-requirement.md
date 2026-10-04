# Constraint-Sensitivity Requirement

> 状态：条件性工作结果。

## 0. 动机

一个很诱人的路线是：不显式“选择” center，而让 absolute center 成为整个现实约束系统的唯一 coherent solution。

形式上：

\[
\Phi(R,E)=0
\]

并希望：

\[
\exists!E^*\in\mathcal E_C:\Phi(R,E^*)=0.
\]

这看起来可以绕过 primitive selector。

但唯一性只有在约束真的对 center 敏感时才能出现。

---

## 1. Center-insensitive constraints

把完整非中心资料写成：

\[
B=(W,\Pi,\rho,\ldots).
\]

候选 center set：

\[
C(B)=\{E_1,E_2,\ldots\}.
\]

若全部约束实际上只依赖 \(B\)：

\[
\Phi(B,E)=\Psi(B)
\]

对所有 \(E\in C(B)\) 成立，则：

- 若 \(\Psi(B)\) satisfied，所有 centers 都是 solutions；
- 若 \(\Psi(B)\) unsatisfied，没有 center 是 solution。

因此不可能恰好一个。

即：

\[
\boxed{
\text{center-insensitive global coherence}
\not\Rightarrow
\text{unique center}
}
\]

---

## 2. Necessary condition

若：

\[
\exists!E^*:\Phi(B,E^*)=0,
\]

则至少存在某个 constraint component：

\[
\phi_k(B,E)
\]

满足：

\[
\phi_k(B,E_i)\neq\phi_k(B,E_j)
\]

对某些 candidates 成立。

所以 unique-center-by-coherence 必须包含：

\[
\boxed{\text{center-sensitive constraint}}
\]

暂称 **Constraint-Sensitivity Requirement**。

---

## 3. This does not evade Q

如果 \(\phi_k\) 的 center sensitivity 来自一个 independently motivated global relation：

\[
Q_R(E),
\]

那么 compatibility-singularity route 实质上仍然依赖：

\[
Q_R(E^*).
\]

如果 \(\phi_k\) 直接写成：

\[
E=E^*,
\]

或：

\[
Absolute(E),
\]

则只是把 primitive selector 写进 constraint system。

因此：

\[
\boxed{
\text{unique solution architecture}\text{ does not remove the need for an asymmetry-maker}
}
\]

它只把 asymmetry-maker 的位置从 selector 移到 equations。

---

## 4. Ordinary self-location does not suffice

若 center-sensitive constraints 来自 ordinary local context：

\[
K_i\Rightarrow E_i,
\]

那么每个主体都有自己的 analogous constraints：

\[
K_A\Rightarrow E_A,
\quad
K_B\Rightarrow E_B,
\ldots
\]

它们能解释 local centering，却产生多个 solutions across local domains。

所以 global unique solution 还需要：

\[
\boxed{\text{globally asymmetric center-sensitive constraint}}
\]

---

## 5. Relation to sheaf/global-section models

Sheaf compatibility 可以保证 local sections glue into one global section。

但只要 center choice 没有进入 compatibility equations，gluing 不会选择 a distinguished stalk / point。

若以后设计 centered sheaf，则必须明确指出：

\[
\text{哪条 gluing / compatibility condition 对 absolute center 敏感？}
\]

否则 absolute center 仍是外加数据。

---

## 6. Current verdict on Compatibility Singularity

“Absolute center is the unique globally coherent solution” 仍是一种可能架构，但它不能单独构成 explanation。

成功版本必须给出：

\[
\boxed{
\phi_{FP}(R,E)
}
\]

其中 \(\phi_{FP}\)：

1. independently motivated；
2. genuinely center-sensitive；
3. global / non-factorizable；
4. manifestation / actuality relevant；
5. has exactly one satisfying token event。

所以 Compatibility Singularity 被保留为 **implementation pattern**，而不是独立来源机制。
