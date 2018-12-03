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
> StartTime: 2017-03-22,ModifyTime:2018-11-29

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

## Git fetch
1. 把远端的代码同步下来，强制覆盖本地:  
```
git fetch --all && git reset --hard origin/master && git pull
```

2. `git fetch` 从服务器下载index区域，并放到新分支，不下载code。

## git commit 正确用法
#### git push 之前，合并式地本地提交多次commit，不应该每次用`-m`的参数零碎的提交:
```
git add XX -p //分每个修改处提交到index区
git commit -m "" //提交一次新的commit
git commit --amend //在没有push之前，在上次commit基础上继续增加commit内容，是合并了两次commit甚至以后多次
```

#### 多次 git push 之后，应该合并一个功能分支的多个commit:
查看代码修改状态：
```
git log
git show HEAD^3
```

1. 先`rebase`要合并的前面的一个commit_id
`git rebase -i commit_id`.之后可以修改前面的commit，可以加入文件，可以删除commit
2. 修改类似下面内容的文件里的第二个开始的所有pick为s
```
pick 16a9a47 update3
pick a7186d8 update2
pick 7b16b28 update1
 # Rebase a9269a3..7b16b28 onto a9269a3 (3 commands)
 #.....
```

`:x`命令保存退出后会进入下一个文件修改。

3. 再修改下一个结果文件
4. `git log` //查看修改后 commit 时候已经合并，应该已经合并。但此时本地当前分支的 base commit_id 已经变了，所以需要重新和目标远端分支 rebase 基准，也就是执行下一步。

5. `git pull origin master/develop --rebase` //这里执行后极有可能发现冲突，解决冲突
6. 现在是返回了之前未 push 的状态，可以看一下`git status`是否所有代码都加入了index区域，然后直接再来一次push就可以了。


## Git status
`git status` 查看目前代码的状态，哪些是冲突的，哪些已经被加入了index进入版本控制，哪些还在 workspace。

## Git reset 本地回滚

```
git log //本地列出所有commit_id
git reset --hard commit-id //本地回滚
git reset --hard origin/master HEAD //从远端恢复代码和记录
```

`git reset` 回滚后想返回原来的代码，则可以用 `git reflog` 命令查看commit_ids操作记录，再恢复代码。

git reset 参数:
+ `--mixed`是git-reset的默认选项，它的作用是重置index索引内容，将其定位到指定的项目版本，而不改变你的工作树中的所有内容，只是提示你有哪些文件还未更新。
+ `--soft`选项既不触动索引的位置，也不改变工作树中的任何内容。该选项会保留你在工作树中的所有更新并使之处于待提交状态。相当于在--mixed基础上加上git add。
+ `--hard` 把整个目录还原到一个版本，包括所有文件。之后如果想返回之前的版本，可以用`git reflog`命令查看操作记录，返回move to的主语commit_id。

+ `--continue` //挨个检查每次commit的冲突情况，修复冲突;
+ `--abort`    //会回到rebase操作之前的状态，之前的提交的不会丢弃；
+ `--skip`     //将引起冲突的commits丢弃掉；

## Git pull 远端回滚
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

## Git branch
#### modify branch name
1. Rename your local branch:  
```
git branch -m new-name //you are on the branch you want to rename
git branch -m old-name new-name // you are on a different branch
```

2. Delete the old-name remote branch and push the new-name local branch:
```
git push origin :old-name new-name
```

3. Reset the upstream branch for the new-name local branch(建立映射关系，使用本命令后后可以直接使用git push):
```
git checkout #new-name-branch
git push origin -u new-name
```

#### pull remote branch and create at local
拉取远端的分支，在本地建立对应的分支：
1. 方法一：
```
git checkout -b 本地分支名x origin/远程分支名x
```
使用该方式会在本地新建分支x，会 **自动切换到该本地分支x**。
并 **会自动和远程分支建立映射关系**。
2. 方式二：
```
git fetch origin 远程分支名x:本地分支名x
```
使用该方式会在本地新建分支x，但是 **不会** 自动切换到该本地分支x，也不会和远程分支建立映射关系

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

## Git remote 建立多个远端
`git remote add XXX` 增加远端头,可以一次推到多个远端

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

[Rename a local and remote branch in git](https://multiplestates.wordpress.com/2015/02/05/rename-a-local-and-remote-branch-in-git/)

[git拉取远程分支并创建本地分支](https://blog.csdn.net/zhangxiaoyang0/article/details/79286825)

[git合并多个commit提交](https://www.jianshu.com/p/29bb983ec48a)
