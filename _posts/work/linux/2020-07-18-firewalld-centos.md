---
layout: post
title:  "Centos firewalld service"
rootCate: "work"
categories:
- live
tags:
- work
- centos
- firewalld
---

Centos firewalld service
<!---more--->

## 开放端口
永久的开放需要的端口
```
//Enable firewall
systemctl enable firewalld
systemctl start firewalld
systemctl status firewalld

sudo firewall-cmd --zone=public --add-port=3000/tcp --permanent
sudo firewall-cmd --reload

// 之后检查新的防火墙规则
firewall-cmd --list-all
```

## 关闭防火墙
由于只是用于开发环境，所以打算把防火墙关闭掉

```
//临时关闭防火墙,重启后会重新自动打开
systemctl restart firewalld


//Disable firewall
systemctl disable firewalld
systemctl stop firewalld
systemctl status firewalld
```

## 检查防火墙状态
```
firewall-cmd --state
firewall-cmd --list-all
```