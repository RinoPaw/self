# History Actualization Partition

## 0. 性质

这是 [`history-actualization-exhaustion.md`](history-actualization-exhaustion.md) 的形式化补充。

目标不是证明所有可能形而上学都只能有六种，而是给出一个**条件性穷尽命题**：只要理论接受一组相当弱的表示前提，history actualization 必须落入当前六路线之一，或明确违反这些前提。

---

## 1. 分类域假设

设理论层级输入为 `D`，候选 complete histories 构成非空集合：

\[
\Omega_D\neq\varnothing.
\]

采用以下工作假设。

### A1 — Candidate-space assumption

理论允许区分：

\[
\text{candidate histories}
\]

与它们的 actualization status。

如果某理论认为这种区分本身完全没有意义，它不在本分类域内。

### A2 — Reality assumption

理论不主张“没有任何 reality / history 成立”。

因此若 global actuality set 存在：

\[
A_D\neq\varnothing.
\]

这排除纯粹的 actuality eliminativism 作为分类对象。

### A3 — Actuality-form assumption

理论关于 actuality 至少采取以下一种形式：

1. determinate global actuality；
2. standpoint-relative actuality；
3. metaphysically indeterminate actuality。

若理论采用一种不能归入这三类的非标准 actuality concept，则它构成对本 schema 的真实反例候选。

### A4 — Nomological-level convention

`D` 在当前分类中只包含该层允许作为 laws / structural constraints / fixed global conditions 的输入；不能把“实际结果就是 H*”偷偷塞进 `D`，否则所有理论都可被平凡改写成 strong determination。

这个 convention 对区分 `S / Z / C` 必不可少。

---

## 2. 条件性穷尽命题

### Proposition — Actualization Partition

给定 A1–A4，任一理论在当前层级必须落入以下六类之一：

\[
\boxed{S\;|\;Z\;|\;C\;|\;P\;|\;R\;|\;I}
\]

其中：

- `S` = Structural / Strong Determination；
- `Z` = Extra Seed / Primitive Actuality；
- `C` = Stochastic Actualization；
- `P` = Plural Actualization；
- `R` = Relational / Perspectival Actualization；
- `I` = Indeterminate Actualization。

---

## 3. Proof by cases

### Case 1 — Theory admits determinate global actuality

存在确定的：

\[
A_D\subseteq\Omega_D.
\]

由 A2：

\[
|A_D|\ge 1.
\]

#### Case 1a — Multiple globally actual histories

若：

\[
|A_D|>1,
\]

则定义上属于：

\[
P=\text{Plural Actualization}.
\]

#### Case 1b — Singleton globally actual history

若：

\[
A_D=\{H^*\},
\]

则继续分：

##### 1b-i — `D` itself entails `H*`

若：

\[
D\vdash H^*,
\]

属于：

\[
S=\text{Structural / Strong Determination}.
\]

##### 1b-ii — `D` does not entail `H*`

若：

\[
D\not\vdash H^*,
\]

actual token 需要额外 realization structure。

若 `D` 给出 non-trivial objective chance / stochastic transition law：

\[
D\Rightarrow\mathbb P(H),
\]

并且 actual history 是该 law 的 ontic realization，则属于：

\[
C=\text{Stochastic Actualization}.
\]

若没有这样的 stochastic actualization law，则 singleton token 的差异只能由当前层级中未被 `D` 推出的额外 actual state / seed / primitive actuality fact 承担：

\[
(D,Z^*)\Rightarrow H^*.
\]

属于：

\[
Z=\text{Extra Seed / Primitive Actuality}.
\]

因此 determinate global actuality 分支穷尽为：

\[
S|Z|C|P.
\]

---

### Case 2 — Theory rejects determinate global actuality

由 A3，剩下两类合法 actuality form。

#### Case 2a — Standpoint-relative

若 theory 用：

\[
Actual(H,S)
\]

而非 global unary：

\[
Actual(H),
\]

则属于：

\[
R=\text{Relational / Perspectival Actualization}.
\]

#### Case 2b — Metaphysically indeterminate

若 actuality status 本身在 reality 中未精确 determinate，则属于：

\[
I=\text{Indeterminate Actualization}.
\]

