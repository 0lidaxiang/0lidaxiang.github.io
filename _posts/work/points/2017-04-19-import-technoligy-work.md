---
layout: post
title:  "Import Technoligy In Develop"
categories:
- work
tags:
- work points
---

> StartTime: 2017-02-05,ModifyTime:2017-04-25
<!---more--->

> 主要内容整理自: [构建大型网站（百万级访问量）的技术准备](https://www.biaodianfu.com/thinking-before-building-site.html)

> StartTime: 2017-04-19,ModifyTime:2017-04-19

## 1.开发之外的考虑
代码管理考虑 git or svn 。

开发语言选择前端可以混合适量 PHP 这种脚本语言，后端根据需求。但 PHP 可能要注意模式建构和代码管理，而 Java 这种就有固定的模式可以依循。

web服务器可以既跑程序又当内存缓存，数据库服务器则只跑主数据库（假如是MySQL的话），备份服务器要把web配置、缓存配置、数据库配置配置地跟前两台一致，这样把备份服务器换个ip就切换上去了。

三种机房尽量不要选：联通访问特别慢的电信机房、电信访问特别慢的联通机房、电信联通访问特别慢的移动或铁通机房。

LAMP Or LNMP 选择要注意版本搭配并及时更新，以利于安全。

## 2.database table engines:  
> About installation, you should read and below each steps carefully which will set root password, remove anonymous users, disallow remote root login, and remove the test database and access to secure MariaDB.

[how to look up it](http://coolnull.com/2759.html)  
[how to modfify it globally](http://stackoverflow.com/questions/2286813/how-to-set-the-default-storage-engine-to-innodb-in-xampp)  
[Installation and Security optimization of MariaDB](http://www.tecmint.com/install-mariadb-in-linux/)

对于mysql，什么样的表用 myisam ，什么样的表用 innodb，在开发之前要确定。复制策略、分片策略，也要确定。表引擎方面，一般，更新不多、不需要事务的表可以用 myisam，需要行锁定、事务支持的，用 innodb。

1. 设计表结构时常常设计很多冗余，虽然不符合传统范式，但为了速度考虑还是值得的，要求高的情况下甚至要杜绝联合查询。编程时得多注意数据一致性。

2. 复制策略方面，多主多从结构也最好一开始就设计好，代码直接按照多主多从来编写，用一些小技巧来避免复制延时问题，并且还要解决多数据库数据是否一致，可以自己写或者找现成的运维工具。

3. 分片策略。总会有那么几个表数据量超大，这时分片必不可免。分片有很多策略，从简单的分区到根据热度自动调整，依照具体业务选择一个适合自己的。避免自增ID作为主键，不利于分片。

NoSQL 只是一个概念。实际应用中，网站有着越来越多的密集写操作、上亿的简单关系数据读取、热备等，这都不是传统关系数据库所擅长的。NoSQL 在测试中，这些几乎都达到了每秒至少一万次的写操作，内存型的甚至5万以上。例如 MongoDB，几句配置就可以组建一个复制+自动分片+ failover的环境，文档化的存储也简化了传统设计库结构再开发的模式。很多业务是可以用这类数据库来替代 MySQL 的。

## 3.缓存
数据库很脆弱，一定要有缓存在前面挡着，其实我们优化速度，几乎就是优化缓存，能用缓存的地方，就不要再跑到后端数据库那折腾。缓存有持久化缓存、内存缓存，生成静态页面是最容易理解的持久化缓存了，还有很多比如 varnish 的分块缓存、内存缓存 (eg. Redis)、 缓存服务器 [memcached](http://memcached.org/) 首当其冲。缓存更新可用被动更新和主动更新。被动更新的好处是设计简单，缓存空了就自动去数据库取数据再把缓存填上，但容易引发雪崩效应，一旦缓存大面积失效，数据库的压力直线上升很可能挂掉。主动缓存可避免这点但是可能引发程序取不到数据的问题。这两者之间如何配合，程序设计要多动脑筋。

NoSQL 还有其他类别：

|Title <th colspan=3>键值存储</th> | 文档存储 | 图存储 |
|---|---|---|---|---|---|
|**Class**| 最终一致性键值存储 | |  | 内存键值存储  |  持久化键值存储 |
|**Content** | Cassandra  Dynamo  Riak  Hibari  Virtuoso  Voldemort|<font color=#DAA520>Memcached  Redis</font>  Oracle Coherence  NCache  Hazelcast  Tuple space  Velocity  |  BigTable  LevelDB  Tokyo Cabinet  Tarantool  TreapDB  Tuple space | <font color=#DAA520>MongoDB</font>  CouchDB  SimpleDB  Terrastore  BaseX   Clusterpoint  Riak  No2DB |  FlockDB  DEX  Neo4J  AllegroGraph  InfiniteGraph  OrientDB  Pregel |

## 4.队列
用户一个操作很可能引发一系列资源和功能的调动，这些调动如果同时发生，压力无法控制，用户体验也不好，可以把这样一些操作放入队列，由另几个模块去异步执行，例如发送邮件，发送手机短信。开源队列服务器很多，性能要求不高用数据库当做队列也可以，只要保证程序读写队列的接口不变，底层队列服务可随时更换就可以，类似 Zend Framework里的 Zend_Queue类，java.util.Queue 接口等。

## 5.文件存储
除了结构化数据，我们经常要存放其他的数据，像图片之类的。这类数据数量繁多、访问量大。典型的就是图片，从用户头像到用户上传的照片，还要生成不同的缩略图尺寸。存储的分布几乎跟数据库扩展一样艰难。不使用专业存储的情况下，基本都是靠自己的 NAS。这就涉及到结构。拿图片存储举例，图片是非常容易产生热点的，**有些图片上传后就不再有人看，有些可能每天被访问数十万次，而且大量小文件的异步备份也很耗费时间**。  

为了将来图片走 cdn 做准备，一开始最好就将图片的域名分开，且不用主域名。很多网站都将 cookie 设置到了.domain.ltd，如果图片也在这个域名下，很可能因为 cookie 而造成缓存失效，并且占多余流量，还可能因为浏览器并发线程限制造成访问缓慢。  

如果用普通的文件系统存储图片，有一个简单的方法。**计算文件的hash值，比如 md5，以结果第一位作为第一级目录，这样第一级有16个目录。从0到F，可以把这个字母作为域名**，0.yourimg.com到f.yourimg.com（客户端dns压力会增大），还可以扩展到最多16个NAS集群上。第二级可用年月例如，201011，第三级用日，第四级可选，根据上传量，比如am/pm，甚至小时。最终的目录结构可能会是 e/201008/25/am/e43ae391c839d82801920cf.jpg。rsync备份时可以用脚本只同步某年某日某时的文件，避免计算大量文件带来的开销。当然最好是能用专门的分布式文件系统或更专业点的存储解决方案。

## 6.架构 Arichitecture
初期架构一般比较简单，**web负载均衡+数据库主从+缓存+分布式存储+队列**。按照将来会有N多WEB，N多主从关系，N多缓存，N多xxx设计就行。

设计上考虑到缓存失效时的雪崩效应、主从同步的数据一致性和时间差、队列的稳定性和失败后的重试策略、电源烧坏、文件存储的效率和数据库备份复制出错等等意外情况。

## 7.安全与加密
#### 密码学的三大作用：  
加密（ Encryption）、认证（Authentication），鉴定（Identification）

#### 已经不安全的加密方法：  
Base64, MD5(现在多用于计算哈希值), SSL(1~3), DES, SHA-1, SHA-2.注意这些算法不安全是意味着即便重复多次加密也没有用，不要自作聪明。

#### 截至2017年3月31日仍安全的加密算法：  
SHA-2(But not recommend), SHA3, AES, RSA, TLS(1.1,1.2)
即便这些尚安全的加密算法也一定要选择最新版本而不是旧版。

#### 使用方法
多数的语言 Python, Java(Android) 等等都有自己的相关加密的 library。
