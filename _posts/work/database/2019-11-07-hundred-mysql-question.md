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


## 4. MySql Host is blocked because of many connection errors 问题(The host_cache Table问题)
原因：　　同一个ip在短时间内产生太多（超过mysql数据库max_connection_errors的最大值）中断的数据库连接而导致的阻塞；

解决办法2种：
1. 进入mysql控制台，执行：flush hosts;
2. 根治办法：max_connect_errors修改，以及查出引起连接错误的地方

## 5. MySQL 性能调优
可以调优的关键指标包括： 
1. IOPS：Input/Output operation Per Second, 每秒处理的IO请求次数。
2. QPS：Query Per Second，每秒请求（查询）次数。这
3. TPS：Transaction Per Second，每秒事务数。TPS参数MySQL原生没有提供，如果需要我们自己算，可以利用计算的公式：TPS = (Com_commit + Com_rollback) / Seconds
具体内容可以看 [文章 - Mysql性能调优与测试](https://juejin.im/entry/59eee654f265da432a7ac432)

5. 查看 MySQL 版本
若没有连接到 MySQL 服务器，使用 `mysql\bin>mysql -V`
若如果已经连接到了MySQL服务器，则运行下面的命令：`mysql> select version();`

6. MySQL时间函数 date_sub(), weekday(), curdate()
   date_sub
含义: 从日期减去指定的时间间隔.
语法格式: SELECT DATE_SUB(date,INTERVAL expr unit)
案例: select date_sub(curdate(),INTERVAL WEEKDAY(curdate())-26 DAY)

日期表示: 年-月-日
时间表示: 年-月-日 时:分:秒

解读:
select curdate();   #获取当前日期
select WEEKDAY(curdate());   #WEEKDAY函数返回一个日期的工作日索引值，即星期一为0，星期二为1，星期日为6。
select WEEKDAY(curdate()) - 26;
select date_sub('2020-02-24', INTERVAL 26 DAY);  #当前日期减去26天的时间
select date_sub('2020-02-24', INTERVAL -26 DAY); #当前日期减去负26天的时间,即加26天

7. MySQL 查看表占用空间大小
```
1，切换数据库
use information_schema;

2，查看数据库使用大小
select concat(round(sum(data_length/1024/1024),2),’MB’) as data from tables where table_schema=’DB_Name’ ;

3，查看表使用大小
select concat(round(sum(data_length/1024/1024),2),’MB’) as data from tables where table_schema=’DB_Name’ and table_name=’Table_Name’;
```

## 参考文献
[MySQL慢查询（一） - 开启慢查询](https://www.cnblogs.com/luyucheng/p/6265594.html)
[The host_cache Table](https://dev.mysql.com/doc/refman/5.6/en/host-cache-table.html)
[MySQL查看表占用空间大小](https://blog.csdn.net/qq_21683643/article/details/81003136?utm_medium=distribute.pc_relevant.none-task-blog-BlogCommendFromMachineLearnPai2-1.nonecase&depth_1-utm_source=distribute.pc_relevant.none-task-blog-BlogCommendFromMachineLearnPai2-1.nonecase)