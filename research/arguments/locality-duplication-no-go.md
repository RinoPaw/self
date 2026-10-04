# Locality–Duplication No-Go

> 状态：条件性工作定理。它不证明绝对第一人称不存在；它排除一大类仅依赖局部、事件相对结构的统一唯一化机制。

## 1. 动机

此前的 **Symmetry Obstruction** 使用完整现实的自同构：若一个真实全局对称把两个意识事件互换，纯结构选择器无法只选其中一个。

但真实宇宙可能高度不对称：

\[
\operatorname{Aut}(\mathcal R)=\{id\}.
\]

这时全局自同构禁阻不再直接适用。

然而，很多 liveness 候选机制并不会读取整个宇宙。它们只依赖当前意识事件附近的：

- phenomenal profile；
- neural / computational profile；
- local causal structure；
- local grounding structure；
- generative-process / frontier status；
- 某个有限或事件相对的结构邻域。

只要两个事件在该机制真正能使用的结构上完全复制，唯一性仍然会失败。

---

## 2. 设置

设意识事件集合为：

\[
\mathcal E_C.
\]

对候选机制 \(D\)，令

\[
N_D(E)
\]

表示决定该机制输出时允许使用的、以 \(E\) 为根的完整相关 profile。

这里的 “local” 不必只指空间局部。它表示：规则只读取某个事件相对、有限、因果邻近或 otherwise bounded 的结构，而不读取完整现实的全部关系。

设 liveness 规则为：

\[
\Lambda_D(E)=F([N_D(E),E])\in\{0,1\},
\]

其中方括号表示 rooted isomorphism class。要求 \(F\) 是统一、同构不变的结构规则。

---

## 3. Locality–Duplication Lemma

若两个不同意识事件满足：

\[
(N_D(E_a),E_a)\cong(N_D(E_b),E_b),
\qquad E_a\neq E_b,
\]

则：

\[
\boxed{\Lambda_D(E_a)=\Lambda_D(E_b)}.
\]

### 推导

\(\Lambda_D\) 按定义只依赖 rooted isomorphism class：

\[
[N_D(E_a),E_a]=[N_D(E_b),E_b].
\]

因此统一规则 \(F\) 对两者得到同一输出。

证毕。

---

## 4. 对绝对唯一性的直接后果

如果 \(E_a\) 与 \(E_b\) 是相对于机制 \(D\) 的精确复制体，并且：

\[
LIVE(E_a),
\]

那么同一局部规则必然给出：

\[
LIVE(E_b).
\]

因此：

\[
\boxed{
Dup_D(E_a,E_b)\land LIVE(E_a)
\Rightarrow LIVE(E_b)
}
\]

从而一个允许这种复制的纯局部机制不能保证：

\[
\exists !E^*\;LIVE(E^*).
\]

这是一项**条件性 no-go**：只要绝对 LIVE 完全 supervene 于可被精确复制的局部相关结构，全局唯一性就无法由该结构获得。

---

## 5. 它比全局自同构禁阻更强在哪里

Symmetry Obstruction 要求存在：

\[
g\in\operatorname{Aut}(\mathcal R)
\]

把整个现实中的两个候选交换。

Locality–Duplication No-Go 不需要这一条件。

可以有：

\[
\operatorname{Aut}(\mathcal R)=\{id\},
\]

同时两个事件在所有被 \(D\) 使用的局部事实上完全同构：

\[
N_D(E_a)\cong N_D(E_b).
\]

远处的星系、历史、随机扰动等可以使整个宇宙完全不对称；只要局部 liveness rule 看不到这些差异，它仍必须给两个复制体同样的 LIVE 值。

所以：

\[
\text{global rigidity}
\]

并不能拯救：

\[
\text{local supervenience of absolute liveness}.
\]

---

## 6. 对当前候选模型的作用

### 普通 for-me-ness

若两个经验在相关第一人称结构上复制，则普通 for-me-ness 会对两者同样成立。这符合预期，也说明它不能提供 global uniqueness。

### Fundamental process / causal-set becoming

若 LIVE 只由：

\[
Generated_G(E)\land Conscious(E)
\]

或者由“处在生成前沿”决定，那么多个结构相同的前沿意识事件都会得到 LIVE。

