# Coherence-Based Singleton

> 状态：条件性论证。它最多建立 absolute first-person 的 **at-most-one** 部分；不会单独证明任何 absolute center 存在。

## 1. 起点

Christian List 的 quadrilemma 明确指出，不同 conscious subjects 的强 first-person facts 彼此不 compossible。

设 Alice 与 Bob 的 complete conscious states 分别是 \(X\) 与 \(Y\)。对应强 first-person facts：

\[
F_A=\text{I am in conscious state }X,
\]

\[
F_B=\text{I am in conscious state }Y.
\]

若 \(X\) 与 \(Y\) 是不同主体的完整 token subjective states，则：

\[
F_A\perp F_B,
\]

其中 \(\perp\) 表示二者不能从同一个 first-person perspective 共同成立。

---

## 2. Absolute facts 的定义层

本项目区分：

### Local / relative first-person facts

\[
F_i^{rel}.
\]

它们明确相对 standpoint：

\[
F_i^{rel}=\text{from }S_i\text{, I am in }X_i.
\]

不同主体的这些事实可以全部真实：

\[
\forall i\;F_i^{rel}.
\]

### Absolute / simpliciter first-person facts

\[
F_i^{abs}.
\]

它们不再加 standpoint parameter，而是作为 reality simpliciter 的 centered fact。

若 \(i\neq j\)，并且二者代表 distinct complete subject-states，则：

\[
F_i^{abs}\perp F_j^{abs}.
\]

---

## 3. Coherence premise

设现实是一个 non-fragmented coherent world：

\[
Coherent(\mathcal R).
\]

也就是现实不由互不 compossible 的 absolute facts 共同构成。

于是：

\[
F_i^{abs}\perp F_j^{abs}
\]

推出：

\[
\neg(F_i^{abs}\in\mathcal R\land F_j^{abs}\in\mathcal R).
\]

所以：

\[
\boxed{
|\{i:F_i^{abs}\in\mathcal R\}|\le1
}
\]

这就是 **Coherence-Based At-Most-One Result**。

---

## 4. 它解决了什么

它把 singleton cardinality 的一部分从 selector 机制中移走。

此前经常要求：

\[
D\Rightarrow\exists!E^*.
\]

现在可以拆成：

\[
Coherence+Incompatibility\Rightarrow \le1
\]

以及：

\[
\mathsf A\Rightarrow \ge1+\text{which one}.
\]

所以 absolute-center theory 不必让一个复杂 global mechanism 同时承担：

- 排除第二个 absolute center；
- 产生第一个 absolute center；
- 选择其 identity。

前一项可以原则上来自 reality coherence。

---

## 5. 它怎样回应 recombination

Effingham 的 Nowplexity pressure 主要针对把 privilege 建模成一个可由多个 duplicates 共同 instantiate 的 fundamental property。

这里 absolute first-personhood 优先建模成 mutually incompatible centered facts，而非：

\[
A(E)
\]

这种普通 intrinsic property。

因此复制两个 locally identical bearers 不会自动得到：

\[
F_a^{abs}\land F_b^{abs}.
\]

因为两项 absolute centered facts 若不可共同成立，就不能进入同一个 coherent reality。

所以 uniqueness 可以来自：

\[
\boxed{\text{compossibility structure}}
\]

而非额外 cardinality law。

---

## 6. 它没有解决什么

### Existence

\[
\le1
\]

不推出：

\[
\ge1.
\]

可能根本没有任何 \(F_i^{abs}\)。这正是 ordinary perspectival pluralism / first-person antirealism 等模型可以利用的空间。

### Identity

即使存在一个 absolute fact，coherence 不告诉我们它为什么是：

\[
F_R^{abs}
\]

而非：

\[
F_A^{abs}.
\]

### Source

它没有解释某个 local first-person fact 怎样变成 simpliciter fact。

因此仍需要：

\[
\boxed{
\mathsf A:F_i^{rel}\mapsto F_i^{abs}
}
\]

作为 Absolutization Mechanism。

---

## 7. Exact Point of Disagreement

这套论证让正方与 pluralist 的分歧变得非常尖锐。

### Absolute realist

至少一个当前 first-person fact 是 reality simpliciter 的事实：

\[
\exists i\;F_i^{abs}.
\]

### Standpoint pluralist / relativist

所有真实 first-person facts 都只在相应 standpoint 中成立：

\[
\forall i\;F_i^{rel},
\]

且：

\[
\neg\exists i\;F_i^{abs}.
\]

### Fragmentalist

可以承认多个强 first-person facts，同时拒绝 global coherence：

\[
\neg Coherent(\mathcal R)
\]

并把 incompatible facts 分布在不同 fragments。

所以本项目真正需要论证的核心已从“为什么不能有两个 absolute centers”部分转移到：

\[
\boxed{
\text{为什么至少一个 first-person fact 应该是 simpliciter，而不只是 standpoint-relative？}
}
\]

---

## 8. Phenomenal Existence Premise

一个最短的正方论证可以加入：

\[
PE:\quad F_{here-now}^{abs}\in\mathcal R.
\]

即“当前第一人称事实本身以 simpliciter 方式属于现实”。

那么：

\[
PE
+
Coherence
+
FirstPersonIncompatibility
\]

可以推出：

\[
\boxed{
\exists!F^{abs}
}
\]

但这里 **PE 正是最有争议的前提**。

普通现象学只明显支持：

\[
F_{here-now}^{rel}
\]

是否还能支持：

\[
F_{here-now}^{abs}
\]

就是 Residual Fact Problem 的另一种表述。

因此不能把 PE 当作已经由 introspection 证明。

---

## 9. 当前价值

这条结果让项目的最深任务再缩小一步：

\[
\boxed{
\text{At-most-one 可能由 coherence 解释；真正剩下的是 Absolutization。}
}
\]

下一阶段优先研究：

\[
D\Rightarrow\mathsf A
\]

而不是继续寻找能够同时完成全部工作的万能 selector。

## 文献入口

- Kit Fine, “Tense and Reality” (2005)；
- Christian List, “A quadrilemma for theories of consciousness”, *The Philosophical Quarterly* 75(3), 2025；
- Martin Lipman, fragmentalism / standpoint work；
- Olla Solomyak, perspectival pluralism；
- Nikk Effingham, “Now, Again and Again” (2026).
