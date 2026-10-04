# Invariance–Definability Gap

> 状态：方法论修正。

## 0. 修正此前 criterion

此前 Structural Selection 使用必要条件：

\[
E^*\in Fix(Aut(R)).
\]

即一个由结构决定的 absolute center 必须被现实的相关自同构固定。

这个条件正确地排除 exact symmetry，但它远远不够。

---

## 1. Rigidity makes invariance cheap

若实际完整结构：

\[
Aut(R)=\{id\},
\]

则任何 event 都满足：

\[
\forall g\in Aut(R),\quad g(E)=E.
\]

所以：

\[
\boxed{\text{automorphism invariance}\not\Rightarrow\text{canonical privilege}}
\]

在 rigid reality 中，invariance test 对所有候选都 vacuous。

---

## 2. Naturalness can also become vacuous

Natural-section formulation 要求：

\[
\sigma(R')=\hat g(\sigma(R))
\]

对 relevant morphisms \(g:R\to R'\) 成立。

但若 reality category 的 morphisms 太少，例如各 models rigid 且彼此没有 relevant maps，则许多完全不同的 sections 都可能 technically natural。

所以：

\[
\boxed{\text{naturality is only as strong as the morphism structure}}
\]

必须加入 **Functorial Richness Requirement**：reality category 的 maps 必须足够表达理论认为 relevant 的结构保持变换 / counterfactual variation。

---

## 3. Model-theoretic lesson

一般 model theory 中，“在这个结构里被 automorphisms 保持”不是 unrestricted definability 的完整判据。

Svenonius-style results把 definability 与 elementary extensions 中 preserving the base vocabulary 的 permutations / automorphisms 联系起来。

方法论意义：

> 若一个 alleged distinguished center 只在 actual model 的 symmetry group 下固定，却不能在理论允许的 richer models / extensions 中被同一结构语言稳定识别，则它可能只是 accidental rigidity，而非真正 structural definition。

因此项目应区分：

### Actual-model invariance

\[
E^*\in Fix(Aut(R_{actual})).
\]

很弱，只是必要检查。

### Actual-model definability

存在不使用 `Absolute` 的结构公式 / relation：

\[
\varphi_R(x)
\]

使 actual structure 中：

\[
\exists!x\;\varphi_R(x).
\]

比 invariance 强。

### Uniform / theory-level definability

设 \(T\) 是 relevant reality theory / structure class。

理想情况存在统一 \(\varphi(x)\)，使：

\[
T\models \exists!x\,[ConsciousEvent(x)\land\varphi(x)].
\]

这最接近“同一独立原则在所有 admissible realities 中都确定 center”。

---

## 4. Do we really require theory-level uniqueness?

未必。

Absolute-first-person hypothesis 也可以允许：某些 possible realities 没有 conscious center，或 center structure 随 contingent whole-world facts 变化。

所以不能把：

\[
T\models\exists!x\varphi(x)
\]

直接设成无条件必需。

更温和的 requirement：

\[
\boxed{\text{Uniform Definability Conditional on the relevant world structure}}
\]

即同一个 non-absolute vocabulary 中的 rule / formula 在各 model 中根据其完整结构输出相应 center，而不是每个 model 任意另选一个。

---

## 5. Consequence for Q

成功的：

\[
Q_R(E)
\]

不能只满足：

- invariant in actual universe；
- unique because actual universe is asymmetric。

它最好还能回答：

1. \(Q\) 用什么 independent vocabulary 定义；
2. 同一个 definition 如何作用于 counterfactual / isomorphic / extended structures；
3. 为什么结构变化时 center 按该 rule 一致变化；
4. 为什么 \(Q\) 不是 actual token 的 disguised name。

---

## 6. Updated hierarchy

当前 structural tests 应按强度分层：

\[
\text{symmetry invariance}
\]

\[
\Downarrow\quad\text{necessary only}
\]

\[
\text{natural / equivariant selection}
\]

\[
\Downarrow
\]

\[
\text{independent definability / universal characterization}
\]

\[
\Downarrow
\]

\[
\text{first-person relevance / Privilege Bridge}
\]

所以通过 automorphism test 只说明“没有立即被 symmetry 杀死”，不再被视为任何 substantive positive evidence。

## 文献入口

- Svenonius theorem on definability and preservation in elementary extensions.
- Logic Journal of the IGPL 23(6), 2015, combinatorial version of the Svenonius theorem.
- General model-theoretic literature on automorphisms and definability.
