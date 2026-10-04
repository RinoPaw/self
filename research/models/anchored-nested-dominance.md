# Anchored Nested Dominance

> 状态：Nested Dominance Architecture 的第二版工作模型。
>
> 目的：把 top whole、perspective、anchoring、competition、winner、intrinsic realization 与 absolute privilege 分开，避免一个模糊的 `D_top` 同时承担全部解释负担。

## 0. 总结构

把候选现实结构写成：

\[
\boxed{
\mathcal R^+
=
\langle
W,\Pi,\rho,U_{\max},\mathfrak D,\preceq,d,H
\rangle
}
\]

其中：

- \(W\)：objective / third-person world structure；
- \(\Pi\)：first-person perspective / locus 集合；
- \(\rho\)：perspective 到客观意识事件的 anchoring relation；
- \(U_{\max}\)：若存在，唯一最大 / fundamental whole；
- \(\mathfrak D\)：experiential / dominance domains；
- \(\preceq\)：domain hierarchy；
- \(d\)：single-output dominance operator；
- \(H\)：structural role 与 intrinsic realizer 之间的 horizontal / inside-out realization relation 候选。

这套结构不预设 absolute center 已经存在。

---

## 1. 普通第一人称层

对每个 ordinary subject：

\[
\pi_i\in\Pi
\]

并有：

\[
\rho(\pi_i)=E_i.
\]

局部 experiential domain \(D_i\) 的 dominant perspective：

\[
d(D_i)=\pi_i.
\]

于是：

\[
FP(\pi_i,E_i)
\]

可对多个主体同时成立。

这一层只解释普通 first-person locus，不承担 global absolute privilege。

---

## 2. Top whole 与 top competition domain 分离

即使存在唯一：

\[
U_{\max},
\]

也不能直接写：

\[
U_{\max}=D_{\top}.
\]

Priority monism 只支持一种 top-whole / basic-whole 结构；它没有自动提供跨全部意识主体的 competition relation。

因此必须显式给出：

\[
C:U_{\max}\mapsto D_{\mathrm{comp}}
\]

并解释 \(C\) 的本体论意义。

需要：

\[
\forall \pi_i\in\Pi_{eligible},
\quad
\pi_i\in D_{\mathrm{comp}}.
\]

这叫 **Competition Closure**。

---

## 3. 顶层 singleton

若存在一个 global competition domain：

\[
D_{\mathrm{comp}},
\]

且 dominance operator 真正 single-output：

\[
d(D_{\mathrm{comp}})=\pi^*,
\]

则得到一个 global winner perspective。

通过 anchoring：

\[
E^*=\rho(\pi^*).
\]

所以：

\[
\boxed{
D_{\mathrm{comp}}
\xrightarrow{d}
\pi^*
\xrightarrow{\rho}
E^*
}
\]

这一步解决的是 singleton location，仍没有自动得到 absolute liveness。

---

## 4. No-New-Subject Requirement

2025/26 关于 overlapping consciousness 的新争论使 Nested Dominance 必须明确：top-level role 不应构成一个新的 larger conscious subject，再把局部 \(E^*\) 包含进去。

否则可能产生：

\[
S_{local}\subset S_{top}
\]

式 phenomenal overlap / subject overlap。

因此当前优先要求：

\[
\boxed{
TopDominance(\pi^*)
\text{ modifies the status of an existing local perspective rather than creating a new subject}
}
\]

形式上：

\[
d(D_{\mathrm{comp}})=d(D_k)=\pi^*.
\]

同一个 perspective 获得两种 domain-role：

- local dominance；
- global dominance。

不额外产生：

\[
\pi_{cosmic}.
\]

---

## 5. 为什么 Superpsychism 是重要反例

Schneider–Bailey 2026 的 Superpsychism 显示：

\[
\text{unique fundamental top structure}
+
\text{consciousness}
\]

可以直接得到一种 top-level superconsciousness。

普通 minds 则作为 emergent / decohered projections 出现。

这说明：

\[
\boxed{
\text{conscious top domain naturally tends toward a cosmic subject}
}
\]

而本项目想要的是：

\[
\boxed{
\text{top status localized onto an already existing finite perspective}
}
\]

两者不是同一任务。

因此引入：

\[
\boxed{\text{Top-Winner Localization Requirement}}
\]

要求 top role 的 carrier 必须来自 local perspective inventory：

\[
\pi^*\in\{d(D_i)\}.
\]

---

## 6. Centered-world pressure

即使 \(U_{\max}\) 唯一，同一个 uncentered totality 仍可能允许多个：

\[
\pi_1,\pi_2,\dots
\]

因此：

\[
U_{\max}\not\Rightarrow\pi^*.
\]

Top competition relation \(D_{\mathrm{comp}}\) 必须真正包含能够区分 / 比较这些 perspectives 的结构，而不能只继承 top whole 的唯一性。

对应：[`../arguments/top-domain-center-gap.md`](../arguments/top-domain-center-gap.md)。

---

## 7. Anchoring pressure

即使知道：

\[
W
\]

和：

\[
\Pi,
\]

还要处理：

