# Centered Total State Hypothesis

> 状态：工作模型。
>
> 核心灵感：Soames 的 actuality-as-instantiation + centered-world / self-location framework + 本项目早期“完整现实可能已经内含 absolute center，而不存在只交换 center 的同一现实”直觉。

## 0. 动机

此前 Structural Selection 常写成：

\[
\mathcal R_0\Rightarrow E^*.
\]

这隐含一个 picture：先有一个完整的 uncentered reality \(\mathcal R_0\)，然后再由某个 selector / mechanism 从其中产生 absolute center。

但本项目很早就提出另一种可能：

> 也许所谓“完整现实”如果真的完整，就已经包含 center-related structure。不存在两个完整现实在所有事实都相同的情况下，仅仅把 absolute first-person 换掉。

Centered Total State Hypothesis 把这一直觉形式化。

---

## 1. Soames 的 actuality 模板

Soames 把 world-state 理解成 universe 可以具有的 consistent, maximally informative property。

actual world-state 的关键差异是：

\[
Inst(U,W^*),
\]

其中 \(U\) 是 concrete universe，\(W^*\) 是被实际 instantiated 的 maximally informative world-state。

其他 metaphysically possible world-states：

\[
W_i
\]

是：

\[
\Diamond Inst(U,W_i)
\]

但没有实际被 instantiated。

所以 actuality 可以被理解成：

\[
\boxed{
Actual(W)\iff Inst(U,W)
}
\]

而不必须先想象一个外部 pointer 指向某个 world。

---

## 2. 从 uncentered state 升级到 centered total state

普通 centered-world framework 可以把一个 self-location 写成：

\[
\langle W,t,i\rangle.
\]

本项目进一步考虑一族 **maximally centered total states**：

\[
\mathcal C_i
=
\langle
W,\Pi,\rho,i,t,\ldots
\rangle.
\]

这里：

- \(W\)：完整 third-person / objective structure；
- \(\Pi\)：全部 ordinary first-person perspectives；
- \(\rho\)：perspective 到 objective conscious events 的 anchoring；
- \(i,t\)：该 total state 的 simpliciter center；
- `...`：其他使状态真正 metaphysically complete 的结构。

关键：不同 center 对应不同 complete centered states：

\[
\mathcal C_i\neq\mathcal C_j
\quad(i\neq j).
\]

即使它们共享同一个 uncentered projection：

\[
Uncenter(\mathcal C_i)=Uncenter(\mathcal C_j)=W.
\]

---

## 3. Absolute center as global instantiation

假设 concrete total reality \(U\) 实例化恰好一个 centered total state：

\[
Inst_G(U,\mathcal C^*).
\]

定义：

\[
AbsoluteCenter(E^*)
\]

当且仅当：

\[
Center(\mathcal C^*)=E^*.
\]

于是候选结构是：

\[
\boxed{
Inst_G(U,\mathcal C^*)
\Rightarrow
Center(\mathcal C^*)=E^*
}
\]

这里不需要另加：

\[
Pointer(U,E^*).
\]

center 已经是被实例化 complete state 的内部组成。

---

## 4. 为什么这符合“不能只交换 center”的直觉

此前可以想象：

\[
R_1=(W,Absolute=E_A)
\]

和：

\[
R_2=(W,Absolute=E_B)
\]

然后追问为什么 pointer 指向 A。

Centered Total State 改成：

\[
\mathcal C_A
\]

与：

\[
\mathcal C_B
\]

本身就是不同 total states。

因此：

\[
\boxed{
\text{center change}\Rightarrow\text{complete-state change}
}
\]

而非：

\[
\text{same complete reality + different external label}.
\]

这直接实现了项目早期的 anti-pointer intuition。

---

## 5. Ordinary first-persons remain real

\(\mathcal C^*\) 并不只有一个 conscious subject。

其中仍包含：

\[
\Pi=\{\pi_A,\pi_B,\pi_C,\ldots\}
\]

及：

\[
\rho(\pi_i)=E_i.
\]

所有 ordinary first-person structures 可以真实存在：

\[
\forall i\;LocalFP(\pi_i).
\]

但完整 total state 还有一个 simpliciter center component：

\[
Center(\mathcal C^*)=\pi^*.
\]

所以模型自然实现 Two-Tier First-Person Realism：

\[
\boxed{
\text{many local first-persons}
+
\text{one globally centered total state}
}
\]

其他 minds 不需要成为 zombie 或 illusion。

---

## 6. Cardinality can come from maximal-state incompatibility

若 \(\mathcal C_i\) 与 \(\mathcal C_j\) 是两个不同、maximally complete centered states，并且中心 component 互不兼容，那么同一个 concrete totality 不能在同一意义下同时完整实例化二者：

\[
\mathcal C_i\perp\mathcal C_j.
\]

于是：

\[
Inst_G(U,\mathcal C_i)
\land
Inst_G(U,\mathcal C_j)
\]

被 coherence / maximality 排除。

这给：

\[
\le1
\]

一种比 `LIVE property has exactly one bearer` 更自然的结构来源。

它与 `Coherence-Based Singleton` 相容。

---

## 7. 它怎样重新解释 Absolutization

此前需要一个 operator：

\[
\mathsf A:F_i^{rel}\mapsto F_i^{abs}.
\]

Centered Total State 给一个候选解释：

\[
F_i^{abs}
\]

并非由一个局部 fact 被“加工”为 absolute。

而是：

\[
F_i^{abs}
\]

属于被 reality instantiated 的 complete centered state \(\mathcal C^*\)。

形式：

\[
F_i^{abs}\in\mathcal C^*
\quad\land\quad
Inst_G(U,\mathcal C^*).
\]

