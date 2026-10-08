# 当前研究立场

> 更新：2026-10-08。研究假说与条件性论证，**没有证明 C2 存在或不存在**。  
> 最新前沿：[2026-10-08 MEP / GCR 审计](frontier-2026-10-08-pointwise-polycentric-reflection.md)。  
> 完整推导：[Pointwise–Polycentric Reflection Audit](../research/arguments/pointwise-polycentric-reflection-audit.md)。  
> 论证依赖：[研究依赖图](../research/DEPENDENCIES.md)；文件状态：[研究审查索引](../research/REVIEW-2026-10-08.md)。

## 1. 问题与概念边界

原始问题：为什么偏偏是这个人、这个时代、这个当前经验？

项目研究比普通第一人称更强的候选：

\[
\exists! E^*\,AbsoluteOrientation(E^*).
\]

同时承认其他意识的真实存在。以下五项需要严格区分：

\[
Consciousness\neq LocalFirstPerson\neq PhenomenalMineness
\neq IrreducibleFirstPersonFact\neq AbsolutePrivilege.
\]

ordinary for-me-ness、de se、自我定位、现象学的在场感都不自动证明 absolute privilege。

## 2. 三种竞争解释

| 理论 | 核心主张 | 当前地位 |
| --- | --- | --- |
| **C0 — Subject-Neutral Actuality** | 一份实际现实，可有多个真实意识与局部第一人称；actuality 本身无需 irreducible first-person mode | 仍可行；承诺较弱，暂有解释经济性优势 |
| **C1 — Plural First-Person Actuality** | 一份现实中有多个 genuine irreducible first-person modes，无全局唯一特权 | **明确的形式／本体论公理候选**；未证 ontic irreducibility 和全局统一 |
| **C2 — Singular Centered Actuality** | 完整现实的 actuality 有一个 global privileged I–NOW opening | 原始研究目标；可提出 primitive role-first architecture，未得到独立证据 |

C2 必须分别跨过**first-person arity**（与 C0 竞争）和**global singular privilege**（与 C1 竞争）；任何只打败 C0 的结果都不能算已建立 C2。

## 3. 最重要的修正：MEP 被拆分

### MEP-S — 单点语义中心性

标准 centered-world 评价点：

\[
\langle\omega,\pi\rangle
\]

一次只用一个 \(\pi\) 解释第一人称命题。不同 complete centers 的 centered propositions 可以没有共同的单点满足者。这是**评价单位的形式约定及其语义后果**。

### MEP-O — 完整现实的本体单中心性

\[
Actual(R)\Rightarrow
|\operatorname{FundamentalFirstPersonModes}(R)|=1.
\]

这比 MEP-S 强；既排除 C1，也排除 C0 的“无需第一人称根本模式”版本，因而无法被直接当作来自 neutral premises 的无争议引理。

### GCR — Global-to-Centered Reflection

对于共同组成同一 actual reality 的 first-person facts：

\[
Actual(R)\land F,G\in FP(R)
\Longrightarrow
\exists\pi\,[\langle R,\pi\rangle\models F\land G].
\]

此式承担从**共同属于现实**到**同一单中心评价点联合成立**的桥梁。其现有理由尚不独立于被争议的全球统一要求。

**已确定的推理边界**：

\[
PerspectiveVariance\not\Rightarrow MEP\text{-}O,
\qquad
MEP\text{-}S\not\Rightarrow GCR.
\]

从 MEP-S 加交集语义得到的，是 pointwise first-person compossibility 的结论。要将其用于整个 actuality 的唯一性，仍须 GCR 或同等强的跨层 unity/completeness premise。

## 4. 有限反模型证明了什么

取一个 objective history \(w\) 与两个 perspective loci \(a,b\)，其第一人称完整状态分别为 \(X,Y\)。可以定义：

\[
\llbracket I\text{ in }X\rrbracket=\{(w,a)\},\quad
\llbracket I\text{ in }Y\rrbracket=\{(w,b)\}.
\]

两组 centered extensions 交集为空，同时构造一个 distributed structure 包含两个 loci、共享 history、只带一个 overall actuality status。

