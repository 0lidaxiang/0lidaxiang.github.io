---
layout: post
title:  "Flutter 在 Ubuntu 18 下的安装和学习"
categories:
- android
rootCate: "work"
tags:
- work
- Android
- Flutter
---

Flutter 是一个开放源代码 SDK，用于创建面向 iOS 和 Android 的高性能、高保真移动应用。Flutter 框架让您可以轻松构建在应用中反应流畅的界面，同时可减少同步和更新应用视图所需的代码量。本文是在 Ubuntu 18 下的安装和学习 Flutter 的文章。后续陆续更新其他教程。

<!---more--->

## Install
```
sudo snap install android-studio --classic  
sudo apt-get install dart
sudo vim /etc/profile
export PATH=/home/hekaiyou/flutter/bin:$PATH
source /etc/profile

```

之后要打开 android-studio ，一路确定会下载一些东西。否则下面的 doctor 命令会检查说不通过。

上面修改了 profile 好像没用，然后还是进去 bin 再执行命令。
```
cd ~/flutter/bin/;./flutter doctor
 ./flutter doctor --android-licenses
```

## Reference
[1]: https://blog.csdn.net/hekaiyou/article/details/52874796 "Flutter基础—开发环境与入门"
[2]: https://juejin.im/post/5ab07fe6f265da23815573c0 "Flutter开发环境配置"
[3]: https://juejin.im/post/5a97c1a6518825556a71cf11 "[Flutter]开始使用：配置编辑器"
