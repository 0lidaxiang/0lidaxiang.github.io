---
layout: post
title:  "Apache config in WindowsServer"
categories:
- work
tags:
- work
- web_backEnd  
- Windows
---

> StartTime: 2017-02-23,ModifyTime: 2017-02-23

<!---more--->

# 0.Install querstion
1. 模块msvcr100.dll已加载但找不到入口点解决方法：
网上百度是说注册表没删除干净，但是实际新系统应该不存在这个问题。后来我发现是自己在C盘的System32和SysWOW64里面传错了文件。

2. msvcr100.dll   msvcr110.dll缺失
云盘地址：http://pan.baidu.com/s/1qWMlPbm

3. 其他环境完整配置过程请参考：
http://secsky.sinaapp.com/91.html

# 1.修改网页根目录及端口(必学)
修改httpd.conf 文件
```
ServerName www.xxxxxx.com:80 #主站点名称（网站的主机名）。

ServerAdmin admin@xxx.com #管理员的邮件地址。

DocumentRoot "/xxx/web/xxxx" #主站点的网页存储位置。
```
# 2.基本设置-设置管理员相关以及网站首页地址
修改httpd.conf 文件
```
<IfModule dir_module>
    DirectoryIndex index.php
</IfModule>
```
# 3.禁止访问文件目录
修改httpd.conf 文件
```
<Directory />#根目录
以及
<Directory "/mnt/web/clusting"> #主站点目录
下面都要加上
Options None
AllowOverride None
Order allow,deny
Allow from all
```
# 4.性能参数配置（进程线程配置）
修改httpd.conf 文件
## 4.1.启用MPM模块配置文件

在默认情况下，Apache的MPM模块配置文件并没有启用。因此，我们需要在httpd.conf文件中启用该配置文件，如下所示：
```
# Server-pool management (MPM specific)
Include conf/extra/httpd-mpm.conf (去掉该行前面的注释符号"#")
```
## 4.2.修改MPM模块配置文件中的相关配置
在Apace安装目录/conf/extra目录中有一个名为httpd-mpm.conf 的配置文件。该文件主要用于进行MPM模块的相关配置。
在上一步4.2启用MPM模块配置文件后，我们就可以使用文本编辑器打开 httpd-mpm.conf 配置文件，我们可以看到，在该配置文件中有许多<IfModule>配置节点，如下图所示：
```
#由于mpm_winnt模块只会创建1个子进程，因此这里对单个子进程的参数设置就相当于对整个Apache的参数设置。

<IfModule mpm_winnt_module>
ThreadsPerChild      150 #推荐设置：小型网站=1000 中型网站=1000~2000 大型网站=2000~3500
MaxRequestsPerChild    0 #推荐设置：小=10000 中或大=20000~100000
```
对应的配置参数作用如下：
***ThreadsPerChild*** ：每个子进程的最大并发线程数。
***MaxRequestsPerChild*** ：每个子进程允许处理的请求总数。如果累计处理的请求数超过该值，该子进程将会结束(然后根据需要确定是否创建新的子进程)，该值设为0表示不限制请求总数(子进程永不结束)。
该参数建议设为非零的值，可以带来以下两个好处：

	(1)可以防止程序中可能存在的内存泄漏无限进行下去，从而耗尽内存。
	(2)给进程一个有限寿命，从而有助于当服务器负载减轻的时候减少活动进程的数量。
# 5. 错误访问处理
修改httpd.conf 文件，以及在第一步对apache设置的根目录下创建新文件，命名为 missing.html
```
ErrorDocument 500 "The server made a boo boo."
ErrorDocument 404 /missing.html  <==將註解拿掉吧！
#ErrorDocument 404 "/cgi-bin/missing_handler.pl"
#ErrorDocument 402 http://www.example.com/subscription_info.html
```

```
//新建html文件，放在第一步对apache设置的根目录下，命名为 missing.html
<html>

<head>
    <meta http-equiv="Content-Type" content="text/html; charset=utf8">
    <title>错误</title>

    <head>

        <body>
            <font size=+2>找不到您要访问的网页</font>
            <br />
            <hr /> 您所输入的网址并不存在我们的服务器当中, 可能是因为该网页已经被管理员删除。
            点击
            <a href="/">这里</a>回到首页！ ^_^
            <br />
            <hr /> 若有任何问题，请联系管理员！
            <a href="mailto:0lidaxiang@gmail.com">0lidaxiang#(把#换成@)gmail.com</a>。
        </body>

</html>
```
# 7.压力测试以及调整日志写入
apache [warn] (OS 64)指定的网络名不再可用
解决办法：如果是apache2.0.49以上：
```
在httpd.conf（或mpm）文件中添加 Win32DisableAcceptEx 标记，如下：
<IfModule mpm_winnt.c>
ThreadsPerChild 1000
MaxRequestsPerChild  10000
Win32DisableAcceptEx
</IfModule>
这样可以允许并发连接更大一些。同时性能上也不会有明显的降低.
```
```
#如果上面的不起作用就在httpd-mpm.conf文件中的对应mpm_winnt_module中添加
AcceptFilter http none
AcceptFilter https none
```
压力测试：http://cloudchen.logdown.com/posts/247932/apache-jmeter-tool-for-load-test-and-measure-performance

# 参考文献：
1.[Apache对管理员邮箱、根目录、端口等基本配置(页面的(1))](http://liudaoru.iteye.com/blog/336338)
2.[Apache配置禁止访问目录](http://www.daixiaorui.com/read/44.html)
3.[Apache优化：修改最大并发连接数](http://www.365mini.com/page/apache-concurrency-configuration.htm)
4.[Apache 找不到網頁時的顯示訊息通知(页面的20.3.3)](http://cn.linux.vbird.org/linux_server/0360apache.php)
