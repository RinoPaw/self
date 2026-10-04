# Feltness Residual Test：被感受到性是否逼出 absolute first-person

> 状态：压力测试。当前结论：Merlo 式 feltness 很接近项目原始直觉，但从现象学可直接得到的更自然是 relational feltness；从 relational feltness 升级到唯一 unary / simpliciter feltness 仍缺独立论证。

## 0. 动机

在 fission 与 I–NOW trajectory 都没有成功逼出 residual `X` 后，最强候选之一是 Giovanni Merlo 所说的 **feltness**。

直觉大致是：

> 我的体验不只是存在；它们以一种直接“被感受到”的方式在场。别人的体验虽然我相信存在，却没有以同样方式出现在这里。

这非常接近本项目最初的：

\[
L=\text{liveness / actuality simpliciter}.
\]

因此需要检查 feltness 能否真正跨过 Xerographic Fork。

---

## 1. Merlo 的核心论证结构

Merlo 2021 区分两种主张。

### Phenomenological solipsism

从当前第一人称看来，只有这些——事实上是我的——体验显得具有 feltness。

### Appearance / Reality Principle

对 phenomenal consciousness，appearance 与 reality 不能像普通外部对象那样分开：若某种 phenomenal character 真正出现，它就在意识现实中存在。

由此 Merlo 推向：

### Metaphysical solipsism

只有我的体验真正具有 feltness。

这不一定意味着别人是 zombie。较温和版本可以允许别人的体验有 pain、colour 等 phenomenal character，却缺少我的体验拥有的那层特殊 `glow`。

对 `self` 来说，Merlo 的结构可粗写成：

\[
AppearsFelt(E_i,S^*)
\Rightarrow
FeltSimpliciter(E_i),
\]

并进一步：

\[
\forall j\neq *\;\neg FeltSimpliciter(E_j).
\]

如果成立，它几乎直接给出 absolute-first-person 所需的 exclusivity。

---

## 2. 第一处压力：关系形式与一元形式

需要严格区分：

\[
Felt(E,S)
\]

和：

\[
FeltSimpliciter(E).
\]

第一种表达：

> 体验 `E` 对主体 `S` 被直接感受到。

第二种表达：

> `E` 本身、无进一步相对化地拥有绝对 feltness。

普通内省最直接支持的是：

\[
Felt(E_{mine},S_{me}).
\]

它并没有直接观察到：

\[
\neg Felt(E_{other},S_{other}),
\]

更没有直接观察到：

\[
\neg FeltSimpliciter(E_{other}).
\]

所以这里存在一个关键升级：

\[
\boxed{
\text{relational feltness}
\not\Rightarrow
\text{unary feltness simpliciter}
}
\]

暂称 **Relational-to-Unary Feltness Gap**。

---

## 3. Phenomenology-to-Exclusivity Gap

设当前主体为 `S_a`。

当前完整 phenomenology 可以支持：

\[
Felt(E_a,S_a).
\]

并且我可以完全没有：

\[
Felt(E_b,S_a)
\]

——你的痛没有直接作为我的痛呈现。

但：

\[
\neg Felt(E_b,S_a)
\]

不推出：

\[
\neg Felt(E_b,S_b).
\]

也不推出：

\[
\neg FeltSimpliciter(E_b).
\]

因此：

\[
\boxed{
\text{absence from this standpoint}
\not\Rightarrow
\text{absence simpliciter}
}
\]

这是 feltness 版的 Relativization Collapse 压力。

如果绝对第一人称的证据仅来自“别人的体验没有在这里被我感到”，那它最多直接建立 standpoint asymmetry。

---

## 4. Kinkaid / Sartre 对 Merlo 第一前提的直接反击

Kinkaid 2025 使用 Sartre 的“公园中的他人”来挑战 Merlo 的 phenomenological solipsism。

Sartre 式现象学认为，遇到另一个人时，对方并不像树或长椅那样只是我世界中的对象；他呈现为另一个 **center of orientation**，一个拥有自己的 hodological space / perspective 的 ipseity。

