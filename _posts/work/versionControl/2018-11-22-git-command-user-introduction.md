---
layout: post
title:  "Introduction of Git commands"
rootCate: "work"
categories:
- VersionControl
tags:
- work
- tools
- Git
- Github
---

介绍Git的几种基本使用场景和解决问题方案，末尾附上更全面的来源资料。

<!---more--->
> StartTime: 2017-03-22,ModifyTime:2018-11-19

## 单账号单仓库
一般情况下(单人单仓库使用默认master开发)，使用下面三条命令就足够用：  
```
git add .
git commit -m ""
git push origin master
```

## 多人协作
1. 新建自己的分支：  
```
git checkout develop (某分支) //本地切换到XXX分支
git checkout -b feature/XXX
git checkout -b bug/XXX
```

2. 在开发和pull之前都要先查看一下本地目前所在分支是什么，列出本地现有的分支:
```
git branch
// 显示的结果里，每行最前面有星号的是当前的分支
```

3. 修改完自己本地的代码后，可以更新自己的代码本地仓库（使用前两条命令）或push到远端自己的分支( **git push 加上u参数，会在远端创建该分支** ):  
```
git add .
git commit -m "XXXX"
git pull origin develop --rebase
//一个选择是可以在本地把某个分支合并到master分支里，再合并其他分支的修改到master:
git checkout master
git merge XXX(某分支)
//另一个选择是本地不合并，按照第4点发起merge request交给其他人merge
git push origin XXX
```
> git pull 加上rebase参数，好处是调整自己的分支到develop分支的最新基准，这样极大可能避免冲突。另外一个好处在于可以检查git pull默认的merge操作，这样就减少了一个分支。(每次merge都会延伸某个新的分支)  

4. push到远端自己的分支后，下一步是在图形化界面发起对master的merge request，指定master分支，指定review人员，请求管理员合并。
5. 合并完成后，如果是bug修复或者不需要这个分支了，可以使用`git branch -d hotfix`命令删除本地这个分支。远端删除使用命令：`git push origin :branch_name`

## 回滚代码
#### 本地回滚：

```
//本地列出所有commit
git log
//本地回滚
git reset HEAD~1
git reset --hard commit-id // 慎重使用！
```

git reset 回滚出现问题则可以用 **git reflog** 命令查看commit_ids记录，再恢复代码。

git reset 参数:
+ --mixed是git-reset的默认选项，它的作用是重置索引内容，将其定位到指定的项目版本，而不改变你的工作树中的所有内容，只是提示你有哪些文件还未更新。
+ --soft选项既不触动索引的位置，也不改变工作树中的任何内容。该选项会保留你在工作树中的所有更新并使之处于待提交状态。相当于在--mixed基础上加上git add。
+ --hard 把整个目录还原到一个版本，包括所有文件。(**慎重使用！**)

+ --continue //当多次本地commit时候，可以使用本参数来挨个检查每次commit的冲突情况，修复冲突。
+ --abort    //会回到rebase操作之前的状态，之前的提交的不会丢弃；
+ --skip     //将引起冲突的commits丢弃掉；

#### 远端回滚：
当自动部署系统发布后发现问题后，需要回滚到某一个commit，再重新发布。

原理：先将本地分支退回到某个commit，删除远程分支，再重新push本地分支。

操作步骤：

```
1、git checkout the_branch
2、git pull
3、git branch the_branch_backup //备份一下这个分支当前的情况
4、git reset --hard the_commit_id //把the_branch本地回滚到the_commit_id
5、git push origin :the_branch //删除远程 the_branch
6、git push origin the_branch //用回滚后的本地分支重新建立远程分支
7、git push origin :the_branch_backup //如果前面都成功了，删除这个备份分支
```

## Git patch
UNIX世界的软件开发大多都是协作式的，因此，Patch（补丁）是一个相当重要的东西，因为几乎所有的大型UNIX项目的普通贡献者，都是通过 Patch来提交代码的。

个人理解：
patch就是打补丁，通过git工具把代码的差分，生成patch文件，
然后通过git工具可以直接把patch文件的内容，merge到代码里面。

生成patch的命令:  

```
git diff  > patch                        //本地变更  git diff 的内容，生成patch文件
git diff  branchname --cached > patch           //branch 之间差分生成patch文件
git format-patch HEAD^                                 //最近一次提交节点的patch
git format-patch  节点A   节点B        //两个节点之间的patch
```

使用patch:

```
git apply patch //将patch文件内容差分到本地
// 在使用patch之前可以使用以下命令，来测试，是否可以将patch完美打入本地src
git apply --check patch
```

## 多个 SSH-Key 如何使用
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


## 其他命令
1. 把远端的代码同步下来，强制覆盖本地:  
```
git fetch --all && git reset --hard origin/master && git pull
```

2. `git fetch` 从服务器下载数据库，并放到新分支，不跟自己的数据库合并。


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
