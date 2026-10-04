# Two-Tier First-Person Realism

> 状态：当前项目对“普通第一人称 / 绝对第一人称”最直接的形式化版本。
>
> 目的：检验是否可以同时保留多个 genuine conscious subjects、一个 coherent world，以及一个 simpliciter absolute center，而不把每个主体都赋予同等级的 unrelativized first-person facts。

## 1. 动机：List Quadrilemma

Christian List 的 quadrilemma 使用四个主张：

1. **First-person realism**：对任意 conscious subject，都有 first-personal facts；
2. **Non-solipsism**：多于一个 conscious subject 真实；
3. **Non-fragmentation**：一个 world 中的全部 facts 是 compossible 的；
4. **One world**：现实只有一个 world。

List 论证四者不能同时成立。

关键原因：如果 Alice 与 Bob 都有 simpliciter first-person facts，那么：

\[
I\text{ am in }X
\]

与：

\[
I\text{ am in }Y
\]

作为不同主体的完整 first-personal facts 不能共同被一个 single coherent world 实例化。

---

## 2. 本项目的原始区分比 List premise 更细

本项目从最开始就区分：

### Ordinary first-personhood

每个 conscious subject 都可以有：

- for-me-ness；
- de se organization；
- self-location；
- direct givenness；
- local standpoint-relative first-person facts。

形式化：

\[
\forall i\;LocalFP(S_i).
\]

### Absolute first-personhood

另外研究是否存在唯一一个：

\[
\exists!E^*\;AbsoluteFP(E^*).
\]

这里的 `AbsoluteFP` 表示一种不可继续相对化、进入 reality simpliciter 的 global centered status。

所以：

\[
\boxed{
LocalFP\neq AbsoluteFP
}
\]

不是语言区分，而是两层 ontology 的候选。

---

## 3. 两类 first-person facts

令：

\[
F_i^{rel}
\]

表示相对于 standpoint \(S_i\) 成立的 ordinary first-person fact。

例如：

