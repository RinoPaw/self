# Center-in-Content / Center-in-Obtaining Gap

> 状态：前沿压力测试。
>
> 目标：区分“把 center 写进完整状态的内容”与“现实的 obtaining / actuality 本身具有第一人称方向”，避免 `Centered Total State` 仅凭 tuple 表示就被误认为已经获得 simpliciter centering。

## 0. 问题

当前 `Centered Total State` 常写成：

\[
\mathcal C_c=\langle W,\Pi,\rho,c,\ldots\rangle.
\]

这至少有两种不同的形而上读法。

### Center in content

`c` 是 complete state 的一个 constituent / parameter：

\[
Content(\mathcal C_c)\supset c.
\]

状态描述了“以 \(c\) 为中心的世界”。

### Center in obtaining

现实不是先实例化一个包含 `c` 参数的中性内容；相反，实际 obtaining 本身以 \(c\) 为第一人称方向：

\[
Obtaining_c(W).
\]

这里真正承担 absolute-first-person 工作的，不是 content 中出现了 `c`，而是 **obtaining mode itself is centered**。

本项目真正需要后者，或某个与后者等价的结构。

---

## 1. 为什么 tuple 中出现 center 还不够

普通 centered-world / self-location framework 已经允许：

\[
\langle W,c_1\rangle,
\quad
\langle W,c_2\rangle,
\quad\ldots
\]

它们可以分别编码不同 subject-relative truths。

但只要这些 centered states 都能作为普通对象存在，就仍然可以有：

\[
Real(\mathcal C_{c_1})
\land
Real(\mathcal C_{c_2})
\land\cdots
\]

而没有：

\[
\exists!c\;Center_{simpliciter}(c).
\]

因此：

\[
\boxed{
\text{center as represented constituent}
\not\Rightarrow
\text{center as simpliciter actuality}
}
\]

这比 `Hidden Primitive Center` 更具体：即使 `c` 不是 hidden，而是公开写进 ontology，仍需说明它为什么改变 **what obtains simpliciter**，而非只增加一个 relational / indexed content coordinate。

---

## 2. Perspectival realism 提供的关键区分

Calosi、Iaquinto、Loss 对 perspectival realism 的刻画提供一个非常有用的诊断。

他们把“purely perspectival facts”理解为：某事实只从某个 perspective 获得，但**相关 perspective 并不作为该事实的 constituent 出现**。

时间类比最清楚：

\[
\text{Socrates is sitting}
\]

若是真正 tensed fact，它可以只从 present perspective obtain；这与：

\[
\text{Socrates is sitting at }t
\]

把时间 \(t\) 明写为 constituent 不同。

对第一人称同理，可区分：

### Relationalized / constituent form

\[
Presented(E,c)
\]

或：

\[
\langle W,c\rangle.
\]

### Pure perspectival / obtaining form

\[
Present(E)
\]

但该 fact 的 obtaining 本身只从 perspective \(c\) 成立。

这个区分说明：

\[
\boxed{
\text{adding }c\text{ to fact-content can neutralize the very perspectivality we wanted to explain}
}
\]

因为原本的 “from-here” 被改写成了一个普通更高元关系中的参数。

---

## 3. Constituent Collapse

假设 absolute-first-person theory 的全部额外结构都可写成 ordinary relation：

\[
A(R,c).
\]

且完整现实可以同时量化所有候选：

\[
\{c\mid Candidate(R,c)\}.
\]

那么除非 `A` 已经带有 primitive absolute semantics，否则 `c` 只是 relation 的 argument。

此时有两种情况。

### A. `A` 对多个 local centers 成立

得到 ordinary first-person plurality：

\[
A(R,c_1),A(R,c_2),\ldots
\]

### B. `A` 只对一个 center 成立

则需要解释：

\[
Why\ A(R,c^*)?
\]

来源问题回到 structural selection / global relation / primitive asymmetry。

因此只把 center 变成 state constituent，并不会自动获得 OIP 所需的：

\[
\boxed{\text{actuality itself is first-personally directed}}
\]

暂称这一失败模式 **Constituent Collapse**。

---

## 4. 对 `Inst_G(U,\mathcal C^*)` 的两种读法

当前 Double-Level Instantiation / Centered Total State 写：

\[
Inst_G(U,\mathcal C_c).
\]

现在必须区分：

### Reading I — content-centered instantiation

`Inst_G` 是普通 instantiation，特殊性全部位于属性内容：

\[
\mathcal C_c=\langle W,c\rangle.
\]

那么：

\[
Inst_G(U,\langle W,c\rangle)
\]

仍然需要说明为何 universe instantiate 这一 `c`-property；center 的 absolute significance 没有从普通 instantiation 自动产生。

这一路仍受：

- Centering Reduction Trilemma；
- Instantiation–Actuality Gap；
- Why This Complete State?；
- Hidden Primitive Center

约束。

### Reading II — centered instantiation

真正强版本应更接近：

\[
Inst_G^{\langle I,NOW\rangle}(U,W),
\]

或：

\[
Open(U,W,c,t).
\]

其中 first-person direction 属于 **instantiation / obtaining relation itself**，不是被 instantiated content 的普通参数。

这更忠实于 Nagai / Opening Identity Principle：

\[
\boxed{
WorldActuality=AbsoluteI=AbsoluteNOW
}
\]

但代价也更清楚：现在需要解释的已经不是 “为什么 tuple 有 center slot”，而是：

