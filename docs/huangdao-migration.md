# 荒岛书生长文迁移记录

核对时间：2026-11-07T11:52:07+08:00（Asia/Shanghai）。仅修改本博客；不提交、推送、部署。

## 来源与版本

- 主来源：当前公开 `https://huangdaoshusheng.cn/api/site`，health 返回 MySQL；公开深度 25 篇、信号 48 条、演化节点 71 条。逐篇 ID、原日期、源保存时间、revision、正文 SHA-256 和新路径见同目录 `huangdao-migration.json`。
- 源代码：`/Users/daxiangli/brand/huangdao` @ `e7739aa`；配套读取全部 6 个内容包 manifest（14 篇深度正文）及运行文档。当前公开 API 与包正文核对后以 API 的作者、正文及元数据为准。
- 本机 MySQL：以现有安全配置执行 `START TRANSACTION READ ONLY`，读取 `huangdao.site_state.id=1` 后回滚；120 条记录，行保存时间 2026-09-10 11:03:36。它是独立且较旧的数据，不能代替生产公开版本。没有启动后端、初始化 seed 或写库。文件模式 `backend/data/site.json` 不存在。
- `huangdaopage` 仅作只读历史参照；其 10 月 AA 榜单不是本次 11 月稿的最新版本，未据此覆盖公开正文。旧 artifacts/临时预览不作为迁移来源。
- 收尾再次读取公开 API，20 篇入选记录与起始快照完全一致。本次工具操作没有写入两个来源仓库；工作期间源仓库由其他并发工作推进到 `4423e45`，并出现未跟踪审阅目录，本次未触碰。源库只读复查的整个快照与起始读取一致。
- 只接受公开 API 当前返回且发布时间已到的成稿。草稿、下线、回收站、未到期内容和原始数据库快照不进入可发布资产。工作快照与截图保留在被忽略且排除构建的 `.migration-work/`。

## 入选（20 篇）

| 标题 | 原发布日期（上海） | 新路径 |
| --- | --- | --- |
| Agent 的分水岭：从调用工具到交付可验证结果 | 2026-09-05 | `/ai/agent-value-loop` |
| 从 CLIP 到多模态助手：对齐、理解与行动是三件事 | 2026-09-05 | `/ai/multimodal-next` |
| 读懂 Transformer：注意力如何把上下文变成计算 | 2026-09-05 | `/ai/transformer-explained` |
| 残差连接为什么有效：从 ResNet 到深层模型的优化 | 2026-09-05 | `/ai/residual-connections` |
| DeepSeek 的 MoE 到底省在哪里：专家、路由、MLA 与训练成本 | 2026-09-05 | `/ai/deepseek-moe-explained` |
| RLHF 与 DPO：模型怎样学会“更符合人的要求” | 2026-09-05 | `/ai/rlhf-and-dpo` |
| LoRA 与 QLoRA：少训练一些参数，究竟省了什么 | 2026-09-05 | `/ai/lora-and-qlora` |
| 扩散模型如何画图：从噪声预测到潜空间生成 | 2026-09-05 | `/ai/diffusion-explained` |
| 大模型为什么不能只比参数：从 GPT-3 到 Chinchilla 的规模问题 | 2026-09-09 | `/ai/scaling-and-compute` |
| RAG 的难点在证据链：长上下文为何没有让检索失去意义 | 2026-09-09 | `/ai/rag-evidence-chain` |
| 从预测文字到遵循指令：RLHF 改变了什么，又没有解决什么 | 2026-09-09 | `/ai/post-training-and-truth` |
| 从 CLIP 到潜空间扩散：AI 图像生成的几个关键分工 | 2026-09-09 | `/ai/diffusion-and-multimodal` |
| 从 Copilot 到 Agent：AI 编程真正扩大的是什么 | 2026-09-09 | `/ai/agent-work-and-verification` |
| LoRA、MoE、FlashAttention：三种“更高效”其实在解决不同问题 | 2026-09-09 | `/ai/efficient-model-systems` |
| 推理模型为什么愿意多花时间：从思维链到可验证的结果 | 2026-09-09 | `/ai/reasoning-compute-and-checks` |
| 编程 Agent 的下一步：从写出代码到跟完一次 PR | 2026-11-05 | `/ai/coding-agent-after-the-first-pr` |
| AI 会模拟、会设计，为什么仍然需要外部验证 | 2026-11-05 | `/ai/world-models-science-and-verification` |
| 万亿IPO要黄了！Anthropic核心团队人才叛逃 | 2026-11-05 | `/ai/anthropic-ipo-team-departures-opinion` |
| 11月最新AI榜单：Gemini第一，Sol与Astra差两分 | 2026-11-05 | `/ai/artificial-analysis-index-guide` |
| Muse 与个人 Agent 浪潮：当 AI 开始替你持续办事 | 2026-10-20 | `/ai/muse-personal-agent-wave` |

