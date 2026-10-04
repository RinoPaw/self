# Two-Tier First-Person Realism

> 状态：工作架构，已根据 List quadrilemma 与 `Relative First-Person Demotion` 修正。
>
> 关键变化：从现在起严格区分 **many ordinary first-person phenomenologies** 与 **many irreducible first-person facts**。前者容易与 one coherent world 相容；后者并不因为加上 standpoint 参数就免费变得 compossible。

## 1. 不变的核心直觉

本项目仍研究：

\[
\boxed{
\text{many genuine conscious subjects}
+
\text{possibly one absolute first-person orientation}
}
\]

所有真实主体都可以拥有 ordinary first-person phenomenology：

\[
\forall i\;LocalFPPhen(S_i).
\]

另外研究是否有唯一：

\[
\exists!E^*\;AbsoluteOrientation(E^*).
\]

但不能再把第一行自动升级成：

\[
\forall i\;F_i^{FP}
\]

其中每个 \(F_i^{FP}\) 都是 List/Fine 意义上的 irreducible, perspective-non-invariant first-person fact。

---

## 2. List quadrilemma 的约束

List 的四个 claims 是：

1. First-person realism：任一 conscious subject 都有 first-personal facts；
2. Non-solipsism：多于一个 conscious subject 真实；
3. Non-fragmentation：一个 world 中全部 facts compossible；
4. One world：现实只有一个 world。

四者不能共同成立。

最关键的是，List 直接考虑过把：

\[
F_A=\text{I am in }X
\]

改写成：

\[
F_A'=\text{there is an A-perspective from which “I am in X” is true}.
\]

这种 meta-fact 与 Bob 的对应 meta-fact当然可以共同成立，但它们在 subjective perspective shift 下 invariant，因此已经不是 first-person facts。

这直接约束本项目旧写法：

\[
F_i^{rel}=\text{“from }S_i\text{, ...”}.
\]

若 relativization 足以让所有 \(F_i^{rel}\) 在一个 coherent world 中共同成立，它们可能已经被 **demoted** 成描述 perspectives 的 third-personal facts。

详见 [`../arguments/relative-first-person-demotion.md`](../arguments/relative-first-person-demotion.md)。

---

## 3. 第一版本：Two-Tier Phenomenology

最弱、也最容易保持 one coherent world 的版本只要求：

\[
\forall i\;LocalFPPhen(S_i).
\]

每个 subject 都 genuinely conscious，并拥有：

- phenomenal character；
- for-me-ness / mineness；
- self-location；
- direct givenness；
- memory / anticipation；
- subject-relative representational or functional organization。

这些 facts 可以由 ordinary objective / relational / contextual structure描述，而不声称每个主体都额外贡献一个 irreducible simpliciter first-person fact。

然后加入：

\[
\exists!E^*\;AbsoluteOrientation(E^*).
\]

这给：

\[
\boxed{
\text{many ordinary FP phenomenologies}
+
\text{one absolute orientation}
}
\]

它可以原则上与：

\[
OneWorld+NonFragmentation+NonSolipsism
\]

相容。

代价明确：它**不保留 universal strong first-person realism**。

---

## 4. 第二版本：Two-Tier Strong Fact Realism

若坚持每个 genuine subject 都有 irreducible first-person facts：

\[
\forall i\;F_i^{FP},
\]

并且这些 facts essential non-invariant，那么不同 subjects 的完整 first-person facts会 non-compossible：

\[
F_i^{FP}\perp F_j^{FP}
\quad(i\neq j).
\]

此时再加入一个 absolute layer：

\[
\exists!i\;F_i^{abs}.
\]

并不会自动解决 List quadrilemma。

理论仍必须接受至少一种：

### Fragmentalist version

\[
OneWorld+
eg NonFragmentation.
\]

不同 FP facts 分布在 fragments / standpoints。

### Many-world version

\[
NonFragmentation+
eg OneWorld.
\]

不同 first-personally centred worlds 分别 realize 不同 FP facts。

所以 strong Two-Tier model 的真实成本是：

\[
\boxed{
\text{plural strong FP architecture}
+
\text{one extra absolute orientation}
}
\]

而不是一个简单 coherent fact-set。

---

## 5. Other-minds realism 与 strong FPR 分离

必须保留：

\[
\boxed{Conscious(S_i)\neq\text{“}S_i\text{ has irreducible FP facts”}}
\]

至少逻辑上二者是不同 premises。

Non-solipsism 只要求：

\[
\exists S_i\neq S_j\;[Conscious(S_i)\land Conscious(S_j)].
\]

Universal strong FPR 进一步要求：

\[
\forall i\;\exists F_i^{FP}.
\]

