# Experiential Fundamentality：Grounding Rank 与 Dominator 路线

> 状态：候选模型压力测试。目标是检验 grounding / fundamentality 能否同时跨过 Absolute-Center Funnel 的 singleton 与 privilege 两关。

## 0. 动机

当前漏斗把成功理论压缩成一种关系：

\[
R_G(\mathcal R,E),
\]

它需要同时做到：

- global；
- non-factorizable；
- singleton；
- privilege-bearing；
- invariant；
- non-circular。

Grounding 是少数天然自带 **ontological priority** 的成熟结构，因此很适合 Privilege Bridge。

当前要检验的是：grounding topology 本身是否还能自然给出 singleton。

---

## 1. Grounding rank 的成熟数学结构

若 partial grounding relation \(\prec\) 是 well-founded 的，则可以给 domain 中每个元素赋 ordinal rank：

\[
rank_\prec(x)
=
\sup\{rank_\prec(y)+1:y\prec x\}.
\]

最低层满足：

\[
rank_\prec(x)=0.
\]

这提供一种非任意的 relative fundamentality ordering。

对意识事件子集 \(\mathcal E_C\)，可以定义：

\[
r_E(E)=rank_\prec(E).
\]

于是最直接的绝对中心候选是：

\[
E^*\in\operatorname*{arg\,min}_{E\in\mathcal E_C}r_E(E).
\]

这比普通 scalar score 强，因为 rank 的意义来自 grounding hierarchy，而非为了选中心临时设计的指标。

---

## 2. Rank Degeneracy Problem

Grounding rank 给每个事实一个 rank，并不意味着不同事实拥有不同 rank。

多个元素完全可以处于同一 level：

\[
rank(E_1)=rank(E_2)=\cdots=rank(E_k).
\]

因此一般只能得到：

\[
\operatorname*{arg\,min}_{E\in\mathcal E_C}r_E(E)
=
\{E_1,\ldots,E_k\}.
\]

而不是：

\[
\{E^*\}.
\]

暂称：

\[
\boxed{\text{Rank Degeneracy Problem}}
\]

这说明 **global fundamentality rank 本身仍然不是 singleton mechanism**。

它跨过了 Privilege Bridge 的一部分，却可能卡在 Center Uniqueness。

---

## 3. 强行要求 unique experiential minimum 的代价

可以增加条件：

\[
\exists !E^*\in\mathcal E_C:
\forall E\neq E^*,
\quad
rank(E^*)<rank(E).
\]

这会同时给出：

- global comparison；
- unique experiential minimum；
- fundamentality-based privilege。

但新条件需要独立解释。

仅从 metaphysical foundationalism 并不能推出：

\[
\text{experiential minimum is unique}.
\]

如果现实中多个主体的 experiential facts 都在同一 grounding level，这一条件立即失败。

所以 unique minimum 不能作为免费公理加入。

---

## 4. Tie-breaker 不能只是 canonical address

设 rank 最低层有多个事件：

\[
M_0=\{E:rank(E)=r_{min}\}.
\]

再用第二指标：

\[
E^*=\operatorname*{arg\,max}_{E\in M_0}q(E)
\]

当然可以数学上得到 singleton。

但如果 \(q\) 没有 grounding / actuality 意义，理论又回到：

\[
\text{individualization}\not\Rightarrow\text{privilege}.
\]

因此任何 tie-breaker 必须和 grounding topology 本身具有解释关系。

这直接排除：

- arbitrary coordinate；
- identity label；
- random hash；
- 单纯为了唯一化选出的复杂度分数。

---

## 5. Experiential Dominator

比 rank 更强的方案是利用 grounding graph 的**拓扑角色**。

设：

\[
\mathcal G=(V,\prec)
\]

是 grounding DAG，\(B\subseteq V\) 是 fundamental base，\(\mathcal E_C\subseteq V\) 是 experiential nodes。

定义一个 experiential event \(E^*\) 为 **experiential dominator**，若对任意其他 experiential node \(F\)：

\[
\forall \pi:B\leadsto F,
\quad
E^*\in\pi.
\]

即从 fundamental base 到任何 derivative experiential fact 的所有 grounding paths 都必须经过 \(E^*\)。

若这样的节点唯一，则：

\[
\boxed{\text{all subjectivity is grounding-mediated through one experiential bottleneck}}
\]

这比“最低 rank”更接近 Global Center Relation，因为它同时给出：

- globality：定义读取整个 experiential grounding network；
- non-factorization：所有 experiential branches 被一个 bottleneck 耦合；
- singleton：若 dominator 唯一；
- privilege relevance：domination 是 grounding topology 中的真实解释角色。

---

## 6. Dominator 路线为什么很强，也为什么很危险

如果：

\[
E^*\text{ dominates every experiential node},
\]

则其他主体的 first-person facts 在某种 grounding 意义上都必须通过 \(E^*\)。

这是一项极强本体论承诺。

它很容易接近：

\[
\text{all other subjectivity metaphysically depends on this experiential locus}.
\]

