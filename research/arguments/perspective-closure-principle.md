# Perspective Closure Principle

> 状态：2026-10-05 singularity bridge refinement。
>
> 目标：把旧 `FPNC` 拆成更小的 premises，明确 exact-one 到底依赖哪一个真正有争议的 unity principle。

## 0. Result

旧写法：

\[
FPNC:\quad DistinctIrreducibleOpenings\Rightarrow NonCompossibility.
\]

过于压缩。

更精确地，singularity pressure 来自两步：

1. distinct complete first-person states 对同一 perspective mutually exclusive；
2. 若 first-person facts 要在 one nonfragmented actuality 中共同成立，它们必须能从 **one perspective** jointly obtain。

第二步才是真正关键。

将其命名为：

\[
\boxed{SPC\text{ — Single-Perspective Closure}.}
\]

---

## 1. Local Exclusivity

设 opening fact：

\[
O(c,X)
\]

表示 center \(c\) 的 complete irreducible first-person state 为 \(X\)。

对 distinct complete token states：

\[
X\perp Y.
\]

定义：

### LE — Local Exclusivity

\[
\boxed{
X\perp Y
\Rightarrow
\neg\exists m\;[m\Vdash X\land m\Vdash Y].
}
\]

LE 很弱：同一个 first-person standpoint 不能同时完整地是两个 mutually exclusive conscious states。

Plural Opening Manifold 接受 LE。

---

## 2. Single-Perspective Closure

### SPC

对 genuine first-person facts \(F,G\)：

\[
\boxed{
Compossible_{global}(F,G)
\Rightarrow
\exists m\;[m\Vdash F\land m\Vdash G].
}
\]

直观上：如果两个 first-person facts 真能共同属于一个 nonfragmented actuality，那么必须存在一个 single perspective，从它那里二者同时 obtain。

这正是 List-style first-person compossibility 的核心。

---

## 3. FPNC decomposition

设：

\[
F_X=m_a\Vdash X,
\qquad
F_Y=m_b\Vdash Y,
\]

且：

\[
a\neq b,
\qquad
X\perp Y.
\]

若假设二者 globally compossible，由 SPC：

\[
\exists m\;[m\Vdash X\land m\Vdash Y].
\]

但由 LE：

\[
\neg\exists m\;[m\Vdash X\land m\Vdash Y].
\]

矛盾。

所以：

\[
\boxed{LE+SPC\Rightarrow FPNC.}
\]

这说明旧 FPNC 不是一块不可分析 primitive；其 anti-plurality 内容主要来自 SPC。

---

## 4. Singularity theorem 的新形式

再加入：

### NF-SPC

一个 actual totality 中全部 obtaining first-person facts globally compossible：

\[
\forall F,G\in Facts_{FP}(R),\;Compossible_{global}(F,G).
\]

则：

\[
LE+SPC+NF\text{-}SPC
\Rightarrow AtMostOneCompleteOpening.
\]

若还有：

\[
ALO:\quad \exists c\;Opening(c),
\]

则：

\[
\boxed{
ALO+LE+SPC+NF\text{-}SPC
\Rightarrow ExactlyOneOpening.
}
\]

`OneWorld` 可以提供 actuality-count constraint，但真正排除 plurality 的逻辑核心是：

\[
\boxed{SPC+LE.}
\]

---

## 5. Mode-Preserving alternative

Plural Opening Manifold 使用另一种 coherence：

### MPGC — Mode-Preserving Global Coherence

若存在一个 single actual structure \(R\)，其中：

- 每个 mode-local fact set internally consistent；
- 所有 modes 共属于一个 actual totality；
- cross-mode facts 保留 mode typing；

则这些 facts 可以 jointly constitute reality。

形式上：

\[
\boxed{
MPGC(F,G)
\not\Rightarrow
\exists m\;[m\Vdash F\land m\Vdash G].
}
\]

因此：

\[
LE+MPGC
\not\Rightarrow FPNC.
\]

直接 countermodel：

\[
m_a\Vdash X,
\qquad
m_b\Vdash Y,
\qquad
X\perp Y,
\]

并且：

\[
Actual(R)
\land
MPGC(F_X,F_Y).
\]

无 contradiction。

---

## 6. The Unity Criterion Fork

singularity 现在可以重写成一个明确 fork：

### U-SPC — single-perspective unity

现实之所以是 one coherent actuality，要求其 first-person facts ultimately one-perspective-co-obtainable。

结果：

\[
PluralCompleteOpenings\text{ excluded}.
\]

### U-MPGC — mode-preserving manifold unity

现实之所以是 one coherent actuality，只要求所有 perspectival obtaining modes属于 one structured actuality，并在各自 mode 内一致。