因此一个 absolute-one-world theory 可以真诚地承认其他人完全有意识，同时拒绝他们都拥有和 absolute layer 同类型的 irreducible first-person facts。

这不是 zombie theory；但它的 first-person metaphysics 是 inegalitarian 的，而且比项目早期 slogan 更弱。

---

## 6. Obtaining-mode route 不能免费修复问题

可能希望用：

\[
[F_A]_{M_A},
\qquad
[F_B]_{M_B}
\]

让各 first-person facts 以不同 mode obtain。

Eker / Lipman 证明这种 architecture 是严肃选项，但仍需说明：

- modes 让原 facts 真正 compossible，还是只把它们放入不同 fragments；
- mode qualifier 是否把原 fact third-personalize；
- broader totality 是否本质上已经是一种 metaphysical relativity / fragmentalism。

所以 obtaining modes 可以构造 strong pluralist ontology，却不让 List pressure 消失。

---

## 7. Absolute layer 的三种来源仍然不变

无论 ordinary layer 选 Phenomenology 还是 Strong Fact Realism，absolute orientation \(\Omega\) 仍有三条主要路线。

### Derived

\[
D\Rightarrow\Omega(E^*).
\]

承担 Grounded Centering Ladder。

### Primitive

\[
\Omega[R;E^*]
\]

作为 actuality 的 primitive singular orientation；见 `Minimal Absolute Opening`。

### Stochastic promotion

\[
D\Rightarrow P(E),
\qquad
E^*\sim P.
\]

可以产生 token asymmetry，但 why-this-one 停在 chance，且仍需 actuality/liveness bridge。

---

## 8. Coherence-based `≤1` 的适用域

Coherence result 现在也必须写得更谨慎。

如果我们已经承认一类 simpliciter absolute centered facts：

\[
F_i^{abs},
\]

且：

\[
F_i^{abs}\perp F_j^{abs},
\]

那么 one coherent absolute layer 可以给：

\[
|AbsoluteCenters|\le1.
\]

但不能拿 ordinary strong FP facts 的 incompatibility直接推出 absolute singleton。

普通层若 strong，则它们本来就把理论推向 fragmentation / many worlds。

所以：

\[
\boxed{\text{coherence constrains an admitted absolute layer; it does not create it}.}
\]

---

## 9. 当前四个主要 package

### P-F — Fragmentalist pluralism

\[
StrongFPR+NonSolipsism+OneWorld+Fragmentation.
\]

没有 absolute orientation。

### P-MW — Many-world first-person realism

\[
StrongFPR+NonSolipsism+NonFragmentation+ManyWorlds.
\]

没有 absolute orientation。

### A-W — Absolute one-world / weak ordinary-FP

\[
ManyConsciousSubjects+LocalFPPhen+OneWorld+NonFragmentation+\Omega.
\]

保持 other minds 与 ordinary phenomenology，但不承诺所有 subjects 都有 strong irreducible FP facts。

### A-F / A-MW — Absolute + strong ordinary-FP

先支付 P-F / P-MW 的 strong-FPR architecture cost，再加入：

\[
\Omega.
\]

这最忠实于项目早期 “many strong ordinary FP + one extra absolute FP” 直觉，但 ontology 成本也最高。

---

## 10. 当前评价

`Two-Tier First-Person Realism` 不再是一套单一模型，而是一族模型。

它最重要的新分叉是：

\[
\boxed{
\text{Two-Tier Phenomenology}
\quad vs\quad
\text{Two-Tier Strong Fact Realism}
}
\]

前者给 absolute one-world theory 一个意外干净的空间；后者则说明，如果项目坚持“其他每个主体也有 irreducible first-person facts”，fragmentation / many-world cost 无法靠加 `relative` 下标绕掉。

因此下一步理论选择必须先回答：

\[
\boxed{
\text{non-negotiable 是 other minds 的 genuine consciousness，还是 universal strong first-person fact realism？}
}
\]

项目最初明确要求前者；是否还必须接受后者，目前应保持开放。

## 文献与关联

- Christian List, “A quadrilemma for theories of consciousness”, *The Philosophical Quarterly* 75(3), 2025。
- Christian List, “The Many-Worlds Theory of Consciousness”, *Noûs* 57(2), 2023。
- Martin Lipman, *Standpoints: Time and Subjectivity* (2026).
- Bahadir Eker, “Perspectivalism about temporal reality” (2023).
- [`../arguments/relative-first-person-demotion.md`](../arguments/relative-first-person-demotion.md)
- [`../arguments/obtaining-mode-pluralization.md`](../arguments/obtaining-mode-pluralization.md)
- [`minimal-absolute-opening.md`](minimal-absolute-opening.md)
