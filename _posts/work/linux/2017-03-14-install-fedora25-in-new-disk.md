---
layout: post
title:  "Install Fedora25 in New Disk"
rootCate: "work"
categories:
- Linux
tags:
- work
- Linux
- Fedora
- Fedora-Install
---

> StartTime: 2017-03-14,ModifyTime: 2017-03-14

<!---more--->

1、下载Fedora25的 **64位** iso(别下错自己电脑的类型，我的是64位)和软碟通软件，准备U盘

2、用软碟通刻录系统到U盘中，直接默认选择刻录就可以。至于什么便捷启动、写入方式不用调整。

3、首先**确认软碟通打开iso文件时的filename**，这才是真的filename。

4、其次更改U盘名字，改的简短一点。例如FEDORA25，因为u盘名字莫名其妙会自动大写。

5、建议使用sublime编辑器的搜索功能，搜索这三个文件**isolinux.cfg、syslinux.cfg、grub.cfg** 中所有的iso 的 filename(和第三步的一样的，不带后缀iso三字母的名字，有时候和下载的iso文件名不一样)，然后统一修改为U盘名字统一，大小写要一致。

6、复制iso文件到U盘根目录下，然后更改它的名字（不算后缀）和U盘名字一致。

7、重启电脑，进入bios修改启动项，开始安装。自动分区我觉得在装双系统的时候最难的，然后果断加了块硬盘，自动分区，顺利安装。如果电脑不能增加硬盘的童鞋，建议可以作为外置硬盘安装系统。

8、未尽事宜和有好的办法可以在一块硬盘上装双系统，可以留言。
