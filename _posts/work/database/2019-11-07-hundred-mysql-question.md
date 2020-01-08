---
layout: post
title:  "100 Questions about MySQL"
rootCate: "work"
categories:
- architecture
tags:
- work
- mysql
---

记录一些常见的 MySQL 问题。
<!---more--->

### 1. MySQL 存储引擎及其优点
MyiSAM 


## 2. 查看系统正在运营的MySQL语句
`show processlist` 命令
SHOW PROCESSLIST显示哪些线程正在运行。您也可以使用mysqladmin processlist语句得到此信息。
各列的含义和用途：
ID列：一个标识，你要kill一个语句的时候很有用，用命令杀掉此查询 /*/mysqladmin kill 进程号。

user列：显示单前用户，如果不是root，这个命令就只显示你权限范围内的sql语句。

host列：显示这个语句是从哪个ip的哪个端口上发出的。用于追踪出问题语句的用户。

db列：显示这个进程目前连接的是哪个数据库。

command列：显示当前连接的执行的命令，一般就是休眠（sleep），查询（query），连接（connect）。

time列：此这个状态持续的时间，单位是秒。

state列：显示使用当前连接的sql语句的状态，很重要的列，后续会有所有的状态的描述，请注意，state只是语句执行中的某一个状态，一个 sql语句，以查询为例，可能需要经过copying to tmp table，Sorting result，Sending data等状态才可以完成

info列：显示这个sql语句，因为长度有限，所以长的sql语句就显示不全，但是一个判断问题语句的重要依据。

### 3. 如何查看slowsql
#### 方法一：全局变量设置
将 slow_query_log 全局变量设置为“ON”状态

mysql> set global slow_query_log='ON'; 
设置慢查询日志存放的位置

mysql> set global slow_query_log_file='/usr/local/mysql/data/slow.log';
查询超过1秒就记录

mysql> set global long_query_time=1;
#### 方法二：配置文件设置
修改配置文件my.cnf，在[mysqld]下的下方加入
```
[mysqld]
slow_query_log = ON
slow_query_log_file = /usr/local/mysql/data/slow.log
long_query_time = 1
```

重启MySQL服务: service mysqld restart

查看是否成功：
```
mysql> show variables like 'slow_query%';
mysql> show variables like 'long_query_time%';
```

其他参数解释:
1. slow_query_log 这个参数设置为ON，可以捕获执行时间超过一定数值的SQL语句。
2. long_query_time 当SQL语句执行时间超过此数值时，就会被记录到日志中，建议设置为1或者更短。
3. slow_query_log_file 记录日志的文件名。
4. log_queries_not_using_indexes  这个参数设置为ON，可以捕获到所有未使用索引的SQL语句，尽管这个SQL语句有可能执行得挺快。

#### 测试
执行`select sleep(2);` ，然后使用命令 `cat /usr/local/mysql/data/slow.log`查看是否生成慢查询日志.




## 参考文献
[MySQL慢查询（一） - 开启慢查询](https://www.cnblogs.com/luyucheng/p/6265594.html)