因此 Process-to-Center Gap 可以进一步加强为：过程唯一性之外，即使局部 process profile 非常丰富，只要它可复制，仍无法单独产生唯一 center。

### Forrest 式 causal-frisson / dead past

Forrest 的 growing-block 路线把 sentience 与现实增长边界上的 activity 联系起来。这可以很好地承担 `frontier -> liveness`，却自然允许边界上的多个主体共同满足同一条件，因此仍停留在 Liveness Generation。

### 局部 grounding / information / complexity 指标

若某个 grounding depth、信息量、整合度、复杂度或其他事件局部指标在两个候选处完全相同，统一规则同样无法只特权其中一个。

---

## 7. Duplication Quadrilemma

这把 Absolute Center Uniqueness Problem 压缩成四条出路。

### A. Local supervenience

\[
LIVE(E)=F(N_D(E)).
\]

若精确复制可能，则复制体得到相同 LIVE 值。

**结果：无法保证全局唯一中心。**

### B. Global relational dependence

让 LIVE 依赖整个现实中关于 \(E\) 的全局关系：

\[
LIVE(E)=F(\mathcal R,E).
\]

这样即使两个事件局部复制，远程关系也可能区分它们。

这条路没有被 no-go 排除，但马上承担新的 **Global Relevance Requirement**。

### C. Primitive / haecceitistic asymmetry

加入一个不由复制 profile 决定的进一步事实、thisness 或 primitive pointer：

\[
A(E^*).
\]

它可以直接打破复制对称，但来源解释在这里停止。这正是当前项目暂不愿过早采用的路线。

### D. 禁止真正复制

理论可以主张现实定律保证每个意识事件在足够完整的结构上都唯一。

这最多得到：

\[
\text{individualization}.
\]

仍然没有推出：

\[
\text{privilege}.
\]

所以它绕过复制禁阻，却没有跨过 Privilege Bridge。

---

## 8. Global Relevance Requirement

如果正方走 B，不能只说“整个宇宙最终能区分两个复制体”。

设：

\[
G_{\mathcal R}(E)
\]

是事件在完整现实中的某种全局关系 profile。

即使存在唯一：

\[
E^*=\operatorname*{arg\,ext}_E J(G_{\mathcal R}(E)),
\]

我们仍只得到一个全局可辨认的特殊位置。

必须继续给出：

\[
\boxed{
G_{\mathcal R}(E^*)
\Longrightarrow
LIVE(E^*)
}
\]

的独立理由。

暂称：

\[
\boxed{\text{Global Relevance Requirement}}
\]

也就是：用于打破复制对称的远程 / 全局事实必须与 liveness 的形而上来源相关，而不能只是一个任意的 canonical address。

这再次体现：

\[
\text{global distinguishability}\not\Rightarrow\text{absolute privilege}.
\]

---

## 9. 与 perfect phenomenal duplication 文献的关系

Kent Nimmo 2026 的工作给出一个高度相邻的压力：在 restricted anti-haecceitist premise 下，一旦 occurrent experience 的 phenomenal 与 structural profile 被固定，就没有额外的 internal first-person fact 能把一个 perfect duplicate 进一步特权化为“唯一是我的”；若坚持进一步事实，需要一个不包含在 duplicated profile 中的 primitive asymmetry-maker。

本项目不直接接受该论文的全部形而上前提，也没有从它推出 absolute first-person 不存在。

它的用途更窄：它支持这里的局部边界判断——**复制 profile 内部本身不足以承担唯一化；任何剩余差异必须来自更广的关系结构或额外 asymmetry-maker。**

---

## 10. 当前推进

这一 no-go 把下一阶段目标进一步收紧。

如果绝对第一人称实在论成立，同时又拒绝 primitive pointer，那么成功模型很可能必须具有：

\[
\boxed{\text{genuinely global metaphysical dependence}}
\]

并且同时满足：

1. 能区分局部精确复制体；
2. 区分方式通过结构本身产生，而非额外标签；
3. 全局关系本身具有生成 liveness / privilege 的意义；
4. 不能只获得 canonical individuation；
5. 在相对论、gauge 与多元宇宙下仍然可定义。

因此新的直接研究目标是：

\[
\boxed{\text{寻找满足 Global Relevance Requirement 的全局关系}}
\]

而不再泛泛寻找任意 selector。