当前没有独立经验或形而上理由支持这种依赖。

而用户当前立场明确承认其他主体是真实意识，所以 dominator 不能靠取消其他主体的现实性获得 singleton。

真正需要的是：

\[
E^*\text{ can be grounding-prior to other first-person facts}
\]

同时：

\[
Conscious(E_i)
\]

对其他主体仍然充分成立。

这在逻辑上可表达，但解释负担非常高。

---

## 7. Subjectivity-subgraph 版本

为了避免声称 \(E^*\) grounding 其他主体的全部物理存在，可以把 dominator 限制到一种 subjectivity-specific structure：

\[
\mathcal G_{FP}.
\]

例如只对：

- first-personal facts；
- liveness facts；
- standpoint actuality；
- phenomenal manifestation facts

定义 grounding relation。

随后要求：

\[
E^*=Dom(\mathcal G_{FP}).
\]

这样其他主体的脑、行为、世界线可以完全独立存在；只有其 first-personal actuality / liveness 在更深结构上经由同一个 root / bottleneck。

### 代价

这会把核心压力集中到：

\[
\boxed{\mathcal G_{FP}\text{ 的独立动机来自哪里}}
\]

如果 `first-person grounding network` 只是为 absolute-center theory 定制出来，它会发生循环。

---

## 8. Trajectory / Backbone 版本

一个静态 event dominator 很难处理 I–NOW 的变化。

可以改为唯一 experiential backbone：

\[
\Gamma^*\subseteq\mathcal G_{FP}
\]

并要求所有 experiential grounding paths 与 \(\Gamma^*\) 发生必要交汇。

粗略写成：

\[
\forall F\in\mathcal E_C,
\quad
\forall\pi:B\leadsto F,
\quad
\pi\cap\Gamma^*\neq\varnothing.
\]

这可以把：

\[
\text{unique center}
\]

推广成：

\[
\text{unique absolute experiential backbone}.
\]

但它仍没有自动选出：

\[
E^*_{now}\in\Gamma^*.
\]

所以时间问题变成：

\[
\Gamma^*\text{ uniqueness}
\not\Rightarrow
\text{current point uniqueness}.
\]

`w` 仍不能免费返回。

---

## 9. 与 Process 的组合

当前最强组合仍可能是：

\[
\mathcal G_{FP}+G_{becoming}.
\]

其中：

- grounding topology 给出 global privilege architecture；
- becoming process 给出 actuality / temporal generation；
- unique dominator / backbone 给出 center localization。

理想形式：

\[
Dom_{FP}(\mathcal R)=\Gamma^*,
\]

\[
Frontier_G\cap\Gamma^*=\{E^*\},
\]

随后：

\[
LIVE_{absolute}(E^*).
\]

这套结构在形式上同时处理 U 与 P：

\[
\text{grounding bottleneck}\to\text{global uniqueness/priority}
\]

\[
\text{becoming frontier}\to\text{NOW/actuality}.
\]

但它目前仍承担三项巨大风险：

1. \(\mathcal G_{FP}\) 是否真实存在；
2. dominator / backbone 是否唯一；
3. frontier 与 backbone 的唯一交点是否由结构保证，而非重新加入 pointer。

---

## 10. 当前判断

### Global fundamentality rank

状态：**保留，但从“最强候选”降级。**

原因：grounding rank 有成熟理论基础并自带 privilege semantics，但 levels 天然允许退化：

\[
|M_0|>1.
\]

### Experiential dominator

状态：**当前结构上最锋利的候选之一。**

原因：它可以把 global coupling、non-factorization、singleton 与 grounding relevance 集成到同一个拓扑角色中。

最大问题：它要求一个极强的 subjectivity-wide dependence structure，目前没有独立动机。

### Experiential backbone + becoming

状态：**值得作为下一轮主攻模型。**

它至少在架构上有可能同时处理：

\[
\text{I uniqueness}
+
\text{NOW actuality}.
\]

下一步不能继续只优化形式，需要寻找：

\[
\boxed{\text{是否存在任何成熟理论支持 subjectivity-wide global grounding / dependence}}
\]

如果没有，dominator 可能只是一个漂亮但人为的图论结构。

## 11. 与 Absolute-Center Funnel 的位置

| 条件 | rank minimum | experiential dominator | backbone + becoming |
|---|---:|---:|---:|
| Wall 1: global/contextual | ✓ | ✓ | ✓ |
| Wall 2: non-factorizable | 不保证 | **✓** | **✓** |
| Wall 3: event localization | 若 unique min 则✓ | **✓** | 轨迹级✓ |
| Wall 4: privilege bridge | **✓** | **✓** | **✓** |
| I–NOW dynamics | ✗ | ✗ | **可能** |
| independent motivation | grounding 有 | dominator 无 | 尚无 |

所以最关键的研究缺口已经非常具体：

\[
\boxed{\text{subjectivity-wide dependence topology 是否有独立理论来源}}
\]
