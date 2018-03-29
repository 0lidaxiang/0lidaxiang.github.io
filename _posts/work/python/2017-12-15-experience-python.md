---
layout: post
title:  "Python and Python3 experience"
categories:
- work
tags:
- work
- Python3
---

> StartTime: 2017-12-15,ModifyTime:2017-12-15  

<!---more--->

## General experience for all
1. 使用正则表达式的速度比 list in 方法检索要快
2. numpy 处理 data 的速度比一般的 list 要快很多，而且可以直接一行 code 读取 txt文档里的数据，不用再转换。
```
dataArr = numpy.loadtxt('./data/data.txt')
```
