---
layout: post
title: Android依赖配置
date: 2018-08-04
description: 使用gradle添加依赖，以及常用依赖笔记
categories: Android
tags: 
- Android
---

## Gradle依赖配置

### implementation和api

`implementation`：依赖隔离

`api`：依赖传递，相当于原来的`compile`

从3.4版本的gradle开始，compile已经被api与implementation取代

compileOnly：只在编译时引用，只能保证代码能编过，运行的时候会由于找不到类失败

## 常用框架、依赖库配置

### ButterKnife配置和使用

1. base module中添加依赖`api rootProject.ext.dependencies["butterknife"]`
2. library module添加注解处理器`annotationProcessor rootProject.ext.dependencies["butterknife-compiler"]`
3. library module添加butterknife插件：在模块的build.gradle顶部添加`apply plugin: 'com.jakewharton.butterknife'`
4. project module引用插件依赖：在工程的build.gradle-->buildscript-->dependencies中添加`classpath "com.jakewharton:butterknife-gradle-plugin:8.4.0"`
5. `@BindView(R.id.**)`改成`@BindView(R2.id.**)`

注意：

* 缺少第3，4步会报`attribute value must be constant……`问题
* 缺少第2步会报空指针
* 不同butterknife版本和gradle版本配置会有所不同。有时候会出现问题，具体怎么解决的忘了，有空再补

补充：

**APT**(Annotation Processing Tool)即**注解处理器**，是一种处理注解的工具，确切的说它是javac的一个工具，它用来在**编译时**扫描和处理注解。注解处理器以**Java代码**(或者编译过的字节码)作为输入，生成**.java文件**作为输出。
 简单来说就是在编译期，通过注解生成**.java**文件。摘自[【Android】APT](ttps://www.jianshu.com/p/7af58e8e3e18)

### ARouter配置

1. base module中添加依赖api rootProject.ext.dependencies["arouter"]

2. 所有的module中添加

   ```groovy
   javaCompileOptions {
   	annotationProcessorOptions {
   		arguments = [moduleName: project.getName()]
   	}
   }
   ```

3. 路由页面使用@Route注解@Route(path = "/homepage/HomePageActivity")，路径前必须带/
4. 跳转使用ARouter.getInstance().build("/homepage/HomePageActivity").navigation();