技术文章按独立价值保留：RLHF/DPO 训练方法与后训练真实性、扩散公式与多模态分工、LoRA 参数账与综合效率、Agent 交付循环与编程/PR 实践，各自讨论不同层次，不按共享来源机械去重。作者评论按原身份收入，不将推测改写成已证实消息。

## 未入选的公开深度

| 标题 | 理由 |
| --- | --- |
| RAG 的价值不在“接上向量库”，而在证据链 | 与 rag-evidence-chain 重叠；选择包含数据入库、混合检索、定位式验收及权限过滤的版本。 |
| Scaling Laws 与 Chinchilla：大模型为什么不能只比参数 | 与 scaling-and-compute 重叠；选择包含训练、推理、任务与运行成本分层的完整版本。 |
| 推理模型为什么要学会验证：从长答案到可靠答案 | 与 reasoning-compute-and-checks 重叠；后者更完整地区分提示、训练、推理预算及独立检查。 |
| Transformer 为什么改变了 AI：从序列处理到可扩展的通用架构 | 与 transformer-explained 重叠；后者包含 Q/K/V 数值演算、掩码、张量与代价解释，更适合长期查阅。 |
| 10 月以来的 AI 更新：模型分工、持续任务与可检验产物 | 阶段性更新综述；核心方法已由 PR 跟进、外部验证和 Muse 专题覆盖，不重复收入。 |

48 条短讯和 71 个演化节点不属于本轮长文迁移。演示/占位记录、非公开和未来记录不补入；不公开披露它们的正文。

## 日期、内容与疑点

- 日期来自每篇公开记录 `publishedAt`，不使用迁入日。源 `updatedAt` 单独存为 `source_updated_at`；它可由批量保存/导入产生，缺少实质改稿证据时不设置 Jekyll `last_modified_at`，避免虚构正文更新时间。
- 正文原样保留，仅加来源核对说明、目录、已迁文章的关联阅读与图表兼容替换；原作者、标题、摘要、资料截止日期、公式、代码及原有参考文献保留。
- 当前选中正文没有 Markdown 配图或站内路径链接；不为“有配图”添加无关图片。榜单含两个 `site-chart` 围栏，须转换成静态图和完整数据表，详见资源处理。
- Anthropic 作者评论的“腰斩式回落”与 25% 口径不一致，原稿也对人员动机、IPO 走向作出强推断。保留标题、第一人称、作者评论/推测声明与文末不背书说明，不自行改写。
- 本次核验确认公开身份、正文版本与引用保留，不等于重新完成所有论文实验或新闻事实核查；图表沿用 2026-11-05 历史快照，不冒充今日实时排名。

## 资源与验证

