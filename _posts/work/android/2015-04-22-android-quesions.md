---
layout: post
title:  "Android 学习和错误"
categories:
- work
tags:
- work
- android
---

> StartTime: 2015-04-22,ModifyTime:2017-01-01

昨天晚上Android课，题目是简单的对一个数累加的程序，结果自己写好竟然出错。

<!---more--->

后来发现两点错误：

1、是OnClickListener的导入的包不对，应该是这样做导入import android.view.View.OnClickListener;

2、是应该在MainActivity类的 onCreate()方法中，把super.onCreate(savedInstanceState);setContentView(R.layout.activity_main);写在最前面，这样后面才可以类似这样写findViewById(R.id.textView2);

原因我认为是界面R.layout.activity_main这个文件应该先编译，才能使用R类，否则我开始把setContentView(R.layout.activity_main);写在后面出错了。
