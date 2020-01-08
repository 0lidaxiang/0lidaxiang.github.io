---
layout: post
title:  "Solutions about MySQL Distributed"
rootCate: "work"
categories:
- architecture
tags:
- work
- mysql
- distributed
---

MySQL 主从复制、备份复制以及分布式集群的方案。
<!---more--->

## 1.主从复制



## 2.分布式
### 2.1 MySQL Group Replication

### 2.2  MySQL InnoDB Cluster
2.2.1
MySQL 5.7 引入了 Group Replication 功能，可以在一组 MySQL 服务器之间实现自动主机选举，形成一主多从结构。经过高级配置后，可以实现多主多从结构。

2.2.2
MySQL Router 是一个轻量级透明中间件，可以自动获取上述集群的状态，规划 SQL 语句，分配到合理的 MySQL 后端进行执行。

2.2.3 
MySQL Shell 是一个同时支持 JavaScript 和 SQL 的交互程序，可以快速配置 InnoDB Cluster。
