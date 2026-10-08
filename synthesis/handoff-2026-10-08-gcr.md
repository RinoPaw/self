# Handoff 2026-10-08 — After GCR and C1 Model Audit

> 取代 2026-10-05 交接；当前研究结论见 [current-position](current-position.md)。

## 已完成

- [GCR 独立论证审计](../research/arguments/gcr-unity-principle-audit.md)：GCR-2 与 GCR-All 不等价；OCC+SEP+GCR-2 条件推出 AtMostOne；一般 one-world、interaction 和 overall truthmaker 不强制 GCR。
- [C1 局部／全局约束与 neutral reduct](../research/models/mode-amalgamation-neutral-reduct.md)：固定 shared valuation 的受限 Amalgamation Lemma；两种局部 SAT 但全局不 SAT 的反例；N0 的遗忘性与 N+ 编码能力并存。
- [有限脚本](../tools/model_audit.py) 和 [回归测试](../tests/test_model_audit.py)：只检验指定的有限布尔结构，没有形而上学证明能力。

## 尚未完成的本体工作

1. 给 U3（所有实际 FP facts 的 co-conscious fusion）或 U4（fundamental pointwise actuality）一个**不预置全局唯一性**的独立根据，并与 C0/C1 进行同尺度比较。
2. 对 C1 明确允许的 neutral base 的 vocabulary、truthmakers、grounding 与 modal variation；论证为什么 typed facts 的编码成功/失败不等同于 ontic reduction。
3. 处理非布尔、hyperintensional 的 constitutional obtaining，与共享客观事实、interaction 和 global factivity 的兼容条件。
4. 若前三项未产生 decisive result，停止新的“唯一性定理”命名，改做 C0/C1/C2 的明确 primitive cost/compression comparison。

## 防止退回旧循环

C2 不能以 MEP-O/GCR 的定义直接充当自身证明；C1 不能以「这些模式是 irreducible」一句话充当 non-reduction proof。C0 仍在 theory space，单单击败 C1 并不足以证成 C2。

与文献比较时继续区分 List 的 centered-world non-compossibility 和本项目的 ontological reflection 假说。
