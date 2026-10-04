# No-Natural-Pointing Theorem

> 状态：形式化工作定理。
>
> 目的：把 Symmetry Obstruction、Natural Section 与“不能从裸候选集合自然选一个中心”统一起来。

## 0. Candidate functor

设 \(\mathbf R\) 是 admissible realities 的 category。

对每个 reality \(R\)，令：

\[
C(R)=\{\text{absolute-eligible conscious events in }R\}.
\]

把 relevant structure-preserving map：

\[
f:R\to R'
\]

送到 candidate map：

\[
C(f):C(R)\to C(R').
\]

于是：

\[
C:\mathbf R\to\mathbf{Set}
\]

是 candidate functor。

一个完全结构性的 absolute-centering rule 是一族元素：

\[
e_R\in C(R)
\]

满足对每个 relevant \(f\)：

\[
\boxed{C(f)(e_R)=e_{R'}}.
\]

categorically，这正是从 terminal functor \(1\) 到 \(C\) 的 natural transformation：

\[
\eta:1\Rightarrow C.
\]

也可以称为 candidate functor 的 natural global element。

---

## 1. Bare-set no-go

先看最贫的情况：objects 只是 nonempty sets，morphisms 包含所有 functions。

假设存在 natural choice：

\[
e_X\in X
\]

满足任意：

\[
f:X\to Y
\]

都有：

\[
f(e_X)=e_Y.
\]

取任意非空 \(X\)，以及至少有两个元素 \(y_1\neq y_2\) 的 \(Y\)。

考虑两个 constant maps：

\[
f_1(x)=y_1,
\qquad
f_2(x)=y_2.
\]

naturality 要求：

\[
f_1(e_X)=e_Y
\]

和：

\[
f_2(e_X)=e_Y.
\]

于是：

\[
y_1=e_Y=y_2,
\]

矛盾。

因此：

\[
\boxed{
\text{there is no natural way to choose one element from every nonempty bare set}
}
\]

当 morphisms 只取 bijections 时，同样的结论已可由 symmetry 得到：二元素集合的 transposition 没有 fixed point。

---

## 2. Reality-level theorem

设 \(R\in\mathbf R\)，且存在 automorphism：

\[
g:R\to R
\]

使其在 candidates 上没有 fixed point：

\[
\forall E\in C(R),\quad C(g)(E)\neq E.
\]

若 natural global element \(\eta\) 存在，则 naturality 要求：

\[
C(g)(e_R)=e_R,
\]

与无 fixed point 矛盾。

所以：

\[
\boxed{
Fix(C(Aut(R)))=\varnothing
\Rightarrow
\text{no natural absolute-centering rule on any category containing }R
}
\]

这是 Symmetry Obstruction 的 functorial 版本。

---

## 3. Transitive symmetry corollary

若 \(Aut(R)\) 对 \(C(R)\) transitively action，并且：

\[
|C(R)|>1,
\]

则没有任何 candidate 被所有 automorphisms 固定。

因此：

\[
\boxed{
\text{transitive candidate symmetry}\Rightarrow\text{no natural global center}
}
\]

只要理论允许一个这样的 admissible reality，理论级 universal centering principle 就失败，除非：

1. theory 禁止该 reality；
2. candidate functor 遗漏了 relevant structure；
3. center 由额外 ontology / primitive data 给出；
4. centering law 是 stochastic，而非 deterministic natural element；
5. singleton requirement 被放弃。

---

## 4. Why this is stronger conceptually than “symmetry is bad”

这个 formulation 明确告诉我们 successful positive theory 必须做什么：

它必须把 candidate set 从 bare set 升级成一种有足够结构的 object，使其中某个 element 由该结构自然 distinguished。

也就是需要：

\[
(C(R),S_R)
\]

其中 \(S_R\) 是：

- grounding relations；
- manifestation relations；
- anchoring network；
- generative order；
- universal-property structure；
- 其他 independent global relations。

然后 natural center 才可能由：

\[
Q_{S_R}(E)
\]

定义。

所以：

\[
\boxed{
\text{absolute centering requires structure beyond mere multiplicity of conscious candidates}
}
\]

---

## 5. But extra structure creates a new burden

加入 \(S_R\) 以后，理论不能只说它让某个点 unique。

还需说明：

1. \(S_R\) independently motivated；
2. \(S_R\) 不是由 `Absolute(E*)` 反向定义；
3. 同一个 construction 在 relevant models / counterfactuals 中工作；
4. \(Q\) 具有 first-person / actuality significance；
5. token identity 足够精细。

这连接到：

- Invariance–Definability Gap；
- Universal-Property–Manifestation Dilemma；
- Manifestation-Bearer Dilemma。

---

## 6. Pointed-set interpretation

一个 centered candidate set 本质上类似 pointed set：

\[
(C(R),E^*).
\]

forgetful map：

\[
U:\mathbf{Set}_*\to\mathbf{Set}
\]

忘掉 basepoint。

问题可以读成：

> complete uncentered candidate structure 是否允许一个 natural lift 回 pointed structure？

对 bare sets，答案是否定的。

对 richer realities，答案取决于额外结构是否真的产生 distinguished point。

这精确区分：

\[
\boxed{\text{having a point}}
\]

与：

\[
\boxed{\text{having a naturally determined point}}.
\]

---

## 7. Current status

本定理不证明 absolute first-person 不存在。

它证明一种更窄但很有用的事：

\[
\boxed{
\text{ordinary plurality of candidates by itself can never generate a natural absolute center}
}
\]

所有解释性正方路线都必须找到：

\[
\boxed{\text{an independently meaningful asymmetry-bearing structure}}
\]

或接受 centeredness / selection 是 fundamental。

## 数学背景

- Pointed sets：一个 set 加一个 chosen basepoint；forgetful functor 忘掉该点。
- Natural transformations / global elements：natural family of elements 可以写成 \(1\Rightarrow C\)。
- Automorphism fixed-point argument：natural choice 必须被 every automorphism preserved。
