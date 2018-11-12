---
layout: post
title:  "Nginx uwsgi config for Django"
rootCate: "work"
categories:
- Python
tags:
- work
- Python3
- Django
- nginx
- uwsgi
---

总结 Django Framework 可以利用的第三方库，以备后用。

<!---more--->

server{}需要插入到nginx.conf下的http里面。表示会监听对 listen 后写的 8000 端口的请求，并将转发给 uwsgi_pass 后的端口8001，而另一个terminal窗口里uwsgi 会启动8001端口在运行。

<font color="#dd0000"> 前端->nginx: 8000->uwsgi: 8001 </font>

如果不需要uwsgi的协助，则可以配置成location  /static 后的形式，nginx会把对8000端口的请求转发到alias 后面的文件夹里的index。
<font color="#dd0000"> 前端->nginx: 8000->project_index_html </font>

启动uwsgi命令：
```
uwsgi --ini      ***.ini
```
nginx.conf 里的配置：
```
server{
		listen 8000;
		server_name  localhost;
		#root /home/lidaxiang/MES_ENV/MES/dist;		
		location  / { 
		    uwsgi_pass 127.0.0.1:8001;
		    include uwsgi_params;	    
		}
		location  /static {
		    alias /home/lidaxiang/MES_ENV/MES/dist/static;
		    #index index.html;
		    #proxy_pass http://127.0.0.1:8001;
		}
	}
```

另外，根据网上总结的资料，除了需要在 setting.py 里面新增一行 ASGI_APPLICATION 这个变量，另外在 nginx.conf 里面需要新增下面这个配置，用于转发 websocket 请求给 daphne 这种专门用于接收 websocket 的服务器：
```
upstream websocket {
	    server 127.0.0.1:8077;
	}																																	
	server{
		listen 8777;
		location  / {
		    proxy_pass http://websocket;
		    proxy_http_version 1.1;
		    proxy_set_header Upgrade $http_upgrade;
		    proxy_set_header Connection "Upgrade";
		}
	}
```

uwsgi 里 ini 文件的配置：
```
[uwsgi]
#http = :8001
#socket = :8000
socket=127.0.0.1:8001（如果需要nginx，则需要使用socket配置）
socket = /home/my_project/my_project.sock  # socket文件的位置，运行时自动生成，但是试验发现并不会生成

# the base directory (full path)
chdir = /home/my_project_name/  # 项目文件夹的位置

# Django's wsgi file
wsgi-file = my_project_name/wsgi.py
module = myproject.wsgi:application

daemonize = /home/myproject/myproject.log  # 存储运行的日志文件， myproject 是我的项目文件夹

master = true # 指定启动主进程
chmod-socket = 664  # 运行时的权限

# maximum number of worker processes ， 设置工作进程的数量，根据电脑配置
processes = 4

#thread numbers startched in each worker process ，根据电脑配置
threads = 2


vacuum = true # 当服务器退出时自动删除unix socket文件和pid文件
```

## 参考文档
[解决nginx+uwsgi部署Django的所有问题](解决nginx+uwsgi部署Django的所有问题)
[python 使用Nginx和uWSGI来运行Python应用](https://www.cnblogs.com/Erick-L/p/7066455.html)
