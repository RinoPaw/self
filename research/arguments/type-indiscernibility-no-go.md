# Type-Indiscernibility No-Go

> 状态：条件性模型论结果。
>
> 目的：把“实际结构刚性仍可能掩盖解释空缺”进一步形式化。

## 0. 设置

设 \(L\) 是允许用于解释 absolute center 的 **independent vocabulary**。

重要：\(L\) 不包含：

- `Absolute(x)`；
- `LIVE_simpliciter(x)`；
- primitive center label；
- 其他直接把答案写进语言的符号。

设实际现实的 \(L\)-structure 为：

\[
M.
\]

候选 conscious events：

\[
a,b\in M.
\]

---

## 1. Same complete type

若：

\[
tp_M(a/\varnothing)=tp_M(b/\varnothing),
\]

则 \(a,b\) 满足完全相同的无参数 \(L\)-公式。

因此不存在无参数 \(L\)-公式：

\[
\varphi(x)
\]

使：

\[
M\models\varphi(a)
\]

但：

\[
M\not\models\varphi(b).
\]

所以任何只使用该 independent vocabulary 的 first-order structural property 都不能区分二者。

---

## 2. Immediate centering consequence

若一个 grounded centering principle 要求：

\[
E^*=\text{the unique }x\text{ such that }\varphi(x),
\]

其中 \(\varphi\) 只使用 \(L\)，那么只要另一个 candidate \(b\neq a\) 与 \(a\) realize same complete type：

\[
\boxed{\text{no such parameter-free }\varphi\text{ can uniquely select }a}
\]

因此：

\[
\boxed{
\text{complete }L\text{-indiscernibility}\Rightarrow\text{no }L\text{-definable absolute center}
}
\]

---

## 3. Why actual rigidity does not save the theory

可以出现：

\[
Aut(M)=\{id\}
\]

同时某些 elements 在允许语言里仍没有足够统一的 definitional basis 来承担 theory-level centering。

模型论中的标准结果给更强的视角：若两个 tuples realize same complete type over parameters \(A\)，则可以 passage 到某个 elementary extension \(N\succ M\)，在其中存在 fixing \(A\) 的 automorphism 把一个送到另一个。

形式：

\[
tp_M(a/A)=tp_M(b/A)
\]

则存在：

\[
N\succ M
\]

和：

\[
\sigma\in Aut(N/A)
\]

满足：

\[
\sigma(a)=b.
\]

所以 actual structure 的 accidental rigidity 不能把 language-internal indiscernibility 变成真正 definitional asymmetry。

---

## 4. Connection to Svenonius

Svenonius-style definability results说明：definability 应通过 elementary extensions 中保持 base vocabulary 的 permutations / automorphisms 检验，而不能只检查 actual structure 的 automorphism group。

方法论上：

\[
\boxed{
\text{actual-world fixed point}\ll\text{uniform structural definability}
}
\]

这加强 `Invariance–Definability Gap`。

---

## 5. Relation to duplication arguments

`Locality–Duplication No-Go` 使用的是某个机制可读取 profile 的 rooted isomorphism：

\[
N_D(E_a)\cong N_D(E_b).
\]

当前结果更逻辑化：只要：

\[
tp_L(E_a)=tp_L(E_b),
\]

那么任何 \(L\)-definable predicate 都无法只挑一个。

所以两条结果可以看成不同层次：

### Structural duplication

\[
\text{same relevant relational profile}
\Rightarrow
\text{same structural output}.
\]

### Logical indiscernibility

\[
\text{same complete }L\text{-type}
\Rightarrow
\text{same }L\text{-definable properties}.
\]

后者尤其适合检验 alleged \(Q_R(E)\) 是否真的在 independent vocabulary 中定义出来。

---

## 6. Necessary positive condition

若正方坚持一个 nonprimitive definable center \(E^*\)，那么至少需要：

\[
\exists\varphi(x)\in L
\]

使 actual relevant structure 中：

\[
M\models\varphi(E^*)
\]

以及：

\[
\forall E\in\mathcal E_C,\quad
M\models\varphi(E)\Rightarrow E=E^*.
\]

更强的版本要求同一个 \(\varphi\) 在 admissible model class 中稳定工作。

因此 target 从：

\[
E^*\text{ is fixed}
\]

升级为：

\[
\boxed{E^*\text{ has an independently expressible unique structural type/role}}
\]

---

## 7. Parameter problem

若允许 arbitrary parameter：

\[
\varphi(x,E^*)\equiv x=E^*,
\]

任何 element 都 trivially definable。

所以 grounded centering 不能允许把目标 token 自己或其 disguised name 当参数。

需要明确：

\[
\boxed{\text{Parameter Discipline Requirement}}
\]

允许的 parameters 只能来自 independently given structure，而不能是待解释的 center 本身。

---

## 8. Current consequence for Q

任何 candidate：

\[
Q_R(E)
\]

现在都需要经过四层检查：

1. **Vocabulary**：Q 使用哪些 independent predicates / relations？
2. **Indiscernibility**：是否有另一 conscious candidate realize same relevant type？
3. **Uniformity**：Q 是否在 relevant counterfactual / elementary extensions 中保持同一解释？
4. **Privilege**：即使 definable，为什么 Q-role 与 absolute liveness 有关？

因此 model theory 可以帮助解决：

\[
\text{which one can structure distinguish?}
\]

却仍不会自动解决：

\[
\text{why does distinguishedness amount to LIVE?}
\]

## 文献入口

- David Marker, *Model Theory: An Introduction*, Proposition 4.1.5：same complete type 可在 elementary extension 中由 automorphism 交换。
- Svenonius theorem：definability 与 elementary extensions 中 preservation by permutations / automorphisms 的关系。
- Logic Journal of the IGPL 23(6), 2015, “A combinatorial version of the Svenonius theorem on definability”.
