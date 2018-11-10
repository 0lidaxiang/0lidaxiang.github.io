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

> StartTime: 2017-03-22,ModifyTime:2018-11-05

<!---more--->

## 单账号单仓库
一般情况下(单人单仓库使用默认master开发)，使用下面三条命令就足够用：
```
git add .
git commit -m ""
git push origin master
```

## 多人协作
新建自己的分支：
```
git checkout -b XXX
```

更新自己的代码到远端自己的分支:
```
git add .
git commit -m ""
git push origin XXX
```

之后可以在图形化界面发起request，指定master分支管理员合并。

列出本地现有的分支:
```
git branch
// 前端加星号的是当前的分支
```

本地切换到XXX分支:
```
git checkout XXX(某分支)
```

本地把某个分支合并到master分支里，再合并其他分支的修改到master:
```
git checkout master
git merge XXX(某分支)
```

把远端的代码同步下来，强制覆盖本地:
```
git fetch --all && git reset --hard origin/master && git pull
```

## 常出现的问题记录
(1)`warning : permanently added the RSA host key for IP address '192.30.252.130' to the list of known list`  ：
这个大概说的是, git自己把公钥自动加到~/.git/known_host文件里面了, 进去查一下,确实是这样的.总之能上传成功就是好的.

(2)提交之后遇到类似Permission denied (publickey).大意说你不具有读和写的权限：
```
解决办法1
git remote rm origin
git remote add origin git@github.com:LyleLee/practice.git
解决办法2
git push origin master
```
(3) `remote: GitLab: You are not allowed to push code to protected branches on this project.`  
解决办法是请管理员开通对应branch的提交权限。
