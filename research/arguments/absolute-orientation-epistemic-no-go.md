# Absolute-Orientation Epistemic No-Go

> 状态：条件性 epistemic result。
>
> 目标：把 `Absolutization Epistemic Fork` 从直觉升级成一个清楚的 evidence-indistinguishability 结果，并隔离 Minimal Absolute Opening 若想获得自知必须新增什么。

## 0. 设置

令：

\[
K
\]

表示 absolute realist 与 opponent 共享的全部 common-core facts，包括：

- physical history；
- all conscious states；
- phenomenal character；
- for-me-ness；
- memories；
- cognition；
- reports；
- behavior；
- ordinary self-location；
- ordinary subject-relative / perspectival structure。

对候选 centers：

\[
E_1,E_2,\ldots,E_n,
\]

Minimal Absolute Opening 增加：

\[
\Omega_i:=\Omega[R;E_i].
\]

于是 centered hypotheses：

\[
H_i=K+\Omega_i.
\]

---

## 1. Epistemic-inertness condition

定义一组主体可获得 evidence：

\[
\mathcal E(K).
\]

若 \(\Omega\) 不改变任何 evidence-bearing variable，则对任意 \(i,j\)：

\[
\boxed{
\mathcal E(H_i)=\mathcal E(H_j).
}
\]

概率版本：对任意 possible evidence \(e\)：

\[
\boxed{
P(e\mid H_i)=P(e\mid H_j).
}
\]

这比单纯：

\[
\Omega\not\Rightarrow\Delta Phen
\]

更强；它要求 absolute status 对 cognition / memory / introspection / reports 等全部 epistemically usable channels 都 inert。

---

## 2. Likelihood-Indifference Result

若：

\[
P(e\mid H_i)=P(e\mid H_j)
\]

则 Bayes factor：

\[
BF_{ij}(e)
=
\frac{P(e\mid H_i)}{P(e\mid H_j)}
=1.
\]

因此 posterior odds：

\[
\frac{P(H_i\mid e)}{P(H_j\mid e)}
=
\frac{P(H_i)}{P(H_j)}.
\]

也就是说：

\[
\boxed{
\text{任何这类 evidence 都不会把 orientation odds 从 prior 推向某个 center。}
}
\]

这不是要求 priors 必须相等。

它只说明：**如果 absolute orientation 对 evidence 完全 inert，那么 experience / observation 不能成为 center-discriminating evidence。**

暂称 **Absolute-Orientation Likelihood Indifference (AOLI)**。

---

## 3. Perfect-Swap version

最清楚的 thought experiment：

\[
H_A=K+\Omega(A),
\]

\[
H_B=K+\Omega(B),
\]

其中：

\[
K_A=K_B=K.
\]

Alice 在两个 hypotheses 中拥有完全相同：

- conscious experience；
- sense of mineness；
- memory；
- thought “I am here”；
- certainty that she is conscious；
- report “this experience is directly present”。

Bob 也一样。

若 Alice 的 total evidence：

\[
e_A
\]

在 \(H_A,H_B\) 中相同，则：

\[
P(e_A\mid H_A)=P(e_A\mid H_B).
\]

所以 Alice 的 ordinary introspection 不能告诉她：

\[
\Omega(A)
\]

还是：

\[
\Omega(B).
\]

同理 Bob。

---

## 4. 这比 “phenomenally inert” 更强在哪里

旧 fork：

### Active

\[
\Omega\Rightarrow\Delta Phen.
\]

### Inert

\[
\Omega\not\Rightarrow\Delta Phen.
\]

但即使没有 phenomenal difference，理论还可能声称：

- direct non-phenomenal acquaintance；
- primitive self-intimation；
- special rational entitlement；
- non-causal epistemic relation。

所以真正 epistemic result 需要检查的是：

\[
\boxed{
\Omega\Rightarrow\Delta Evidence?
}
\]

若否，AOLI 成立。

若是，则理论必须把该 evidence channel 明确加入 ontology。

---

## 5. Builes 的 escape route 恰好落在 active horn

Builes 在回应 First-Person Realism skeptical objection 时提出：若 privileged person's mental states 真和 others 不同，则 privileged person 可以通过知道自己的 mental states 而知道 privilege。

结构是：

\[
\boxed{
\Omega(E^*)
\Rightarrow
MentalSignature(E^*)
\Rightarrow
Know(\Omega(E^*)).
}
\]

这说明一种清楚的 epistemic rescue 确实存在。

但 MAO 当前默认 ordinary phenomenal equality：

\[
Phen(E^*)\approx Phen(E_i).
\]

若再扩成 mental/cognitive equality，Builes rescue 被关闭。

所以 MAO 不能同时轻易拥有：

1. perfect ordinary mental symmetry；
2. straightforward introspective knowledge of absolute status。

---

## 6. Local-Signature Replication Problem

假设理论为了恢复 knowledge，引入一个 locally readable signature：

\[
Sig(E).
\]

并：

\[
Sig(E)\Rightarrow Evidence(Absolute(E)).
\]

若 signature supervenes on可复制 local phenomenal / neural / cognitive profile：

\[
Sig(E)=f(N(E)),
\]

