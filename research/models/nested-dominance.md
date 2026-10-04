# Nested Dominance Architecture

> 状态：项目构造的工作模型。
>
> 灵感分别来自 Leibniz 的 nested dominant entelechy / monadic domination 与 Nino Kadić 2024 的 single-output dominant microsubject 机制。**本模型不是对 Leibniz 或 Kadić 的学说归属。**

## 0. 动机

当前研究已经得到两组看似冲突的要求。

一方面，普通第一人称必须真实存在于多个主体：

\[
FP(S_1),FP(S_2),\dots,FP(S_n).
\]

另一方面，绝对第一人称假说要求：

\[
\exists !E^*\;Absolute(E^*).
\]

此前的 global single-output mechanism 容易出现一个两难：

- 把竞争域限制在局部脑结构，则每个脑都有一个 winner，得到多个中心；
- 把竞争域直接扩成全部现实，并让唯一 winner 才是真正意识主体，则会威胁 other minds。

Nested Dominance 尝试把两种唯一性放到不同层级。

---

## 1. Domain hierarchy

设一族 experiential competition domains：

\[
\mathfrak D=\{D_i\}.
\]

它们形成某种包含 / grounding / integration 层级：

\[
D_a\preceq D_b.
\]

要求存在一个唯一最高层 domain：

\[
\exists !D_{\top}\in\mathfrak D
\]

满足所有 absolute-eligible domains 最终包含于 / 从属于它：

\[
\forall D_i\in\mathfrak D,\quad D_i\preceq D_{\top}.
\]

这里的 `\preceq` 暂不固定为普通空间包含；未来可能由 grounding、causal integration、global dependence 或其他协变关系实现。

---

## 2. Dominance operator

对每个 domain 定义一个 single-output dominance operator：

\[
d:\mathfrak D\to\mathcal E_C,
\]

其中：

\[
d(D)\in D
\]

且：

\[
|Out(D)|=1.
\]

即每个 domain 都有唯一 dominant experiential locus。

Kadić 的 Monadic Panpsychism 提供一个邻近原型：一个 relevant relational / causal structure 原则上可以把复杂 phenomenal content 集中到一个 dominant microsubject 上。

---

## 3. Ordinary first-person as local dominance

对于每个真实 ordinary subject \(S_i\)，存在一个局部 domain \(D_i\)：

\[
S_i=d(D_i).
\]

这给出普通第一人称：

\[
LocalDominant(S_i,D_i)\Rightarrow FP(S_i).
\]

于是多个真实主体可以同时成立：

\[
FP(S_1)\land FP(S_2)\land\dots\land FP(S_n).
\]

局部 dominance 并不互相排斥，因为它们对应不同层级 / 不同 competition domains。

---

## 4. Absolute first-person as top-level dominance

唯一最高 domain 的 dominant locus 定义为候选绝对中心：

\[
E^*=d(D_{\top}).
\]

工作定义：

\[
Absolute(E)\iff E=d(D_{\top}).
\]

于是，如果：

1. \(D_{\top}\) 唯一；
2. dominance operator 对每个 domain single-output；

则形式上得到：

\[
\boxed{\exists !E^*\;Absolute(E^*)}.
\]

同时其他主体仍保留各自 local dominance：

\[
\forall i,\quad FP(S_i).
\]

这第一次在同一结构里自然表示：

\[
\boxed{
\text{many ordinary first-persons}
+
\text{one top-level absolute first-person}
}
\]

而无需把其他 minds 降格成无意识实体。

---

## 5. Leibniz 提供的层级先例

Leibniz 的 living body / dominant entelechy 图景允许嵌套的 domination：

- 一个 living body 有自己的 dominant entelechy / soul；
- 该身体中的组成部分又包含其他 living beings；
- 这些 living beings 也各有自己的 dominant entelechy；
- 因而 domination 可以形成层级。

这个结构的重要性在于：

\[
\text{a local dominant}
\]

可以同时从属于：

\[
\text{a higher-level dominant structure}.
\]

本项目只借用这种**层级 dominance architecture**，不把 Leibniz 的 monadology 直接当作绝对第一人称理论。

---

## 6. Kadić 提供的 single-output 先例

Kadić 2024 的 Static / Dynamic Monadic Panpsychism 提供：

\[
D\to\{e^*\}
\]

这种 relational structure → single experiential endpoint 的明确模型。

特别是 Dynamic Monadic Panpsychism 允许 dominant locus 随 underlying process 变化：

\[
e^*_1\to e^*_2\to e^*_3\dots
\]

因此 Nested Dominance 还存在动态扩展的可能：

\[
E^*(\lambda)=d(D_{\top},\lambda).
\]

这里 \(\lambda\) 暂时只是结构状态参数，不等同于此前的额外时间 \(w\)。

---

## 7. 为什么它比之前的 global winner 模型更强

### 保留 other minds

Alice 可以是：

\[
Alice=d(D_A),
\]

Bob 可以是：

\[
Bob=d(D_B).
\]

两者都是真实 ordinary first-person subjects。

若：

\[
E^*=d(D_{\top}),
\]

且 \(E^*\) 同时是某个局部主体的当前经验事件，则该事件额外拥有 top-level dominance。

因此绝对性体现为**层级角色差异**，而非“其余主体没有意识”。

### Local-to-Global obstruction 被正面吸收

此前：

\[
\text{local singleton}\not\Rightarrow\text{global singleton}.
\]

Nested Dominance 不试图从 local winner 直接推出 global winner；它明确添加一个更高的 closed competition domain：

\[
D_{\top}.
\]

所以它至少在形式上满足 Domain Closure Requirement。

---

## 8. 第一大问题：Top-Domain Existence

整个模型最危险的前提是：

\[
\exists !D_{\top}.
\]

