# Synthesis 导航

`synthesis/` 保存当前 authority、frontier、handoff 与历史综合。**历史 frontier 不自动代表当前立场。**

## 当前入口

权威优先级：

1. [`current-position.md`](current-position.md) — 当前 authority。
2. [`frontier-2026-10-05-fpnc-accommodation-audit.md`](frontier-2026-10-05-fpnc-accommodation-audit.md) — 最新 frontier；FPNC re-audit + Neutral Accommodation。
3. [`handoff-2026-10-05-fpnc-accommodation.md`](handoff-2026-10-05-fpnc-accommodation.md) — 当前唯一操作交接。

第一次阅读可看：[`core-argument-neutral-vs-centered-actuality.md`](core-argument-neutral-vs-centered-actuality.md)。它是 reader-facing synthesis，不取代 authority。

## 当前终局结构

\[
NeutralActuality\;|\;CenteredActuality
\]

Centered horn：

\[
CenteredActuality\Rightarrow AtLeastOneOpening.
\]

旧版把下一步写成 USL 直接“解决” singularity。现在修正为：

\[
AtLeastOneOpening
\xrightarrow{+FPNC/LFPC+unity\ criterion}
ExactlyOneOpening\;?
\]

`?` 表示形式条件式有效，但 FPNC/LFPC 的独立依据尚未建立。

如果将来 singularity 成立，才继续：

\[
ExactlyOneOpening
\to Locality\;|\;UniversalI
\to DiachronicPath.
\]

## 最新方法论修正

旧 completion witness criterion：

\[
Independent(X)\land N\not\models X\land C\models X
\]

已被判定过弱。

当前使用：

\[
\boxed{
Independent(X)
\land NaturalFit(C,X)
\land \neg CheapNeutralAccommodation(N,X).
}
\]

即候选事实必须抵抗 strongest still-neutral explanation，而不仅是 Neutral baseline 没有把它写成 theorem。

## Frontier 阅读地图

### A. 最新 frontier

- [`frontier-2026-10-05-fpnc-accommodation-audit.md`](frontier-2026-10-05-fpnc-accommodation-audit.md) — 当前最高优先级；supersedes “singularity conditionally solved” 的旧判断。
- [`frontier-2026-10-05-presence-route-closure.md`](frontier-2026-10-05-presence-route-closure.md) — Presence route closure 继续有效，但不再是最新 terminal frontier。

### B. Completion / actuality 前史

- [`frontier-2026-10-05-neutral-baseline.md`](frontier-2026-10-05-neutral-baseline.md)
- [`frontier-2026-10-05-constructive-neutral.md`](frontier-2026-10-05-constructive-neutral.md)
- [`frontier-2026-10-05-centered-actuality.md`](frontier-2026-10-05-centered-actuality.md)
- [`frontier-2026-10-05-role-first-completion.md`](frontier-2026-10-05-role-first-completion.md)
- [`frontier-2026-10-05-actuality-endgame.md`](frontier-2026-10-05-actuality-endgame.md)

这些仍解释为什么主问题收缩成 Neutral vs Centered Completion。

### C. Singularity 历史

- [`frontier-2026-10-05-unitary-singularity.md`](frontier-2026-10-05-unitary-singularity.md)
- [`frontier-2026-10-05-arity-singularity-localization.md`](frontier-2026-10-05-arity-singularity-localization.md)
- [`frontier-2026-10-05-absolute-orientation.md`](frontier-2026-10-05-absolute-orientation.md)

这些记录 USL 如何形成，但其“exact-one no longer primitive / singularity solved”的强解释已由最新 frontier 降级。形式条件式仍保留。

### D. Locality / Universal-I

- [`frontier-2026-10-05-stage-first-opening-universal-i.md`](frontier-2026-10-05-stage-first-opening-universal-i.md)
- [`frontier-2026-10-05-subject-bearer-funnel.md`](frontier-2026-10-05-subject-bearer-funnel.md)
- [`frontier-2026-10-05-universal-centering.md`](frontier-2026-10-05-universal-centering.md)
- [`frontier-2026-10-05-local-opening-presence-monism.md`](frontier-2026-10-05-local-opening-presence-monism.md)

仍有研究史价值，但现在全部 conditional on singularity bridge。

### E. Presence / manifestation

- [`frontier-2026-10-05-self-manifesting-actuality.md`](frontier-2026-10-05-self-manifesting-actuality.md)
- [`frontier-2026-10-05-grounded-centering-ladder.md`](frontier-2026-10-05-grounded-centering-ladder.md)
- [`frontier-2026-10-05-alo-completion.md`](frontier-2026-10-05-alo-completion.md)
- [`frontier-2026-10-05-presence-route-closure.md`](frontier-2026-10-05-presence-route-closure.md)

Presence closure 仍有效：ordinary presence data 不能独立推出 `PresenceSimpliciter`。

## Handoff 规则

当前只使用：

[`handoff-2026-10-05-fpnc-accommodation.md`](handoff-2026-10-05-fpnc-accommodation.md)

旧 `handoff-2026-10-05-terminal-frontier.md` 保留历史价值，但其中 “singularity is conditionally solved” 与旧 R1 entailment criterion 已被 supersede。
