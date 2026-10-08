# GCR Defense Audit — Global Unity Does Not Yet Yield a Single Viewpoint

> 日期：2026-10-08  
> 状态：条件性定理 + 反模型 + 独立前提压力测试。**未证明 C2、也未否定 C1/C0。**  
> 主要前提：[MEP-S / GCR 上轮审计](pointwise-polycentric-reflection-audit.md)、[当前立场](../../synthesis/current-position.md)。

## 0. 最精确的新结论

**在实际 first-person fact 的共同现实性和不同 complete centers 的可分辨性成立时，GCR 足以推出 at-most-one；但 GCR 本身尚无法从一般的 unity / truthmaker / actuality 原则中导出。**

另外，须区分两个 GCR 强度：

- **GCR-2（pairwise reflection）**：同一 actual reality 中每一对 first-person facts，都能在一个共同 viewpoint 联合为真。
- **GCR-All（total reflection）**：同一 actual reality 的**全部** actual first-person facts，可在同一个 viewpoint 联合为真。

GCR-All 蕴涵 GCR-2；一般情形下，反方向不成立。全局唯一性证明有时只需要 GCR-2，但需要**separating facts**，并且每个 opening 的这些事实都算 actuality-constituting facts。

## 1. 不含糊的模型语言

设：

- \(R\)：一个 actual totality；
- \(\Pi_R\)：其中允许的 centered evaluation points；
- \(FP_R\)：声称由 \(R\) 本体组成的 first-person facts，而非仅由人讲述的句子；
- \(S_R(F)\subseteq\Pi_R\)：centered evaluations 中 fact \(F\) 成立的 pointwise support；
- \(A_R(F)\)：\(F\) 构成完整现实的事实（本体承诺）；形式上 **不能**偷换为 \(S_R(F)\neq\varnothing\)。

那么：

\[
GCR_2:\quad \forall F,G\in FP_R\,[
A_R(F)\land A_R(G)\Rightarrow
S_R(F)\cap S_R(G)\neq\varnothing].
\]

\[
GCR_{All}:\quad
\{F\in FP_R:A_R(F)\}\neq\varnothing
\Rightarrow
\bigcap_{F:A_R(F)}S_R(F)\neq\varnothing.
\]

**量词警戒**：当 \(FP_R=\varnothing\)，GCR-2 真得空泛，不能推出一个 first-person opening 存在。C0 因此不是从 GCR-2 自动排除。

**类型警戒**：\(A_R(F)\) 与 \(S_R(F)\) 原本来自不同语义/本体层；GCR 本身正是它们之间的桥梁，不能把二者都定义为“同一单点满足”后称它被证明。

## 2. 有效的条件性 singleton theorem

设：

- **OCC**：每个 genuine opening \(i\) 都贡献 actuality-constituting \(F_i\in FP_R\)；
- **SEP**：不同 complete openings \(i\ne j\) 有 identifying / separating facts，满足 \(S_R(F_i)\cap S_R(F_j)=\varnothing\)；
- **GCR-2**：实际 first-person facts 两两同点联合相容。

则：

\[
\boxed{OCC+SEP+GCR_2\Longrightarrow |\operatorname{Openings}(R)|\le1.}
\]

证明：若 \(i\ne j\) 都 genuine，OCC 给出 actual \(F_i,F_j\)。SEP 使其 support 交集为空；GCR-2 又要求非空，矛盾。加 **ALO**（至少一个 opening）得到 exact-one。

这里 SEP 可以由恰当理解的 complete token states + Local Exclusivity 推动；但一般谓词如“我有经验”可能在多个中心同为真，因而**不能**以 arbitrary first-person proposition 的不相容性为前提。

不能把上述结果简称成“one actuality ⇒ one opening”，因为 **OCC、SEP、GCR-2、ALO** 全是额外工作。

## 3. Pairwise 与全体反映也要区分

取 \(\Pi=\{a,b,c\}\)，三个 actual facts 的 support 为：

\[
S(F_1)=\{a,b\},\quad
S(F_2)=\{b,c\},\quad
S(F_3)=\{a,c\}.
\]

任意两集合交集非空：

\[
GCR_2=\text{true},
\]

但：

\[
S(F_1)\cap S(F_2)\cap S(F_3)=\varnothing.
\]

故：

\[
GCR_2\not\Rightarrow GCR_{All}.
\]

当 argument 使用的是完整的 truthmaker/total-state 统一，而只证明 pairwise compossibility，不能直接推出完整观点的 existence。对于**已经含两两互斥的 characteristic facts**，第 2 节证明仍有效；不要混淆这两种语境。

## 4. 五种 unity defense 的严格压力测试

### U0 — One-world identity

所有主体在同一个 causal / objective history；\(\exists!R\,Actual(R)\)。

