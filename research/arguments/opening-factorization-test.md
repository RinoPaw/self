# Opening Factorization Test

> 状态：2026-10-05 UIWO / CC3 unification pressure test。
>
> 目标：检验 `Opening(w,t,s)` 是否真的统一 modal / temporal / first-person privilege，还是只是把三个已有 unary privilege predicates 打包成一个三元记号。

## 0. Target

UIWO 定义一个 centered opening relation：

\[
O(w,t,s),
\]

并令：

\[
Actual(w)\iff\exists t,s\,O(w,t,s),
\]

\[
Present(t)\iff\exists w,s\,O(w,t,s),
\]

\[
AbsoluteI(s)\iff\exists w,t\,O(w,t,s).
\]

最初的正方直觉是：one ternary Opening 比 three independent spotlights 有 unification / role-coincidence advantage。

本审计给一个重要修正：**unique projections 本身不足以产生这种 advantage。**

---

## 1. Product construction

设 separate theory 已经有三个 exactly-one predicates：

\[
\exists!w^*\,A(w^*),
\]

\[
\exists!t^*\,P(t^*),
\]

\[
\exists!s^*\,I(s^*).
\]

若 candidate triples 还需满足普通 compatibility relation：

\[
C(w,t,s),
\]

例如：

- \(t\) 是 \(w\) 中的 time / stage；
- \(s\) 在 \(w,t\) 中存在并 conscious；
- subject-location关系满足 ordinary ontology。

则可以定义：

\[
\boxed{
O_\times(w,t,s)
:=
A(w)\land P(t)\land I(s)\land C(w,t,s).
}
\]

只要 privileged members彼此 compatible，就自动得到：

\[
\exists!\langle w^*,t^*,s^*\rangle\,O_\times(w^*,t^*,s^*).
\]

所以：

\[
\boxed{
ThreeUniquePrivileges
\not\Rightarrow
NeedForExtraCoincidencePrimitive.
}
\]

原 UIWO 中把 `Coincidence(w*,t*,s*)` 当作 separate package必付第四 primitive 的说法过强。

---

## 2. Conitzer reinforces this correction

Conitzer 的 personalized A-theory明确指出：若 distinguished I 与 distinguished Now 同时成立，它们的 combination 会直接 imply 一个 distinguished Here / observational frame（在 ordinary spatial-location assumptions 下）。

这说明至少在 I–NOW case：

\[
\boxed{
I^*+NOW^*+ordinary\ location
\Rightarrow
centered\ coordinate
}
\]

而不需要再加一个独立 `I-NOW coincidence` primitive。

因此 Conitzer支持 **combined significance**，却不支持“组合本身需要第四 primitive”的强说法。

---

## 3. Projection–Factorization Result

定义：若一个 Opening relation 满足：

\[
O(w,t,s)
\equiv
A(w)\land P(t)\land I(s)\land C(w,t,s),
\]

其中 `C` 完全属于双方共享的 ordinary world/time/subject structure，则称 `O` **factorizable**。

于是：

\[
\boxed{
FactorizableOpening
\text{ has no explanatory advantage merely from arity compression}.}
\]

原因：

- `O` 的 truth conditions完全由旧 predicates决定；
- projections没有新增 modal content；
- one relation symbol vs three predicate symbols只是表示选择；
- exact-one triple由三个 exact-one margins自动给出。

这是 **Projection–Factorization Result (PFR)**。

---

## 4. Genuine unification requires non-factorization

Opening要获得真实 CC3 / compression credit，必须存在：

\[
\boxed{
O\neq O_\times.
}
\]

更具体地，至少要有一个 **Cross-Domain Coupling**。

### NF1 — Combination exclusion

存在：

\[
A(w_i),\ P(t_j),\ I(s_k)
\]

在 separate marginal laws看来各自允许，但：

\[
\neg Possible[O(w_i,t_j,s_k)].
\]

即 Opening law禁止某些 product combinations。

### NF2 — Joint counterfactual dependence

改变一个 privilege role会 lawfully约束另两个：

