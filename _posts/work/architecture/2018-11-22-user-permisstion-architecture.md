---
layout: post
title:  "User permisstion architecture"
rootCate: "work"
categories:
- architecture
tags:
- work
- user_permisstion
- architecture
---

总结用户与权限架构有关的基础概念，总结多种实现方法。
<!---more--->

## 1.RBAC
#### 1.1基本原理
基于角色的权限访问控制（Role-Based Access Control）作为传统访问控制（自主访问，强制访问）的有前景的代替受到广泛的关注。

RBAC认为权限授权实际上是Who、What、How的问题。在RBAC模型中，who、what、how构成了访问权限三元组,也就是“Who对What(Which)进行How的操作”。

在RBAC中，权限与角色相关联，用户通过成为适当角色的成员而得到这些角色的权限。在一个组织中，这就极大地简化了权限的管理。User和role的关系是Many-to-Many关系

+ 角色是为了完成各种工作而创造，由权限组成
+ 用户则依据它的责任和资格来被指派相应的角色，切换非常容易
+ 角色可依新的需求而赋予新的权限或回收

#### 1.2  RBAC 安全原则
RBAC支持三个著名的安全原则：最小权限原则，责任分离原则和数据抽象原则。
+ 最小权限原则: RBAC可以将其角色配置成其完成任务所需要的最小的权限集。

+ 责任分离原则: 通过调用相互独立互斥的角色来共同完成敏感的任务而体现，比如要求一个计帐员和财务管理员共参与同一过帐。

+ 数据抽象: 通过权限的抽象来体现，如财务操作用借款、存款等抽象权限，而不用操作系统提供的典型的读、写、执行权限。然而这些原则必须通过RBAC各部件的详细配置才能得以体现。

RBAC有许多部件(BUCU)，这使得RBAC的管理多面化。

#### 1.3 RBAC与Group
考虑到多人可以有相同权限，RBAC也借鉴了一些GBAC的概念，引入了Group的概念。Group：用户组，权限分配的单位与载体。权限不考虑分配给特定的用户而给组。组可以包括组(以实现权限的继承)，也可以包含用户，组内用户继承组的权限。

User与Group是多对多的关系。Group可以层次化，以满足不同层级权限控制的要求。


## 参考文献
[RBAC百度百科](https://baike.baidu.com/item/RBAC/1328788?fr=aladdin)
