# Local-to-Global Singleton Obstruction

## 0. 目标

当前项目已经区分：

\[
\text{Liveness Generation Problem}
\neq
\text{Absolute Center Uniqueness Problem}.
\]

这一笔记继续收紧第二个问题。

大量候选理论都能在某个局部系统中产生“一个”体验、一个 workspace winner、一个 maximal complex、一个 self-model fixed point 或一个当前中心。问题在于：若现实里有多个彼此独立或弱耦合的局部域，局部唯一性会被复制。

因此需要把“局部 singleton”与“全局 singleton”严格分开。

---

## 1. Competition domains

设全部候选意识事件为：

\[
\mathcal E_C.
\]

一个选择/排他机制并不一定直接作用于整个 \(\mathcal E_C\)。它通常先把候选分成若干 competition domains：

\[
D_1,D_2,\dots,D_k\subseteq\mathcal E_C.
\]

对每个非空 \(D_i\)，局部机制 \(s_i\) 选出至多一个 winner：

\[
s_i(D_i)=E_i.
\]

若不同 domain 之间没有参与同一个选择过程，则全局结果自然是：

\[
S=\{E_i\mid D_i\neq\varnothing\}.
\]

于是只要至少两个 domain 各自产生 winner：

\[
|S|\ge 2.
\]

### 工作引理：Local-to-Global Singleton Obstruction

> 若一个 singleton 机制只在多个相互独立的 competition domains 内部分别工作，并且每个非空 domain 都能产生一个 winner，那么该机制本身不能推出全局唯一 winner。

这只是一个简单结构事实，但它统一了项目此前遇到的很多复制问题。

---

## 2. Non-Factorization Requirement

设现实可以相对于某个候选机制分解成两个独立部分：

\[
\mathcal R=\mathcal R_A\oplus\mathcal R_B.
\]

若该机制满足可分解性：

\[
M(\mathcal R_A\oplus\mathcal R_B)
=
M(\mathcal R_A)\cup M(\mathcal R_B),
\]

且两边各产生一个中心，那么：

\[
|M(\mathcal R)|\ge2.
\]

所以任何要生成唯一 absolute center 的机制，都必须在相关意义上**不可因子化**：

\[
\boxed{
M(\mathcal R_A\oplus\mathcal R_B)
\neq
M(\mathcal R_A)\cup M(\mathcal R_B)
}
\]

至少对于那些分别含有真实意识的分解如此。

暂称 **Non-Factorization Requirement**。

这比此前的“不复制原则”更精确：真正的问题不是理论里出现了多个局部结构，而是 absolute-center-generating law 本身不能逐域复制运行。

---

## 3. Global Coupling Requirement

Non-Factorization 进一步要求：所有具有 absolute-center 资格的候选，必须进入某个共同的全局比较、竞争、依赖或生成结构。

设该结构诱导关系：

\[
R_G\subseteq\mathcal E_C\times\mathcal E_C.
\]

最低要求是，对于任意两个真正有资格竞争 absolute status 的候选 \(E_i,E_j\)，结构中必须存在足以影响最终选择的 cross-domain relation。

粗略写成：

\[
\forall E_i,E_j\in\mathcal E_C^{eligible},
\quad
E_i\mathrel{R_G}E_j
\;\text{or they participate in one common global constraint}.
\]

暂称 **Global Coupling Requirement**。

它不要求 \(R_G\) 必须是普通全序；可以是：

- grounding / relative fundamentality；
- 一个全局极值问题；
- 全局自同构不变量；
- 一个非局部约束；
- 一个协变定义的 distinguished role；
- 其他真正跨 domain 的结构。

---

## 4. IIT：最清楚的局部排他先例

IIT 的 exclusion postulate 很接近 singleton mechanism。

在 IIT 4.0 中，多个重叠 candidate substrates 可以有正 integrated information；exclusion 选择其中的 maximal substrate / complex，并排除与之重叠、较低的候选。

但在 universal substrate 上，IIT 会递归寻找第一个 complex、第二个 complex，依此类推。互不重叠的 complexes 可以同时存在。

因此 IIT 给出的结构是：

\[
\text{one winner per overlapping competition domain},
\]

并非：

\[
\text{one conscious winner in total reality}.
\]

这正好实例化 Local-to-Global Singleton Obstruction。

若把 IIT 擅自改成“全宇宙只保留全局最大 \(\Phi\) 的一个 complex”，那已经不再是标准 IIT，而且会直接威胁其他真实主体的意识地位。