这表明：**单点互不相容**与**分布式共处一个总结构**在规定相应语义时可以相容。它反驳了未经 GCR 论证的直接跃迁。

它**没有证明**：
1. distributed modes 是本体论不可还原的 first-person obtaining；
2. 把模式写进事实定义便完成 third-person non-reduction；
3. 声明一个 actuality status 就足以解释 global unity；
4. 分别相容的 mode-local facts 一定在加入任意 cross-mode constraints 后仍相容。

旧 Plural Opening Manifold 的 FP2–FP4 是清楚的**理论原始承诺**，不得再以“通过 collapse 检查”为由计作它们已获得独立证明。局部一致性也需要额外的 objective-invariance 与 cross-mode-compatibility 条件才能安全推广。

详见 [C1 旧构造](../research/models/plural-opening-manifold.md) 与 [本轮严格审计](../research/arguments/pointwise-polycentric-reflection-audit.md)。

## 4.1. 本轮进一步检验：GCR 与 C1 的明确边界

**GCR 的强弱不能混淆**。GCR-2 只要求现实内任意**两个** genuine first-person facts 有共同单点见证，GCR-All 要求**全部**事实有一个共同单点见证。三个 supports \(\{a,b\},\{b,c\},\{a,c\}\) 给出 GCR-2 成立、GCR-All 失败的有限反例。

得到条件定理：

\[
\boxed{OCC+SEP+GCR_2\Rightarrow AtMostOneOpening}
\]

其中 **OCC** 要求每个 opening 提供一个 actuality-constituting fact；**SEP** 要求不同 complete openings 有 support 不相交的 characteristic facts；**GCR-2** 是本体的全球到单点反映。再加 ALO 才得到 exact-one。**GCR-2 在无实际 FP facts 时真得空泛，不能排除 C0。**

分别检查的 unity 路线：

- U0：one history / one actual totality；
- U1：跨主体 causal/constraint coherence；
- U2：共同 overall truthmaker / grounding root；
- U3：global co-conscious fusion；
- U4：最终 actuality 必须 pointwise-centered。

前 **U0–U2 均不足以单独推出 GCR**；U3 还需独立的所有主体 co-consciousness 证据；U4 可以支持单中心，但风险是将结论预置在 actuality 的定义里。因此目前没有一个不循环的 GCR 推导。

对 C1 则得到**受限 amalgamation lemma**：在共享 objective valuation \(w\) 固定、各 local vocabularies 在 \(w\) 外不重叠、每一局部可延拓至 \(w\)、没有冲突的 cross-mode bridge \(K\) 时，全局布尔约束可满足。共享命题要求相反赋值，或 \(K\) 明确禁止两局部状态共现时，可出现「局部皆可满足、全局不可满足」。

中立 reduct 的边界也已确定：遗忘 local facts 的弱中立投影 \(N_0\) 无法恢复它们；包含所有 mode data 的增强中立 tuples \(N_+\) 可无损编码有限结构。**前者没有证明 ontic irreducibility，后者也没有证明 metaphysical grounding reduction。**

- [GCR 完整论证](../research/arguments/gcr-unity-principle-audit.md)
- [C1 跨模式相容与中立编码](../research/models/mode-amalgamation-neutral-reduct.md)
- [有限可执行例子](../tools/model_audit.py) 与 [回归测试](../tests/test_model_audit.py)

---

## 5. 条件性唯一性链：显式列出额外前提

- **LE**：同一 perspective 不能同时具有互斥的 complete conscious states。
- **SPC-pointwise**：两个第一人称命题若在同一个 centered evaluation point 联合为真，就存在同一 perspective 的满足者；这是点级语义结果。
- **GCR / NF-SPC**：一个实际现实内多个 genuine first-person facts 必须 pointwise 联合相容；这是**独立待证的本体论统一前提**。
- **FPNC**：不同 complete standpoints 的适当第一人称内容无法在同一点完全同现（依赖内容互斥性及同一评价视角）。
- **ALO**：现实至少需要一个 genuine first-person opening；C0 不接受它为必然。

所以，保留的**条件**推导是：

