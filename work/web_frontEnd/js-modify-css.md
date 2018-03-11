1.用js改css和style：

```
	var headTop = document.getElementById("headTop");
	// headTop.style.position = "fixed";
	    headTop.style.padding-Left = "40px";
	    headTop.style.width = "1150px";
```
2.用jquery改css：
```
	$("#searchDiv").css("width","1150px");
```

3.// 获取radio的value值方法一(jquery)
```
$('input[name=xxx]:checked').val();    (xxx不需要有引号包括)
```

   // 获取radio的value值方法二(js)
```
    function GetRadioValue(RadioName){
		var obj;
		obj=document.getElementsByName(RadioName);
		if(obj!=null){
			var i;
			for(i=0;i<obj.length;i++){
				if(obj[i].checked){
					return obj[i].value;
				}
			}
		}
		return null;
	}
```
