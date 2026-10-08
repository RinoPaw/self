# 当前研究立场

> 更新：2026-10-08。研究假说与条件性论证，**没有证明 C2 存在或不存在**。  
> 最新前沿：[2026-10-08 B1 解释剩余审计](frontier-2026-10-08-b1-explanatory-residue.md)；上轮 [GCR / U3-U4](frontier-2026-10-08-gcr-and-mode-adequacy.md)。  
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

## 4.2. U3/U4 与 C1 grounding 的二次压力测试

本轮把之前尚宽泛的 U3、U4 论证进一步收缩到**明确的新前提**：

- **U3 global co-consciousness**：local subject unity / causal connectivity 不会自动成为宇宙级 co-conscious coverage。若进一步接受 **MI**（co-conscious episodes 有同一 fundamental obtaining mode）与每个 mode 都由实际 episode 实现，才条件性推出一个 mode；随后仍需 mode-to-centered-fact 的 **reflection**，以及涉及局部 I–NOW 时的 **localization**。
- **U4 单一 actuality/truthmaker**：\(\forall F\exists\pi\,T(F,\pi)\) 不推出 \(\exists\pi\forall F\,T(F,\pi)\)。一份 reality 或一个 actualization source 并不规定其 mode realizers 只有一个。必须另证 **AIM**（Actualizer–Mode Identity）；若以 single centered actualizer 直接定义 AIM，则预设结论。
- **C1 non-reduction**：引入较强的 neutral baseline **B1**（客观历史、真实主体、完整 local phenomenality、psychophysical facts），不能只拿纯物理 B0 做稻草人。B1 与模式的有限样本独立性，尚不能证明其差异是 metaphysically admissible。更强的 B2 可以完整编码 modes，但也不能凭编码证明 grounding reduction。**relative determination、metaphysical supervenience、grounding/identity** 是三层不同判别。

文档：[U3 与 MI](../research/arguments/co-conscious-unity-to-mode-audit.md)、[U4 与量词作用域](../research/arguments/actuality-quantifier-scope-audit.md)、[B1 与 grounding](../research/models/neutral-contrast-grounding-audit.md)。有限例子由 [测试](../tests/test_model_audit.py) 检验；测试不涉及本体论真实性。

以上收紧了正反双方的证明责任，**没有新增支持 C2 的独立经验事实，也没有使 C1 获得不可还原性的证明**。

## 4.3. 经验共享与 MI/AIM 基数的进一步修正

以单值函数 mode:E→M 表示 first-person realization，会**预先排除**同一个经验 token 参与多个模式的竞争假说。现在使用一般 relation B⊆E×M，并明确：

- **MI-Share**：共同意识的两经验至少共享一个 mode，允许其它 memberships；不推出 singleton。
- **MI-Excl**：共同意识的两经验所参与的所有 modes 均相等，才与 global Cover、realization、nonempty 等条件合取推出 one-mode cardinality。这要求独立排除重叠，不能只凭 unity 一词成立。
- **AIM-Functionality**：一个 actualizer 至多 realize 一个 mode。每个 mode 恰有一个 actualizer 属于反向唯一性，即使世界只有一个 source，仍允许它 realize 多个 modes。

Roelofs（2016）提出不同主体之间的 co-consciousness 和 shared token experience 的哲学可能性，是排他式 MI 的认真反方；尚不证明根本模式本身能够多重归属，或这种经验共享在现实中存在。

[严格论证和来源等级](../research/arguments/mi-aim-incidence-audit.md)；[C0/C1/C2 成本比较](../research/models/endgame-theory-matrix.md)。


## 4.4. 研究主轴：C0 的 B1 解释剩余（2026-10-08）

[本轮完整审计](../research/arguments/b1-explanatory-residue-audit.md) 以包含所有真实局部体验的 B1 挑战 C0，避免拿「只有物理数据」冒充其最强版本。最重要的是区分：

