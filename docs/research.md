# 类似项目与本项目的取舍

核对日期：2026-10-02。搜索范围为 GitHub 上的论证审读、事实核查和相关 Agent Skills；找到相近项目，不主张这是完整项目普查或首次实现。

以下仅依据实际阅读的项目文件及 GitHub 许可证标识。没有运行这些第三方程序、重现论文实验或验证它们的效果声明。

| 项目 | 参考的优点 | Reasoned Lens 的取舍 |
| --- | --- | --- |
| [Fabric](https://github.com/danielmiessler/fabric) | `analyze_claims` 将主张、证据和反驳分开，使用模块化指令 | 采用逐项检查；不强制生成正反证据，不继承真伪分数、政治标签或“中间立场”要求 |
| [agentic-coding](https://github.com/sammcj/agentic-coding) | 批判性思维 Skill 强调准确理解、隐含前提和有用的追问 | 保留合理论证；把材料内逻辑检查与可选的外部事实核查分开 |
| [Bullshit Detector](https://github.com/SerhiiKorniienko/bullshit-detector) | 文档将内容取得与分析分开，并强调主张对应来源及消息起源 | 只描述实际可读取材料；不继承综合 BS 分数，不承诺平台抓取；补充正文与评论的归属关系 |
| [Missci](https://github.com/UKPLab/acl2024-missci) | 研究要求解释证据与主张之间被省略或误用的推理连接 | 追问“哪一步把证据变成更强结论”；不导入生物医学数据集，不把其结果当作我们的准确率 |

## 实际参考文件与版本

| 项目 | 核对的文件 | GitHub 标识的许可 |
| --- | --- | --- |
| Fabric | [analyze_claims/system.md](https://github.com/danielmiessler/fabric/blob/c7e57051e8951679dd675a1983064c4bc6387f5a/data/patterns/analyze_claims/system.md) | MIT |
| agentic-coding | [critical-thinking-logical-reasoning/SKILL.md](https://github.com/sammcj/agentic-coding/blob/dc738b4de1078ba6b561d12c37239d98f7a6c19e/Skills/critical-thinking-logical-reasoning/SKILL.md) | Apache-2.0 |
| Bullshit Detector | [README.md](https://github.com/SerhiiKorniienko/bullshit-detector/blob/d5f6156a8a5c72977bf2d4edae834dd22f7fa736/README.md) | MIT |
| Missci | [README.md](https://github.com/UKPLab/acl2024-missci/blob/9b3ddc904d11244aa0f04b608969b5c4619bd8c1/README.md) | Apache-2.0 |

版本链接用于说明调研时看的内容；上游后续可能变化。本项目的中文指令、案例和构建程序独立编写，没有复制上游提示词、代码或数据。链接不表示上游作者背书、合作或认可。

## 本项目的重点

正文与评论同时纳入分析，但分开署名和主张；热评不代表总体。每个追问对应可定位的原话、影响结论的缺口和可能改变判断的回答。支持、反对和自己的评论草稿使用相同标准。

设计目标是帮助理解与核对，而不是训练获胜话术、提高围攻效率或提供未经校准的“客观程度”分数。
