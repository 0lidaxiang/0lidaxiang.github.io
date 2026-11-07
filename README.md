# 荒岛书生

个人主页和博客，使用 Jekyll 4.4.1 与官方 Hydejack 9.2.1 免费主题。

## 本地预览

使用 Ruby 3.3 或更新的兼容版本（仓库的 `.ruby-version` 为 3.3）。macOS 自带 Ruby 2.6 不适用。

```sh
bundle install
bundle exec jekyll serve
```

访问 http://127.0.0.1:4000 。主题来自 RubyGems，首页使用免费的 `blog` 布局，未使用 PRO 的网格、作品集或简历功能。
中文采用系统字体，不依赖 Google Fonts。

## 发布

`.github/workflows/pages.yml` 使用 Ruby 3.3 构建，发布到 GitHub Pages。首次启用时，在仓库 Settings → Pages → Build and deployment 中将 Source 设为 **GitHub Actions**。
之后推送 `master` 或手动运行工作流即可部署；自定义域名继续由原来的 `CNAME` 文件指定。

发布构建命令：

```sh
JEKYLL_ENV=production bundle exec jekyll build --trace
```

主题版本和依赖由 `Gemfile.lock` 固定，锁文件包含 macOS ARM 和 Linux x86_64 平台。

## 内容和旧网址

- `_posts/` 的 102 个 Markdown 源文件及 `assets/images/` 均原样保留。
- 切换前后按原配置核对了 92 篇已发布文章的网址，保持 `/:categories/:title`。
- 其余不符合文章命名规则的历史文件保持原来的未发布状态，不自动补日期或发布。
- 文章摘要分隔符仍为 `<!---more--->`，图片中的 Liquid 路径保持不变。
- `/workOutline/`、`/lifeOutline/`、`/tags/`、联系、关于和赞赏等原页面网址保留。
- `/index/`、`/indexlife.html` 和 `/tags_cloud/` 保留兼容跳转；首页分页仍为 `/page2/` 等原格式。
- 侧栏与文章作者介绍共用地球猫头像，分别由 `_config.yml` 的 `logo` 和 `author.picture` 指定，图片保存在 `assets/img/avatar-earth-cat.png`；主题原生样式以圆形显示，原始方图保留。
- 浏览器图标使用猫脸局部裁切，`favicon.ico` 包含 16/32/48/64px 四档尺寸；`assets/apple-touch-icon.png` 为 180px 触屏图标。图标 URL 带版本参数以更新浏览器缓存。
- 导航、中文文案、字体与色彩见 `_config.yml`、`_data/strings.yml` 和 `_sass/my-style.scss`。
- 关闭 Hydejack 的宽屏大标题；`_sass/_site-typography.scss` 分别约束列表标题（约 22–30px）与文章/独立页标题（约 26–34px），通过 `my-inline.scss` 和 `my-style.scss` 同时用于正式首屏和完整样式。`_layouts/blog.html` 保留官方列表逻辑，增加 `.post-list` 容器以区分列表排版。
- 顶部工具栏通过 `_sass/_site-navigation.scss` 统一为 56px，按钮宽 48px，正文从工具栏下方 `2rem` 开始；首屏和完整样式共用，避免宽屏根字号导致高度变化。
- 首页默认隐藏摘要后的“继续阅读”，点击文章标题进入全文。`_config.yml` 的 `hydejack.hide_read_more` 是本仓库通过 `_includes/components/post.html` 增加的开关，设为 `false` 可恢复主题入口；摘要显示保持不变。首页文章间距为 `2.5rem`，标题区到摘要为 `.75rem`。
- 联系页顶部新增小红书与微信公众号卡片，账号名称均为“荒岛书生codedoctor”；配置位于 `contact.md` 的 `social_accounts`，二维码原图保存在 `assets/img/contact/`，显示宽度为 180px，可点击打开原图，小红书提供主页链接。宽屏并排，窄屏单列。
- 联系页使用独立的 `contact` 布局，标题改为“联系我”，微信 ID 按用户要求更新为 `codedoctor`，其余联系方式保留；宽屏自动并排，手机单列。
- 文章分类和标签完整换行；目录的长标题与日期分开排版；宽表格与代码块在自身范围内横向滚动。
- `_plugins/legacy_image_paths.rb` 在构建时为 Lightworks 文章的两张图片生成原 `/images/work/lightworks/` 地址，从现有资产复制，文章里的链接不改。

## 历史访客统计

继续使用原 Flag Counter **6972**，未创建新计数器，也没有修改、重置或导入计数数据。
图片地址与历史统计链接保存在 `_data/legacy_analytics.yml`，通过 `_includes/flag-counter.html` 接入 Hydejack 页脚。
历史数据由 Flag Counter 服务端保存，可点击页脚进入 https://info.flagcounter.com/6972 查看。

本地预览与正式发布均使用同一计数器的 `mini` 图片，仅显示总访问量（累计浏览次数 / pageviews），不展示国家、地区或国旗列表；访问仍按 Flag Counter 的规则参与计数。
`flags_0` 在迷你样式中表示显示累计浏览次数；宽屏与窄屏共用 160 × 20px 图片。
Hydejack 的站内页面切换会替换正文和页脚，因此各页面均可显示原计数器；未启用离线缓存，也没有额外增加统计请求。
浏览器缓存、拦截扩展和服务方规则可能影响新增计数，历史记录仍由原服务管理。

旧 Google Universal Analytics 标识 **UA-91050128-1** 也已原样归档于该文件。
UA 服务已停用，标识不能用于恢复已被 Google 删除的数据，也不能自动迁移成 GA4；因此不再加载失效的 UA 脚本。
Flag Counter 和 Google Analytics 是两套独立的统计系统。

## 改版验证

```sh
python3 scripts/verify_migration.py
```

这是一项针对本次主题迁移的验收，使用改版前的 Git 提交 `7734176f35ee4e5ff3fce957b1a067c1b0ff4c17` 核对文章、图片和独立内容页；不是日后禁止修改文章的规则。
路由清单为 `scripts/legacy-post-routes.json`，在改版前后用同一 Jekyll 读取原配置及新配置得到并比对。

## 主题来源与许可

- [Hydejack](https://hydejack.com/) / [官方源码](https://github.com/hydecorp/hydejack/tree/v9.2.1)：GPL-3.0，通过 gem 引用；保留页脚署名。
- `_includes/body/footer.html` 和 `_includes/head/meta-static.html` 是官方 9.2.1 的局部覆盖，分别加入原计数器、恢复浏览器缩放。
- 原 Tale 主题的 MIT 许可保留于 `LICENSE`。

本网站中除了研究论文（一般为 PDF 格式）以外，若无特别说明，发表的文章仍遵循原来的 CC-BY-NC-SA 协议。