- **Descriptive saturation**：B1 **包含**所有 local qualia、mineness、de se 和主体间普通事实；
- **Grounding/constitution**：B1 中写出这些事实**尚未解释它们为何成立**。C0 的 G 层有真实尚未偿还的解释债务；
- **Absolute-centered completeness**：现实是否还需唯一 global I–NOW，是 C2 的独立新增前提，不能预先定义为 B1 的“缺口”。

Mary 的知识论证首先关乎 physical facts 与 phenomenal knowing/being 的争论；自我定位关乎 centered cognitive state；Conitzer 的 Case A 有独立的*模拟外* selector，Case B/C 不提供对应现实世界里的独立机制证明。**三者都不直接推出一个 unique absolute selector**。

新增的判断标准：指出 independently identifiable residual \(X\)（不能以「唯一绝对第一人称」定义），或证明 B1 的 local phenomenal grounding 不可行；然后检查 C1 的多模式候选。没有得到新的 C2 witness；C0 的理论经济性仍仅为条件性的，不表示它已完成 local consciousness 的 constitution。

---
## 4.5. 首次具体化 C0 意识奠基：I / F / Q

[三套 C0 意识构成候选](../research/models/c0-phenomenal-constitution-packages.md) 与 [反方压力测试](../research/arguments/b1-grounding-adversarial-test.md) 将 C0 由「全部局部意识事实均可列入世界」推进至三套分别需要辩护的解释方式：

| C0 包 | 假设的 \(P_i\) 构成方式 | 尚未清偿的解释成本 |
| --- | --- | --- |
| **C0-I** | 局部现象事实与神经/机体事实后验同一 | 同一性及 phenomenal concepts 的实质理由 |
| **C0-F** | 每个主体真实的 \(P_i\) 是 fundamental world-side fact | 原始意识事实、因果配合、主体边界；无更深 ground |
| **C0-Q** | 内在范畴基底 \(Q\) 与主体组织、构成规律 \(L_Q\) 联合 ground \(P_i\) | Q 的具体性质、组合及所有权、非循环的 bridge |

C0 的 subject-neutral actuality 与严格物理主义是两种不同分类轴；Russellian 中立一元论亦不天然等于本项目的 C0。

**同尺度新检验**：即使单独引入 C2 的唯一 \(\Omega^*\)，它仍未自动解释所有其他主体的 \(P_i\)。C1 的 modes 亦须针对相同的局部 consciousness grounding 问题提供真实 explanation delta。C0-F 作为不否认任何人体验的最强竞争者仍存活为**本体候选**，其基础事实的解释停点则必须如实记账。

本轮未证明 I/F/Q 任一正确、未独立证明 C1 的 obtaining modes，也未发现 C2 独有的剩余事实。

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

1. **C0-F 的事实身份审计（优先）**：能否严谨地论证「某主体实际感到痛」无法作为 fundamental、bearer-indexed 的 world-side fact，除非额外包含一个 irreducible mode？不能先将 mode 放入真正体验的定义。
2. **C0-I/Q 的具体机制**：后验同一论需要认真解释 identity；范畴本体方案需要非循环的 composition law 使局部 P 真正 obtain。不能让待解释意识偷偷充当其 ground。
3. **共同的解释债务**：如果 C0 在一个地方失败，应检查 C1/C2 是否修复了同一个缺口，特别是 C2 如何解释全部其他主体的真实现象生活。
4. **只在有新增判别事实时重启全局唯一性**：GCR/MI/AIM 仍为条件论证，不将同一逻辑非蕴涵反复命名为突破。

[研究依赖图](../research/DEPENDENCIES.md) 已加入这一路线的分层结构。

## 9. 当前总判定

\[
\boxed{\text{C0、C1、C2 均未被决定性排除；C2 的 absolute singleton 尚未建立。}}
\]

**当前进展**：B1 已由简单的意识事实清单推进为三套具体 C0-I/F/Q 的 local consciousness constitution 候选；它们各有未证明的身份同一、原始现象事实或范畴组合前提。C1/C2 还没有展示对这些同一难题的独立修复。**C0 尚未被证明完成意识的最终 grounding，C2 也尚无独有的绝对中心事实 witness。**
