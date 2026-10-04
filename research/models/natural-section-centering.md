# Natural-Section Formulation of Absolute Centering

> 状态：工作模型。

## 0. 动机

此前的 Centered Total State 与 Structural Selection 看似是两种路线：

\[
R\Rightarrow E^*
\]

和：

\[
C^*=\langle R,E^*\rangle.
\]

但两者都可以放进一个更统一的数学框架。

设 \(\mathfrak R\) 是 uncentered realities 的类，\(\mathfrak C\) 是 centered completions 的类，并有 forgetful map：

\[
\pi:\mathfrak C\to\mathfrak R.
\]

对于给定 reality \(R\)，纤维

\[
\pi^{-1}(R)
\]

包含所有与同一 uncentered structure 相容、但 center 不同的 centered completions。

---

## 1. Centering as a section

一个 center-selection rule 可以写成 section：

\[
\sigma:\mathfrak R\to\mathfrak C
\]

满足：

\[
\pi\circ\sigma=id_{\mathfrak R}.
\]

即 \(\sigma(R)\) 在每个 uncentered reality 上选出一个 centered completion。

若：

\[
Center(\sigma(R))=E^*,
\]

则 absolute center 来自 section 的输出。

---

## 2. Naturalness requirement

任意 choice function 不够。

若 reality morphism / isomorphism：

\[
g:R\to R'
\]

诱导 centered lift：

\[
\hat g:\pi^{-1}(R)\to\pi^{-1}(R'),
\]

则结构性 selector 应满足自然性：

\[
\boxed{\sigma(R')=\hat g(\sigma(R))}.
\]

对 automorphism \(g:R\to R\)，这立即要求：

\[
\hat g(\sigma(R))=\sigma(R).
\]

所以 center 必须是 relevant automorphism action 的 fixed point。

这把此前的 Symmetry Obstruction 重新表达成 section-existence condition。

---

## 3. 三种 ontology

### A. Natural section exists

\[
\exists!\sigma_{nat}.
\]

则 absolute centering 可以由 uncentered reality 的独立结构恢复。

这等价于一种加强版 Structural Selection：

\[
R\Rightarrow\sigma_{nat}(R)\Rightarrow E^*.
\]

优点：避免 primitive pointer。

代价：必须真的找到 independently motivated natural section。

### B. Sections exist but none is natural/canonical

则 mathematically 可以选 center，但所有选择都依赖额外 convention / choice。

这与 gauge fixing 很相似：选择一个 representative 不等于发现一个新的 physical fact。

若 absolute center 被这样引入，则需要额外 ontology 说明为什么某个 section physically / metaphysically real。

### C. Centered reality is fundamental

拒绝 \(\mathfrak R\) 是 fundamental base。

完整现实直接是：

\[
C^*\in\mathfrak C.
\]

这对应 Centered Total State 的 primitive / constitutive-centered 版本。

此时不存在从 \(R\) 恢复 center 的 section problem，因为 uncentered \(R\) 只是 projection：

\[
R=\pi(C^*).
\]

代价：centeredness 本身必须被接受为 fundamental，除非还有更深结构解释 \(C^*\)。

---

## 4. 与 Transition Factorization Challenge 的关系

传统 transition 架构：

\[
R\to\mathcal C(R)\to E^*.
\]

Natural-section formulation 表明，这等价于试图构造：

\[
\sigma(R).
\]

Centered Total State 则可能主张 ontology 从一开始位于 \(\mathfrak C\)，不经过 \(\mathfrak R\) 的 fundamental stage。

因此真正分歧不是“有没有 centered tuple”，而是：

\[
\boxed{\text{centered structure 是否可以自然地从 uncentered structure 恢复？}}
\]

---

## 5. Natural section 仍不等于 LIVE

即使成功得到：

\[
\exists!\sigma_{nat},
\]

仍然只得到：

\[
\text{canonical centered completion}.
\]

还需：

\[
Center(\sigma_{nat}(R))=E^*
\Rightarrow
LIVE_{simpliciter}(E^*).
\]

因此：

\[
\boxed{\text{Natural Centering}\not\Rightarrow\text{Absolute Liveness}}
\]

Privilege Bridge 没有自动消失。

---

## 6. 当前价值

这个 formulation 的主要价值是统一此前多个问题：

- Symmetry Obstruction → natural section 必须 fixed under automorphisms；
- Centering Reduction Trilemma → section 可恢复 / context-relative / primitive；
- Centered Total State → fundamental point in total space \(\mathfrak C\)；
- Structural Selection → natural/canonical section；
- stochastic actualization → random section / random lift；
- standpoint pluralism → 不要求单值 global section，或者 fundamental ontology 本身是多 centered fibres。

下一步不是随便寻找一个 selector，而是寻找：

\[
\boxed{\text{具有独立 first-person meaning 的 natural section}}
\]

或者证明这种 section 在合理结构下不存在。
