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
source_updated_at: "2026-11-05T17:43:18+08:00"
source_revision: 3
source_body_sha256: "995ab39be6a7213d9e5668ffa3f85f323ccd8748aeb26125c3cbb930a19614c3"
source_verified_at: "2026-11-07T11:52:07+08:00"
---

> 原载：[荒岛书生 · 原文](https://huangdaoshusheng.cn/depth/agent-work-and-verification) · 作者：荒岛书生 · 原始发布日期：2026-09-09。
> 迁移核对：2026-11-07，依据当前公开正文；保留原文资料截止日期、作者观点与核验说明，不将历史资料视作今日消息。

* 目录
{:toc}

<!-- source-body:start -->
## 委托的单位变了

补全工具的基本单位是一段建议：人正在编辑，模型提供候选，人决定是否接受。编程 Agent 的单位可能是一项问题：找原因、改代码、运行检查、解释结果。能力范围扩大之后，用户需要判断的不只是代码对不对，还有过程是否可信。

2021 年 Copilot 的技术预览让生成建议进入编辑器。2023 年 SWE-bench 又把真实仓库的问题解决带进评估。前者是产品入口，后者是测量方式，两者共同帮助我们理解任务单位的变化。[Copilot 公告](https://github.blog/news-insights/product-news/introducing-github-copilot-ai-pair-programmer/)；[SWE-bench](https://arxiv.org/abs/2310.06770)。

## 一个任务循环包含什么

ReAct 研究把推理与行动交替组织：根据已有信息决定下一步行动，再利用环境反馈更新后续步骤。它展示了语言模型如何通过外部环境获得新信息，而不是一次性写完全部计划。[ReAct](https://arxiv.org/abs/2210.03629)。

对编程任务，可以把这个循环落实为读取相关文件、形成修改假设、实施小范围改动、运行检查、依据失败调整。这里的流程是本文的工程建议，不是 ReAct 论文对所有软件开发场景的保证。

## 上下文决定模型究竟在解决哪个问题

同一句“修复登录失败”，可能涉及前端状态、接口字段、会话过期，也可能只是环境变量缺失。没有检查仓库与运行条件，模型很容易为想象中的系统写出合理代码。

有效上下文也不是把所有文件塞进去。应该先确定用户观察到的行为、预期行为、触发条件与相关路径，再选择能验证假设的文件和日志。若问题跨越接口，还要核对调用方与实现方的契约，而不是只改报错位置。

## 工具接通之后，仍然需要边界

MCP 尝试为模型应用连接数据与工具提供共同接口。连接器减少重复集成工作，但协议不会替团队决定哪些操作可以自动执行。[MCP 原始公告](https://www.anthropic.com/news/model-context-protocol)。

读文件、运行测试、修改本地分支，与推送生产配置的代价不同。一个可用系统应让权限与任务范围相匹配，并在写入前知道目标对象。仅靠提示“请小心”，无法替代明确的工具边界和可恢复操作。

## 通过测试为什么还不等于完成

测试只检查已编码的性质。修改可能通过现有测试，却漏掉用户报告的场景；也可能为了让测试变绿，删掉了原本必要的约束。验收需要回到最初问题，证明触发条件下的行为已经改变，并说明仍未覆盖的部分。

例如修复日期筛选，不能只看构建成功，还要验证时区边界、空结果和今天这一天是否按产品定义计算。这个假设案例说明，验证范围应来自需求与风险，不应来自工具最容易运行的命令。

## 怎样评价一个编程 Agent

可以从固定的一组仓库问题开始，记录任务完成情况、耗时、修改范围、人工介入与回归错误。不同系统应使用相近的工具权限和预算。重试次数、测试环境和失败任务都需保留，否则比较的可能是不同工作条件。

| 观察点 | 读者应寻找的证据 |
| --- | --- |
| 理解任务 | 修改对应实际触发条件 |
| 执行过程 | 读写目标与授权范围一致 |
| 验证结果 | 检查覆盖了修复目标 |
| 交付说明 | 说明变化、证据与未完成项 |

本站的判断是，Agent 的价值应表现为更可靠地完成一项委托。运行时间长、工具调用多或代码改动大，都不能单独证明价值。成熟系统应该知道何时已有足够证据收工，也知道何时缺少关键事实必须暂停。

## 资料来源

- [Jimenez 等：SWE-bench（2023）](https://arxiv.org/abs/2310.06770)
- [GitHub：Copilot（2021）](https://github.blog/news-insights/product-news/introducing-github-copilot-ai-pair-programmer/)
- [Yao 等：ReAct（2022）](https://arxiv.org/abs/2210.03629)
- [Anthropic：MCP（2024）](https://www.anthropic.com/news/model-context-protocol)

资料核验：2026-09-09。本文为基于公开资料的原创整理。
<!-- source-body:end -->
