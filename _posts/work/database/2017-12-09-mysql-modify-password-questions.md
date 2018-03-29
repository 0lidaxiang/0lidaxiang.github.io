---
layout: post
title:  "Quesions about MySQL/Mariadb modify password"
categories:
- work
tags:
- work 
- database
- MySQL
---

> StartTime: 2017-12-09,ModifyTime:2017-12-09

<!---more--->

## Modify root's password
```
MariaDB [(none)]> sudo mysqld_safe --skip-grant-tables &
```
New terminal:
```
MariaDB [(none)]> mysql -u root
MariaDB [(none)]> UPDATE user SET password=PASSWORD("your_password") WHERE user='root' AND Host = 'localhost';
MariaDB [(none)]> FLUSH PRIVILEGES;
```
Check result:
```
MariaDB [(none)]> select user, host, password, plugin, authentication_string from mysql.user;
```
## Modify the login method
If you try the method
IDENTIFIED VIA  **unix_socket**  should be IDENTIFIED BY PASSWORD.
```
MariaDB [(none)]> SHOW GRANTS FOR 'root'@'localhost';
GRANT ALL PRIVILEGES ON *.* TO 'root'@'localhost' IDENTIFIED VIA unix_socket USING '*A4B6157319038724E3560894F7F932C8886EBFCF' WITH GRANT OPTION |
| GRANT PROXY ON ''@'%' TO 'root'@'localhost' WITH GRANT OPTION
```

The column of **plugin,authentication_string** should be null.
```
MariaDB [(none)]> select user, host, password, plugin, authentication_string from mysql.user;

```

## References:  
[Modify root's password](http://www.cnblogs.com/wangs/p/3346767.html)  
[Modify root's password](https://www.digitalocean.com/community/tutorials/how-to-reset-your-mysql-or-mariadb-root-password)  
[Add mysql user](http://www.jianshu.com/p/ae78ce8d8e14)
