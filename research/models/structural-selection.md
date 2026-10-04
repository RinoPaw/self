# 结构性选择模型

## 目标

研究完整现实 \(\mathcal R\) 是否可能内在地、唯一地确定绝对经验事件或绝对经验轨迹。

最简形式：

\[
\mathcal R \Longrightarrow E^*
\]

动态形式：

\[
\mathcal R \Longrightarrow \Gamma^*
\]

这里 \(\Gamma^*\) 是经过意识事件空间的一条唯一轨迹。

## 不把绝对第一人称当作可交换标签

当前模型不预设存在一个外加指针：

```text
absolute_subject -> C
```

更强的设想是：完整现实一旦确定，绝对位置也随之确定。因而可能不存在“全部其他事实完全相同，只交换绝对第一人称”的两个完整现实。

形式上至少要求：

\[
\mathcal R_1=\mathcal R_2
\Rightarrow
E^*(\mathcal R_1)=E^*(\mathcal R_2)
\]

## 结构性选择器

设

\[
S(\mathcal R)=E^*.
\]

若 \(S\) 真正只依赖 \(\mathcal R\) 的结构，它至少应该尊重同构。对任意同构

\[
g:\mathcal R\to\mathcal R',
\]

要求

\[
S(\mathcal R')=g(S(\mathcal R)).
\]

这不是完整理论，只是“纯结构选择”应满足的最低自然性要求。

## 第一门槛：对称性禁阻

若 \(g\in\operatorname{Aut}(\mathcal R)\)，则

\[
g\mathcal R=\mathcal R.
\]

于是

\[
S(\mathcal R)=g(S(\mathcal R)).
\]

因此：

\[
\boxed{E^*\in\operatorname{Fix}(\operatorname{Aut}(\mathcal R))}
\]

也就是说，若某个完整现实的真实自同构能够把两个候选意识事件互换，纯结构性的唯一选择器不能只挑其中一个。

详细推导见 [`../arguments/symmetry-obstruction.md`](../arguments/symmetry-obstruction.md)。

## 第二门槛：可区分不等于特权

即使现实完全刚性：

\[
\operatorname{Aut}(\mathcal R)=\{id\},
\]

仍然只得到“每个候选都能够在完整结构中被唯一辨认”。这不会自动产生：

\[
\exists !E^*\;Absolute(E^*).
\]

因此：

\[
\boxed{\text{individualization}\not\Rightarrow\text{privilege}}
\]

这是当前 Structural Selection Problem 的真正核心。

## 第三门槛：典范选择必须有解释增益

可以探索一种由完整现实定义的量：

\[
J_{\mathcal R}:\mathcal E(\mathcal R)\to X
\]

并要求存在唯一极值：

\[
E^*=\operatorname*{arg\,ext}_{E\in\mathcal E(\mathcal R)}J_{\mathcal R}(E)
\]

轨迹版本则是：

\[
\Gamma^*=\operatorname*{arg\,ext}_{\Gamma}\mathcal A_{\mathcal R}[\Gamma].
\]

但找到唯一极值仍不够。\(J_{\mathcal R}\) 必须满足：

1. 不循环使用“绝对第一人称”定义自身；
2. 来源比第一人称特权更基础；
3. 尊重完整现实的相关同构与物理不变量；
4. 解释为什么极值对应 absolute liveness / actuality，而不只是一个数学上独特的事件；
5. 比 standpoint pluralism 等无全局特权模型提供额外解释力。

这些公式目前只是研究模板。尚未找到合适且无循环定义的 \(J_{\mathcal R}\) 或 \(\mathcal A_{\mathcal R}\)。

## 当前最强反方

Martin Lipman 式 standpoint pluralism 允许：

\[
\mathcal R\Longrightarrow\{S_i,F(S_i)\}_{i\in I}
\]

其中多个主体/时间 standpoint 都承载真实的 perspectival facts，但不存在进一步的全局唯一特权中心。

因此，正方不能只证明某个 \(E\) 可被唯一辨认，还需要证明多 standpoint 的全部真实事实仍然遗漏某种不可相对化的 liveness / actuality。

详细压力测试见 [`../arguments/standpoint-pluralism-challenge.md`](../arguments/standpoint-pluralism-challenge.md)。

## 候选来源

后续重点检查：

- 全局因果结构；
- 时空几何与边界条件；
- 熵与时间箭头；
- 意识的信息/因果结构；
- 全局拓扑；
- 极值原则；
- 多种结构的联合约束。

## 关于 \(w\)

当前优先顺序仍是：

\[
\mathcal R\rightarrow\Gamma^*\rightarrow w.
\]

若唯一轨迹尚未解释，就让 \(w\) 自己负责“选择”只会把问题向上搬一层。因而 \(w\) 暂时只作为可能的轨迹参数，而不承担唯一化工作。

## 成功条件

一个可接受的结构性选择模型至少需要：

1. 唯一确定候选，而不靠随机附加标签；
2. 同时处理主体与当前时刻；
3. 在多元宇宙或分支结构下不自动复制多个最终中心；
4. 与相对论的坐标不变性兼容；
5. 不循环使用“绝对第一人称”本身定义选择规则；
6. 通过自同构禁阻；
7. 从“可区分”进一步解释“为什么被特权化”；
8. 给出比真实但多元的 standpoint facts 更强的解释力。