**不推出 GCR**：可以有一个 W、一个 R 和两个 pointwise non-compossible actual first-person fact slots。否认此模型的本体合法性，还要额外给出理由。

### U1 — Shared causal and relational coherence

主体互动、彼此可约束；局部事实对共同物理数据相容。

**不推出 GCR**：跨模式规则可以把经验事实联结成一个 constraint-satisfiable structure，却不需要单点同时经历两种 complete states。

### U2 — Global compositional truthmaker

完整状态 \(T_R\) 使各个事实 obtain；它们有一个共同 overall truthmaking base。即使假设：

\[
\exists!T_R\,GroundsAllFacts(T_R),
\]

也不蕴涵：

\[
\exists!\pi\,\forall F\in FP_R\,\pi\models F.
\]

一个 truthmaker 允许对不同 modes 有不同 typed manifestations。**ground/source identity 与 standpoint identity 不是一个关系**。要从 U2 推出 GCR，还需：

\[
\text{SharedTruthmaker}(F,G)
\Rightarrow \text{SharedCenter}(F,G),
\]

这正是尚待辩护的额外原则。

### U3 — Phenomenal co-conscious global fusion

规定 complete actual first-person facts 必须处在同一 maximal co-conscious experiential unity 内。

这一路线可能产生强约束，但必须证明**所有实际第一人称事实都要求同一 co-conscious field**。普通主体间有互动、同属一个物理世界、甚至有共同来源，都不满足这个强前提。若把 U3 直接定义成「共同主体全部经验可被一个 perspective 同时经验」，则等价于假设反对 C1 的核心内容。

### U4 — Irreducible pointwise actuality / truthmaker singularity

把 genuine actuality 的最终 obtaining 本质定义为一个具体 centered evaluation point；多 perspective 的总结构只能是外在集合。

**足以接近 GCR，但争议最大**。若只有这个定义才排除 C1，则它是 primitive ontological choice，尚未独立比较过 polycentric candidate，也没有由 ordinary first-person data 推出。

## 5. Countermodel strength and verdict

在 typed finite structure 里可以令：

\[
Actual(R)\land OneWorld(R)\land SharedObjectiveBase(R)
\land SAT(GlobalConstraints_R)
\]

并令：

\[
S(F_a)=\{a\},\quad S(F_b)=\{b\},\quad
A_R(F_a)=A_R(F_b)=1.
\]

它满足 U0、U1、弱的 U2，却违反 GCR-2。有关 constrained amalgamation 的正反实例见 [跨模式模型审计](../models/mode-amalgamation-neutral-reduct.md) 与 [可执行穷举](../../tools/model_audit.py)。

这足以证明：**给定上述形式化的 U0/U1/U2，不蕴涵 GCR-2**。它仍未解决这个有模式的结构是否包含不可还原的实际 first-person facts；**形式反例只打击未经附加本体前提的推理**。

## 6. 与 List / Lipman 的公平关系

Christian List 的 *A quadrilemma for theories of consciousness*（2025）区分了 first-person realism、non-solipsism、non-fragmentation、one world，并讨论多个替代 horn。其 centered-world 单点 non-compossibility 论证保持有效；本项目须进一步说明，为何选择能推出 singleton 的 global non-fragmentation/unity 要求。

Martin Lipman 的 *Subjective Facts about Consciousness*（2023）和 *Standpoints: Time and Subjectivity*（2026）提供可以认真讨论世界侧 subjective facts 与多 standpoint 的理论资源；这不等于他的立场已获证明，或已证明我们的 typed model 就是其最优模型。

核验级别：本次以出版方论文页、可查找摘要/公开书目为主；**没有以新一轮完整精读代替此前文献笔记的论证**。

- List: https://doi.org/10.1093/pq/pqae053
- Lipman 2023: https://doi.org/10.3998/ergo.4649
- Lipman 2026: https://doi.org/10.1093/9780198921318.001.0001

## 7. 结论与下一次可判别的任务

1. **得到**：精确的 OCC+SEP+GCR-2 ⇒ AtMostOne 证明；GCR-2/GCR-All 非等价反例。
2. **没得到**：从一般 one-world、shared causal history、共同 grounding root、局部一致性独立推出 GCR。
3. **保留的正方途径**：论证 U3 / U4 在所有 non-solipsistic conscious reality 中普遍适用，且其解释增益超过 C0/C1；不能通过词义强行排除多元模式。
4. **反方任务**：C1 必须面对自己的 irreducibility、global grounding 与 cross-mode consistency 压力；不能把 U0/U1 满足性称作 metaphysical adequacy。

当前 **C2 无新胜负结果**。最上游问题依然是：全现实 unity 为何必然是 *single-center* unity？
