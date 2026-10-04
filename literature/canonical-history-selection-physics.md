# 物理中的 canonical history / worldline / event 选择先例

本笔记寻找和 `self` 当前结构最接近的成熟先例：

\[
\text{global / boundary structure}
\Rightarrow
\text{history / worldline / distinguished event}.
\]

这些理论都**不直接证明 absolute first-person**；用途是判断“从整体结构典范地选出历史、曲线或内部事件”是否在成熟物理中有真实先例。

## 阅读状态

当前为 **metadata-checked / abstract-read + targeted fulltext sections**。

- Choquet-Bruhat–Geroch / Sbierski：核对定理陈述与现代证明摘要；
- Beiglböck / Dixon / Tulczyjew-Dixon：核对 existence/uniqueness 摘要和现代综述；
- Barbour–Koslowski–Mercati：核对 PRL 摘要及 Janus point 后续讨论；
- Chen / Wentaculus：核对作者公开全文的 IPH、Bohm、Everett、GRW 小节；
- Tumulka / GRWf：核对 point-process 论文摘要及 flash ontology 结构。

---

## 1. Cauchy data → unique maximal spacetime history

### Choquet-Bruhat–Geroch theorem

广义相对论的 Cauchy 问题提供一个非常强的先例。

给定满足 Einstein constraint equations 的初始数据：

\[
I=(\Sigma,h,K),
\]

可以得到一个 maximal globally hyperbolic development：

\[
\operatorname{MGHD}(I).
\]

并且该 development 在保持初始数据的意义下 **unique up to isometry**。

粗略写成：

\[
I+\mathrm{EFE}
\Longrightarrow
[H_I]_{\cong}.
\]

这里输出不是某个坐标表示，而是一个等距同构类，所以 canonicality 已经把 gauge freedom 排除在外。

### 对 self 的意义

这证明：

\[
\boxed{\text{constraint-satisfying global data + laws can determine a unique maximal history modulo gauge}}
\]

并非空洞设想。

但它没有选出内部 center：

\[
H_I\not\Rightarrow E^*.
\]

同一个唯一 spacetime history 中仍然可以包含大量主体、worldlines 和事件。

因此它只完成：

\[
\text{global data}\Rightarrow\text{global history}.
\]

参考：

- Y. Choquet-Bruhat & R. Geroch, “Global Aspects of the Cauchy Problem in General Relativity” (1969).
- Jan Sbierski, “On the Existence of a Maximal Cauchy Development for the Einstein Equations: a Dezornification” (2015/2016), DOI `10.1007/s00023-015-0401-5`.

---

## 2. Distributed body structure → unique center-of-mass worldline

### Dixon / Beiglböck / Tulczyjew-Dixon

在 relativistic extended-body mechanics 中，一个物体不是先天附带唯一代表 worldline。不同 centroid 条件可以给出不同代表线。

Tulczyjew-Dixon spin supplementary condition：

\[
S^{\mu\nu}P_\nu=0
\]

在相应假设下可以选出唯一 center-of-mass worldline。

Beiglböck 1967 明确证明 center-of-mass line / center-of-motion line 的存在与唯一性（在一定弱场等条件下）。现代 MPD 文献仍把 TD condition 作为能给出唯一 center-of-mass worldline 的重要条件。

可以抽象成：

\[
\mathcal B=\{T^{\mu\nu},P^\mu,S^{\mu\nu},\ldots\}
\]

\[
K_{TD}(\mathcal B)=\Gamma_{CM}.
\]

### 对 self 的意义

这是目前找到的最直接：

\[
\boxed{\text{distributed physical structure}\Rightarrow\text{unique distinguished worldline}}
\]

先例。

它说明 `\Gamma^*` 这种对象在形式上完全可以由整体结构通过 intrinsic condition 选出，而无需给每个时刻手工标号。

### 但限制很关键

1. 先要给定“哪个 body”的 worldtube；它没有从整个宇宙中选出唯一 body。
2. TD condition 本身需要独立物理理由；不能只因为它给唯一结果就算解释。
3. 一条唯一 worldline 仍不等于该 worldline 是 metaphysically privileged。
4. worldline 上仍有无穷多个事件：

\[
\Gamma_{CM}\not\Rightarrow E^*.
\]

参考：

- W. Beiglböck, “The Center-of-Mass in Einstein’s Theory of Gravitation”, *Communications in Mathematical Physics* 5 (1967), 106–130, DOI `10.1007/BF01646841`.
- Dixon / Mathisson-Papapetrou-Dixon literature on center-of-mass worldlines and spin supplementary conditions.

---

## 3. Complete dynamical solution → unique internal event: Janus point

Barbour, Koslowski & Mercati 的 Newtonian N-body toy universe 给出一个更接近：

\[
\Gamma\Rightarrow E_J.
\]

在他们研究的零总角动量、相关能量条件下，典型解存在一个**唯一** Janus point。用 dilatational momentum `D` 或 moment of inertia 的极值表示：

\[
D(E_J)=0,
\]

并且这个点把一条完整解分成两个相反方向展开的 halves。

PRL 2014 的核心结论之一正是：typical solutions divide at a uniquely defined point into two halves。

### 这提供了什么

它证明一个完整 history 可以凭借自身 global/dynamical structure 选出一个 distinguished internal event：

\[
\boxed{\text{history-internal invariant/extremal structure}\Rightarrow\text{unique event}}
\]

而无需把那个点作为外部初始标签写进去。

### 对 self 的启示

这和我们原来的：

