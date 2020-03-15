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
MySQL 主从复制 比较简单，但需要把已有的 MySQL 服务的 my.cnf 文件修改，再把 slave MySQL 服务的配置文件修改，最后重启两个服务。以下 1.1 ~ 1.4 是在 Django 中具体的用法。

#### 1.1 配置
Django默认的是default,我们按照它的格式直接添加一个新的配置：
```
DATABASES = {
 'default': {
 'ENGINE': 'django.db.backends.mysql',
 'HOST': '127.0.0.1', # 主服务器的运行ip
 'PORT': 3306, # 主服务器的运行port
 'USER': 'django', # 主服务器的用户名
 'PASSWORD': 'django', # 主服务器的密码
 'NAME': 'djangobase' # 数据表名
 },
 'slave': {
 'ENGINE': 'django.db.backends.mysql', 
 'HOST': '127.0.0.1',
 'PORT': 8306,
 'USER': 'django_slave',
 'PASSWORD': 'django_slave',
 'NAME': 'djangobase_slave'
 }
}
```



#### 1.2 手动操作方式
代码里可以直接操控数据库：
```
 models.User.objects.using('default').create
```
#### 1.3 自动操控方式
在settings.py中指定DATABASE_ROUTERS
```
DATABASE_ROUTERS = ["app001.db_router.MasterSlaveDBRouter"]
```

并新建 routers.py 文件：
```
class MasterSlaveDBRouter(object):
 """数据库主从读写分离路由"""
 
 def db_for_read(self, model, **hints):
 """读数据库"""
 return "slave"
 
 def db_for_write(self, model, **hints):
 """写数据库"""
 return "default"
 
 def allow_relation(self, obj1, obj2, **hints):
 """是否运行关联操作"""
 return True　
 ```
 
#### 1.4 存在问题
主要问题是: 同步延迟。
原因: 
1. 慢查询
2. 大事务同步慢
3. Binlog 同步时对 IO 有要求


## 2.分布式 MySQL 集群 -  MySQL InnoDB Cluster
#### 2.1  MySQL InnoDB Cluster
MySQL 5.7 终于实现了原生的基于InnoDB的集群功能。它由以下三个组件完成:

#### 2.2 MySQL Group Replication 
MySQL Group Replication（下简称MGR）准确来说是官方推出的高可用解决方案，基于原生复制技术，并以插件的方式提供。

MySQL 5.7 引入了 Group Replication 功能，可以在一组 MySQL 服务器之间实现自动主机选举，形成一主多从结构。经过高级配置后，可以实现多主多从结构。

#### 2.3 MySQL Router
MySQL Router 是一个轻量级透明中间件，可以自动获取上述集群的状态，规划 SQL 语句，分配到合理的 MySQL 后端进行执行。MySQL Router是InnoDB Cluster（MySQL 7.X）的一部分，MySQL 5.6 等版本数据库仍然可以使用Router作为其中间代理层。MySQL Router是MySQL Proxy的替代方案，MySQL官方不建议将MySQL Proxy用于生产环境。

当下游有多个MySQL Servers，无论主、从，Router可以对读写请求进行负载均衡。当下游某个Server失效时，Router可以将其从Active列表中移除，当其online后再次加入Active列表，即提供了Failover特性。通常建议基于“Agent”方式部署，即将Router与应用部署在机器上。Router通常是解决“MySQL集群规模性迁移”，比如跨机房部署、流量迁移、异构兼容，或者解决MySQL集群规模性宕机时快速切换等。

#### 2.4 MySQL Shell
MySQL Shell 是一个同时支持 JavaScript 和 SQL 的交互程序，可以快速配置 InnoDB Cluster。

#### 2.5 Admin API
Admin API：一个特殊的API通过MySQL Shell使用，可以用于对Innodb Cluster进行配置管理


#### 如何使用上述组建
1. 准备同一内网下多个mysql环境
2. 在任一台服务器上启动 mysql-shell
3. `dba.configureLocalInstance` 命令修正 MySQL 配置
4. 在主节点机器上使用`mysqlsh`命令，完成集群创建和子节点添加
5. 安装 mysqlrouter，使用主节点获取配置，启动 mysqlrouter
6. 测试请求是否被 SQL Router 负载给后端 MySQL 服务器

## 3. MySQL NDB Cluster
MySQL NDB Cluster 容易与MySQL InnoDB Cluster混淆，是另外一款产品，提供更高级别的可用性和冗余性。适用于分布式计算环境，使用内存型的NDB存储引擎。

## Refrences
[使用MySQL Router实现高可用、负载均衡、读写分离](https://blog.csdn.net/wzy0623/article/details/81103469)
[如何使用 MySQL 5.7 内置的 InnoDB 集群](https://zhuanlan.zhihu.com/p/31311700)
[如何看待MySQL发布的Group Replication](https://www.zhihu.com/question/53617036/answer/135776740)
[Django连接多个数据库并实现读写分离](https://zhuanlan.zhihu.com/p/84214079)
[MySQL InnoDB Cluster 详解](https://www.modb.pro/db/13606)
