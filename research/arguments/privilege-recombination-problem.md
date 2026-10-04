# Privilege–Uniqueness Recombination Problem

> 状态：从时间形而上学借来的条件性压力测试。
>
> 核心来源：Nikk Effingham 2026 对 multiple presents / Nowplexity 的讨论。

## 1. 时间版本

设 classic moving spotlight theory 使用一个 fundamental property：

\[
P=Presentness.
\]

某个 instant \(t\) 之所以 metaphysically privileged，是因为：

\[
P(t).
\]

Effingham 考虑一种标准的 metaphysical recombination principle：fundamental properties 原则上可以由 fundamental duplicates 多重实例化。

若：

\[
P(t_1)
\]

是可能的，recombination 可以支持某些世界中：

\[
P(t_1)\land P(t_2),
\quad t_1\neq t_2.
\]

于是：

\[
\Diamond(\exists t_1\neq t_2\;Present(t_1)\land Present(t_2)).
\]

即 **Nowplexity**。

Effingham 的关键点之一是：如果一个 tense theory 想让 Presentness 必然唯一，就需要说明为什么 ordinary recombination 不适用于 Presentness，或者让唯一性来自别的结构（例如 unique growing edge）。

---

## 2. 第一人称 analogue

设未来的 absolute-first-person theory 最终引入某个 privilege property：

\[
A=LIVE_{simpliciter}.
\]

并有：

\[
A(E^*).
\]

如果 \(A\) 只是一个普通 fundamental / intrinsic property，并且其 bearer 可以被 metaphysically duplicated / recombined，则可能出现：

\[
A(E_1)\land A(E_2),
\quad E_1\neq E_2.
\]

因此：

\[
\boxed{
Fundamental(A)
\not\Rightarrow
\Box\exists!E\;A(E)
}
\]

甚至 actual-world uniqueness：

\[
\exists!E\;A(E)
\]

也不能仅从 `A is fundamental` 推出；还需要 actual structure 保证只一个 bearer。

---

## 3. 为什么这对 primitive LIVE 也重要

Primitive LIVE 路线常被视为最简单终点：

\[
\exists!E^*\;LIVE(E^*).
\]

但这里其实包含两个独立 primitive commitments：

### Privilege primitiveness

\[
LIVE\text{ is fundamental / primitive}.
\]

### Cardinality constraint

\[
|\{E:LIVE(E)\}|=1.
\]

前者不自动给后者。

因此理论必须选择：

1. 把 singleton cardinality 也写成 primitive law；
2. 让 LIVE 的 essence 包含 unique-instantiation；
3. 提供 global structural reason 使只有一个 bearer；
4. 接受多个 absolute-like centers 的 metaphysical possibility。

---

## 4. Unique-instantiation essence

一种回应是把 LIVE 写成 essentially singleton：

\[
\Box\forall x\forall y
((LIVE(x)\land LIVE(y))\rightarrow x=y).
\]

这形式上完全可行。

但项目仍会问：

\[
\boxed{
\text{为什么 LIVE 的本性包含 unique instantiation？}
}
\]

若答案只是“absolute 就定义成唯一”，这保证术语一致，却没有解释现实为何实例化这种 essence。

因此 essence strategy 解决 cardinality consistency，不自动解决 source explanation。

---

## 5. Global-role strategy

另一种回应更符合 Anchored Nested Dominance：LIVE 不是可自由复制的 intrinsic property，而是一种 global role：

\[
LIVE(E)\iff Role_{\mathcal R}(E).
\]

例如 role 本身的定义可以要求一个 global structure 只有一个 occupant：

\[
\exists!E\;Role_{\mathcal R}(E).
\]

这种 relational role 可以避开简单的 property recombination，因为复制一个 bearer 的 local intrinsic profile并不会自动复制其 global role。

这与 Locality–Duplication No-Go 的结论一致：

\[
\text{absolute privilege likely must be genuinely global if it is non-primitive and singleton}.
\]

但它重新承担 Global Relevance Requirement：为什么该 role 与 actuality / liveness 有关？

---

## 6. 对 Nested Dominance 的影响

如果 top-level actuality 被写成：

\[
TopDominant(E),
\]

其 singleton 不能只靠一个可复制的 intrinsic marker。

更稳妥的是：

\[
TopDominant_{\mathcal R}(E)
\]

作为完整 hierarchy 中的 relational role，并由 top competition structure 保证：

\[
\exists!E\;TopDominant_{\mathcal R}(E).
\]

这样 **uniqueness** 可以来自 role topology，而不是来自 `actuality property` 自己。

于是任务进一步分离：

\[
\text{global role topology}\Rightarrow\text{singleton}
\]

和：

\[
\text{role–realizer / actuality bridge}\Rightarrow\text{LIVE meaning}.
\]

这正是 Anchored Nested Dominance 当前的两大未解模块。

---

## 7. 与多元宇宙 / 多时间流的关系

Effingham 还指出，若存在多个独立 timestreams，很自然地每个 timestream 都拥有自己的 present。

对应到本项目：若现实分成多个完全独立 absolute-eligible sectors：

\[
\mathcal R=R_1\sqcup R_2\sqcup\dots,
\]

而 privilege rule 分别在每个 sector 内运行，则：

\[
E^*_1,E^*_2,\dots
\]

会自然复制。

所以 global singleton 还要求：

\[
\boxed{\text{privilege mechanism must not factorize over independent sectors}}
\]

这再次支持 Non-Factorization / Global Coupling Requirement。

---

## 8. 当前结论

Effingham 的 Nowplexity 结果为本项目提供一个很强的新提醒：

\[
\boxed{
\text{privilege and uniqueness are logically distinct explanatory burdens}
}
\]

一个 theory 可以成功解释：

\[
Why\ E\ is\ privileged
\]

却仍失败于：

\[
Why\ exactly\ one\ E\ is\ privileged.
\]

因此以后所有 actuality / LIVE 候选都必须单独通过：

1. **Privilege Test**：为什么这一性质 / role 是 actuality-like；
2. **Cardinality Test**：为什么其 extension 恰好是 singleton；
3. **Recombination Test**：复制 / 多 sector / 多时间流时是否重新多实例化；
4. **Non-Stipulation Test**：唯一性是否只靠额外 brute clause。

## 文献入口

- Nikk Effingham, “Now, Again and Again: The Metaphysics of Many Presents”, *Pacific Philosophical Quarterly*, online 28 July 2026, DOI 10.1111/papq.70023；
- Daniel Deasy, “The Modal Moving Spotlight Theory”, *Mind* 131 (2022)；
- Peter Forrest, growing block / locus-of-change work；
- Phillip Bricker, “Absolute Actuality and the Plurality of Worlds” (2006).
