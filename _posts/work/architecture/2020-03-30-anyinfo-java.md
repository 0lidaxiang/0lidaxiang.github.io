---
layout: post
title:  "漫谈架构技术"
rootCate: "work"
categories:
- architecture
tags:
- work
- user_permisstion
- architecture
---

本文介绍电商场景里的超卖如何处理，技术选型原则等零散知识点。

<!---more--->


## 技术选型原则：
越合适越好，越简单越好。多使用第三方库。

#### 编程语言
想要用最少的人力时间开发，选Python 。
想要最容易找到员工，选Java。
想要跟随潮流，2020年比较流行的、个人比较看好 Golang、Ruby。

#### 数据库选型
tidb：不会有join、事务问题。
crdb： 搭建复杂，对性能配置要求高

#### 数据仓库&流计算
olap
doris
sparksql presto impala  druid  flink

##  高并发，高可用，高性能
#### 软件工程方面
1. 事前：多机服务冗余、隔离、自动发布、灰度发布、数据库加索引、集成测试 & 单元测试
2. 中间：多级缓存（业务，sql缓存，中间件），离线，重试i，限流降级，异步，监控，回滚策略
3. 事后：复盘，优化迭代

#### 编程技巧
1. 不要在for循环里查询数据库，造成过多查询
2. 重要的日志要区分error、info、debug 记录下来
3. 调用第三方服务要考虑好服务重试问题
4. 严格命名参数、方法名、类名，这将在后来给你大大节约回想代码的时间
5. 强烈建议加注释，即便其他人都不写。除非你的记忆里能记得起来几个月之前的代码是什么意思。
6. 保持类、方法只要有单一职责。所以要多拆分，不要写一个100行的方法，让别人很难迅速理解！如何拆分设计各个类、类的方法，这是一件入门容易学成难的事情！

## 数据库配置
数据库连接池大小  一般配置 100左右，针对4核CPU、10，能支持7k的并发量。
druid 连接池

分布式存储：
mysql  NoSQL   NewSQL   olap
MySQL： 分表  500w，2G大小；index  pool  buffer  size
tidb：

## 场景一：超卖
超卖是商业 to C 的系统里常碰到的问题，要想解决这个问题，需要设计高可用、高并发、高性能、高拓展等多个方面。

1. 服务重试 
   1. A--B；
   2. 竞争
2. redis 解决：
    分布式锁：lua+key+自动失效；
            redsion，springinteration
    串行 -- 高并发
        分段锁 -- K   100，K1,K2，Kn
        A随机负载   K1重试   K1 flag

    mysql 解决
        1. 悲观锁，select * from where user for update  排它锁，航所，
        串行
        1. 乐观锁，RR
            1. mvcc，业务检查
            2. case when ，update set case when then 下单

springboot 过滤器  拦截器 微服务主件    数据库选型   技术选型  基于业务的设计思想    可拓展性   业务场景   技术场景  总结