- 地球猫头像、favicon.ico（16/32/48/64px）和 180px apple-touch-icon 均复用，文件未修改；配置继续指向原资源和原缓存版本参数。
- 微信公众号与小红书二维码 PNG 均复用，未生成、重绘或覆盖。Vision 解码：微信为 `http://weixin.qq.com/r/mp/OCpbQ4TEq9nUrcAg938q`；目标小红书原图为 `http://xhslink.com/m/7mMhFIxAvCX`，源内容包为同路径的 HTTPS。GET 跟随跳转确认两种协议均进入同一用户 `63e1a9e50000000025004c73` 的小红书登录入口；微信 GET 返回 200。
- 名称与源公开配置、asset-sources.json 一致，均为“荒岛书生codedoctor”。联系页补充微信实际目标链接，保留已有小红书 HTTPS 链接。二维码 180px 显示、带白边，可点击原图；桌面和手机渲染后的截图再次解码均通过。未实际使用微信/小红书手机 App 扫码关注或登录。
- 榜单仅复制源 `figures/aa-november-2026.json` 至 `assets/data/huangdao/`，保留全部 8 行配置、品牌色、显示整数、成本、单位、日期、版本和来源。两个专有组件替换为 matplotlib 生成的静态 PNG（约 113KB/85KB）及完整 Markdown 数据表；图片支持点击放大，无 React/Go/API 运行依赖。散点图使用原定对数成本轴与整数分数，未添加不存在的全榜或拟合数据。
- 原有文章、域名 CNAME、Flag Counter 6972、兼容网址、导航和主题机制保持；只为新文章补 `ai` 分类、原分类/话题标签和 `rootCate: work`。首页与分页、技术目录、标签目录均能进入新文章。

## 实际验证结果

- Ruby **3.4.8**（README 允许的 3.3+ 兼容环境）、Jekyll 4.4.1、Hydejack 9.2.1，复用锁文件及现有 `vendor/bundle`。`JEKYLL_ENV=production BUNDLE_PATH=vendor/bundle …/bin/bundle exec jekyll build --trace` 成功，无 Liquid/Markdown 构建错误。未更换主题或更新 Gemfile.lock。
- `python3 scripts/verify_migration.py` 通过：337 个历史内容源原样保留、92 个历史已发布网址存在、两张历史图片兼容地址一致。保留原脚本及全部断言，未通过修改旧验收消除错误。
- `python3 scripts/verify_huangdao_import.py` 通过：20 篇原正文 SHA-256 可逆核对、适配正文 SHA-256、原日期/作者、目录、首页分页/技术目录/标签入口、站内链接/锚点/图片及 8 行图表数据。
- Chromium 实际访问 **1440×1000** 桌面与 **390×844** 手机：每种尺寸检查首页、技术目录、标签、联系页和全部 20 篇新文章，共 **48** 次页面验收；状态均为 200，无页面横向溢出、缺图、脚本错误或失败请求。查看截图确认全文、作者评论声明、长标题、图表与代码/公式块排版。
- 实际点击技术目录进入正文、点击目录锚点；核对关联文章和图片原图链接。favicon 与触屏图标实际 URL 均返回 200；地球猫侧栏和个人文章作者头像使用原图。
- 所有 **92** 个旧文章 URL 逐个 HTTP 请求返回 200；关闭 JavaScript 后新榜单、Muse 长文及历史文章仍可阅读。
- 联系页桌面并排、手机单列，均完整显示两张 180px 二维码并可查看原图；渲染截图的四次 Vision 解码全部成功。另检查两种尺寸的暗色模式，二维码继续保持白色底板。
- `git diff --check` 与新文件的 `git diff --no-index --check` 均通过。构建产物不包含 `docs/`、原始快照、私密配置、临时核验目录或后端。

本地证据位于被忽略的 `.migration-work/build.log`、`browser-report.json`、`dark-qr-report.json`、`rendered-qr-decodes.jsonl`、`channel-get-check.json` 和 `screenshots/`。本地预览服务为 `http://127.0.0.1:4000/`，仅使用已构建的静态产物。

## 已知边界

内容版本与公开身份已经核对，没有发现迁移实现阻塞。原文的全部外部参考链接没有逐篇重新事实核查，也没有复现实验；作者评论的实质疑点按上文记录保留。平台链接已验证 GET 跳转，未进行手机客户端登录/关注测试。未提交、推送或部署。
