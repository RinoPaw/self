# Instantiation–Actuality Gap

> 状态：由 Soames 的 world-state actuality 类比得到的工作分析。

## 1. 模态先例：Actuality as Instantiation

Scott Soames 把 world-states 理解成 attributed to the universe 的 complete / maximally informative properties。

其中：

- actual world-state：被 universe 实例化的 world-state；
- metaphysically possible world-state：可能被实例化的 world-state；
- 其他 epistemically possible states：可一致设想但不一定 metaphysically possible。

可以抽象为：

\[
Actual(w)
\iff
Inst(U,w),
\]

其中 \(U\) 是唯一 concrete universe / world-bearer。

这提供一种不同于 Bricker primitive actuality 的结构：actuality 可以由一个普通-looking metaphysical relation——instantiation——承担。

---

## 2. 为什么模态版本容易 singleton

如果 world-states 是彼此完整、最大、互不兼容的 total states，则一个具体 universe 在同一意义上不能同时处于两个 genuinely distinct complete states：

\[
w_a\neq w_b
\]

且两者在某事实 \(p\) 上相反时：

\[
Inst(U,w_a)\land Inst(U,w_b)
\]

不可能同时成立。

因此 actuality cardinality 可以来自：

\[
\boxed{
\text{one bearer}
+
\text{mutually exclusive maximal states}
}
\]

而不只是额外写：

\[
|Actual|=1.
\]

这是当前非常重要的先例。

---

## 3. 第一人称迁移立即失败的地方

设每个 ordinary first-person perspective 对应一个 experiential state：

\[
P_i.
\]

项目坚持多个 genuine minds：

\[
Inst(S_A,P_A),
\quad
Inst(S_B,P_B),
\quad
Inst(S_C,P_C).
\]

所以如果简单定义：

\[
LIVE(P)\iff Inst(P),
\]

立刻得到：

\[
LIVE(P_A)\land LIVE(P_B)\land LIVE(P_C).
\]

这只解释普通 first-person reality，不会得到绝对中心。

因此：

\[
\boxed{
\text{ordinary experiential instantiation}
\not\Rightarrow
\text{absolute liveness}
}
\]

暂称 **Instantiation–Actuality Gap**。

---

## 4. Double-Level Instantiation 候选

Soames 类比仍然留下一个有价值的模型空间。

区分：

### Local instantiation

\[
Inst_L(S_i,P_i)
\]

产生 ordinary consciousness / first-personhood。

### Global instantiation

存在一个唯一 global bearer \(U\)，以及一族 mutually exclusive centered actuality-states \(A_i\)：

\[
Inst_G(U,A_i).
\]

若恰有一个：

\[
Inst_G(U,A^*),
\]

并且 \(A^*\) 锚定到已有 local perspective \(\pi^*\)，则：

\[
E^*=\rho(\pi^*)
\]

可以同时满足：

\[
\forall i\;FP(E_i)
\]

以及：

\[
\exists!E^*\;GlobalActual(E^*).
\]

形式上：

\[
\boxed{
Inst_L\text{ gives ordinary first-persons};
\quad
Inst_G\text{ gives candidate absolute actuality}
}
\]

---

## 5. 这条路线为什么和 Nested Dominance 很契合

Anchored Nested Dominance 已经要求同一个 local perspective 拥有两层 role：

\[
d(D_k)=\pi^*
\]

以及：

\[
d(D_{comp})=\pi^*.
\]

Double-Level Instantiation 可以给这个结构一个新的 actuality interpretation：

- local dominance / instantiation：为什么 \(\pi_i\) 是 genuine ordinary perspective；
- global dominance / instantiation：为什么 \(\pi^*\) 还承担 universe-level actualized centered state。

候选链：

\[
D_{comp}
\xrightarrow{d}
\pi^*
\]

\[
\pi^*
\mapsto
A^*
\]

\[
Inst_G(U,A^*)
\Rightarrow
GlobalActual(\pi^*).
\]

如果成立，它比：

\[
TopRank(\pi^*)\Rightarrow LIVE(\pi^*)
\]

更像一个真正 actuality bridge，因为 `instantiation` 在模态理论里已经承担 actual / merely-possible 的区分。

---

## 6. 三个严重问题

### 6.1 Global Bearer Problem

什么是：

\[
U?
\]

若 \(U\) 是 cosmos，为什么 cosmos 能 instantiate 一个 centered experiential actuality-state？

若这意味着 cosmos 自己拥有该 perspective，就会产生 cosmic subject。

### 6.2 State Content Problem

什么是：

\[
A_i?
\]

若定义：

\[
A_i=\text{“}E_i\text{ is absolutely live”},
\]

模型完全循环。

必须独立定义一族 global centered states，并解释它们为什么 mutually exclusive。

### 6.3 Instantiation-Type Problem

为什么：

\[
Inst_G
\]

是一种真实的、独立于 absolute LIVE 的 instantiation relation，而不是为了制造唯一性额外发明的二阶标签？

这与当前 `top competition domain` 的问题同型。

---

## 7. No-New-Subject 要求

Global instantiation 不能意味着：

\[
U\text{ phenomenally experiences }P^*.
\]

否则会重新生成 cosmic / overlapping subject。

最安全版本必须是：

\[
\boxed{
Inst_G\text{ changes the actuality-status of an existing local perspective without adding a second subject}
}
\]

但当前没有现成理论说明这种 instantiation relation 是什么。

---

## 8. 与 @-facts 的连接

Chaoan He 2026 把 ordinary facts 与 actuality-modified `@-facts` 纳入 grounding 关系讨论，例如：

\[
[Billy\ killed\ Suzy]
\]

与：

\[
@[Billy\ killed\ Suzy].
\]

这说明在 contemporary grounding theory 中，ordinary fact 与 actuality-modified fact 可以被当成不同结构对象研究。

因此第一人称 analogue 可以至少在形式上区分：

\[
[Conscious(E_i)]
\]

与：

\[
@[Conscious(E_i)].
\]

但 He 的工作本身没有提供“为什么 @ 只落在一个 first-person event”或“@ 从哪里来”的答案。

项目只借用这种 **ordinary fact / actuality-qualified fact** 的分层方式。

---

## 9. 当前评价

Actuality-as-instantiation 是本轮找到的第一个真正值得加入 quadrilemma 之外的第五种机制原型：

\[
\boxed{
\text{actuality through instantiation rather than primitive property}
}
\]

它的重要性在于：

- privilege 与 uniqueness 可以由 bearer–state relation 联合产生；
- 不直接依赖可自由 recombine 的 intrinsic actuality property；
- 可以和 Anchored Nested Dominance 的 local/global 双层结构自然接合。

但迁移到 first-person 后，普通 minds 已经使多个 experiential states 被 instantiated，因此必须解释一种额外的 global instantiation level。

新的直接问题：

\[
\boxed{
\text{Can there be a non-conscious global bearer that instantiates exactly one centered actuality-state without that state already containing primitive absolute liveness?}
}
\]

## 文献入口

- Scott Soames, “Actually”, *Aristotelian Society Supplementary Volume* 81 (2007): 251–277；
- Scott Soames, later world-state discussions；
- Chaoan He, “Grounding, Internality, and Actuality”, *Philosophy and Phenomenological Research* 113(1), 2026；
- Robert Stalnaker, possible worlds as ways the world could be.
