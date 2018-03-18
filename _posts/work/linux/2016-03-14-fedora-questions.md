---
layout: post
title:  "Fedora remove nouse kernel version"
categories:
- work
tags:
- work Linux Fedora
---

> StartTime: 2016-03-14,ModifyTime:2016-03-14

<!---more--->

1. 如何删除开机画面中多余的内核选项：

   （1）普通用户权限下，用uname    -r 命令检查出当前使用内核的版本。

   （2）rpm -qa  |  grep kernel可以检查出系统中所有安装的内核。

   （3）在root权限下，对比第一步中查出的当前内核版本，用yum remove 内核名称   这个命令删除该内核。例子如下（网上的例子）：
   ```
    yum remove kernel-2.6.33.6-147.fc13.i686
    kernel-PAE-2.6.33.6-147.fc13.i686  
    kernel-PAE-devel-2.6.33.6-147.fc13.i686  
    ```
   （4）说明：yum remove 和  rpm -e 这两个命令虽然都能删除内核，但是rpm -e只是会删除内核，而yum remove命令则会删除与该内核相依赖的软件（这些软件与当前新的内          核无关）。
