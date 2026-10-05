# Stochastic-Grounded Opening Path

> 状态：2026-10-05 Stage-First Opening persistence upgrade。
>
> 目标：利用 Bader stochastic grounding 与 Moorfoot indeterministic building，把 `Opening Successor` 从一个完全 primitive stochastic pointer 改造成可由 lower/base facts **概率性 building/ground** 的 derivative continuation fact。

## 0. Starting problem

Stage-First Opening：

\[
Open(\sigma_t).
\]

在普通 non-branching case，future stage candidate可能近似唯一。

但 fission：

\[
\sigma_t\to\sigma_L+\sigma_R.
\]

并可有 exact symmetry：

\[
Profile(\sigma_L)=Profile(\sigma_R).
\]

项目要求 absolute opening继续成 exactly-one path：

\[
\boxed{Open(\sigma_L)\oplus Open(\sigma_R).}
\]

传统 deterministic structural selector无法在 exact symmetry 下 canonically选择。

---

## 1. Primitive-chance solution

此前 SFNOM 可直接写：

\[
P_O(\sigma_L\mid\sigma_t,R)
=
P_O(\sigma_R\mid\sigma_t,R)=1/2.
\]

然后 realization：

\[
\sigma^*\sim P_O.
\]

这 coherent-looking，但留下：

\[
\boxed{\text{what grounds the probability distribution?}}
\]

若 `P_O` 完全 primitive，就可能只是把 branch selector换成 random branch selector。

---

## 2. Bader upgrade

Bader允许 lower-level facts只 **stochastically ground** derivative fact。

令：

\[
G_t=\text{all relevant physical/psychological/causal facts around }\sigma_t.
\]

candidate transitions：

\[
T_i=Succ_O(\sigma_t,\sigma_i).
\]

定义：

\[
\boxed{
G_t\;\overset{stoch}{\ground}\;T_i.
}
\]

其 modal force不是：

\[
\square(G_t\to T_i),
\]

而类似：

\[
\square(G_t\to P(T_i)>0).
\]

exact outcome：

\[
T_L\;|\;T_R
\]

可保持 determinate，但哪一个被 build 出来由 objective chance 决定。

---

## 3. Admissibility before probability

这给一个重要分层。

### A — candidate/admissibility structure

base facts先决定：

\[
C^+(\sigma_t)=\{\sigma_i:\text{eligible continuation stage}\}.
\]

若：

\[
\sigma_j\notin C^+(\sigma_t),
\]

则：

\[
P(T_j)=0.
\]

### B — relative grounding strengths / symmetries

对于 eligible candidates：

\[
P(T_i)\propto Strength(G_t,\sigma_i).
\]

exact duplicates：

\[
Strength_L=Strength_R
\Rightarrow
P(T_L)=P(T_R).
\]

### C — exact realization

\[
\boxed{\exists!i\;T_i.}
\]

这使 explanation不再完全从零开始。

---

## 4. What is explained

stochastic-grounding model可以解释：

1. 为什么 successor来自某些 stages，而非任意未来意识；
2. 为什么某些 transitions probability 0；
3. 为什么 near-continuous candidate可能概率更高；
4. 为什么 exact symmetry给 equal chance；
5. 为什么 actual outcome exactly one而 base又不含 deterministic winner asymmetry（若 one-outcome building law成立）。

它不能解释：

\[
\boxed{\text{why exact admissible winner }\sigma_L\text{ rather than }\sigma_R.}
\]

这里 chance 是合法 explanatory stopping point。

---

## 5. Non-fundamental bruteness is useful here

若 actual outcome：

\[
Succ_O(\sigma_t,\sigma_L),
\]

它可以同时：

- not be necessitated by \(G_t\)；
- be brute in exact-outcome respect；
- yet be grounded / derivative。

所以：

\[
\boxed{
OutcomeBruteness
\not\Rightarrow
OutcomeFundamentality.
}
\]

这显著改善 NOM 的 ontology accounting。

我们不需要把每一时刻的：

\[
\boxed{\text{“absolute path chose left”}}
\]

都当作新的 fundamental fact。

---

## 6. Strongest formulation: SG-SFNOM

定义：

### Fundamental / base package

\[
R+\Lambda_O+\Lambda_G
\]

其中：

- \(R\)：physical/phenomenal world structure；
- \(\Lambda_O\)：Opening semantics / exact-one stage role；
- \(\Lambda_G\)：stochastic building/grounding architecture。

### Current opening

\[
Open(\sigma_t).
\]

### Continuation grounds

\[
G_t(R,\sigma_t).
\]

### Stochastic grounding

\[
G_t\overset{stoch}{\ground}Succ_O(\sigma_t,\sigma_{t+1}).
\]

### Path

\[
\boxed{
\Pi_O
=
\langle\sigma_0,\sigma_1,\ldots\rangle
}
\]

由 stochastic-grounded successor facts逐步形成。

暂称：

\[
\boxed{\text{SG-SFNOM}.}
\]

---

## 7. Relation to spontaneous symmetry breaking

此前 SAOB：

\[
SymmetricBase
+
Law
\to
AsymmetricRootedCompletion.
\]

Bader-style path version：

\[
SymmetricSuccessorBase
+
StochasticGrounding
\to
AsymmetricContinuationFact.
\]