因此经验他人时，至少可能出现：

\[
Appears(OtherCenter(S_b),S_a).
\]

Kinkaid 的核心压力是：若他人在我的经验中本来就呈现为拥有其自身 `mineness` 的另一个中心，那么 Merlo 所需的：

\[
\text{“它显得只有我的体验有 feltness”}
\]

并非无争议的 phenomenological datum。

这不会证明别人具有和我完全相同的 feltness；但它削弱了从“纯现象学描述”直接得到 exclusivity 的第一步。

---

## 5. Lipman 的 pluralist reconstruction

Lipman 2026 对 phenomenal consciousness 的基本处理是：phenomenal appearances **relative to subjects** obtain。

可以粗略表示：

\[
Appearance(p,S_i).
\]

每个真实主体都可以是自己的 factual standpoint，并拥有真实、不可删除的 subjective facts。

于是可以同时接受：

\[
Felt(E_a,S_a),
\]

\[
Felt(E_b,S_b),
\]

以及：

\[
\neg Felt(E_b,S_a),
\]

而无需再增加：

\[
FeltSimpliciter(E_a)
\]

和：

\[
\neg FeltSimpliciter(E_b).
\]

因此 pluralist E-horn 能保留几乎全部局部 phenomenological asymmetry，同时拒绝 global exclusivity。

---

## 6. Unary-Feltness Underdetermination

给定当前主体 `S_a` 的全部 phenomenology 与 self-locating facts：

\[
P_{S_a}.
\]

至少下面几种 global ontology 原则上可以共享相同 `P_{S_a}`：

### Model A — Inegalitarian unary feltness

\[
FeltSimpliciter(E_a),
\qquad
\neg FeltSimpliciter(E_b).
\]

### Model B — Standpoint pluralism

\[
Felt(E_a,S_a),
\qquad
Felt(E_b,S_b),
\]

没有额外 unary `FeltSimpliciter`。

### Model C — Two-tier model

所有主体有 relational feltness：

\[
\forall i\;Felt(E_i,S_i),
\]

另外仍有一个：

\[
FeltSimpliciter(E^*).
\]

只要这个额外 absolute status 对 `S_a` 的 local phenomenology 没有独立影响，当前 phenomenology 不能在 A/B/C 之间判定。

因此得到一个条件性认识论结果：

\[
\boxed{
P_{S_a}\text{ alone underdetermines global unary feltness}
}
\]

暂称 **Unary-Feltness Underdetermination**。

这不是说 unary feltness 不存在；它说明纯内省无法独自证明它的 global distribution。

---

## 7. Appearance / Reality Principle 能不能救 unary feltness

Merlo 的强点是：对 consciousness，appearance 与 reality 很难分离。

但即使接受：

\[
AppearsFelt(E_a,S_a)
\Rightarrow
Felt(E_a,S_a),
\]

也还没有得到：

\[
AppearsOnlyMineFelt
\Rightarrow
OnlyMineFeltSimpliciter.
\]

因为这里多出一个量词与层级转换：

1. 从一个 standpoint 内什么出现；
2. 到整个现实中哪些体验具有 unary absolute status。

Appearance / Reality Principle 最自然保证的是“出现的 phenomenal character 真实”，并不自动保证“当前 standpoint 对别的 standpoint 的缺席经验”构成关于全局 unary distribution 的完备事实。

所以正方还需要一个更强原则，例如：

\[
\boxed{\text{Phenomenal Completeness for Feltness}}
\]

大意是：当前第一人称 phenomenology 不仅无误地呈现自身 feltness，还完整呈现整个现实中 feltness simpliciter 的分布。

这个原则非常强，目前没有独立支持。

---

## 8. Perfect Duplicate Pressure

设两个 conscious systems 在 physical / functional / phenomenal / memory / local-causal profile 上完全复制：

\[
E_a\cong E_b.
\]

普通 psychophysical law 很自然给出：

\[
Felt(E_a,S_a)
\]

与：

\[
Felt(E_b,S_b).
\]

若 unary feltness 只属于一个：

