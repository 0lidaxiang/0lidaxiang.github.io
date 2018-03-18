---
layout: post
title:  Linux 远程连接与 SCP 复制 Files"
categories:
- work
tags:
- work Linux Fedora command
---

> StartTime: 2016-03-15,ModifyTime:2016-03-15

<!---more--->

## 远程连接与
首先在本机上，执行以下命令(假设服务器地址为192.168.0.11，假设远程服务器用户为user):

1. $cd ~/.ssh

2. $ssh-keygen   -t   rsa
      然后一直按回车键，就会按照默认的选项将生成的密钥保存在.ssh/id_rsa文件中。

3. $cp id_rsa.pub authorized_keys
      这步完成后，正常情况下就可以无密码登录本机了，即ssh localhost，无需输入密码。但是往往出现端口拒绝错误，因为本机22端口一般不开放。

4. $scp authorized_keys summer@192.168.0.11:/home/user/.ssh
      把刚刚产生的authorized_keys文件拷一份到服务器上.　　

5. $chmod 600 authorized_keys
      接下来，继续执行ssh命令连接到服务器，第一次需要输入进入服务器的root密码（默认一般是root用户），以后就不用了。命令如下：
      $ssh root@192.168.0.11
      也可以这样连接指定的user用户$ssh user@192.168.0.11 ，这时候就要输入服务器user用户的密码了。
> 参考文献：http://haitao.iteye.com/blog/1744272

## 与远程服务器进行文件和目录的交互操作
1.   获取远程服务器上的目录(传文件则去掉-r参数)
scp -P 2222 -r root@www.vpser.net:/root/lnmp0.4/ /home/lnmp0.4/
    上端口大写P 为参数，2222 表示更改SSH端口后的端口，如果没有更改SSH端口可以不用添加该参数。-r 参数表示递归复制（即复制该目录下面的       文件和目录）；root@www.vpser.net 表示使用root用户登录远程服务器www.vpser.net，:/root/lnmp0.4/ 表示远程服务器上的目录，最后面                     的/home/lnmp0.4/表示保存在本地上的路径。
2.  上传本地目录到服务器中(传文件则去掉-r参数)
   scp -P 2222 -r /home/lnmp0.4/ root@www.vpser.net:/root/lnmp0.4/
  上端口大写P 为参数，2222 表示更改SSH端口后的端口，如果没有更改SSH端口可以不用添加该参数。-r 参数表示递归复制（即复制该目录下面的文    件和目录）；/home/lnmp0.4/表示准备要上传的目录，root@www.vpser.net 表示使用root用户登录远程服务器www.vpser.net，:/root/lnmp0.4/ 表示      保存在远程服务器上的目录位置。
> 参考文献：http://biohazard2k.blog.51cto.com/68212/506583