两者结构一致，但 grounding framework提供更明确的 metaphysical dependence：

\[
\boxed{\text{the asymmetric outcome can still be built by symmetric lower-level facts}.}
\]

这避免：

> “既然 lower facts没决定 winner，winner必须 fundamental。”

该 inference。

---

## 8. Halvorson compatibility

Halvorson-style lesson：base automorphism不必延伸成 full completed model automorphism。

SG-SFNOM 可写：

\[
Aut(G_t)\ni\phi(\sigma_L)=\sigma_R,
\]

但 actual derivative structure满足：

\[
Succ_O(\sigma_t,\sigma_L)
\]

而非：

\[
Succ_O(\sigma_t,\sigma_R).
\]

因此：

\[
\boxed{
SymmetricGround
+
AsymmetricDerivativeFact
}
\]

原则上不要求在 ground 中预埋 token haecceity。

---

## 9. Comparison with indeterminate identity

Fine / Akiba / Ehring 等允许 fission 中 personal identity indeterminate。

那类 route：

\[
Indeterminate[A=B/A=C].
\]

SG-SFNOM target不同：

\[
\boxed{\text{base underdetermines, but actual Opening continuation is determinate}.}
\]

所以：

\[
MetaphysicalIndeterminacy
\neq
StochasticDeterminateOutcome.
\]

Moorfoot 2026 也明确强调 indeterministic building与 metaphysical vagueness不同：chance可以决定一个完全 determinate built outcome。

这与 absolute opening 的 one-path requirement 更贴合。

---

## 10. Main remaining problem: why exactly-one building?

Bader fission account本身愿意 exactly-one persistence branch。

项目仍需为 Opening说明：

\[
\boxed{
\sum_i Indicator[Succ_O(\sigma_t,\sigma_i)]=1.
}
\]

为什么 outcome space排除：

- zero successors；
- two successors；
- universal continuation；
- indeterminate continuation。

因此 stochastic grounding解决：

\[
\boxed{\text{which branch, given a one-branch ontology}}
\]

没有解决：

\[
\boxed{\text{why a one-branch ontology at all}}.
\]

这再次回到 LNP / Universal-I challenge。

---

## 11. Main remaining problem: continuity strengths

对于 real-world non-fission progression，需要定义 `contributing grounds`：

candidate variables可能包括：

- causal continuity；
- memory-chain continuity；
- neural/functional continuity；
- phenomenal similarity；
- bodily/spatiotemporal continuity；
- information preservation。

但不能 ad hoc 调 weights 以保证 current ordinary person总获胜。

必须满足：

\[
\boxed{\text{independently motivated grounding-strength rule}.}
\]

否则 stochastic grounding只把 arbitrariness从 winner搬到 probability weights。

---

## 12. Death and unconscious gaps

Stage-first path会遇到没有 conscious stage 的区间。

需要区分：

### Gap continuation

\[
\sigma_{before}\to\sigma_{after}
\]

允许 crossing a dreamless/surgical unconscious interval by ordinary causal continuity grounds。

### Termination

\[
P(C^+(\sigma)=\varnothing)=1.
\]

opening path终止。

### Jump/relocalization

\[
Succ_O(\sigma,\sigma_j)
\]

where \(\sigma_j\) belongs to a different ordinary organism。

Conitzer明确把这些作为 distinct αA possibilities。

SG-SFNOM本身不决定哪类 metaphysics正确。

---

## 13. Impact on “why this one?”

对于一个 exact fission outcome：

> 为什么 opening去了 L 而非 R？

SG-SFNOM 可以回答：

> 两边都有由共同 structure产生的 objective continuation chance；stochastic grounding实际 build 了 L-continuation。

所以 contrastive why-chain可以合法止于 chance。

但对于最初：

> 为什么存在一个 selective opening path，而不是所有 experiences都属于 Universal-I？

Bader不给答案。

因此当前 burden hierarchy变成：

\[
\boxed{
LNP
\to
InitialOpening
\to
PSP
\to
StochasticGrounding.
}
\]

最后一箭头现在有成熟 mechanism；第一箭头仍最难。

---

## 14. Verdict

Stage-First Opening 的 trajectory side 获得真实升级：

旧：

\[
\boxed{PSP\text{ has only an invented stochastic selector}.}
\]

新：

\[
\boxed{PSP\text{ has a literature-backed stochastic-building solution schema}.}
\]

而且它提供一个此前很重要的 metaphysical lesson：

\[
\boxed{
ExactOutcomeCanBeDerivative
\land
NotDeterministicallyGrounded.
}
\]

所以 project当前最强 selective architecture可写成：

\[
\boxed{
NomologicalStageOpening
+
StochasticallyGroundedPath.
}
\]

其最深剩余问题已经进一步集中为：

\[
\boxed{\text{Why selective first-person localization at all?}}
\]

## Sources / links

- [`../../literature/bader-moorfoot-indeterministic-building.md`](../../literature/bader-moorfoot-indeterministic-building.md)
- [`../models/stage-first-opening.md`](../models/stage-first-opening.md)
- [`presence-localization-universalism-fork.md`](presence-localization-universalism-fork.md)
- [`stochastic-absolute-orientation-law.md`](stochastic-absolute-orientation-law.md)