\[
FeltSimpliciter(E_a),
\qquad
\neg FeltSimpliciter(E_b),
\]

则 asymmetry-maker 必须来自 duplicated profile 外部：

- genuinely global relation；
- constitutively centered total state；
- primitive center；
- ontic stochastic actualization；
- 或其他非局部 generative structure。

所以 feltness 并没有绕过 Locality–Duplication No-Go。

---

## 9. 正方真正需要的原则：Exclusive Feltness Principle

如果仍坚持：

\[
\exists !E^*\;FeltSimpliciter(E^*),
\]

可以把这一承诺隔离成：

\[
\boxed{\text{Exclusive Feltness Principle (EFP)}}
\]

> 在全部真实 conscious experiences 中，恰有一个 experience / thread 的 feltness 是 simpliciter；其他体验即使对自己的 subjects 真正被感受到，也没有同等级的 absolute feltness。

EFP 非常接近项目真正想证明的 absolute-first-person thesis。

因此不能把 EFP 当作 Merlo phenomenology 的直接翻译；它必须获得独立证据或结构来源。

---

## 10. 两种 positive architecture 下 EFP 的位置

### Transition Architecture

先有：

\[
H\to\mathcal C(H),
\]

再需要：

\[
T_{C\to A}(\mathcal C)=E^*,
\]

并定义：

\[
FeltSimpliciter(E^*).
\]

这里 EFP 面临 selector / global relevance / stochastic / seed 等已知压力。

### Constitutively Centered Architecture

完整现实状态：

\[
R^*
\]

本身包含 center component：

\[
Center(R^*)=E^*.
\]

然后 unary feltness 可以被理解为该 globally instantiated centered total state 的 constituent。

这避免了“先有 uncentered reality 再额外选一个”的 picture，但问题转为：

\[
\boxed{\text{为什么 centeredness / unary feltness 是 complete reality 的合法 constituent？}}
\]

以及：

\[
\boxed{\text{为什么实际实例化的是这个 centered total state？}}
\]

所以 feltness residual 对两种架构都还没有给出独立胜利。

---

## 11. 当前结论

Feltness 是目前最接近项目原始直觉的 candidate `X`，但现阶段仍没有通过 Xerographic Fork 的 Necessity test。

我们可以很稳地保留：

\[
\boxed{\text{ordinary relational feltness is real}}
\]

而正方真正需要证明的是额外的：

\[
\boxed{\text{there is exactly one unary feltness simpliciter}}
\]

当前三道压力是：

1. **Phenomenological premise pressure**：Kinkaid/Sartre 认为他人本就呈现为另一个有自身 mineness 的中心；
2. **Relational reconstruction pressure**：Lipman 能把 phenomenal appearance 作为 relative-to-subject 的真实事实保存；
3. **Global underdetermination pressure**：当前 phenomenology 无法单独决定整个现实中 unary feltness 的分布。

所以 Merlo 的 feltness 并未被淘汰，但它被精确压缩成 EFP。

下一步最值得检查的已不再是“我有没有一种特殊 felt quality”，而是：

\[
\boxed{\text{有什么理由认为 feltness 的正确逻辑形式是一元的，而不是关系性的？}}
\]

如果 unary form 没有独立理由，absolute-first-person 的 phenomenological foundation 会受到很大削弱。

## 文献入口

- Giovanni Merlo, “The Metaphysical Problem of Other Minds”, *Pacific Philosophical Quarterly* 102(4), 2021, 633–664. DOI `10.1111/papq.12380`.
- Giovanni Merlo, “Subjectivism and the Mental”, *Dialectica* 70(3), 2016, 311–342. DOI `10.1111/1746-8361.12153`.
- James Kinkaid, “A ‘Drainage Hole’ in Being: Sartre and First-Person Realism”, *Journal of the American Philosophical Association* 11(4), 2025, 782–799. DOI `10.1017/apa.2025.8`.
- Martin Lipman, *Standpoints: Time and Subjectivity* (Oxford University Press, 2026), chapters 7–8.