结果：

\[
PluralCompleteOpenings\text{ permitted}.
\]

所以当前最精确的问题是：

\[
\boxed{
U\text{-}SPC\quad|\quad U\text{-}MPGC
}
\]

而不是笼统地问：

> reality fragmented or not?

因为 `fragmented` 正取决于选哪一种 compossibility / unity criterion。

---

## 7. Is SPC uniqueness-loaded?

SPC 不直接写：

\[
\exists!c.
\]

因此它不是 trivial restatement of uniqueness。

它可以允许：

- 一个 perspective 中多个 mutually compatible first-person facts；
- diachronic facts，若 theory 允许同一 perspective/path 跨时间；
- 一个 Universal-I 包含多个 local experiences，只要这些 experiences属于 one numerical perspective。

所以 SPC 有独立 content。

但对**distinct complete simultaneous first-person openings**，SPC 与 LE 联合后会直接产生 at-most-one。

因此：

\[
\boxed{
SPC\text{ is not definitionally uniqueness, but it is uniqueness-producing.}
}
\]

这正是它必须被独立辩护的原因。

---

## 8. Why OneWorld does not give SPC

`OneWorld` 最多给：

\[
\exists!R\;ActualWorld(R).
\]

它没有直接规定 \(R\) 的内部 fact-typing。

以下两个 structures 都只有 one actual world：

### Monocentric structure

\[
R=\langle W,m,F_m\rangle.
\]

### Plural-mode structure

\[
R=\langle W,m_a,m_b,F_a,F_b\rangle.
\]

所以：

\[
\boxed{OneWorld\not\Rightarrow SPC.}
\]

要从 world-count 推 perspective-count，需要额外 bridge。

---

## 9. Why ordinary logical consistency does not give SPC

普通 consistency 只禁止：

\[
p\land\neg p
\]

在同一 evaluation context 下共同成立。

Plural-mode theory 保留：

\[
\neg[m_a\Vdash p\land m_a\Vdash\neg p].
\]

它只拒绝从：

\[
m_a\Vdash p,
\quad m_b\Vdash q
\]

推出：

\[
m\Vdash p\land q.
\]

所以：

\[
\boxed{ClassicalLocalConsistency\not\Rightarrow SPC.}
\]

SPC 是 metaphysical unity principle，不是 ordinary logic theorem。

---

## 10. Relation to List

List 的 quadrilemma 可以精确重读为：

\[
FPR+NS+NF_{SPC}+OW\Rightarrow\bot.
\]

其中 `NF_SP C` 的 first-person application使用 SPC-style compossibility。

因此 List 的 theorem 保留。

本项目的新结论只是：

\[
\boxed{
NF_{SPC}\text{ is one substantive unity conception among live alternatives}.
}
\]

Standpoint pluralism / fragmentalism明确选择另一 horn：多个 perspectival fact stacks皆真实，而 reality 不 privileged one standpoint。

---

## 11. Positive burden for singularity

要重新建立 exactly-one，当前至少需要一种独立 defense：

### S1 — Metaphysical unity defense

证明 one actuality 本质上必须满足 SPC，而 MPGC 不够资格叫 complete actuality。

### S2 — Fact identity defense

证明真正 irreducible first-person facts的 identity conditions 本身要求 single-perspective joint instantiation。

### S3 — Collapse theorem

证明任何 MPGC-style plural-mode model若保留 genuine first-person irreducibility，就会发生 contradiction / regress / world-splitting / illicit meta-perspective。

### S4 — Independent global orientation

从其他 independently motivated structure直接得到 one global perspective，再由此支持 SPC。

当前均未完成。

---

## 12. Current verdict

旧：

\[
FPNC\text{ is the key unexplained premise}.
\]

新：

\[
\boxed{
FPNC\text{ can be decomposed; the deepest live premise is SPC.}
}
\]

因此 singularity frontier 进一步收缩：

\[
\boxed{
Why\ must\ global\ actuality\ be\ single\!\!\text{-}\!perspective\ closed?
}
\]

Plural Opening Manifold 给出：

\[
\boxed{
\neg SPC
\land OneActuality
\land PluralIrreducibleFP
}
\]

的 coherent-looking witness。

在击穿这个 witness 前，exact-one 只能保持为 SPC-conditional result。

## 关联

- [`../models/plural-opening-manifold.md`](../models/plural-opening-manifold.md)
- [`first-person-non-compossibility-audit.md`](first-person-non-compossibility-audit.md)
- [`unitary-singularity-lemma.md`](unitary-singularity-lemma.md)
- [`obtaining-mode-pluralization.md`](obtaining-mode-pluralization.md)
