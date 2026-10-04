# 文献获取流水线

`self` 的文献层分成两部分：

- `index.md` 与专题笔记：人工整理后的研究地图；
- `candidates/` 与 `records/`：机器检索得到的候选和结构化记录。

机器检索只负责发现、去重、排序和保存来源证据。候选论文不会因为自动评分较高就自动进入项目立场。

## 数据源

### OpenAlex

主发现源。适合跨哲学、物理、数学和认知科学检索，也提供引用关系、开放获取位置与语义检索。

环境变量：

```text
OPENALEX_API_KEY
```

API key 可选；需要较高调用额度时再配置。

### Semantic Scholar

用于第二路语义检索，以及从 seed paper 向前追 references、向后追 citations。

环境变量：

```text
SEMANTIC_SCHOLAR_API_KEY
```

key 可选，但配置后更适合稳定批量使用。

### Crossref

用于 DOI 和正式出版元数据交叉核验。它不承担主要的语义发现任务。

环境变量：

```text
CROSSREF_MAILTO
```

可选；配置后进入 Crossref polite pool。

### PhilPapers

继续作为哲学领域的人工导航和分类校准源。目前不把它放入自动 API 流水线，因为缺少与 OpenAlex / Crossref 同等级的稳定公共检索接口。

## 使用

全部代码只依赖 Python 标准库。

搜索：

```bash
python tools/literature.py search "first person metaphysical privilege subjectivism" \
  --semantic \
  -o literature/candidates/first-person.json \
  --markdown literature/candidates/first-person.md
```

运行项目预设查询：

```bash
python tools/literature.py batch
```

沿某篇 seed paper 的后续引用扩展：

```bash
python tools/literature.py expand "Against Egalitarianism" \
  --direction citations \
  -o literature/candidates/hellie-citations.json \
  --markdown literature/candidates/hellie-citations.md
```

查看它引用的更早研究：

```bash
python tools/literature.py expand "Against Egalitarianism" \
  --direction references
```

## `triage_score`

自动结果会得到一个 `triage_score`。它综合：

- 多个索引是否同时找到同一作品；
- 引用数量的对数尺度信号；
- DOI、期刊/来源、年份等元数据完整度；
- 是否存在开放获取链接；
- 在各检索源中的相对排名。

它只是阅读优先级，不是论文质量分，更不是理论真值分。

尤其在哲学研究中，新论文、少数派观点和书籍可能引用数很低，但仍可能直接击中核心问题。

## 从 candidate 到正式文献

一篇候选进入 `literature/` 前，AI 应完成以下检查：

1. **身份核验**：确认标题、作者、年份、DOI/正式出版版本，避免预印本与正式版重复。
2. **全文层级**：明确自己读到了全文、摘要，还是只有元数据；摘要不能支撑对细节论证的断言。
3. **来源质量**：记录期刊、学术出版社、同行评审状态或其他可信出版背景。
4. **引用上下文**：至少检查关键 seed 的 references/citations，避免把孤立论文当成整个领域共识。
5. **项目相关性**：明确它具体影响哪个问题、论证或模型。
6. **反方优先**：对当前立场构成强反例或替代理论的工作，不因结论不合意而降权。
7. **人工综合**：只有经过阅读和论证比较后，才更新 `index.md`、专题笔记或 `synthesis/`。

## 目录约定

```text
literature/
├── index.md
├── pipeline.md
├── queries.json
├── candidates/        # 自动发现结果；可重新生成
├── records/           # 已核验的机器可读文献记录
└── *.md               # 人工研究笔记

tools/
└── literature.py
```

`records/` 的格式见 `records/schema.json`。结构化记录和 Markdown 笔记可以并存：前者方便 AI 和程序读取，后者保存真正的哲学分析。