于是 `absolutization` 可以改写为 **global obtaining / instantiation**：

\[
\boxed{
\mathsf A(F_i)
\iff
F_i\text{ is the centered component of the globally instantiated total state}
}
\]

这比一个单独 primitive `A` operator 多了一层成熟的 actuality analogue。

---

## 8. 最大优点：不需要 neutral base 先决定 center

模型拒绝一个长期隐藏前提：

\[
\text{complete reality must first be uncentered}.
\]

完整 metaphysical state 可以从一开始就是：

\[
\text{centered}.
\]

因此中心不一定需要从更贫化的第三人称 structure 里被 selector 推导出来。

这与 Stalnaker 式 enriched-world escape 有亲缘关系，但更强：center-related structure 被放进 total metaphysical state，而不只是 epistemic representation。

---

## 9. 第一大风险：Hidden Primitive Center

最大的批评非常直接。

若：

\[
\mathcal C_i=\langle W,i\rangle,
\]

那么 `i` 会不会只是 primitive absolute pointer 被塞进 complete state 的 tuple？

若回答是“是”，模型只完成 re-description：

\[
Pointer(i)
\]

变成：

\[
CenterComponent(\mathcal C)=i.
\]

没有解释增益。

所以成功版本必须说明 `center component` 为什么是一个 legitimate constituent of complete reality，而不是人为加入的 haecceitistic slot。

---

## 10. 第二大风险：Why This Complete State?

即使 actuality 来自：

\[
Inst_G(U,\mathcal C^*),
\]

仍可追问：

\[
\boxed{
\text{为什么 }U\text{ 实例化 }\mathcal C^*\text{ 而不是 }\mathcal C_j？
}
\]

Soames 对 actual world-state 的理论同样允许 actual state 本来可以不同。

因此该模型可能把原问题升级成一种 **centered contingency**：

\[
\Diamond Inst_G(U,\mathcal C_j).
\]

它消除了 separable pointer picture，却不一定提供 deeper sufficient reason。

这点必须诚实保留。

---

## 11. 第三大风险：Universe as bearer of a center

普通 world-state 是 universe 的 complete property。

但一个 centered total state 包含：

\[
I=this\ subject,
\quad
NOW=this\ event.
\]

为什么这些可以是 universe / reality-as-a-whole 的 property constituents？

若这意味着：

\[
U\text{ itself has a first-person perspective},
\]

则模型滑向 cosmic subject / superpsychism。

理想版本必须区分：

\[
\text{reality is globally centered at }E^*
\]

与：

\[
\text{reality itself is a conscious subject experiencing }E^*.
\]

当前还没有现成 theory 给出这个区别的完整 metaphysics。

---

## 12. 第四大风险：Dynamics / I–NOW

若中心随经验变化：

\[
\mathcal C^*_1
\to
\mathcal C^*_2
\to
\mathcal C^*_3,
\]

则：

\[
Center(\mathcal C^*_k)=E^*_k.
\]

需要解释 complete centered state 的 change / passage。

若所有 centered total states 静态存在，而只有一个“当前被实例化”，就需要一个 moving actuality relation；元时间问题可能返回。

若 reality 本身 genuinely changes which centered state it instantiates，需要 dynamic metaphysics compatible with relativity。

所以该模型主要先解决 **I + actuality architecture**，尚未解决 NOW dynamics。

---

## 13. 第五大风险：Relativity

center 的 time-component 不能简单等于 universal simultaneity slice。

更安全地写：

\[
Center(\mathcal C^*)=E^*=(C,p),
\]

其中 \(p\) 是局部 spacetime event。

若模型要求整个 reality 在某个 global now hypersurface 上共同更新，就承担额外 relativity pressure。

---

## 14. 与 Nested Dominance 的关系

两条路线可以有两种关系。

### Competition-generated centered state

Nested dominance 先给：

\[
d(D_{comp})=\pi^*.
\]

然后：

\[
Center(\mathcal C^*)=\pi^*.
\]

并由：

\[
Inst_G(U,\mathcal C^*)
\]

提供 actuality interpretation。

### Centered state fundamental

反过来，\(\mathcal C^*\) 本身是 complete metaphysical state，Nested Dominance 只负责解释其内部 ordinary/local perspective structure。

后一种更忠实于“完整现实本来就 centered”的思路，也更少依赖 selector；但 primitive-center pressure 更强。

---

## 15. 当前评价

Centered Total State 是目前最贴合以下直觉的模型：

\[
\boxed{
\text{absolute center may be inseparable from complete reality rather than selected after reality is fixed}
}
\]

它结合了：

- Soames：actuality via instantiation of a maximally informative world-state；
- centered worlds：person/time location belongs to a centered state；
- Two-Tier FP：多个 ordinary perspectives + 一个 simpliciter center；
- coherence：不同 complete absolute centers 可视为 incompatible total states。

它目前最大的优势不是“解释了为什么是我”，而是消除了一个可能错误的前提：**先存在一个完整、绝对中性的现实，再额外选择一个我。**

最大的未解问题也因此变得更诚实：

\[
\boxed{
\text{centeredness 是完整现实的可解释结构，还是一个 disguised primitive？}
}
\]

## 文献入口

- Scott Soames, “Actually” (2007)；
- David Lewis, “Attitudes De Dicto and De Se” (1979)；
- SEP, *Self-Locating Beliefs*；
- Robert Stalnaker, work on centered worlds / self-location；
- Peter Pagin, “Constructing the World and Locating Oneself” (2017)；
- Christian List, “The many-worlds theory of consciousness” (2023)；
- Kit Fine, “Tense and Reality” (2005).
