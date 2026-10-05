# First-Person Non-Compossibility Audit

> 状态：2026-10-05 uniqueness-premise re-audit。
>
> 目标：检查 `First-Person Non-Compossibility`（FPNC）究竟是独立理由、List-style first-person fact semantics 的条件后果，还是已经把 singularity 写进了定义。

## 0. 为什么重新打开

此前 Unitary Singularity Lemma（USL）写成：

\[
CenteredExistence+OneWorld+NonFragmentation+FPNC
\Rightarrow ExactlyOneOpening.
\]

形式推导本身没有问题。真正需要审计的是：

\[
\boxed{FPNC\text{ 凭什么成立？}}
\]

如果 FPNC 已经等价于“不同 irreducible centers 不能共同 obtain”，那么 USL 的 uniqueness 工作主要由这个前提完成，而不能笼统归功于 `OneWorld + NonFragmentation`。

---

## 1. List 真正给出的结构

Christian List 的 quadrilemma 讨论 genuine first-person facts。对不同 conscious subjects，其 complete first-person standpoints 可能给出：

\[
I\text{ am in }X,
\qquad
I\text{ am in }Y,
\]

其中 `X` 与 `Y` 是 mutually exclusive complete token states。

List 的关键 compossibility idea 可以抽成：

### LFPC — List First-Person Compossibility

\[
\boxed{
Compossible_{FP}(F,G)
\Rightarrow
\exists p\;[ObtainsFrom(F,p)\land ObtainsFrom(G,p)].
}
\]

也就是：两个 genuine first-person facts 若要 qua first-person facts 共同成立，必须能从同一个 perspective 共同 obtain。

若 `F_X` 与 `F_Y` 分别要求同一 perspective 处于 mutually exclusive complete states，就得到：

\[
\neg Compossible_{FP}(F_X,F_Y).
\]

这是 List 论证的真实力量。

---

## 2. 从 List 到项目 FPNC 多了一步

项目需要的是更一般的命题：

\[
\boxed{
DistinctIrreducibleCenters
\Rightarrow
NonCompossibility.
}
\]

但这并不单纯由“有两个 irreducible centers”推出。

需要额外接受：

1. 每个 candidate opening 都应按 List 意义理解为 genuine first-person fact；
2. 它们的共同成立必须以 **single-perspective co-obtaining** 为 compossibility 标准；
3. 不允许一个 complete reality 基本地包含多个 perspective-indexed / perspective-constituted modes of obtaining，而这些 modes 共同构成该 reality。

第 2、3 点正是 standpoint pluralism / constitutional perspectivalism 会争论的地方。

所以更准确：

\[
\boxed{
ListSemantics+DistinctCompleteFPCenters
\Rightarrow FPNC.
}
\]

而不是无条件：

\[
IrreducibleFP+DistinctCenters\Rightarrow FPNC.
\]

---

## 3. 旧直觉解释中的 equivocation risk

旧 USL 用：

\[
I\text{ am in }X,
\qquad I\text{ am in }Y
\]

解释两个 distinct centers 的冲突。

这里存在一个需要明确的跳步：

- 起点说的是 `center_i` 与 `center_j`；
- 冲突展示却把两者放到同一个 unindexed `I` 下。

如果 `I_i` 与 `I_j` 被允许作为不同 irreducible standpoint 的 primitive obtaining modes，那么：

\[
[I_i:X],
\qquad
[I_j:Y]
\]

是否冲突，不能只靠 `X` 与 `Y` 对**同一主体** mutually exclusive 来决定。

把两者强制送入同一个 `I` / single perspective，正是 LFPC 的 substantive assumption。

因此不能把这个步骤当作无争议逻辑事实。

---

## 4. Plural-opening stress model

为了测试 FPNC，构造：

\[
R_P=\langle W,C,M,A\rangle
\]

其中：

- `W`：one objective / causal history；
- `C={c_1,c_2,\ldots}`：多个 genuine centers；
- `M={M_{c_1},M_{c_2},\ldots}`：多个 irreducible first-person modes of obtaining；
- `A`：one actuality / one total reality relation。

要求：

\[
M_{c_i}\neq M_{c_j}
\]

但不规定：

\[
\exists!c\;Absolute(c).
\]

并允许 complete reality 包含：

\[
[P_i]_{c_i},
[P_j]_{c_j}
\]

作为不同 perspective-constituted facts。

这个模型与仓库已有 `Obtaining-Mode Pluralization Challenge`、Lipman-style standpoint pluralism、Whitehead-style plural subject-bearing actuality 同构。

它的意义不是已经证明 pluralism 正确，而是暴露：

\[
\boxed{OneReality+PluralIrreduciblePerspectiveModes}
\]

