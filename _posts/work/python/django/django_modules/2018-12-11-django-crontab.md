---
layout: post
title:  "Django Crontab"
rootCate: "work"
categories:
- Python
tags:
- work
- Python3
- Django
- Crontab
---

Django-crontab实现Django定时任务,因为celery 插件学习曲线较大，这个小的需求就使用django-crontab 解决。

<!---more--->


## 安装
```
pip install django-crontab
```

添加app名称到 settings.py中
```
INSTALLED_APPS = (
        'django_crontab',
        ...
    )
```

settings 配置定时任务:
```
CRONJOBS = [
    ('*/5 * * * *', 'myapp.cron.my_scheduled_job')
]
```

cronjob 时间配置说明:
```
5 4 * * * At 04:05.
5 1/2 * * * //At minute 5 past every 2nd hour from 1 through 23.
* */2 * * * //At every minute past every 2nd hour.
12 12 2 * * //At 12:12 on day-of-month 2
```

5个参数从左到右分别是： 分钟、小时、天数、月份、年份。
```
*	any value
,	value list separator
-	range of values
/	step values
```

## 启动

1. 以上都完成后，需要执行
```
python3 manage.py crontab add
```
将任务添加并生效。

2. 3显示当前的定时任务
```
python3 manage.py crontab show
```

3. 删除所有定时任务
```
python3 manage.py crontab remove
```

4. 重启django服务。 执行 `corntab -e `
应该是可以看到系统中创建了该定时任务。

说到底，只是django-crontab插件对linux底层的调用，不确定这个方法在windows 上是否生效。
```


## 参考列表
[django-crontab 定时执行任务方法](https://blog.csdn.net/sinat_21302587/article/details/72831002)

[利用 Django REST framework 编写 RESTful API（drf的filter）](https://github.com/kraiz/django-crontab)

[cron时间配置](https://crontab.guru/)
