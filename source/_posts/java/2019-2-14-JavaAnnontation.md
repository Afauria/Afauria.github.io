---
layout: post
title: java注解（更新中）
date: 2019-2-14
description: java注解
categories: Java
tags: 
- Java
---

## 1.1. 注解的分类

按运行机制分：通过@Retention注解进行分类

> - 源码注解：只在源码中存在。RetentionPolicy.SOURCE
> - 编译时注解：在class中依然存在，RetentionPolicy.CLASS。如@Deprecated。
> - 运行时注解：运行阶段起作用，RetentionPolicy.RUNTIME。如@Autowired。

按来源分：

> - JDK自带注解，内置注解：如@Override ，@Deprecated 等
> - 三方注解：如Hibernate，Struts，ButterKnife，ARouter等
> - 自定义注解

>  元注解：注解的注解
>
> 普通注解：用于注解类、变量、方法，参数等