\[
\rho:\Pi\to\mathcal E(W).
\]

因此 top winner 的物理 / 时空 location 不是免费得到：

\[
\pi^*\xrightarrow{\rho}E^*.
\]

如果 \(\rho\) 本身是 primitive haecceitistic matching，项目的“由完整结构推出”目标会受损。

对应：[`../arguments/anchoring-correlation-gap.md`](../arguments/anchoring-correlation-gap.md)。

---

## 8. Role–Realizer Bridge：horizontal grounding 候选

此前 Priority–Liveness Gap 是：

\[
TopDominant(\pi^*)
\not\Rightarrow
LIVE_{simpliciter}(\pi^*).
\]

Merlo 的 panquidditist monism 提供一个可以借用的结构思想：区分

- vertical grounding：从下层解释一个角色；
- horizontal grounding：从“内部”解释该角色由什么 intrinsic realizer 实现。

于是可以把 top dominance 写成：

\[
R_{\top}(\pi^*)
\]

并要求存在一个 intrinsic realizer：

\[
H(q_{\top},R_{\top}).
\]

理想情况下：

\[
q_{\top}\text{ is experiential / manifestation-relevant}.
\]

这提供一个比“最高 rank 因此最 live”更有内容的桥：

\[
\boxed{
\text{global structural role}
+
\text{intrinsic phenomenal/manifestational realizer}
}
\]

---

## 9. Role–Realizer 路线的三个风险

### 9.1 Cosmic Experience Risk

若 \(q_{\top}\) 是 top domain 本身的 phenomenal nature，则容易得到：

\[
S_{cosmic}
\]

而非 local \(E^*\)。

### 9.2 Primitive-Realizer Risk

若只是规定：

\[
q_{\top}=\text{absolute liveness}
\]

则只是把 primitive LIVE 改名成 quiddity / intrinsic realizer。

### 9.3 Double-Phenomenology Risk

若 \(\pi^*\) 已有 local phenomenal content，而 \(q_{\top}\) 又构成一个新的 phenomenal field，则可能重新触发 overlap / content explosion。

因此最安全的候选必须满足：

\[
\boxed{
q_{\top}\text{ affects actuality/status without introducing a second phenomenal subject or extra cosmic content}
}
\]

目前没有成熟理论做到这一点。

---

## 10. Phenomenal Powers 的启发

Mørch 的 phenomenal powers 路线提供一个邻近思想：phenomenal property 不只是 inert qualitative item，而可以与 causal power / grounding role 内在关联。

这证明：

\[
\text{phenomenality}
\]

与：

\[
\text{structural / causal role}
\]

不必永远是外在拼接。

对本项目而言，它支持继续研究：

\[
R_{\top}\leftrightarrow q_{\top}
\]

这种 role–realizer unity。

它没有直接给出：

\[
q_{\top}=LIVE_{simpliciter}.
\]

---

## 11. 当前最小模型

如果把目前所有门槛都写进来，候选绝对中心至少需要：

\[
\mathcal R^+
\Rightarrow
U_{\max}
\]

\[
U_{\max}
\Rightarrow
D_{\mathrm{comp}}
\]

\[
D_{\mathrm{comp}}
\xrightarrow{d}
\pi^*
\]

\[
\pi^*
\xrightarrow{\rho}
E^*
\]

\[
R_{\top}(\pi^*)
\xleftrightarrow{H}
q_{\top}
\]

最终还需要：

\[
\boxed{
q_{\top},R_{\top}
\Rightarrow
LIVE_{simpliciter}(E^*)
}
\]

最后一箭头仍未建立。

---

## 12. 当前评价

Anchored Nested Dominance 比第一版多完成了三件事：

1. 不再把 top whole 当成 top competition domain；
2. 不再把 perspective 与其 objective carrier 自动等同，引入 anchoring relation \(\rho\)；
3. 给 Priority–Liveness Gap 增加了一个 `structural role + intrinsic realizer` 的中间候选。

但最大的突破口依旧是：

\[
\boxed{
\text{是否存在一种 independently motivated }q_{\top}
\text{，既与 top role 内在相关，又只改变 actuality 而不生成第二意识？}
}
\]

如果找不到，Nested Dominance 最终可能只能提供 absolute-center 的形式架构，而无法提供 absolute liveness 的来源解释。

## 文献入口

- David Lewis, “Attitudes De Dicto and De Se” (1979)；
- Robert Stalnaker, work on self-location (2008, 2019)；
- Peter Pagin, “Constructing the World and Locating Oneself” (2017)；
- Christian List, “The many-worlds theory of consciousness” (2023)；
- Nino Kadić, “Monadic panpsychism” (2024)；
- Giovanni Merlo, “Panquidditist Monism” (forthcoming, *Grounding and Consciousness*)；
- Hedda Hassel Mørch, “How Can the Mental Ground the Physical? The Case for Phenomenal Powers Panpsychism” (forthcoming)；
- Hedda Hassel Mørch, “Why Consciousness Can’t Overlap” (2025 draft)；
- Susan Schneider & Mark Bailey, “Superpsychism” (2026).