perfect duplicates：

\[
N(E_A)\cong N(E_B)
\]

给：

\[
Sig(E_A)=Sig(E_B).
\]

于是 signature 不能唯一识别 absolute center。

所以：

\[
\boxed{
\text{ordinary locally readable epistemic signature faces the same duplication no-go as liveness selectors}.}
\]

---

## 7. Absolute-Orientation Epistemic Trilemma

若希望 absolute status 同时：

- singular；
- compatible with genuine duplicate minds；
- knowable from first person，

大体出现三条路线。

### E1 — Epistemically inert

\[
\Omega\not\Rightarrow\Delta Evidence.
\]

结果：AOLI；orientation identity 无法由 experience / observation discriminatively确认。

### E2 — Locally epistemically active

\[
\Omega\Rightarrow Sig_{local}(E^*).
\]

结果：需要 non-replicating local mental difference；否则 duplication 让 signature 复制。

这会迫使 privileged subject 与 others 的 ordinary mental states 不完全同型。

### E3 — Sui generis absolute acquaintance

增加：

\[
Acq_{abs}(S^*,\Omega).
\]

它不 supervene on ordinary mental profile，并只属于 absolute center。

这可以原则上给 knowledge，但新 relation 本身已经是 absolute-sensitive primitive structure。

于是来源问题改写成：

\[
\boxed{
Why\ Acq_{abs}(S^*,\Omega)\text{ only here?}
}
\]

它并没有消除 absolute asymmetry；只是把 asymmetry 从 orientation ontology 延伸到 epistemology。

因此：

\[
\boxed{
\text{silence}
\;|\;
\text{unique mental signature}
\;|\;
\text{primitive absolute acquaintance}.
}
\]

暂称 **Absolute-Orientation Epistemic Trilemma**。

---

## 8. Reliability pressure

若所有 ordinary subjects 都由于 identical local first-person architecture 而形成：

\[
Bel_i(Absolute(i)),
\]

但实际：

\[
\exists!i^*\;Absolute(i^*),
\]

则除一个以外其余 beliefs false。

若 absolute subject 的 belief mechanism 与 others 在 common core 中同型：

\[
Mechanism_{i^*}\cong Mechanism_j,
\]

则该 mechanism 本身不能解释为什么 absolute subject 的 belief reliable 而其他人的不可靠。

因此 active epistemology还需要：

\[
\boxed{
\text{truth-sensitive asymmetry in the epistemic mechanism itself}.}
\]

否则只是 lucky true belief。

这把 epistemic problem 与 source problem 再次绑定。

---

## 9. 对原始“绝对感”的裁决

若所有 subjects 都有 ordinary：

\[
ForMe+Mineness+DirectGivenness,
\]

那么这些 features 不能独立区分：

\[
H_i=K+\Omega_i.
\]

所以当前 subject 的强烈：

> “这里就是绝对在场。”

有三种可能：

1. 它只是 common-core first-person phenomenology → 不区分 \(\Omega\)；
2. 它包含 unique mental signature → 必须具体描述并通过 duplication test；
3. 它是 sui generis absolute acquaintance → 理论明确增加 primitive epistemic asymmetry。

不能只用词语 “absolute feeling” 模糊三者。

---

## 10. 对 Minimal Absolute Opening 的当前推荐

最稳定版本仍是：

\[
\boxed{
\Omega\text{ is epistemically inert with respect to ordinary evidence}.
}
\]

这样可以保留：

- genuine other minds；
- perfect duplicates；
- no unique phenomenal quale；
- no ad hoc cognitive mark。

但必须坦率接受：

\[
\boxed{
\text{我们没有 ordinary evidential route 确认谁是 }E^*.
}
\]

甚至更强：若 AOLI 条件完整成立，普通 evidence 不会提高某一 orientation hypothesis 相对 permutation alternatives 的概率。

所以 MAO 的证据地位会从：

> directly introspectively evident

降为：

> metaphysical hypothesis motivated by a vertiginous intuition but not discriminatively confirmed by that intuition alone。

---

## 11. 对整个项目的影响

这形成一个新的 endgame gate：

\[
\boxed{
\text{Absolute layer must either earn an epistemic signature or accept evidential silence.}
}
\]

于是 `self` 的两个问题正式分离：

### Ontology

\[
Does\ \Omega\ exist?
\]

### Orientation epistemology

\[
How\ could\ any\ subject\ know\ which\ E\ bears\ \Omega?
\]

后者不能再被“因为我就在这里体验”直接回答，因为 ordinary for-me-ness 在 competitor subjects 中也存在。

## 文献连接

- David Builes, “Eight Arguments for First-Person Realism” (2024), DOI `10.1111/phc3.12959`。
- David Builes, “Center indifference and skepticism” (2024), DOI `10.1111/nous.12478`。
- [`absolutization-epistemic-fork.md`](absolutization-epistemic-fork.md)
- [`locality-duplication-no-go.md`](locality-duplication-no-go.md)
- [`../models/minimal-absolute-opening.md`](../models/minimal-absolute-opening.md)
- [`../../literature/builes-2024-center-indifference-epistemic.md`](../../literature/builes-2024-center-indifference-epistemic.md)
