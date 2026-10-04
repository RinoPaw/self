# 对称性禁阻：结构性绝对第一人称选择的必要条件

> 状态：工作引理。它不是绝对第一人称存在性的证明，只是在“绝对中心完全由完整现实结构决定”的假设下给出必要条件。

## 1. 设置

设完整现实为结构 \(\mathcal R\)，其中候选意识事件构成集合

\[
\mathcal E(\mathcal R).
\]

假设存在一个**纯结构性的唯一选择器**

\[
S(\mathcal R)=E^*\in\mathcal E(\mathcal R),
\]

把完整现实唯一映射到绝对经验事件。

“纯结构性”至少要求选择器尊重结构同构。若

\[
g:\mathcal R\to\mathcal R'
\]

是同构，则要求

\[
S(\mathcal R')=g(S(\mathcal R)).
\]

特别地，当 \(g\) 是 \(\mathcal R\) 的自同构时，\(g\mathcal R=\mathcal R\)。

## 2. 对称性禁阻引理

若 \(S\) 是上述等变（equivariant）的唯一选择器，则

\[
\forall g\in\operatorname{Aut}(\mathcal R),\qquad g(E^*)=E^*.
\]

### 推导

因为 \(g\) 是自同构：

\[
g\mathcal R=\mathcal R.
\]

由结构性要求：

\[
S(g\mathcal R)=g(S(\mathcal R)).
\]

左侧等于 \(S(\mathcal R)=E^*\)，因此

\[
E^*=g(E^*).
\]

证毕。

## 3. 直接后果

若存在自同构 \(g\) 把两个不同候选意识事件互换：

\[
g(E_1)=E_2,\qquad E_1\neq E_2,
\]

那么任何只使用 \(\mathcal R\) 中已给结构、并尊重该自同构的唯一选择器，都不能把 \(E_1\) 单独选成 \(E^*\)。

换言之，同一自同构轨道中的多个元素不能被无参数、纯结构地任意挑出一个。

这与模型论中的一个一般事实相呼应：无参数可定义的元素必须被所有自同构固定。这里暂时只借用这一结构思想，不宣称现实本身就是某种一阶模型。

## 4. 它解决了什么

它把此前模糊的“对称性会让唯一绝对中心可疑”收紧成一个必要条件：

\[
E^*\in\operatorname{Fix}(\operatorname{Aut}(\mathcal R)).
\]

因此，如果绝对第一人称由现实结构唯一推出，候选位置至少不能处在一个被真实结构对称交换的非平凡轨道中。

这同时解释了为什么以下方案都没有自动解决问题：

- 每个主体一个中心；
- 每个光锥一个中心；
- 每个宇宙一个中心；
- 多个完全对称复制体各自一个中心。

只要更高层结构仍允许交换这些中心，它们就没有被纯结构唯一化。

## 5. 它没有解决什么

### 可区分不等于被特权化

即使

\[
\operatorname{Aut}(\mathcal R)=\{id\},
\]

所有意识事件都能在完整结构中被唯一辨认，也仍然没有推出其中一个具有绝对第一人称地位。

因此：

\[
\text{individualization}\not\Rightarrow\text{privilege}.
\]

对称性禁阻只能告诉我们哪些选择不可能由结构完成，不能直接给出真正的选择原则。

### 自发对称破缺不能直接拿来当答案

物理学中对称的定律可以拥有非对称的具体解，但若本项目把“完整现实” \(\mathcal R\) 已经理解成包含实际解、边界条件和全部相关事实，那么真正相关的是**完整现实自身还剩哪些自同构**。

若把某个额外随机变量、初始扰动或选择结果加入 \(\mathcal R\) 才打破对称，还需要继续说明该额外结构与绝对第一人称之间的关系。

## 6. 下一道门槛：典范特权

对称性禁阻通过以后，仍需要一个非循环的典范原则：

\[
J_{\mathcal R}:\mathcal E(\mathcal R)\to X
\]

使某个意识事件成为唯一极值：

\[
E^*=\operatorname*{arg\,ext}_{E\in\mathcal E(\mathcal R)}J_{\mathcal R}(E).
\]

更可能的轨迹版本为

\[
\Gamma^*=\operatorname*{arg\,ext}_{\Gamma}\mathcal A_{\mathcal R}[\Gamma].
\]

真正困难已经从“怎样打破候选之间的对称”推进到：

> 哪一种比第一人称特权更基础的现实结构，能够产生一个**典范且唯一的特权位置**？

## 7. 与充分理由原则的关系

经典对称性论证常与 Leibniz 式充分理由原则联系：若两个候选在完整相关结构下完全等价，就缺少偏向其中一个的充分理由。

本项目目前不把充分理由原则当作公理，但它提供了一个有用的压力测试：若理论声称从完全对称的结构中得到唯一 \(E^*\)，则必须明确指出哪一项非对称结构承担了选择工作。

## 参考入口

- Stanford Encyclopedia of Philosophy, *Symmetry and Symmetry Breaking*: https://plato.stanford.edu/entries/symmetry-breaking/
- Stanford Encyclopedia of Philosophy, *Structural Realism*: https://plato.stanford.edu/entries/structural-realism/
- 关于模型论类比：definable sets/elements 在相应自同构下保持不变；这里只使用这一一般结构原则作为类比。
