---
layout: post
title:  "Linux helpful commands"
categories:
- work
tags:
- work Linux command
---

> StartTime: 2018-03-14,ModifyTime:2018-03-14

<!---more--->

1. 批量删除一个目录以及子目录下的 html 文件
 ```
 find . -name "*.html" -exec rm -r "{}" \;
 ```
