# Internal Asymmetry Generators

## 0. 位置

`Monism Selector Gap` 之后，Stage 0 不再只问：

\[
\exists !D\ ?
\]

还要问：

\[
D\text{ 内部怎样出现一个非任意的 }A_D?
\]

本文件整理目前两类最有根据的生成方式。

## 1. Configurational Asymmetry

设 fundamental whole / deeper reality 为：

\[
D=\langle X,R_1,\ldots,R_n,P_1,\ldots,P_m\rangle.
\]

即使每个 fundamental relation 都是 symmetric：

\[
R_i(x,y)\Leftrightarrow R_i(y,x),
\]

整个配置仍然可能 asymmetric。

关键量不是单个 relation 的方向，而是：

\[
Aut(D).
\]

如果某个 conscious event `E` 满足：

\[
E\in Fix(Aut(D)),
\]

它至少通过了结构唯一化的必要条件。

### 优点

- 不需要 primitive directional relation；
- 与现有 symmetry obstruction / canonical selector 框架完全兼容；
- 可以由 global property distribution、network topology、boundary conditions 等产生。

### 限制

仍然只有：

\[
\text{structural distinguishedness}.
\]

所以：

\[
E\in Fix(Aut(D))\not\Rightarrow LIVE(E).
\]

这条路线只解决 **Internal Selector Problem**，没有单独跨过 Privilege Bridge。

## 2. Generative Asymmetry

第二条路线让 order 来自真实 generation。

设 generative operation：

\[
O:I\mapsto O(I).
\]

output 依赖 operation 与 input 才出现，所以自然得到：

\[
I\prec_O O(I).
\]

Bader 把 grounding、causation、composition 作为这一类操作讨论。

在 `self` 中可写成：

\[
D\xrightarrow{O}E_i.
\]

或动态版本：

\[
E_i\xrightarrow{G}E_j.
\]

这提供一种比普通结构差异更强的 priority source。

### 优点

- asymmetry 由 generation 产生，不只是坐标或描述差异；
- 很适合和 grounding / fundamental becoming 接轨；
- 对 Privilege Bridge 比纯 configurational asymmetry 更有希望。

### 限制

一个 operation 可以生成很多 outputs：

\[
O(D)=\{E_1,E_2,\ldots,E_n\}.
\]

所以：

\[
\exists !O\not\Rightarrow\exists !E^*.
\]

这就是 Process-to-Center Gap 的更一般形式。

## 3. Hybrid：配置决定 channel，operation 提供 priority

目前最值得测试的是混合结构。

设：

\[
A_D^{config}
\]

先在 `D` 中唯一确定一条 generative channel：

\[
\Gamma^*.
\]

再由 fundamental operation `G` 在这条 channel 上产生事件：

\[
G:\Gamma^*(w)\mapsto\Gamma^*(w').
\]

于是可能得到：

\[
(D,A_D^{config},G)
\Rightarrow
\Gamma^*
\Rightarrow
E^*.
\]

相比单纯 selector，这个版本多了真正的 generation；相比单纯 becoming，它又避免整个 frontier 上同时出现多个同等级 centers。

## 4. 新的三重要求

一个成功的 `A_D` 现在至少要通过：

### Invariance

\[
A_D\text{ 在真实表示变换 / gauge 下保持不变。}
\]

### Uniqueness

\[
A_D\Rightarrow\exists !E^*\quad\text{或}\quad\exists !\Gamma^*.
\]

### Privilege relevance

`A_D` 的结构角色必须与 actuality / generation / fundamentality 有独立关系，不能只是 arbitrary mathematical label。

否则仍会失败于：

\[
\text{individualization}\not\Rightarrow\text{privilege}.
\]

## 5. 目前最有希望的具体形式

第一版候选顺序：

1. **unique invariant generative channel**：完整结构中唯一不变的生成链；
2. **unique grounding ancestry**：只有一个 conscious event / trajectory 占据特殊 grounding ancestry；
3. **boundary-selected process**：global boundary condition 先打破结构对称，再由 process 提供时间/生成方向；
4. **extremal + generative**：extremal principle 负责唯一化，generative operation 负责 privilege bridge。

这些都仍只是工作模型，下一步需要寻找现有物理或形而上理论中的真正先例。

## 6. 当前最紧的问题

现在可以把正方最重要的问题压缩成：

\[
\boxed{\exists A_D\text{ such that }D\Rightarrow A_D\Rightarrow E^*\text{ and }A_D\text{ is privilege-relevant}?}
\]

这比早期直接寻找：

\[
\mathcal R\Rightarrow E^*
\]

多了一层，但也更精确：我们现在知道缺的到底是什么。

## 文献入口

- Ralf M. Bader, “Fundamentality and Non-Symmetric Relations” (2020).
- Jonathan Schaffer, “Monism: The Priority of the Whole” (2010).
- Lok-Chi Chan, “Nature's Complexity Alive” (2026).
- `research/arguments/monism-selector-gap.md`.
- `research/arguments/symmetry-obstruction.md`.
- `research/arguments/process-to-center-gap.md`.
