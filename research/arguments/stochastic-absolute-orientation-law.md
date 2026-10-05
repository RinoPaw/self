# Stochastic Absolute-Orientation Law

> 状态：2026-10-05 Privilege-Sensitive-Law audit。
>
> 目标：检验一种此前没有认真建模的 PLP：不要求 global structure deterministicly 选出 canonical local winner，而允许一条 fundamental psychophysical chance law 在 genuine local subjects 之间实现 exactly-one absolute orientation。

## 0. Motivation

此前 derived PLP 主要假定：

\[
Structure(R)\Rightarrow\exists!E^*\;Distinguished(E^*).
\]

perfect duplication / automorphism 会阻止这种 deterministic canonical selector。

但这只排除：

\[
\boxed{\text{deterministic structural selection}.}
\]

它没有排除 fundamental stochastic laws。

Albert–Loewer single-mind interpretation、GRW-style stochastic dynamics 与 objective-chance literature 都提供一般方法论先例：一个完整 pre-outcome state 可以 lawfully admit several future/mental outcomes，而实际 world realizes exactly one。

因此定义 **Stochastic Absolute-Orientation Law (SAOL)**。

---

## 1. Basic model

令 complete non-absolute base 为：

\[
R.
\]

其 genuine local conscious loci：

\[
S(R)=\{E_1,\ldots,E_N\}.
\]

引入 fundamental law：

\[
\Lambda_\Omega.
\]

该 law 给 objective chance distribution：

\[
\boxed{
P_\Omega(E_i\mid R)
=\frac{w(E_i;R)}{\sum_jw(E_j;R)}.
}
\]

并规定一次 realization：

\[
E^*\sim P_\Omega(\cdot\mid R),
\]

满足：

\[
\boxed{
AbsoluteOrientation(E^*).
}
\]

且：

\[
\forall E_j\neq E^*,\quad\neg AbsoluteOrientation(E_j).
\]

所以 law 直接保证：

\[
\boxed{\exists!E^*\;AbsoluteOrientation(E^*).}
\]

---

## 2. Why this is genuinely new relative to Kadić-style dominance

Kadić-style route：

\[
Structure\to DominantRole\to ?\to AbsolutePrivilege.
\]

它面对两个问题：

1. symmetry may prevent unique structural winner；
2. dominance semantics不是 privilege semantics。

SAOL直接把 target predicate放入 law-output：

\[
\Lambda_\Omega:\quad R\to AbsoluteOrientation(E_i).
\]

所以它不需要：

\[
Dominance\Rightarrow Privilege.
\]

换言之，它放弃 derived-DPB ambition，改成 **nomological privilege semantics**。

这并非简单等于 static selector，因为 law 还给：

- cross-world generality；
- objective chances；
- counterfactual structure；
- possible symmetry-respecting probability assignments。

---

## 3. Symmetry advantage

若：

\[
Aut(R)
\]

把 `E_i,E_j` 交换，而且 `w` 只依赖 invariant facts，则 covariance 要求：

\[
w(E_i;R)=w(E_j;R).
\]

所以 perfect duplicates 获得 equal chance：

\[
P_\Omega(E_i\mid R)=P_\Omega(E_j\mid R).
\]

但 actual realization仍可以：

\[
Absolute(E_i)\land\neg Absolute(E_j).
\]

因此：

\[
\boxed{
ExactSymmetry
\not\Rightarrow
NoUniqueStochasticOutcome.
}
\]

这与 radioactive decay / GRW-style chance 的一般 explanatory pattern 类似：pre-outcome structure 不需要 contain an asymmetry that predetermines the unique outcome。

### 重要收窄

这只说明 symmetry 不排除 stochastic unique outcome。

它没有说明：

\[
\boxed{\text{why the stochastic outcome should have first-person privilege semantics}.}
\]

那是 law-content本身承担的工作。

---

## 4. Law-quality constraints

为了避免 `SAOL = random selector` 的空洞化，至少要求：

### L1 — Generality

同一 law 必须跨 possible realizations / worlds应用，而不是只写：

\[
Absolute(E_{Rino}).
\]

### L2 — Permutation covariance

若 candidates在 base结构中对称，则 chance assignment也必须对称：

