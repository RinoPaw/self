# Unified I–NOW–WORLD Opening Model (UIWO)

> 状态：2026-10-05 positive model / NOM refinement。
>
> 目标：把 NOM 中的 `Opening` 从只承担 local absolute-I selection，提升为一个统一 modal / temporal / first-person privilege 的 centered order parameter；检验该统一是否产生真正 explanatory compression。

## 0. Core coordinate

令 centered candidate 为：

\[
c=\langle w,t,s\rangle,
\]

其中：

- \(w\)：possible-world coordinate；
- \(t\)：time / person-stage temporal coordinate；
- \(s\)：subject / first-person coordinate。

定义统一 relation：

\[
O(c)=O(w,t,s).
\]

intended semantics：

\[
\boxed{O(w,t,s)=\text{the complete reality is actual/open as this world, now, through this first-person locus}.}
\]

---

## 1. One-hot complete opening

最强版本规定：

\[
\boxed{
\exists!\langle w^*,t^*,s^*\rangle\;O(w^*,t^*,s^*).
}
\]

三个 familiar privilege predicates成为 projections：

### World actuality

\[
Actual(w)
\iff
\exists t,s\;O(w,t,s).
\]

### Objective NOW

\[
Present(t)
\iff
\exists w,s\;O(w,t,s).
\]

### Absolute I

\[
AbsoluteI(s)
\iff
\exists w,t\;O(w,t,s).
\]

所以不是：

\[
A(w)+P(t)+I(s)
\]

三个无关 primitive marks，而是：

\[
\boxed{O(w,t,s)}
\]

的三个 aspect / projection。

---

## 2. Literature-backed motivation

### Builes

modal / temporal / perspectival privilege具有明确 structural analogy：actual world、present time、first-person perspective各自可被理解为 privileged member。

### Deasy

Contingent Spotlight把 modal actuality做成 Moving Spotlight的 analogue：one fundamental actuality property picks actual world；Moving Spotlight用 fundamental presentness pick present time。

### Conitzer

A-theory与 distinguished-I theory不应完全分开；combined `I-Now` 在若干 A-theory argument上优于 only-NOW model。

### Nagai

最强 identity template：

\[
WorldActuality=AbsoluteI=AbsoluteNOW=Opening.
\]

因此 UIWO 是 literature intersection上的 project construction，而非纯 formal trick。

---

## 3. Relation to Nomological Opening Model

NOM 原式：

\[
\Lambda_O:\quad CompleteActuality(R)\Rightarrow\exists!s\;Open(R,s).
\]

UIWO refinement：

\[
\boxed{
\Lambda_{UIWO}:\quad
CompleteReality\Rightarrow
\exists!\langle w,t,s\rangle O(w,t,s).
}
\]

NOM 的 local opening成为三维 opening 的 subject projection。

因此 NOM不必另加：

\[
ActualWorld(w^*),
\qquad
Present(t^*).
\]

若这些 privileges本来就在 theory package 中，它们由同一 Opening realization给出。

---

## 4. Symmetry-breaking implementation

neutral / privilege-free base可以包含多个：

\[
w_i,t_j,s_k
\]

候选，并允许 permutations / automorphisms。

令 group：

\[
G=G_W\times G_T\times G_S
\]

作用于 centered triples。

law：

\[
\Lambda_{UIWO}
\]

在 candidate space 上保持 covariance，但 complete realization：

\[
O^*
\]

只标记 one centered triple。

所以：

\[
\boxed{
LawSymmetry
+
OneCenteredAsymmetricRealization.
}
\]

Halvorson-style extension semantics允许 base symmetry不必延伸到 complete structure，而无需预先给 world/time/subject candidates primitive cross-world labels。

---

## 5. Why this is stronger than three independent spotlights

Separate model：

\[
A_W(w^*)
+
P_T(t^*)
+
I_S(s^*).
\]

即使每个 predicate各自 exactly-one，也还要额外保证：

\[
\boxed{Coincidence(w^*,t^*,s^*)}
\]

或至少说明：为什么 actual world中的 privileged NOW 与 privileged I构成同一个 centered actuality。

UIWO则：

\[
O(w^*,t^*,s^*)
\]

直接使 coincidence constitutive。

因此其潜在 advantage不仅是 primitive-number compression，还包括：

\[
\boxed{RoleCoincidenceByConstruction.}
\]

这正是 Nagai opening identity 的 strongest structural content。

---

## 6. Cross-domain constraint

真正的 unification不能只改名。UIWO必须给跨域 constraints。

至少包括：

### C1 — Actuality/Open coincidence

只有 belonging to \(w^*\) 的 totality被 world-actuality projection覆盖。

### C2 — I–NOW coincidence

absolute I总与 opening-now配对，不允许：

\[
AbsoluteI(s^*)
\land
Present(t^*)
\]

