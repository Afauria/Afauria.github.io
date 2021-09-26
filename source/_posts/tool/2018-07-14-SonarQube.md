---
layout: post
title: 静态代码分析平台SonarQube
date: 2018-7-14
categories: 工具
tags: 
- 工具
- 笔记
description: SonarQube使用笔记
keywords: [SonarQube , Lint]
---

## Sonar是什么？

SonarQube(以前叫Sonar)是持续检测代码质量的开源平台
静态代码分析工具、代码质量检测工具
支持不同编程语言

## 系统架构

作为一个代码分析平台，Sonar由以下三个部分组成：

1. 数据库：存放配置信息和分析结果信息；
2. 一个Web服务器：建立工程，在线浏览分析结果，配置分析规则；
3. 客户端、分析端：执行源代码分析；

服务端和客户端有多种搭配方式
sonarqube + sonar-runner
/sonar-scanner
sonarqube + maven
sonarqube + IDE 	如：IntelliJ、android studio、eclipse

sonar的命令行分析端软件有两种分别是Runner和Scanner，官网文档中写的是Scanner，但Runner和它安装、使用都基本一致。

客户端分析代码后将结果显示在服务端（浏览器），也可以存到数据库中，服务端可以部署在本地部署到远程
本地默认端口为localhost:9000

## 配置



```
>在SonarQube平台创建工程，设置ProjectName和ProjectKey

>在本地需要扫描的工程目录下创建sonar-project.properties，内容如下：
>sonar.projectKey=project_key 
>sonar.projectName=project_name 
>sonar.projectVersion=1.0 
>sonar.sources=./ 
>sonar.language=py //需要扫描哪种语言的代码，如python:py，java:java
>sonar.sourceEncoding=UTF-8 
>sonar.host.url=http://your_host:your_port/[your_prefix] 

>执行sonar-scanner -X 命令，结果会上传到SonarQube平台

```