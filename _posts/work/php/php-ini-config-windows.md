本文主要是记录一下自己为了开启gd库的惨痛经历。（GD库是第三方函数库，可以在php中画图）

主要是针对从官网下载压缩包的安装方式。如果有权限问题，可以用管理员登录电脑去操作，一了百了，解决所有麻烦。

首先，应该在开启GD库之前要先把php.ini文件设置好。设置过程：

1. 将php下载包解压后的主目录下的php.ini-development 文件重命名为php.ini。
2. 将“;extension_dir = "ext" ”这一选项修改为“extension_dir = "你的php下载包解压后的主目录/ext“”。注意，这个修改的路径是你自己的ext文件夹的完整绝对路径，另外还要把最前面的逗号删除。PS:可以利用很多文本编辑器的搜索功能查找。
3. 打开apache压缩包主目录下conf文件夹里的httpd.conf文件，然后搜索  PHPIniDir 这个选项，然后修改它的值为自己下载的php压缩包解压后的主目录的完整绝对路径。
4. 接下来至于其他的开启另外的功能支持可以自行百度，不在本文范围内。
5. 自己写一个php文件测试，内容主要是phpinfo();    其实就是调用这个函数，在浏览器中访问这个文件，去查看它的loadfile选项里是否是正确的自己php压缩包解压后的位置。
6. 剩下的开启GD库支持也很简单了。直接搜索  ; extension=php_gd2.dl   然后删除最前面的分号就可以了。
希望能对你有所帮助。谢谢看完。
详细的windows下配置Apache\MySql\Php环境可以参照该博客：http://www.51gametek.com/?post=9