至少需要被独立排除，不能只靠把 `NonFragmentation` 定义成 List-style single-perspective compossibility 后宣布失败。

---

## 5. “这只是 fragmentation”不足以完成审计

List 可以把上述 plural standpoint package 分类为 fragmentation，因为其 NF 要求 world 中 obtaining facts 全部 compossible，而 genuine first-person facts跨主体不满足 single-perspective compossibility。

这保持了 List quadrilemma 的有效性。

但对本项目而言，问题变成：

> 为什么 complete actuality 的 unity 必须采用这种 compossibility 标准？

也就是：

\[
\boxed{
OneWorld
\not\Rightarrow
ListStyleNonFragmentation
}
\]

除非另有 argument。

因此“plural openings 必须 fragment”目前是一项 metaphysical classification / constraint，而不是从 minimal one-world commitment 免费得到的 theorem。

---

## 6. FPNC 与 uniqueness 的关系

设预唯一性的 opening predicate 为：

\[
Open(c)
\]

它只表示 `c` 是 irreducible first-person opening，不包含 `unique`。

若独立接受：

\[
FPNC:\quad c_i\neq c_j\land Open(c_i)\land Open(c_j)
\Rightarrow \neg Compossible(c_i,c_j),
\]

再接受：

\[
NF:\quad \text{all obtaining facts in one actuality are compossible},
\]

那么：

\[
NF+FPNC\Rightarrow AtMostOneOpening.
\]

这是有效的。

但其 explanatory decomposition 应写成：

\[
\boxed{
FPNC\text{ supplies the anti-plurality content; }NF\text{ converts it into a one-totality exclusion.}
}
\]

不能把 `NF` 单独描述成 at-most-one principle。

---

## 7. Role-First model 的额外循环风险

当前 `role-first-absolute-opening.md` 本身规定：

\[
\exists!L_i\;Occupies(L_i,G)
\]

并明确：

\[
|Occupants(G)|=1.
\]

因此在这个 strongest centered model 内，exact-one 已经是 primitive architecture 的一部分。

若随后再用 USL 说“exact-one 被 derivation 消除了”，会发生 bookkeeping confusion：

- 要么先构造一个**不含 uniqueness** 的 weaker centered/opening theory，再由 FPNC + NF 推出 uniqueness；
- 要么保留 Role-First exact-one primitive，并承认 USL 只显示该 primitive 与 List-style unitary package 相容/可被另一组前提重建。

当前不能同时把 exact-one 写进 `G` 的 essence，又把它计成 USL 的独立推导收益。

---

## 8. 与早期 singularity-gap 结果的 reconciliation

仓库已有：

\[
Unity\not\Rightarrow SingularityOfSubject
\]

以及：

\[
ConstitutionalPerspectivality
+NoIndependentGlobalAsymmetry
\not\Rightarrow
\exists!c\;Absolute(c).
\]

这些结果没有被 USL 真正推翻。

USL 新增的是条件：

\[
FPNC/LFPC.
\]

所以最公平的统一读法是：

\[
\boxed{
Unity\ alone\ does\ not\ yield\ singularity;
\quad Unity+FPNC\ does.
}
\]

现在真正 burden 是 FPNC，而不是 singularity 已经无条件解决。

---

## 9. 当前 verdict

### 保留

USL 的形式条件式仍有效：

\[
\boxed{
AtLeastOneOpening+OW+NF+FPNC
\Rightarrow ExactlyOneOpening.
}
\]

### 降级

不能再写：

\[
\boxed{Singularity\text{ is conditionally solved by unitary reality alone}.}
\]

更准确：

\[
\boxed{
Singularity\text{ is reduced to the independent status of FPNC/LFPC plus the chosen unity criterion}.}
\]

### 重新开放的问题

需要证明至少一个：

1. LFPC 是 genuine first-person fact 的独立 constitutive truth，而非定义性 stipulation；
2. plural irreducible perspective modes 不能属于一个 nonfragmented complete actuality；
3. any coherent plural-opening model secretly collapses into relative/meta facts；
4. `OneWorld` 本身独立要求 List-style compossibility，而不是更宽的 plural-perspective unity。

在此之前，`ExactlyOne` 的正面分量必须降级。

## 关联

- [`unitary-singularity-lemma.md`](unitary-singularity-lemma.md)
- [`actuality-arity-singularity-gap.md`](actuality-arity-singularity-gap.md)
- [`obtaining-mode-pluralization.md`](obtaining-mode-pluralization.md)
- [`standpoint-pluralism-challenge.md`](standpoint-pluralism-challenge.md)
- [`../models/role-first-absolute-opening.md`](../models/role-first-absolute-opening.md)
- [`../../literature/list-2025-quadrilemma-unitary-opening.md`](../../literature/list-2025-quadrilemma-unitary-opening.md)
