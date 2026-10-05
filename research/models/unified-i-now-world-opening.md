# Unified I–NOW–WORLD Opening Model (UIWO)

> 状态：2026-10-05 positive model / NOM refinement，已通过 Factorization Test 修正。
>
> 目标：把 NOM 中的 `Opening` 建模为 modal / temporal / first-person privilege 的统一 centered order parameter，同时严格区分 genuine unification 与 mere conjunction。

## 0. Core coordinate

令 centered candidate 为：

\[
c=\langle w,t,s\rangle,
\]

其中：

- \(w\)：possible-world coordinate；
- \(t\)：time / person-stage coordinate；
- \(s\)：subject / first-person coordinate。

定义：

\[
O(c)=O(w,t,s),
\]

intended semantics：

\[
\boxed{
O(w,t,s)=\text{complete reality is actual/open as this world, now, through this first-person locus}.
}
\]

最强版本规定：

\[
\boxed{
\exists!\langle w^*,t^*,s^*\rangle\;O(w^*,t^*,s^*).
}
\]

三个 privilege aspects 为 projections：

\[
Actual(w)\iff\exists t,s\;O(w,t,s),
\]

\[
Present(t)\iff\exists w,s\;O(w,t,s),
\]

\[
AbsoluteI(s)\iff\exists w,t\;O(w,t,s).
\]

---

## 1. Literature-backed motivation

UIWO 不是任何一个现有作者的完整理论，而是几条 literature lines 的 intersection。

### Builes

modal / temporal / perspectival privilege 有明确 structural analogy：

\[
ActualWorld:PossibleWorlds,
\]

\[
PresentTime:Times,
\]

\[
MyPerspective:Perspectives.
\]

但 analogy 本身不是 identity。

### Deasy

Contingent Spotlight 把 modal actuality 做成 Moving Spotlight 的 analogue：one fundamental actuality property 产生 actual-world privilege；Moving Spotlight 使用 fundamental presentness。

### Conitzer

A-theory 的若干动机对 combined `I–NOW` 比对 `NOW` alone 更强；distinguished I + distinguished Now 也直接产生一个 distinguished centered location / Here。

这最后一点对 UIWO 很重要：它支持 joint motivation，同时也说明 mere centered coincidence 不需要额外第四 primitive。

### Nagai

最强 identity template：

\[
\boxed{
WorldActuality=AbsoluteI=AbsoluteNOW=Opening.
}
\]

Nagai 因而是 UIWO 真正 non-factorizable reading 的主要 semantic ancestor。

---

## 2. Relation to Nomological Opening Model

旧 NOM：

\[
\Lambda_O:\quad CompleteActuality(R)\Rightarrow\exists!s\;Open(R,s).
\]

UIWO：

\[
\boxed{
\Lambda_{UIWO}:\quad CompleteReality\Rightarrow\exists!\langle w,t,s\rangle O(w,t,s).
}
\]

如果 world actuality 与 objective NOW 本来就在 theory package 中，UIWO 尝试让它们成为同一 Opening 的 projections，而不是增加一个纯 I-selector。

但这只有在 Opening 通过下面的 Factorization Gate 时才有 explanatory significance。

---

## 3. Factorization correction

最初模型有一个过强说法：three separate exactly-one spotlights 还需要额外 `Coincidence(w*,t*,s*)` primitive。

这一般不成立。

设 rival 已有：

\[
\exists!w^*\;A(w^*),
\]

\[
\exists!t^*\;P(t^*),
\]

\[
\exists!s^*\;I(s^*),
\]

并有双方共享的 ordinary compatibility relation：

\[
C(w,t,s).
\]

则可直接定义：

\[
\boxed{
O_\times(w,t,s)
:=A(w)\land P(t)\land I(s)\land C(w,t,s).
}
\]

只要 privileged members compatible，就自动有 one centered triple。

所以：

\[
\boxed{
ThreeUniquePrivileges
\not\Rightarrow
ExtraCoincidencePrimitive.
}
\]

因此 UIWO 不能靠 “three predicates become one ternary predicate” 获得 credit。

---

## 4. Projection–Factorization Result

若：

\[
O(w,t,s)
\equiv
A(w)\land P(t)\land I(s)\land C(w,t,s),
\]

则 `O` 称为 **factorizable**。

在这种情况下：

