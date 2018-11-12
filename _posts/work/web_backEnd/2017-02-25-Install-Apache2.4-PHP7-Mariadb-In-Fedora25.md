---
layout: post
title:  "在Fedora25上安装Apache2.4 & PHP7 &Mariadb"
rootCate: "work"
categories:
- Web_BackEnd
tags:
- work
- web_backEnd
- LAMP
- Fedora
---

> StartTime: 2017-02-25,ModifyTime:2017-02-25

<!---more--->

## 1. Install Apache2.4 & PHP7 &Mariadb
```
dnf install httpd php mariadb
dnf install php-mysqlnd
```
## 2. Configure Mariadb
```
$ mysql
> use mysql;
```
For MySQL 5.7.6 and newer as well as MariaDB 10.1.20 and newer, use the following command.
```
> ALTER USER 'root'@'localhost' IDENTIFIED BY 'new_password';
```
For MySQL 5.7.5 and older as well as MariaDB 10.1.20 and older, use:
```
> SET PASSWORD FOR 'root'@'localhost' = PASSWORD('new_password');
```
After under commands ,
```
> FLUSH PRIVILEGES;
> exit;
$ systemctl restart mariadb.service  //重启服务
$ mysql -u root -p 'new_password';
> Welcome.....
```
Finish it ! Congratulation!
## 3.Check
1.在网站目录下新建 testphp.php 文件，用 vi 输入以下 code：
```
<?php
	phpinfo();
?>
```
2.在网站目录下新建 test.php 文件，用 vi 输入以下 code：
```
<?php
   $con = mysql_conncet('localhost','root','root');
   if(!$con){
      die("connet mysql failed".mysql.error());     
    }
   echo "connet mysql successful";       
?>
```
## 4. Question & Answer
 正常来说，只要执行命令就能完成安装。如果出错，可能需要注意 php 和 mariadb 版本问题。有时候最新版本不需要做什么额外动作。低版本可能需要开启配置什么。具体请根据 apache 的error.log 上网查询，有很多说明。

## 参考文章：
1. [CentOS 7 yum方式配置LAMP环境](http://www.cnblogs.com/zutbaz/p/4420791.html)
2. [PHP7 connect mysql by PDO](https://www.sitepoint.com/re-introducing-pdo-the-right-way-to-access-databases-in-php/)
3. [ How To Reset Your MySQL or MariaDB Root Password](https://www.digitalocean.com/community/tutorials/how-to-reset-your-mysql-or-mariadb-root-password)
