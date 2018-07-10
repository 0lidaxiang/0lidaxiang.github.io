---
layout: post
title:  "Linux helpful commands"
rootCate: "work"
categories:
- Linux
tags:
- work
- Linux
- command
---

To introduce some helpful commands in Linux(ubuntu 18).

<!---more--->

> StartTime: 2018-03-14,ModifyTime:2018-07-10

1. 批量删除一个目录以及子目录下的 html 文件
 ```
 find . -name "*.html" -exec rm -r "{}" \;
 ```

２. 批量修改一个文件夹下面所有文件的后缀名为 .jpg
```
for i in `ls`; do mv -f $i `echo $i | sed 's/.....$/.jpg/'`; done
```

3. 列出磁盘的容量和占用情况
```
df -h
 ```
4. use htop or top tool watch which program use unnormal resource of computer, and kill it by this command:
```
htop
top
kill -9 PID
```
5. 列出当前 folder 的 folders 大小：
```
sudo du -h --max-depth=1
```
