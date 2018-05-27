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

> StartTime: 2018-03-14,ModifyTime:2018-03-14

<!---more--->

1. 批量删除一个目录以及子目录下的 html 文件
 ```
 find . -name "*.html" -exec rm -r "{}" \;
 ```

２. 批量修改一个文件夹下面所有文件的后缀名为 .jpg
```
for i in `ls`; do mv -f $i `echo $i | sed 's/.....$/.jpg/'`; done
```
