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

它没有排除 fundamental stochastic laws，甚至没有排除一种更一般的 **law-governed symmetry breaking**：complete outcome可以比 pre-outcome base拥有更少的 automorphisms，而不要求 base里预先藏着一个 token haecceity。

Albert–Loewer single-mind interpretation、GRW-style stochastic dynamics与 objective-chance literature提供一般方法论先例；Halvorson 2026 对 symmetric initial conditions / asymmetric complete models 的形式分析进一步说明，symmetry breaking本身不等于 haecceitistic difference。

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
- symmetry-respecting probability assignments；
- potentially law-governed symmetry breaking from an uncentered base to a centered completion。

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

这与 radioactive decay / GRW-style chance 的一般 explanatory pattern 类似：pre-outcome structure不需要 contain an asymmetry that predetermines the unique outcome。

Halvorson 2026 又进一步提醒：即使 complete model出现一个新的 asymmetric predicate / relation，也不能直接推出 outcome difference必须是 primitive haecceitistic difference。形式上可以存在：

\[
Aut(R)\ni\phi
\]

但：

\[
\phi\notin Aut(R+Absolute(E^*)).
\]

即某个 initial symmetry不能延伸为 completed-world symmetry。

### 重要收窄

这只说明 symmetry不排除 law-governed unique outcome。

它没有说明：

\[
\boxed{\text{why the outcome predicate should have first-person privilege semantics}.}
\]

那仍由 law-content本身承担。

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

### L7 — Symmetry-breaking coherence

在 perfect-duplicate cases 中，theory必须说明 complete centered outcome如何相对于 uncentered base减少 symmetry，而不偷渡 winner-specific initial data。

Halvorson-style model theory说明这类结构原则上 coherent；但 SAOL仍需要自己的 chance semantics。

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

## 6. Symmetry-Breaking / Anti-Haecceitist Trilemma

设 `E_A,E_B` 是 perfect duplicates，base `R` 有 automorphism：

\[
\phi(E_A)=E_B.
\]

SAOL 想说：

\[
P(Absolute(E_A))=P(Absolute(E_B))=1/2.
\]

completed structures分别可写作：

\[
\Omega_A=(R,Absolute(E_A))
\]

与：

\[
\Omega_B=(R,Absolute(E_B)).
\]

这里至少有三个 readings。

### Horn H1 — Token-level outcomes are primitively distinct

若：

\[
\Omega_A\neq\Omega_B
\]

并且差异最终只由 `which numerical token` 承担，则进入：

\[
\boxed{\text{haecceitistic / D-haecceitistic chance pressure}.}
\]

这种版本最容易说：

\[
P(E^*=A)=P(E^*=B)=1/2,
\]

但代价是部分放弃项目此前 role-first anti-haecceitism 的优势。

### Horn H2 — Quotient exact automorphic completed outcomes

若把：

\[
\Omega_A\sim\Omega_B
\]

完全 quotient 成一个 structural centered outcome type：

\[
\exists!E^*\;Absolute(E^*),
\]

law可以保证“there is exactly one center”，但 unlabeled outcome space不再自然支持：

\[
P(E^*=A)=1/2.
\]

original coincidence question可重现为：

\[
\boxed{L_{self}=E^*\ ?}
\]

### Horn H3 — Relational / rooted symmetry-breaking completion

Halvorson 2026 提供更细的 formal possibility：base `R` 中 A/B exchange是 symmetry；完整模型加入一个 asymmetric relation/predicate 后，该 symmetry不能延伸到 full model。

对本项目可写成：

\[
Aut(R)\ni\phi,
\qquad
\phi\notin Aut(\Omega[R;E^*]).
\]

此时 centered completion可以被理解为：

\[
\boxed{\text{a rooted / marked relational structure}}
\]

而无需说 A 或 B 在 uncentered base里已携带 primitive thisness。

这让 anti-haecceitism 与 unique realized center **原则上兼容得更好**。

但 H3 还有两个开放问题：

1. 若 `Ω_A` 与 `Ω_B` 作为 unlabelled structures同构，objective chance over “which actual element becomes root” 应如何严格定义？
2. law-added `Absolute` predicate 是否只是把 centeredness本身 fundamentalize，而没有进一步解释其 first-person semantics？

所以 Halvorson关闭的是：

\[
\text{symmetry breaking necessarily implies primitive haecceities}
\]

而没有关闭：

\[
\text{privilege-content / chance-semantics burden}.
\]

---

## 7. Does objective chance answer “why this one?”

在 H1 或可成功形式化的 H3 下，contrastive question：

> 为什么 E_A 是 absolute 而 E_B 不是？

可以得到 stochastic explanation：

> `ΛΩ` 给对称 candidates 相同 objective chance；actual complete world realizes an A-rooted outcome。

这种 explanation 与 fundamental radioactive-decay outcome同型：law解释 outcome-space与 chance，不再要求一个 further deterministic reason说明为什么 exactly this realization发生。

所以：

\[
\boxed{\text{fundamental chance can terminate the contrastive why-chain}.}
\]

但这是一个 substantive metaphysical stopping rule。

若 target要求：

\[
\text{a sufficient reason why this exact subject rather than its duplicate},
\]

SAOL不会满足；它明确允许 there is no deeper sufficient reason。

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

这形成当前最接近 target 的 hybrid：

- Bitbol supplies privilege semantics；
- single-mind / objective-chance literature supplies stochastic selection form；
- subject-harmony literature supplies legitimacy of subject-sensitive psychophysical laws；
- Halvorson-style symmetry analysis supplies a possible anti-haecceitist reading of asymmetric completion。

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
- can integrate with psychophysical-law framework；
- Halvorson-style H3 gives a route to centered asymmetric completion without straightforward primitive token haecceities。

SAOL 的 costs：

- adds law + objective chance ontology；
- privilege semantics仍 fundamental in the law；
- perfect-duplicate case仍需要明确 H1/H2/H3 中哪种 chance ontology；
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

Halvorson 2026 又削弱了一个此前看似致命的反对：

\[
\boxed{
SymmetricBase+AsymmetricCompletion
\not\Rightarrow
PrimitiveHaecceitism.
}
\]

因此 `Derived PLP Near-Closure` 被真实地重新打开了一条 **nomological/stochastic route**。

但它仍没有关闭两个终极问题：

### V1 — privilege-content primitiveness

为什么 law 的 outcome predicate 是 `AbsoluteOrientation`，而不是普通 subjecthood / dominance？

### V2 — chance ontology over automorphic candidates

H1/H2/H3 哪种 reading最好？尤其在 anti-haecceitist H3 下，如何定义非平凡 objective chance over isomorphic rooted outcomes / actual elements？

所以最准确的最新 verdict：

\[
\boxed{
\text{Derived structural PLP is near-closed; nomological PLP is now a live opening}.}
\]

这条 opening是真实的，但代价是承认 absolute orientation 可能是 **fundamental law-governed chance fact**，而非从 neutral structure完全 derive。

## 关联

- [`../../literature/psychophysical-subject-selection-laws.md`](../../literature/psychophysical-subject-selection-laws.md)
- [`dominance-privilege-bridge-audit.md`](dominance-privilege-bridge-audit.md)
- [`../models/maximal-fusion-dominant-locus.md`](../models/maximal-fusion-dominant-locus.md)
- [`../../synthesis/frontier-2026-10-05-derived-plp-near-closure.md`](../../synthesis/frontier-2026-10-05-derived-plp-near-closure.md)
