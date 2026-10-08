# Mode Amalgamation and Neutral Reduct — C1 Adequacy Audit

> 日期：2026-10-08  
> 状态：有限约束模型、明确可证明的 amalgamation 定理与非还原性边界。  
> 关联：[Plural Opening Manifold](plural-opening-manifold.md)、[GCR 审计](../arguments/gcr-unity-principle-audit.md)。

## 0. 结论（不夸大）

原模型「每个 \(F_i\cup W\) 一致 ⇒ 所有 facts 在同一现实中一致」**对一般情况不成立**。可证明的替代命题必须显式固定 shared objective assignment，并约束跨模式规则。

此外，**有限 typed first-person 事实可以被一套中立语言无损编码**；这不自动证明它们在形而上学上可以还原。反过来，忽略 first-person facts 的弱中立 projection 无法复原它们，也不自动证明它们不可还原。两种捷径都无效。

## 1. 规范化的两层约束结构

取以下互不重名的布尔命题：

\[
O=\{o_1,\ldots,o_m\}
\]

是共享客观命题。对于每个 standpoint \(i\)：

\[
L_i=\{(i,p):p\in P_i\}
\]

是 mode-indexed local tokens。取：

- \(W(O)\)：shared objective constraints；
- \(C_i(O,L_i)\)：每个主体的局部事实约束；
- \(K(O,L_1,\ldots,L_n)\)：可包含跨主体联系的 bridge constraints。

定义：

\[
\boxed{Coherent(R)\iff SAT\big(W\land\bigwedge_i C_i\land K\big).}
\]

这里 SAT 是**有限布尔约束的可满足性**。它既不是 ontic actuality 的定义，也不是 first-person irreducibility 的证明。

### 一个肯定案例

共享 \(o:\mathrm{message}\)，局部 \(a:X\)、\(b:Y\)。设：

\[
o:\mathrm{message}=1,\quad a:X=1,\quad b:Y=1,
\]

并有非平凡跨模式联结：

\[
a:X\Rightarrow b:Y.
\]

全局可满足；两个 first-person contents 的单点 supports 可分别是 \(\{a\}\)、\(\{b\}\)，交集为空。故约束统一性可以与 pointwise noncompossibility 并存。

### 一个局部皆可满足、全局却矛盾的案例

若 shared objective \(o:q\) 尚未由 \(W\) 决定：

\[
C_a=(o:q),\qquad C_b=(\neg o:q),
\]

则 \(W\land C_a\) 与 \(W\land C_b\) 分别 satisfiable；联立不 satisfiable。这不是“两个 subject 有不同体验”的合法例子，因为他们对**同一个共享客观命题**作了相反约束。

### 一个跨模式约束导致失败的案例

\[
C_a=a:X,\quad C_b=b:Y,\quad
K=\neg(a:X\land b:Y).
\]

局部二者都 satisfiable，整体不可满足。这表示一个实质的 cross-mode incompatibility；不能靠给不同视角加类型标签消除。

## 2. 有条件成立的 Amalgamation Lemma

设每个 local language 是 \(O\cup L_i\)，其中：

\[
L_i\cap L_j=\varnothing,\;i\ne j.
\]

固定**同一份** shared objective valuation \(w\)；假设对每个 \(i\)，存在局部 valuation \(v_i\)：

\[
v_i\models W\land C_i,\quad
v_i|_O=w.
\]

若 \(K=\top\)（没有额外跨模式限制），定义：

\[
v=w\cup\bigcup_i v_i|_{L_i}.
\]

由于局部字母表除了 \(O\) 外互不相交，这个 \(v\) 定义良好，并使：

\[
v\models W\land\bigwedge_i C_i.
\]

因此：

\[
\boxed{\text{fixed shared }w
+\text{locally extendable }C_i
+\text{disjoint private vocabularies}
+\text{no cross constraints}
\Rightarrow \text{global satisfiability}.}
\]

只说「每份 \(W\land C_i\) 有*某个*模型」远远不够：各局部模型可能对同一未决定的 \(O\) 选择了不同赋值。

有 \(K\) 时，充分条件可改为存在一个**同一联合扩张** \(v\)，使 \(v\models K\)；这需要单独证明或运行 solver，不能从局部 satisfiability 得到。

**逻辑边界**：这个 lemma 仅说明 typed classical satisfiability；不处理 List 所说多个 bare first-person facts 若被视作 mode-erased facts 时的不可共真。若把 typed atoms 悄悄读成 object-level neutral relations，就丢掉了 C1 所需的 ontic interpretive weight。

## 3. First-Person Modes 的不可还原性：三种不同的「还原」

- **编码或翻译（encoding）**：存在注入映射，将整个 typed-model 信息记为若干第三人称 tuples；可以解码。这只说明**表达能力**。
- **相对于给定 reduct 的重建（relative reconstruction）**：某个被明确限制的 neutral base \(B\) 是否唯一决定全部 mode facts？这可以用共享同一个 \(B\)、不同 mode facts 的反例判定。
- **形而上学 grounding / identity reduction**：所有 genuine first-person facts 是否**由**非 first-person facts 完全构成，或与之同一？编码等价、语义刻画、有限可计算性，均不足以独立判定。

