---
layout: "post"
title: "从 Copilot 到 Agent：AI 编程真正扩大的是什么"
date: "2026-09-09T08:00:00+08:00"
author: "荒岛书生"
categories: ["ai"]
rootCate: "work"
tags: ["技术解读", "Agent", "开发者", "产品"]
excerpt: "当任务从补全一段代码扩大到交付修改，上下文、工具、权限和验收开始决定系统价值。"
source_site: "荒岛书生"
source_id: "launch-agent-work-and-verification"
source_url: "https://huangdaoshusheng.cn/depth/agent-work-and-verification"
source_reference: "https://arxiv.org/abs/2310.06770"
source_category: "技术解读"
source_published_at: "2026-09-09T08:00:00+08:00"
source_updated_at: "2026-11-07T13:42:14+08:00"
source_revision: 4
source_body_sha256: "fd9f366bb5223608483a8957a9d036311193cece187c6e87087616bda0c08171"
source_verified_at: "2026-11-07T17:34:30+08:00"
last_modified_at: "2026-11-07T13:42:14+08:00"
---

* 目录
{:toc}

<!-- source-body:start -->
## 委托的单位变了

代码补全出现时，开发者正在编辑，模型给出一段建议。Agent 继续把范围扩大到整个问题：找原因、改代码、运行检查，再把结果交回来。这个委托单位的变化，我觉得特别值得讲。

2021 年 Copilot 的技术预览让生成建议进入编辑器。2023 年 SWE-bench 又把真实仓库的问题解决带进评估。前者是产品入口，后者是测量方式，两者共同帮助我们理解任务单位的变化。[Copilot 公告](https://github.blog/news-insights/product-news/introducing-github-copilot-ai-pair-programmer/)；[SWE-bench](https://arxiv.org/abs/2310.06770)。

## 一个任务循环包含什么

ReAct 研究把推理与行动交替组织：根据已有信息决定下一步行动，再利用环境反馈更新后续步骤。它展示了语言模型如何通过外部环境获得新信息，而不是一次性写完全部计划。[ReAct](https://arxiv.org/abs/2210.03629)。

对编程任务，可以把这个循环落实为读取相关文件、形成修改假设、实施小范围改动、运行检查、依据失败调整。让每次反馈影响下一步，Agent 才能顺着真实项目推进。

## 上下文决定模型究竟在解决哪个问题

一句“修复登录失败”，背后有前端状态、接口字段、会话过期和环境配置。先读仓库和运行条件，把真实触发场景找出来，后面的修改才有具体目标。

有效上下文也不是把所有文件塞进去。应该先确定用户观察到的行为、预期行为、触发条件与相关路径，再选择能验证假设的文件和日志。若问题跨越接口，还要核对调用方与实现方的契约，而不是只改报错位置。

## 工具怎样接到实际开发

MCP 尝试为模型应用连接数据与工具提供共同接口。连接器减少重复集成工作，但协议不会替团队决定哪些操作可以自动执行。[MCP 原始公告](https://www.anthropic.com/news/model-context-protocol)。

读文件、运行测试、修改本地分支，与推送生产配置的代价不同。一个可用系统应让权限与任务范围相匹配，并在写入前知道目标对象。仅靠提示“请小心”，无法替代明确的工具边界和可恢复操作。

## 回到最初那个问题检查结果

修完以后，回到用户遇见的那个场景再走一遍。已有测试负责检查编码过的行为，实际问题再由对应的页面或接口来确认。每一份检查都有自己的用途，开发者也更容易审阅。

比如日期筛选，看看今天的范围怎样按时区计算，空结果能否正常显示，跨日输入会得到什么。把问题问具体，检查也就变得很直接。

## 怎样评价一个编程 Agent

我建议保留几项常做的仓库任务，记录耗时、改动范围、人工接管和回归问题。不同助手用相近工具与预算跑一遍，结果更容易对照，也更能说明日常使用差别。

| 观察点 | 读者应寻找的证据 |
| --- | --- |
| 理解任务 | 修改对应实际触发条件 |
| 执行过程 | 读写目标与授权范围一致 |
| 验证结果 | 检查覆盖了修复目标 |
| 交付说明 | 说明变化、证据与未完成项 |

我愿意长期用的编程 Agent，要把目标一直带到结果：读对项目、改到问题、检查对应行为，再交回能审阅的差异。开发者少来回解释几轮，工具的价值就已经很实在。

## 资料来源

- [Jimenez 等：SWE-bench（2023）](https://arxiv.org/abs/2310.06770)
- [GitHub：Copilot（2021）](https://github.blog/news-insights/product-news/introducing-github-copilot-ai-pair-programmer/)
- [Yao 等：ReAct（2022）](https://arxiv.org/abs/2210.03629)
- [Anthropic：MCP（2024）](https://www.anthropic.com/news/model-context-protocol)

<!-- source-body:end -->

---

<!-- source-note:start -->
原载：[荒岛书生](https://huangdaoshusheng.cn/depth/agent-work-and-verification) · 首发：2026-09-09 · 本次修订：2026-11-07。
<!-- source-note:end -->