\[
do(O_w=w')
\Rightarrow
constraints\ on\ O_t,O_s.
\]

而不是三个 spotlight independent variation。

### NF3 — Non-product chance

若 privilege realization stochastic：

\[
\boxed{
P_O(w,t,s)
\neq
P_A(w)P_P(t)P_I(s)
}
\]

且 deviation由 principled joint law解释，而非 ad hoc correlation。

### NF4 — Common causal / grounding source

存在同一个 independently characterized process / ground \(G\)，使：

\[
G\Rightarrow Actual(w^*)+Present(t^*)+AbsoluteI(s^*)
\]

而三个 effects不能由三个 independent grounds equally well解释。

### NF5 — Shared explanatory residual

竞争 theory independently承认一个跨域 explanandum `X`，例如：

\[
X=\text{why actuality, presentness, and first-person liveness covary as one centered occurrence},
\]

且：

\[
Explain(O,X)\land\neg Explain(A+P+I,X).
\]

没有这种共同 residual，unification credit不能计算。

---

## 5. Analogy is not identity

Builes / Deasy / Conitzer 提供的是强 **structural analogy / argumentative pressure**：

\[
ActualWorld\sim PresentTime\sim FirstPersonPerspective.
\]

但 analogy 本身不推出 one ontology。

这点在 world–time literature 中已有明确警告：Ulrich Meyer 2006 认为 worlds/times虽然在 modal/tense model theory中有显著平行，但 analogy 有实质断点；特别地，他反对把 presentism简单当成 actualism 的 tense analogue。

Samuele Iaquinto 2026 仍把 time/modality analogy当成重要研究框架，但其综述本身也是对 parallel theories 的比较，不是 identity theorem。

所以记录：

\[
\boxed{
PrivilegeAnalogy
\not\Rightarrow
PrivilegeIdentity.
}
\]

Nagai 的 `Actuality=I=NOW=Opening` 因而仍是一项额外 metaphysical thesis，而非 Builes/Deasy/Conitzer 类比自动给出的结论。

---

## 6. Where Conitzer genuinely helps

Factorization correction不消灭 Conitzer 的价值。

Conitzer 的 strongest result更接近：

\[
\boxed{
Motivation(A\text{-}theory)
\Rightarrow
PressureToward(I\text{-}NOW),
}
\]

因为：

- presence-simpliciter argument同时指向 distinguished I 与 NOW；
- `Thank goodness` / self-bias cases 对 personalized A-theory更有力；
- some objections to global NOW (e.g. relativity pressure) 对 local I–NOW版本更弱。

这给 **joint motivation**，而非 logical non-factorization。

因此它可帮助建立 NF5（shared explanatory residual），但尚未直接建立 NF1–NF4。

---

## 7. Where Nagai genuinely helps

Nagai 是当前 strongest non-factorization template，因为他不说：

\[
Actual(w^*)\land NOW(t^*)\land I(s^*)
\]

三个 facts恰好同时成立。

他的更强主张是：

\[
\boxed{
WorldActualization
=
I\text{-}Actualization
=
NOW\text{-}Actualization
=
OneOpening.
}
\]

如果这个 identity有独立内容，则 UIWO不是 conjunction。

但当前问题正是：

\[
\boxed{
Why\ accept\ this\ identity\ rather\ than\ the\ factorizable\ package?
}
\]

Nagai主要诉诸 opening/actuality intuition与 sheer contingency；尚未给一个 neutral rival也必须接受的 non-factorization phenomenon。

---

## 8. Revised compression comparison

### Separate Spotlight Package

\[
T_{sep}=K+A+P+I.
\]

### Factorized Opening

\[
T_{fact}=K+O_\times.
\]

如果：

\[
O_\times\equiv A\land P\land I\land C,
\]

则：

\[
\boxed{
T_{fact}\approx T_{sep}
}
\]

在 explanatory content 上没有明显 gain。

### Non-factorizable Opening

\[
T_{open}=K+O,
\qquad O\neq O_\times.
\]

只有当 `O` 带来 independently motivated cross-domain constraints / joint law / common explanatory residual，才可能：

\[
\boxed{
Compression(T_{open})>Compression(T_{sep}).
}
\]

---

## 9. Revised UIWO burden

UIWO 以后必须通过三关：

### U1 — Common-slot gate

rival independently accepts至少两个 privilege dimensions；否则 Opening主要是新增内容。

### U2 — Non-factorization gate

证明 `O` 不能等价消去为：

\[
A\land P\land I\land C.
\]

### U3 — Independent-coupling gate

证明 non-factorization来自一个 independently motivated law / ground / explanandum，而非为了让 Opening看起来 unified 而 stipulate covariance。

只有三关都过，才有 genuine primitive-replacement / unification advantage。

---

## 10. Current verdict

此前 UIWO 的 strongest claim：

\[
A+P+I+Coincidence
\quad vs\quad
O
\]

需要收窄。

更公平的是：

\[
\boxed{
A+P+I
\quad vs\quad
O
}
\]

而且：

\[
\boxed{
O\text{ wins only if it is independently non-factorizable}.}
\]

因此最新结果：

\[
\boxed{
\text{UIWO has a live unification opportunity, but not yet a demonstrated compression win}.}
\]

真正的新 target 从“能否把三个 spotlight写成一个 relation”变成：

\[
\boxed{
\text{Is there a real cross-domain law tying world actuality, NOW, and absolute-I together?}
}
\]

如果找不到，`Opening(w,t,s)` 很可能只是 elegant notation。

如果找到，Opening 才第一次获得 neutral-rival-recognizable explanatory content。

## Literature / links

- Vincent Conitzer, “The Personalized A-Theory of Time and Perspective”, *Dialectica* 74(1), 2020, 3–31, DOI `10.48106/dial.v74.i1.02`.
- David Builes, “Eight Arguments for First-Person Realism”, *Philosophy Compass* 19(1), 2024, e12959, DOI `10.1111/phc3.12959`.
- Daniel Deasy, “The Contingent Spotlight Theory”, *Pacific Philosophical Quarterly* 106(3), 2025, 162–172, DOI `10.1111/papq.12485`.
- Ulrich Meyer, “Worlds and Times”, *Notre Dame Journal of Formal Logic* 47(1), 2006, 25–37, DOI `10.1305/ndjfl/1143468309`.
- Samuele Iaquinto, “Time and Modality”, in *The Routledge Companion to Philosophy of Time*, Routledge, 2026, 261–269.
- [`../models/unified-i-now-world-opening.md`](../models/unified-i-now-world-opening.md)
- [`primitive-actuality-replacement-test.md`](primitive-actuality-replacement-test.md)
- [`../../literature/deasy-conitzer-privilege-unification.md`](../../literature/deasy-conitzer-privilege-unification.md)
- [`../../literature/nagai-2007-2010-opening-actuality.md`](../../literature/nagai-2007-2010-opening-actuality.md)