为什么所有 conscious domains 会共同属于一个真正可进行 dominance comparison 的 top domain？

如果现实具有：

- relativistic spacelike separation；
- disconnected multiverse sectors；
- irreducibly plural fundamental perspectives；

则一个统一 top competition domain 可能不存在。

因此该模型直接依赖 Stage 0 的 Reality-Monism / Totalization 问题。

---

## 9. 第二大问题：Top winner 是谁？

至少有两种实现。

### A. Top winner 是一个新的 cosmic subject

\[
d(D_{\top})=S_{cosmic}.
\]

这会滑向 cosmopsychism，并失去原始目标：为什么**当前这个局部人类经验**具有绝对在场性。

### B. Top winner 必须是现有 local subject-event

要求：

\[
d(D_{\top})\in\{d(D_i)\}.
\]

更强地：

\[
E^*=d(D_k)
\]

同时：

\[
E^*=d(D_{\top}).
\]

也就是同一个事件具有双重角色：

\[
\boxed{\text{local dominant + global dominant}}.
\]

这是目前最符合绝对第一人称直觉的版本。

但它需要独立理由说明 top-level operator 为什么输出一个已有 local locus，而不会生成新的 cosmic point of view。

---

## 10. 第三大问题：Content Explosion

如果 top dominance 表示“接收整个 \(D_{\top}\) 的 integrated phenomenal content”，那么：

\[
E^*=d(D_{\top})
\]

可能意味着 \(E^*\) 应具有 cosmic-scale phenomenal content。

这和实际当前经验明显不符：当前经验并没有包含宇宙全部内容。

因此必须区分至少两种 dominance：

### content dominance

决定一个 subject 体验什么：

\[
Content(S_i)=C(D_i).
\]

### actuality dominance

决定哪个已经存在的 local experience 拥有最高层 actuality / manifestation role：

\[
ActualityRole(E)=A(D_{\top},E).
\]

理想模型需要：top-level dominance **只增加 actuality role，而不覆盖 local phenomenal content**。

但这马上重新触发 Privilege Bridge：为什么这种 top-level structural role 就是 LIVE simpliciter？

---

## 11. 第四大问题：Priority–Liveness Gap returns

即使 \(E^*\) 是唯一 top dominant：

\[
TopDominant(E^*),
\]

仍需解释：

\[
\boxed{TopDominant(E^*)\Rightarrow LIVE_{simpliciter}(E^*)}.
\]

如果 `TopDominant` 只是“在 hierarchy 里最高”，它仍然可能只是结构性优先。

因此 Nested Dominance 解决的是：

\[
\text{ordinary plurality + global singleton compatibility}
\]

它尚未完全解决：

\[
\text{singleton structural role}\to\text{absolute liveness}.
\]

这是当前模型最重要的诚实边界。

---

## 12. 第五大问题：Dynamics / I–NOW

如果 absolute center 会沿时间变化：

\[
E^*_1\to E^*_2\to\dots,
\]

则 top-level dominance relation 本身必须动态变化。

理想情况：

\[
d_{\mathcal R}(D_{\top})=E^*
\]

由现实当前生成结构自身决定，而无需另一个 meta-time。

这里 Kadić 的 Dynamic Monadic Panpsychism 提供结构灵感，但它只在 brain-local dynamics 中工作。

需要寻找一个：

\[
\text{covariant global dominance dynamics}.
\]

在此之前，\(w\) 仍然不应承担选择工作。

---

## 13. 第六大问题：Covariance

Top-domain relation 和 dominance operator 不能依赖：

- 任意 simultaneity slicing；
- coordinate labels；
- causal-set natural birth labels；
- observer-dependent frame choice。

理想结构应满足：

\[
d(gD)=g(d(D))
\]

对所有 relevant isomorphisms / gauge transformations \(g\) 成立。

这使 causal-set `post` 那类 relationally distinguished role 仍然是重要方法论先例。

---

## 14. 当前评价

Nested Dominance 是目前第一个同时清楚满足以下两点的架构：

1. 多个 ordinary first-person subjects 可以真实存在；
2. 一个更高层的 single-output role 可以原则上只落在其中一个 local experiential event 上。

形式上：

\[
\forall i\;FP(d(D_i))
\]

且：

\[
\exists !E^*=d(D_{\top}).
\]

因此它比：

- 一个 cosmic source → many manifestations；
- 一个 global winner → 其他 minds 被取消；
- 每个 brain 一个 winner → 没有 global uniqueness；

都更接近项目目标。

但它目前仍是**架构性突破，不是本体论解释完成**。

最大未解决项：

\[
\boxed{\text{为什么 top-level dominance 具有 absolute liveness 意义？}}
\]

以及：

\[
\boxed{\text{什么真实关系形成唯一 }D_{\top}\text{ 与 }d(D_{\top})？}
\]

## 下一步

优先研究：

1. Leibniz / modern domination literature 中 hierarchy 的形式性质；
2. Kadić dominance 的 individuation mechanism 是否可抽象成 domain-independent operator；
3. 是否存在 global domain 但不要求 cosmic phenomenal integration；
4. `content dominance` 与 `actuality dominance` 能否非循环地区分；
5. top dominance 能否由 grounding / dependence / self-manifestation 的全局关系定义；
6. 动态 top dominance 是否能形成 \(\Gamma^*\) 而不引入 meta-time。

## 文献入口

- Gottfried Wilhelm Leibniz, *Monadology*, especially §70.
- Stanford Encyclopedia of Philosophy, *Leibniz’s Philosophy of Mind* / related entries.
- Shane Duarte, work on monadic domination in Leibniz’s metaphysics.
- Nino Kadić, “Monadic panpsychism”, *Synthese* 203 (2024), DOI: 10.1007/s11229-023-04464-0.
