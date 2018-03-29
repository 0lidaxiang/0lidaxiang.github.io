---
layout: post
title:  "Java 泛型"
categories:
- work
tags:
- work
- Java
---

> StartTime: 2015-08-24,ModifyTime:2017-01-01

<!---more--->

> 主要参考：
		http://www.runoob.com/java/java-generics.html
		http://download.csdn.net/detail/qeveeqnui/6206751

## 定义：

		Java泛型（ generics ）是JDK 5中引入的一个新特性,泛型提供了编译时类型安全检测机制，该机制允许程序员在编译时检测到非法的类型。
		泛型（Generic type 或者 generics）是对 Java 语言的类型系统的一种扩展，以支持创建可以按类型进行参数化的类甚至是参数化的方法。
		Java泛型方法和泛型类支持程序员使用一个方法指定一组相关方法，或者使用一个类指定一组相关的类型。
		可以定义多个类型参数，

## 下面是定义泛型类的规则：

		可以把类型参数看作是使用参数化类型时指定的类型的一个占位符，就像方法的形式参数是运行时传递的值的占位符一样。常见的用处有在map和list里。
		泛型类的声明和非泛型类的声明类似，除了在类名后面添加了类型参数声明部分。
		和泛型方法一样，泛型类的类型参数声明部分也包含一个或多个类型参数，参数间用逗号隔开。一个泛型参数，也被称为一个类型变量，是用于指定一个泛型类型名称的标识符。因为他们接受一个或多个参数，这些类被称为参数化的类或参数化的类型。
		这种语法中，implements和extends统一写成extends。

		Example：Problem<T extends Comparable

## 下面是定义泛型方法的规则：

		1所有泛型方法声明都有一个类型参数声明部分（由尖括号分隔），该类型参数声明部分在方法返回类型之前（在下面例子中的<E>）。
		2每一个类型参数声明部分包含一个或多个类型参数，参数间用逗号隔开。一个泛型参数，也被称为一个类型变量，是用于指定一个泛型类型名称的标识符。
		3类型参数可以被用来声明返回值类型，并且能作为泛型方法得到的实际参数类型的占位符。
		4泛型方法方法体的声明和其他方法一样。注意类型参数只能代表引用型类型，不能是原始类型（像int,double,char的等）。

## 另外关于泛型的特别之处：

	<T extends Comparable<? super T>>
	首先这是运用了java的泛型
	①extends后面跟的类型如<任意字符 extends 类/接口>表示泛型的上限
	②同样的super表示泛型的下限
	③<T extends Comparable<? super T>>这里来分析T表示任意字符名，extends对泛型上限进行了限制即T必须是Comparable<? super T>的子类，然后<? super T>表示Comparable<>中的类型下限为T！
