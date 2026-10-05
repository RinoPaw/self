# Bader / Moorfoot — Stochastic Grounding, Indeterministic Building, and Fission

> 状态：2026-10-05 focused literature note。
>
> 阅读层级：Bader 2020 publisher metadata/full abstract + indexed full-text excerpts / author manuscript excerpts；Moorfoot 2026 publisher full-text HTML read。
>
> 项目用途：给 Stage-First Opening 的 `Path Selection Problem` 提供一个几乎精确的既有形而上学先例：对称 fission 中 persistence / successor fact 可以由 stochastic grounding / indeterministic building产生。

## 1. Ralf Bader — The Fundamental and the Brute

Ralf M. Bader, “The Fundamental and the Brute”, *Philosophical Studies* 178, 1121–1142. Published online 2020-06-05; issue 2021. DOI `10.1007/s11098-020-01486-z`.

核心理论：

\[
\boxed{\text{stochastic grounding}.}
\]

通常 grounding被理解为 necessitating：

\[
G\Rightarrow X.
\]

Bader允许：

\[
\boxed{G\Rightarrow P(X)>0}
\]

而不要求：

\[
P(X)=1.
\]

因此 fundamental / lower-level facts可对 derivative outcome **underdetermine**，同时仍 genuinely ground it。

---

## 2. Non-fundamental bruteness

Bader 的重要 distinction：

\[
\boxed{Brute\neq Fundamental.}
\]

一个 derivative fact可以：

- 有 genuine contributing grounds；
- 由这些 grounds概率性支持；
- 但 exact outcome仍留给 chance。

所以 explanation 可以是 incomplete but genuine：

\[
X\text{ because of }\Gamma,\text{ despite }\Delta.
\]

这里：

- \(\Gamma\)：contributing grounds；
- \(\Delta\)：contravening grounds。

这使某个 derivative outcome不需要成为 fundamental primitive，尽管其 exact realization没有 sufficient deterministic ground。

---

## 3. Bader's fission application

fission：

\[
A@t_1\to B@t_2+C@t_2.
\]

B、C可以在 relevant respects完全对称。

传统困难：

- A cannot be numerically identical to both B and C under classical identity；
- selecting only B looks arbitrary；
- denying persistence on either branch can make outcome depend extrinsically on the other branch；
- one-many counterpart theories face agglomeration / symmetric-relation problems。

Bader stochastic account：

\[
\boxed{A\text{ persists on exactly one branch}.}
\]

但：

\[
\boxed{\text{which branch is left to objective chance}.}
\]

如果 actual outcome：

\[
A=B,
\]

则 C 是 newly existing person；另一个 possible realization可反过来。

因此 symmetric fission不要求 pre-existing structural asymmetry决定 winner。

---

## 4. Symmetry breaking without arbitrary deterministic tie-breaker

Bader 的主要 payoff之一：

\[
\boxed{
SymmetricGrounds
\not\Rightarrow
SymmetricDerivativeOutcome.
}
\]

只要：

\[
\text{grounding relation itself is stochastic}.
\]

这与项目此前 SAOL / spontaneous symmetry-breaking insight同方向，但更强：

absolute-path transition不一定需要一个独立 fundamental random selector；可以尝试把：

\[
Succ_O(\sigma_t,\sigma_{t+1})
\]

做成 derivative stochastic-grounding fact。

---

## 5. Necessary without sufficient conditions

Bader特别强调：branching cases可以保留 necessary conditions，即使没有 sufficient conditions。

抽象：

\[
C^+(\sigma)=\{\sigma_1,\sigma_2,\ldots\}
\]

candidate successor structure可以由 lower-level facts确定：

\[
\boxed{\sigma'\notin C^+(\sigma)\Rightarrow P(Succ_O(\sigma,\sigma'))=0.}
\]

但对多个 admissible successors：

\[
0<P(Succ_O(\sigma,\sigma_i))<1.
\]

所以理论可以解释：

- 为什么 winner必须来自某个 admissible set；
- 为什么某些 branches不可能继承；
- 为什么 symmetric candidates有 symmetric chances；

同时承认：

\[
\boxed{\text{why this exact admissible branch won has no further sufficient reason}.}
\]

---

## 6. Objective chance

Bader把概率理解为 objective chance / propensity-like structure，而非 subjective credence。

这使其 fission model 真正适合作为 SFO 的 ontic analogue：

