# MI / AIM Bridge Audit — Overlap, Realization Incidence, and Cardinality

> 2026-10-08 | **条件性形式结论 + 文献反方压力**。  
> 不代表宇宙级 co-consciousness 已成立，也不代表 C1 获得不可还原性证明。  
> 上游：[U3](co-conscious-unity-to-mode-audit.md)、[U4](actuality-quantifier-scope-audit.md)、[C1 中立对照](../models/neutral-contrast-grounding-audit.md)。

## 0. 本轮最重要的修正：不要预设 mode_of 是函数

前一轮使用 \(\operatorname{mode}:E\to M\) 描述每个体验对应一个 mode。对于允许 **experience sharing / overlapping subjects** 的对手，此写法自带一个重要假设：**单一经验 token 只能实现一个 ontic mode**。

为了公平检验 C1，需要允许一般的 incidence relation：

\[
B\subseteq E\times M,\quad B(e,m):\text{episode }e\text{ realized in mode }m.
\]

同时单独记录：

- \(P\subseteq E\times S\)：某经验属于哪些 *subjects*；
- \(C\subseteq E\times E\)：哪些经验之间有 phenomenal co-consciousness；
- \(G\subseteq A\times M\)：哪些 ultimate actualizers 支持哪些 modes。

三种关系 **subject ownership、mode realization、actualizer grounding** 不能自动同一。主体和根本模式可能一对一，也可能一对多；是否允许后一种关系是争议的本体论选择。

## 1. MI 有两个强度：共享模式 ≠ 同一个模式

### MI-Share（弱）

\[
\forall e,f\,[C(e,f)\Rightarrow
\exists m\,B(e,m)\land B(f,m)].
\]

相关 co-conscious 经验**至少共享一个**模式。它完全不排除每个 episode 同时参与其他 modes。

### MI-Excl（强）

\[
\forall e,f,m,n\,
[C(e,f)\land B(e,m)\land B(f,n)\Rightarrow m=n].
\]

只要两经验 co-conscious，其所有 realized modes 必须完全一致且唯一。这不只是共用一个 experiential component；它否认 co-conscious participants 的**额外 mode memberships**，具有 overlap-exclusion 负担。

若每个实际 mode 至少被一个实际 episode realize (**Surj**)，\(E\neq\varnothing\)、所有 episodes 两两 \(C\)-相关 (**Cover**)，并接受 MI-Excl，则：

\[
\boxed{Cover+MI\text{-}Excl+Surj+Nonempty
\Rightarrow |M|=1.}
\]

形式证明：对任意 \(m,n\in M\)，Surj 给出 \(e,f\) 使 \(B(e,m)\)、\(B(f,n)\)；Cover 给出 \(C(e,f)\)，MI-Excl 推出 \(m=n\)。

MI-Share **不足以**得到此结论。取两经验 \(e,f\)，各自有 modes \(\{m_1,m_2\}\)；即使 \(C=E\times E\)，MI-Share 真且 \(|M|=2\)。这一反例使用一般 incidence relation，正是先前 single-valued mode_of 表达不了的情况。

**额外警告**：MI-Excl 在 \(C(e,e)\) 成立时本身就排除「同一经验 token 属于多个 modes」。不能以其过强的假设排除 overlap，然后声称对 overlap 构造了独立反证。

## 2. Roelofs 提供了什么实质反方

Luke Roelofs (2016) 直接论证 **between-subject phenomenal unity 可以有一致的哲学解释**，且在某些方案中同一个 token experience 可属于不止一个 numerically distinct subject；他逐条回应 subsumption、phenomenal interdependence 与 unintelligibility 异议。

这使「co-consciousness 必定只发生在同一个 subject 内」不能当作无需争论的定义。但它**并未直接证明** experience-sharing 的实际存在，更没有证明两个 metaphysically irreducible obtaining modes 能共同 realized by one episode。主体多重归属到 mode 多重归属还需要额外的 **Subject–Mode Realization** 桥梁，不能偷换。

Roelofs & Sebo (2024) 开放获取论文研究 shared *token mental states* 在伦理计算中的后果；其出发点也是条件可能性，不能从 neurotechnology 的设想推出 shared subjects 已实证确认。

新的区分：

\[
\text{Co-consciousness}
\not\Rightarrow \text{OneSubject}
\not\Rightarrow \text{OneMode}
\not\Rightarrow \text{OneAbsoluteLocalI–NOW}
\]

这个箭头链中的每一个 **非蕴涵** 均须相对于允许相应的主体/mode incidence 的**形式签名**理解；文献本身不证明最后两个形而上学非蕴涵。

## 3. 连接性及 partial overlap 不能替代 global Cover

可构造三个 episodes：

\[
P(e_1)=\{a\},\quad
P(e_2)=\{a,b\},\quad
P(e_3)=\{b\}.
\]

若假设「共享某 subject」足以给 co-consciousness：

\[
C(e_1,e_2),\quad C(e_2,e_3),\quad
\neg C(e_1,e_3).
\]

