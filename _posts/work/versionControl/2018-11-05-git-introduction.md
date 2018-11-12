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

在开发和pull之前都要先查看一下本地目前所在分支是什么，列出本地现有的分支:
```
git branch
// 显示的结果里，每行最前面有星号的是当前的分支
```

修改完自己本地的代码后，可以更新自己的代码本地仓库（使用前两条命令）或push到远端自己的分支:
```
git add .
git commit -m ""
git push origin XXX
```

push到远端自己的分支后，下一步是在图形化界面发起request，指定master分支，指定review人员，请求管理员合并。


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

## 多个ssh-key如何使用
git可以新建多个ssh-key，有的可以专门用于自己的github，有的可以用于公司提交代码。

第一步是使用`ssh-keygen -t rsa -c 'YOUR_WANT_NAME'`创建自己想要命名的一对key文件，
第二步是创建名为`config`的文件，里面内容类似下方代码这样:
```
Host github.com
HostName github.com
User git
IdentityFile ~/.ssh/github

Host code.aliyun.com
HostName code.aliyun.com
User git
IdentityFile ~/.ssh/COMPANY
```
第三步是把.pub结尾的公钥文件里的全部内容，粘贴到对应的远端仓库服务里，比如GitHub的setting里可以加入ssh-key，
第四步是提交或pull测试。

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
