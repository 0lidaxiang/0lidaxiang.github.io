---
layout: post
title:  "Git Introduction and Questions"
rootCate: "work"
categories:
- VersionControl
tags:
- work
- tools
- Git
- Github
---

介绍Git的一些基本概念和规范。
<!---more--->
> StartTime: 2017-03-22,ModifyTime:2018-11-23

## 1.基本概念
1. commit或merge发生冲突的情况解释：  

```
<<<<<<< HEAD
<div id="footer">contact : email.support@github.com</div>
=======
<div id="footer">
  please contact us at support@github.com
</div>
>>>>>>> iss53
```

可以看到 `=======` 隔开的上半部分，是 HEAD（即 master 分支，在运行 merge 命令时所切换到的分支）中的内容，下半部分是在 iss53 分支(与自己修改内容冲突的分支)中的内容。

2. GitHub以开源代码出名，GitLab比GitHub更方便的在于提供免费私有仓库。

## 2. git 分支命名规范
git 分支分为集成分支、功能分支和修复分支，分别命名为 develop、feature 和 hotfix，均为单数。不可使用 features、future、hotfixes、hotfixs 等错误名称。请注意，一个分支尽量开发一个功能模块，不要多个功能模块在一个分支上开发。

+ master（主分支，永远是可用的稳定版本，不能直接在该分支上开发）
+ develop（开发主分支，所有新功能以这个分支来创建自己的开发分支，该分支只做只合并操作，不能直接在该分支上开发）
+ feature-xxx（功能开发分支，在develop上创建分支，以自己开发功能模块命名，功能测试正常后合并到develop分支）
+ feature-xxx-fix(功能bug修复分支，feature分支合并之后发现bug，在develop上创建分支修复，之后合并回develop分支。PS:feature分支在申请合并之后，未合并之前还是可以提交代码的，所以feature在合并之前还可以在原分支上继续修复bug)
+ hotfix-xxx（紧急bug修改分支，在master分支上创建，修复完成后合并到 master）
个分支尽量开发一个功能模块，不要多个功能模块在一个分支上开发。

## 3.  git commit 规范
Commit message 的格式
每次提交，Commit message 都包括三个部分：Header，Body 和 Footer。其中，Header 是必需的，Body 和 Footer 可以省略。


Header包括 type（必需）、scope（可选）和subject（必需） :
+ \<type>(<scope>): \<subject>// 空一行
+ \<body>// 空一行
+ \<footer>

不管是哪一个部分，任何一行都不得超过72个字符（或100个字符）。这是为了避免自动换行影响美观。

### 3.1 Header
Header部分只有一行，包括三个字段：type（必需）、scope（可选）和subject（必需）。

#### 3.1.1 type

type用于说明 commit 的类别，只允许使用下面7个标识。

+ feat：新功能（feature）
+ fix：修补bug
+ docs：文档（documentation）
+ style： 格式（不影响代码运行的变动）
+ refactor：重构（即不是新增功能，也不是修改bug的代码变动）
+ test：增加测试
+ chore：构建过程或辅助工具的变动

如果type为feat和fix，则该 commit 将肯定出现在 Change log 之中。其他情况（docs、chore、style、refactor、test）由你决定，要不要放入 Change log，建议是不要。

#### 3.1.2 scope

scope用于说明 commit 影响的范围，比如数据层、控制层、视图层等等，视项目不同而不同。

#### 3.1.3 subject

subject是 commit 目的的简短描述，不超过50个字符。

以动词开头，使用第一人称现在时，比如change，而不是changed或changes。

第一个字母小写，结尾不加句号（.）

### 3.2 Body
Body 部分是对本次 commit 的详细描述，可以分成多行。下面是一个范例。

```
More detailed explanatory text, if necessary.  Wrap it to
about 72 characters or so. Further paragraphs come after blank lines.- Bullet points are okay, too- Use a hanging indent
```
注意两点：  
（1）使用第一人称现在时，比如使用change而不是changed或changes。

（2）应该说明代码变动的动机，以及与以前行为的对比。

## 参考文献
[Git 分支 - 分支的新建与合并](https://git-scm.com/book/zh/v1/Git-%E5%88%86%E6%94%AF-%E5%88%86%E6%94%AF%E7%9A%84%E6%96%B0%E5%BB%BA%E4%B8%8E%E5%90%88%E5%B9%B6)

[git 删除本地分支和远程分支、本地代码回滚和远程代码库回滚](https://www.cnblogs.com/hqbhonker/p/5092300.html)

[git reset soft,hard,mixed之区别深解](https://www.cnblogs.com/kidsitcn/p/4513297.html)
[git 分支命名规范](https://www.cnblogs.com/yorkyang/p/9147309.html)
[Git 提交的正确姿势：Commit message 编写指南](https://www.oschina.net/news/69705/git-commit-message-and-changelog-guide?from=20160110)
[git commit配置模板](https://www.jianshu.com/p/19e3b1e891b4)
[使用git进行团队合作开发](https://www.cnblogs.com/ShaYeBlog/p/5575852.html)
[Git的Patch功能](https://www.cnblogs.com/y041039/articles/2411600.html)
[](https://blog.csdn.net/jiangzd_yanzi/article/details/76573987)