---

## 5. GNWT：winner-take-all 仍是 system-local

Global Neuronal Workspace Theory 可以在一个脑系统内部通过 winner-take-all competition 产生一个当前占据 workspace 的 dominant content。

但两个不同主体拥有两个不同 workspace：

\[
W_A\to E_A,
\qquad
W_B\to E_B.
\]

没有跨主体的统一 workspace competition，就只能得到：

\[
\{E_A,E_B\}.
\]

所以“winner-take-all”这个形式本身完全不等于 global singleton。

---

## 6. Fixed point / self-reference：唯一性也会逐系统复制

设一个自指系统 \(X_i\) 上有 contraction：

\[
T_i:X_i\to X_i.
\]

Banach fixed-point theorem 可以保证：

\[
\exists !x_i^*\quad T_i(x_i^*)=x_i^*.
\]

但若存在两个独立系统：

\[
T_A:X_A\to X_A,
\qquad
T_B:X_B\to X_B,
\]

则完全可以同时有：

\[
x_A^*,x_B^*.
\]

所以“每个 reflexive system 有唯一 fixed point”解释的是局部 self-unity / stabilization；它没有推出“全部现实只有一个 fixed point center”。

若要让 fixed point 真正服务于 absolute first-person，operator 必须是**全局 operator**，并且它的固定点还要通过 Privilege Bridge Requirement。

---

## 7. Self-manifestation：自显现天然容易复制

现象学中的 self-manifestation / auto-affection 路线可以把经验的第一人称性理解成经验自身显现给自身。

但若每个真实经验都具有这种性质：

\[
\forall E_i\in\mathcal E_C,
\quad
SelfManifest(E_i),
\]

则它非常自然地解释普通 first-personality，同时自动产生多个 self-manifesting centers。

Michel Henry 的 Absolute Life 路线甚至提供一个更强先例：一个更深的 Life 可以通过多个 individual living beings 自我显现。

因此：

\[
\text{one deeper source of manifestation}
\not\Rightarrow
\text{one manifestation locus}.
\]

这和 Process-to-Center Gap 同构。

---

## 8. 与 Process-to-Center Gap 的统一

此前已经得到：

\[
\exists !G
\not\Rightarrow
\exists !E^*.
\]

现在可以看出它属于更一般的模式。

无论局部机制是：

- becoming；
- exclusion；
- workspace competition；
- fixed point；
- self-manifestation；
- one-center-per-world / light cone / subject；

只要最终可以在多个独立 domain 中重复应用，就会重新得到多个中心。

因此 absolute-center mechanism 必须具有真正的**global non-factorizability**。

---

## 9. Global singleton 仍不足以得到 absolute privilege

即使找到一个全局机制：

\[
M(\mathcal R)=\{E^*\},
\]

仍然还有此前已经确认的第二道门槛：

\[
\text{global uniqueness}
\not\Rightarrow
\text{absolute privilege}.
\]

所以一个完整候选至少需要同时满足：

1. **Globality**：所有 eligible candidates 处于同一全局约束中；
2. **Singleton**：全局约束有唯一结果；
3. **Invariance**：结果不依赖 gauge / arbitrary labels；
4. **Privilege Bridge**：胜出角色本身具有独立的本体论意义；
5. **Non-circularity**：不能把 `absolute` 预先写进选择规则；
6. **Other-minds compatibility**：不能通过简单取消其他真实意识来制造 singleton。

---

## 10. 下一步

现在 absolute-center 问题可以进一步收紧为：

\[
\boxed{
\text{寻找一个 global, non-factorizable, invariant, privilege-bearing singleton mechanism}
}
\]

下一轮优先检查：

- 全局 fundamentality rank / unique experiential minimum；
- grounding structure 中的 unique experiential dominator / bottleneck；
- 全局 self-manifestation operator；
- 协变定义的 distinguished event / chain；
- 这些方案是否又偷偷变成 primitive spotlight。

## 文献入口

- IIT 4.0: Albantakis et al., *Integrated information theory (IIT) 4.0* (2023).
- IIT Wiki, *Exclusion* (2024).
- Baars et al., *Global Workspace Dynamics* (2013).
- Stanford Encyclopedia of Philosophy, *The Unity of Consciousness*.
- Stanford Encyclopedia of Philosophy, *Self-Reference*.
- Stanford Encyclopedia of Philosophy, *Michel Henry*.
