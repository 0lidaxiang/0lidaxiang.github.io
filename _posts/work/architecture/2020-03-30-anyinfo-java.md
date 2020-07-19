---
layout: post
title:  "漫谈 java"
rootCate: "work"
categories:
- architecture
tags:
- work
- user_permisstion
- architecture
---

## 超卖
1. 服务重试 --  A--B；竞争
2. redis 解决：
    分布式锁：lua+key+自动失效；
            redsion，springinteration
    串行 -- 高并发
        分段锁 -- K   100，K1,K2，Kn
        A随机负载   K1重试   K1 flag

    mysql 解决
        1. 悲观锁，select * from where user for update  排它锁，航所，
        串行
        2. 乐观锁，RR
            1. mvcc，业务检查
            2. case when ，update set case when then 下单

springboot 过滤器  拦截器 微服务主件    数据库选型   技术选型  基于业务的设计思想    可拓展性   业务场景   技术场景  总结

## 技术选型原则：
 越合适越好，越简单越好。

tidb：不会有join、事务问题。
crdb： 搭建复杂，对性能配置要求高

olap
doris
sparksql presto impala  druid  flink

高并发，高科哟用，高性能
1. 事前   多机   服务冗余   隔离  自动发布灰度
2. 中 多级缓存（业务，sql缓存，中间件） ，离线，重试i，限流降级，异步，监控，回滚策略
3. 复盘

中间件  JVM  会用
索引失效：
1.左
2.索引做操作
3. int varchar
4. ！=  isnull
5. 查询里爱你高达
6. like
explain： type rows extra

数据库连接池大小  一般配置 100左右，针对4核CPU、10，能支持7k的并发量。
druid 连接池

分布式存储：
mysql  NoSQL   NewSQL   olap
MySQL： 分表  500w，2G大小；index  pool  buffer  size
tidb：
