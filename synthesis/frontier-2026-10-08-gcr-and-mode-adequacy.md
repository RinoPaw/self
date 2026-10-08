# Frontier 2026-10-08 — GCR and Mode Adequacy

> 当前前沿；取代同日 [Pointwise/Polycentric frontier](frontier-2026-10-08-pointwise-polycentric-reflection.md) 的默认导航，但保留它的原始推理。
>
> 判定：**得到若干可检验的有限形式定理/反例；C0/C1/C2 的本体论胜负仍不确定。**

## 1. 全球唯一性条件

- **GCR-2**：同一个 reality 内任意两个 actual FP facts 可以在同一 centered point 合取；
- **GCR-All**：现实内全部实际 FP facts 有一个共同 centered evaluation point。
- \(GCR_{All}\Rightarrow GCR_2\)，逆向**不成立**；三个 supports \(\{a,b\},\{b,c\},\{a,c\}\) 足以反例。
- 每个 genuine opening 有 actuality-constituting characteristic fact（OCC），不同中心的这些事实 pointwise supports 不相交（SEP），再加 GCR-2，才能推出 AtMostOne。还需 ALO 才能推出 ExactlyOne。

## 2. Unity 候选的真实压力

已测试 U0（single world）、U1（causal / constraint coherence）和 U2（shared overall truthmaker）：**都不单独蕴涵 GCR**。U3（global phenomenal fusion）与 U4（fundamental pointwise actuality）可以强化论证，但各自需新的独立本体根据，且不得循环预设 singleton。

## 3. C1 可满足性与不可还原性

固定同一 objective valuation \(w\)，当 \(L_i\) 的 private vocabularies 两两不交、各局部有兼容 \(w\) 的赋值且 \(K=\top\)，可组合为统一布尔模型。

但 local satisfiability 不保证 global satisfiability：可在未固定的共享 objective \(q\) 上冲突，或被跨模式约束 \(K\) 共同禁止。

弱中立 reduct 遗忘 local-mode facts；增强 neutral tuple 数据又可以无损编码它们。以上都**没有**解决 metaphysical grounding / non-reduction；C1 的不可还原性和其 one-actuality unity 仍是重要本体承诺。

## 4. 可重复检查

- [GCR 条件定理与 U0–U4 检验](../research/arguments/gcr-unity-principle-audit.md)
- [C1 拼接引理、中立 reduct](../research/models/mode-amalgamation-neutral-reduct.md)
- [代码](../tools/model_audit.py)、[单元测试](../tests/test_model_audit.py)

## 5. 下一轮关口

优先 U3/U4 的独立根据、C1 的 hyperintensional grounding 与跨模式 factivity，再做三套理论的同尺度本体成本比较。结果不改变 [current-position](current-position.md) 的 C0/C1/C2 未定判断。
