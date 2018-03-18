---
layout: post
title:  "HTML Experience"
categories:
- work
tags:
- work web_frontEnd  HTML Experience
---

> StartTime: 2017-12-12,ModifyTime: 2017-12-12

<!---more--->

1. Div
margin两层div才能用
width设置100%才可以不随大屏变化

//根据这个定位，可以实现对图片的居中，并且多余的溢出被隐藏。父div设置overflow:

2. JS 修改 HTML
js改的input会不激发onchange，那么可以再用val（）方法改变时，顺手来个change()方法，如$("#sheng3").val($("#sheng2").html()).change();

jquery对象和dom对象不一样

注册事件

html()  针对div

val()针对input


## HTML upload by FormData
**1、如何使用**
use `multipart/form-data` when your form includes any `<input type="file">` elements.

**2、怎么用ajax获取传递**
```
var formdata = new FormData();
formdata.append('name','fdipzone');
formdata.append('gender','male');
//或者
var form = document.getElementById('form1');
var formdata = new FormData(form);
```
**3、服务端需要做什么**
java版本解决：
http://www.blogjava.net/xyzroundo/articles/186217.html
php版本解决（使用 $_POST函数就可以接收）：
http://blog.csdn.net/fdipzone/article/details/38910553
