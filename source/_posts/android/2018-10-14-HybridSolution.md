---
layout: post
title: 安卓跨平台方案简介
date: 2018-10-14
description: 占坑，有空补
categories: Android
tags: 
- Android
- 进阶
keywords: [Android]
---

## Hybrid App

//todo 跨平台方案对比，选型

Hybrid App（混合模式移动应用）：介于web-app、native-app这两者之间的app，兼具Native App（原生app）良好用户交互体验的优势”和“Web App跨平台开发的优势”。

原因：

* 传统app需要同时开发android和iOS两个app，成本较大。
* 使用H5具有低成本、高效率、跨平台等特性

原理：Hybrid APP底层依赖于Native提供的容器（UIWebview），上层使用Html&Css&JS做业务开发，底层透明化、上层多样化。

优点：共享ui代码，提高开发效率

缺点：性能比不上Native。

场景：有利于前端介入，适合业务快速迭代。

## 方案选择

flutter，weex，reactnative等