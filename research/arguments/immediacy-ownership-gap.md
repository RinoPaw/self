# Immediacy–Ownership Gap

> 状态：2026-10-05 Universalism pressure test。
>
> 目标：检验 Universalism 的核心推理 `all experience is immediate -> all experience is mine` 是否有效，还是把 for-me-ness、mineness 与 subject-ownership 混在一起。

## 0. Universalist chain

Zuboff / Builes-style Universalism最核心可写成：

\[
Experience(e)
\Rightarrow
Immediate(e)
\Rightarrow
Mine(e).
\]

第一箭头：任何 experience qua experience 都是 live / immediate / given / for-me。

第二箭头：这种 immediacy 足以说明 experience 是 `mine simpliciter`。

由此：

\[
\boxed{\forall e\,[Experience(e)\to Mine(e)]}.
\]

本审计只攻击第二箭头。

---

## 1. Guillot distinction

Marie Guillot 区分：

### For-me-ness

experience 对某 subject 显现 / 有 something-it-is-like-for-S 的结构。

### Me-ness

subject自身在 experience 中以某种方式显现。

### Mineness

experience 被体验为 **my own**。

关键：

\[
\boxed{ForMeNess\not\Rightarrow MeNess}
\]

且：

\[
\boxed{ForMeNess\not\Rightarrow Mineness}.
\]

因此即使：

\[
\forall e\;ForMeNess(e),
\]

也不能直接推出：

\[
\exists I_U\;\forall e\;Mine_I(e).
\]

这就是 **Immediacy–Ownership Gap**。

---

## 2. The index problem

更精确地说，local for-me-ness 更自然写：

\[
For(e,S_e).
\]

Universalism需要把所有局部 subject-index消掉：

\[
\forall e\;For(e,S_e)
\quad\Rightarrow\quad
\forall e\;Mine_I(e).
\]

但中间缺：

\[
\boxed{\forall e\;S_e=I}.
\]

所以从 universal immediacy到 universal I 需要一个 **Subject-Identity Bridge**：

### SIB

\[
\boxed{
For(e_i,S_i)\land For(e_j,S_j)
\Rightarrow
S_i=S_j.
}
\]

而这个原则显然不是由 `for-me-ness` 概念自动给出。

因此 Zuboff-style move：

\[
\text{all experience is immediate}
\to
\text{all experience is mine}
\]

真正隐藏的是：

\[
\boxed{\text{local first-person indices collapse into one universal subject-index}.}
\]

这正需要独立论证。

---

## 3. Nida-Rümelin: subjective character back to subject-properties

Nida-Rümelin 2023 明确主张：experience-property framework 中关于 subjective character 的真理，可以翻译回更基础的 subject-property framework。

典型 translations：

\[
ForMe(e)
\Rightarrow
\exists S\;Subject(S)\land Undergoes(S,e).
\]

更强 readings还包括：

\[
AwareOfHaving(S,e),
\]

\[
AwareOfSelfAsBearer(S,e),
\]

\[
SeemsOwn(S,e).
\]

这提供 **Local Ownership Principle (LOP)** 的 serious precedent：

\[
\boxed{
SubjectiveCharacter(e)
\Rightarrow
\exists S\;Bearer(S,e).
}
\]

它不证明 bearer必须 ordinary organism，也不证明 different experiences必有 different subjects；但它直接反对 `mine` 完全漂浮成无 bearer 的 abstract quality。

---

## 4. Schlicht: from mineness to subject

Schlicht 2018 直接提出：若接受 conscious experience具有 mineness，这可提供 minimal notion of a subject of experience。

其 preferred route进一步把 phenomenal subject 与 organism联系。

对本项目最重要的不是 organism conclusion，而是结构：

\[
\boxed{Mineness\Rightarrow SubjectCommitment}
\]

至少是严肃哲学选项。

这正打 Builes 的 U-M horn：

\[
UniversalMine\ without\ UniversalBearer.
\]

若 mineness本身要求 bearer，则 U-M不能靠删除 subject ontology轻易逃出 subject-unity pressure。

---

## 5. Fasching: presence as dimension of one experiential realm

Fasching 的 local dimensional account同样支持 bearer/dimension structure：

\[
D_I=\text{dimension of first-personal manifestation}.
\]

experiential contents在：

\[
D_{I_1},D_{I_2},\ldots
\]

这样的 presence dimensions 中获得 manifestness。

因此：

\[
Presence(e)
\]

并非天然等于 anonymous universal immediacy；可以被分析成：

\[
PresentIn(e,D_{I_i}).
\]

这提供一个直接 countermodel to Zuboff inference：

\[
\forall e\;Presence(e)
\]

但：

\[
\neg\exists!I_U\;\forall e\;PresentIn(e,D_{I_U}).
\]

