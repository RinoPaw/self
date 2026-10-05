# Neutral Accommodation Test

> 状态：2026-10-05 theory-discrimination refinement。
>
> 目标：修正旧 CC1 witness criterion。`NeutralActuality \not\models X` 只表示中性理论不推出 `X`；它不表示中性理论不能低成本容纳或解释 `X`。

## 0. 旧标准的问题

此前 CC1 常写成：

\[
Independent(X)
\land
N\not\models X
\land
C\models X.
\]

这对于寻找 logical residual 有用，但作为 theory-discriminating evidence 太弱。

因为：

\[
\boxed{N\not\models X\not\Rightarrow N\models\neg X.}
\]

也不推出：

\[
\boxed{N\text{ cannot explain or accommodate }X.}
\]

一个理论完全可能没有把 `X` 写成 theorem，却能用一个自然、低成本、仍保持自身核心 ontology 的扩展解释 `X`。

---

## 1. Neutral Accommodation

设 Neutral theory 为 `N`，候选事实为 `X`。

定义一个 extension：

\[
N^+=N+\Delta_N.
\]

若 `\Delta_N` 满足：

1. `N+\Delta_N` 可以实现 / 解释 / 预测 `X`；
2. `N+\Delta_N` 仍不含 irreducible global first-person arity；
3. `\Delta_N` 有独立动机，或至少不是只为救 `X` 临时添加；
4. `\Delta_N` 的理论成本不明显高于 centered theory 为解释 `X` 所承担的 distinctive commitment；
5. `\Delta_N` 没有把 `G / AbsoluteI / global opening` 换名后偷偷加回去；

则称：

\[
\boxed{CheapNeutralAccommodation(N,X).}
\]

这里的 `cheap` 不是只数 primitive 数量，而比较：

- ideological content；
- structural complexity；
- independent motivation；
- modal commitments；
- law / selector arbitrariness；
- explanatory integration。

---

## 2. 新的 CC1+

真正能给 Centered Actuality 提供 abductive pressure 的 `X` 至少应满足：

\[
\boxed{
Independent(X)
\land
NaturalFit(C,X)
\land
\neg CheapNeutralAccommodation(N,X).
}
\]

若还能够证明：

\[
N+X\Rightarrow CenteredEquivalentStructure,
\]

则得到更强结果：

### Accommodation-Collapse

Neutral side 想保留 `X`，必须加入一个与 centered actuality 在关键结构上等价的东西。

这时 `X` 才真正逼迫 theory space 向 centered horn 收缩。

---

## 3. 四种区分强度

### D0 — Entailment gap only

\[
C\models X,
\qquad N\not\models X.
\]

但 Neutral 可廉价扩展。

结论：几乎没有 discriminating force。

### D1 — Cost asymmetry

Neutral 可以容纳 `X`，但需要明显更 ad hoc / 更复杂的 extension。

结论：Centered 获得 abductive advantage，不是逻辑证明。

### D2 — Neutral instability

Neutral 若容纳 `X`，会破坏它自己的核心动机，例如必须加入 privilege-sensitive selector、global subject arity 或相当昂贵的 assignment structure。

结论：Centered 获得强 explanatory pressure。

### D3 — Accommodation collapse / impossibility

\[
N+X\vdash\bot
\]

或：

\[
N+X\equiv C\text{-like centered structure}
\]

结论：真正 decisive / near-decisive discriminator。

---

## 4. 为什么这比旧 criterion 更公平

Centered theory 不应因为把 `X` 写进自己的基本结构就自动获得解释优势。

同样，Neutral theory 也不能只靠说“我可以再加一条 law”就宣布吸收成功。

双方都要过同一问题：

> 为了得到 `X`，你额外支付了什么？这个增加是否 independently motivated？它是否只是把对方理论换名？

因此真正比较对象是：

\[
\boxed{
BestCenteredExplanation(X)
\quad vs\quad
BestStillNeutralExplanation(X).
}
\]

而不是 bare entailment matrix。

---

## 5. 对旧 witness families 的快速重审

### Ordinary phenomenology / mineness

Neutral 可给每个 subject local first-person organization、for-me-ness、zero-point、de se。

\[
CheapNeutralAccommodation=Yes.
\]

不区分。

### Presence / temporal immediacy

relational presence、B-compatible phenomenology、stage/perdurantist availability 等仍可保留核心 data。

\[
CheapNeutralAccommodation\approx Yes.
\]

Presence route 继续关闭。

### Bare actuality / facticity

instantiation、brute obtaining、fundamental uncentered actuality、absolute-but-non-FP actuality 都可承担。

\[
CheapNeutralAccommodation=Yes.
\]

不区分。

### One-world unity

one actual totality 与 many local centers 本来就是 Neutral strongest package 的内容。

