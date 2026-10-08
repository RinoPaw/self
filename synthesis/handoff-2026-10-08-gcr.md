# Handoff 2026-10-08 — After GCR and C1 Model Audit

> 取代 2026-10-05 交接；当前研究结论见 [current-position](current-position.md)。

## 已完成

- [GCR 独立论证审计](../research/arguments/gcr-unity-principle-audit.md)：GCR-2 与 GCR-All 不等价；OCC+SEP+GCR-2 条件推出 AtMostOne；一般 one-world、interaction 和 overall truthmaker 不强制 GCR。
- [C1 局部／全局约束与 neutral reduct](../research/models/mode-amalgamation-neutral-reduct.md)：固定 shared valuation 的受限 Amalgamation Lemma；两种局部 SAT 但全局不 SAT 的反例；N0 的遗忘性与 N+ 编码能力并存。
- [有限脚本](../tools/model_audit.py) 和 [回归测试](../tests/test_model_audit.py)：只检验指定的有限布尔结构，没有形而上学证明能力。

## 2026-10-08 的补充进展

- [U3 MI / global co-conscious audit](../research/arguments/co-conscious-unity-to-mode-audit.md)：global co-conscious field 是否存在，与共同 mode 身份、同一 centered perspective 分开审查。
- [U4 scope / actualizer audit](../research/arguments/actuality-quantifier-scope-audit.md)：从「每个事实某点可真」到「全体事实共同单点为真」有量词缺口；AIM 是仍需独立辩护的候选。
- [C1 B1 grounding audit](../research/models/neutral-contrast-grounding-audit.md)：中立比较基底必须包含完整 local phenomenality；语义编码、sample determinacy、metaphysical grounding 不能相互替代。
- [有限测试](../tests/test_model_audit.py) 已增加相关反例与条件模型；测试通过只涉及给定有限结构。

### 重叠模型更新

- [MI/AIM 关系审计](../research/arguments/mi-aim-incidence-audit.md) 区分 weak MI-Share、strong MI-Excl 及 AIM-Functionality；原 mode:E→M 单值表示过强。
- [同尺度成本比较](../research/models/endgame-theory-matrix.md) 固定各理论均需解释普通意识与同一现实。
- [Roelofs 文献核验](../literature/roelofs-2016-between-subject-unity.md) 为 across-subject unity 提供独立哲学反方，**不证明 C1 的多重 fundamental modes 真实存在**。

## 当前新方向：B1 explanatory residue（优先于更多单中心定理）

- [完整研究](../research/arguments/b1-explanatory-residue-audit.md)：\(\mathcal B_1\) 的 descriptive coverage、phenomenal grounding、absolute global center 是三个不同问题。
- Conitzer Case A 中的 external display mapping 在**模拟内部事实**之外有额外机制，但不能自动外推为我们世界的绝对中心。Mary 的 knowledge gap、Lewis/Perry 的 de se gap 也首先是独立于 C2 singleton 的议题。
- 下一轮核心任务：从最强 C0 构造一个具体的 local phenomenal grounding/identity account，找准其未付出的解释成本；再检查是否需要 C1 的 irreducible modes 或 C2 的 global singleton。
- 保留现有 MI/AIM/GCR 条件审计作为 secondary route；无新证据不反复输出相同结论。

## B1 constitution 完整化的实际进展

- [三套 C0 构成模型](../research/models/c0-phenomenal-constitution-packages.md)：I 后验同一、F 基础局部意识、Q 中立范畴根与意识组合。
- [双向压力测试](../research/arguments/b1-grounding-adversarial-test.md)：C0 不能拿列出 P 冒充 grounding；C1/C2 不能仅添加 mode 或 absolute opening 并继续复用未解释的全部 P。
- 接下来优先对 **C0-F 的 bearer-indexed P 的事实身份**开展具体非还原性反驳；其次审 C0-I 和 C0-Q 的 real explanatory links。


## 当前新增：C0-F 体验事件身份论

[新审计](../research/arguments/c0-f-subject-experience-identity-gate.md) 与[文献档案](../literature/subject-experience-givenness-dossier.md)核对 Taylor 2020、Guillot 2017、Sá Pereira 2026、SEP 与 Roelofs 2016。局部主体—体验的 token identity 可被 PE 事件本体论解释，仍未得到现象性质 q 的深层 grounding；token sharing 是该模型的反方压力。下轮先检查一个真正 lived、bearer-indexed 事件的事实身份是否还缺不可还原的 ontic mode。

## 尚未完成的本体工作

1. 具体重建 B1 的 full local consciousness grounding（包括 identity、phenomenal primitives、psychophysical connection），不能拿 coverage 当作完整 explanation。
2. 在 B1 的真正 grounding 缺口上与 C1 / C2 同尺度比较；若发现 independent residual X，先过 C0，再过 C1。
3. 处理非布尔、hyperintensional 的 constitutional obtaining，与共享客观事实、interaction 和 global factivity 的兼容条件。
4. 若前三项未产生 decisive result，停止新的“唯一性定理”命名，改做 C0/C1/C2 的明确 primitive cost/compression comparison。

## 防止退回旧循环

C2 不能以 MEP-O/GCR 的定义直接充当自身证明；C1 不能以「这些模式是 irreducible」一句话充当 non-reduction proof。C0 仍在 theory space，单单击败 C1 并不足以证成 C2。

与文献比较时继续区分 List 的 centered-world non-compossibility 和本项目的 ontological reflection 假说。