\[
F_A^{rel}=\text{Alice-from-Alice's-standpoint is in state }X.
\]

所有主体都可以真实拥有：

\[
\forall i\;F_i^{rel}.
\]

这些 facts 因为显式带有 standpoint parameter，可以共同存在：

\[
F_A^{rel}\land F_B^{rel}\land F_C^{rel}.
\]

另外设：

\[
F_i^{abs}
\]

表示同一 perspective 被提升为 simpliciter / unrelativized first-person fact。

绝对假说要求：

\[
\exists!i\;F_i^{abs}.
\]

---

## 4. Coherence-Based At-Most-One Principle

如果不同 center 的 absolute first-person facts 真的是 unrelativized centered facts，则对 \(i\neq j\)：

\[
F_i^{abs}\perp F_j^{abs}
\]

其中 \(\perp\) 表示不能在同一个 coherent non-fragmented reality 中共同实例化。

若现实满足 Non-Fragmentation / Coherence：

\[
Coherent(\mathcal R),
\]

则：

\[
\boxed{
|\{F_i^{abs}:F_i^{abs}\in\mathcal R\}|\le 1
}
\]

这给 absolute-center uniqueness 的 **at-most-one** 部分提供一种结构来源。

它不依赖：

- arbitrary scalar maximum；
- global ranking tie-breaker；
- freely recombinable LIVE property；
- one-winner-per-brain competition。

其来源是：

\[
\boxed{\text{global coherence of unrelativized centered facts}}
\]

---

## 5. 它怎样回应 Effingham 的 Recombination Pressure

Effingham 2026 指出，若 Presentness 是普通 fundamental property，recombination 可以允许多个 bearers 同时 instantiate Presentness。

Two-Tier model 不把 absolute first-personhood 首先建模成：

\[
A(E)
\]

这种可自由复制的 intrinsic property。

它把绝对层建模成：

\[
F_i^{abs}\in Reality_{simpliciter}.
\]

若两个 absolute centered facts 是 incompatible，则多实例化会破坏 coherence，而不是得到一个正常的 “two LIVE centers” world。

因此：

\[
\boxed{
\text{uniqueness can come from compossibility constraints rather than property cardinality}
}
\]

这只解决 at-most-one；仍没有给 existence。

---

## 6. 它如何绕开 List Quadrilemma

严格说，这个模型没有同时接受 List 的四个原始 claims。

它修改 / 分层第一条。

List 的 strong first-person realism：

\[
\forall S_i\;FPFact_{simpliciter}(S_i).
\]

本模型改成：

\[
\forall S_i\;FPFact_{relative/local}(S_i)
\]

并：

\[
\exists!S^*\;FPFact_{simpliciter}(S^*).
\]

所以它可以原则上同时保留：

- non-solipsism；
- one world；
- non-fragmentation；
- ordinary first-person phenomenology for all subjects。

代价是：不同主体在 metaphysical first-person status 上不平权。

这正是本项目希望检验的 absolute-first-person hypothesis，而不是隐藏代价。

---

## 7. 关键：这没有证明“至少一个”

Coherence 只给：

\[
\le 1.
\]

它没有给：

\[
\ge 1.
\]

因此仍需一个 **Absolutization / Actualization Mechanism**：

\[
\mathsf A:
F_i^{rel}
\mapsto
F_i^{abs}.
\]

并要求：

\[
\exists!i\;\mathsf A(F_i^{rel}).
\]

当前最深问题因而可以重新写成：

\[
\boxed{
\text{What makes exactly one local first-person fact simpliciter?}
}
\]

这比模糊的 “why am I absolute?” 更适合继续结构分析。

---

## 8. 与 Anchored Nested Dominance 的关系

Nested Dominance 可以被重新解释为一个候选 **absolutization selector**，而不必独自解释 absolute liveness 的全部性质。

局部：

\[
d(D_i)=\pi_i
\]

产生 ordinary local perspective。

顶层：

\[
d(D_{comp})=\pi^*
\]

可尝试决定哪一个 local perspective 被 absolutized：

\[
\mathsf A(F_{\pi^*}^{rel})=F_{\pi^*}^{abs}.
\]

然后 uniqueness 的一部分来自 coherence：

\[
F_i^{abs}\perp F_j^{abs}.
\]

这样 dominance 不再承担“为什么多个 absolute facts 不能共存”的全部负担。

---

## 9. 与 Actuality-as-Instantiation 的关系

Soames 类比提供另一个 absolutization template：

\[
Actual(w)\iff Inst(U,w).
\]

对应到 Two-Tier model，可以探索：

\[
Absolute(F_i)
\iff
Inst_G(U,A_i),
\]

其中 \(A_i\) 是与 local perspective \(i\) 对应的 global centered state。

如果这些 global centered states mutually incompatible，则：

\[
\text{one global bearer}
+
\text{maximal state incompatibility}
\Rightarrow
\le1\text{ absolutized perspective}.
\]

这使 Soames 的 instantiation route 与 coherence route 可以结合。

---

## 10. 最大压力：是不是把其他人的 first-personality 降格了

Strong pluralist 会反驳：

如果 Alice 的 first-person fact 只 “relative to Alice” 成立，而我的 first-person fact 却 simpliciter 成立，那么理论只是直接把目标不对称写进 ontology。

这项批评成立到什么程度，取决于：

\[
\mathsf A
\]

能否获得独立解释。

若不能，本模型只是 absolute first-person hypothesis 的清晰表示。

若能由更深结构推出：

\[
D\Rightarrow\mathsf A,
\]

则它会成为真正 explanatory theory。

所以本模型当前的价值是**分解问题**，没有完成最终解释。

---

## 11. 当前成功条件

Two-Tier First-Person Realism 要变成完整理论，需要：

1. 给 ordinary local FP 一个独立完整解释；
2. 证明 absolute centered facts 对不同 centers 真正 mutually incompatible；
3. 保持 one coherent world；
4. 给出非循环的 \(\mathsf A\)；
5. 解释为什么 \(\mathsf A\) 与 LIVE / actuality simpliciter 等价或相关；
6. 解释 \(\mathsf A\) 的时间变化，得到 I–NOW dynamics；
7. 保持其他 minds genuine consciousness；
8. 通过 relativity / covariance / duplication tests。

## 12. 当前评价

这是目前最直接忠实于项目原始直觉的模型：

\[
\boxed{
\text{many real ordinary first-persons}
+
\text{one absolute first-person fact}
}
\]

它最重要的新贡献是把 global uniqueness 拆成：

### At-most-one

由 unrelativized centered facts 的 incompatibility + coherence 支持。

### At-least-one / which-one

由尚未找到的 absolutization mechanism \(\mathsf A\) 负责。

这使下一阶段不必再同时解决所有 cardinality 问题，而可以死盯：

\[
\boxed{D\Rightarrow\mathsf A}
\]

## 文献入口

- Kit Fine, “Tense and Reality” (2005), especially §12 on first-personalism；
- Christian List, “A quadrilemma for theories of consciousness” (2025)；
- Martin Lipman, fragmentalist / standpoint work；
- Olla Solomyak, perspectival pluralism；
- Nikk Effingham, “Now, Again and Again” (2026).