\[
E_i\cong_RE_j\Rightarrow P_\Omega(E_i|R)=P_\Omega(E_j|R).
\]

### L3 — Natural weighting

若 weights不相等，`w` 必须来自 independently motivated property，而非把 current winner编码进函数。

### L4 — Exactly-one normalization

law 必须解释为何 realization 类型是 exactly-one，而非 zero / many：

\[
\sum_iP_\Omega(E_i|R)=1,
\]

且 outcome ontology只允许一个 marked locus。

### L5 — Privilege semantics

law-output 必须 genuinely 是：

\[
AbsoluteOrientation(E_i),
\]

而不是：

\[
Dominant(E_i),\quad Central(E_i),\quad Richest(E_i).
\]

否则 DPB 没有消失。

### L6 — Non-epistemic status

`P_Ω` 必须是 objective chance / nomological propensity，而不是 xerographic credence、typicality assumption 或 ordinary self-locating probability。

---

## 5. Epistemic distribution is not enough

Srednicki–Hartle：

\[
(T,\xi)
\]

中的 `ξ` 给 first-person predictive distribution。

Sebens–Carroll / Everettian self-location也给 branch-relative credences。

Alastair Wilson的 Indexicalism甚至把 objective chance解释为 essentially self-locating phenomenon。

但这些 routes通常保留所有 candidate centers/worlds；probability表示 uncertainty / branch measure，而非：

\[
OneCenterBecomesMetaphysicallyAbsolute.
\]

所以：

\[
\boxed{
SelfLocatingProbability
\not\Rightarrow
StochasticAbsoluteSelection.
}
\]

SAOL必须明确采用 ontic chance reading。

---

## 6. Anti-Haecceitist Fork

这是 SAOL 的最大新问题。

设 `E_A,E_B` 是 perfect duplicates，base `R` 有 automorphism：

\[
\phi(E_A)=E_B.
\]

SAOL 想说：

\[
P(Absolute(E_A))=P(Absolute(E_B))=1/2.
\]

但两种 completed outcomes：

\[
\Omega_A=(R,Absolute(E_A))
\]

与：

\[
\Omega_B=(R,Absolute(E_B))
\]

在交换 A/B 后 isomorphic。

### Horn H1 — Token-level outcomes are genuinely distinct

则 chance可以真正分布在：

\[
\Omega_A\neq\Omega_B.
\]

但 distinction只来自哪个 numerical token 获得 role。

这接近：

\[
\boxed{\text{haecceitistic / D-haecceitistic chance}.}
\]

代价：项目此前 role-first anti-haecceitism 的优势被部分放弃。

### Horn H2 — Quotient exact automorphic outcomes

若：

\[
\Omega_A\sim\Omega_B,
\]

它们只是一个 structural centered outcome type：

\[
\exists!E^*\;Absolute(E^*).
\]

则 objective law可以保证“there is one center”，但不能在 unlabelled outcome space里再说：

\[
P(E^*=A)=1/2.
\]

因为 A/B pre-label 已被 quotient。

于是 original coincidence question仍可重现为：

\[
\boxed{L_{self}=E^*\ ?}
\]

这就是 **Stochastic-Selector / Anti-Haecceitist Fork**。

---

## 7. Does objective chance answer “why this one?”

如果接受 H1 / token-level objective chance，那么 contrastive question：

> 为什么 E_A 是 absolute 而 E_B 不是？

可以得到 stochastic explanation：

> law `ΛΩ` 给 A/B 相应 objective chances；actual outcome is A。

这种 explanation 与 fundamental radioactive-decay outcome同型：law解释 outcome-space与 chance，不再要求一个 further deterministic reason说明为什么 exactly this token realized。

所以：

\[
\boxed{\text{fundamental chance can terminate the contrastive why-chain}.}
\]

但这是一个 substantive metaphysical stopping rule。

若用户的 target要求：

\[
\text{a sufficient reason why this exact subject rather than its duplicate},
\]

SAOL不会满足；它明确回答：there is no deeper sufficient reason。

---

## 8. Subject Harmony → Absolute-Subject Harmony

Schmid/Cutter 文献允许 psychophysical principles决定 subject pairing / number / persistence。

