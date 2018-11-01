---
layout: post
title:  "Django experience"
rootCate: "work"
categories:
- Python
tags:
- work
- Python3
- Django
---

总结 Django Framework 使用过程中的技巧和经验，以备后用。内容包括但不限于 ORM 模型、Static、Templates、Admin 模块等原生 Django 的功能。

<!---more--->

## migrate 和makemigrations的差别
```python3 manger.py makemigrations``` 相当于在该app下建立 migrations目录，并记录下你所有的关于modes.py的改动，比如0001_initial.py， 但是这个改动还没有作用到数据库。

在此之后执行命令```python3 manager.py migrate```
将该改动作用到数据库文件，比如产生table之类。

## 关于优化执行时间
1. **尽可能减少对database的访问次数**，把需要for循环多次请求的query一次全部提取出来再做进一步python的筛选和计算，即便会因此产生join问题、大量for循环和重复计算的问题。实例操作证明：通过把query从520个减少到10个，访问时间从2700ms降低到430ms，整体接口访问时间从6s降低到1s左右。(真实要看server当前访问的对database访问的压力，既有压力越大那么可能请求多的情况下速度更慢)
2. 少用split，多使用他人开发好的Library。
3. 多构造和使用复杂的数据结构(比如dict)，这样更容易理清代码的逻辑关系、也有助于解决牵扯多个model时的bussiness复杂逻辑处理的问题。
4. 正向查询：以使用外键的表为主，以外键为id的表数据为条件。B中某个具体实例所关联的A。
```
models.ForeignKey(A)
A.B_set.all()    //比下面的方法多消耗0.2-0.3秒
B.objects.filter(A)  //更快
```
5. 反向查询: 想查询A 中某个具体实例所关联的 B



## Django ORM
1. ORM：Object Relational Mapping(关系对象映射)
2. ORM 原理：
+ Django自带的orm是data_first类型的ORM，使用前必须先创建数据库。
+ 在django中，根据代码中的类自动生成数据库的表也叫--code first。obj.id  obj.name.....类实例对象的属性
+ 类名对应------》数据库中的表名
+ 类属性对应---------》数据库里的字段
+ 类实例对应---------》数据库表里的一行数据

3. ORM 操作流程：
+ 创建数据库，设计表结构和字段
+ 使用 MySQLdb 来连接数据库，并编写数据访问层代码
+ 业务逻辑层去调用数据访问层执行数据库操作

4. Django orm的优势：
Django的orm操作本质上会根据对接的数据库引擎，翻译成对应的sql语句；所有使用Django开发的项目无需关心程序底层使用的是MySQL、Oracle、sqlite....，如果数据库迁移，只需要更换Django的数据库引擎即可；

## Django class-view method
基于函数的视图的问题在于，虽然它们很好地覆盖了简单的情形，但是不能扩展或自定义它们，即使是一些简单的配置选项，这让它们在现实应用中受到很多限制。  

基于类的通用视图然后应运而生，目的与基于函数的通用视图一样，就是为了使得视图的开发更加容易。


## 参考
[Django ForeignKey 反向查询中 filter 和 _set的效率对比](https://blog.csdn.net/aaazz47/article/details/78914956/)
