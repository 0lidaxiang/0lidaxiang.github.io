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

总结 Django Framework 使用过程中的小技巧，以备后用。

<!---more--->

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