co-consciousness 的**无向图是连通的**，但不满足「全部 episodes 两两共同意识」的 Cover。这个关系可能非传递；不能未经证据把 connectivity 或 transitive closure 当作完整 shared experience。

这里仅是一个**形式上的部分重叠模型**。真实 phenomenal unity 的传递性、共享体验的身份，以及 sub-experiences 的边界都是理论争点；模型不宣称所有 co-consciousness 事实真的遵循「共享主体」规则。

## 4. AIM：唯一 source 与唯一 target 被混淆

令 \(G(a,m)\)：ultimate actualizer \(a\) ground / realize mode \(m\)。若只有一个 ultimate actualizer \(a^*\)，它完全可以与 \(m_1,m_2\) 都处于 \(G\) 关系：

\[
G(a^*,m_1)\land G(a^*,m_2),\qquad m_1\neq m_2.
\]

一个源头可以拥有多个 outputs；**source-cardinality 为 1** 不约束其 \(G\) relation 的 output-cardinality。

强版 AIM 是：

\[
\boxed{\forall a,m,n\,[G(a,m)\land G(a,n)\Rightarrow m=n].}
\]

即 **AIM-Functionality**：每个 source 至多 realize 一个 mode。再加 one-source、每个 actual mode 都由该 source realized、至少一个 mode，才得到 \(|M|=1\)。

更弱的原则「每个 mode 只依赖一个 source」是 **reverse functionality**，一个 actualizer 可 support 多 modes，故无法推出 mode singularity。

**AIM 的核心证明责任**：给 source→mode 的单值性一个独立的 metaphysical account。即使其能得 one mode，mode→joint centered truth（GCR）和 local privileged I–NOW 仍需论证。

## 5. 不能用单一 mode 的定义回避反方

MI-Excl 和 AIM-Functionality 都是强判别原则：

- **对于 C2**：若获得独立事实支持，可协助 C2 的 at-most-one 主张；仍须对抗 C0 的 mode-existence 拒绝。
- **对于 C1**：可通过非排他的 overlapping incidences、one actualizer→many modes 的本体架构拒绝；仍须正面辩护 modes 的 irreducibility 与 one-actuality unity。
- **对于 C0**：可承认共享体验 / 一个 actualizer，却认为根本 mode 集合为空；由此发现 MI/AIM 的 singleton 推导不能自动保证模式 existence。

因此比较重点是**独立的 mode individuation / functional grounding principles**，不是重复计算符合所选公理的有限结果。

## 6. 本轮可检验的形式结果

[tools/model_audit.py](../../tools/model_audit.py) 与 [回归测试](../../tests/test_model_audit.py) 继续保留旧 single-valued mapping 的有限实例，同时增加：

- 全 pairwise co-conscious Cover + MI-Share + two modes **可满足**；
- Cover + MI-Excl + all modes realized **无法保留两个 distinct modes**；
- overlapping subject incidence 的 connectivity 与 complete Cover 分离；
- one source 可 support two modes；AIM-Functionality 才阻止这种 cardinality；
- weak reverse-functionality 不能替代 AIM-Functionality。

这些是给定有限关系的可复核检查，**不是**关于真实本体论或实际 shared consciousness 的经验验证。

## 7. 文献记录（本轮核验级别）

1. Luke Roelofs (2016), “The Unity of Consciousness, Within Subjects and Between Subjects”, *Philosophical Studies* 173(12), 3199–3221, DOI https://doi.org/10.1007/s11098-016-0658-7 — **ANU 研究门户作者/出版元数据和摘要核验**。摘要明确讨论 between-subject unity 与 shared token experience；本轮未对全部正式全文逐页审查。
2. Luke Roelofs & Jeff Sebo (2024), “Overlapping Minds and the Hedonic Calculus”, *Philosophical Studies* 181, 1487–1506, https://doi.org/10.1007/s11098-024-02167-x — **出版方开放获取论文网页摘要、开头部分核验**；这是条件性 overlap 讨论。
3. SEP, [The Unity of Consciousness](https://plato.stanford.edu/entries/consciousness-unity/) (2025 revision) — **条目相关段落核验**，包括 unity 的多重意义与 split-brain/partial-stream 模型争议。
4. SEP, [Supervenience](https://plato.stanford.edu/entries/supervenience/) §3.5 — **条目相关段落核验**：supervenience 与 grounding 不等同；本文 AIM 是自拟的条件原则，不应归于 SEP。
5. Martin Lipman, *Standpoints: Time and Subjectivity* (2026), https://doi.org/10.1093/9780198921318.001.0001 — **出版方书籍与章节摘要**；世界可以采用多 standpoint 描述，不能未经全文核验把我们的 MI/AIM 公式归给作者。

## 8. 下一步最低价值门槛

下一轮只有在找到 MI-Excl / AIM-Functionality 的**非定义性**根据、具体的 world-side mode individuation 方案，或真实影响 C0/C1/C2 成本比较的新结果时，才继续增加正方 unique proof。否则应进入 **C0/C1/C2 同尺度 primitive-grounding cost comparison**，而不是对同一个逻辑非蕴涵无限重述。