\[
GCR+LE+\text{cross-center incompatibility}
\Longrightarrow AtMostOneOpening;
\]

\[
AtMostOneOpening+ALO\Longrightarrow ExactlyOneOpening.
\]

旧链“MEP → SPC → FPNC → at-most-one”仅在 MEP 被加强、且 global-to-pointwise 桥梁明确成立时可用于全球唯一性。直接采用 MEP-O 已经预置中心数目，不能再把它当作独立推导的成果。

[SPC 论证](../research/arguments/perspective-closure-principle.md)、[FPNC 审计](../research/arguments/first-person-non-compossibility-audit.md)、[USL 条件结果](../research/arguments/unitary-singularity-lemma.md) 继续保留，按以上边界阅读。

## 6. 各理论目前必须支付的成本

| 测试 | C0 | C1 | C2 |
| --- | --- | --- | --- |
| actuality 的形而上学底层 | neutral obtaining / instantiation 等 | one actual totality + plural constitutive modes | one global opening role |
| genuine ordinary consciousness | 允许 | 允许 | 允许 |
| irreducible first-person mode | 不需要额外假定 | 多个；**原始承诺待辩护** | 唯一；**原始承诺待辩护** |
| 全局一致性 | 共享世界内的普通一致性 | **cross-mode constraints 与 unity 待完善** | global role 与 actuality 的同一性待解释 |
| 独有的证据支持 | 尚无排除其可能性的反例 | 尚无决定性证明 | 尚无能同时排除 C0/C1 的 witness |

C1 应被视为严肃竞争者，同时其形式模型**不能自动升级为完整形而上学证明**。C2 也不能通过对 C1 的疑虑直接获胜，必须面对 C0。

与 Christian List 的讨论关系：pointwise non-compossibility 在 centered-world semantics 中成立；plural/fragmentalist 方案属于其讨论过的可选理论位置。本项目需要独立论证 C2 才能胜出。

## 7. 证据与研究止损原则

C2 的新增 witness \(X\) 至少应满足：

\[
Independent(X)\land NaturalFit(C2,X)
\land \neg CheapNonSingularAccommodation(X).
\]

其中 NonSingular 包含 C0 与 C1。**不以模型文件数量、术语命名、现象学的强烈感受、纯结构上的唯一性或 conditional lemma 数量更新证据等级。**

默认不重复投入 generic mineness、ordinary presence、pure selection、duplicate lottery、death transfer、global cosmic subject 等旧路线，除非出现独立的新前提或能击败 C0/C1 的判别事实。

Locality（Selective Local vs Universal-I）与 trajectory/dynamics 保留为**C2 成立之后的下游课题**。

## 8. 下一步真正开放的关口

1. **强 unity 路线审计**：U0–U2 已有条件反例；接下来需研究 U3 的 global co-consciousness / U4 的 pointwise actuality 是否有独立理由，且不得把 single opening 先写进定义。
2. **C1 ontic non-reduction**：已给出弱 reduct 的不充分性与强编码的可逆性；下一步要限定合法的 neutral grounding base，并检验 modes 的 hyperintensional identity / grounding。
3. **C1 具体 MPGC 公理审计**：有限布尔约束已能展示相容与不相容；下一步需给交互、共享历史及 constitutional first-person facts 一个实际可用的跨 mode 规则。
4. **同尺度成本比较**：将 C0、C1、C2 的 primitive content、解释收益、模态成本与认识论后果摆在同一表中。

[论证依赖与缺口图](../research/DEPENDENCIES.md) 将这四条任务与历史证据对应起来。

## 9. 当前总判定

\[
\boxed{\text{C0、C1、C2 均未被决定性排除；C2 的 absolute singleton 尚未建立。}}
\]

**本轮真正推进**：在 MEP-S/MEP-O/GCR 分层上，给出 OCC+SEP+GCR-2 的条件单中心定理、GCR-2 与 GCR-All 的非等价反例、U0–U2 不蕴涵 GCR 的受限形式反例，以及 C1 跨模式约束和中立 reduct 的判别边界。**这些形式结果均不能直接证明 C1/C2 的形而上学真实性。**