### N0 — 弱中立 reduct

\[
N_0(R)=\text{only shared objective assignment }w.
\]

取两个 structures \(R_1,R_2\) 具有相同 \(w\)，但 local obtaining arrangements 不同：

\[
N_0(R_1)=N_0(R_2),\quad
FP(R_1)\ne FP(R_2).
\]

它反驳「\(N_0\) 单独固定所有 FP facts」；**不反驳**更强、可包含 local phenomenal/psychophysical facts 的 C0。

### N+ — 增强中立编码

令：

\[
N_+(R)=\big(w,\{(i,p,v_i(p))\}_{i,p},\ldots\big).
\]

对于有限 typed data，可以无损恢复其全部赋值。这说明“元语言中写出 \(m\Vdash p\)”或「第三人称能编码它」都不足以裁决 ontic non-reduction。

但 N+ 是否是**合法、非循环、说明性充分**的 neutral metaphysical base，正是需要哲学论证的地方。把模式标签搬进关系事实后，不能再凭编码本身宣布已解释「模式如何 fundametally obtain」。

## 4. C1 真正需要给出的定义与辩护

| 前提 | 最小承诺 | 目前证据强度 |
| --- | --- | --- |
| I1 — Ontic modes | \(m_i\Vdash p\) 是构成现实的事实，mode 对 identity 本质性 | 作为 C1 primitive 接受；无独立推导 |
| I2 — Grounding non-reduction | 给出 neutral theory class，证明无法完整 grounding 或 identity-reduce I1 | 未得到 |
| I3 — Objective agreement | 每个模式遵循同一共享 objective history / invariant facts | 形式模型可明确定义并检验 |
| I4 — Cross-mode bridges | 跨主体关系 \(K\) 不引入与各局部 facts 冲突的约束 | 每个具体 \(K\) 需联合检验 |
| I5 — One actuality | 多个 modes 属于 one actual totality，且没有各自独立 actual worlds | 在模型中可设定；独立 metaphysical unity 仍待辩护 |

这五项不能缩成一句「它是 non-relational constitutional mode」；I1+I5 是最难从第三人称解释与 U0/U1 的区别中获得独立理由的部分。

## 5. C0/C1/C2 同尺度差异

| 层级 | C0 | C1 | C2 |
| --- | --- | --- | --- |
| 形式层 | 一个共享 W + 主体相关事实 | W + 多个 typed / primitive modes | W + 一个 global opening / role |
| 意义层 | ordinary perspective / local mineness genuine | mode constitutive of first-person facts | one absolute I–NOW status |
| 一致性 | 普通逻辑与心理物理模型 | typed coherence + explicit K | global role assignment / consistency |
| 本体论待证 | neutral completion 对 actuality 足够 | 多模式的不可还原性与单一 actuality unity | 唯一性及为何需要该 global role |
| 可反驳门槛 | 独立 FP arity witness | neutral reduction 或 unity 不可能证明 | 缺乏额外见证、C0/C1 自然容纳事实 |

本轮没有「C1 已经胜出」的结论。它已经有比之前更严格的**类型化逻辑候选模型和反例边界**；其不可还原性仍须正面证明，C2 也仍须单独处理 C0。

## 6. 有限可执行检验

[tools/model_audit.py](../../tools/model_audit.py) 枚举少量布尔变量，验证：

1. typed two-mode total structure satisfiable 且 pointwise supports disjoint；
2. 每个 local problem satisfiable 但共享未确定的 objective variable 无法 amalgamate；
3. cross-mode constraints 可阻止 joint satisfaction；
4. pairwise centered intersections 可以全非空而全体交集为空；
5. weak neutral projection 多对一；带模式标签的中立编码可无损表示有限数据。

命令：

- `python tools/model_audit.py`
- `python -m unittest discover -s tests -v`

该脚本不含哲学真实性验证器：每项 passing test **只证明对应有限模型中的布尔断言和编码性质**。

## 7. 相关文献及解释边界

- Christian List, *A quadrilemma for theories of consciousness*（2025）：与 pointwise non-compossibility、one-world fragmentalism 的分类相关。https://doi.org/10.1093/pq/pqae053
- Martin A. Lipman, *Subjective Facts about Consciousness*（2023）：world-side first-person facts / metaphysical standpoint 的重要竞争结构。https://doi.org/10.3998/ergo.4649
- Martin Lipman, *Standpoints: Time and Subjectivity*（2026）：多 standpoint / fragmentation 的持续讨论。https://doi.org/10.1093/9780198921318.001.0001

引用提供哲学背景；本文的有限 SAT lemma、反例和 reduct 区分是本项目的模型工作，**不归因于这些作者**。