\[
\boxed{
FactorizableOpening
\text{ has no explanatory gain merely from arity compression}.
}
\]

因为：

- `O` 的 truth conditions 完全由 separate predicates 决定；
- exactly-one triple 由 exactly-one marginals 自动给出；
- projections 没有增加 modal / counterfactual content；
- one relation symbol vs three predicate symbols 只是表示选择。

这是 UIWO 必须遵守的 **Projection–Factorization Result (PFR)**。

---

## 5. Genuine UIWO must be non-factorizable

真正的 Unified Opening 需要：

\[
\boxed{O\neq O_\times.}
\]

至少需要以下一种 cross-domain coupling。

### U1 — Combination exclusion

有些 world/time/subject privilege values 在 marginals 上分别允许，却不能 jointly instantiate one Opening：

\[
Possible[A(w_i)]
\land Possible[P(t_j)]
\land Possible[I(s_k)]
\]

但：

\[
\neg Possible[O(w_i,t_j,s_k)].
\]

### U2 — Joint counterfactual dependence

改变 one privilege aspect 会 lawfully constrain others：

\[
do(O_w=w')
\Rightarrow
Constraint(O_t,O_s).
\]

### U3 — Non-product chance

若 Opening stochastic：

\[
\boxed{
P_O(w,t,s)
\neq
P_A(w)P_P(t)P_I(s).
}
\]

且 correlation 来自 independently motivated law，而不是手工关联。

### U4 — One common ground

存在 independently characterized `G`：

\[
G\Rightarrow Actual(w^*)+Present(t^*)+AbsoluteI(s^*),
\]

并且三个 independent grounds 无法同样好地解释共同现象。

### U5 — Shared explanatory residual

竞争双方都承认某个跨域 explanandum `X`，而：

\[
Explain(O,X)
\land
\neg Explain(A+P+I,X).
\]

只有 U1–U5 这类内容才能让 Opening 真正承担 unification work。

---

## 6. Symmetry-breaking implementation

privilege-free base可含多个候选：

\[
w_i,t_j,s_k,
\]

并有 symmetry group：

\[
G=G_W\times G_T\times G_S.
\]

Opening law 在 candidate level 可保持 covariance，但 realized complete structure只含 one root：

\[
\exists!c^*\;O(c^*).
\]

Halvorson-style model-extension semantics允许：

\[
Aut(R)\ni\phi,
\qquad
\phi\notin Aut(R+O),
\]

即 symmetric base 获得 asymmetric rooted completion，而不必预先给 candidate tokens primitive haecceities。

因此 symmetry breaking 仍是 UIWO / NOM 的重要 architecture。

但：

\[
\boxed{
SymmetryBreaking
\not\Rightarrow
CrossDomainUnification.
}
\]

它解决 realization form，不解决 Opening 是否可 factorize。

---

## 7. Analogy-to-Identity Gap

Builes / Deasy / Conitzer 显示：

\[
ModalPrivilege\sim TemporalPrivilege\sim FirstPersonPrivilege.
\]

但：

\[
\boxed{
PrivilegeAnalogy
\not\Rightarrow
PrivilegeIdentity.
}
\]

world–time literature本身也警告 analogy 有断点。Ulrich Meyer 2006 明确论证 worlds 与 times 的 formal parallels 不能无限推广，并反对简单把 presentism 当作 actualism 的 tense analogue。Iaquinto 2026 继续把 time/modality parallel当重要研究框架，但这仍是 analogy map，不是 identity theorem。

所以 Nagai-style identity 仍是 extra metaphysical content。

---

## 8. Conitzer's real contribution after PFR

PFR 不削掉 Conitzer 的核心价值。

Conitzer 的 result 更准确写成：

\[
\boxed{
Motivation(A\text{-}theory)
\Rightarrow
PressureTowardPersonalizedA\text{-}theory.
}
\]

其主要理由包括：

- presence simpliciter 对 distinguished I 与 NOW 同时施压；
- `Thank goodness` / self-bias cases 对 I–NOW 更有解释力；
- 某些针对 global NOW 的 relativity objections 对 local I–NOW 版本更弱。

这给的是 **joint explanatory motivation**，可能帮助 UIWO 建立 U5。

它尚未给：

\[
O\neq O_\times.
\]

---

## 9. Nagai's role after PFR

Nagai 是当前 strongest non-factorization template。

他的主张不是：

\[
Actual(w^*)\land Present(t^*)\land I(s^*).
\]

而是：

\[
\boxed{
WorldActualization
=
NOWActualization
=
IActualization
=
OneOpening.
}
\]

若这一 identity 被接受，Opening 确实不是 conjunction。

但项目仍要问：

\[
\boxed{
Why\ identity\ rather\ than\ factorization?
}
\]

Nagai 允许 sheer contingency / primitive opening，因此给成熟 endpoint，却没有从 neutral ground 推出 non-factorization。

---

## 10. Dynamic vs atemporal variants

### Atemporal UIWO

\[
O(w^*,t^*,s^*)
\]

作为 complete centered structure 的 distinguished coordinate。

优点：避免 meta-time / passage-rate problem。

### Dynamic UIWO

\[
O(w^*,t(\tau),s(\tau)).
\]

需要 supertime 或另一种 dynamical semantics，并重开：

- rate of passage；
- subject transfer / jump；
- relativity；
- trajectory continuity。

当前项目 default 仍是 **atemporal rooted Opening**，除非 objective passage 本身独立成为 common explanandum。

---

## 11. Other minds remain genuine

UIWO 不要求：

\[
\forall s\neq s^*\;\neg Conscious(s).
\]

仍可有：

\[
\forall s_i\in S(w^*)\;LocalConscious(s_i).
\]

并严格区分：

\[
LocalFirstPerson(s_i)
\]

与：

\[
AbsoluteI(s^*).
\]

所以 UIWO 是 two-tier model，不等于 ordinary solipsism。

---

## 12. Epistemic projection

若 Opening bearer 有 factive acquaintance：

\[
O(w^*,t^*,s^*)
\Rightarrow
K_{s^*}[O(w^*,t^*,s^*)],
\]

同一 relation可投影成：

- de se acquaintance；
- de nunc acquaintance；
- actuality acquaintance。

这有 potential epistemic-unification value。

但如果三类 knowledge 本来也可以分别由 status-sensitive entitlement 给出，仍需通过 PFR 对应的 epistemic non-factorization test。

普通 evidence permutation-invariant 时：

\[
BF=1
\]

结果保持。

---

## 13. Revised compression comparison

### Separate package

\[
T_{sep}=K+A+P+I.
\]

### Factorized opening

\[
T_{fact}=K+O_\times.
\]

其中：

\[
O_\times\equiv A\land P\land I\land C.
\]

则：

\[
\boxed{T_{fact}\approx T_{sep}}
\]

在 explanatory content 上没有明显 gain。

### Genuine unified opening

\[
T_{open}=K+O,
\qquad
O\neq O_\times.
\]

只有当 `O` 带来 independently motivated cross-domain coupling，才可能：

\[
\boxed{
Compression(T_{open})>Compression(T_{sep}).
}
\]

---

## 14. Current verdict

UIWO 仍是 NOM 最值得保留的 positive refinement，但其 claim 需要明显收窄。

旧强 claim：

\[
A+P+I+Coincidence
\quad vs\quad
O.
\]

现改为：

\[
\boxed{
A+P+I
\quad vs\quad
O.
}
\]

而且：

\[
\boxed{
O\text{ only wins if independently non-factorizable}.}
\]

因此：

\[
\boxed{
\text{UIWO has a live unification opportunity, not yet a demonstrated compression win}.}
\]

最值得继续找的已经非常具体：

\[
\boxed{
\text{a real cross-domain law tying world actuality, NOW, and absolute-I together}.
}
\]

找不到它，`Opening(w,t,s)` 很可能只是 elegant notation。

找到它，NOM 才第一次拥有 neutral-rival-recognizable explanatory content。

## 关联

- [`../arguments/opening-factorization-test.md`](../arguments/opening-factorization-test.md)
- [`../../literature/deasy-conitzer-privilege-unification.md`](../../literature/deasy-conitzer-privilege-unification.md)
- [`../../literature/nagai-2007-2010-opening-actuality.md`](../../literature/nagai-2007-2010-opening-actuality.md)
- [`nomological-opening-model.md`](nomological-opening-model.md)
- [`spontaneous-absolute-orientation-breaking.md`](spontaneous-absolute-orientation-breaking.md)
- [`../arguments/primitive-actuality-replacement-test.md`](../arguments/primitive-actuality-replacement-test.md)
