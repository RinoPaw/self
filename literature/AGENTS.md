# Literature agent protocol

本目录中的 AI 研究工作遵循以下规则。

1. `literature/index.md` 是人工综合后的文献地图；自动搜索结果只能进入 `literature/candidates/`，不能直接改写项目立场。
2. 开始新的文献调查时，先查看 `queries.json` 和已有专题笔记，再用 `tools/literature.py` 搜索。避免每次从零生成一套不同关键词。
3. 核心论文至少用两个元数据来源交叉核验；有 DOI 时优先用 DOI 消歧。
4. 区分 `metadata-only`、`abstract-read` 与 `fulltext-read`。没有读到全文时，不声称作者在正文中完成了某个细节论证。
5. 引用数只作为发现信号。哲学专著、新论文、少数派理论和直接反方可以在低引用情况下进入最高优先级。
6. 优先追踪论证链：seed paper 的 references、citations、直接回应、批评和作者后续修订，比宽泛关键词堆积更重要。
7. 对当前 `synthesis/` 有压力的反方与替代理论应主动保留。不要根据与项目立场的一致程度排序证据。
8. 新文献经过阅读后，先写专题笔记或结构化 `records/`；确认它改变研究地图后再更新 `index.md`。
9. 任何进入 `synthesis/` 的外部主张都应能追溯到具体文献和实际阅读层级。
10. 当自动源互相冲突时，保留冲突并回到出版社、DOI 注册信息或论文原文核验，不自行猜测。
