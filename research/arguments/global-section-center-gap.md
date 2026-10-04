# Global-Section–Center Gap

> 状态：条件性结构结果。

## 0. 动机

Sheaf / global-section frameworks 很适合表达：多个局部 perspective 是否能共同拼成一个一致的 global state。

这类结构看起来很接近当前目标，因为它天然具有：

- globality；
- compatibility；
- non-factorization；
- unique gluing。

但 global coherence 与 absolute centering 是不同任务。

---

## 1. Sheaf gluing

设 \(X\) 是 perspective / context space，\(\mathcal F\) 是其上的 sheaf。

局部 sections：

\[
s_i\in\mathcal F(U_i)
\]

若在 overlaps 上兼容：

\[
s_i|_{U_i\cap U_j}=s_j|_{U_i\cap U_j},
\]

则 sheaf condition 给出唯一 global section：

\[
s\in\mathcal F(X)
\]

满足：

\[
s|_{U_i}=s_i.
\]

这意味着：局部资料可以属于一个 coherent global structure。

---

## 2. Global section does not select a point

关键：global section 是一个对所有 points / contexts 同时赋值的对象。

它给：

\[
\forall x\in X,\quad s_x.
\]

但不自动给：

\[
\exists!x^*\in X.
\]

若要从 global section 得到特定 local value，必须 evaluation：

\[
ev_{x^*}(s)=s_{x^*}.
\]

而 \(ev_{x^*}\) 已经预先需要 distinguished point \(x^*\)。

所以：

\[
\boxed{\text{unique global section}\not\Rightarrow\text{unique center}}
\]

甚至：

\[
\boxed{\text{global coherence}\not\Rightarrow\text{global first-person privilege}}
\]

---

## 3. Application to perspectives

设 local sections 表示不同主体 / 时刻的 ordinary first-person data：

\[
\{s_A,s_B,s_C,\ldots\}.
\]

唯一 gluing：

\[
\Gamma=Glue(s_A,s_B,s_C,\ldots)
\]

最多说明：这些 perspectives 共同属于一个 coherent totality。

它没有给出：

\[
Absolute(A),
\]

也没有给出：

\[
Absolute(B),
\]

或者任何：

\[
Absolute(x^*).
\]

因此 global-section frameworks 更像是 Stage 0 / anchoring / totalization 的工具，而非 absolute-center selector。

---

## 4. If one adds a distinguished stalk

可以尝试额外要求存在：

\[
x^*\in X
\]

使：

\[
E^*=s_{x^*}.
\]

但这重新产生：

\[
\boxed{\text{Distinguished-Point Problem}}
\]

即 \(x^*\) 从哪里来。

如果 \(x^*\) 由独立 global structure 唯一确定，问题退回 Structural Selection / Natural Section。

如果 \(x^*\) 是额外 primitive，则 global section 没有解释它。

---

## 5. Relation to current literature

2026 年的 phenomenal-consciousness sheaf work 用 global section 表达局部 qualia / perceptual fields 的一致 gluing；它解决的是 unity / global coherence。

另一份 consciousness-first category/sheaf preprint 也把 actual world 建模为 relational sheaf 加 global section，并强调 compatible perspectives glue into one coherent global relational state。

这些工作说明 global-section language 很适合 formalize unity / one-world coherence。

它们也反而清楚展示：

\[
\text{one global state containing many perspectives}
\]

仍不是：

\[
\text{one absolute perspective}.
\]

---

## 6. 当前结论

Global section 是当前项目很好的 **totalization formalism**，但不能单独承担 centering。

因此如果以后使用 sheaf model，应严格区分：

\[
\boxed{\text{gluing problem}}
\]

与：

\[
\boxed{\text{centering problem}}.
\]

最简结论：

\[
\boxed{
\Gamma(\mathcal F)\text{ unique}
\not\Rightarrow
E^*\text{ unique absolute center}
}
\]

## 文献入口

- Tsuchiya & Saigo, “A relational approach to consciousness: categories of level and contents of consciousness”, *Neuroscience of Consciousness* (2021).
- Recent work on sheaf-theoretic / global phenomenal consciousness and global sections (2026).
