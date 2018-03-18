---
layout: post
title:  "在Fedora25中安装和使用Laravel 框架"
categories:
- work
tags:
- work web_backEnd  Laravel
---

> StartTime: 2017-05-22,ModifyTime:2017-05-22

> 至于Lamp环境配置，请自行百度。
> 本篇中安装操作可能需要连接到国外网站用于下载 laravel。
> 得出来的经验是一但有错误就立马研究日志。Apache日志。

<!---more--->

## Install
```
[root]$dnf install composer
[user]$mkdir code    //用来放所有的项目，以免和主目录下其他东西混合
//第一种方法，通过laravel新建program
[user]$export PATH="~/.config/composer/vendor/bin:$PATH"
//或者有人是执行
//export PATH="$PATH:$HOME/.config/composer/vendor/bin"
//或者有人执行
export PATH="~/.composer/vendor/bin:$PATH"
//这个要根据具体composer安装路径来，我是第一种，网络资料比较少。
//这种效果按照参考资料4中解释是暂时的。
[user]$composer global require "laravel/installer"
[user]$laravel new blog
//第二种方法：[user]$composer create-project --prefer-dist laravel/laravel blog
//要稍等几十秒，然后屏幕上陆续会显示当前进度。
```
## Use And Test
1.Method 1 : Use Mini-Server In PHP (version >5.4)
输入
```
[user]$php artisan serve //这个命令应该是在上述文件夹内执行才有用
```
启动php内置server，再在浏览器中访问 `http://localhost:8000` ，如果可以看到本页最下方的图那样，表示成功安装环境。


2.Method 2 : Use Apache Server
在超级管理员的权限下给 /etc/httpd/httpd.conf  添加 :
```
Listen 8008  #监听的端口
<VirtualHost *:8008>
    ##ServerAdmin webmaster@dummy-host.example.com
    DocumentRoot "/home/xxx/code/blog/public"
    ##ServerName dummy-host.example.com
    ##ServerAlias www.dummy-host.example.com
    <Directory />
      AllowOverride All
      #Require all denied
    </Directory>
    ErrorLog "logs/laravel.com-error.log"
    CustomLog "logs/laravel.com-access.log" common
</VirtualHost>
```
如果还出现关于 Apache 的错误，可能还需要把根目录的权限做修改。但一般不会出现。

下一步是让 Apache 可以访问位于非默认目录下的网站文件。主要是修改文件夹权限
```
[root]$chmod -R 755 /home/xxx/blog/   //也许不用修改
```
与设定 selinux 安全政策配置。
```
//方法一，临时半关闭selinux
[root]$setenforce 0   

//方法二，通过chcon授权给apache可以读写这个文件夹
[root]$chcon -R -t httpd_sys_content_rw_t /home/lidaxiang/blog

//方法三，基本判定是个没用的一个方法。备份一下。
//首先为 /srv/www 这个目录下的文件添加默认标签类型：
[root]$semanage fcontext -a -t httpd_sys_content_t '/srv/www(/.*)?'
//然后用新的标签类型标注已有文件：
[root]$restorecon -Rv /srv/www 之后 Apache 就可以使用该目录下的文件构建网站了。
```
在浏览器中访问 `http://localhost:8008` ，如果可以看到本页最下方的图那样，表示成功安装环境。

## If you  install successlly, you will see
![Laravel成功安装](http://img.blog.csdn.net/20170224235028491?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQveGllcWlhb3hpeWFuZw==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)


## 参考资料
1. [基本安装步骤](https://laravel.com/docs/5.4#installing-laravel)
2. [检查、临时关闭以及 semanage 授权](http://os.51cto.com/art/201105/265956.htm)
3. [chcon 命令授权文件夹 selinux 权限 以及出现莫名其妙的被拒绝时要检查每级folder 的 selinux 权限](http://ericbbs.blogspot.tw/2007/10/apache-under-selinux-apache.html)
4. [Linux系统添加、修改、删除PATH环境变量](http://www.cnblogs.com/bionmr/p/4149527.html)
5. [.htaccess pcfg_openfile 错误原因之一，另一个是 selinux ](http://www.ixueyi.com/jingyan/122200.html)
6. [Apache 配置虚拟主机三种方式](http://www.cnblogs.com/hi-bazinga/archive/2012/04/23/2466605.html)