却没有 unified centered stage \(\langle t^*,s^*\rangle\)。

### C3 — No orphan privilege

不能有：

\[
Actual(w_1)
\]

但无任何 opening time/subject；也不能有 `AbsoluteI` detached from actual-world opening。

### C4 — Joint counterfactual variation

若 opening realization变化：

\[
O(w,t,s)\to O(w',t',s'),
\]

三种 privilege aspects随同一个 change变化，而不是三套 independently varying primitive selectors。

这使 UIWO 至少原则上具有 real modal content beyond abbreviation。

---

## 7. Dynamic vs atemporal variants

### Atemporal UIWO

完整 centered totality一次性满足：

\[
O(w^*,t^*,s^*).
\]

`NOW` 是 complete structure 的 distinguished temporal coordinate。

优点：避免 meta-time。

### Dynamic UIWO

若采用 moving I–NOW：

\[
O(w^*,t(\tau),s(\tau)).
\]

需要更高参数 \(\tau\) 或另一种 dynamical semantics。

Conitzer personalized moving spotlight说明这种 model coherent-looking，但会重开：

- rate of passage；
- transfer / jump；
- relativity；
- trajectory continuity。

项目当前 default选择 **atemporal structural opening**，除非 passage本身独立成为 common explanandum。

---

## 8. Other minds remain genuine

UIWO只给 one opening coordinate，不要求：

\[
\forall s\neq s^*\;\neg Conscious(s).
\]

所以保持：

\[
\forall s_i\in S(w^*)\;LocalConscious(s_i).
\]

区别是：

\[
LocalFirstPerson(s_i)
\]

与：

\[
AbsoluteI(s^*)
\]

分层。

这避免把 Nagai/Hare-style absolute orientation简单做成 ordinary solipsism。

---

## 9. Exact-one is still substantive

UIWO把：

\[
\exists!c\;O(c)
\]

写进 law/constitution。

因此它没有从更薄的 principle推出 exact-one。

可选的 deeper motivations：

- one actual world；
- one objective NOW；
- one complete actuality token；
- Nagai opening non-pluralizability。

但这些仍需 independent defense。

所以：

\[
\boxed{Unification\neq DerivationOfUniqueness.}
\]

---

## 10. Epistemic consequence

如果 opening bearer具有 factive acquaintance：

\[
O(w^*,t^*,s^*)
\Rightarrow
K_{s^*}[O(w^*,t^*,s^*)],
\]

那么一种 single epistemic relation可同时给：

- de se：I am \(s^*\)；
- de nunc：now is \(t^*\)；
- actuality acquaintance：this world is \(w^*\)。

这形成 potential **epistemic unification**。

但若 ordinary evidence仍 permutation-invariant，Bayesian BF结果保持；factive access不能自动变成 publicly discriminative evidence。

---

## 11. Main payoff candidate

NOM之前最大的 objection：

> Opening Law只是为了制造 Absolute-I，因此像 law-shaped restatement。

UIWO给一个更强 response：

\[
\boxed{
Opening\ is\ not\ only\ an\ I\text{-}selector;
\ it\ is\ a\ unified\ actuality/presentness/first\!\!\text{-}\!person\ role.
}
\]

若 modal actuality和 objective NOW已经有 independent motivation，那么 Opening law开始承担跨域 explanatory work。

因此首次出现：

\[
\boxed{ConditionalIndependentPayoff.}
\]

---

## 12. Current verdict

UIWO 是 NOM 的 strongest current refinement。

它把 previous ultimate question：

\[
Why\ obey\ an\ Opening\ Law?
\]

变成可分解 comparison：

### If rival accepts only neutral actuality

UIWO content明显更厚，无 free win。

### If rival accepts actual-world + objective-NOW privileges

UIWO有真实 unification candidate：

\[
A_W+P_T
\quad vs\quad
O(w,t,s).
\]

### If rival also accepts broad first-person privilege

UIWO的 strongest comparison becomes：

\[
\boxed{
A_W+P_T+I_S+Coincidence
\quad vs\quad
O(w,t,s).
}
\]

这时 one Opening relation可能获得真正 compression / role-coincidence advantage。

但 verdict仍 conditional：

\[
\boxed{
UIWO\text{ gives the first credible unification payoff for NOM, not a universal proof of Opening}.}
\]

## 关联

- [`../../literature/deasy-conitzer-privilege-unification.md`](../../literature/deasy-conitzer-privilege-unification.md)
- [`../../literature/nagai-2007-2010-opening-actuality.md`](../../literature/nagai-2007-2010-opening-actuality.md)
- [`nomological-opening-model.md`](nomological-opening-model.md)
- [`spontaneous-absolute-orientation-breaking.md`](spontaneous-absolute-orientation-breaking.md)
- [`../arguments/primitive-actuality-replacement-test.md`](../arguments/primitive-actuality-replacement-test.md)