\[
P_O(\sigma'\mid\sigma,R)
\]

可以被解释为 metaphysical chance of opening-continuation，而不是 observer uncertainty。

---

## 7. Moorfoot 2026 — In Defence of Indeterministic Building

Will Moorfoot, “In Defence of Indeterministic Building”, *Australasian Journal of Philosophy*, published online 2026-07-07, DOI `10.1080/00048402.2026.2684630`.

Moorfoot 的目标更一般：证明 indeterministic building 至少 logically coherent。

核心论证：

### P1

若 logical modal space中存在 indeterministic supervenience，则 indeterministic building coherent。

### P2

indeterministic supervenience logically possible。

因此：

\[
\boxed{\text{IndeterministicBuilding is coherent}.}
\]

他区分：

- metaphysical vagueness；
- contingent building；
- indeterministic building。

后者是真的 ontic chance：同一 building base允许不同 determinate built outcomes。

---

## 8. Moorfoot explicitly reuses Bader fission

Moorfoot 在讨论 non-fundamental objective chance 时直接使用 Bader 2020 §3：

\[
S_1@t_1\to S_2@t_2+S_3@t_2.
\]

其总结是：

\[
\boxed{
S_1\text{ can expect to become }S_2\text{ or }S_3,\text{ but not both; which one is left to chance}.}
\]

所以到 2026 年，fission + ontic chance / indeterministic building 已经不是孤立 proposal，而进入一个持续发展的 grounding/building literature。

---

## 9. Direct mapping to Stage-First Opening

SFO 当前：

\[
Open(\sigma_t)
\]

然后面对：

\[
C^+(\sigma_t)=\{\sigma_L,\sigma_R\}.
\]

Bader-style mapping：

### Lower/base facts

\[
G(\sigma_t,R)
\]

determine admissibility / strength of continuation candidates。

### Stochastic building

\[
G(\sigma_t,R)
\xrightarrow{stochastic\ grounding}
Succ_O(\sigma_t,\sigma_i).
\]

### Actual derivative outcome

\[
\boxed{\exists!\sigma_i\;Succ_O(\sigma_t,\sigma_i).}
\]

这样 complete opening path：

\[
\Pi_O
\]

可由一系列 stochastic-grounded successor facts生成。

---

## 10. Potential advantage over fundamental SAOL transition

### Fundamental transition law

\[
\Lambda_{succ}
\]

直接 primitive 地给 objective chance。

### Stochastic-grounding version

\[
\boxed{
physical/psychological/stage structure
\to
contributing+contravening grounds
\to
objective persistence chances.
}
\]

若成功，weights不再完全 free：

\[
w_i
\]

需来自实际 grounding structure / symmetries / strengths。

所以可减少：

\[
\boxed{\text{arbitrary weighting burden}.}
\]

这尤其适合 perfect fission：exact symmetry自然支持 equal chance，而无需先给两 branch token-specific qualities。

---

## 11. But it does not solve Absolute semantics

Bader只讨论 ordinary persistence / identity-related facts。

他没有：

\[
AbsoluteOrientation.
\]

所以项目只能借其 **transition metaphysics**：

\[
StochasticGrounding
\]

不能借出：

\[
\boxed{\text{why persistence of Opening has absolute first-person significance}.}
\]

这一点仍由 NOM / Opening semantics承担。

---

## 12. It also does not solve Localization Necessity

Universal-I 可以对 fission说：

\[
Mine(\sigma_L)\land Mine(\sigma_R).
\]

Bader-style stochastic persistence则只在已经采用：

\[
\boxed{ExactlyOneContinuation}
\]

时提供 elegant mechanism。

因此 logical order保持：

\[
LNP
\to
SelectiveOpening
\to
PSP
\to
StochasticGroundingSolution.
\]

Bader 解决的是 PSP mechanism，不是 LNP。

---

## 13. New distinction: fundamentality of law vs fundamentality of outcome

最重要的新项目收益：

\[
\boxed{\text{a brute exact outcome need not be a fundamental fact}.}
\]

因此若 opening trajectory在 fission中随机走左 branch：

\[
Succ_O(\sigma,\sigma_L)
\]

可以是：

- metaphysically contingent；
- not sufficiently determined；
- nevertheless derivative / stochastically grounded。

这比“absolute path必须由一个 primitive winner fact构成”更有理论空间。

但可能仍需要 fundamental：

\[
\boxed{\text{the stochastic building law / grounding architecture itself}.}
\]

---

## 14. Current verdict

Bader + Moorfoot 显著升级 Stage-First Opening 的 persistence route。

此前 PSP：

\[
\boxed{\text{no known principled mechanism for symmetric fission selection}.}
\]

现在应改为：

\[
\boxed{
\text{there is a mature stochastic-grounding / indeterministic-building mechanism template}.}
\]

它可以：

- respect symmetric base；
- produce one asymmetric persistence outcome；
- use objective chance；
- avoid deterministic arbitrary tie-breaking；
- let exact outcome be derivative rather than fundamental。

所以 SFO 的 strongest persistence model 可升级为：

\[
\boxed{
Open(\sigma_t)
+
StochasticGrounding(G_t)
\Rightarrow
\exists!\sigma_{t'}\;Succ_O(\sigma_t,\sigma_{t'}).
}
\]

但 absolute-local theory 的 deepest burden仍在更早：

\[
\boxed{Why\ SelectiveOpening\ rather\ than\ UniversalI?}
\]

## Sources

- Ralf M. Bader, “The Fundamental and the Brute”, *Philosophical Studies* 178, 1121–1142, DOI `10.1007/s11098-020-01486-z`.
- Will Moorfoot, “In Defence of Indeterministic Building”, *Australasian Journal of Philosophy*, published online 2026-07-07, DOI `10.1080/00048402.2026.2684630` — publisher full-text HTML read.