---

## 6. Universalism's strongest reply

Universalist可以说：

- `For(e,S)` 已经错误地把 subject-index放入分析；
- experience 的最原始形式只有：

\[
Immediate(e),
\]

- ordinary local subjects是 access/causal organization的后设产物；
- universal `I` 不是从 local subjects identity 得出，而是从 immediacy的数值同一性得出。

这正是 Zuboff 的路线。

因此本 gap 不是 refutation；它迫使 Universalism承担一个更明确的本体论 thesis：

### Immediacy Identity Thesis (IIT-U)

\[
\boxed{
\forall e_i,e_j\;ImmediateToken(e_i)=ImmediateToken(e_j)
}
\]

或至少：

\[
\boxed{\text{all immediacies instantiate one numerically identical first-person universal}.}
\]

没有这一步，Universalism只有：

\[
\forall e\;Immediate(e)
\]

而不是：

\[
\forall e\;Mine(e).
\]

---

## 7. Type/Token danger

Zuboff 通过 universal/type ontology说：不同 brains / times可以 instantiate numerically one experience/self universal。

但这里必须区分：

\[
SamePropertyType(Immediate)
\]

与：

\[
SameSubjectToken(I).
\]

从：

\[
\forall e\;Instantiates(e,Immediacy)
\]

不能自动推出：

\[
\exists!I\;SubjectOf(I,e_1,e_2,\ldots).
\]

否则类似：

\[
\forall red\ object\;Instantiates(Redness)
\]

会错误推出它们是一个 object。

Zuboff尝试通过 experience/self的特殊逻辑避免这种类比，但 burden必须明确记录：

\[
\boxed{
SharedFirstPersonUniversal
\not\Rightarrow
OneNumericalSubjectToken
}
\]

除非补充 identity theory。

---

## 8. Consequence for Universal-I fork

此前 Universalism二叉：

\[
U\text{-}S:\ OneUniversalSubject
\quad|\quad
U\text{-}M:\ UniversalMineWithoutBearer.
\]

现在进一步：

### U-S

必须解释：

\[
PhenomenalDisunity+OneSubject
\]

与 subject-unity literature的冲突。

### U-M

必须解释：

\[
Immediacy\to Mine
\]

并跨过本文件的 Immediacy–Ownership Gap。

所以：

\[
\boxed{
Universalism\text{ cannot get one universal I merely from universal for-me-ness}.}
\]

---

## 9. What this gives the selective-opening side

这还没有证明：

\[
\exists!E^*\;Absolute(E^*).
\]

但它阻止一个过快的反论证：

> “所有 experience都有 first-person immediacy，所以它们必然都是同一个 I 的 experience。”

正确结论最多是：

\[
\boxed{
Experience\to ForMeNess
}
\]

然后仍要选择：

\[
\boxed{
\text{LocalBearerPlurality}
\;|\;
\text{UniversalBearerIdentity}
\;|\;
\text{BearerlessImmediacy}.
}
\]

这恢复了本项目的理论空间。

更重要的是，新的正方目标变得可操作：

### LOP

\[
SubjectiveCharacter(e)\Rightarrow\exists S\;Bearer(S,e).
\]

### CUP

\[
SameSubject(e_i,e_j)\Rightarrow CoConscious(e_i,e_j).
\]

若两者共同成立，则 Universal-I受到显著压力。

---

## 10. Current verdict

Builes/Zuboff 的 strongest intuition：

\[
\boxed{\text{all experience is immediate}}
\]

仍然非常强，也与 phenomenology 广泛相容。

但：

\[
\boxed{
UniversalImmediacy
\not\Rightarrow
UniversalOwnership
}
\]

现在有明确文献支持的 conceptual reason：

\[
ForMeNess\neq Mineness\neq SubjectIdentity.
\]

所以 Universalism真正需要的，不是再证明 immediacy，而是证明：

\[
\boxed{
\text{the first-person index carried by every experience is numerically one and the same}.}
\]

这成为下一轮最精确的 Universal-I burden。

## Sources

- Marie Guillot, “I Me Mine: on a Confusion Concerning the Subjective Character of Experience”, *Review of Philosophy and Psychology* 8, 2017, 23–53, DOI `10.1007/s13164-016-0313-4`.
- Martine Nida-Rümelin, “Experiencing Subjects and So-Called Mine-Ness”, in *Self-Experience: Essays on Inner Awareness*, OUP, 2023.
- Tobias Schlicht, “Experiencing organisms: from mineness to subject of experience”, *Philosophical Studies* 175(10), 2018, 2447–2474, DOI `10.1007/s11098-017-0968-4`.
- Wolfgang Fasching, “The mineness of experience”, *Continental Philosophy Review* 42(2), 2009, 131–148.