\[
E^*=\operatorname*{arg\,ext}_E J(E)
\]

非常接近，但它有真实动力学内容：极值不是任意造出来的评分函数，而来自 N-body dynamics / shape-space structure。

### 限制

Janus point 给的是一个 global temporal divider，并没有从该时刻的许多局部事件中选出一个 conscious center。

所以：

\[
\Gamma\Rightarrow t_J
\]

仍可能有：

\[
|\mathcal E_C(t_J)|\gg1.
\]

参考：

- Julian Barbour, Tim Koslowski, Flavio Mercati, “Identification of a Gravitational Arrow of Time”, *Physical Review Letters* 113, 181101 (2014), DOI `10.1103/PhysRevLett.113.181101`.
- Barbour, Koslowski, Mercati, “Janus Points and Arrows of Time” (2016), arXiv:1604.03956.

---

## 4. Boundary + canonical state + dynamics：Wentaculus

Eddy Keming Chen 的 Wentaculus 是目前最接近 `self` 四层结构的完整实验台。

### 4.1 Past-Hypothesis subspace → unique initial quantum state

Initial Projection Hypothesis (IPH) 定义：

\[
W_{IPH}(t_0)=\frac{I_{PH}}{\dim\mathcal H_{PH}}.
\]

给定 Past-Hypothesis subspace `\mathcal H_{PH}`，这是一个 natural normalized projection，因此 initial density matrix 被**唯一且简单**地确定。

这是真正的：

\[
\boxed{\text{boundary/global constraint}+\text{canonical construction}\Rightarrow\text{unique state}}
\]

先例。

### 4.2 Everettian Wentaculus：unique fundamental history，但不产生唯一 branch

IPH + deterministic von Neumann dynamics 给出一个 nomologically unique universal density-matrix history；Chen 称该版本 strongly deterministic。

但 Everettian structure 内部仍产生 branching：

\[
W^*+U
\Rightarrow
H_{multi}=\{b_1,b_2,\ldots\}.
\]

所以：

\[
\boxed{\text{unique fundamental history}\not\Rightarrow\text{unique local experienced branch}}
\]

这和 Monism Selector Gap 几乎同构。

### 4.3 Bohmian Wentaculus：unique velocity field，但仍需 actual initial configuration

IPH 固定唯一 initial quantum state，也就固定唯一 Bohmian velocity field。

但粒子轨迹仍需要实际初始 configuration：

\[
Q(t_0).
\]

作者公开全文明确指出，Bohmian Wentaculus 剩下的 nomological contingency 来自 initial particle configuration。

因此：

\[
W^*\Rightarrow v_W,
\]

但：

\[
(W^*,Q_0)\Rightarrow\Gamma_Q.
\]

这给出了一个非常清楚的 **Seed Gap**：

\[
\boxed{\text{canonical law/state}\not\Rightarrow\text{actual trajectory without an actual seed}}
\]

### 4.4 GRW Wentaculus：stochastic dynamics 产生 actualization

GRW 版本把 IPH 接到 stochastic collapse dynamics。

于是：

\[
W^*\Rightarrow \mathbb P(H),
\]

其中不同 collapse histories 都是 nomologically possible。

这不是 deterministic canonical selector：

\[
W^*\not\Rightarrow H^*.
\]

但若采用 GRW flash ontology，collapse centers 对应真实 spacetime flashes；Tumulka 将其表示成 spacetime point process。一个具体世界实际实现一个 flash history。

于是得到另一种结构：

\[
\boxed{\text{law}+\text{objective chance}\Rightarrow\text{one realized event history}}
\]

而不要求 laws 预先典范地指出哪一个 history。

Tumulka 2009 研究的数学对象是 flashes 的 joint distribution / point process，并证明若干版本中该 distribution 的 existence/uniqueness；这和“实际 realization 唯一由定律决定”要严格区分。

参考：

- Eddy Keming Chen, “The Wentaculus: Density Matrix Realism Meets the Arrow of Time”, in *Physics and the Nature of Reality* (Springer, 2024), pp. 87–104, DOI `10.1007/978-3-031-45434-9_8`.
- Eddy Keming Chen, “Quantum Mechanics in a Time-Asymmetric Universe: On the Nature of the Initial Quantum State”, *BJPS* 72(4), 1155–1183.
- Roderich Tumulka, “The Point Processes of the GRW Theory of Wave Function Collapse”, *Reviews in Mathematical Physics* 21(2), DOI `10.1142/S0129055X09003608`.

---

## 5. 目前得到的 selection ladder

成熟物理已经分别展示：

\[
\text{initial/global data}
\Rightarrow
\text{unique global history modulo gauge}
\]

（GR Cauchy development）

\[
\text{distributed body structure}
\Rightarrow
\text{unique worldline}
\]

（Dixon / TD center of mass）

\[
\text{complete trajectory}
\Rightarrow
\text{unique internal point}
\]

（Janus point）

以及：

\[
\text{canonical boundary state}+\text{stochastic generative law}
\Rightarrow
\text{one realized local-event history}
\]

（GRWf-style actualization；非 deterministic selector）。

所以“从整体结构选出 history / worldline / event”本身已经有很多成熟先例。

真正没有现成答案的仍是：

\[
\boxed{\text{为什么被选中的 event 是 LIVE simpliciter？}}
\]

以及：

\[
\boxed{\text{如何在不偷放 center seed 的情况下，从宇宙级结构选出 conscious }E^*?}
\]

这两项仍然是 `self` 的原创困难。