这启发一个更强 law schema：

### Ordinary subject harmony

\[
PhysicalStructure
\xrightarrow{L_S}
SubjectBearers.
\]

### Absolute-subject harmony

\[
SubjectStructure(R)
\xrightarrow{\Lambda_\Omega}
AbsoluteBearer(E^*).
\]

如果 absolute orientation theory还加入 winner-specific factive access：

\[
Absolute(E^*)\Rightarrow AcquaintedWithAbsoluteStatus(E^*),
\]

则可形成：

\[
\boxed{\text{ontic–epistemic absolute harmony}.}
\]

这可以与 Bricker-style：

\[
SameEvidence\not\Rightarrow SameEpistemicStatus
\]

结合。

但它目前只改善 theory architecture；没有独立 evidence证明实际存在这种 harmony。

---

## 9. Bitbol synthesis: correct semantics, missing law

Bitbol 提供：

\[
OneMind+AvailablePOVs\to Identification(M,E^*),
\]

且 adopted POV 从内部就是 `my point of view`。

可把 SAOL 重述为给 Bitbol identification 加 dynamics：

\[
\boxed{
P(Identification(M,E_i)\mid R)
= P_\Omega(E_i\mid R).
}
\]

这形成当前最接近 target 的 hybrid：

- Bitbol supplies privilege semantics；
- single-mind / objective-chance literature supplies stochastic selection form；
- subject-harmony literature supplies legitimacy of subject-sensitive psychophysical laws。

暂称：

\[
\boxed{\text{Stochastic Identification Model (SIM)}.}
\]

但 Bitbol自己明确不把 identification当普通 physical process；SIM 是本项目的新 construction，不应反写成 Bitbol的原主张。

---

## 10. Comparison with Role-First Ω

### Role-First Ω

\[
\Omega[R;E^*]
\]

直接把 center/orientation作为 complete actuality 的 constitutive aspect。

### SAOL

\[
R+\Lambda_\Omega+ChanceOutcome(E^*)
\Rightarrow
\Omega[R;E^*].
\]

SAOL 的 potential advantage：

- explains exact-one as law-governed outcome form；
- supplies modal/chance/counterfactual structure；
- exact symmetry不再需要 deterministic structural breaker；
- can integrate with psychophysical-law framework。

SAOL 的 costs：

- adds law + objective chance ontology；
- privilege semantics仍 fundamental in the law；
- perfect-duplicate case faces haecceitistic fork；
- if absolute status has no empirical/epistemic consequences, law risks explanatory idleness。

所以：

\[
\boxed{
SAOL\text{ is more structured than primitive }\Omega,
\text{ but not yet better supported}.}
\]

---

## 11. Current verdict

本轮首次找到一个 serious **Privilege-Sensitive Law architecture**：

\[
\boxed{
R
\xrightarrow{\Lambda_\Omega\;\text{(objective chance)}}
\exists!E^*\;AbsoluteOrientation(E^*).
}
\]

它确实绕过 deterministic canonical-selection obstruction。

但它没有免费关闭两个终极问题：

### V1 — privilege-content primitiveness

为什么 law 的 outcome predicate 是 `AbsoluteOrientation`，而不是普通 subjecthood / dominance？

### V2 — anti-haecceitist stochasticity

perfect duplicates 下，token-indexed chances需要 haecceitistic structure；quotient outcomes又让 `why my token?` 回来。

因此最准确：

\[
\boxed{
\text{Derived PLP near-closure is reopened only by a nomological/stochastic route}.}
\]

这条 reopening是真实的，但代价是承认 absolute orientation 可能是 **fundamental law-governed chance fact**，而非从 neutral structure完全 derive。

## 关联

- [`../../literature/psychophysical-subject-selection-laws.md`](../../literature/psychophysical-subject-selection-laws.md)
- [`dominance-privilege-bridge-audit.md`](dominance-privilege-bridge-audit.md)
- [`../models/maximal-fusion-dominant-locus.md`](../models/maximal-fusion-dominant-locus.md)
- [`../../synthesis/frontier-2026-10-05-derived-plp-near-closure.md`](../../synthesis/frontier-2026-10-05-derived-plp-near-closure.md)
