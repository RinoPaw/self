# Anchoring / Correlation Gap

> 状态：工作问题。目标是区分“有哪些第一人称 perspectives”与“这些 perspectives 分别锚定到现实中的什么位置”。

## 1. 两类事实还不够

设：

\[
W=\text{全部 objective / third-person facts},
\]

\[
\Pi=\{\pi_1,\pi_2,\dots\}=\text{全部 first-person perspectives}.
\]

仅仅把两类事实并列起来：

\[
(W,\Pi)
\]

仍未显式给出：

\[
\pi_i\text{ 对应世界中的哪个主体 / 事件}.
\]

Peter Pagin 2017 的核心压力正是：experience facts 与 objective facts 即使全部给出，它们之间的 empirical correlation 仍可能欠定。

---

## 2. Anchoring relation

因此引入一个关系：

\[
\rho:\Pi\to\mathcal E(W),
\]

其中 \(\mathcal E(W)\) 是世界中的候选主体 / 意识事件集合。

\[
\rho(\pi_i)=E_i
\]

表示 perspective \(\pi_i\) 锚定到客观世界中的经验事件 \(E_i\)。

于是一个更丰富的 reality representation 至少是：

\[
\mathcal R_{anch}=\langle W,\Pi,\rho\rangle.
\]

---

## 3. 普通第一人称只需要 anchoring

普通第一人称可以原则上表示为：

\[
FP(\pi_i,E_i)\iff \rho(\pi_i)=E_i.
\]

这样可以同时有：

\[
\rho(\pi_A)=E_A,
\quad
\rho(\pi_B)=E_B,
\quad
\rho(\pi_C)=E_C.
\]

多个真实 perspectives 与多个真实主体并不冲突。

---

## 4. Anchoring 不等于 privilege

即使 \(\rho\) 完全确定，仍然只得到：

\[
\{(\pi_i,E_i)\}_{i\in I}.
\]

它没有自动得到：

\[
\exists !(\pi^*,E^*)\;Absolute(\pi^*,E^*).
\]

因此：

\[
\boxed{\text{anchoring}\not\Rightarrow\text{absolute privilege}}
\]

这叫 **Anchoring–Privilege Separation**。

它是此前 `individualization != privilege` 在 first-person / world-correlation 层面的版本。

---

## 5. 绝对层还需要一个 relation

若保留 absolute first-person 假说，需要在 anchored pairs 上出现进一步结构。

可以抽象成：

\[
\alpha\subseteq \{(\pi_i,E_i)\}
\]

并要求：

\[
|\alpha|=1.
\]

但若 \(\alpha\) 只是一个 primitive pointer，则解释停止。

Nested Dominance 的目标可以重写成：让 \(\alpha\) 由 domain hierarchy 与 dominance relation 导出：

\[
\alpha
=
\{(\pi^*,\rho(\pi^*))\},
\]

其中：

\[
\pi^*=d(D_{\top}).
\]

这样 top dominance 负责 absolute selection，\(\rho\) 只负责把 winner 锚到世界中的具体事件。

---

## 6. Correlation Gap 对 Structural Selection 的修正

此前写：

\[
\mathcal R\Rightarrow E^*.
\]

现在需要问 `R` 是否已经包含 anchoring relation。

### 若没有 \(\rho\)

则从客观世界与 perspective inventory 到具体 location 的对应仍可能欠定。

### 若包含 \(\rho\)

则必须解释：

1. \(\rho\) 是 fundamental、grounded 还是 emergent；
2. \(\rho\) 是否由 physical / phenomenal facts 唯一决定；
3. 若存在 perfect duplicates，\(\rho\) 是否仍唯一；
4. \(\rho\) 是否 merely stipulative；
5. \(\rho\) 与 absolute selector \(\alpha\) 是不是两种不同关系。

因此以后“完整现实”更精确地至少写成：

\[
\boxed{
\mathcal R^+
=
\langle W,\Pi,\rho,\ldots\rangle
}
\]

而不能默认 `all facts` 已经自动解决 first/third-person mapping。

---

## 7. Stalnaker 与 Pagin 的分歧对本项目的意义

Stalnaker 的 Propositionality 路线提供一种可能：self-location uncertainty 最终总能理解成对 uncentered world 本身的 uncertainty；换言之，把 world 描述得足够丰富，center 差异可能成为 world difference。

Pagin 则提出更强反对：total experience record 与 total objective record 仍可能无法固定两者的 correlation。

本项目目前不预判谁最终正确。

它们形成一个很干净的分叉：

### Enrichment Thesis

\[
W^+\Rightarrow\rho.
\]

足够丰富的 complete reality 可以导出 anchoring。

### Correlation Primitive / Extra-Structure Thesis

\[
(W,\Pi)\not\Rightarrow\rho.
\]

还需要一种额外的 cross-level relation。

这正好对应本项目原先的问题：完整现实是否已经内含绝对第一人称，还是仍需要 further fact。

---

## 8. 新的成功条件

一个非循环 absolute-center model 现在至少要说明：

1. perspective inventory \(\Pi\) 从哪里来；
2. objective structure \(W\) 从哪里来；
3. anchoring \(\rho\) 怎样得到；
4. absolute selection \(\alpha\) 怎样得到；
5. \(\alpha\) 为什么具有 privilege / liveness，而不仅是 selection；
6. \(\rho\) 与 \(\alpha\) 都不能靠 primitive thisness 偷渡，除非理论明确接受 primitive 路线。

## 文献入口

- Peter Pagin, “Constructing the World and Locating Oneself”, *Review of Philosophy and Psychology* 8 (2017): 827–852；
- Robert Stalnaker, *Our Knowledge of the Internal World* (2008)；
- Robert Stalnaker, “Modeling a Perspective on the World” (2019)；
- David Lewis, “Attitudes De Dicto and De Se” (1979)；
- Christian List, “The many-worlds theory of consciousness” (2023).
