---
layout: post
title:  "Python string-datetime-convertion"
rootCate: "work"
categories:
- Python
tags:
- work
- Python3
---

总结 Python 中 String、datetime、date 的转换。

<!---more--->

## String to Datetime

```
str = '2012-11-19'
date_time = datetime.datetime.strptime(str,'%Y-%m-%d')
date_time
```

## Datetime to String
strftime("%Y-%m-%d %H:%M:%S"):
```
date_time.strftime('%Y-%m-%d')
```

## Time to timestamp
```
time_time = time.mktime(date_time.timetuple())
time_time
```

## date to date_time
```
date = datetime.date.today()
datetime.date(2012,11,19)
datetime.datetime.strptime(str(date),'%Y-%m-%d') #将date转换为str，在由str转换为datetime
datetime.datetime(2012,11,19,0,0)
```

## 日期加减几天
```
today=datetime.date.today()
oneday=datetime.timedelta(days=1)
yesterday=today-oneday
```

## With timezone
python自带timezone 获取今天0点的带时区的时间:
```
end_date_str = datetime.date.today().strftime("%Y-%m-%d") + " 00:00:00"
end_date_str = datetime.datetime.strptime(end_date_str, "%Y-%m-%d %H:%M:%S")
end_date = end_date_str.replace(tzinfo=timezone("Asia/Shanghai"))
```

django 获取带timezone的时间：
```
from django.utils import timezone
now = timezone.now()
> datetime.datetime(2018, 2, 22, 3, 13, 2, 383795, tzinfo=<UTC>)
new = timezone.localtime(now)
> datetime.datetime(2018, 2, 22, 11, 13, 2, 383795, tzinfo=<DstTzInfo 'Asia/Shanghai' CST+8:00:00 STD>)
```