因此 non-global-determinate 分支穷尽为：

\[
R|I.
\]

合并即得：

\[
\boxed{S|Z|C|P|R|I}.
\]

QED relative to A1–A4.

---

## 4. 为什么 `C` 不简单等于 `Z`

从 complete mosaic 视角看，一次 stochastic realization 当然也留下额外 token facts。

所以：

\[
C
\]

和：

\[
Z
\]

不是绝对本体论互斥类别，而是**当前解释层级上的分类**。

区别是：

### `C`

理论包含：

\[
\text{objective chance law / stochastic transition structure}
\]

实际 token 被这种 law-governed process realization。

### `Z`

理论只有额外 actual state / primitive fact：

\[
Z^*,
\]

而没有一条 non-trivial stochastic actualization law 解释 token transition / outcome distribution。

因此这套 taxonomy 是 explanatory architecture taxonomy，不声称把 world-mosaic 的所有 facts 切成互斥 natural kinds。

---

## 5. Hybrid theories

混合理论不构成反例。

例如：

\[
Z_0+ C_{dynamics}
\]

可以表示：

- 初始实际 configuration 属于 `Z`；
- 后续演化包含 stochastic jumps，属于 `C`。

分类应逐层应用：

\[
\text{initial actualizer}\to\text{transition actualizer}\to\text{first-person center}.
\]

同样：

\[
S_{universe}+P_{branches}
\]

完全可能成立。

Everettian Wentaculus 正是关键例子：fundamental universal history 可以 strong-deterministic，而 emergent branch structure 仍 plural。

所以：

\[
\boxed{\text{one theory can occupy different routes at different ontological levels}}
\]

这解释了此前为什么“strong determinism”和“many worlds”看似冲突却能同时出现。

---

## 6. 对 absolute first-person 的直接后果

绝对第一人称问题至少涉及两个 actualization level：

### Level H — Universe / physical-history actualization

\[
\Omega_D\to H^*\quad\text{or alternatives}
\]

### Level F — First-person actualization

给定完整 physical/history ontology 后：

\[
\mathcal E_C(H)\to E^*
\]

或拒绝 singleton `E*`。

因此必须分别标记：

\[
Route_H\in\{S,Z,C,P,R,I\},
\]

和：

\[
Route_F\in\{S,Z,C,P,R,I\}.
\]

例如：

### Everettian Wentaculus

可以粗略写成：

\[
Route_H=S,
\qquad
Route_{branch}=P.
\]

### Bohmian-style ontology

可写成：

\[
Route_H=Z
\]

相对于只包含 wave-function / law package 的 `D`。

### GRWf

可写成：

\[
Route_H=C.
\]

### Standpoint pluralism

first-person actuality 更接近：

\[
Route_F=R.
\]

这给 `self` 一个以后必须遵守的 bookkeeping rule：

> **任何论证都必须注明自己正在解决哪个 actualization level；不得从 universe-level singleton 直接跳到 first-person singleton。**

---

## 7. 当前最值得攻击的组合

正方最强路线不一定是单个字母，而是跨层组合。

### Deterministic strong route

\[
Route_H=S,
\qquad
Route_F=S,
\]

并另加 Privilege Bridge。

### Stochastic center route

\[
Route_H=S\text{ or }C,
\qquad
Route_F=C.
\]

### Primitive center route

\[
Route_F=Z.
\]

### Pluralist challenge

\[
Route_F=P\text{ or }R.
\]

### Indeterminacy challenge

\[
Route_F=I.
\]

所以新的核心比较对象是：

\[
\boxed{Route_H\times Route_F}
\]

而不再是一条单线 selector。

---

## 8. 开放点

当前最重要的潜在反例方向：

1. 有理论拒绝 A1：根本没有 well-defined candidate-history space；
2. 有理论拒绝 A3：actuality 既非 global、perspectival，也非 indeterminate，而采用第四种 irreducible form；
3. process metaphysics 认为 complete history 只是 derivative abstraction，因此分类必须下沉到 event actualization；
4. fundamentality / grounding 理论可能给 actuality 一种 gradable / ordered structure，而非 set-membership。

这些都应作为寻找第七类的明确搜索目标。
