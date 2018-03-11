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