\[
CheapNeutralAccommodation=Yes.
\]

不区分。

### Objective NOW

即使独立得到 privileged time，Neutral 仍可接受 impersonal A-theory / presentness without unique I。

除非 I–NOW coupling 本身有独立理由，否则：

\[
CheapNeutralAccommodation=Yes/Moderate.
\]

### Causal / dynamical privilege

若 absolute center 有独特 causal signature，Neutral 可以尝试添加一条 subject-sensitive law。

这里不能立刻判 fail；关键变成：

- 这条 law 是否 independently motivated；
- 是否仍 genuinely neutral；
- 是否只是 `L_\Omega` 的改名；
- 是否产生同等 selector / assignment mystery。

所以这是 accommodation-cost 问题，而非 entailment 问题。

### Privilege-sensitive evidence

若找到 evidence `e*`：

\[
P(e^*\mid C)\neq P(e^*\mid N)
\]

且任何 Neutral reproduction 都需 centered-equivalent structure，那么这是高价值 D2/D3 候选。

当前没有 survivor。

---

## 6. Accommodation must remain neutral

最重要的边界：Neutral 不能通过下面方式“吸收”一切：

\[
N+\text{unique global first-person actuality fact}.
\]

这已经退出 Neutral theory class。

所以每个 accommodation 都必须通过：

### Neutrality Preservation Test

\[
\boxed{
N+\Delta_N\models \neg RequiredGlobalFPArity
}
\]

或至少没有把 global first-person arity作为 primitive / constitutive structure。

如果 `\Delta_N` 事实上引入：

- unique global subject slot；
- absolute first-person obtaining；
- one privileged lived locus simpliciter；
- equivalent role-coincidence primitive；

那么它属于 theory migration，不是 neutral accommodation。

---

## 7. Explanation vs mere compatibility

还要区分：

\[
Compatible(N,X)
\]

与：

\[
Explain(N,X).
\]

Neutral side不能只说“我允许 X 恰好发生”。若 centered theory 从其核心结构自然预期 `X`，而 Neutral 只能加 brute exception，那么仍然存在 explanatory asymmetry。

因此对每个 candidate `X` 记录：

1. entailment；
2. compatibility；
3. natural explanation；
4. extension cost；
5. neutrality preservation；
6. predictive/evidential consequences。

---

## 8. 新的 completion-witness ladder

以后一个候选 `X` 依次过：

### W1 — Independent specification

不用 contested absolute vocabulary 能说明 `X` 是什么。

### W2 — Shared recognition

Neutral 与 Centered 都承认 `X` 是需要解释的数据 /事实，而不是只有一方承认的 theory-internal explanandum。

### W3 — Centered natural fit

Centered structure确实自然解释 `X`，而非另加独立 stipulation。

### W4 — Neutral accommodation test

搜索 strongest still-neutral extension。

### W5 — Cost comparison

若 Neutral 也能解释，比较新增成本。

### W6 — Collapse test

Neutral 的最佳解释是否已经等价于 centered structure？

只有通过 W1–W4，`X` 才值得称 completion discriminator；W5/W6 决定其强度。

---

## 9. 对 Completion Underdetermination 的影响

旧 underdetermination result 仍保留，但 U3 应增强。

旧 U3：

\[
\neg\exists X[Independent(X)\land C\models X\land N\not\models X].
\]

新 U3+：

\[
\boxed{
\neg\exists X[
Independent(X)
\land NaturalFit(C,X)
\land \neg CheapNeutralAccommodation(N,X)
].
}
\]

当前已审 candidate families 大多甚至在 W4 就被 Neutral 吸收，因此现有 underdetermination 至少没有被削弱，反而得到了更公平的表述。

但这个新标准也为真正突破留下空间：只要找到一个 D2/D3 级 `X`，理论比较就会实际移动。

---

## 10. 当前 verdict

\[
\boxed{
N\not\models X\text{ is not enough.}
}
\]

真正需要的是：

\[
\boxed{
Centered\ explains\ X\ naturally,
\quad Neutral\ cannot\ explain\ X\ cheaply\ while\ remaining\ neutral.
}
\]

因此今后不再把 bare entailment gap 计作 centered evidence。

## 关联

- [`centered-completion-witness-exhaustion.md`](centered-completion-witness-exhaustion.md)
- [`primitive-actuality-replacement-test.md`](primitive-actuality-replacement-test.md)
- [`completion-underdetermination-result.md`](completion-underdetermination-result.md)
- [`actuality-arity-orthogonality.md`](actuality-arity-orthogonality.md)
- [`../models/neutral-actuality-core.md`](../models/neutral-actuality-core.md)
- [`../models/role-first-absolute-opening.md`](../models/role-first-absolute-opening.md)