\[
\boxed{
\text{为什么 actuality / obtaining 本身具有 irreducible first-person direction?}
}
\]

这正是 Actuality-to-Center Bridge。

---

## 5. Center-Erasure Test

可以给 centered actuality theory 一个简单压力测试。

定义 forgetful operation：

\[
U_c:\mathcal C_c\mapsto W.
\]

问：遗忘 center 后，是否仍得到一个 metaphysically complete actual reality？

### 若答案为是

\[
Actual(\mathcal C_c)
\Rightarrow
Actual(U_c(\mathcal C_c))
\]

且后者仍 complete，则 centeredness 不是 actuality 的 constitutive condition。

center 至多是：

- additional first-person structure；
- self-location parameter；
- privilege property；
- extra pointer。

### 若答案为否

则 theory 真正主张：

\[
\boxed{
\neg\exists R_0\;[Actual(R_0)\land Complete(R_0)\land Uncentered(R_0)]
}
\]

这才是强 `Centered Actuality`。

但此时理论必须提供一个**不预设 absolute center 的 completeness / actuality criterion**，说明为什么 `U_c(\mathcal C_c)` 丢失的是现实本身，而不只是丢失一种描述方式。

因此 Center-Erasure Test 把问题压到：

\[
\boxed{
\text{centeredness 是否属于 obtaining 的必要形式，而不只是 complete content 的附加维度？}
}
\]

---

## 6. 与 fragmentalism 的三岔

若存在多个 incompatible first-personal facts，Calosi–Iaquinto–Loss 的框架提示三种总体方向。

### 1. Relationalize

把 perspective 写进 fact：

\[
F(c_i).
\]

优点：所有 facts 可在一个 coherent reality 中共存。

代价：perspectival incompatibility 被参数化，得到 ordinary plurality；absolute privilege 仍需额外来源。

### 2. Keep facts purely perspectival + neutrality

多个 incompatible perspectival facts 都真实，但不 privileged。

为了避免共同 obtaining 的矛盾，需要 fragment / standpoint structure。

这自然导向：

\[
\text{perspectival / fragmentalist pluralism}.
\]

### 3. Keep facts purely perspectival + coherent unitism

若坚持一个 coherent unitary actual reality，又坚持 incompatible first-person facts 不能共同 simpliciter obtain，那么至多一个能够 simpliciter obtain。

这可以帮助 `≤1`，但 `≥1` 与 which-one 仍需 centered actuality / opening 原理。

于是得到：

\[
\boxed{
\text{coherence can constrain multiplicity, but cannot by itself generate centered obtaining}
}
\]

这和现有 `Exclusivity–Existence Split` 完全一致。

---

## 7. 新的最小要求：Obtaining-Level Centering

`Centered Total State` 若要成为比 primitive pointer 更强的正方，至少需要满足：

### O1. Non-relationalizability

absolute first-person fact 不能被完整消去为：

\[
F(R,c)
\]

并让所有 `c` 在同一 uncentered totality 中平权共存。

### O2. Center-erasure destroys completeness or actuality

\[
U_c(\mathcal C_c)
\]

不能仍是同一意义下 complete actual reality。

### O3. Obtaining semantics is independently motivated

`centered obtaining` 不能只是：

\[
Actual_c(R):=\text{“}c\text{ is absolute”}.
\]

否则只是换名 primitive。

### O4. Ordinary perspectives remain local

其他主体仍可拥有：

\[
F_i^{rel}
\]

而无需把它们变成 illusion / zombie。

### O5. Coherence explains at-most-one, not at-least-one

不要再把 incompatibility / coherence 误用成 existence proof。

---

## 8. 对当前前沿的影响

这一分析不淘汰 `Centered Total State`，反而把它的最强版本辨认得更清楚。

弱版本：

\[
\boxed{\text{complete content contains a center parameter}}
\]

不足以推进项目。

强版本：

\[
\boxed{\text{complete actuality obtains in an irreducibly centered mode}}
\]

才真正对应当前核心问题：

> 现实的“现成如此”本身有没有第一人称方向？

因此下一步对 OIP / Nagai / actuality-as-instantiation 的研究应该优先问：

\[
\boxed{
\text{Is center a constituent of what obtains, or a constitutive mode of obtaining?}
}
\]

如果只是前者，理论很可能重新落回 self-location / relational plurality。

如果是后者，则真正需要解释的是一种 **first-personal mode of actuality**。

---

## 文献连接

- Claudio Calosi, Samuele Iaquinto & Roberto Loss, “Fragmentalism: Putting All the Pieces Together”, *Australasian Journal of Philosophy* 104(2), 2026, pp. 501–520; DOI `10.1080/00048402.2025.2515850`。当前使用层级：accepted/fulltext excerpt + publisher abstract。关键用途是区分 relevant perspective 作为 fact constituent 与 purely perspectival obtaining。
- Christian List, “The Many-Worlds Theory of Consciousness”, *Noûs* 57(2), 2023, pp. 316–340。用途：第一人称 centered world 作为 ontic `<ω,π>` 结构，以及多个 first-personally centred worlds 的 pluralist precedent。
- Kit Fine, *Tense and Reality* (2005)。用途：perspectival reality、fragmentalism 与 coherence/fragmentation 的基础框架。
- `centering-reduction-trilemma.md`
- `centered-completeness-gap.md`
- `instantiation-actuality-gap.md`
- `actuality-to-center-gap.md`
- `coherence-based-singleton.md`
- `synthesis/frontier-2026-10-05-centered-actuality.md`
