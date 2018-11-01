---
layout: post
title:  "Python and Python3 experience"
rootCate: "work"
categories:
- Python
tags:
- work
- Python3
---

总结 Python 使用过程中的小技巧，以备后用。内容包括但不限于对list/set/map等数据结构、算法的记录。

<!---more--->

## General experience for all
1. 使用正则表达式的速度比 list in 方法检索要快
2. numpy 处理 data 的速度比一般的 list 要快很多，而且可以直接一行 code 读取 txt文档里的数据，不用再转换。
```
dataArr = numpy.loadtxt('./data/data.txt')
```
3. 移除 list 中的空格项：
```
while ' ' in list1:
    list1.remove(' ')
```
4. list 转换成 string：
```
','.join(list1)
```
5.  string 替换 replace，可以去掉多余的字符或者重复的字符：
```
str.replace(old, new[, max])
old -- 将被替换的子字符串。
new -- 新字符串，用于替换old子字符串。
max -- 可选字符串, 替换不超过 max 次
```

6. python dict 数据类型
```
a={'a':1,'b':[2]}
a['c']=3
// 此时a = {'a':1,'b':[2],'c':3}

a['b'].append(4)
// 此时a = {'a':1,'b':[2,4],'c':3}
 ```
7.
